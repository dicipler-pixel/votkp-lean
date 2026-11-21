"""Independent exact checker for stored archive, chemistry and ASD comparisons. Stdlib only."""
import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

DIR = Path(__file__).resolve().parent
DIGEST = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"


def keyed(path, fields):
    with path.open() as f:
        src = list(csv.DictReader(f))
    keyed_rows = {tuple(int(r[k]) for k in fields): r for r in src}
    if len(src) != len(keyed_rows):
        raise ValueError(f"Duplicate rows in {path}")
    return keyed_rows


def test(condition, context):
    if not condition:
        raise ValueError(context)


def rounded(x, places):
    n, d = x.numerator, x.denominator
    magnitude, r = divmod(abs(n)*10**places, d)
    magnitude += 2*r >= d
    s = "-" if n < 0 else ""
    return f"{s}{magnitude // 10**places}.{magnitude % 10**places:0{places}d}"


def classify(x, y):
    return "outside" if 2*(y-x)**2 > (x+y)**2 else "inside" if 2*(y-x)**2 < (x+y)**2 else "on"


def verify(path, folder):
    test(hashlib.sha256(path.read_bytes()).hexdigest() == DIGEST, "Archive digest failed")
    with gzip.open(path, "rt") as f:
        elements = json.load(f, parse_float=Decimal)["records"][55:60]
    ladder=keyed(folder/"batch12_ba_nd.csv",("Z","k"))
    detail=keyed(folder/"rungs_detailed.csv",("Z","k"))
    chem=keyed(folder/"anion_chemistry.csv",("Z",))
    public=keyed(DIR/"asd_states_20261121.csv",("Z","q"))
    affinities=keyed(DIR/"affinities.csv",("Z",))
    energy_keys = {(z,q) for z in range(56,61) for q in range(z)}
    test(public.keys()==energy_keys==detail.keys(),"Threshold, detail or public key mismatch")
    test(ladder.keys()==energy_keys|{(z,z) for z in range(56,61)},"Ladder keys differ")
    differences, grades, sides, maxordinary = [], Counter(), Counter(), []
    complete = 0
    fieldmatches = Counter()
    for e in elements:
        z,sym = e["Z"], e["symbol"]
        a = affinities[z,]
        x, dx, grade, ref = F(a["EA_eV"]),F(a["unc_eV"]),"EA22",a["source"]
        for k,t in enumerate(e["thresholds"]):
            key=(z,k)
            row=ladder[key]
            d=detail[key]
            y,dy = F(t["IE_eV"]), F(t["unc_eV"]) if t["unc_eV"] is not None else None
            asd=public[key]
            text=asd["NIST_energy_eV"]
            live=(F(text.strip("()[]")),F(asd["NIST_unc_eV"]) if asd["NIST_unc_eV"] else None,
                  {"(":"T","[":"S"}.get(text[0],"E"),asd["NIST_refs"])
            pinned=(y,dy,t["grade"],t["references"])
            diffs=[i for i in range(4) if live[i]!=pinned[i]]
            labels=("energy","uncertainty","grade","reference")
            fieldmatches.update(labels[i] for i in range(4) if i not in diffs)
            if diffs:
                differences.append((sym,k+1,tuple(labels[i] for i in diffs),pinned,live))
            ratio=y/x
            gamma=(ratio-1)/(ratio+1)
            wall=classify(x,y)
            test((row["symbol"],F(row["IE_k (eV)"]),row["source"])==(sym,x,grade),("base", key))
            test((row["z_k"],row["Gamma_k"])==(rounded(ratio,6),rounded(gamma,6)),("rounded",key))
            test((F(d["E_start_eV"]),F(d["E_end_eV"]),d["start_ref"],d["end_ref"])==
                 (x,y,ref,t["references"]),("detailed input",key))
            test((d["start_grade"],d["end_grade"])==(grade,t["grade"]),("grade",key))
            test((F(d["unc_start_eV"]) if d["unc_start_eV"] else None,
                  F(d["unc_end_eV"]) if d["unc_end_eV"] else None)==(dx,dy),
                 ("detailed uncertainties",key))
            test((d["z"],d["Gamma"])==(rounded(ratio,10),rounded(gamma,10)),("detail ratio",key))
            test(d["wall"]==wall,("wall",key))
            sides[k==0,wall]+=1
            grades[t["grade"]]+=1
            if dx is not None and dy is not None:
                lower,upper=(y-dy)/(x+dx),(y+dy)/(x-dx)
                test((d["z_lo"],d["z_hi"])==(rounded(lower,9),rounded(upper,9)),("box",key))
                test(lower>=1 and classify(F(1),lower)==wall==classify(F(1),upper)==d["box_wall"],
                     ("box wall or positivity failure",key))
                complete+=1
            if k==0:
                c=chem[z,]
                eta,chi=(y-x)/2,(y+x)/2
                w=chi**2/(2*eta)
                test((F(c["eta_eV"]),F(c["chi_eV"]))==(eta,chi),("chem inputs",key))
                test((c["omega_eV"],c["omega_over_eta"])==(rounded(w,10),rounded(w/eta,10)),
                     ("chem derived",key))
                test(w/eta == 1/(2*gamma**2),("chem identity",key))
                test(wall==("outside" if w<eta else "inside" if w>eta else "on"),("chem wall",key))
            if k:
                maxordinary.append((ratio,sym,k))
            x,dx,grade,ref=y,dy,t["grade"],t["references"]
        end=ladder[z,z]
        test((end["symbol"],F(end["IE_k (eV)"]),end["source"],end["z_k"],end["Gamma_k"])==
             (sym,x,grade,"",""),("final threshold",z))
    print("Archive SHA-256:",DIGEST)
    print(f"Serialized rows: {len(ladder)}. Archive energy matches: {len(public)}. Sources preserved.")
    print("Six-place z and Gamma independently rounded from exact fractions:",dict(sides))
    print("Endpoint boxes complete and classifications stable:",complete)
    print("Archive threshold grades:",dict(grades))
    print("Fresh ASD field matches of",len(public),":",dict(fieldmatches))
    print("Public ASD differing rows:",len(differences))
    for sym,k,labels,pinned,live in differences:
        print(f"  {sym} IE_{k}, changed {', '.join(labels)}: {pinned} -> {live}")
    print("Maximum ordinary ratio:",maxordinary and max(maxordinary))
    print("Ladder SHA-256:",hashlib.sha256((folder/"batch12_ba_nd.csv").read_bytes()).hexdigest())
    # Freeze the independently observed revision; an amended snapshot requires renewed conclusions.
    test([(s,k,labels) for s,k,labels,_,_ in differences]==[("Nd",1,("energy","uncertainty","reference"))],
         "Fresh ASD-vs-archive differences changed")


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive",type=Path)
    parser.add_argument("--folder",type=Path,default=DIR)
    args=parser.parse_args()
    verify(args.archive,args.folder)
