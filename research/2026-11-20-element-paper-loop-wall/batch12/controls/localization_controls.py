"""Finite periodic controls for the per-electron projector moments. Length unit a=1."""
import csv
import math
import sys

import numpy as np


def near(left, right, tol=2e-11):
    if not np.allclose(left, right, rtol=tol, atol=tol):
        raise AssertionError((left, right))


def moments(weights, filling):
    count = len(weights)
    sites = np.arange(count)
    q = 2 * np.pi / count
    distance = np.minimum(sites, count - sites)
    chord = 2 * np.sin(q * sites / 2) / q
    budget = np.sum(weights[1:])
    nearest = weights[1] + weights[-1]
    return (nearest / budget, weights @ distance**2 / (2 * filling),
            weights @ chord**2 / (2 * filling))


def metal_weights(count):
    """One spin, N=4m+2, occupied k indices -m..m for hopping -1."""
    modes = np.fft.fftfreq(count) * count
    occupation = np.abs(modes) < count / 4
    near(occupation.sum(), count // 2)
    weights = abs(np.fft.ifft(occupation))**2
    ell = np.arange(1, count)
    expected = (np.sin(np.pi * ell / 2) / (count * np.sin(np.pi * ell / count)))**2
    near(weights[1:], expected)
    return weights


def dimer_projector(count, intercell):
    bonds = np.zeros((count * 2, count))
    cells = np.arange(count)
    bonds[2 * cells, cells] = 1 / np.sqrt(2)
    partners = (cells + int(intercell)) % count
    bonds[2 * partners + 1, cells] = 1 / np.sqrt(2)
    return bonds @ bonds.T


def explicit_q(projector, positions, q):
    """Direct occupied-to-empty phase leakage per electron and q squared."""
    phase_times_p = np.exp(1j * q * positions)[:, None] * projector
    leakage = phase_times_p - projector @ phase_times_p
    return np.vdot(leakage, leakage).real / (np.trace(projector).real * q**2)


def finite_controls(count):
    q = 2 * np.pi / count
    cell_centres = np.repeat(np.arange(count), 2)
    rho = 0.37
    true_positions = cell_centres + np.tile([-rho, rho], count)
    for intercell in (False, True):
        projector = dimer_projector(count, intercell)
        near(projector @ projector, projector)
        centred = explicit_q(projector, cell_centres, q)
        full = explicit_q(projector, true_positions, q)
        separation = 2 * rho + int(intercell)
        near(full, (np.sin(q * separation / 2) / q)**2)
        near(centred, (np.sin(q * int(intercell) / 2) / q)**2)
        difference = abs(math.sqrt(full) - math.sqrt(centred))
        if difference > rho + 1e-12:
            raise AssertionError((difference, rho))
        if intercell:
            blocks = projector[:2, :].reshape(2, count, 2)
            weights = np.sum(abs(blocks)**2, axis=(0, 2))
            near(weights[0], .5)
            near(weights[[1, -1]], .25)
            near(moments(weights, 1), (1, .25, centred))
        else:
            near(centred, 0)
            if not full > 0:
                raise AssertionError("Intra-cell control lost its physical spread")
    # Independent check of the metal's momentum-space leakage on the full ring.
    modes = np.fft.fftfreq(count) * count
    sites = np.arange(count)
    occupied = np.exp(1j * q * np.outer(sites, modes[np.abs(modes) < count / 4])) / np.sqrt(count)
    projector = occupied @ occupied.conj().T
    near(explicit_q(projector, sites, q), count / (2 * np.pi**2))


def main():
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("model", "N", "nu", "S1", "lambda_minimum_a2", "lambda_chord_a2"))
    for count in (6, 10, 18, 34, 66, 130, 258, 514, 1026, 2050):
        q = 2 * np.pi / count
        metal = moments(metal_weights(count), .5)
        near(metal[0], 8 / (count * np.sin(np.pi / count))**2)
        near(metal[2], count / (2 * np.pi**2))
        if count == 2050:
            near(metal[1] / count, np.log(2) / np.pi**2, 2e-7)
        dimer = np.zeros(count)
        dimer[[0, 1, -1]] = [.5, .25, .25]
        insulator = moments(dimer, 1)
        near(insulator, (1, .25, (np.sin(q / 2) / q)**2))
        if count < 100:
            finite_controls(count)
        for name, filling, values in (("half_filled_chain", .5, metal), ("filled_dimer_band", 1, insulator)):
            writer.writerow((name, count, filling, *(f"{value:.10f}" for value in values)))


if __name__ == "__main__":
    main()
