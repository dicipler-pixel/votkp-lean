"""Rebuild the six published Ba-IVb superspace bond tables (Python standard library).

python barium_modulation.py [directory containing the six COD CIFs]
Without an input directory the script downloads the cited COD records.
Outputs are written beside this script.
"""
import argparse
import csv
import hashlib
import re
import urllib.request
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
CIF_HASH = {
    "1545111": "26223218214e138ce1afa518364d36b07d74860bfc429f41a214d9162393a34d",
    "1545112": "cf095a8a58b6e989a5b0bbefa663e9cc6e67a669dc5b3dc3402f3a0b2b054a3d",
    "1545113": "a43e1d8d1ba040b2725237f942f42268de43c1a1ccff19683397e6e01550d215",
    "1545114": "551a1c563cc4db463ce1adcfc8c1201b089c4928ffd215751f2a7261969a970f",
    "1545115": "e832859c5122d7ac21e08978f62b7dfbaa68ca0409e36f85b84dbd5fb2ae670b",
    "1545116": "32ec1196a6889b2e571da7ebde782c52e1f4e847fd5f6ead406ade8b987c9b8d",
}


def number(text):
    """Return the printed central value and its stated standard uncertainty."""
    match = re.fullmatch(r"(-?\d+(?:\.\d+)?)(?:\((\d+)\))?", text)
    if match is None:
        raise ValueError(text)
    value = Decimal(match[1])
    uncertainty = Decimal(match[2]).scaleb(value.as_tuple().exponent) if match[2] else None
    return value, uncertainty


def source(cod, folder):
    url = f"https://qiserver.ugr.es/cod/{cod}.cif"
    data = (folder / f"{cod}.cif").read_bytes() if folder else urllib.request.urlopen(url, timeout=40).read()
    if hashlib.sha256(data).hexdigest() != CIF_HASH[cod]:
        raise ValueError(f"Source revision changed: {url}")
    return data.decode(), url


def cif_loop(body, first_tag):
    """Read these simple, whitespace-delimited CIF loops, checking every row length."""
    blocks = body.split("loop_")
    lines = next(b for b in blocks if b.strip().startswith(first_tag)).strip().splitlines()
    header = [tag.strip() for tag in lines if tag.startswith("_")]
    start = len(header)
    rows = []
    for line in lines[start:]:
        if not line.strip() or line.lstrip().startswith(("#", "_")):
            break
        values = line.split()
        if len(values) != len(header):
            raise ValueError(line)
        rows.append(dict(zip(header, values)))
    return rows


def write(name, rows):
    with (HERE / name).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=tuple(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main(folder):
    bonds, summaries = [], []
    for cod in CIF_HASH:
        body, url = source(cod, folder)
        # The chemical name explicitly specifies GPa. The pressure CIF tag
        # prints the same number without a unit.
        pressure = re.search(r"at high pressure of (\d+(?:\.\d+)?) GPa", body)[1]
        temp = re.search(r"^_diffrn_ambient_temperature\s+(\S+)", body, re.M)[1]
        c_repeat = re.search(r"^_cell_length_c\s+(\S+)", body, re.M)[1]
        q = cif_loop(body, "_cell_wave_vector_seq_id")[0]
        grouped = {}
        for row in cif_loop(body, "_geom_bond_atom_site_label_1"):
            a, b = (row["_geom_bond_atom_site_label_" + i] for i in ("1", "2"))
            family = ("host-host", "host-guest", "guest-guest")[sum(s.endswith("g") for s in (a, b))]
            lo, hi, avg = (row["_geom_bond_distance_" + i] for i in ("min", "max", "av"))
            assert number(lo)[0] <= number(avg)[0] <= number(hi)[0]
            grouped.setdefault(family, []).append((lo, hi))
            bonds.append(dict(COD=cod, P_GPa=pressure, T_K=temp, family=family, site_1=a,
                              site_2=b, superspace_operation_2=row["_geom_bond_site_ssg_symmetry_2"],
                              min_A_esd=lo, mean_A_esd=avg, max_A_esd=hi, source=url))
        for family, values in grouped.items():
            summaries.append(dict(COD=cod, P_GPa=pressure, T_K=temp, c_A_esd=c_repeat,
                                  q_a=q["_cell_wave_vector_x"], q_b=q["_cell_wave_vector_y"],
                                  q_c=q["_cell_wave_vector_z"], family=family,
                                  pairs=len(values), smallest_min_A_esd=min((v[0] for v in values), key=number),
                                  largest_max_A_esd=max((v[1] for v in values), key=number)))
    assert len(bonds) == 175 and len(summaries) == 18
    check = {r["P_GPa"]: r for r in summaries if r["family"] == "guest-guest"}
    lower, higher = check["17.4"], check["18.5"]
    x, sx = number(lower["largest_max_A_esd"])
    y, sy = number(higher["largest_max_A_esd"])
    c1, c2 = number(lower["c_A_esd"])[0], number(higher["c_A_esd"])[0]
    assert x + 3 * sx < y - 3 * sy and c2 < c1
    write("barium_modulated_bonds.csv", bonds)
    write("barium_modulation_summary.csv", summaries)
    print(f"{len(bonds)} superspace bond rows; {len(summaries)} family-pressure summaries")
    print(f"17.4 → 18.5 GPa, guest maximum {x} → {y} Å; host c {c1} → {c2} Å")
    print(f"At 3 reported standard uncertainties: {x + 3*sx} < {y - 3*sy} Å")


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("folder", nargs="?", type=Path)
    main(arg.parse_args().folder)
