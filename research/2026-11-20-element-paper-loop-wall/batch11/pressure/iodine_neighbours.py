"""Reconstruct commensurate iodine first-neighbour shells from Bykova et al. Table 1."""

import csv
from itertools import product
from pathlib import Path

import gemmi
import numpy as np

# Pressure, space-group setting, conventional orthorhombic axes in Å,
# fractional iodine y,z coordinates (both x=0), refined volume, calculated density.
CELLS = [
    (9.90, "Cmce", [6.163, 4.1435, 9.2864], [(0.18376, 0.62197)], 237.15, 7.109),
    (15.0, "Cmce", [5.978, 4.0396, 9.1487], [(0.19087, 0.62278)], 220.94, 7.630),
    (
        17.0,
        "Cmc21",
        [5.908, 4.0055, 9.0992],
        [(0.4299, 0.26446), (0.0387, 0.51173)],
        215.3,
        7.830,
    ),
    (
        19.0,
        "Cmc21",
        [5.829, 3.9773, 9.0739],
        [(0.4306, 0.26390), (0.0291, 0.51229)],
        210.4,
        8.014,
    ),
    (32.0, "Immm", [2.9077, 3.0333, 5.226], [(0, 0)], 46.10, 9.143),
]


def expand(group, sites):
    atoms = {}
    for i, (y, z) in enumerate(sites, start=1):
        for op in gemmi.find_spacegroup_by_name(group).operations():
            coord = tuple(np.round(np.mod(op.apply_to_xyz([0, y, z]), 1), 9) % 1)
            assert coord not in atoms or atoms[coord] == i
            atoms[coord] = i
    return atoms


def neighbours(cell, atoms, site, extent):
    candidates = []
    for pos, other in atoms.items():
        for translation in product(range(-extent, extent + 1), repeat=3):
            vector = (np.array(pos) + translation - site) * cell
            d = np.linalg.norm(vector)
            if d > 1e-5:
                candidates.append((round(d, 7), other))
    return sorted(candidates)[:12]


def main():
    with (
        Path(__file__)
        .with_name("I_commensurate_neighbours.csv")
        .open("w", newline="") as f
    ):
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(
            [
                "p_GPa",
                "space_group",
                "conventional_atoms",
                "unique_central_site",
                "neighbor_site",
                "rank",
                "I_to_I_distance_A",
            ]
        )
        for pressure, group, cell, sites, volume, density in CELLS:
            atoms = expand(group, sites)
            assert len(atoms) == (2 if group == "Immm" else 8)
            assert abs(np.prod(cell) - volume) < 0.06
            check_density = len(atoms) * 126.90447 / 0.602214076 / volume
            assert abs(check_density / density - 1) < 0.001
            for i, (y, z) in enumerate(sites, start=1):
                central = np.array([0, y, z])
                first = neighbours(cell, atoms, central, 1)
                assert first == neighbours(cell, atoms, central, 2)
                for rank, (d, other) in enumerate(first, start=1):
                    writer.writerow([pressure, group, len(atoms), i, other, rank, d])
                print(
                    pressure,
                    group,
                    i,
                    first[:4],
                    "d2/d1",
                    round(first[1][0] / first[0][0], 5),
                )


if __name__ == "__main__":
    main()
