"""Clamped-ion electronic dielectric response of fcc krypton in Quantum ESPRESSO."""

import argparse
import csv
import os
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

import numpy as np


FIELD_INPUT = """Static electronic dielectric tensor, fcc krypton
&inputph
 prefix='system', outdir='./out', tr2_ph=1.0d-14,
 epsil=.true., trans=.false., ldisp=.false., fildyn='Kr.dyn',
/
0.0 0.0 0.0
"""


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("work", type=Path)
    p.add_argument("--ph", default="ph.x")
    args = p.parse_args()
    with (args.work / "Kr_dielectric.csv").open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(
            [
                "ecutwfc_Ry",
                "ecutrho_Ry",
                "kgrid",
                "epsilon_electronic",
                "max_deviation_from_cubic_epsilon",
                "n_longwave",
                "Fresnel_R_longwave",
                "abs_max_unadjusted_Born_charge_e",
            ]
        )
        for cutoff, rho, n in [(64, 320, 4), (64, 320, 6), (64, 320, 8), (75, 400, 8)]:
            case = args.work.resolve() / f"Kr-{cutoff}-{rho}-{n}-0"
            assert "JOB DONE." in (case / "scf.out").read_text()
            result = case / "dielectric.out"
            if not result.is_file() or "JOB DONE." not in result.read_text():
                (case / "dielectric.in").write_text(FIELD_INPUT)
                env = {
                    **os.environ,
                    "OPENBLAS_NUM_THREADS": "1",
                    "OMP_NUM_THREADS": "1",
                    "UCX_VFS_ENABLE": "n",
                }
                with result.open("w") as log:
                    subprocess.run(
                        [args.ph, "-in", "dielectric.in"],
                        cwd=case,
                        env=env,
                        stdout=log,
                        stderr=subprocess.STDOUT,
                        check=True,
                    )
            tensors = (
                ET.parse(case / "out/_ph0/system.phsave/tensors.xml")
                .getroot()
                .find("EF_TENSORS")
            )
            assert tensors.findtext("DONE_ELECTRIC_FIELD") == "true"
            eps = np.fromstring(
                tensors.findtext("DIELECTRIC_CONSTANT"), sep=" "
            ).reshape((3, 3))
            e = np.trace(eps) / 3
            anisotropy = np.max(abs(eps - e * np.eye(3)))
            assert anisotropy < 1e-9 and e > 1
            charge = np.fromstring(tensors.findtext("EFFECTIVE_CHARGES_EU"), sep=" ")
            writer.writerow(
                [
                    cutoff,
                    rho,
                    n,
                    e,
                    anisotropy,
                    np.sqrt(e),
                    ((np.sqrt(e) - 1) / (np.sqrt(e) + 1)) ** 2,
                    np.max(abs(charge)),
                ]
            )
            stream.flush()


if __name__ == "__main__":
    main()
