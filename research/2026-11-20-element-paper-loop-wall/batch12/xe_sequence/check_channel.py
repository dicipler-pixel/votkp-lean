"""Recompute the 55 -> 54 -> 53 electron threshold channel without orbital labels."""
import csv
import gzip
import hashlib
import json
import sys
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ARCHIVE = ROOT / 'data/element_thresholds_20261011.json.gz'
SHA = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == SHA
with gzip.open(ARCHIVE, 'rt') as f:
    atoms = json.load(f, parse_float=Decimal)['records']
writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(('Z', 'element', 'k', 'IE_k_eV', 'u_k_eV', 'grade_k',
                 'IE_next_eV', 'u_next_eV', 'grade_next', 'z', 'z_low', 'z_high',
                 'Gamma', 'relative_to_36_over_25', 'wall'))
prior_low = None
for atom in atoms[54:60]:
    z = atom['Z']
    k = z - 54
    e, f = atom['thresholds'][k-1:k+1]
    assert (e['q'], f['q']) == (z-55, z-54)
    a, b, da, db = (Fraction(x) for x in (e['IE_eV'], f['IE_eV'], e['unc_eV'], f['unc_eV']))
    ratio = b/a
    low, high = (b-db)/(a+da), (b+db)/(a-da)
    assert 1 < low <= ratio <= high
    assert prior_low is None or high < prior_low
    prior_low = low
    floor = Fraction(36, 25)
    side = 'above' if low > floor else 'below' if high < floor else 'straddles'
    assert side == ('above' if z <= 58 else 'straddles' if z == 59 else 'below')
    outside = (z == 55)
    for x in (low, high):
        assert (x*x-6*x+1 > 0) == outside
    g = (b-a)/(b+a)
    def display(x):
        return format(Decimal(x.numerator)/Decimal(x.denominator), '.9f')
    writer.writerow((z, atom['name'], k, e['IE_eV'], e['unc_eV'], e['grade'],
                     f['IE_eV'], f['unc_eV'], f['grade'], *map(display, (ratio,low,high,g)),
                     side, 'outside' if outside else 'inside'))
