"""Rebuild the palladium–tin tables and the two cross-archive comparisons."""
from pathlib import Path
import subprocess
import sys
import tempfile

paper = Path(__file__).resolve().parents[1]
batch = paper / "batch10"
archive = paper.parents[1] / "data/element_thresholds_20261011.json.gz"

def run(script, *args, capture=False):
    result = subprocess.run([sys.executable, str(script), *map(str, args)],
                            stdout=subprocess.PIPE if capture else None, check=True)
    return result.stdout

def check_bytes(blob, path):
    if blob != path.read_bytes():
        raise ValueError(f"Generated data differ from {path.relative_to(paper)}")

with tempfile.TemporaryDirectory() as work:
    tmp = Path(work)
    source = batch / "ladder"
    run(source / "batch10_ladder.py", archive, tmp)
    for name in ("batch10_pd_sn.csv", "batch10_rungs_detailed.csv", "batch10_summary.csv"):
        check_bytes((tmp/name).read_bytes(), source/name)
    public = batch / "independent"
    run(public/"verify_pd_sn.py", archive, public/"nist_pd_sn_20261121.csv", tmp/"batch10_pd_sn.csv")
    run(source/"screening_controls.py", archive, tmp/"components.csv")
    check_bytes((tmp/"components.csv").read_bytes(), source/"screening_controls.csv")
    run(source/"batch10_controls.py", archive)
    pairs = batch / "mixed_map"
    run(pairs/"adjacent_pairs.py", archive, tmp)
    for name in ("opening_faces.csv", "adjacent_pairs.csv"):
        check_bytes((tmp/name).read_bytes(), pairs/name)
    cutoffs = batch/"robust"
    report = run(cutoffs/"cutoff_intervals.py", archive, "--missing", tmp/"missing.csv", capture=True)
    check_bytes(report, cutoffs/"cutoff_results.txt")
    check_bytes((tmp/"missing.csv").read_bytes(), cutoffs/"cutoff_missing_boxes.csv")
    angles = paper/"batch8/lambert"
    check_bytes(run(angles/"angle_control.py", archive, capture=True), angles/"angle_control.csv")
print("All generated tables and independent scalar-cutoff, component and geometry comparisons reproduce.")
