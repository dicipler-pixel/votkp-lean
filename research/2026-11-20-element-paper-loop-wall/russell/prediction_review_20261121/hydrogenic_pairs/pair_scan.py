from decimal import Decimal as D
from fractions import Fraction as F
import csv, gzip, hashlib, itertools, json, math, sys
from collections import Counter
from pathlib import Path

archive = Path(sys.argv[1])
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
outdir=Path(sys.argv[2]) if len(sys.argv)>2 else Path(__file__).parent
outdir.mkdir(exist_ok=True)
recs=json.load(gzip.open(archive,'rt'),parse_float=D)['records']
c=(F('7.576234')/F('1.30447')+F('8.15168')/F('1.3895212'))/2
def above_w(z):return z>1 and z*z-6*z+1>0
def winner(z):return above_w(z) and z<c
levels=[];missing=[]
for r in recs:
    z=r['Z']
    t=next((t for t in r['thresholds'] if t['q']==z-1),None)
    if t and t['IE_eV'] is not None:
        levels.append((z,r['symbol'],F(t['IE_eV']),None if t['unc_eV'] is None else F(t['unc_eV']), t['grade'],t['references']))
    else:missing.append(r['symbol'])
fs=['Za','a','Zb','b','Ea','Eb','dEa','dEb','grade_a','grade_b','ref_a','ref_b','ratio','low','high','central','overlap','robust','z_NonRel','z_Dirac','hit_NonRel','hit_Dirac']
alpha=1/137.035999177
def dirac(z):
    x=(alpha*z)**2
    return x/(1+math.sqrt(1-x))
def fmt(x):return '' if x is None else f'{float(x):.13g}'
rows=[]
for a,b in itertools.combinations(levels,2):
    assert a[0]<b[0]
    z=b[2]/a[2];lo=hi=None
    if a[3] is not None and b[3] is not None:
        lo=(b[2]-b[3])/(a[2]+a[3]);hi=(b[2]+b[3])/(a[2]-a[3])
    nr=F(b[0],a[0])**2
    dr=dirac(b[0])/dirac(a[0])
    rows.append(dict(zip(fs,[a[0],a[1],b[0],b[1],fmt(a[2]),fmt(b[2]),fmt(a[3]),fmt(b[3]),a[4],b[4],a[5],b[5],fmt(z),fmt(lo),fmt(hi),winner(z),None if lo is None else above_w(hi) and lo<c,None if lo is None else above_w(lo) and hi<c,fmt(nr),fmt(dr),winner(nr),winner(F(dr))])))
def write(file,selection):
    with (outdir/file).open('w') as f:
        w=csv.DictWriter(f,fieldnames=fs);w.writeheader();w.writerows(selection)
hits=[r for r in rows if r['central'] or r['overlap']]
theoryhits=[r for r in rows if r['hit_NonRel'] or r['hit_Dirac']]
write('candidates.csv',hits);write('comparison.csv',theoryhits)
print('assigned ion energies',len(levels),'missing',len(missing),','.join(missing))
print('grade counts',dict(Counter(r[4] for r in levels)))
print('levels without widths:',[r[1] for r in levels if r[3] is None])
print('pairs:',len(rows),'complete boxes',sum(r['robust'] is not None for r in rows),'central',sum(r['central'] for r in rows),'overlap',sum(r['overlap'] is True for r in rows),'robust',sum(r['robust'] is True for r in rows))
for r in hits: print('archived candidate',*[r[k] for k in ('a','b','ratio','low','high','grade_a','grade_b','z_NonRel','z_Dirac')])
for key in ('z_NonRel','z_Dirac'):
    print(key,'candidates',[(r['a'],r['b'],r[key]) for r in theoryhits if r[key.replace('z_','hit_')]])
