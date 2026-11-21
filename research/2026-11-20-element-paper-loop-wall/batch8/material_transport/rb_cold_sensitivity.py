"""Hold the 5 K measured cell fixed and change three electronic integration settings."""

import argparse
import csv
import gzip
import json
from pathlib import Path
import subprocess
import sys

from rb_fermi_surface import extract_nodes
from rb_orbits import compute
from qe_compare import run_case


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("work", type=Path)
    p.add_argument("--pw", default="pw.x")
    p.add_argument("--save", type=Path)
    p.add_argument("--replay", type=Path)
    a = p.parse_args()
    work = a.work.resolve() / "Rb-5K-sensitivity"
    work.mkdir(parents=True, exist_ok=True)
    if a.replay:
        data = json.loads(gzip.decompress(a.replay.read_bytes()))
    else:
        run_case("Rb", work, a.pw, (55, 420, 16, 0.005), lattice_parameter=5.585)
        subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("rb_dense.py")),
                str(work),
                "--pw",
                a.pw,
                "--reference",
                "Rb-55-420-16-0.005",
                "--grids",
                "32",
            ],
            check=True,
        )
        data = extract_nodes(
            work / "Rb-55-420-32-nscf/out/system.save/data-file-schema.xml"
        )
    if a.save:
        a.save.write_bytes(
            gzip.compress(json.dumps(data, separators=(",", ":")).encode(), mtime=0)
        )
    rows = compute(data, 32, 256)
    with (work / "Rb_cold_convergence.csv").open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(
            [
                "pw_Ry",
                "charge_Ry",
                "SCF_grid",
                "SCF_width_Ry",
                "band_grid",
                "direction",
                "area_distortion_parts_per_10000",
                "onsager_frequency_kT",
            ]
        )
        for row in rows:
            w.writerow(
                [55, 420, 16, 0.005, row[0], row[3], round(row[8], 8), round(row[9], 8)]
            )


if __name__ == "__main__":
    main()
