"""Exact extremal directed edge counts over a half-filling uncertainty shell."""
from itertools import combinations
import csv
import gzip
import json
import sys

import numpy as np

from rank_flow import CUBIC_STEPS, TIE_WIDTH_EV, TRANSPORT, band_grid, interval_counts


def merge(ranges, key, low, high):
    if key in ranges:
        prior_low, prior_high = ranges[key]
        low, high = min(low, prior_low), max(high, prior_high)
    ranges[key] = (low, high)


def cycle_bounds(labels):
    """Map number of selected ambiguous vertices to min/max 1→0 charged edges."""
    # 0 and 1 are fixed; 2 means the vertex is free.
    free = labels == 2
    if not free.any():
        outgoing = int(np.sum((labels == 1) & (np.roll(labels, -1) == 0)))
        return {0:(outgoing,outgoing)}
    allowed = ((0,), (1,), (0,1))
    result = {}
    for start in allowed[labels[0]]:
        states = {(start if free[0] else 0, start):(0,0)}
        for label in labels[1:]:
            updated = {}
            for (selected, previous), (low,high) in states.items():
                for value in allowed[label]:
                    new_count = selected + (value if label == 2 else 0)
                    transition = int(previous == 1 and value == 0)
                    merge(updated, (new_count,value), low+transition, high+transition)
            states = updated
        for (selected,last), (low,high) in states.items():
            closure = int(last == 1 and start == 0)
            merge(result, selected, low+closure, high+closure)
    return result


def exact_counts(labels, shift, selected):
    mesh = len(labels)
    order = np.arange(labels.size).reshape(labels.shape)
    successors = np.roll(order, -shift, axis=(0,1,2)).ravel()
    content = labels.ravel()
    seen = np.zeros(len(content),dtype=bool)
    fixed_total = 0
    ranges = {0:(0,0)}
    for seed in range(len(content)):
        if seen[seed]:
            continue
        cycle = []
        i = seed
        while not seen[i]:
            seen[i] = True
            cycle.append(content[i])
            i = successors[i]
        if i != seed:
            raise AssertionError("reciprocal step is not a permutation")
        partial = cycle_bounds(np.array(cycle))
        if len(partial) == 1:
            fixed_total += partial[0][0]
            continue
        updated = {}
        for left, (left_lo,left_hi) in ranges.items():
            for right, (right_lo,right_hi) in partial.items():
                if left + right <= selected:
                    merge(updated,left+right,left_lo+right_lo,left_hi+right_hi)
        ranges = updated
    lo,hi = ranges[selected]
    return fixed_total+lo,fixed_total+hi


def brute_checks():
    rng = np.random.default_rng(52009)
    for n in (2,3,4):
        for _ in range(6):
            labels = rng.integers(0,2,size=(n,n,n))
            chosen = rng.choice(labels.size,size=min(7,labels.size),replace=False)
            labels.flat[chosen] = 2
            selected = len(chosen)//2
            for step in ((1,0,0),(1,1,1),(2,0,0)):
                shift = np.array(step)
                extrema = []
                for fill in combinations(chosen,selected):
                    occ = labels == 1
                    occ.flat[list(fill)] = True
                    extrema.append(int(np.sum(occ & ~np.roll(occ,-shift,axis=(0,1,2)))))
                if exact_counts(labels,shift,selected) != (min(extrema),max(extrema)):
                    raise AssertionError("failed brute-force control")


def main():
    brute_checks()
    writer = csv.writer(sys.stdout,lineterminator="\n")
    writer.writerow(("geometry","QE_mesh","hkl","q_invA","num_occ","shell_size","shell_filled",
                     "simple_min","exact_min","exact_max","simple_max",
                     "L_lower_A2","rank_term_upper_A2","qL_lower_A","qLrank_upper_A"))
    for geometry, file in (("297K","Rb_band_inputs.json.gz"),("5K","Rb_cold_band_inputs.json.gz")):
        records=json.loads(gzip.decompress((TRANSPORT/file).read_bytes()))
        for n in sorted(map(int,records)):
            inp=records[str(n)]
            bands,reciprocal,_,_=band_grid(inp)
            band=bands[...,4]
            half=band.size//2
            for hkl in CUBIC_STEPS:
                shift=np.rint(np.array(hkl) @ np.linalg.inv(inp["reciprocal"])).astype(int)
                mu,free,simple_lo,simple_hi=interval_counts(band,shift)
                labels=np.where(band<mu-TIE_WIDTH_EV,1,np.where(band>mu+TIE_WIDTH_EV,0,2))
                nfill=int(half-np.sum(labels==1))
                lo,hi=exact_counts(labels,shift,nfill)
                if not simple_lo<=lo<=hi<=simple_hi:
                    raise AssertionError("range enclosure")
                q=np.linalg.norm(shift@reciprocal)/n
                writer.writerow((geometry,n,"".join(map(str,hkl)),f"{q:.11f}",half,free,nfill,
                                 simple_lo,lo,hi,simple_hi,f"{lo/(half*q*q):.9f}",f"{hi/(half*q*q):.9f}",
                                 f"{lo/(half*q):.9f}",f"{hi/(half*q):.9f}"))


if __name__=="__main__":
    main()
