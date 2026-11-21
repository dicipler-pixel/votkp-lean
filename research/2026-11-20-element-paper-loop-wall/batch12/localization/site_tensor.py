"""Outer-band Wigner–Seitz center-position second moments from finite QE meshes."""
import argparse
import csv
from itertools import product
from pathlib import Path
import sys

import numpy as np

BATCH8 = Path(__file__).resolve().parents[2] / "batch8"
sys.path.insert(0, str(BATCH8 / "nc_control"))
sys.path.insert(0, str(BATCH8 / "ws_control"))
import nc_projector
import pseudo_projector
from weight_io import write_weights

# Same lattice conversion as the Angstrom coordinates in the QE input (CODATA 2018).
BOHR_A = 0.529177210903
COMPONENTS = ("xx", "yy", "zz", "xy", "xz", "yz")
AXES = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def site_weights(waves, owner, indices, mesh):
    """X_D includes both spins. Fourier-sum the occupied–occupied cell overlaps."""
    shape = (mesh,) * 3
    histogram = np.zeros(mesh**3)
    cross_histogram = np.zeros(mesh**3)
    wavevectors = indices[owner]
    # A pair in distinct tiles contributes conjugate overlaps at opposite
    # translations. Evaluate it only once to reduce the large Kr contractions.
    for first in range(0, len(waves), 64):
        last = min(first + 64, len(waves))
        bra = waves[first:last].conj()
        for start,stop,destination in ((first,last,histogram),
                                       (last,len(waves),cross_histogram)):
            if start==stop:
                continue
            overlaps = bra @ waves[start:stop].T
            delta = (wavevectors[first:last,None] - wavevectors[None,start:stop]) % mesh
            bins = np.ravel_multi_index(delta.reshape(-1,3).T,shape)
            destination += np.bincount(bins,weights=(abs(overlaps)**2).ravel(),
                                       minlength=mesh**3)
    reverse = (-np.arange(mesh)) % mesh
    histogram += cross_histogram + cross_histogram.reshape(shape)[np.ix_(reverse,reverse,reverse)].ravel()
    weights = 2 * np.fft.ifftn(histogram.reshape(shape)) / mesh**3
    assert np.max(abs(weights.imag)) < 1e-10
    return weights.real


def image_dyads(mesh, cell):
    """Average dyads over ALL equal shortest images; bound the enumeration."""
    # Start with fractional coordinates in [-1/2,1/2]. The smallest singular
    # value bounds Cartesian length from below for every omitted translation.
    offsets = np.indices((mesh,) * 3).reshape(3, -1).T
    centered = (offsets + mesh // 2) % mesh - mesh // 2
    reference = centered @ cell
    largest_upper_bound = np.linalg.norm(reference, axis=1).max()
    min_stretch = np.linalg.svd(cell, compute_uv=False).min()
    radius = int(np.ceil(largest_upper_bound / (mesh * min_stretch) + 0.5))
    translations = np.array(list(product(range(-radius, radius + 1), repeat=3)))
    vectors = (centered[:, None] + mesh * translations[None]) @ cell
    norms = np.sum(vectors**2, axis=2)
    least = norms.min(axis=1)
    closest = np.isclose(norms, least[:, None], atol=1e-9, rtol=1e-12)
    dyads = np.einsum("nt,nti,ntj->nij", closest / closest.sum(axis=1)[:, None],
                      vectors, vectors)
    assert np.allclose(dyads.trace(axis1=1, axis2=2), least, rtol=1e-12, atol=1e-10)
    return least, dyads, closest.sum(axis=1)


def calculate(save, symbol, mesh, grid, family, weights_path, disk=False):
    if disk or (symbol=="Kr" and mesh>=10):
        from disk_blocks import disk_weights
        weights,count,cell=disk_weights(save,symbol,mesh,grid,family)
    else:
        projector = nc_projector if family == "NC" else pseudo_projector
        waves, owner, indices, cell, _ = projector.blocks(
            save, symbol, mesh, grid, np.array([.213, .367, .479]), False)
        count = 2 * len(waves) / mesh**3
        weights = site_weights(waves, owner, indices, mesh)
    assert weights.min() > -1e-9 and abs(weights.sum() - count) < 1e-9
    assert np.max(abs(weights - weights[np.ix_(*[(-np.arange(mesh)) % mesh]*3)])) < 1e-10
    cell = cell * BOHR_A
    squared, dyads, multiplicity = image_dyads(mesh, cell)
    nearest = np.isclose(squared, squared[squared > 0].min())
    assert nearest.sum() == {"Rb": 8, "Kr": 12}[symbol]
    budget = count - weights.flat[0]
    fraction = weights.ravel()[nearest].sum() / budget
    tensor = np.einsum("i,ijk->jk", weights.ravel(), dyads) / (2 * count)
    assert np.linalg.eigvalsh(tensor).min() > 0
    if weights_path:
        # Cell rows are primitive lattice vectors, in Angstrom; indices I,J,K
        # are translations modulo mesh. Unrounded raw weights allow independent checks.
        write_weights(weights_path, weights, cell, count)
    row = dict(symbol=symbol, family=family, mesh=mesh, grid=grid, electrons_per_cell=count,
               offsite_B=budget, nearest_shell_fraction=fraction, trace_A2=np.trace(tensor),
               trace_over_3_A2=np.trace(tensor)/3, tied_image_classes=(multiplicity>1).sum())
    row.update({name + "_A2":tensor[i,j] for name,(i,j) in zip(COMPONENTS,AXES)})
    return row


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("save", type=Path)
    parser.add_argument("symbol", choices=["Kr","Rb"])
    parser.add_argument("mesh", type=int)
    parser.add_argument("grid", type=int)
    parser.add_argument("--family", choices=["NC","PAW-smooth"], default="NC")
    parser.add_argument("--weights", type=Path, help="save complete finite site-weight array")
    parser.add_argument("--disk",action="store_true",help="store orbital tiles beside the QE run; automatic for Kr mesh ≥ 10")
    args = parser.parse_args()
    result = calculate(args.save, args.symbol, args.mesh, args.grid, args.family, args.weights, args.disk)
    writer = csv.DictWriter(sys.stdout, result.keys())
    writer.writeheader()
    writer.writerow(result)
