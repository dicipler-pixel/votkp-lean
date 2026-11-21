"""Find the observable resolution of a scalar cutoff across the first ten batches."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
import gzip
import json
import csv

paper=Path(__file__).resolve().parents[1]
archive=paper.parents[1]/'data/element_thresholds_20261011.json.gz'
with gzip.open(archive,'rt') as stream:
    records=json.load(stream,parse_float=Decimal)['records'][:50]
files=[
    paper/'gpt_batches/VOTKP_H_to_Ne_corrected_ladders.csv',
    *(paper/'checks'/name for name in (
        'batch3.csv','batch4.csv','batch5_corrected.csv','batch6_corrected.csv','batch7.csv')),
    paper/'batch8/ladder/batch8_kr_zr.csv',
    paper/'batch9/ladder/batch9_nb_rh.csv',
    paper/'batch10/ladder/batch10_pd_sn.csv',
]
affinities={}
for file in files:
    with file.open(newline='') as stream:
        for row in csv.DictReader(stream):
            if row['k']!='0':continue
            element=int(row['Z'])
            assert element not in affinities
            value=row.get('energy_eV',row.get('IE_k (eV)'))
            affinities[element]=Q(value) if value and value.strip() not in ('—','NA') else None

# Some historic corrected CSVs omit an unbound rung entirely. Require an explicit
# allowed set and verify all other elements are represented by a positive affinity.
unbound={2,4,7,10,12,18,25,30,36,48}
assert {r['Z'] for r in records if not affinities.get(r['Z'])}==unbound
families={'ordinary':[], 'anion':[]}
for row in records:
    Z=row['Z']
    energies=[Q(t['IE_eV']) for t in row['thresholds']]
    assert len(energies)==Z and all(a<b for a,b in zip(energies,energies[1:]))
    for k,(a,b) in enumerate(zip(energies,energies[1:]),1):
        families['ordinary'].append((b/a,row['name'],k))
    if affinities.get(Z):families['anion'].append((energies[0]/affinities[Z],row['name'],0))

def analyze(label,values):
    def outside(r):return 2*(r-1)**2>(r+1)**2
    inside=[row for row in values if not outside(row[0])]
    out=[row for row in values if outside(row[0])]
    lower=max(inside); upper=min(out)
    print(f'{label}: {len(values)} defined pairs, {len(inside)} inside, {len(out)} outside')
    for side,(v,e,k) in [('max inside',lower),('min outside',upper)]:
        print(f'  {side}: {e}, rung {k}, {v.numerator}/{v.denominator} = {float(v):.10f}')
    print(f'  equivalent-cutoff interval width {float(upper[0]-lower[0]):.10f}')
    return lower,upper

analyze('Ordinary only',families['ordinary'])
analyze('Anion only (including calculated technetium)',families['anion'])
analyze('All central inputs',families['ordinary']+families['anion'])
analyze('Omitting the calculated technetium anion',families['ordinary']+[v for v in families['anion'] if v[1].lower()!='technetium'])
