"""Intrinsic path closure controls in the bcc and hcp embeddings, plus beta-Ta bond contrast."""
import csv
from decimal import Decimal as D
from pathlib import Path

HERE=Path(__file__).resolve().parent
cells={r["COD"]:r for r in csv.DictReader((HERE/"crystals.csv").open())}
# Fractions of conventional axes. The first and last coordinates agree in R^3.
bcc=[(0,0,0),(1,1,1),(2,0,0),(1,-1,-1),(0,0,0)] # halves
# A -> B(up) -> its nearest basal A -> vertically repeated B(down) -> A
hcp=[(0,0,0),(2,4,3),(0,6,0),(2,4,-3),(0,0,0)] # sixths; axes at 120 deg
with (HERE/"explicit_closed_paths.csv").open("w",newline="") as f:
    out=csv.writer(f,lineterminator="\n")
    out.writerow(["element","COD","graph","vertices_units","divisor","nominal_edge_A","closure","test"])
    for cod in ["9010998","9008501","1541266","9008558","9008512"]:
        r=cells[cod]
        a,c=D(r["a_A"]),D(r["c_A"])
        is_bcc=r["space_group"]=="I m -3 m"
        path,scale=(bcc,2) if is_bcc else (hcp,6)
        lengths=[]
        for left,right in zip(path,path[1:]):
            x,y,z=[D(v-u)/scale for u,v in zip(left,right)]
            lengths.append((a*a*(x*x+y*y-(0 if is_bcc else x*y))+c*c*z*z).sqrt())
        assert max(lengths)-min(lengths)<D("1e-24")
        assert abs(lengths[0]-D(r["shortest_A"]))<D(".000001")
        out.writerow([r["element"],cod,"bcc" if is_bcc else "hcp",
                      " ".join("/".join(map(str,u)) for u in path),scale,lengths[0],"zero translation",
                      "parallelogram" if is_bcc else "four-segment simple polygon"])
        print(r["element"],cod,path[0]==path[-1],lengths[0])
short,long,u=D("2.622"),D("2.687"),D("0.010")
contrast=(long-short)/(long+short)
bounds=( (long-u-(short+u))/(long-u+short+u),
         (long+u-(short-u))/(long+u+short-u))
print("Published 2002 beta-Ta principal channel lengths: normalized contrast and box",contrast,bounds)
