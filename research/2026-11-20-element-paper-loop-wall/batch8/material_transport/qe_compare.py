"""Small, reproducible Quantum ESPRESSO PBE band-character comparison.

Usage: python qe_compare.py Rb ./qe-runs --pw pw.x
"""

import argparse
import csv
import hashlib
import os
from pathlib import Path
import subprocess
import urllib.request
import xml.etree.ElementTree as ET

ELEMENTS = {
    "Kr": (
        2,
        5.721,
        83.798,
        13,
        "dn",
        "e642273d4df7ae7c3d0d195b301f30336ff2b5977163d35f429270c7728ed4e8",
    ),
    "Rb": (
        3,
        5.700,
        85.4678,
        9,
        "spn",
        "6e8ebe2c70064c509eb4a50578939662802c3b1dc99b51b8d302487842dc9fdb",
    ),
}
# Wavefunction and density cutoffs in Ry, uniform Gamma-centered k mesh,
# and Fermi-Dirac degauss in Ry (0 means fixed Kr occupations).
RUNS = {
    "Rb": [
        (35, 260, 6, 0.02),
        (35, 260, 8, 0.02),
        (35, 260, 12, 0.02),
        (35, 260, 12, 0.01),
        (45, 340, 12, 0.01),
    ],
    "Kr": [(64, 320, 4, 0), (64, 320, 6, 0), (64, 320, 8, 0), (75, 400, 8, 0)],
}
EV = 27.211386245981


def run_case(symbol, work, pw, case, lattice_parameter=None):
    lattice, a, mass, bands, family, digest = ELEMENTS[symbol]
    if lattice_parameter is not None:
        a = lattice_parameter
    cutoff, rho, grid, smear = case
    pp = f"{symbol}.pbe-{family}-kjpaw_psl.1.0.0.UPF"
    ppdir = work / "pps"
    ppdir.mkdir(exist_ok=True)
    if not (ppdir / pp).is_file():
        urllib.request.urlretrieve(
            "https://pseudopotentials.quantum-espresso.org/upf_files/" + pp, ppdir / pp
        )
    assert hashlib.sha256((ppdir / pp).read_bytes()).hexdigest() == digest
    folder = work / f"{symbol}-{cutoff}-{rho}-{grid}-{smear:g}"
    folder.mkdir(exist_ok=True)
    additional = (
        f"occupations='smearing', smearing='fd', degauss={smear}"
        if smear
        else "occupations='fixed'"
    )
    input_text = f"""&CONTROL
    calculation='scf', prefix='system', pseudo_dir='{ppdir}', outdir='./out', verbosity='high'
/
&SYSTEM
    ibrav={lattice}, A={a}, nat=1, ntyp=1, ecutwfc={cutoff}, ecutrho={rho}, nbnd={bands},
    {additional}
/
&ELECTRONS
    conv_thr=1.0d-9, mixing_beta=0.5
/
ATOMIC_SPECIES
{symbol} {mass} {pp}
ATOMIC_POSITIONS crystal
{symbol} 0 0 0
K_POINTS automatic
{grid} {grid} {grid} 0 0 0
"""
    (folder / "scf.in").write_text(input_text)
    output = folder / "scf.out"
    if not output.exists() or "JOB DONE." not in output.read_text():
        env = {
            **os.environ,
            "OPENBLAS_NUM_THREADS": "1",
            "OMP_NUM_THREADS": "1",
            "UCX_VFS_ENABLE": "n",
        }
        with output.open("w") as log:
            subprocess.run(
                [pw, "-in", "scf.in"],
                cwd=folder,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                check=True,
            )
    xml = ET.parse(folder / "out/system.save/data-file-schema.xml").getroot()
    report = xml.find("output")
    assert report.findtext("convergence_info/scf_conv/convergence_achieved") == "true"
    bs = report.find("band_structure")
    fermi = bs.findtext("fermi_energy")
    levels = [
        [float(e) * EV for e in item.findtext("eigenvalues").split()]
        for item in bs.findall("ks_energies")
    ]
    occupied_index = 8 if symbol == "Kr" else 4
    low = min(e[occupied_index] for e in levels)
    high = max(e[occupied_index] for e in levels)
    nxt = min(e[occupied_index + 1] for e in levels)
    mu = float(fermi) * EV if symbol == "Rb" else None
    if symbol == "Rb":
        assert low < mu < high
    else:
        assert nxt > high
    return [
        symbol,
        cutoff,
        rho,
        grid,
        smear,
        len(levels),
        len(levels[0]),
        occupied_index + 1,
        low,
        high,
        nxt,
        mu,
        high - low,
        nxt - high if symbol == "Kr" else None,
        report.findtext("convergence_info/scf_conv/n_scf_steps"),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("element", choices=ELEMENTS)
    parser.add_argument("work", type=Path)
    parser.add_argument("--pw", default="pw.x")
    args = parser.parse_args()
    work = args.work.resolve()
    work.mkdir(exist_ok=True, parents=True)
    with (work / f"{args.element}_pbe.csv").open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(
            (
                "element",
                "ecut_wfc_Ry",
                "ecut_rho_Ry",
                "kgrid",
                "smearing_Ry",
                "irreducible_kpts",
                "nbands",
                "tracked_band",
                "band_min_eV",
                "band_max_eV",
                "next_band_min_eV",
                "mu_eV",
                "tracked_bandwidth_eV",
                "indirect_KS_gap_eV",
                "scf_steps",
            )
        )
        for case in RUNS[args.element]:
            writer.writerow(run_case(args.element, work, args.pw, case))
            stream.flush()


if __name__ == "__main__":
    main()
