"""Retrospective, fixed-window tests of VOTKP log-step shape on H–Rh.

Usage: python3 test_ladder_shape.py /path/to/element_thresholds_20261011.json.gz output_dir
No external packages or network calls.
"""
import argparse
import csv
import gzip
import hashlib
import itertools
import json
import math
import random
import statistics
from dataclasses import dataclass
from pathlib import Path

PIN = "182da01a14b10ce1e07e247565466d01822121c5"
DIGEST = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
CELLS = (10,18,36)      # Closed Ne, Ar and Kr core positions (all support four outgoing rungs)
OFFSETS = (0,1,2)       # This many electrons above the respective closed core
CHARGES = tuple(range(8))
SHUFFLES = 999
SEED = 20261121


@dataclass(frozen=True)
class Window:
    core: int
    offset: int
    charge: int
    z: int
    span: float
    shares: tuple


def composition(levels):
    steps = [math.log(y/x) for x,y in zip(levels,levels[1:])]
    span = math.log(levels[-1]/levels[0])
    if abs(math.fsum(steps)-span)>2e-13:
        raise ValueError("telescoping control failed")
    total_variation = math.fsum(map(abs,steps))
    return span, tuple(x/total_variation for x in steps) if steps else ()


def tv(a,b):
    """Half the L1 difference between two ordered probability vectors."""
    if len(a) != len(b):
        raise ValueError("matched window lengths required")
    return 0.5*math.fsum(abs(x-y) for x,y in zip(a,b))


def dims(row,mode):
    if mode == "endpoint":
        return (row.span,)
    if mode == "first_two_contrast":
        return (row.shares[0]-row.shares[1],)
    if mode == "first_two":
        return row.shares[:2]
    if mode == "sorted":
        return tuple(sorted(row.shares,reverse=True))
    return row.shares


def nearest_centroid(windows,mode):
    output = {}
    for core in CELLS:
        train = [w for w in windows if w.core != core]
        # A held-out fold drops overlapping chemical elements for this prediction too.
        for case in (w for w in windows if w.core == core):
            reference = [w for w in train if w.z != case.z]
            distances = []
            for label in OFFSETS:
                vectors = [dims(w,mode) for w in reference if w.offset == label]
                center = tuple(map(statistics.fmean,zip(*vectors)))
                distances.append(sum(abs(x-y) for x,y in zip(dims(case,mode),center)))
            # Equal distances resolve by the smaller offset, independently of true label.
            output[core,case.offset,case.charge] = distances.index(min(distances))
    return output


def scores(predictions):
    return tuple(sum(predictions[k]==k[1] for k in predictions if k[0]==c) for c in CELLS)


def shuffled_shape_control(windows):
    # Optimize repeated nearest-centroid fits: training membership is fixed by core,Z.
    # Order randomization is independent per unique four-rung window, preserving its span
    # and its exact multiset of shares. Each trial reruns both training and prediction.
    n=len(windows)
    training = []
    for case in windows:
        training.append([[j for j,w in enumerate(windows)
                          if w.core!=case.core and w.z!=case.z and w.offset==label] for label in OFFSETS])
    rng=random.Random(SEED)
    perms=list(itertools.permutations(range(4)))
    totals=[]
    for _ in range(SHUFFLES):
        vectors=[tuple(w.shares[i] for i in rng.choice(perms)) for w in windows]
        # Centroids can be reused across cases with identical training indices.
        cache={}
        correct=0
        for i,(w, groups) in enumerate(zip(windows,training)):
            candidate=[]
            for group in groups:
                key=tuple(group)
                if key not in cache:
                    cache[key]=tuple(math.fsum(vectors[j][d] for j in group)/len(group) for d in range(4))
                candidate.append(sum(abs(a-b) for a,b in zip(vectors[i],cache[key])))
            correct+=candidate.index(min(candidate))==w.offset
        totals.append(correct)
    return sorted(totals)


def write(path,columns,records):
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f,lineterminator="\n");w.writerow(columns)
        for row in records:
            w.writerow([format(x,".9g") if isinstance(x,float) else x for x in row])


def group_period(z):
    if z<3:return (1,1 if z==1 else 18)
    if z<=10:return (2, (1,2,13,14,15,16,17,18)[z-3])
    if z<=18:return (3, (1,2,13,14,15,16,17,18)[z-11])
    if z<=36:return (4,z-18)
    return (5,z-36)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive",type=Path)
    parser.add_argument("output",type=Path)
    args=parser.parse_args()
    if hashlib.sha256(args.archive.read_bytes()).hexdigest()!=DIGEST:
        raise ValueError("archive mismatch")
    with gzip.open(args.archive,"rt",encoding="utf-8") as file:
        source=json.load(file)["records"][:45]
    data={r["Z"]:[t["IE_eV"] for t in r["thresholds"]] for r in source}
    symbols={r["Z"]:r["symbol"] for r in source}
    if set(data)!=set(range(1,46)) or any(len(a)!=z for z,a in data.items()):
        raise ValueError("unexpected coverage")
    args.output.mkdir(parents=True,exist_ok=True)
    full=[]
    for z,a in data.items():
        span,s=composition(a)
        rev_span,reversed_s=composition(a[::-1])
        if abs(rev_span+span)>1e-12 or any(abs(x+y)>1e-12 for x,y in zip(reversed_s,reversed(s))):
            raise ValueError("directed reversal law failed")
        for k,x in enumerate(s,1):
            full.append([z,symbols[z],k,math.log(a[k]/a[k-1]),span,x,
                         (x-s[-k])/2,(x+s[-k])/2])
    write(args.output/"neutral_log_shares.csv",["Z","symbol","k","log_step","log_total","directed_share",
          "reversal_even","reversal_odd"],full)
    print(f"Input pin {PIN}. {len(full)} ordinary steps H–Rh; H has no ordinary ratio.")
    windows=[]
    for core,offset,charge in itertools.product(CELLS,OFFSETS,CHARGES):
        z=core+offset+charge
        a=data[z][charge:charge+5]   # five consecutive removal energies of ion q+
        if len(a)!=5:raise ValueError("incomplete fixed window")
        span,s=composition(a)
        windows.append(Window(core,offset,charge,z,span,s))
    predictions={mode:nearest_centroid(windows,mode) for mode in ("endpoint","sorted","first_two_contrast","first_two","ordered")}
    results=[]
    for w in windows:
        key=(w.core,w.offset,w.charge)
        results.append([w.core,w.offset,w.charge,w.z,symbols[w.z],w.span,*w.shares,
                        *(predictions[mode][key] for mode in predictions)])
    write(args.output/"matched_charge_windows.csv",["core_electrons","extra_electrons","ion_charge","Z",
          "symbol","log_span","p1","p2","p3","p4","guess_span","guess_sorted","guess_contrast","guess_first_two","guess_ordered"],results)
    print("Leave-one-core-out, equal ion charges 0–7, held-out element removed, 24 cases/core:")
    for mode,pred in predictions.items():
        values=scores(pred);print(f"{mode}: {values}, {sum(values)}/{len(windows)}")
    # Interval propagation (outward mathematical bound; floating reporting at 9 digits).
    # Four distinct energy entries enter the first-two contrast. Errors on the fourth
    # energy cancel identically. Class centroid boundaries are held at their fitted
    # central values; we vary inputs to each test window only.
    uncertainty=[]
    for w in windows:
        q=w.charge
        t=source[w.z-1]["thresholds"]
        ref=[v for v in windows if v.core!=w.core and v.z!=w.z]
        centers={o:statistics.fmean(v.shares[0]-v.shares[1] for v in ref if v.offset==o) for o in OFFSETS}
        cut_neg=(centers[2]+centers[0])/2;cut_pos=(centers[0]+centers[1])/2
        bound_lo,bound_hi={2:(float("-inf"),cut_neg),0:(cut_neg,cut_pos),1:(cut_pos,float("inf"))}[w.offset]
        row=[w.core,w.offset,w.charge,w.z,w.shares[0]-w.shares[1],cut_neg,cut_pos]
        used=[t[q+j] for j in (0,1,2,4)]
        if any(v["unc_eV"] is None for v in used):
            uncertainty.append(row+["","","missing input uncertainty"])
            continue
        (a,b,c,e)=[(v["IE_eV"]-v["unc_eV"],v["IE_eV"]+v["unc_eV"]) for v in used]
        num=(math.log(b[0]**2/(a[1]*c[1])),math.log(b[1]**2/(a[0]*c[0])))
        den=(math.log(e[0]/a[1]),math.log(e[1]/a[0]))
        if den[0]<=0: raise ValueError("denominator range is not positive")
        endpoints=[i/j for i in num for j in den]
        lower,upper=min(endpoints),max(endpoints)
        uncertainty.append(row+[lower,upper,"same class" if bound_lo<lower<=upper<bound_hi else "crosses a decision boundary"])
    write(args.output/"contrast_uncertainty.csv",["core_electrons","extra_electrons","q","Z","D","cut_low",
          "cut_high","D_interval_lo","D_interval_hi","fixed_classifier"],uncertainty)
    from collections import Counter
    print("Conservative test-input boxes, fixed central training centroids:",dict(Counter(r[-1] for r in uncertainty)))
    null=shuffled_shape_control(windows)
    obs=sum(scores(predictions["ordered"]))
    print(f"Endpoint-preserving order reshuffles: {SHUFFLES}, seed={SEED}, "
          f"range={null[0]}..{null[-1]}, median={statistics.median(null)}, "
          f"central 95% empirical ranks={null[24]}..{null[974]}, >=observed {sum(n>=obs for n in null)}.")
    # Preserve all within-core covariation and overlapping-window dependence in feature
    # space. Test all relative registrations, keeping Ne fixed to remove the redundant
    # globally shared permutation (L1 is invariant to a common permutation).
    perms=list(itertools.permutations(range(4)))
    grouped=[]
    for Ar,Kr in itertools.product(perms, repeat=2):
        orders={10:perms[0],18:Ar,36:Kr}
        alternate=[Window(w.core,w.offset,w.charge,w.z,w.span,tuple(w.shares[i] for i in orders[w.core]))
                   for w in windows]
        grouped.append(sum(scores(nearest_centroid(alternate,"ordered"))))
    print(f"All {len(grouped)} relative whole-core shell registrations: "
          f"range={min(grouped)}..{max(grouped)}, median={statistics.median(grouped)}, "
          f">=observed {sum(n>=obs for n in grouped)} (includes identity).")
    # Each electron count has the same eight ion charges and four ordinary steps.
    # Vary Z at fixed electron count to probe the isoelectronic change in profile.
    continuation=[]
    for electrons in range(5,39):
        profiles=[composition(data[electrons+q][q:q+5]) for q in CHARGES]
        nearby=[(a,b) for a,b in itertools.combinations(CHARGES,2) if b-a==1]
        distant=[(a,b) for a,b in itertools.combinations(CHARGES,2) if b-a>=5]
        def mean_d(pairs,shape):
            if shape:
                return statistics.fmean(tv(profiles[a][1],profiles[b][1]) for a,b in pairs)
            return statistics.fmean(abs(profiles[a][0]-profiles[b][0]) for a,b in pairs)
        continuation.append([electrons,symbols[electrons],symbols[electrons+7],
                             mean_d(nearby,True),mean_d(distant,True),
                             mean_d(nearby,False),mean_d(distant,False)])
    write(args.output/"isoelectronic_continuity.csv",["electron_count","neutral_start","charge7_element",
          "adjacent_mean_TV","far_mean_TV","adjacent_mean_abs_logspan_change","far_mean_abs_logspan_change"],
          continuation)
    print(f"Isoelectronic continuation, q=0..7: adjacent/far mean TV smaller in "
          f"{sum(r[3]<r[4] for r in continuation)}/{len(continuation)} electron counts; "
          f"analogous endpoint effect {sum(r[5]<r[6] for r in continuation)}/{len(continuation)}.")
    # Candidate groups shared between successive periods; every input is four initial
    # steps, irrespective of its actual neutral ladder length. Restrict to same block
    # family when comparing d-block or main-group atoms.
    neutral={z:composition(a[:5]) for z,a in data.items() if len(a)>=5}
    groups=dict((group_period(z),z) for z in neutral)
    neutral_results=[]
    for z,(span,s) in neutral.items():
        per,group=group_period(z)
        if (per-1,group) not in groups:continue
        is_d=3<=group<=12
        candidates=[g for (pp,g) in groups if pp==per-1 and (per,g) in groups and (3<=g<=12)==is_d]
        if len(candidates)<2:continue
        by_span=sorted((abs(span-neutral[groups[per-1,g]][0]),g) for g in candidates)
        by_shape=sorted((tv(s,neutral[groups[per-1,g]][1]),g) for g in candidates)
        homolog=groups[per-1,group]
        neutral_results.append([z,symbols[z],group,per,symbols[homolog],len(candidates),
                                next(d for d,g in by_shape if g==group),
                                next(i for i,(_,g) in enumerate(by_shape,1) if g==group),
                                next(i for i,(_,g) in enumerate(by_span,1) if g==group),
                                symbols[groups[per-1,by_shape[0][1]]],symbols[groups[per-1,by_span[0][1]]]])
    write(args.output/"neutral_column_controls.csv",["Z","element","group","period","homolog","candidates",
          "same_group_TV","shape_rank","span_rank","closest_shape","closest_span"],neutral_results)
    for p in (3,4,5):
        cases=[r for r in neutral_results if r[3]==p]
        print(f"Period {p} neutral retrieval: ordered top-1 {sum(r[7]==1 for r in cases)}/{len(cases)}, "
              f"span top-1 {sum(r[8]==1 for r in cases)}/{len(cases)}, "
              f"chance expectation {sum(1/r[5] for r in cases):.3f}.")
    print("Control: an exact geometric ladder (ratio two) has uniform shares, so permuting steps leaves the fingerprint unchanged.")
    if composition([1,2,4,8,16])[1]!=(0.25,)*4: raise ValueError("flat control failed")


if __name__=="__main__":
    main()
