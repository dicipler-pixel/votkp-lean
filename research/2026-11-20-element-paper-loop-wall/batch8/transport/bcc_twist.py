"""Dimensionless occupied-projector and twist-curvature controls for a bcc torus."""
import csv
from itertools import product
from math import pi
from pathlib import Path

import numpy as np

SIZES = (8, 16, 32, 64, 96)
SHIFTS = ((0.137, 0.271, 0.413), (0.5, 0.5, 0.5), (0.389, 0.217, 0.079))
STAGGER = (0, 1, 4)
PHI_STEP = 0.01


def measure(size, shift, delta):
    q = [(2 * pi * (np.arange(size) + s) / size - pi) / 2 for s in shift]
    x, y, z = np.ix_(*q)
    yz = -8 * np.cos(y) * np.cos(z)
    g = yz * np.cos(x)
    gprime = -yz * np.sin(x) / 2
    energy = np.hypot(delta, g)
    # K is d²E/dq_x² per site, summing spin degeneracy. The doubled cell
    # has two sites, so the factors for spin and sites cancel.
    curvature = (g*g/(4*energy) - delta**2*gprime**2/energy**3).mean()
    # Independent small-twist finite difference on the same occupied branch.
    # No grid point crosses the Fermi plane for either sign of PHI_STEP.
    assert PHI_STEP < 2*pi*min(shift[0], 1-shift[0])
    dq = PHI_STEP / size
    upper = -np.hypot(delta, yz*np.cos(x + dq/2))
    lower = -np.hypot(delta, yz*np.cos(x - dq/2))
    k_fd = ((upper + energy) + (lower + energy)).mean()/dq**2
    assert abs(k_fd - curvature) < 5e-5

    occ = ((1 - delta/energy)/2).mean()
    budget = 2 * occ * (1-occ)
    p_ab = -g/(2*energy)
    # Sign-reversed bonds are conjugate in this real gauge.
    weights = []
    for sy, sz in product((-1, 1), repeat=2):
        phase = np.exp(1j*x) * np.exp(1j*sy*y) * np.exp(1j*sz*z)
        weights.append(2 * abs((p_ab * phase).mean())**2)
    shell_share = 2 * sum(weights) / budget
    assert shell_share > 1/3 and shell_share <= 1 + 1e-12
    return (size, '/'.join(map(str, shift)), delta, curvature, k_fd, abs(k_fd-curvature),
            sum(weights)/4, budget, shell_share)


def main():
    rows = [measure(n, offset, d) for n in SIZES for offset in SHIFTS for d in STAGGER]
    for d in STAGGER:
        final = [row for row in rows if row[0] == max(SIZES) and row[2] == d]
        limit = 16/pi**3 if d == 0 else 0
        assert max(abs(row[3] - limit) for row in final) < 8e-5
    with Path(__file__).with_suffix('.csv').open('w', newline='') as out:
        writer = csv.writer(out, lineterminator='\n')
        writer.writerow(('L','fractional_mesh_offsets','delta_over_t','twist_curvature_over_t',
                         'finite_difference_over_t','abs_derivative_difference',
                         'mean_nearest_X','B','nearest_shell_fraction'))
        for row in rows:
            writer.writerow([*row[:3], *(format(x,'.12g') for x in row[3:])])


if __name__ == '__main__':
    main()
