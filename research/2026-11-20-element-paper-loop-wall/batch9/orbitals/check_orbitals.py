"""Resolve adjacent ground-configuration changes and cross-check the pinned energies."""
import argparse
import csv
import gzip
import hashlib
import json
import re
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP, localcontext
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
DIGEST='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
KR={'1s':2,'2s':2,'2p':6,'3s':2,'3p':6,'3d':10,'4s':2,'4p':6}
CORES={'[Kr]':KR,'[Ar]':{k:v for k,v in KR.items() if k not in ('3d','4s','4p')},
       '[Ne]':{'1s':2,'2s':2,'2p':6}}

def occupancies(shell):
    result={}
    for token in shell.split('.'):
        if token in CORES:
            result.update(CORES[token])
        else:
            match=re.fullmatch(r'(\d[spdf])(\d*)',token)
            if not match:
                raise ValueError(token)
            orbital,power=match.groups()
            result[orbital]=int(power or '1')
    return result

def change(old,new):
    keys=old.keys() | new.keys()
    deltas={k:old.get(k,0)-new.get(k,0) for k in keys}
    if list(sorted(v for v in deltas.values() if v)) == [1]:
        return next(k for k,v in deltas.items() if v)
    return 'rearranged: '+','.join(f'{k} {v:+d}' for k,v in sorted(deltas.items()) if v)

def decimals(x):
    with localcontext() as ctx:
        ctx.prec=60
        return str((Decimal(x.numerator)/Decimal(x.denominator)).quantize(Decimal('.000001'),rounding=ROUND_HALF_UP))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('archive',type=Path)
    parser.add_argument('--csv',type=Path)
    args=parser.parse_args()
    if hashlib.sha256(args.archive.read_bytes()).hexdigest()!=DIGEST:
        raise ValueError('The archive differs from this analysis pin.')
    with gzip.open(args.archive,'rt') as handle:
        archive=json.load(handle,parse_float=Decimal)['records']
    with (HERE/'asd_ground_shells.csv').open() as handle:
        inputs=list(csv.DictReader(handle))
    source=defaultdict(dict)
    energies={}
    for row in inputs:
        q,Z=int(row['q']),int(row['Z'])
        assert archive[Z-1]['symbol']==row['symbol']
        e=archive[Z-1]['thresholds'][q]
        assert q==e['q']
        shell=occupancies(row['ground_shells'])
        assert sum(shell.values())==Z-q
        # NIST [] and () delimit provenance class. The energy source for each
        # ratio stays the archive; the live ASD snapshot is a separate check.
        nist=Decimal(row['ASD_display_IE_eV'].strip('[]() '))
        assert nist==e['IE_eV'],(Z,q,nist,e)
        source[Z][q]=shell
        energies[Z,q]=F(e['IE_eV'])
    print(f'{len(inputs)} ground-shell populations match their ion electron counts and pinned IE values: 215 batch rows, 12 Y/Zr context rows, 6 Pd/Ag applicability controls.')
    out=[]
    for Z in range(41,46):
        sym=archive[Z-1]['symbol']
        assert sorted(source[Z])==list(range(Z))
        shell=[source[Z][q] for q in range(Z)]+[{}]
        steps=[change(shell[q],shell[q+1]) for q in range(Z)]
        assert not any(s.startswith('rearranged:') for s in steps)
        assert all(c.get('4d',0)<10 for c in shell)
        key={}
        d5=[]
        for k in range(1,Z):
            a,b=energies[Z,k-1],energies[Z,k]
            z=b/a; g=(b-a)/(a+b)
            kind='ordinary'
            # k means IE_(k+1) / IE_k. The state between removals has q=k.
            if (steps[k-1],steps[k])==('5s','4d'):
                kind='5s to first open 4d'
            if (steps[k-1],steps[k])==('4d','4p'):
                kind='last 4d to Kr core'
            if kind!='ordinary':
                key[kind]=(k,decimals(z),decimals(g))
            if shell[k].get('4d')==5 and all(x in KR or x=='4d' for x in shell[k]):
                d5.append((k,steps[k-1],steps[k],decimals(z),decimals(g)))
            out.append([sym,k,steps[k-1],steps[k],kind,decimals(z),decimals(g)])
        print(sym,'first open 4d k,z,Gamma:',key['5s to first open 4d'],
            'Kr core k,z,Gamma:',key['last 4d to Kr core'],'pure d5:',d5 or 'absent')
    # Test whether a one-orbital label even exists in the preceding Y sequence.
    y = source[39]
    assert change(y[0], y[1]) == '4d'
    assert change(y[1], y[2]) == 'rearranged: 4d -1,5s +2'
    print('Y caution: first loss is 4d; the next change 5s2 → 4d has net 5s −2 and 4d +1.')
    for Z,k in [(40,2),(41,1)]:
        last = Z-36
        outer = energies[Z,k] / energies[Z,k-1]
        core = energies[Z,last] / energies[Z,last-1]
        assert change(source[Z][k-1],source[Z][k]) == '5s'
        assert change(source[Z][k],source[Z][k+1]) == '4d'
        print(f'{archive[Z-1]["symbol"]} rank test: open 4d {decimals(outer)} '
              + ('<' if outer<core else '>') + f' Kr core {decimals(core)}')
    # A filled d shell appears first in Pd, before the first neutral removal.
    # Ag is the first ordinary 5s -> filled 4d10 boundary with a preceding IE.
    assert source[46][0].get('4d')==10 and source[46][0].get('5s',0)==0
    assert [change(source[47][q],source[47][q+1]) for q in range(2)]==['5s','4d']
    assert source[47][1].get('4d')==10
    print('Pd neutral has 4d10 at q=0; its first ordinary ratio compares two 4d removals. Ag has a 5s → filled 4d10 opening at k=1.')
    if args.csv:
        with args.csv.open('w',newline='') as handle:
            writer=csv.writer(handle,lineterminator='\n');writer.writerow(['symbol','k','first_ground_occupancy_loss','second_ground_occupancy_loss','boundary','z','Gamma']);writer.writerows(out)

if __name__=='__main__':
    main()
