"""Compare the seven cutoffs printed before batch 11 using exact fractions."""
import argparse
import csv
import gzip
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

HASH = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
CUTS = tuple(map(F, ('5', '5.8', '5.82', '5.83', '5.85', '5.9', '6')))
WAVENUMBER = F('6.62607015e-34')*299792458*100/F('1.602176634e-19')


def table(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def rung(symbol,k,x,u,y,v):
    z=y/x
    lo=hi=None
    if u is not None and v is not None:
        assert min(x-u,y-v)>0
        lo,hi=(y-v)/(x+u),(y+v)/(x-u)
    label=2*(y-x)**2>(x+y)**2
    return (symbol,k,z,lo,hi,label)


def asfrac(value):
    return None if value is None or value=='' else F(value)


def ratio_value(row,grade):
    return row[2] if grade=='central' else row[3] if row[5] else row[4]


def describe(row,grade):
    v=ratio_value(row,grade)
    return f'{row[0]} k={row[1]} {float(v):.12f} ({v})'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    parser.add_argument('older_affinities',type=Path)
    parser.add_argument('new_batch_detail',type=Path)
    args=parser.parse_args()
    assert hashlib.sha256(args.archive.read_bytes()).hexdigest()==HASH
    with gzip.open(args.archive,'rt',encoding='utf-8') as fp:
        atoms=json.load(fp,parse_float=Decimal)['records'][:55]
    affinities={}
    for ea in table(args.older_affinities):
        if ea['status']=='unbound':
            continue
        scale=WAVENUMBER if ea['source']=='Se26_cm-1' else F(1)
        u=asfrac(ea['unc_source_units'])
        affinities[ea['symbol']]=(F(ea['EA_source_units'])*scale,u*scale if u is not None else None)
    later=table(args.new_batch_detail)
    for r in later:
        if r['k']=='0':
            affinities[r['symbol']]=(F(r['start_eV']),asfrac(r['start_unc_eV']))
    prev=[];new=[]
    for atom in atoms:
        z=atom['Z']; sym=atom['symbol']
        energies=[(F(t['IE_eV']),asfrac(t['unc_eV'])) for t in atom['thresholds']]
        group=prev if z<=50 else new
        for k,(a,b) in enumerate(zip(energies,energies[1:]),1):
            group.append(rung(sym,k,*a,*b))
        if sym in affinities:
            group.append(rung(sym,0,*affinities[sym],*energies[0]))
    assert len(new)==len(later)
    actual={(r[0],r[1]):r for r in new}
    assert set(actual)=={(r['symbol'],int(r['k'])) for r in later}
    for r in later:
        s,k,val,low,high,call=actual[r['symbol'],int(r['k'])]
        assert r['central_wall']==('outside' if call else 'inside')
        assert abs(val-F(r['z'])) <= F('0.0000000005')
        if low is None:
            assert r['endpoint_wall']=='unavailable'
        else:
            assert abs(low-F(r['z_low'])) <= F('0.0000000005')
            assert abs(high-F(r['z_high'])) <= F('0.0000000005')
    full=prev+new
    for name,rs in [('H-Sn',prev),('Sb-Cs',new),('H-Cs',full)]:
        print(f'{name}: {len(rs)} rungs, {sum(r[3] is not None for r in rs)} complete boxes, {sum(r[5] for r in rs)} outside.')
        for scope,cases in [('ordinary',[r for r in rs if r[1]]),('all',rs)]:
            for grade in ['central','box']:
                have=[r for r in cases if grade=='central' or r[3] is not None]
                key=lambda r:ratio_value(r,grade)
                inside=max((r for r in have if not r[5]),key=key)
                outside=min((r for r in have if r[5]),key=key)
                lower=key(inside);upper=key(outside)
                assert lower<upper
                if grade=='box':
                    for r in have:
                        for end in r[3:5]:
                            gamma=(end-1)/(end+1)
                            assert (2*gamma**2>1)==r[5]
                            assert (end>lower)==r[5] and (end>(lower+upper)/2)==r[5]
                print(f'  {scope} {grade}: [{describe(inside,grade)}, {describe(outside,grade)})')
    for c in CUTS:
        groups=[[(r[0],r[1]) for r in rs if (r[2]>c)!=r[5]] for rs in (prev,new)]
        print(f'Cutoff {float(c):g}: H-Sn disagreements {len(groups[0])} {groups[0]}; Sb-Cs {len(groups[1])} {groups[1]}')
    with localcontext() as ctx:
        ctx.prec=40
        wall=Decimal(3)+2*Decimal(2).sqrt()
        for name,rs in [('H-Cs',full),('Sb-Cs',new)]:
            ans=sorted((abs(Decimal(r[2].numerator)/Decimal(r[2].denominator)-wall),r) for r in rs if r[1]==0)
            print(f'{name} closest anion by absolute forward-z distance: {describe(ans[0][1],"central")} distance {ans[0][0]:.12f}')
    print('New input boxes unavailable:', [(r[0],r[1]) for r in new if r[3] is None])
    cs=actual['Cs',1]
    print(f'Cs k=1 outside, z {float(cs[2]):.12f}, bounds [{float(cs[3]):.12f},{float(cs[4]):.12f}]')
    # Both caesium endpoints distinguish cutoff 6 from the wall.
    assert cs[3] > F('5.9') and cs[4] < F(6)
    assert all((r[2]>F('5.83')) == r[5] for r in full)

if __name__=='__main__':
    main()
