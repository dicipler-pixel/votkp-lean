# SCRIPT: c2_reconcile
"""Why does order-4 give median 0.107 % here and 0.076 % in the VOTKP paper?

Candidate causes, each testable against the 12,941 records already computed:
  A  the knot set: they report 12,954 knots, this run has 12,941
  B  the denominator of the relative error: |pred-vol|/vol (used here) versus
     |pred-vol|/(n V0), the "full volume" scale
  C  restricting to knots whose pieces are all near the vacuum
  D  a different set of shapes (canonical retriangulation)
Reported: the median under each convention, so the gap can be attributed or left open.
"""
import json, math, statistics as st
import sys
sys.path.insert(0,'code')

V0 = 1.0149416064096536

rows = [json.loads(l) for l in open('.scratch/c2_orders.jsonl')]
print(f'records: {len(rows)}')
for key, lbl in [('e2','order 2'), ('e3','order 3'), ('e4','order 4')]:
    v = sorted(r[key] for r in rows)
    print(f'  {lbl}: median {100*st.median(v):.4f}%  90th {100*v[int(0.9*(len(v)-1))]:.4f}%')

print()
print('B. denominator = n*V0 (the full-volume scale) instead of vol:')
# we stored only the ratio; recover |pred-vol| from e4*vol
alt = []
for r in rows:
    err_abs = r['e4']*r['vol']
    scale = r['n']*V0
    alt.append(err_abs/scale)
alt_s = sorted(alt)
print(f'   median {100*st.median(alt_s):.4f}%  90th {100*alt_s[int(0.9*(len(alt_s)-1))]:.4f}%')

print()
print('A. knot set: how much could 13 extra knots move a median over ~12,941?')
v = sorted(r['e4'] for r in rows)
for extra in (5, 10, 13, 20):
    # worst case: the extra knots are extremely bad
    hi = v + [1.0]*extra
    lo = [0.0]*extra + v
    print(f'   +{extra} knots, if all terrible: {100*st.median(sorted(hi)):.4f}%   '
          f'if all perfect: {100*st.median(sorted(lo)):.4f}%   (was {100*st.median(v):.4f}%)')

print()
print('C. by number of tetrahedra (are the small-n knots the low-error ones?)')
from collections import defaultdict
byn = defaultdict(list)
for r in rows: byn[r['n']].append(r['e4'])
for n in sorted(byn)[:10]:
    vv = sorted(byn[n])
    print(f'   n={n:3d}  count {len(vv):5d}  median {100*st.median(vv):7.4f}%')
allv = sorted(r['e4'] for r in rows)
print(f'   n<=6 only: {100*st.median(sorted(x for r in rows for x in [r["e4"]] if r["n"]<=6)):.4f}%')
