"""Find exact feasible forward cutoffs using reported independent input boxes."""
import argparse
import csv
import gzip
import itertools
import hashlib
import json
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

DIGEST="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
WAVENUMBER=F("6.62607015e-34")*299792458*100/F("1.602176634e-19")


@dataclass(frozen=True)
class Rung:
    symbol: str
    k: int
    ratio: F
    outside: bool
    lower: F | None
    upper: F | None


def make_rung(symbol, k, x, y, u, v):
    r = y/x
    if r <= 1: raise ValueError(f"non-forward central rung {symbol} {k}")
    label = 2*(y-x)**2 > (y+x)**2
    lo=hi=None
    if u is not None and v is not None:
        if x<=u or y<=v: raise ValueError("nonpositive interval endpoint")
        lo,hi=(y-v)/(x+u),(y+v)/(x-u)
    return Rung(symbol,k,r,label,lo,hi)


def extrema(rows,uncertain):
    good=[r for r in rows if not uncertain or r.upper is not None]
    left=max((r.upper if uncertain else r.ratio,r.symbol,r.k) for r in good if not r.outside)
    right=min((r.lower if uncertain else r.ratio,r.symbol,r.k) for r in good if r.outside)
    return left,right


def mismatches(rows,c):
    return [(r.symbol,r.k) for r in rows if (r.ratio>c)!=r.outside]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive",type=Path)
    p.add_argument("--affinities",type=Path,default=Path(__file__).with_name("affinities_h_sn.csv"))
    p.add_argument("--missing",type=Path,default=Path("cutoff_missing_boxes.csv"))
    args=p.parse_args()
    if hashlib.sha256(args.archive.read_bytes()).hexdigest()!=DIGEST:raise ValueError("wrong archive")
    with gzip.open(args.archive,"rt",encoding="utf-8") as f: records=json.load(f,parse_float=Decimal)["records"][:50]
    with args.affinities.open(encoding="utf-8",newline="") as f: aff=list(csv.DictReader(f))
    rows=[]
    silicon_inputs=None
    for atom, ea in zip(records,aff,strict=True):
        symbol=atom["symbol"]
        if atom["Z"]!=int(ea["Z"]) or symbol!=ea["symbol"]:raise ValueError("wrong affinity key")
        levels=[(F(t["IE_eV"]),F(t["unc_eV"]) if t["unc_eV"] is not None else None) for t in atom["thresholds"]]
        for k,((x,u),(y,v)) in enumerate(zip(levels,levels[1:]),1):
            rows.append(make_rung(symbol,k,x,y,u,v))
        if ea["status"]=="unbound":continue
        scale=WAVENUMBER if ea["source"]=="Se26_cm-1" else F(1)
        x=F(ea["EA_source_units"])*scale
        u=F(ea["unc_source_units"])*scale if ea["unc_source_units"] else None
        y,v=levels[0]
        rows.append(make_rung(symbol,0,x,y,u,v))
        if symbol=="Si":silicon_inputs=y,v
    known=[r for r in rows if r.lower is not None]
    missing=[r for r in rows if r.lower is None]
    print(f"Central rows {len(rows)} ({sum(r.k>0 for r in rows)} ordinary, {sum(r.k==0 for r in rows)} anion). "
          f"Outside {sum(r.outside for r in rows)}; complete uncertainty boxes {len(known)}; unavailable {len(missing)}.")
    with args.missing.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f,lineterminator="\n");w.writerow(["element","k","central_z","central_wall"])
        w.writerows((r.symbol,r.k,f"{float(r.ratio):.9f}","outside" if r.outside else "inside") for r in missing)
    # Independent two-sided control: these boxes never meet the reverse wall.
    if any(r.lower < F(1,2) for r in known): raise ValueError("lower wall needs separate investigation")
    for index,subset in [("ordinary",[r for r in rows if r.k>0]),("all",rows)]:
        for uncertain in [False,True]:
            left,right=extrema(subset,uncertain)
            label="reported-box" if uncertain else "central"
            print(f"{index} {label}: [{left[0]} ({float(left[0]):.12f}, {left[1]} k={left[2]}), "
                  f"{right[0]} ({float(right[0]):.12f}, {right[1]} k={right[2]}))")
            if left[0]>=right[0]:raise ValueError("empty equivalence interval")
            # Compare direct polynomial wall to endpoint labels throughout each complete box.
            if uncertain:
                for r in subset:
                    if r.lower is None:continue
                    for endpoint in (r.lower,r.upper):
                        if (endpoint**2-6*endpoint+1>0)!=r.outside:
                            raise ValueError("reference wall straddled")
                        # c=L is allowed, c=U is not. Check interior and left endpoint.
                        if any((endpoint>cut)!=r.outside for cut in [left[0],(left[0]+right[0])/2]):
                            raise ValueError("endpoint equivalence control failed")
                if not any(r.lower==right[0] and r.outside for r in subset):raise ValueError("right boundary witness missing")
    print("Alternative scalar thresholds: disagreement lists vs the loop wall on all central inputs")
    for c in map(F,["5","5.8","5.82","5.83","5.85","5.9","6"]):
        bad=mismatches(rows,c)
        print(f"{c}  {len(bad)}: {bad}")
        for r in rows:
            # Independent check in energy-ratio form AND Gamma coordinates; no sqrt.
            g=(r.ratio-1)/(r.ratio+1)
            if (g>(c-1)/(c+1))!=(r.ratio>c):raise ValueError("Gamma control disagrees")
            if (2*g*g>1)!=r.outside:raise ValueError("Gamma wall disagrees")
    below=max((r.ratio,r.symbol,r.k) for r in rows if r.ratio<F(5))
    above=min((r.ratio,r.symbol,r.k) for r in rows if r.ratio>F(5))
    print(f"Nearest central ratios bracketing five: {below[1]} k={below[2]} {float(below[0]):.12f}; "
          f"{above[1]} k={above[2]} {float(above[0]):.12f}")
    print("Optional sensitivity assuming all intervening true IEs are increasing (no invented error bars):")
    for atom in records:
        a=atom["thresholds"]
        for unknown,indices in itertools.groupby(range(len(a)),lambda i:a[i]["unc_eV"] is None):
            block=list(indices)
            if not unknown:continue
            i,j=block[0]-1,block[-1]+1
            if i<0 or j>=len(a):continue
            low=F(a[i]["IE_eV"])-F(a[i]["unc_eV"])
            high=F(a[j]["IE_eV"])+F(a[j]["unc_eV"])
            print(f"{atom['name']} IE {block[0]+1}..{block[-1]+1}: adjacent z <= "
                  f"{float(high/low):.12f} conditional on ordering.")
    for name,k in [("Ne",8),("Ag",0),("Si",0)]:
        r=next(z for z in rows if z.symbol==name and z.k==k)
        print(f"{name} k={k}: z={float(r.ratio):.12f} "
              f"[{float(r.lower):.12f}, {float(r.upper):.12f}], "
              f"Gamma={float((r.ratio-1)/(r.ratio+1)):.12f}")
    if len(mismatches(rows,F("5.83")))!=0 or ("Ag",0) not in mismatches(rows,F("5.8")):
        raise ValueError("negative control no longer reproduces")
    # The pinned IE is elemental: these are EA substitution checks, not isotope-resolved IE determinations.
    y,v=silicon_inputs
    for isotope,x,u in [(28,"1.38952201",".00000017"),(29,"1.38952172",".00000012"),(30,"1.38952078",".00000012")]:
        alt=make_rung("Si",0,F(x),y,F(u),v)
        subset=[alt if (r.symbol,r.k)==("Si",0) else r for r in rows]
        print(f"Silicon-{isotope} alternate EA, elemental IE retained: "
              f"z={float(alt.ratio):.12f}, guaranteed upper endpoint "
              f"{float(extrema(subset,True)[1][0]):.12f} (exclusive).")


if __name__=="__main__":
    main()
