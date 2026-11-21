"""Leading occupied-rank escape from the piecewise-linear energy surface at half filling."""
import csv
import gzip
from itertools import permutations
import json
import sys

import numpy as np
from scipy.optimize import brentq

from rank_flow import TRANSPORT, band_grid
from rb_tetrahedra import slice_volume

DIRECTIONS = np.array(((1,0,0),(1,1,0),(1,1,1)))
UNIT = DIRECTIONS / np.linalg.norm(DIRECTIONS, axis=1)[:,None]
DIAGONALS = ((1,1,1),(1,1,-1),(1,-1,1),(-1,1,1))


def coefficients(band, reciprocal, signs):
    n = len(band)
    gradient_list, corner_list = [], []
    for order in permutations(range(3)):
        energy = band
        corners = [band]
        differences = [None] * 3
        for axis in order:
            next_energy = np.roll(energy, -signs[axis], axis=axis)
            differences[axis] = (next_energy - energy) * signs[axis] * n
            corners.append(next_energy)
            energy = next_energy
        cart_grad = np.linalg.solve(reciprocal, np.stack(differences).reshape(3,-1))
        gradient_list.append(cart_grad.T)
        corner_list.append(np.sort(np.stack(corners,axis=-1).reshape(-1,4),axis=1))
    all_corners = np.vstack(corner_list)
    gradients = np.vstack(gradient_list)
    lower, upper = band.min(), band.max()
    level = brentq(lambda e: slice_volume(all_corners,e)[0].mean() - .5, lower, upper)
    occupancy, density = slice_volume(all_corners,level)
    projected = (gradients @ UNIT.T) * density[:,None]
    # One outgoing face per line segment through the occupied pocket.
    # The inward and outward total fluxes agree by periodicity.
    outgoing = np.maximum(projected, 0).mean(axis=0)
    incoming = -np.minimum(projected, 0).mean(axis=0)
    np.testing.assert_allclose(outgoing, incoming, rtol=2e-9, atol=1e-12)
    np.testing.assert_allclose(occupancy.mean(), .5, rtol=1e-10, atol=1e-12)
    return level, outgoing / occupancy.mean()


def main():
    mesh = 10
    coord = np.indices((mesh,)*3)[0] / mesh
    slab = -np.cos(2*np.pi*coord)
    for signs in DIAGONALS:
        _, slope = coefficients(slab, np.eye(3), signs)
        np.testing.assert_allclose(slope, 2*np.abs(UNIT[:,0]), rtol=1e-9)
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("geometry","QE_mesh","diagonal","hkl","half_filled_mu_eV","qLrank_limit_A",
                     "sphere_limit_A","deHaas_area_lower_central_A","deHaas_area_lower_low_A","deHaas_area_lower_high_A"))
    for name, source, meshes in (("297K","Rb_band_inputs.json.gz",(24,32,40,48)),
                                  ("5K","Rb_cold_band_inputs.json.gz",(24,32,40))):
        records = json.loads(gzip.decompress((TRANSPORT/source).read_bytes()))
        for n in meshes:
            cube, reciprocal, volume, _ = band_grid(records[str(n)])
            kf = (3*np.pi**2/volume)**(1/3)
            sphere = 3/(4*kf)
            # Shoenberg and Stiles (1964), as reported in Lee (1969) Table III:
            # 10^4 times the excess area divided by A0 in [100], [110], [111].
            excess = np.array((38.4,-27.9,56.5))
            uncertainty = 2.2
            for signs in DIAGONALS:
                mu, slope = coefficients(cube[...,4], reciprocal, signs)
                for idx, val in enumerate(slope):
                    conditional_bounds = []
                    if name == "5K":
                        conditional_bounds = [f"{sphere*(1+d/10000):.9f}" for d in
                                              (excess[idx],excess[idx]-uncertainty,excess[idx]+uncertainty)]
                    else:
                        conditional_bounds = ["","",""]
                    writer.writerow((name,n,"".join("+" if s>0 else "-" for s in signs),
                                     "".join(map(str,DIRECTIONS[idx])),f"{mu:.9f}",f"{val:.9f}",
                                     f"{sphere:.9f}",*conditional_bounds))


if __name__ == "__main__":
    main()
