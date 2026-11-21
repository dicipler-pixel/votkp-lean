"""Compare archive→public ASD→published ladder using distinct inputs and integer arithmetic."""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal
from fractions import Fraction
from pathlib import Path


PIN = "182da01a14b10ce1e07e247565466d01822121c5"
ARCHIVE_DIGEST = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
AFFINITIES = {
    "Nb": ("0.91740", "EA22"), "Mo": ("0.74723", "EA22"),
    "Tc": ("0.636", "EA22-estimate"), "Ru": ("1.046270", "EA22"),
    "Rh": ("1.14273", "Rh26")
}


def check(condition, detail):
    if not condition:
        raise ValueError(detail)


def records(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def display(rational):
    """Round a positive exact ratio to six decimal places, half up."""
    quotient, remainder = divmod(10**6 * rational.numerator, rational.denominator)
    quotient += 2 * remainder >= rational.denominator
    return "%d.%06d" % divmod(quotient, 10**6)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("nist_csv", type=Path)
    parser.add_argument("ladder_csv", type=Path)
    args = parser.parse_args()
    check(hashlib.sha256(args.archive.read_bytes()).hexdigest() == ARCHIVE_DIGEST,
          f"archive does not match pin {PIN}")
    with gzip.open(args.archive, "rt", encoding="utf-8") as f:
        all_records = json.load(f, parse_float=Decimal)["records"]
    public = {}
    for r in records(args.nist_csv):
        z, q = int(r["Z"]), int(r["q"])
        key = (z, q)
        check(key not in public, f"duplicate NIST row {key}")
        text = r["NIST_energy_eV"]
        grade = {"[": "S", "(": "T"}.get(text[0], "E")
        value = Fraction(text.strip("[]()"))
        uncertainty = Fraction(r["NIST_unc_eV"]) if r["NIST_unc_eV"] else None
        public[key] = (value, uncertainty, grade, r["NIST_refs"])
    expected = {(z,q) for z in range(41,46) for q in range(z)}
    check(public.keys() == expected, "public ASD rows differ from expected keys")
    for atom in all_records:
        if atom["symbol"] not in AFFINITIES:
            continue
        for t in atom["thresholds"]:
            key = (atom["Z"], t["q"])
            check(public[key] == (t["IE_eV"], t["unc_eV"], t["grade"], t["references"]),
                  f"archive differs from public ASD at {key}")
    rows = records(args.ladder_csv)
    expected_order = [(z, k) for z in range(41,46) for k in range(z+1)]
    check([(int(r["Z"]), int(r["k"])) for r in rows] == expected_order, "CSV keys differ")
    outside = []
    for r, (z,k) in zip(rows, expected_order):
        symbol = all_records[z - 1]["symbol"]
        check(r["symbol"] == symbol, f"wrong symbol at {z},{k}")
        if k == 0:
            energy = Fraction(AFFINITIES[symbol][0])
            source = AFFINITIES[symbol][1]
        else:
            energy, _, source, _ = public[z,k-1]
        check(Fraction(r["IE_k (eV)"]) == energy, f"printed energy mismatch {symbol},{k}")
        check(r["source"] == source, f"source mismatch {symbol},{k}")
        if k == z:
            check(r["z_k"] == r["Gamma_k"] == "", f"nonblank endpoint {symbol},{k}")
            continue
        y = public[z,k][0]
        ratio = y/energy
        reflection = (y-energy)/(y+energy)
        check([r["z_k"],r["Gamma_k"]] == [display(ratio),display(reflection)],
              f"derived display mismatch {symbol},{k}")
        if 2 * (y-energy)**2 > (y+energy)**2:
            outside.append((symbol, k, source))
    print(f"Archive pin {PIN}")
    print(f"Matches to standalone public ASD snapshot: {len(public)} energies, uncertainty "
          "fields (including blanks), classes and reference strings in each category.")
    print(f"Reparsed {len(rows)} rows. All 215 stored ionization energies, 5 affinity "
          "source/value pairs, 210 ordinary outgoing pairs, 5 anion pairs and 5 terminal "
          "blanks agree. Differences: none.")
    print("Outside at central inputs: " + str(outside))
    print("Ladder SHA-256 " + hashlib.sha256(args.ladder_csv.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
