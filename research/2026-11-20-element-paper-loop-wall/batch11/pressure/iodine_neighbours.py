"""Read all five commensurate iodine cells in Bykova et al. Table 1, then expand them."""

import argparse
import csv
import hashlib
from itertools import product
from pathlib import Path
import re
import subprocess
from urllib.request import urlopen

import gemmi
import numpy as np

URL = "https://link.aps.org/accepted/10.1103/PhysRevB.108.024104"
DIGEST = "630a3b8bb229db6bf93b1771404d8e460c8b5dc940aa5f31b78eb6bad565e051"


def number(s):
    val, unc = re.fullmatch(r"(\d+(?:\.\d+)?)(?:\((\d+)\))?", s).groups()
    places = len(val.partition(".")[2])
    return float(val), int(unc or 0) * 10 ** (-places)


def extract(pdf):
    assert hashlib.sha256(pdf).hexdigest() == DIGEST
    text = subprocess.run(
        ["pdftotext", "-layout", "-", "-"], input=pdf, capture_output=True, check=True
    ).stdout.decode()

    def row(name):
        matches = [
            line.strip()[len(name) :].split()
            for line in text.splitlines()
            if line.strip().startswith(name + " ")
        ]
        assert len(matches) == 1
        return matches[0]

    def nums(name):
        return [number(s) for s in row(name)]

    xyz = [nums(k + " (Å)") for k in "abc"]
    names = row("Space group")
    one = [nums(k + "(I 1)") for k in "yz"]
    two = [nums(k + "(I 2)") for k in "yz"]
    assert len(names) == 5 and all(len(xs) == 2 for xs in two)
    for j, (pressure, _) in enumerate(nums("Pressure, GPa")):
        group = names[j].replace("₁", "1")
        c, dc = np.array([x[j] for x in xyz]).T
        sites = [[one[0][j], one[1][j]]]
        if j in (2, 3):
            sites.append([two[0][j - 2], two[1][j - 2]])
        sites = np.asarray(sites)
        yield (
            pressure,
            group,
            c,
            dc,
            sites[:, :, 0],
            sites[:, :, 1],
            nums("V (Å3)")[j][0],
            nums("ρcalc (g/cm3)")[j][0],
        )


def expand(group, sites):
    atoms = {}
    for i, (y, z) in enumerate(sites):
        for op in gemmi.find_spacegroup_by_name(group).operations():
            coord = tuple(np.round(np.mod(op.apply_to_xyz([0, y, z]), 1), 9) % 1)
            assert coord not in atoms or atoms[coord] == i
            assert np.all(np.asarray(op.rot) == np.diag(np.diag(op.rot)))
            atoms[coord] = i
    return atoms


def neighbours(cell, dcell, atoms, sites, dsite, i, extent):
    samples = []
    central = np.r_[0, sites[i]]
    for pos, j in atoms.items():
        for translation in product(range(-extent, extent + 1), repeat=3):
            direction = abs(np.array(pos) + translation - central)
            if max(direction) < 1e-6:
                continue
            sigma = np.r_[0, dsite[i] + dsite[j]]
            lo = np.linalg.norm(np.maximum(0, direction - sigma) * (cell - dcell))
            hi = np.linalg.norm((direction + sigma) * (cell + dcell))
            samples.append((np.linalg.norm(direction * cell), j, lo, hi))
    # Independent lower/upper order statistics enclose the sorted distances
    # even when equal neighbours exchange ranks inside this parameter box.
    ordered = sorted(samples)[:12]
    lower = sorted(x[2] for x in samples)[:12]
    upper = sorted(x[3] for x in samples)[:12]
    return [
        (round(v[0], 7), v[1], round(lo - 1e-8, 8), round(hi + 1e-8, 8))
        for v, lo, hi in zip(ordered, lower, upper, strict=True)
    ]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--pdf", type=Path)
    p.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("I_commensurate_neighbours.csv"),
    )
    a = p.parse_args()
    pdf = a.pdf.read_bytes() if a.pdf else urlopen(URL, timeout=25).read()
    with a.output.open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(
            [
                "p_GPa",
                "space_group",
                "conventional_atoms",
                "unique_central_site",
                "neighbor_site_at_central_parameters",
                "rank",
                "I_to_I_distance_A",
                "one_esd_box_low_A",
                "one_esd_box_high_A",
            ]
        )
        for pressure, group, cell, dcell, sites, dsite, volume, density in extract(pdf):
            atoms = expand(group, sites)
            assert len(atoms) == (2 if group == "Immm" else 8)
            assert abs(np.prod(cell) - volume) < 0.06
            assert (
                abs((len(atoms) * 126.90447 / 0.602214076 / volume) / density - 1)
                < 0.001
            )
            for i in range(len(sites)):
                links = neighbours(cell, dcell, atoms, sites, dsite, i, 1)
                assert links == neighbours(cell, dcell, atoms, sites, dsite, i, 2)
                for rank, (d, j, lo, hi) in enumerate(links, start=1):
                    writer.writerow(
                        [pressure, group, len(atoms), i + 1, j + 1, rank, d, lo, hi]
                    )
                d1, d2 = links[:2]
                print(
                    f"{pressure:g} GPa {group} I{i + 1}: {d1[0]:.5f}, {d2[0]:.5f} Å; "
                    f"d2/d1={d2[0] / d1[0]:.5f}, box [{d2[2] / d1[3]:.5f},{d2[3] / d1[2]:.5f}]"
                )


if __name__ == "__main__":
    main()
