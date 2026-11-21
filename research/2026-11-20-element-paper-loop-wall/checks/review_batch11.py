"""Regenerate the antimony–cesium publication tables without changing the checkout."""
from pathlib import Path
import subprocess
import sys
import tempfile

paper = Path(__file__).resolve().parents[1]
batch = paper / "batch11"
archive = paper.parents[1] / "data/element_thresholds_20261011.json.gz"

def run(script, *arguments, capture=False):
    process = subprocess.run([sys.executable, str(script), *map(str,arguments)],
                             check=True,stdout=subprocess.PIPE if capture else None)
    return process.stdout

def compare(actual, expected):
    if actual != expected.read_bytes():
        raise ValueError(f"Reproduction differs from {expected.relative_to(batch)}")

with tempfile.TemporaryDirectory() as directory:
    tmp = Path(directory)
    ladder = batch / "ladder"
    independent = batch / "independent"
    run(ladder/"batch11_ladder.py", archive, tmp)
    for name in ("batch11_sb_cs.csv", "batch11_rungs_detailed.csv", "batch11_summary.csv"):
        compare((tmp/name).read_bytes(), ladder/name)
    run(independent/"verify_sb_cs.py", archive, independent/"nist_sb_cs.csv", tmp/"batch11_sb_cs.csv")
    run(ladder/"batch11_controls.py",archive,tmp/"homologs.csv")
    compare((tmp/"homologs.csv").read_bytes(), ladder/"batch11_homologs.csv")
    comparable = run(batch/"robust/cutoff_holdout.py",archive,
                     paper/"batch10/robust/affinities_h_sn.csv",tmp/"batch11_rungs_detailed.csv",capture=True)
    compare(comparable,batch/"robust/cutoff_holdout.txt")
    compare(run(independent/"assign_openings.py",independent/"asd_configurations.csv",capture=True),
            independent/"opening_orbitals.csv")
    compare(run(batch/"screw/tellurium_screw.py",capture=True),batch/"screw/tellurium_screw.txt")
print("Published thresholds, rounded ratios, cutoff windows, homologs, orbital changes and screw signs reproduce.")
