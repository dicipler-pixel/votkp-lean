"""Enumerate same-core faces in adjacent elements with element-wise endpoint boxes."""
import argparse
import csv
from collections import Counter
from fractions import Fraction as F
from dataclasses import dataclass
import gzip
import hashlib
import json
import math
from pathlib import Path

ARCHIVE_SHA='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
CORES={2:'helium',10:'neon',18:'argon',36:'krypton',54:'xenon',86:'radon'}

def dec(x):
    # Signed half-up to nine decimals; for display only.
    a=abs(x)
    q=(2*a.numerator*10**9+a.denominator)//(2*a.denominator)
    return f'{"-" if x<0 else ""}{q//10**9}.{q%10**9:09d}'

def power(z):
    return ((z-1)/(z+1))**2

def power_range(lo,hi):
    a,b=power(lo),power(hi)
    return (F(0) if lo<=1<=hi else min(a,b),max(a,b))

def which(margin):
    return 'open' if margin>0 else 'closes' if margin<0 else 'ideal'

def endpoints(low,high):
    return which(low) if which(low)==which(high) else 'straddles/touches'

@dataclass
class Face:
    name: str
    Z: int
    q: int
    den: dict
    num: dict
    ratio: F
    low: F
    high: F

    @property
    def grades(self):
        return self.den['grade']+self.num['grade']

def face(rec,n):
    q=rec['Z']-n-1
    th={t['q']:t for t in rec['thresholds']}
    if q<0 or q not in th or q+1 not in th:
        return None
    a,b=th[q],th[q+1]
    x,y=F(a['IE_eV']),F(b['IE_eV'])
    da,db=a['unc_eV'],b['unc_eV']
    if da is None or db is None:
        raise ValueError(f'Missing uncertainty on {rec["name"]}, q={q}')
    low,high=(y-db)/(x+da),(y+db)/(x-da)
    if not (F(0)<low<=y/x<=high and y>x):
        raise ValueError(f'Non-forward interval on {rec["name"]}, q={q}')
    return Face(rec['name'],rec['Z'],q,a,b,y/x,low,high)

def pair_row(core,a,b):
    if b.Z!=a.Z+1:
        raise ValueError('Nonadjacent element pair')
    l,r=power(a.ratio),power(b.ratio)
    margin=l+r-1
    la,ha=power_range(a.low,a.high)
    lr,hr=power_range(b.low,b.high)
    lb,hb=la+lr-1,ha+hr-1
    # Distinct independent test on raw threshold fractions:
    # sinh²(h_a)sinh²(h_b)-1 has the sign of
    # (a-1)²(b-1)² - 16ab. Circle crossing uses no reflected power.
    raw=(a.ratio-1)**2*(b.ratio-1)**2-16*a.ratio*b.ratio
    assert which(raw)==which(margin)
    def circle(z):
        u=math.tanh(math.log(float(z))/4)
        return ((1+u*u)/(2*u),(1-u*u)/(2*u))
    ca,ra=circle(a.ratio); cb,rb=circle(b.ratio)
    assert (math.hypot(ca,cb)<ra+rb)==(margin<0)
    margin_text=dec(margin)
    row=dict(core=core,left=a.name,right=b.name,Z_left=a.Z,Z_right=b.Z,
             q_left=a.q,q_right=b.q,left_IE_grades=a.grades,right_IE_grades=b.grades,
             z_left=dec(a.ratio),z_right=dec(b.ratio),self_left=which(2*l-1),
             self_right=which(2*r-1),mixed=which(margin),signed_margin=margin_text,
             margin_low=dec(lb),margin_high=dec(hb),mixed_endpoints=endpoints(lb,hb),
             central_direction='rising' if b.ratio>a.ratio else 'falling' if b.ratio<a.ratio else 'flat',
             direction_endpoints='rising' if b.low>a.high else 'falling' if b.high<a.low else 'overlap',
             self_left_endpoints=endpoints(2*la-1,2*ha-1),
             self_right_endpoints=endpoints(2*lr-1,2*hr-1))
    return row,margin,lb,hb

def save(path,rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,list(rows[0]),lineterminator='\n')
        writer.writeheader();writer.writerows(rows)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive',type=Path)
    p.add_argument('outdir',type=Path)
    args=p.parse_args()
    args.outdir.mkdir(parents=True,exist_ok=True)
    raw=args.archive.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=ARCHIVE_SHA:
        raise ValueError('Archive hash differs from this check.')
    records=json.loads(gzip.decompress(raw),parse_float=F)['records']
    assert [r['Z'] for r in records]==list(range(1,119))
    allfaces=[];allpairs=[];margins=[]
    print('Energy grades in order: denominator then numerator (E evaluated, S semiempirical, T theoretical).')
    for n,core in CORES.items():
        faces=[f for rec in records if (f:=face(rec,n)) is not None]
        for f in faces:
            lowpow,highpow=power_range(f.low,f.high)
            allfaces.append(dict(core=core,element=f.name,Z=f.Z,q=f.q,
                 start_q_IE_eV=str(F(f.den['IE_eV'])),end_q_plus_1_IE_eV=str(F(f.num['IE_eV'])),
                 start_unc_eV=str(F(f.den['unc_eV'])),end_unc_eV=str(F(f.num['unc_eV'])),
                 start_grade=f.den['grade'],end_grade=f.num['grade'],
                 start_reference=f.den['references'],end_reference=f.num['references'],
                 exact_z=str(f.ratio),z_low=dec(f.low),z_high=dec(f.high),
                 self_central=which(2*power(f.ratio)-1),
                 self_endpoints=endpoints(2*lowpow-1,2*highpow-1)))
        missing=[z for z in range(n+1,119) if all(f.Z!=z for f in faces)]
        gaps=[(a.Z,b.Z) for a,b in zip(faces,faces[1:]) if b.Z!=a.Z+1]
        pairs=[]
        for a,b in zip(faces,faces[1:]):
            if b.Z!=a.Z+1:
                continue
            row,m,lo,hi=pair_row(core,a,b)
            pairs.append(row);margins.append((abs(m),row,lo,hi))
        allpairs.extend(pairs)
        typ=Counter((r['self_left'],r['mixed'],r['self_right']) for r in pairs)
        uncertain=[r for r in pairs if r['mixed']!=r['mixed_endpoints']]
        comparison=Counter(r['direction_endpoints'] for r in pairs)
        direction=Counter(r['central_direction'] for r in pairs)
        print(f'\n{core.title()} core: {len(faces)} faces {faces[0].Z}–{faces[-1].Z}, '
              f'{len(pairs)} adjacent pairs, internal gaps {gaps}, '
              f'missing eligible Z range {min(missing)}–{max(missing)}.')
        assert missing==list(range(faces[-1].Z+1,119)) and not gaps
        print('  pair classes (left self, mixed, right self):',dict(typ))
        print('  central ratio direction:',dict(direction),'interval direction:',dict(comparison))
        print('  central mixed calls unresolved by endpoints:',[(r['left'],r['right']) for r in uncertain])
        rises=[f"{r['left']}/{r['right']} ({r['left_IE_grades']}:{r['right_IE_grades']})" for r in pairs if r['central_direction']!='falling']
        if rises:print('  Central nondecreases (source grades): '+', '.join(rises))
        for r in pairs:
            if r['self_left']!=r['self_right'] or 'straddles/touches' in (r['self_left_endpoints'],r['self_right_endpoints']):
                print(f"  boundary: {r['left']} / {r['right']}, {r['self_left']} / {r['mixed']} / {r['self_right']}, "
                      f"margin {r['signed_margin']} [{r['margin_low']}, {r['margin_high']}], "
                      f"self interval calls {r['self_left_endpoints']} / {r['self_right_endpoints']}.")
    save(args.outdir/'opening_faces.csv',allfaces)
    save(args.outdir/'adjacent_pairs.csv',allpairs)
    closest=min(margins,key=lambda t:t[0])[1]
    closest_box=next((lo,hi) for _,r,lo,hi in margins if r is closest)
    others_min=min(min(abs(lo),abs(hi)) for _,r,lo,hi in margins if r is not closest)
    assert all(lo*hi>0 for _,_,lo,hi in margins)
    assert max(map(abs,closest_box))<others_min
    print(f'Even the farthest edge of the closest pair box is closer to zero than the nearest edge of every other box: {dec(max(map(abs,closest_box)))} < {dec(others_min)}.')
    print('Three-way agreement: reflected powers, raw squared sinh product and disk-circle geometry on every central pair.')
    print(f'\n{len(allfaces)} archived faces, {len(allpairs)} distinct adjacent pairs.')
    print('Total mixed verdicts:',dict(Counter(r['mixed'] for r in allpairs)))
    print('Number of interval-supported mixed calls:',sum(r['mixed_endpoints']==r['mixed'] for r in allpairs))
    print(f"Closest central distinct-element mixed wall: {closest['core']} core {closest['left']} / {closest['right']}, "
          f"margin {closest['signed_margin']} [{closest['margin_low']}, {closest['margin_high']}].")

if __name__=='__main__':
    main()
