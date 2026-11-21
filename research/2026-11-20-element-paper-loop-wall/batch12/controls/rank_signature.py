"""Compact directional necklaces on the unshifted 48³ half-filled rubidium mesh."""
import csv
from collections import Counter
import gzip
from itertools import groupby, product
import json
from pathlib import Path
import re
import sys

import numpy as np

from rank_flow import CUBIC_STEPS, TIE_WIDTH_EV, TRANSPORT, band_grid, interval_counts
from shell_interval import Q, atan


def necklace(word):
    # Repeated fixed symbols carry self-edges which never count. Preserve every
    # ambiguous vertex independently, including consecutive ambiguous sites.
    reduced=[]
    for label, grp in groupby(word):
        if label == 2:
            reduced.extend(list(grp))
        else:
            reduced.append(label)
    if len(reduced)>1 and reduced[0] == reduced[-1] and reduced[0] != 2:
        reduced.pop()
    # Rotation preserves edges and the set of all possible fillings.
    return min(tuple(reduced[i:]+reduced[:i]) for i in range(len(reduced)))


def census(labels, shift):
    flat_ids=np.arange(labels.size).reshape(labels.shape)
    succ=np.roll(flat_ids,-shift,axis=(0,1,2)).ravel()
    flat=labels.ravel()
    seen=np.zeros(labels.size,dtype=bool)
    out=Counter()
    for seed in range(labels.size):
        if seen[seed]:
            continue
        i=seed
        word=[]
        while not seen[i]:
            seen[i]=True
            word.append(int(flat[i]))
            i=succ[i]
        assert i == seed
        out[necklace(word)]+=1
    return out


def exits_range(word):
    values=[]
    for assignment in product((0,1),repeat=word.count(2)):
        fills=iter(assignment)
        cycle=[next(fills) if c==2 else c for c in word]
        values.append(sum(a==1 and b==0 for a,b in zip(cycle,cycle[1:]+cycle[:1])))
    return min(values), max(values)


def main():
    # Reuse the earlier rigorous Machin enclosure for the independent Lean
    # arithmetic predicate. Each printed 5-decimal lower threshold is rounded down.
    pi=16*atan(Q(1,5))-4*atan(Q(1,239))
    assert pi.high < Q(31415926536,10**10)
    inp=json.loads(gzip.decompress((TRANSPORT/'Rb_band_inputs.json.gz').read_bytes()))['48']
    energy=band_grid(inp)[0][...,4]
    writer=csv.writer(sys.stdout,lineterminator="\n")
    writer.writerow(("hkl","cyclic_signature_0empty_1occupied_2ambiguous",
                     "number_of_cycles","min_exits_per_cycle","max_exits_per_cycle"))
    for hkl in CUBIC_STEPS:
        shift=np.rint(np.array(hkl)@np.linalg.inv(inp["reciprocal"])).astype(int)
        mu,*_=interval_counts(energy,shift)
        labels=np.where(energy<mu-TIE_WIDTH_EV,1,np.where(energy>mu+TIE_WIDTH_EV,0,2))
        # Check the entire compact pattern tables compiled by Lean against this archive run.
        direction = "".join(map(str, hkl))
        source = Path(__file__).with_name("RankFlow.lean").read_text()
        section = source.split("def patterns" + direction + " :", 1)[1].split("\ntheorem ",1)[0]
        encoded = {}
        for encoded_word, multiplicity, exits in re.findall(r"⟨\[([0-2, ]+)\], (\d+), (\d+)⟩", section):
            signature = tuple(map(int, encoded_word.split(",")))
            if signature in encoded:
                raise AssertionError("duplicate Lean signature")
            encoded[signature] = (int(multiplicity), int(exits))
        found = {}
        for word,count in sorted(census(labels,shift).items()):
            lo,hi=exits_range(word)
            if lo != hi:
                raise AssertionError("tie-dependent signature")
            found[word] = (count,lo)
            writer.writerow((direction,"".join(map(str,word)),count,lo,hi))
        if found != encoded:
            raise AssertionError("archive and Lean signature tables disagree")


if __name__=="__main__":
    main()
