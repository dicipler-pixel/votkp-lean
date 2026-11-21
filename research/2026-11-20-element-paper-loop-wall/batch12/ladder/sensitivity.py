"""Display declared source variants and test cutoff controls without refitting."""
from decimal import Decimal as D, getcontext
from pathlib import Path
import argparse
import csv

from batch12_ladder import archive, rows

DIR=Path(__file__).resolve().parent
getcontext().prec=60
W=D(3)+2*D(2).sqrt()


def variant(name,x,dx,y,dy):
    z=y/x
    lo=(y-dy)/(x+dx)
    hi=(y+dy)/(x-dx)
    status="inside" if hi<W else "outside" if lo>W else "straddles"
    return [name,x,dx,y,dy,*(f"{v:.10f}" for v in (z,(y-x)/(y+x),lo,hi)),status]


def main(path, folder):
    atoms=archive(path)
    aff={r["symbol"]:(D(r["EA_eV"]),D(r["unc_eV"])) for r in rows(DIR/"affinities.csv")}
    state={(r["Z"],r["q"]):r for r in rows(DIR/"asd_states_20261121.csv")}
    print("Test A: every committed ordinary input box must stay below the retained wall.")
    print("Test B: every committed affinity input box must stay above it.")
    boxes=[]
    for e in atoms:
        val,unc=aff[e["symbol"]]
        for k,t in enumerate(e["thresholds"]):
            y,dy=D(t["IE_eV"]),D(t["unc_eV"])
            z=y/val
            lo=(y-dy)/(val+unc)
            hi=(y+dy)/(val-unc)
            boxes.append((e["symbol"],k,z,lo,hi))
            val,unc=y,dy
    print("Maximum inside central:",max((z,s,k) for s,k,z,lo,hi in boxes if k))
    print("Maximum ordinary upper:",max((hi,s,k) for s,k,z,lo,hi in boxes if k))
    print("Minimum outside central:",min((z,s,k) for s,k,z,lo,hi in boxes if k==0))
    print("Minimum anion lower:",min((lo,s,k) for s,k,z,lo,hi in boxes if k==0))
    print("Direction can reach zero at a reported endpoint:",[(s,k) for s,k,z,lo,hi in boxes if lo<=1<=hi])
    for value in ("5","5.8","5.82","5.83","5.85","5.9","6"):
        c=D(value)
        disagree=[(s,k) for s,k,z,lo,hi in boxes if (z>c)!=(z>W)]
        ambiguous=[(s,k) for s,k,z,lo,hi in boxes if lo<=c<=hi]
        print("Pre-existing comparator", value, "central disagreements",disagree,"box touches cutoff",ambiguous)
    nd=atoms[-1]["thresholds"]
    A,da=aff["Nd"]
    pind=D(nd[0]["IE_eV"])
    dpind=D(nd[0]["unc_eV"])
    asd=state["60","0"]
    live=D(asd["NIST_energy_eV"])
    dlive=D(asd["NIST_unc_eV"])
    table=[]
    for source,I,dI in (("pinned Nd IE1",pind,dpind),("live Nd IE1 Miyabe 2024",live,dlive)):
        table.extend([variant(source+" / Fu 2020 Nd EA",A,da,I,dI),
                      variant(source+" / Fu 2020 Table IV Nd EA",D(".09749"),D(".00032"),I,dI),
                      variant(source+" / compiled converted Nd EA",D(".09749"),D(".00033"),I,dI),
                      variant("pinned Nd IE2 / "+source,I,dI,D(nd[1]["IE_eV"]),D(nd[1]["unc_eV"]))])
    pr=atoms[-2]["thresholds"][0]
    I,dI=D(pr["IE_eV"]),D(pr["unc_eV"])
    table.append(variant("Pr IE1 / Fu 2020 Pr EA",*aff["Pr"],I,dI))
    table.append(variant("Pr IE1 / Davis-Thompson 2001 Pr EA (superseded)",D(".926"),D(".024"),I,dI))
    print("Historical Pr EA threshold for a wall call (eV):",I/W)
    conversion=D("1.2398419843320026e-4")
    print("Nd conversion from 786.3(2.6) inverse cm (eV):",D("786.3")*conversion,"+/-",D("2.6")*conversion)
    with (folder/"source_variants.csv").open("w",newline="") as f:
        writer=csv.writer(f,lineterminator="\n")
        writer.writerow("variant,start_eV,unc_start_eV,end_eV,unc_end_eV,z,Gamma,z_lo,z_hi,wall_box".split(","))
        writer.writerows(table)
    if any(hi>=W for _,k,_,_,hi in boxes if k) or any(lo<=W for _,k,_,lo,_ in boxes if k==0):
        raise ValueError("Held classifications failed")
    if [(r[0],r[-1]) for r in table if r[-1]=="straddles"] != [(table[-1][0],"straddles")]:
        raise ValueError("Historical Pr sensitivity changed")


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive",type=Path)
    p.add_argument("--out",type=Path,default=DIR)
    a=p.parse_args()
    main(a.archive,a.out)
