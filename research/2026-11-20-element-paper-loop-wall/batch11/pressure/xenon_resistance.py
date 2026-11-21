"""Read the vector point centres in Eremets et al. (2000), Figure 2, at 300 K."""

import argparse
import csv
import hashlib
import math
from pathlib import Path
from urllib.request import urlopen

import numpy as np
import pymupdf

URL = "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=28731"
DIGEST = "cf1885e7771c5d5a8e4d48806d9413f6a4aef74ab30cc31c8297b47585209c3c"


def extract(data):
    assert hashlib.sha256(data).hexdigest() == DIGEST
    doc = pymupdf.open(stream=data, filetype="pdf")
    p = doc[1]
    assert "FIG. 2." in p.get_text()
    tick_x = []
    tick_y = []
    markers = []
    for d in p.get_drawings():
        for item in d["items"]:
            if item[0] != "l":
                continue
            start, end = item[1:]
            dx, dy = end.x - start.x, end.y - start.y
            if abs(dx) < 0.01 and 258.9 < start.y < 259.2 and -3.8 < dy < -3.6:
                tick_x.append(start.x)
            if 340.3 < start.x < 340.6 and abs(dy) < 0.01 and 2.7 < dx < 2.9:
                tick_y.append(start.y)
        box = d["rect"]
        if (
            d["type"] == "fs"
            and len(d["items"]) == 1
            and d["items"][0][0] == "re"
            and 340 < box.x0 < 552
            and 52 < box.y0 < 259
            and 2.7 < box.width < 2.9
            and 3.6 < box.height < 3.8
        ):
            markers.append(((box.x0 + box.x1) / 2, (box.y0 + box.y1) / 2))
    xp = np.sort(tick_x)
    yp = np.sort(tick_y)[::-1]
    assert (len(xp), len(yp), len(markers)) == (6, 9, 16)
    # Cross-check the marked x-axis labels against tick coordinates.
    labels = [
        (w[4], (w[0] + w[2]) / 2)
        for w in p.get_text("words")
        if w[0] > 340 and 259 < w[1] < 275
    ]
    assert [text for text, _ in labels] == list(map(str, range(60, 161, 20)))
    assert np.max(abs(xp - np.array([x for _, x in labels]))) < 0.2
    pressure = np.polyfit(xp, np.arange(60, 161, 20), 1)
    decades = np.polyfit(yp, np.arange(9), 1)
    assert np.max(abs(np.polyval(pressure, xp) - np.arange(60, 161, 20))) < 0.025
    assert np.max(abs(np.polyval(decades, yp) - np.arange(9))) < 0.003
    return [
        (float(np.polyval(pressure, x)), 10 ** float(np.polyval(decades, y)))
        for x, y in sorted(markers)
    ]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--pdf", type=Path, help="Local copy of the pinned NIST-hosted PDF.")
    p.add_argument(
        "--output", type=Path, default=Path(__file__).with_name("Xe_300K_figure2.csv")
    )
    a = p.parse_args()
    data = a.pdf.read_bytes() if a.pdf else urlopen(URL, timeout=30).read()
    rows = extract(data)
    with a.output.open("w", newline="") as out:
        writer = csv.writer(out, lineterminator="\n")
        writer.writerow(
            [
                "Z",
                "element",
                "temperature_K",
                "plotted_pressure_GPa",
                "plotted_sample_resistance_ohm",
                "source",
            ]
        )
        for pressure, resistance in rows:
            writer.writerow(
                [
                    54,
                    "xenon",
                    300,
                    f"{pressure:.2f}",
                    f"{resistance:.4g}",
                    "Eremets et al. 2000; Fig. 2; point centre",
                ]
            )
    p_first, r_first = rows[0]
    p_last, r_last = rows[-1]
    print(
        f"First and last marker: {p_first:.2f} GPa, {r_first:.4g} ohm; {p_last:.2f} GPa, {r_last:.4g} ohm."
    )
    print(f"Full plotted change: {math.log10(r_first / r_last):.3f} decades.")
    for low, hi in [(55, 75), (75, 150)]:
        sample = [(p, math.log10(r)) for p, r in rows if low <= p <= hi]
        slope, intercept = np.polyfit(*zip(*sample, strict=True), 1)
        print(
            f"{low}–{hi} GPa: {len(sample)} plotted measurements; descriptive log10(R) slope {slope:.4f}/GPa."
        )


if __name__ == "__main__":
    main()
