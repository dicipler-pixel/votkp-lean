"""Find candidate adjacent atomic removal thresholds at the two frozen forward cutoffs."""
from fractions import Fraction as Q
from decimal import Decimal as D
from pathlib import Path
import csv,gzip,json,sys,hashlib
archive=Path(sys.argv[1])
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
records=json.load(gzip.open(archive,'rt'),parse_float=D)['records']
rival=(Q('7.576234')/Q('1.30447')+Q('8.15168')/Q('1.3895212'))/2
def above_wall(v):
 return v>1 and v*v-6*v+1>0
def hit(v):
 return above_wall(v) and v<rival
def disp(x):
 return '' if x is None else f'{float(x):.10f}'
rows=[]
for rec in records:
 energies={t['q']:t for t in rec['thresholds'] if t['IE_eV'] is not None}
 for q,a in sorted(energies.items()):
    if q+1 not in energies:continue
    b=energies[q+1]
    e,n=[Q(t['IE_eV']) for t in (a,b)]
    if e<=0 or n<=0: continue
    lo=hi=None
    if all(t['unc_eV'] is not None for t in (a,b)):
      de,dn=[Q(t['unc_eV']) for t in (a,b)]
      if e>de:lo,hi=(n-dn)/(e+de),(n+dn)/(e-de)
    touch=None if hi is None else above_wall(hi) and lo<rival
    rows.append((rec['Z'],rec['symbol'],q+1,e,n,a['grade'],b['grade'],n/e,lo,hi,touch,hit(n/e)))
for label,ss in [('all',rows),('H–At',[r for r in rows if r[0]<=85]),('Rn–Og',[r for r in rows if r[0]>85])]:
 print(label,len(ss),'central hits',sum(r[-1] for r in ss),'overlaps',sum(r[-2] is True for r in ss),'incomplete',sum(r[-2] is None for r in ss))
print('overlapping boxes')
for r in rows:
 if r[-2]:print(r[:3],r[5:7],*[disp(x) for x in r[7:10]])
print('closest central (Rn–Og)')
w=3+2*2**.5
for r in sorted((r for r in rows if r[0]>85),key=lambda r:min(abs(float(r[7])-w),abs(float(r[7]-rival))))[:8]:
 print(r[:3],r[5:7],*[disp(x) for x in r[7:10]])
out=Path(sys.argv[2]);out.mkdir(exist_ok=True)
with (out/'heavy_archived_pairs.csv').open('w') as f:
 writer=csv.writer(f);writer.writerow('Z symbol earlier_k IE_k_eV IE_next_eV grade_k grade_next z lower upper interval_overlaps central_hit'.split())
 for r in rows:
  if r[0]>85:writer.writerow([*r[:3],*[disp(v) for v in r[3:5]],*r[5:7],*[disp(v) for v in r[7:10]],*r[10:]])
