"""Compare both frozen extrapolations with the independent archive thresholds."""
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIN = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
archive = HERE.parents[3]/'data/element_thresholds_20261011.json.gz'
assert hashlib.sha256(archive.read_bytes()).hexdigest() == PIN
with gzip.open(archive, 'rt') as f:
    atoms = json.load(f, parse_float=D)['records']
with (HERE/'predictions.csv').open() as f:
    forecasts = {int(row['Z']):row for row in csv.DictReader(f)}
assert list(forecasts) == list(range(71,86))
previous_low = None
first_below = None
with (HERE/'scores.csv').open('w') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow('Z symbol denominator numerator grades ratio lower upper secant_minus_observed secant_in_box dirac_minus_observed dirac_in_box'.split())
    for atom in atoms[2:85]:
        z = atom['Z']
        a,b = atom['thresholds'][-3:-1]
        assert (a['q'],b['q']) == (z-3,z-2)
        x,y,dx,dy = (D(a['IE_eV']),D(b['IE_eV']),D(a['unc_eV']),D(b['unc_eV']))
        value,low,high = y/x,(y-dy)/(x+dx),(y+dy)/(x-dx)
        if previous_low is not None:
            assert high < previous_low, (atom['symbol'],'overlapping neighbours')
        previous_low = low
        if value < 4 and first_below is None:
            first_below = z
        if z not in forecasts:
            continue
        model_values = [D(forecasts[z][name]) for name in ('linear_from_65_70','dirac_plus_constant_over_Z')]
        fmt = lambda number: format(number,'.9f')
        fields = []
        for estimate in model_values:
            fields.extend([fmt(estimate-value),low<=estimate<=high])
        w.writerow([z,atom['symbol'],x,y,a['grade']+'/'+b['grade'],fmt(value),fmt(low),fmt(high),*fields])
assert first_below == 80
print('82 adjacent nonoverlapping boxes from Li through At. First central ratio below four: Hg.')
