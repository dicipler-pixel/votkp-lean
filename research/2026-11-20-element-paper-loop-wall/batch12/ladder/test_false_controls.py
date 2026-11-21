"""Mutate single public fields in disposable copies and require the offline independent checker to fail."""
import argparse
import contextlib
import csv
import io
import shutil
import tempfile
from pathlib import Path

from verify_batch12 import DIR, verify


def controls(archive):
    cases = [
        ("batch12_ba_nd.csv", 60, 1, "IE_k (eV)", "5.52475", "replace pinned Nd first IE with live ASD"),
        ("batch12_ba_nd.csv", 56, 54, "z_k", "4.096049", "mistype last displayed digit of barium ratio"),
        ("batch12_ba_nd.csv", 59, 0, "Gamma_k", "0.960844", "mistype last displayed digit of praseodymium reflection"),
        ("rungs_detailed.csv", 58, 1, "unc_end_eV", "0.002", "shrink cerium second IE uncertainty tenfold"),
        ("anion_chemistry.csv", 56, None, "omega_over_eta", "0.6", "replace measured-branch chemistry ratio"),
        ("batch12_ba_nd.csv", 60, 60, "z_k", "1.000000", "invent outgoing ratio past the bare nucleus"),
    ]
    for filename,z,k,column,value,label in cases:
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)
            for name in ("batch12_ba_nd.csv","rungs_detailed.csv","anion_chemistry.csv"):
                shutil.copyfile(DIR/name,target/name)
            p=target/filename
            with p.open() as f:
                reader=csv.DictReader(f)
                fields=reader.fieldnames
                records=list(reader)
            matches=[r for r in records if int(r["Z"])==z and (k is None or int(r["k"])==k)]
            if len(matches)!=1 or matches[0][column]==value:
                raise ValueError(f"Invalid test mutation for {label}")
            matches[0][column]=value
            with p.open("w",newline="") as f:
                w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n")
                w.writeheader()
                w.writerows(records)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    verify(archive,target)
            except ValueError as err:
                print(f"REJECTED: {label}: {err}")
            else:
                raise ValueError(f"Incorrect input accepted: {label}")
    print(f"{len(cases)} deliberate mutations rejected.")


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive",type=Path)
    args=p.parse_args()
    controls(args.archive)
