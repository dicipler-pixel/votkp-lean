"""Preserve three measured rubidium orbit sections but change the scalar shell call."""

import argparse
import csv
from itertools import permutations, product
from pathlib import Path

import numpy as np
from scipy.optimize import brentq
from scipy.special import expit

from rb_shape_controls import H, Q, TARGET, control_rows, harmonic


def solve(points, c0, coeff):
    z, weights = np.polynomial.legendre.leggauss(points)
    phi = np.arange(2 * points) * np.pi / points
    s = np.sqrt(1 - z * z)
    angular = np.stack(
        [
            s[:, None] * np.cos(phi),
            s[:, None] * np.sin(phi),
            np.broadcast_to(z[:, None], (points, len(phi))),
        ],
        axis=-1,
    )
    weights = np.broadcast_to(weights[:, None] / (4 * points), angular.shape[:-1])
    normals = set()
    for direction in [(1, 0, 0), (1, 1, 0), (1, 1, 1)]:
        for perm in permutations(direction):
            for signs in product((-1, 1), repeat=3):
                vector = tuple(x * y for x, y in zip(perm, signs, strict=True))
                if tuple(-x for x in vector) not in normals:
                    normals.add(vector)

    def shape_constants(angles):
        distance = np.ones(angles.shape[:-1])
        for normal in normals:
            distance = np.minimum(
                distance, abs(angles @ normal) / np.linalg.norm(normal)
            )
        blend = 1 - np.exp(-((np.maximum(0, distance - 0.035) / 0.025) ** 2))
        sorted_abs = np.sort(abs(angles), axis=-1)
        zone_boundary = np.pi / Q / (sorted_abs[..., 1] + sorted_abs[..., 2])
        base = np.sqrt(
            1
            + c0
            + sum(
                c * harmonic(angles, order)
                for c, order in zip(coeff, [4, 6, 8], strict=True)
            )
        )
        assert np.all((base > 0.2) & (base < zone_boundary))
        return blend, sorted_abs[..., 2], 0.995 * zone_boundary, base

    def radii(constants, level):
        blend, score, cap, base = constants
        mod = 0.2**3 + (cap**3 - 0.2**3) * expit((score - level) / 0.025)
        return np.cbrt((1 - blend) * base**3 + blend * mod)

    constants = shape_constants(angular)
    contour = brentq(
        lambda level: np.sum(weights * radii(constants, level) ** 3) - 1,
        0,
        1.4,
        xtol=1e-13,
    )
    radius = radii(constants, contour)
    assert abs(np.sum(weights * radius**3) - 1) < 1e-12
    for direction, observed in zip(H, TARGET, strict=True):
        a = np.cross(direction, [0, 0, 1])
        a /= np.linalg.norm(a)
        b = np.cross(direction, a)
        plane = np.cos(phi)[:, None] * a + np.sin(phi)[:, None] * b
        check = shape_constants(plane)
        assert np.all(check[0] == 0)
        assert abs(np.mean(radii(check, contour) ** 2) - 1 - observed) < 1e-12

    # Exact radial cosine integral, with its even Taylor expansion near zero.
    arg = Q * np.sum(angular, axis=-1) * radius
    av = np.empty_like(arg)
    small = abs(arg) < 0.05
    x = arg[small] ** 2
    av[small] = 1 + x * (-3 / 10 + x * (1 / 56 - x / 2160))
    t = arg[~small]
    av[~small] = 3 * ((t**2 - 2) * np.sin(t) + 2 * t * np.cos(t)) / t**3
    amp = np.sum(weights * radius**3 * av)
    return [points, len(phi), contour, radius.min(), radius.max(), amp, 8 * amp**2]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("output", type=Path)
    args = p.parse_args()
    # Base has the same measured central areas and the one-electron volume.
    base = next(row for row in control_rows(48) if row[1] == 0)
    with args.output.open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(
            [
                "polar_order",
                "azimuth_order",
                "volume_calibration",
                "sampled_min_radius",
                "sampled_max_radius",
                "normalized_amplitude",
                "shell_fraction",
            ]
        )
        for points in [64, 128, 256, 384]:
            row = solve(points, base[2], base[3:6])
            writer.writerow([round(v, 11) if isinstance(v, float) else v for v in row])
    assert base[-1] > 1 / 3 and row[-1] < 1 / 3


if __name__ == "__main__":
    main()
