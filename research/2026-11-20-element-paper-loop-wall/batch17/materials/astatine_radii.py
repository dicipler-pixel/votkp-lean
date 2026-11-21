"""Rebuild Tables II (ground and isomer data) and the within-isotope radius test.

Usage: python astatine_radii.py /path/to/PhysRevC.97.054327.pdf
Source: https://upload.wikimedia.org/wikipedia/commons/1/18/PhysRevC.97.054327.pdf
The file is the fixed 2018 publisher version. Requires pdftotext on PATH.
"""
import csv
from decimal import Decimal as D
from hashlib import sha256
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
DOI = "10.1103/PhysRevC.97.054327"
PDF_HASH = "42e4da0b7bc7b88386422950175393dc3a399b720534991b2da32e794f7a93f3"


def write(name, rows):
    with (HERE / name).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def extract(path):
    if sha256(path.read_bytes()).hexdigest() != PDF_HASH:
        raise ValueError("PDF digest differs from the publisher copy used for this extraction")
    text = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    table = text.split("TABLE II. Extracted values")[1].split("For I = 5,")[0]
    rows = []
    mass, state = None, ""
    for line in table.replace("−", "-").splitlines():
        ident = re.fullmatch(r"(\d{3})(?: (g|m[12]?))?", line)
        if ident:
            mass, state = int(ident.group(1)), ident.group(2) or ""
        if not line.strip().startswith("At"):
            continue
        label, n, spin, radius, deformation, moment, *quadrupole = re.split(r"\s{2,}", line.strip())
        state = label.removeprefix("At").strip() or state or "unqualified"
        if int(n) != mass - 85:
            raise ValueError(f"Bad state alignment at {mass}At")
        if radius == "0":
            value, unc_stat, unc_sys = (D(0),) * 3
        else:
            match = re.fullmatch(r"(-?\d+\.\d+)\((\d+)\)\{(\d+)\}", radius)
            value = D(match.group(1))
            unit = D(10) ** value.as_tuple().exponent
            unc_stat, unc_sys = (D(digits) * unit for digits in match.groups()[1:])
        rows.append(dict(A=mass, state=state, N=n, spin_parity=spin.replace(" ", ""),
                         delta_r2_A_minus_205_fm2=value, stat_fm2=unc_stat, sys_fm2=unc_sys,
                         dipole_muN_as_printed=moment, quadrupole_b_as_printed="".join(quadrupole),
                         table="II", doi=DOI))
    if len(rows) != 24 or len({(r["A"], r["state"]) for r in rows}) != 24:
        raise ValueError("Expected 24 distinct published isotope states")
    return rows


def contrasts(rows):
    result = []
    ground = {r["A"]: r for r in rows if r["state"] == "g"}
    for isomer in rows:
        if not isomer["state"].startswith("m"):
            continue
        ref = ground[isomer["A"]]
        diff = isomer["delta_r2_A_minus_205_fm2"] - ref["delta_r2_A_minus_205_fm2"]
        # The shared reference and theoretical electronic factor induce correlations.
        # A sum of absolute errors gives a box, without fitting an unknown covariance.
        budget = sum(r[key] for r in (isomer, ref) for key in ("stat_fm2", "sys_fm2"))
        result.append(dict(A=isomer["A"], contrast=isomer["state"]+"-g",
                           delta_isomer_minus_ground_fm2=diff, one_box_budget_fm2=budget,
                           worst_three_box_lower_fm2=diff-3*budget,
                           worst_three_box_upper_fm2=diff+3*budget,
                           positive_at_three_boxes=diff > 3*budget))
    return result


if __name__ == "__main__":
    rows = extract(Path(sys.argv[1]))
    tests = contrasts(rows)
    write("astatine_radii.csv", rows)
    write("astatine_isomer_controls.csv", tests)
    print(f"{len(rows)} states, {len(tests)} isomer contrasts, "
          f"{sum(r['positive_at_three_boxes'] for r in tests)} positive at three boxes")
