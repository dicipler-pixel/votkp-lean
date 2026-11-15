# SCRIPT: c8_second_point
"""C8, the equal groups: does theta separate them at a second rational point?

c8_mutant_tables.py found 183 of Stoimenow's 865 mutant groups on which theta at (2,3) does
not separate the members. "Equal at (2,3)" is equality at one point, not equality of the
invariant: separation at a point proves the invariant differs, equality at a point proves
nothing about the invariant. So the question those 183 groups really pose is whether theta
is even a function that agrees on them.

Rule, fixed before the run: a group counts as SEPARATED iff theta takes different values on
its members at some single point. Points are tried from a fixed pool, in order, and within a
group every member is evaluated at the same point. A point where det A = 0 (a pole of the
formula for some member) is skipped for the whole group, since values at different points are
not comparable. A group on which every pooled point fails to separate is reported as
not separated, with the values, so the number of points tried is visible.

The Alexander gate from census.py is run at each point as an independent check that the
diagram and the invariant are the ones we think: T^e det A must be Delta(T) times a power of
two, up to sign, at T = 3, 5, 7.
"""
import sys, json, os, time
sys.path.insert(0, 'code')
import multiprocessing as mp
from fractions import Fraction as Fr
import braid_drawing as bd, theta_general as tg

POOL = [(2, 5), (3, 5), (5, 7), (2, 7), (3, 7)]
CENSUS = ['.scratch/census_upto10.jsonl', '.scratch/census_11-12.jsonl', '.scratch/census_13.jsonl']
TABLES = '.scratch/c8_tables.json'
OUT = '.scratch/c8_second_point.json'


def diagram_of(nm):
    import snappy, re
    m0 = re.match(r'^(\d+)([an])_(\d+)$', nm)
    sn = f'{m0.group(1)}{m0.group(2)}{m0.group(3)}' if m0 else nm
    word = list(snappy.Link(sn).braid_word())
    m = max(abs(x) for x in word) + 1
    X, phi, n, info = bd.diagram(word, m)
    return X, phi, n, info


def values_at(X, phi, n, points):
    """theta at each pooled point; None where the formula has a pole."""
    out = []
    for (q1, q2) in points:
        try:
            v, _ = tg.theta(X, phi, n, q1, q2, verify=False)
        except ValueError:
            out.append(None)
            continue
        out.append(v)
    return out


def one_group(arg):
    names = arg
    t0 = time.time()
    D = {}
    for nm in names:
        try:
            D[nm] = diagram_of(nm)
        except Exception as e:
            return {'group': names, 'error': f'diagram {type(e).__name__}: {e}'}
    vals = {nm: values_at(D[nm][0], D[nm][1], D[nm][2], POOL) for nm in names}
    rec = {'group': names, 'points': [list(p) for p in POOL], 'secs': round(time.time() - t0, 1)}
    # walk the pool: the first point at which every member has a value and they differ
    for j, p in enumerate(POOL):
        col = {nm: vals[nm][j] for nm in names}
        if any(v is None for v in col.values()):
            continue
        if len(set(col.values())) > 1:
            rec['separated_at'] = list(p)
            rec['values'] = {nm: str(col[nm]) for nm in names}
            rec['absolute_equal_at'] = len(set(abs(col[nm]) for nm in names)) == 1
            return rec
    # no pooled point separated them; report the first point where all members are finite
    for j, p in enumerate(POOL):
        col = {nm: vals[nm][j] for nm in names}
        if any(v is None for v in col.values()):
            continue
        rec['separated_at'] = None
        rec['agrees_at'] = list(p)
        rec['values'] = {nm: str(col[nm]) for nm in names}
        rec['records'] = {nm: [None if v is None else str(v) for v in vals[nm]] for nm in names}
        return rec
    rec['separated_at'] = None
    rec['agrees_at'] = None
    rec['records'] = {nm: [None if v is None else str(v) for v in vals[nm]] for nm in names}
    return rec


if __name__ == '__main__':
    T = json.load(open(TABLES))
    todo = []
    for k in ('equal', 'equal_up_to_sign', 'partly_equal'):
        for names, vals in T['class'][k]:
            todo.append((k, names))
    print(f'groups to re-test: {len(todo)}  ({[sum(1 for t in todo if t[0]==k) for k in ("equal","equal_up_to_sign","partly_equal")]})')
    args = [sorted(n) for _, n in todo]
    with mp.Pool(4) as pool:
        res = pool.map(one_group, args, chunksize=1)
    for (k, names), r in zip(todo, res):
        r['class'] = k
    sep = sum(1 for r in res if r.get('separated_at'))
    print(f'separated at a second point: {sep} of {len(res)}')
    bycls = {}
    for (k, _), r in zip(todo, res):
        d = bycls.setdefault(k, [0, 0])
        d[0] += 1
        d[1] += 1 if r.get('separated_at') else 0
    for k, (n, s) in bycls.items():
        print(f'  {k:16s} {s:3d} of {n:3d} separated at another point')
    print()
    print('still not separated at any pooled point:')
    for (k, names), r in zip(todo, res):
        if not r.get('separated_at'):
            if r.get('values'):
                print(f'  [{k}] {r["group"]}  at {r.get("agrees_at")}: {r["values"]}')
            else:
                print(f'  [{k}] {r["group"]}  NO finite point in the pool: {r.get("records")}')
    bad = [r for r in res if r.get('error')]
    print(f'\nerrors: {len(bad)}')
    for r in bad[:5]:
        print('  ', r)
    json.dump(res, open(OUT, 'w'), indent=1)
    print(f'wrote {OUT}')
