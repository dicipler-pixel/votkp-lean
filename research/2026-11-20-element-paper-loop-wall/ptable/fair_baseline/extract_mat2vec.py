"""Reproduce the F–At slice of CrabNet's published mat2vec table (Python 3)."""
from pathlib import Path
import csv
import hashlib
import json
import math
import sys

HERE = Path(__file__).resolve().parent
SOURCE_HASH = "5dcde1a0fe13040af99dbcb7b3d73eb022ffd085e7f598dce70844d0af83b137"


def extract(source):
    if hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Input does not match the pinned CrabNet CSV")
    with source.open(newline="") as stream:
        rows = csv.reader(stream)
        header = next(rows)
        if header != ["element", *map(str, range(200))]:
            raise ValueError("Unexpected embedding columns")
        vectors = {symbol: values for symbol, *values in rows}
    data = json.loads((HERE.parent / "v2" / "ptable_v2_data.json").read_text())
    eligible = [e["sym"] for e in data["elements"] if len(e["ie"]) >= 9
                and e.get("col") and not e.get("heavy")]
    if len(vectors) != 118 or len(eligible) != 77:
        raise ValueError("Unexpected population")
    with (HERE / "published_features.csv").open("w", newline="") as out:
        writer = csv.writer(out, lineterminator="\n")
        writer.writerow(["symbol", *[f"f{i:03d}" for i in range(1, 201)]])
        for symbol in eligible:
            values = vectors[symbol]
            if (len(values) != 200 or not all(math.isfinite(float(v)) for v in values)
                    or not any(float(v) != 0 for v in values)):
                raise ValueError(f"Invalid embedding for {symbol}")
            writer.writerow([symbol, *values])


if __name__ == "__main__":
    extract(Path(sys.argv[1]))
