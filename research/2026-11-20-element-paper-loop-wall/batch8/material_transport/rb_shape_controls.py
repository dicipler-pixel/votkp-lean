"""Cubic rubidium pocket controls using observed orbit areas and a radial envelope."""

import argparse
import csv
from pathlib import Path

import numpy as np
from scipy.optimize import root_scalar
from scipy.special import eval_legendre

# Shoenberg and Stiles (1964), tabulated in Lee (1969), Table III.
H = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]], dtype=float)
H /= np.linalg.norm(H, axis=1)[:, None]
TARGET = np.array([38.4, -27.9, 56.5]) * 1e-4
Q = (6 * np.pi**2) ** (1 / 3) / 2  # k0*a/2
X = np.sqrt(3) * Q  # k0*Rnn
F = 3 * (np.sin(X) - X * np.cos(X)) / X**3


def harmonic(direction, order):
    return eval_legendre(order, direction).sum(axis=-1)


def control_rows(points):
    z, weights = np.polynomial.legendre.leggauss(points)
    phi = np.arange(2 * points) * np.pi / points
    s = np.sqrt(1 - z * z)
    directions = np.stack(
        [
            s[:, None] * np.cos(phi),
            s[:, None] * np.sin(phi),
            np.broadcast_to(z[:, None], (points, len(phi))),
        ],
        axis=-1,
    )
    w = np.broadcast_to(weights[:, None] / (2 * len(phi)), (points, len(phi)))
    orders = [4, 6, 8, 10]
    vals = np.stack([harmonic(directions, order) for order in orders], axis=-1)
    # For a degree-l spherical harmonic, its mean around the circle normal to
    # h is P_l(0) H_l(h). Areas constrain s^2=(kF/k0)^2 linearly.
    matrix = np.column_stack(
        [eval_legendre(order, 0) * harmonic(H, order) for order in orders]
    )
    assert np.linalg.cond(matrix[:, :3]) < 200
    for c10 in (-0.002, 0, 0.002):

        def coeff(c0):
            return np.r_[
                np.linalg.solve(matrix[:, :3], TARGET - c0 - matrix[:, 3] * c10), c10
            ]

        def radial(c0):
            return np.sqrt(1 + c0 + vals @ coeff(c0))

        def volume_error(c0):
            return np.sum(w * radial(c0) ** 3) - 1

        c0 = root_scalar(volume_error, bracket=(-0.005, 0.005), xtol=1e-14).root
        r = radial(c0)
        assert abs(np.sum(w * r**3) - 1) < 1e-12
        assert np.max(np.abs(c0 + matrix @ coeff(c0) - TARGET)) < 1e-12
        # Independent numerical azimuthal integrals of s^2 in the three planes.
        for direction, target in zip(H, TARGET, strict=True):
            x = np.cross(direction, [0, 0, 1])
            x /= np.linalg.norm(x)
            y = np.cross(direction, x)
            circle = np.cos(phi)[:, None] * x + np.sin(phi)[:, None] * y
            cvals = np.column_stack([harmonic(circle, order) for order in orders])
            assert abs(np.mean(1 + c0 + cvals @ coeff(c0)) - 1 - target) < 1e-12
        # Integral 3 int_0^s r² cos(t*r) dr; Gauss volume integration avoids
        # removable cancellation at t=0. Normalize by the free-sphere volume.
        azimuth = np.einsum("abi,i->ab", directions, H[2]) * X
        nodes, rw = np.polynomial.legendre.leggauss(20)
        unit = (nodes + 1) / 2
        transform = (
            3
            * r**3
            * np.sum(
                rw / 2 * unit**2 * np.cos(azimuth[:, :, None] * r[:, :, None] * unit),
                axis=2,
            )
        )
        amplitude = np.sum(w * transform)
        sphere = 3 * np.sum(
            w * np.sum(rw / 2 * unit**2 * np.cos(azimuth[:, :, None] * unit), axis=2)
        )
        assert abs(sphere - F) < 1e-12
        yield [
            points,
            c10,
            c0,
            *coeff(c0)[:3],
            r.min(),
            r.max(),
            amplitude,
            8 * amplitude**2,
        ]


def envelope(epsilon):
    # Occupied pocket lies between spheres (1±epsilon)k0 and has the sphere's
    # total volume. A cubic-symmetric Fourier weight averages over all 8 bonds,
    # giving K=cos(kxa/2)cos(kya/2)cos(kza/2). At most one factor is negative.
    assert (1 + epsilon) * Q < np.pi / np.sqrt(2)
    lo = np.cos((1 + epsilon) * Q)
    # For a positive product all three cosines are positive. Log(cos(sqrt(u)))
    # is concave on 0≤u<(pi/2)^2, giving the stronger cubic Jensen bound.
    hi = np.cos((1 - epsilon) * Q / np.sqrt(3)) ** 3
    moved = min((1 + epsilon) ** 3 - 1, 1 - (1 - epsilon) ** 3)
    return 8 * max(0, F - moved * (hi - lo)) ** 2


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("output", type=Path)
    args = p.parse_args()
    with args.output.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(
            [
                "polar_order",
                "extra_l10",
                "c0",
                "c4",
                "c6",
                "c8",
                "sampled_min_radius_over_k0",
                "sampled_max_radius_over_k0",
                "nearest_bond_normalized_amplitude",
                "shell_fraction",
            ]
        )
        for points in (24, 48):
            for row in control_rows(points):
                w.writerow([round(x, 12) if isinstance(x, float) else x for x in row])
    print("Sphere shell share:", 8 * F**2)
    print("1% full-direction radial-envelope floor:", envelope(0.01))
    print("2.2% full-direction radial-envelope floor:", envelope(0.022))
    print(
        "Critical envelope for this sufficient lower bound:",
        root_scalar(lambda eps: envelope(eps) - 1 / 3, bracket=(0.022, 0.023)).root,
    )


if __name__ == "__main__":
    main()
