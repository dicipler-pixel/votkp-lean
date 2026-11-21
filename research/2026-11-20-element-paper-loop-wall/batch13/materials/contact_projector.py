"""Spinless single-orbital, nearest-contact Fddd/oF8 diagnostic (half filling)."""
import csv
from itertools import product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OFFSET = (0.137, 0.271, 0.419)  # avoid hitting a zero of the gap at finite N


def moments(grid, mass):
    waves = [np.exp(2j*np.pi*(np.arange(grid)+s)/grid) for s in OFFSET]
    amplitude = diagonal = off_diagonal = square = fourth = 0.0
    min_gap = float("inf")
    # Fractional reciprocal coordinates of the primitive translations. The
    # Euclidean lengths of these three translations enter reciprocal axes,
    # then cancel exactly from the normalized Brillouin-zone integral.
    for x in waves[0]:
        f = 1+x+waves[1][:, None]+waves[2][None, :]
        norm2 = np.abs(f)**2
        energy = np.sqrt(mass**2+norm2)
        min_gap = min(min_gap, 2*energy.min())
        diagonal += (mass/energy).sum()
        amplitude += np.sqrt(norm2).sum()
        off_diagonal += (norm2/energy).sum()
        square += norm2.sum()
        fourth += (norm2**2).sum()
    ntot = grid**3
    mean = amplitude/ntot
    density = (1-diagonal/ntot)/2
    budget = density*(1-density)
    # This averages the equivalent four bonds. In the continuum they are equal.
    p = off_diagonal/(8*ntot)
    return [mean,square/ntot,fourth/ntot,density,budget,p,p*p,budget/12,4*p*p/budget,min_gap]


def main():
    with (HERE/"contact_projector.csv").open("w",newline="") as f:
        out=csv.writer(f,lineterminator="\n")
        out.writerow(["grid","staggered_mass_over_t","mean_abs_f","mean_abs_f2","mean_abs_f4",
                      "site_A_occupancy","budget_A","nearest_abs_projector","nearest_X",
                      "cutoff_budget_over_12","nearest_shell_fraction","sampled_band_gap_over_t"])
        for mass, grid in product([0,1], [24,48,96,192]):
            row=moments(grid,mass)
            if not (abs(row[1]-4)<1e-10 and abs(row[2]-28)<1e-10 and row[6]>row[7]):
                raise ValueError("moments or cutoff control failed")
            if mass==0 and not 1/28<=row[6]<=1/16:
                raise ValueError("gapless half-filled result escaped exact moment bounds")
            out.writerow([grid,mass]+[f"{x:.10f}" for x in row])
    print("Passed independent second, fourth moment, interval and cutoff checks for both masses.")


if __name__=="__main__":
    main()
