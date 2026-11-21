"""Snapshot a public ASD table including both the leading ground shells and the energies."""
import argparse
import csv
import sys
from pathlib import Path
from subprocess import check_output
from urllib.parse import urlencode

DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(DIR.parents[1] / "batch11" / "independent"))
from fetch_asd import datarows

ELEMENTS = ("Dy", "Ho", "Er", "Tm", "Yb")
FIELDS = "Z,q,element,isoelectronic,ground_shells,ground_term_NIST,NIST_energy_eV,NIST_unc_eV,NIST_refs".split(",")


def snapshot(path, cache=None):
    allrows = []
    for z, sym in enumerate(ELEMENTS, 66):
        query = dict(at_num_out="on", biblio="on", e_out=0, el_name_out="on",
                     level_out="on", seq_out="on", shells_out="on", spectra=sym, unc_out="on", units=1)
        url = "https://physics.nist.gov/cgi-bin/ASD/ie.pl?" + urlencode(query)
        raw = ((cache / (sym + ".html")).read_bytes() if cache else
               check_output(["curl", "--retry", "2", "-fsSL", "--max-time", "45", url]))
        rows = datarows(raw.decode())
        if len(rows) != z or rows[0][2] != sym or rows[-1][2] != "H":
            raise ValueError(f"Incomplete table for {sym}")
        for q, row in enumerate(rows):
            if len(row) != 8 or int(row[0]) != z:
                raise ValueError(f"Malformed ASD record at {sym} charge {q}")
            allrows.append([z, q, *row[1:]])
    with path.open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(FIELDS)
        writer.writerows(allrows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--cache", type=Path)
    args = parser.parse_args()
    snapshot(args.path, args.cache)
