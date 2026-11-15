# SCRIPT: c8_benchmark_equal
"""C8 benchmark, second pass: the groups on which theta is EQUAL.

c8_mutant_benchmark.py reported 694 of 829 candidate mutant groups separated by theta at
(2,3) and 135 not separated. This script does the cut that was promised in that docstring
and left undone:

  (a) candidate groups by Stoimenow's criterion (equal volume, Alexander, Jones -- we add
      determinant and signature, which mutation also preserves);
  (b) theta compared as an exact rational at the single common point (2,3), so "equal"
      means equal over the integers, not up to floating point;
  (c) every non-separated group classified as
        all members theta = 0   (no information available from theta by construction)
        all members theta != 0  (theta genuinely agrees on that mutation)
        mixed                   (impossible: a zero against a nonzero would separate);
  (d) the rate split by crossing number <= 12 (where Stoimenow's tables are) and 13;
  (e) group membership written out, so the equal groups can be looked at by name.

The restricted rate promised in the first script -- groups where every member has
theta != 0 -- is the number that actually bears on "is theta a mutation invariant".
"""
import sys, json, os, re, csv, collections
from fractions import Fraction
sys.path.insert(0, 'code')
import knotnames

CSV = '.scratch/venv/lib/python3.12/site-packages/database_knotinfo/csv_data/knotinfo_data_complete.csv'
CENSUS = ['.scratch/census_upto10.jsonl', '.scratch/census_11-12.jsonl', '.scratch/census_13.jsonl']
OUT = '.scratch/c8_benchmark.json'


def load_census():
    """knot -> (point, exact theta as Fraction, certified-zero flag)."""
    vals = {}
    for p in CENSUS:
        if not os.path.exists(p):
            continue
        for line in open(p):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            t = r.get('tested') or []
            if not t:
                continue
            pt = tuple(t[0][:2])
            vals[r['knot']] = (pt, Fraction(t[0][2]), bool(r.get('zero', False)))
    return vals


def load_knotinfo_poly():
    csv.field_size_limit(10**9)
    out = {}
    with open(CSV, newline='') as fh:
        for r in csv.DictReader(fh, delimiter='|'):
            nm = r['name']
            if nm == 'Name':
                continue
            out[nm] = {'jones': (r['jones_polynomial'] or '').replace(' ', ''),
                       'alex': (r['alexander_polynomial'] or '').replace(' ', '')}
    return out


def build_groups(K, P, V, keys):
    g = collections.defaultdict(list)
    for nm in V:
        k = K.get(nm)
        if not k or not k['volume'] or not k['det']:
            continue
        try:
            v = round(float(k['volume']), 7)
        except Exception:
            continue
        key = [v]
        if 'det' in keys:
            key.append(str(k['det']))
        if 'sig' in keys:
            key.append(str(k['sig']))
        if 'jones' in keys:
            key.append(P.get(nm, {}).get('jones', ''))
        if 'alex' in keys:
            key.append(P.get(nm, {}).get('alex', ''))
        g[tuple(key)].append(nm)
    return {k: sorted(v) for k, v in g.items() if len(v) > 1}


def classify(groups, V):
    """Split groups into separated / equal, with equal groups sub-classified."""
    rec = {'separated': [], 'equal_zero': [], 'equal_nonzero': [], 'mixed': []}
    for key, g in sorted(groups.items()):
        vals = [V[nm][1] for nm in g]
        zeros = [V[nm][2] for nm in g]
        if len(set(vals)) > 1:
            rec['separated'].append((g, [str(v) for v in vals]))
        elif all(zeros):
            rec['equal_zero'].append((g, [str(v) for v in vals]))
        elif any(zeros):
            # a certified zero against a nonzero value at the same point cannot be equal
            rec['mixed'].append((g, [str(v) for v in vals]))
        else:
            rec['equal_nonzero'].append((g, [str(v) for v in vals]))
    return rec


def split12(groups):
    le, hi = {}, {}
    for key, g in groups.items():
        (le if all(KC[nm] <= 12 for nm in g) else hi)[key] = g
    return le, hi


if __name__ == '__main__':
    K = knotnames.load()
    P = load_knotinfo_poly()
    V = load_census()
    KC = {nm: k['cross'] for nm, k in K.items()}
    print(f'census theta values loaded: {len(V)}  (all at the point {next(iter(V.values()))[0]})')
    print(f'certified zeros: {sum(1 for x in V.values() if x[2])}')
    print()

    # --- which filter reproduces Stoimenow's counts (865 through 13, 91 through 12)?
    print('filter variants (Stoimenow: 865 groups through 13 crossings, 91 through 12):')
    for keys in (('det', 'jones'), ('det', 'sig', 'jones'),
                 ('det', 'sig', 'jones', 'alex'), ('jones', 'alex')):
        G = build_groups(K, P, V, keys)
        le, hi = split12(G)
        print(f'  {str(keys):40s} total {len(G):4d}   <=12 {len(le):4d}   13 {len(hi):4d}')
    print()

    KEYS = ('det', 'sig', 'jones')
    G = build_groups(K, P, V, KEYS)
    rec = classify(G, V)
    le, hi = split12(G)
    print(f'GROUPS ({"+".join(KEYS)}): {len(G)}')

    def report(name, groups, r):
        n = sum(len(v) for v in groups.values())
        s, ez, en, mx = len(r['separated']), len(r['equal_zero']), len(r['equal_nonzero']), len(r['mixed'])
        eq = ez + en + mx
        print(f'  {name:10s} groups {len(groups):4d} (knots {n:5d})  '
              f'separated {s:4d} equal {eq:4d}  ->  {100.0*s/max(1,s+eq):5.1f}% separated')
        print(f'             equal: all theta=0 {ez:3d}, all nonzero {en:3d}, mixed {mx:3d}')
        den = s + en
        if den:
            print(f'             restricted to groups with no zero member: {100.0*s/den:5.1f}% separated ({s}/{den})')
        return s, eq, ez, en, mx

    print()
    report('all', G, rec)
    rle = classify(le, V)
    rhi = classify(hi, V)
    report('<=12', le, rle)
    report('13', hi, rhi)

    print()
    print('groups where theta is equal and NONZERO (genuine agreement):')
    for g, vals in rec['equal_nonzero']:
        fams = {re.match(r'^(\d+)', n).group(1) for n in g}
        am = [K[n]['symmetry'] for n in g]
        print(f'   {g}  theta={vals[0]}  crossings={sorted(fams)}  symmetry={am}')

    print()
    print('groups where theta is equal because every member is a certified zero:')
    for g, vals in rec['equal_zero']:
        fams = sorted({K[n]['cross'] for n in g})
        print(f'   {g}  crossings={fams}  symmetry={[K[n]["symmetry"] for n in g]}')

    json.dump({'keys': list(KEYS), 'total_groups': len(G),
               'separated': rec['separated'],
               'equal_zero': rec['equal_zero'],
               'equal_nonzero': rec['equal_nonzero'],
               'mixed': rec['mixed'],
               'le12': {'groups': len(le), **{k: v for k, v in rle.items()}},
               'at13': {'groups': len(hi), **{k: v for k, v in rhi.items()}}},
              open(OUT, 'w'), indent=1)
    print(f'\nwrote {OUT}')
