"""Independent real-space readout from the sibling's full Wigner-Seitz weight cubes."""
import csv
import itertools
import sys
from pathlib import Path

import numpy as np


def audit(path):
    with np.load(path, allow_pickle=False) as record:
        weights = record["X"]
        cell = record["cell_A"]
        filling = float(record["nu"])
    mesh = len(weights)
    if weights.shape != (mesh, mesh, mesh):
        raise ValueError(path)
    np.testing.assert_allclose(weights.sum(), filling, atol=2e-9, rtol=0)
    if np.min(weights) < -1e-10:
        raise AssertionError("negative link weight")
    backwards = (-np.arange(mesh)) % mesh
    np.testing.assert_allclose(weights, weights[np.ix_(backwards, backwards, backwards)], rtol=0, atol=1e-10)
    # Wrap fractional supercell coordinates into [-.5,.5). The zero image is
    # at most upper away. Any omitted translation is longer by the smallest
    # singular value bound, in units of one primitive cell.
    upper = np.linalg.norm(cell, axis=1).sum() / 2
    smallest = np.linalg.svd(cell, compute_uv=False).min()
    limit = int(np.ceil(upper / smallest + .5))
    shifts = np.array(list(itertools.product(range(-limit, limit + 1), repeat=3)))
    tensor = np.zeros((3, 3))
    squared = np.zeros_like(weights)
    for coord in np.ndindex(weights.shape):
        wrapped = (np.asarray(coord) / mesh + .5) % 1 - .5
        images = (wrapped + shifts) @ cell * mesh
        distance2 = np.sum(images**2, axis=1)
        squared[coord] = distance2.min()
        shortest = images[np.isclose(distance2, distance2.min(), rtol=1e-12, atol=1e-10)]
        tensor += weights[coord] * (shortest.T @ shortest) / len(shortest)
    tensor /= 2 * filling
    shell_mask = np.isclose(squared, np.min(squared[squared > 0]), atol=1e-8)
    fraction = weights[shell_mask].sum() / (filling - weights[0, 0, 0])
    np.testing.assert_allclose(np.trace(tensor), np.sum(weights * squared) / (2 * filling), atol=1e-11)
    if np.linalg.eigvalsh(tensor).min() < -1e-9:
        raise AssertionError("tensor fails positivity")
    # A primitive reciprocal direction obeys q·R=2πh_i/M. No image
    # convention enters the three direction-resolved phase-leakage readouts.
    covectors = 2 * np.pi * np.linalg.inv(cell).T / mesh
    fractions = np.indices(weights.shape) / mesh
    chord = []
    chord_distances2 = np.zeros_like(weights)
    for i in range(3):
        q2 = covectors[i] @ covectors[i]
        axis_chord2 = 4 * np.sin(np.pi * fractions[i])**2 / q2
        chord_distances2 += axis_chord2
        chord.append(np.sum(weights * axis_chord2) / (2 * filling))
    condition = np.linalg.cond(cell)
    lower = 4 / (np.pi * condition)**2
    upper = condition**2
    if (np.any(chord_distances2 < lower * squared - 1e-9)
            or np.any(chord_distances2 > upper * squared + 1e-9)):
        raise AssertionError('chord / shortest-image comparison failed')
    return (path.stem, int(shell_mask.sum()), fraction, *(tensor[i,j] for i,j in ((0,0),(1,1),(2,2),(0,1),(0,2),(1,2))), np.trace(tensor)/3, *chord)


if __name__ == "__main__":
    directory = Path(__file__).resolve().parent.parent / "localization" / "weights"
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("case","nearest_count","S1","xx_A2","yy_A2","zz_A2","xy_A2","xz_A2","yz_A2","trace_over_3_A2","q1_chord_A2","q2_chord_A2","q3_chord_A2"))
    for path in sorted(directory.glob("*.npz")):
        case, nc, *vals = audit(path)
        writer.writerow((case, nc, *(f"{v:.10f}" for v in vals)))
