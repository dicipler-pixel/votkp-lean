"""Fit only K-opening ratios at Z <= 70 and freeze the first sub-four bracket."""
import csv
import gzip
import hashlib
import json
import math
from pathlib import Path
from decimal import Decimal
from fractions import Fraction

here=Path(__file__).resolve().parent
archive=here.parents[3]/'data/element_thresholds_20261011.json.gz'
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
with gzip.open(archive,'rt') as f:
    training=json.load(f,parse_float=Decimal)['records'][:70]
assert training[-1]['Z']==70
ratio={}
for r in training[2:]:
    t=r['thresholds']
    ratio[r['Z']]=Fraction(t[-2]['IE_eV'])/Fraction(t[-3]['IE_eV'])
# Both readouts use only the training energies. Alpha is CODATA 2022.
alpha=1/137.035999177
def bare(z):
    return 2*(1+math.sqrt((1+math.sqrt(1-(alpha*z)**2))/2))
def line(z):
    return float(ratio[70]+(z-70)*(ratio[70]-ratio[65])/5)
def screened(z):
    return bare(z)+70*(float(ratio[70])-bare(70))/z
with (here/'predictions.csv').open('w',newline='') as out:
    writer=csv.writer(out,lineterminator='\n')
    writer.writerow(['Z','linear_from_65_70','dirac_plus_constant_over_Z'])
    for z in range(71,86):
        writer.writerow([z,f'{line(z):.9f}',f'{screened(z):.9f}'])
for name, fn in [('linear',line),('spinor point nucleus plus anchored 1/Z',screened)]:
    k=next(z for z in range(71,86) if fn(z)<4)
    print(name,'first strictly below 4 at',k,'values on either side',fn(k-1),fn(k))
