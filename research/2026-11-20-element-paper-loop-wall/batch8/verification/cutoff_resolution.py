"""Find the interval of forward cutoffs with identical central ordinary labels."""
import argparse
from decimal import Decimal
from fractions import Fraction
import gzip
import json

def evaluate(path, zmax):
    with gzip.open(path, "rt") as file:
        records = json.load(file, parse_float=Decimal)["records"]
    inside, outside = [], []
    for record in records:
        if record["Z"] > zmax:
            continue
        energies = [Fraction(t["IE_eV"]) for t in record["thresholds"]]
        for k, (a, b) in enumerate(zip(energies, energies[1:]), 1):
            assert b > a > 0
            row = (b / a, record["symbol"], k)
            (outside if 2 * (b-a)**2 > (b+a)**2 else inside).append(row)
    lower, upper = max(inside), min(outside)
    print(f"Z 1–{zmax}: {len(inside)} inside, {len(outside)} outside")
    for name, (ratio, symbol, k) in [("lower inclusive", lower), ("upper exclusive", upper)]:
        print(f"{name}: {symbol} k={k}, z={ratio} = {float(ratio):.10f}")
    print("Outside:", ", ".join(f"{s} k={k}" for _, s, k in outside))
    for threshold in [5, 6, 7]:
        missed = [s for z, s, _ in outside if z <= threshold]
        added = [s for z, s, _ in inside if z > threshold]
        print(f"z>{threshold}: lost {missed}, added {added}")
    assert (lower[1:], upper[1:]) == (("N",5), ("C",4))
    assert len(inside)+len(outside) == zmax*(zmax-1)//2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive")
    args = parser.parse_args()
    evaluate(args.archive, 40)
