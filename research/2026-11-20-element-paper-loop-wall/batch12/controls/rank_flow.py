"""Wavefunction-independent rank-crossing lower bounds from archived rubidium band energies."""
import csv
import gzip
import json
from pathlib import Path
import sys

import numpy as np

TRANSPORT = Path(__file__).resolve().parents[2] / "batch8" / "material_transport"
sys.path.insert(0, str(TRANSPORT))
from rb_fermi_surface import band_grid

TIE_WIDTH_EV = 1e-7
# Shortest reciprocal translation parallel to these physical cubic directions.
CUBIC_STEPS = ((1, 1, 0), (2, 0, 0), (2, 2, 2))


def interval_counts(energy, shift):
    """All Bloch-diagonal half fillings including arbitrary choices in the possible tie shell."""
    target = energy.size // 2
    ranked = np.partition(energy.ravel(), (target - 1, target))
    midpoint = (ranked[target - 1] + ranked[target]) / 2
    definitely_occ = energy < midpoint - TIE_WIDTH_EV
    definitely_empty = energy > midpoint + TIE_WIDTH_EV
    uncertain = energy.size - definitely_occ.sum() - definitely_empty.sum()
    if not (definitely_occ.sum() <= target <= energy.size - definitely_empty.sum()):
        raise AssertionError("rank enclosure failed")
    next_empty = np.roll(definitely_empty, -shift, axis=(0,1,2))
    next_occ = np.roll(definitely_occ, -shift, axis=(0,1,2))
    lower = np.sum(definitely_occ & next_empty)
    upper = np.sum(~definitely_empty & ~next_occ)
    if not 0 <= lower <= upper <= energy.size:
        raise AssertionError("rank count")
    return midpoint, int(uncertain), int(lower), int(upper)


def main():
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("geometry","QE_mesh","hkl","q_invA","half_filled_count","mu_mid_eV","ambiguous_states",
                     "forced_min","rank_crossing_max","L_lower_A2","rank_term_upper_A2","qL_lower_A","qLrank_upper_A","sphere_qL_A"))
    for geometry, file in (("297K", "Rb_band_inputs.json.gz"), ("5K","Rb_cold_band_inputs.json.gz")):
        data = json.loads(gzip.decompress((TRANSPORT / file).read_bytes()))
        for key in sorted(data, key=int):
            record = data[key]
            n = record["n"]
            cube, reciprocal, volume, _ = band_grid(record)
            band = cube[...,4]
            filling = band.size // 2
            kf = (3 * np.pi**2 / volume)**(1/3)  # one electron/primitive cell including two spins
            for hkl in CUBIC_STEPS:
                indices = np.asarray(hkl) @ np.linalg.inv(record["reciprocal"])
                shift = np.rint(indices).astype(int)
                np.testing.assert_allclose(shift, indices, rtol=0, atol=1e-9)
                q = np.linalg.norm(shift @ reciprocal) / n
                mu, uncertain, forced, possible = interval_counts(band, shift)
                if not (np.max(cube[...,3]) < mu - TIE_WIDTH_EV and np.min(cube[...,5]) > mu + TIE_WIDTH_EV):
                    raise AssertionError("semi-core or higher band crosses the outer-band cutoff")
                sphere = 3/(4*kf)-q**2/(16*kf**3)
                if not q < 2*kf:
                    raise AssertionError("sphere lens formula domain")
                lower = forced / (filling*q**2)
                rank_upper = possible / (filling*q**2)
                writer.writerow((geometry,n,"".join(map(str,hkl)),f"{q:.11f}",filling,f"{mu:.8f}",uncertain,
                                 forced,possible,f"{lower:.9f}",f"{rank_upper:.9f}",f"{q*lower:.9f}",
                                 f"{q*rank_upper:.9f}",f"{sphere:.9f}"))


if __name__ == "__main__":
    main()
