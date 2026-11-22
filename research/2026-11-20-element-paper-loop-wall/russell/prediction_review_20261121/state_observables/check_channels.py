"""Observable controls for C/O. Usage: python check_channels.py ARCHIVE CHIANTI_ROOT."""
from decimal import Decimal as D, getcontext
from pathlib import Path
import gzip
import hashlib
import json
import sys

getcontext().prec = 42
arc, ch = map(Path, sys.argv[1:])
assert hashlib.sha256(arc.read_bytes()).hexdigest() == '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
records = json.loads(gzip.decompress(arc.read_bytes()), parse_float=D)['records']
cm = D('8065.543937')
w = 3 + 2*D(2).sqrt()
mid = (D('7.576234')/D('1.30447')+D('8.15168')/D('1.3895212'))/2
def ies(symbol):
    ion = next(r for r in records if r['symbol'] == symbol)
    return [D(str(x['IE_eV'])) for x in ion['thresholds'][:2]]
def states(z):
    return '/'.join('outside' if z>cut else 'inside' for cut in (w,mid))
o1,o2 = ies('O')
for f,E in enumerate(map(D,['356736.30','356844.98','357117.01'])):
    for J,p in zip([2,1,0],map(D,['0','158.265','226.977'])):
        z=(o2+E/cm)/(o1-p/cm)
        print(f'O initial J={J}, final J={f}: z={z:.12f}, {states(z)}')
    if f==0:
        print('neutral initial shifts for the two boundaries (cm^-1):',*[f'{(o1-(o2+E/cm)/cut)*cm:.5f}' for cut in (w,mid)])
c1,c2=ies('C')
for lab,E in [('2s4d 1D even','324212.5'),('2p3d 1D odd','332691.28'),('2p3p 1D even','333118.21'),('2s5d 1D even','346658.3')]:
    a=c2+D(E)/cm; z=a/c1
    print(f'C {lab}: threshold={a:.7f} eV, z={z:.9f} {states(z)}')
rates=ch/'o/o_3/o_3.wgfa'
assert hashlib.sha256(rates.read_bytes()).hexdigest()=='19b9363a630a092eb24963f72ee9b201b8354ed3b0535ec0c4da0c3be922d2e3'
rows=[]
for ln in rates.read_text().splitlines():
    if ln.strip()=='-1': break
    lower,upper,lam,gf,rate,name=ln.split(maxsplit=5)
    rows.append((int(upper),D(lam),D(rate),name))
tau=[]
for J,upper,tag in [(0,53,'1590.589'),(1,54,'1591.290'),(2,55,'1589.979')]:
    chosen=[r for r in rows if r[0]==upper]
    total=sum(r[2] for r in chosen); tau.append(D('1e9')/total)
    branch=next(r for r in chosen if r[1]==D(tag))[2]/total
    print(f'O J={J}: published retained rates n={len(chosen)}, tau={tau[-1]:.9f} ns, tag={tag} A, A_tag/sum(A)={branch:.9f}')
print(f'O lifetime contrast tau2 / sqrt(tau0*tau1)={tau[2]/(tau[0]*tau[1]).sqrt():.9f}')
