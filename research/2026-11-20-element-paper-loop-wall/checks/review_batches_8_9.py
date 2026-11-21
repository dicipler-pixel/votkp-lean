"""Reproduce both printed tables in a temporary folder and check independent ASD inputs."""
from pathlib import Path
import subprocess
import sys
import tempfile

paper = Path(__file__).resolve().parents[1]
root = paper.parents[1]
archive = root/'data/element_thresholds_20261011.json.gz'
b8, b9 = paper/'batch8', paper/'batch9'

def check(script, *args):
    subprocess.run([sys.executable, str(script), *map(str, args)], check=True)

def equal(a, b):
    if a.read_bytes() != b.read_bytes():
        raise ValueError(f"Reproduction differs: {b.name}")

with tempfile.TemporaryDirectory() as tmp:
    scratch = Path(tmp)
    kr = b8/'ladder/batch8_kr_zr.csv'
    rh = b9/'ladder/batch9_nb_rh.csv'
    check(b8/'ladder/batch8_ladder.py', archive, scratch/kr.name)
    equal(scratch/kr.name, kr)
    check(b8/'verification/verify_batch8.py', archive, kr)
    check(b8/'provenance/check_nist_snapshot.py', archive, b8/'provenance/nist_kr_zr_20261121.csv')
    check(b9/'ladder/batch9_ladder.py', archive, scratch)
    equal(scratch/rh.name, rh)
    equal(scratch/'batch9_rungs_detailed.csv', b9/'ladder/batch9_rungs_detailed.csv')
    check(b9/'independent/verify_nb_rh.py', archive, b9/'independent/nist_nb_rh_20261121.csv', rh)
    check(b9/'orbitals/check_orbitals.py', archive, '--csv', scratch/'opening_labels.csv')
    equal(scratch/'opening_labels.csv', b9/'orbitals/opening_labels.csv')
    check(b9/'ladder/batch9_rank_control.py', archive)
print("Both printed CSVs and the configuration labels reproduce byte-for-byte.")
