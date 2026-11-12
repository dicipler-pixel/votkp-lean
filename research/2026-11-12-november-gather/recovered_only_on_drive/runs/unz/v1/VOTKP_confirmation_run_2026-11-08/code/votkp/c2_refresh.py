# SCRIPT: c2_refresh
"""Recompute selected records of c2_orders.jsonl, and report how far they move.

Written while checking the archive. The bowl law's error is a function of the tetrahedron shapes,
so it depends on which triangulation of the knot SnapPy returns, and for some knots that is not
unique: a fresh process can come back with a different ideal triangulation of the same exterior.
$7_4$ is the example -- 0.311 per cent at order 2 on one triangulation, 0.544 on another -- and
the report says so next to its eleven-knot table.

The script recomputes the named knots with c2_bowl_orders.one() and rewrites only those records,
printing every change in per cent. It does not decide which value is right; it makes the
difference visible, and it is how the 7_4 row of the report was reconciled with the data file.

    python3 code/votkp/c2_refresh.py 7_4 12a_803 13a_3143 11a_247 ...
"""
import json
import sys
sys.path.insert(0, 'code')
sys.path.insert(0, 'code/votkp')
from c2_bowl_orders import one

F = '.scratch/c2_orders.jsonl'

if __name__ == '__main__':
    want = sys.argv[1:]
    if not want:
        sys.exit('give knot names')
    recs = []
    for line in open(F):
        line = line.strip()
        if line:
            recs.append(json.loads(line))
    at = {r['knot']: i for i, r in enumerate(recs)}
    changed = 0
    for nm in want:
        if nm not in at:
            print(f'{nm}: not in {F}, skipped')
            continue
        new = one(nm)
        if new is None:
            print(f'{nm}: recomputation failed, left alone')
            continue
        old = recs[at[nm]]
        diff = {k: (round(100 * old[k], 3), round(100 * new[k], 3))
                for k in ('e0', 'e2', 'e3', 'e4') if abs(old[k] - new[k]) > 1e-12}
        if diff:
            print(f'{nm}: {diff}  (old %, new %)')
            recs[at[nm]] = new
            changed += 1
        else:
            print(f'{nm}: unchanged')
    if changed:
        with open(F, 'w') as fh:
            for r in recs:
                fh.write(json.dumps(r) + '\n')
        print(f'rewrote {F}: {changed} record(s) replaced')
    else:
        print('nothing to do')
