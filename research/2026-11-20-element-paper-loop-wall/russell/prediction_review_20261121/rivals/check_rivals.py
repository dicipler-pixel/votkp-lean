#!/usr/bin/env python3
"""Verify the finite-data no-go and distinguish the declared rival family by a new diagonal setting."""
import argparse
import csv
import gzip
import hashlib
import io
import itertools
import json
import math
import zipfile
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

SOURCE = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
CSV = "9f7b21e9eba6f76d0cbfa4ffcae65eeac7bf43cd6289bf3205432799ba8c3803"
W = 3 + 2 * math.sqrt(2)
FAMILIES = (0, 2, 10, 18, 36, 54)


def g(z):
    return (z - 1) / (z + 1)


def invert_g(gamma):
    return (1 + gamma) / (1 - gamma)


def sinh_half(z):
    return math.sinh(math.log(z) / 2)


def power_mean(a, b, p):
    return math.sqrt(a*b) if p == 0 else ((a**p + b**p)/2)**(1/p)


def cutoff_midpoints(lo, hi):
    return {
        "arithmetic_z": (lo+hi)/2,
        "geometric_z": math.sqrt(lo*hi),
        "harmonic_z": 2/(1/lo+1/hi),
        "arithmetic_gamma": invert_g((g(lo)+g(hi))/2),
        "arithmetic_gamma_squared": invert_g(math.sqrt((g(lo)**2+g(hi)**2)/2)),
        "geometric_sinh_half": math.exp(2*math.asinh(math.sqrt(sinh_half(lo)*sinh_half(hi)))),
    }


def mixed_scores(a, b, c):
    expo = math.log(W)/math.log(c)
    return {
        "quadrature": g(a)**2+g(b)**2-2*g(c)**2,
        "sinh_product": sinh_half(a)*sinh_half(b)-sinh_half(c)**2,
        "log_clock_gain": g(a**expo)**2+g(b**expo)**2-1,
        "asin_angle_sum": math.asin(g(a))+math.asin(g(b))-2*math.asin(g(c)),
    }


@dataclass(frozen=True)
class Face:
    symbol: str
    k: int
    core: int
    ratio: F
    low: F
    high: F
    has_width: bool
    outside: bool


def load_faces(record_zip, archive):
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == SOURCE
    with gzip.open(archive,"rt") as source:
        items = json.load(source,parse_float=F)["records"]
    with zipfile.ZipFile(record_zip) as source:
        table = source.read("H_to_At_thresholds.csv")
    assert hashlib.sha256(table).hexdigest() == CSV
    rows = list(csv.DictReader(io.StringIO(table.decode())))
    by_key = {(r["symbol"],int(r["k"])):r for r in rows}
    energy_matches = 0
    faces = []
    for r in rows:
        Z, sym, k = int(r["Z"]), r["symbol"], int(r["k"])
        if k > 0:
            entry = items[Z-1]["thresholds"][k-1]
            assert items[Z-1]["symbol"] == sym and entry["q"] == k-1
            assert F(r["energy_eV"]) == F(entry["IE_eV"])
            energy_matches += 1
        if not r["z"]:
            continue
        following = by_key[sym,k+1]
        first, second = F(r["energy_eV"]), F(following["energy_eV"])
        assert F(r["next_energy_eV"]) == second
        z = second/first
        has_width = bool(r["uncertainty_eV"] and following["uncertainty_eV"])
        if has_width:
            d1, d2 = F(r["uncertainty_eV"]), F(following["uncertainty_eV"])
            assert first > d1 and second > d2
            low,high = (second-d2)/(first+d1),(second+d2)/(first-d1)
            assert low <= z <= high
        else:
            low = high = z  # Unknown widths held fixed only for the explicit sensitivity exercise.
        side = 2*g(z)**2 > 1
        assert z > 1 and side == (r["central_wall"] == "outside")
        faces.append(Face(sym,k,0 if k==0 else Z-k,z,low,high,has_width,side))
    assert (energy_matches,len(faces),sum(f.has_width for f in faces)) == (3655,3637,3614)
    return faces


def exact_geometric_sides(a,b):
    return g(a)**2+g(b)**2 > 1


def path_warp(x, zl, zc, zh):
    l,c,h = (g(float(z)) for z in (zl,zc,zh))
    if x <= l or x >= h:
        return x
    if x <= c:
        return l+(g(W)-l)*(x-l)/(c-l)
    return g(W)+(h-g(W))*(x-c)/(h-c)


def main(options):
    faces = load_faces(options.tables,options.archive)
    inside,outside = ([f for f in faces if f.outside==state] for state in (False,True))
    L,H = max(f.ratio for f in inside), min(f.ratio for f in outside)
    c = (L+H)/2
    Lmin,Lmax = max(f.low for f in inside), max(f.high for f in inside)
    Hmin,Hmax = min(f.low for f in outside), min(f.high for f in outside)
    mid = cutoff_midpoints(float(L),float(H))
    mid_low = cutoff_midpoints(float(Lmin),float(Hmin))
    mid_high = cutoff_midpoints(float(Lmax),float(Hmax))
    get = {(f.symbol,f.k):f for f in faces}
    settings = {
        "Be_Rb": (get["Be",2],get["Rb",35]),
        "Si_Ag": (get["Si",0],get["Ag",0]),
    }
    options.out.mkdir(parents=True,exist_ok=True)
    with (options.out/"rival_boxes.csv").open("w") as stream:
        writer = csv.writer(stream,lineterminator="\n")
        writer.writerow(["setting","midpoint","extension","cutoff","cutoff_low","cutoff_high",
                         "score","score_low","score_high","rival_call_on_box"])
        stability = {}
        for setting,(A,B) in settings.items():
            calls=[]
            for name,center in mid.items():
                lo,hi = mid_low[name],mid_high[name]
                # All four scores increase with each forward input and decrease with c.
                midscores = mixed_scores(float(A.ratio),float(B.ratio),center)
                lows = mixed_scores(float(A.low),float(B.low),hi)
                highs = mixed_scores(float(A.high),float(B.high),lo)
                for ext,value in midscores.items():
                    # The Si/Ag midpoint and Si/Ag inputs share measured quantities.
                    # Independent rectangular bounding is conservative. The gamma² tie is exact.
                    if setting=="Si_Ag" and name=="arithmetic_gamma_squared" and ext=="quadrature":
                        value=lows[ext]=highs[ext]=0.
                    call = "open" if lows[ext]>0 else "closed" if highs[ext]<0 else "ideal" if lows[ext]==highs[ext]==0 else "unresolved"
                    calls.append(call)
                    writer.writerow([setting,name,ext,center,lo,hi,value,lows[ext],highs[ext],call])
            stability[setting]={s:calls.count(s) for s in sorted(set(calls))}
    A,B=settings["Be_Rb"]
    m,n = g(A.ratio),g(B.ratio)
    t = 2*g(c)**2
    lam = (t-m**2-n**2)/(m-n)**2
    lo,hi=2.,3.
    for _ in range(70):
        p=(lo+hi)/2
        if power_mean(float(m),float(n),p)>g(float(c)):
            hi=p
        else:
            lo=p
    # The uncalibrated coupling perturbation lambda changes no equal-face test.
    assert 0<lam<F(1,40)
    assert m*m+n*n+F(1,40)*(m-n)**2>t
    assert power_mean(float(m),float(n),2.)<g(float(c))<power_mean(float(m),float(n),2.05)

    # Exact implementation of the finite-support no-go. All inputs lie where the warp is identity.
    assert all(f.ratio<=L or f.ratio>=H for f in faces)
    assert g(float(c))!=g(W) and abs(path_warp(g(float(c)),L,c,H)-g(W))<1e-15
    assert all(path_warp(g(float(f.ratio)),L,c,H)==g(float(f.ratio)) for f in faces)
    family_sets = [[f for f in faces if f.core==n] for n in FAMILIES]
    pair_count=sum(math.comb(len(fs),2) for fs in family_sets)
    disagreements=[]
    for fs in family_sets:
        for x,y in itertools.combinations(fs,2):
            S=g(x.ratio)**2+g(y.ratio)**2
            if (S>1)!=(S>t):
                assert x.low>=1 and y.low>=1 and exact_geometric_sides(x.low,y.low)
                disagreements.append((x.symbol,y.symbol))
    assert pair_count==12241 and set(disagreements)=={("Si","Ag"),("Be","Rb")}

    # Exact positive-rational engineered diagonal, plus enclosing margin for changed cutoffs.
    target=F(35,6)
    assert g(target)==F(29,41) and 2*g(target)**2==F(1682,1681)
    trace=2-4*((target-1)**2/(4*target))**2
    assert trace==F(-354481,176400)
    assert W<5.832<float(target)<5.835<min(mid_low.values())
    # The first proposed interval contains no lower-denominator ratio.
    assert not any(W<n/d<min(mid_low.values()) for d in range(1,6) for n in range(5*d,6*d+1))
    fitbox = [min(mid_low.values()),max(mid_high.values())]
    print("3,655 IE matched; 3,637 numeric faces; 3,614 complete rectangles")
    print("L, H, c:",*[f"{float(q):.12f}" for q in (L,H,c)])
    print("6 midpoint rules, extrema of calibration boxes:",*[f"{v:.12f}" for v in fitbox])
    print("6 x 4 calls using marginal boxes:",stability)
    print("Be-Rb first positive lambda to reach midpoint wall:",f"{float(lam):.12f}", "p*:",f"{p:.12f}")
    print("All",pair_count,"same-family pairs scanned; two shifted-quadrature disagreements:",disagreements)
    print("Warp fixes every one of",len(faces),"observed reflections; all cross-pairs fixed by construction")
    print("Diagonal z:",target,"power:",2*g(target)**2,"trace:",trace,"class stable on [5.832, 5.835]")


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tables",type=Path,help="Russell_Peel_Wall_Prediction_Record.zip")
    parser.add_argument("archive",type=Path,help="pinned element_thresholds_20261011.json.gz")
    parser.add_argument("out",type=Path)
    main(parser.parse_args())
