"""Onsager central areas of the low-temperature rubidium Fermi pocket."""

import argparse
import csv
import gzip
import json
from pathlib import Path

import numpy as np
from scipy.constants import elementary_charge, hbar
from scipy.ndimage import map_coordinates, spline_filter
from scipy.optimize import brentq

from rb_fermi_surface import band_grid


def compute(data, polar_count=32, circle_count=256):
    bands, recip, volume, chemical_potential = band_grid(data)
    sizes = len(bands)
    # One electron per primitive bcc cell; both spins included.
    radius = (3 * np.pi**2 / volume) ** (1 / 3)
    area_sphere = np.pi * radius**2
    spline = spline_filter(bands[:, :, :, 4], mode="grid-wrap")
    to_grid = np.linalg.inv(recip) * sizes

    def energy(k):
        coords = (k @ to_grid).T
        return map_coordinates(
            spline, coords, order=3, mode="grid-wrap", prefilter=False
        )

    def radii(mu, directions, origin=None):
        center = 0 if origin is None else origin

        def evaluate(r):
            return energy(center + directions * np.asarray(r)[..., None])

        # Stay on the first crossing of the bounded Gamma pocket. Explicitly
        # check monotonicity throughout the local radial interval before Newton.
        probe = np.array([evaluate(radius * x) for x in (0.90, 0.95, 1.0, 1.05, 1.1)])
        assert np.all(np.diff(probe, axis=0) > 0)
        assert np.max(probe[0]) < mu < np.min(probe[-1])
        r = np.broadcast_to(radius, len(directions)).copy()
        dr = radius * 1e-4
        for _ in range(6):
            residual = evaluate(r) - mu
            slope = (evaluate(r + dr) - evaluate(r - dr)) / (2 * dr)
            assert slope.min() > 0 and np.max(abs(r / radius - 1)) < 0.10
            r -= residual / slope
        assert np.max(abs(evaluate(r) - mu)) < 1e-10
        return r

    # Angular average of r(theta,phi)^3 fixes the occupied pocket volume
    # without a free-sphere assumption for its angular dependence.
    z, wt = np.polynomial.legendre.leggauss(polar_count)
    phis = np.arange(2 * polar_count) * np.pi / polar_count
    s = np.sqrt(1 - z**2)
    coords = np.stack(
        [
            s[:, None] * np.cos(phis),
            s[:, None] * np.sin(phis),
            np.broadcast_to(z[:, None], (polar_count, len(phis))),
        ],
        axis=-1,
    )
    rays = coords.reshape(-1, 3)

    def unit_volume(mu):
        radii_cubed = (radii(mu, rays) / radius) ** 3
        return np.dot(wt, radii_cubed.reshape(polar_count, -1).mean(axis=1)) / 2 - 1

    mu = brentq(
        unit_volume, chemical_potential - 0.12, chemical_potential + 0.12, xtol=1e-12
    )
    phis = np.arange(circle_count) * 2 * np.pi / circle_count
    rows = []
    for label, normal in [("100", (1, 0, 0)), ("110", (1, 1, 0)), ("111", (1, 1, 1))]:
        direction = np.array(normal, dtype=float)
        direction /= np.linalg.norm(direction)
        u = np.cross(direction, [0, 0, 1])
        u /= np.linalg.norm(u)
        v = np.cross(direction, u)
        rays_circle = np.cos(phis)[:, None] * u + np.sin(phis)[:, None] * v

        def area(offset):
            return np.pi * np.mean(
                radii(mu, rays_circle, offset * radius * direction) ** 2
            )

        center = area(0)
        upper, lower = area(0.025), area(-0.025)
        assert center > max(upper, lower) and abs(upper - lower) < 1e-9
        normalized = center / area_sphere
        # Reciprocal Å² to reciprocal m², then Onsager frequency in tesla.
        freq = hbar * center * 1e20 / (2 * np.pi * elementary_charge)
        rows.append(
            [
                sizes,
                polar_count,
                circle_count,
                label,
                mu,
                radius,
                center,
                normalized,
                1e4 * (normalized - 1),
                freq / 1000,
                (center - upper) / center,
            ]
        )
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    records = json.loads(gzip.decompress(args.bundle.read_bytes()))
    with args.output.open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(
            [
                "QE_grid",
                "polar_quadrature",
                "orbit_angles",
                "field_direction",
                "mu_eV",
                "free_sphere_kF_Ainv",
                "central_area_Ainv2",
                "area_over_sphere",
                "area_distortion_parts_per_10000",
                "onsager_frequency_kT",
                "fractional_area_loss_at_offset_0p025_kF",
            ]
        )
        for data in records.values():
            if data["n"] < 24:
                continue
            for n, m in [(16, 128), (32, 256)]:
                rows = compute(data, n, m)
                for row in rows:
                    writer.writerow(
                        [round(x, 10) if isinstance(x, float) else x for x in row]
                    )


if __name__ == "__main__":
    main()
