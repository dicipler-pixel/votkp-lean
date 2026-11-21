"""Generate or independently audit the Kr–Zr printed ladder using Python 3.10+."""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction
from pathlib import Path

PIN = "c35b18b1c577bde90eacd3ef7cfa1bb2bb93024f"
SHA256 = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
COLUMNS = ["Z", "symbol", "k", "IE_k (eV)", "z_k", "Gamma_k", "source"]
# EA22 is Ning & Lu (2022), DOI 10.1063/5.0080243, Table I.
# Y23 is Zhang et al. (2023), DOI 10.1063/5.0124882.
# Zr17 is Fu et al. (2017), DOI 10.1063/1.4986547.
# Nonpositive krypton affinity gives no bound ground-state rung.
AFFINITIES = {
    "Kr": (None, None, "no bound ground-state anion"),
    "Rb": ("0.485916", "0.000021", "EA22"),
    "Sr": ("0.05206", "0.00006", "EA22"),
    "Y": ("0.31129", "0.00022", "Y23"),
    "Zr": ("0.433283", "0.000089", "Zr17"),
}


def read_input(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != SHA256:
        raise ValueError(f"archive bytes differ from pin {PIN}")
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        records = json.load(stream, parse_float=Decimal)["records"]
    selected = [r for r in records if 36 <= r["Z"] <= 40]
    if [(r["Z"], r["symbol"]) for r in selected] != list(enumerate(AFFINITIES, 36)):
        raise ValueError("missing or reordered element record")
    for r in selected:
        if [t["q"] for t in r["thresholds"]] != list(range(r["Z"])):
            raise ValueError(f"missing or reordered charge for {r['symbol']}")
    return selected


def print_digits(number):
    return format(number.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP), "f")


def generate(archive, csv_path):
    records = read_input(archive)
    with csv_path.open("w", newline="", encoding="utf-8") as stream, localcontext() as ctx:
        ctx.prec = 60
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(COLUMNS)
        for record in records:
            z, symbol = record["Z"], record["symbol"]
            ea, _, ea_source = AFFINITIES[symbol]
            energies = [Decimal(ea) if ea else None] + [Decimal(t["IE_eV"]) for t in record["thresholds"]]
            for k, start in enumerate(energies):
                ratio = reflection = ""
                if k < z and start is not None:
                    end = energies[k + 1]
                    ratio = print_digits(end / start)
                    reflection = print_digits((end - start) / (end + start))
                source = ea_source if k == 0 else record["thresholds"][k - 1]["grade"]
                writer.writerow([z, symbol, k, "" if start is None else format(start, "f"), ratio, reflection, source])


def round_positive_fraction(frac):
    """Round a nonnegative rational half-up without decimal division or float."""
    if frac < 0:
        raise ValueError("unexpected negative forward readout")
    numerator, denominator = frac.numerator, frac.denominator
    scaled = (2 * 10**6 * numerator + denominator) // (2 * denominator)
    integer, fractional = divmod(scaled, 10**6)
    return f"{integer}.{fractional:06d}"


def verify(archive, csv_path):
    records = read_input(archive)
    with csv_path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != COLUMNS:
            raise ValueError("wrong columns")
        rows = list(reader)
    expected_keys = [(r["Z"], r["symbol"], k) for r in records for k in range(r["Z"] + 1)]
    if [(int(x["Z"]), x["symbol"], int(x["k"])) for x in rows] != expected_keys:
        raise ValueError("missing, extraneous or reordered CSV row")
    by_z = {r["Z"]: r for r in records}
    energy_count = ordinary = anions = 0
    outside = []
    for row in rows:
        z, symbol, k = int(row["Z"]), row["symbol"], int(row["k"])
        thresholds = by_z[z]["thresholds"]
        ea, _, ea_source = AFFINITIES[symbol]
        grade = ea_source if k == 0 else thresholds[k - 1]["grade"]
        if row["source"] != grade:
            raise ValueError(f"incorrect source at {symbol}, k={k}")
        if k == 0 and ea is None:
            if any(row[c] for c in COLUMNS[3:6]):
                raise ValueError("krypton should have an empty k=0 record")
            continue
        energy = Fraction(ea) if k == 0 else Fraction(thresholds[k - 1]["IE_eV"])
        if Fraction(row["IE_k (eV)"]) != energy:
            raise ValueError(f"energy mismatch at {symbol}, k={k}")
        energy_count += k > 0
        if k == z:
            if row["z_k"] or row["Gamma_k"]:
                raise ValueError(f"terminal row {symbol} has an outgoing ratio")
            continue
        ratio = Fraction(thresholds[k]["IE_eV"]) / energy
        reflection = (ratio - 1) / (ratio + 1)
        if [row["z_k"], row["Gamma_k"]] != [round_positive_fraction(v) for v in (ratio, reflection)]:
            raise ValueError(f"ratio/reflection mismatch at {symbol}, k={k}")
        if 2 * reflection**2 > 1:
            outside.append(f"{symbol} k={k}")
        ordinary += k > 0
        anions += k == 0
    print(f"Archive {PIN}\nArchive SHA-256 {SHA256}")
    print(f"Verified {len(rows)} rows, {energy_count} archive energies, {ordinary} ordinary pairs, "
          f"{anions} externally sourced anion pairs. Differences: none.")
    print("Outside (exact central values): " + ", ".join(outside))
    print("CSV SHA-256 " + hashlib.sha256(csv_path.read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    if not args.verify_only:
        generate(args.archive, args.csv)
    verify(args.archive, args.csv)


if __name__ == "__main__":
    main()
