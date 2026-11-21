"""Recompute the visible columns and both endpoints independently from the frozen inputs."""
import csv
from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import argparse

DIR = Path(__file__).resolve().parent
ARCH = DIR.parents[3]/'data/element_thresholds_20261011.json.gz'
HASH = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'


def read(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def keyrows(values):
    t = {(int(r['Z']),int(r['k'])):r for r in values}
    if len(t)!=len(values):
        raise ValueError('duplicate element/rung key')
    return t


def require(test, *message):
    if not test:
        raise ValueError(message)


def within(text, number, digits):
    # Midpoint ties use half-up rounding as in the source CSV.
    n,d=abs(number.numerator)*10**digits,number.denominator
    i,r=divmod(n,d)
    if 2*r>=d:
        i+=1
    if number<0:
        i=-i
    return F(text)==F(i,10**digits) and len(text.partition('.')[2])==digits


def check(printed, folder=DIR, *, first=61, last=65, outside=(('Eu',0),('Gd',0),('Tb',0))):
    require(hashlib.sha256(ARCH.read_bytes()).hexdigest()==HASH,'archive digest')
    with gzip.open(ARCH,'rt') as f:
        atoms=json.load(f,parse_float=F)['records'][first-1:last]
    plain=keyrows(printed)
    details=keyrows(read(folder/'rungs_detailed.csv'))
    affinity={int(a['Z']):a for a in read(folder/'affinities.csv')}
    asd={(int(a['Z']),int(a['q'])):a for a in read(folder/'asd_states_20261121.csv')}
    expected={(z,k) for z in range(first,last+1) for k in range(z+1)}
    require(plain.keys()==expected, 'complete row keys')
    dkeys={(z,k) for z,k in expected if k<z and (k>0 or affinity[z]['EA_eV'])}
    require(details.keys()==dkeys, 'complete ratio keys')
    require(len(asd)==sum(range(first,last+1)), 'public NIST snapshot')
    result=Counter()
    outs=[]
    for atom in atoms:
        n,sym,t=atom['Z'],atom['symbol'],atom['thresholds']
        a=affinity[n]
        vals=[F(a['EA_eV']) if a['EA_eV'] else None]+[q['IE_eV'] for q in t]
        unc=[F(a['unc_eV']) if a['unc_eV'] else None]+[q['unc_eV'] for q in t]
        for k in range(n+1):
            row=plain[n,k]
            require(row['symbol']==sym,sym,k,'symbol')
            x=vals[k]
            if k:
                t0=t[k-1]
                obs=asd[n,k-1]
                ie=obs['NIST_energy_eV']
                mark='T' if ie.startswith('(') else 'S' if ie.startswith('[') else 'E'
                require((F(ie.strip('[]()')),F(obs['NIST_unc_eV']),mark,obs['NIST_refs'])==
                        (x,unc[k],t0['grade'],t0['references']),sym,k,'public NIST record')
                require(row['source']==t0['grade'],sym,k,'archive grade')
                result['NIST records']+=1
                result['pinned grade '+mark]+=1
            else:
                require(row['source']==a['status'],sym,k,'anion status')
            if x is None:
                require(row['IE_k (eV)']==row['z_k']==row['Gamma_k']=='',sym,'no numeric EA')
                continue
            require(F(row['IE_k (eV)'])==x,sym,k,'pinned input')
            if k==n:
                require(row['z_k']==row['Gamma_k']=='',sym,'bare nucleus final row')
                continue
            y=vals[k+1]
            q=y/x
            gamma=(q-1)/(q+1)
            require(within(row['z_k'],q,6) and within(row['Gamma_k'],gamma,6),sym,k,'rounding')
            low=(y-unc[k+1])/(x+unc[k])
            high=(y+unc[k+1])/(x-unc[k])
            def wall(z):
                return 'outside' if 2*(z-1)**2>(z+1)**2 else 'inside'
            detail=details[n,k]
            require(wall(q)==wall(low)==wall(high)==detail['wall']==detail['box_wall'],sym,k,'wall boxes')
            require(wall(q)=='inside' or low>1 or high<1,sym,k,'interior of box')
            require(within(detail['z_lo'],low,9) and within(detail['z_hi'],high,9),sym,k,'box rounding')
            if wall(q)=='outside':
                outs.append((sym,k))
            result['ordinary pairs' if k else 'anion point pairs']+=1
            result['complete joint widths']+=1
            if low<1:
                result['rectangle permits reverse']+=1
            if low==1:
                result['rectangle touches at one']+=1
    require(outs==list(outside),'outside')
    return result


def controls(source):
    def clear(r):
        r[1]['z_k']=''
    def flip(r):
        r[1]['Gamma_k']='-0.100000'
    def invent(r):
        r[0]['IE_k (eV)']='0.154'
    def wrong(r):
        r[3]['IE_k (eV)']='22.1307'
    def erase(r):
        r[62]['source']='unbound'
    tests=(('skip terminal row',lambda r:r.pop()),('duplicate row',lambda r:r.append(r[5].copy())),
           ('missing ratio',clear),('reflection sign',flip),('insert theoretical promethium EA',invent),
           ('wrong pinned energy',wrong),('relabel samarium as unbound',erase))
    for label,corrupt in tests:
        mutated=[r.copy() for r in source]
        corrupt(mutated)
        try:
            check(mutated)
        except (ValueError, ZeroDivisionError):
            print('rejected:',label)
        else:
            raise AssertionError(f'false control unexpectedly passed: {label}')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--controls',action='store_true')
    args=parser.parse_args()
    printed=read(DIR/'batch13_pm_tb.csv')
    result=check(printed)
    print('Archive SHA256:',HASH)
    print('Printed CSV SHA256:', hashlib.sha256((DIR/'batch13_pm_tb.csv').read_bytes()).hexdigest())
    print('Printed rows:',len(printed))
    for label,value in sorted(result.items()):
        print(f'{label}: {value}')
    if args.controls:
        controls(printed)
