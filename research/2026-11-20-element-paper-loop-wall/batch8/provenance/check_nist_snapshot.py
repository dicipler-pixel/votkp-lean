"""Compare a public ASD energy-table snapshot to the pinned VOTKP archive.

Usage: python3 check_nist_snapshot.py ARCHIVE NIST_SNAPSHOT.csv
Numeric values, punctuation-derived grades, uncertainty field and references must agree.
"""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal
from pathlib import Path


def compare(archive, snapshot):
    if hashlib.sha256(archive.read_bytes()).hexdigest() != "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c":
        raise ValueError("archive differs from c35b18b1c577bde90eacd3ef7cfa1bb2bb93024f")
    with gzip.open(archive, "rt", encoding="utf-8") as f:
        records = json.load(f, parse_float=Decimal)["records"]
    expected = {(r["Z"], t["q"]): t for r in records if 36 <= r["Z"] <= 40 for t in r["thresholds"]}
    with snapshot.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    seen = set()
    counts = dict.fromkeys(["energy", "uncertainty", "grade", "references"], 0)
    for row in rows:
        key = (int(row["Z"]), int(row["q"]))
        if key in seen or key not in expected:
            raise ValueError(f"unexpected or duplicate key {key}")
        seen.add(key)
        t = expected[key]
        formatted = row["NIST_energy_eV"]
        grade = "T" if formatted.startswith("(") else "S" if formatted.startswith("[") else "E"
        energy = Decimal(formatted.strip("[]()"))
        unc = Decimal(row["NIST_unc_eV"]) if row["NIST_unc_eV"] else None
        for name, x, y in [
            ("energy", energy, t["IE_eV"]), ("uncertainty", unc, t["unc_eV"]),
            ("grade", grade, t["grade"]), ("references", row["NIST_refs"], t["references"])
        ]:
            if x != y:
                raise ValueError(f"{key} {name} mismatch: public table {x}, pin {y}")
            counts[name] += 1
    if expected.keys() != seen:
        raise ValueError(f"missing rows: {sorted(expected.keys() - seen)}")
    for label, number in counts.items():
        print(f"{label}: {number} matched, 0 differences")
    print("Uncertainty comparisons include blank Zr q=1 matched to archived null.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    compare(args.archive, args.snapshot)
