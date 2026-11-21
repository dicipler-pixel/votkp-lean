"""Reparse the finished companion and independently recompute every numeric chemistry field."""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D, getcontext
from pathlib import Path

getcontext().prec=60
HERE=Path(__file__).resolve().parent
EV_PER_CM=D("6.62607015e-34")*299792458*100/D("1.602176634e-19")


def fields(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def verify(archive, folder):
    raw=archive.read_bytes()
    if hashlib.sha256(raw).hexdigest()!="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c":
        raise ValueError("wrong archive")
    atoms=json.loads(gzip.decompress(raw),parse_float=D)["records"]
    rows=fields(folder/"anion_chemistry_h_nd.csv")
    omitted=fields(folder/"no_bound_anion_h_nd.csv")
    ids=sorted([int(row["Z"]) for row in rows+omitted])
    if ids!=list(range(1,61)) or len(rows)!=49:
        raise ValueError("wrong coverage or duplicates")
    for row in rows:
        z=int(row["Z"])
        atom=atoms[z-1]
        t=atom["thresholds"][0]
        I,dI=D(t["IE_eV"]),D(t["unc_eV"])
        if (row["symbol"],D(row["IE1_pinned_eV"]),D(row["IE1_unc_eV"]),row["IE1_grade"],row["IE1_ref"])!=(
            atom["symbol"],I,dI,t["grade"],t["references"]):
            raise ValueError(f"wrong archive reference on {z}")
        factor=EV_PER_CM if row["EA_source_unit"]=="cm^-1" else D(1)
        A=D(row["EA_source_value"])*factor
        H=I-A
        chi=(I+A)/2
        eta=H/2
        omega=chi**2/H
        g=(I/A-1)/(I/A+1)
        full=omega/2
        cutoff=I/(3+2*D(2).sqrt())
        expected={
            "EA_eV":A, "z0":I/A, "Gamma0":g, "eta_half_eV":eta, "chi_eV":chi,
            "omega_eV":omega, "omega_over_eta":omega/eta,
            "H_full_eV":H, "omega_over_H":omega/H, "Omega_full_index_eV":full,
            "Omega_over_H":full/H, "chi_over_H":chi/H,
            "signed_wall_slack":(I**2-6*I*A+A**2)/(I+A)**2,
            "critical_EA_eV":cutoff, "EA_minus_critical_eV":A-cutoff}
        endpoint_columns=("slack_lo","slack_hi","omega_over_eta_lo","omega_over_eta_hi")
        if row["EA_source_unc"]:
            dA=D(row["EA_source_unc"])*factor
            expected["EA_unc_eV"]=dA
            # Test all four corners independently; no monotonic endpoint substitution.
            corners=[(x-y)/(x+y) for x in (I-dI,I+dI) for y in (A-dA,A+dA)]
            slack=[2*h*h-1 for h in corners]
            ratios=[1/(2*h*h) for h in corners]
            expected.update(zip(endpoint_columns,(min(slack),max(slack),min(ratios),max(ratios))))
        elif row["EA_status"]!="estimated" or any(row[c] for c in ("EA_unc_eV",*endpoint_columns)):
            raise ValueError(f"fabricated missing uncertainty at {z}")
        for field,expected_value in expected.items():
            if row[field]!=f"{expected_value:.12f}":
                raise ValueError(f"{row['symbol']} {field}: read {row[field]}, expected {expected_value:.12f}")
        if row["wall"]!=("outside" if A<cutoff else "inside" if A>cutoff else "on"):
            raise ValueError(f"wrong classification: {z}")
    print("All 49 serialized sets of chemistry fields match direct independent recomputation.")
    print("Four-corner bounds checked on 48 complete input boxes; technetium uncertainty remains blank.")
    print("Each Z from 1 through 60 has exactly one numeric or omitted row.")


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive",type=Path)
    p.add_argument("--folder",type=Path,default=HERE)
    args=p.parse_args()
    verify(args.archive,args.folder)
