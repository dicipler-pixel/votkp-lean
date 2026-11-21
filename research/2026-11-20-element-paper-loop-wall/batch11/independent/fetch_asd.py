"""Fetch two independent ASD tables and require agreement on duplicate fields."""
import argparse
import csv
import html
import re
import subprocess
from pathlib import Path

ELEMENTS = ("Sb:antimony", "Te:tellurium", "I:iodine", "Xe:xenon", "Cs:cesium")
ISO = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs".split()


def decode(value):
    value = value.replace("<sup>", "^{").replace("<sub>", "_{")
    value = value.replace("</sup>", "}").replace("</sub>", "}")
    return "".join(html.unescape(re.sub(r"<[^>]*>", "", value)).split())


def datarows(raw):
    return [[decode(c) for c in re.findall(r"<td\b[^>]*>(.*?)</td>", row, re.S)]
            for row in re.findall(r'<tr class="bsl">(.*?)</tr>', raw, re.S)]


def write_csv(path, columns, rows):
    with path.open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(columns.split(","))
        writer.writerows(rows)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("out", type=Path)
    p.add_argument("--saved-html", type=Path, help="Optional cache containing symbol_{0,1}.html")
    a = p.parse_args()
    a.out.mkdir(exist_ok=True, parents=True)
    energies, states = [], []
    for z, spec in enumerate(ELEMENTS, 51):
        s, n = spec.split(":")
        base = "https://physics.nist.gov/cgi-bin/ASD/ie.pl?"
        links = (base + f"at_num_out=1&biblio=1&e_out=0&el_name_out=1&ion_charge_out=1&spectra={n}&unc_out=1&units=1",
                 base + f"at_num_out=on&biblio=on&e_out=0&el_name_out=on&level_out=on&seq_out=on&shells_out=on&spectra={s}&unc_out=on&units=1")
        tables = []
        for i, url in enumerate(links):
            raw = ((a.saved_html / f"{s}_{i}.html").read_bytes() if a.saved_html else
                   subprocess.check_output(["curl", "-fsSL", "--max-time", "60", url]))
            table = datarows(raw.decode("utf-8"))
            if len(table) != z:
                raise ValueError(f"{s} query {i}: expected {z} rows, found {len(table)}")
            tables.append(table)
        for q, (e, cfg) in enumerate(zip(*tables)):
            if not (int(e[0]) == int(cfg[0]) == z and int(e[1]) == q and e[-3:] == cfg[-3:]
                    and e[2] == cfg[1] and cfg[2] == ISO[z-q-1]):
                raise ValueError(f"ASD query disagreement at {s}, q={q}")
            energies.append([z, q, *e[-3:]])
            states.append([z, q, *cfg[1:5]])
    write_csv(a.out/"nist_sb_cs.csv", "Z,q,NIST_energy_eV,NIST_unc_eV,NIST_refs", energies)
    write_csv(a.out/"asd_configurations.csv", "Z,q,element,isoelectronic,ground_shells,ground_term_NIST", states)


if __name__ == "__main__":
    main()
