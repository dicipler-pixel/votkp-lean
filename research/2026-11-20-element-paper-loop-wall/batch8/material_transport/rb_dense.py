"""Calculate dense Rb bands at the fixed highest-cutoff self-consistent density."""

from pathlib import Path
import argparse
import os
import shutil
import subprocess
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work", type=Path)
    parser.add_argument("--pw", default="pw.x")
    parser.add_argument(
        "--grids", nargs="+", type=int, default=[16, 20, 24, 32, 40, 48]
    )
    parser.add_argument(
        "--reference",
        default="Rb-45-340-12-0.01",
        help="Name of a completed rubidium SCF case in WORK.",
    )
    args = parser.parse_args()
    work = args.work.resolve()
    reference = work / args.reference
    elem, wave_cutoff, density_cutoff, scf_grid, _ = reference.name.split("-")
    if elem != "Rb":
        raise ValueError("The valence band count here is specific to Rb.")
    if "JOB DONE." not in (reference / "scf.out").read_text():
        raise ValueError("Run qe_compare.py Rb and wait for a completed density.")
    for n in args.grids:
        case = work / f"Rb-{wave_cutoff}-{density_cutoff}-{n}-nscf"
        case.mkdir(exist_ok=True)
        saved = Path("out/system.save")
        dest = case / saved
        dest.mkdir(parents=True, exist_ok=True)
        old = dest / "data-file-schema.xml"
        if (
            old.exists()
            and (case / "nscf.out").exists()
            and "JOB DONE." in (case / "nscf.out").read_text()
        ):
            old_grid = (
                ET.parse(old)
                .getroot()
                .find("output/band_structure/starting_k_points/monkhorst_pack")
            )
            if old_grid is not None and int(old_grid.attrib["nk1"]) == n:
                continue
        for filename in ("data-file-schema.xml", "charge-density.dat", "paw.txt"):
            if (reference / saved / filename).exists():
                shutil.copy2(reference / saved / filename, dest / filename)
        inp = (
            (reference / "scf.in")
            .read_text()
            .replace("calculation='scf'", "calculation='nscf'")
            .replace("verbosity='high'", "verbosity='low', disk_io='low'")
            .replace("conv_thr=1.0d-9", "conv_thr=1.0d-9, diago_thr_init=1.0d-9")
            .replace(f"{scf_grid} {scf_grid} {scf_grid} 0 0 0", f"{n} {n} {n} 0 0 0")
        )
        if n >= 32:
            inp = inp.replace("nbnd=9", "nbnd=6").replace(
                "disk_io='low'", "disk_io='medium'"
            )
        (case / "nscf.in").write_text(inp)
        with (case / "nscf.out").open("w") as log:
            env = {
                **os.environ,
                "OMP_NUM_THREADS": "1",
                "OPENBLAS_NUM_THREADS": "1",
                "UCX_VFS_ENABLE": "n",
            }
            subprocess.run(
                [args.pw, "-in", "nscf.in"],
                cwd=case,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                check=True,
            )
        kgrid = (
            ET.parse(dest / "data-file-schema.xml").getroot().find(".//monkhorst_pack")
        )
        assert int(kgrid.attrib["nk1"]) == n
        for orbital_file in dest.glob("wfc*.dat"):
            orbital_file.unlink()


if __name__ == "__main__":
    main()
