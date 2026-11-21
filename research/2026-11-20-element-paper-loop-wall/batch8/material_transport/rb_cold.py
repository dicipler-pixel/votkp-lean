"""Re-evaluate the Rb DOS at the 5 K bcc diffraction lattice parameter."""

import argparse
import csv
import gzip
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.constants import Avogadro, Boltzmann, elementary_charge

from qe_compare import run_case
from rb_fermi_surface import extract_nodes, band_grid
from rb_tetrahedra import integrate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work", type=Path)
    parser.add_argument("--pw", default="pw.x")
    parser.add_argument(
        "--archive", type=Path, help="Save the compact cold-cell band bundle."
    )
    parser.add_argument(
        "--replay", type=Path, help="Use a supplied band bundle without QE."
    )
    args = parser.parse_args()
    work = args.work.resolve() / "Rb-5K"
    work.mkdir(parents=True, exist_ok=True)
    if args.replay:
        records = json.loads(gzip.decompress(args.replay.read_bytes()))
    else:
        run_case("Rb", work, args.pw, (45, 340, 12, 0.01), lattice_parameter=5.585)
        subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("rb_dense.py")),
                str(work),
                "--pw",
                args.pw,
                "--grids",
                "24",
                "32",
                "40",
            ],
            check=True,
        )
        records = {}
        for n in (24, 32, 40):
            xml = work / f"Rb-45-340-{n}-nscf" / "out/system.save/data-file-schema.xml"
            records[str(n)] = extract_nodes(xml)
    if args.archive:
        args.archive.write_bytes(
            gzip.compress(json.dumps(records, separators=(",", ":")).encode(), mtime=0)
        )
    coeff = 1e3 * np.pi**2 / 3 * Boltzmann**2 * Avogadro / elementary_charge
    with (work / "Rb_cold.csv").open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(
            [
                "diffraction_T_K",
                "a_A",
                "k_grid",
                "orientation",
                "chemical_potential_eV",
                "DOS_states_per_eV_cell",
                "K_eV_A2",
                "intraband_plasma_energy_eV",
                "gamma_band_mJ_per_mol_K2",
            ]
        )
        for data in records.values():
            e, b, vol, _ = band_grid(data)
            assert abs((2 * vol) ** (1 / 3) - 5.585) < 1e-6
            for signs in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]:
                n, sign, mu, dos, k, wp, _ = integrate(e[:, :, :, 4], b, vol, signs)
                writer.writerow(
                    [
                        5,
                        5.585,
                        n,
                        sign,
                        *[round(val, 8) for val in (mu, dos, k, wp, coeff * dos)],
                    ]
                )


if __name__ == "__main__":
    main()
