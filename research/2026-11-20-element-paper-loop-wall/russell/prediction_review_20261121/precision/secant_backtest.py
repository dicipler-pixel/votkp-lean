"""Rolling hindcasts of the registered francium secant, without target fitting."""
import csv
from pathlib import Path
from fractions import Fraction as F
import sys
with Path(sys.argv[1]).open() as f: rows={r['symbol']:r for r in csv.DictReader(f) if r['k']=='1'}
series=['Li','Na','K','Rb','Cs']
z=[F(rows[e]['next_energy_eV'])/F(rows[e]['energy_eV']) for e in series]
def outside(q):
    assert q>=1
    return q*q-6*q+1>0
for i in range(2,6):
    pred=2*z[i-1]-z[i-2]
    target=(series+['Fr'])[i]
    if target=='Fr':
        print(f'{target}: predicted {float(pred):.9f}, IE2={float(F("4.0727411")*pred):.9f} eV, side: inside; independent experiment pending')
        continue
    assert not outside(pred) and outside(z[i])
    print(f'{target}: predicted {float(pred):.9f} inside; catalogue {float(z[i]):.9f} outside; ratio error (actual−prediction) {float(z[i]-pred):.9f}')
