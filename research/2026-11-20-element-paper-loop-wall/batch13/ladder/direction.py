"""Exact shared-energy tests; z and Gamma in each row use the same two energies."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import csv
import gzip
import hashlib
import json

DIR = Path(__file__).resolve().parent
ARCHIVE = DIR.parents[3]/'data/element_thresholds_20261011.json.gz'
HASH = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'


def study(atom):
    thresholds = atom['thresholds']
    c = [F(t['IE_eV']) for t in thresholds]
    u = [F(t['unc_eV']) for t in thresholds]
    lo = [x-y for x,y in zip(c,u)]
    hi = [x+y for x,y in zip(c,u)]
    assert all(a < b for a,b in zip(c,c[1:]))
    candidates = [k for k in range(1,len(c)) if hi[k-1] > lo[k]]
    contacts = [k for k in range(1,len(c)) if hi[k-1] == lo[k]]
    # Two strict reversals in a row require E(k) > E(k+1) > E(k+2).
    # In this data each two-apart interval is strictly separated.
    assert all(hi[k] < lo[k+2] for k in range(len(c)-2))
    feasible = []
    for n in range(len(candidates)+1):
        for group in combinations(candidates,n):
            if any(j == i+1 for i,j in zip(group,group[1:])):
                continue
            values = list(c)
            for k in group:
                values[k-1],values[k] = hi[k-1],lo[k]
            assert all(a <= v <= b for a,v,b in zip(lo,values,hi))
            # Require exactly these reversals, so all 2^n candidate sign vectors
            # are either explicitly realized here or excluded by the two-apart test.
            assert [k for k in range(1,len(c)) if values[k-1] > values[k]] == list(group)
            feasible.append(group)
    max_group = max(feasible,key=len)
    t,k_min = min(((c[k]-c[k-1])/(u[k-1]+u[k]),k) for k in range(1,len(c)))
    equality = c[k_min-1]+t*u[k_min-1]
    assert equality == c[k_min]-t*u[k_min]
    return (atom['symbol'],','.join(map(str,candidates)),','.join(map(str,contacts)),
            len(feasible),len(max_group),','.join(map(str,max_group)),k_min,str(t),str(equality))


if __name__ == '__main__':
    assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() == HASH
    with gzip.open(ARCHIVE,'rt') as f:
        atoms = json.load(f,parse_float=F)['records'][60:65]
    results = [study(atom) for atom in atoms]
    with (DIR/'joint_direction.csv').open('w', newline='') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerow(('symbol','reversible_k','touch_only_k','possible_strict_reversal_sets',
                         'max_simultaneous','example_k','first_to_touch_k',
                         'common_width_multiplier_to_touch','common_energy_at_touch_eV'))
        writer.writerows(results)
    for row in results:
        print(*row,sep=' | ')
    assert sum(r[4] for r in results) == 5
