# SCRIPT: c8_mutant_tables
"""C8 benchmark against Stoimenow's actual mutant tables.

The first pass (c8_mutant_benchmark.py) built candidate groups from a criterion -- equal
volume, Alexander, Jones -- which found 829 groups against the tables' 865. That filter is
shown here to be neither complete nor sound. This script uses the tables themselves.

Source: Stoimenow, knot data tables, <stoimenov.net/stoimeno/homepage/ptab/>,
files 12mut.out and 13mut.out, downloaded 2026-11-08. The page states: 91 groups through 12
crossings (86 pairs, 5 triples) and 774 at 13 (703 pairs, 38 triples, 32 quadruples, one
group of 6) -- 865 in all, 1841 knot positions. Both files parse to exactly those counts.

Numbering: through 10 crossings Rolfsen; 11 and 12 KnotScape; 13 KnotScape with the
non-alternating knots appended after the alternating ones. So index i at crossing c maps to

    c <= 10 :  c_i
    c >= 11 :  c a_i                if i <= A(c)
               c n_(i - A(c))       otherwise        A = 367, 1288, 4878 for 11, 12, 13

which is KnotInfo's own a/n convention, so the names compare directly with the census.

Two things this script is careful about:

  * Stoimenow states "care is not taken how the knots are mirrored". His table is a list of
    GROUPS; a member may be the mirror of the knot KnotInfo names. theta changes sign under
    mirroring, so a group can come out "equal up to sign" purely as an artefact of that
    convention. Such groups are counted separately from genuine equality.

  * "equal at (2,3)" is equality at one rational point, not equality of the invariant.
    Separation at one point is a proof of inequality; equality is not a proof of equality.
    The equal groups are therefore re-evaluated at a second point.
"""
import sys, json, re, os
from fractions import Fraction
sys.path.insert(0, 'code')

TABLES = [('.scratch/stoimenow/12mut.out', 0), ('.scratch/stoimenow/13mut.out', 0)]
A = {11: 367, 12: 1288, 13: 4878}
CENSUS = ['.scratch/census_upto10.jsonl', '.scratch/census_11-12.jsonl', '.scratch/census_13.jsonl']
OUT = '.scratch/c8_tables.json'


def parse(path):
    txt = open(path).read()
    blocks = [b for b in re.split(r'\n\s*\n', txt) if b.strip()]
    groups = []
    for b in blocks:
        g = []
        for line in b.strip().splitlines():
            tok = line.split()
            if tok:
                g.append((int(tok[0]), int(tok[1])))
        groups.append(g)
    return groups


def knotinfo_name(c, i):
    if c <= 10:
        return f'{c}_{i}'
    a = A[c]
    return f'{c}a_{i}' if i <= a else f'{c}n_{i - a}'


def load_census():
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
            if t:
                vals[r['knot']] = (tuple(t[0][:2]), Fraction(t[0][2]), bool(r.get('zero', False)))
    return vals


def classify(values):
    """values: list of Fractions. Returns one of separated / equal / equal_up_to_sign."""
    if len(set(values)) == 1:
        return 'equal'
    if len(set(abs(v) for v in values)) == 1:
        return 'equal_up_to_sign'
    # a group of 3 or 4 can be partly equal; report the finest common pattern
    if len(set(values)) < len(values):
        return 'partly_equal'
    return 'separated'


if __name__ == '__main__':
    groups12 = parse(TABLES[0][0])
    groups13 = parse(TABLES[1][0])
    groups = [(12, g) for g in groups12] + [(13, g) for g in groups13]
    print(f'groups: {len(groups12)} through 12 crossings, {len(groups13)} at 13, {len(groups)} total')
    print(f'knot positions: {sum(len(g) for _, g in groups)}')
    V = load_census()
    print(f'census theta values: {len(V)}')
    missing = [(c, i) for c, g in groups for (cc, i) in [(c, x) for x in g] if False]
    named = []
    for c, g in groups:
        names = [knotinfo_name(c, i) for _, i in g]
        if any(nm not in V for nm in names):
            missing.append((c, names))
        named.append(names)
    print(f'groups with a member absent from the census: {len(missing)}')
    for m in missing[:10]:
        print('   ', m)
    if missing:
        raise SystemExit('mapping is wrong somewhere; stopping')

    counts = {'separated': 0, 'equal': 0, 'equal_up_to_sign': 0, 'partly_equal': 0}
    rec = {k: [] for k in counts}
    by_cross = {}
    for names in named:
        vals = [V[nm][1] for nm in names]
        cl = classify(vals)
        counts[cl] += 1
        rec[cl].append((names, [str(v) for v in vals]))
        key = max(int(re.match(r'^(\d+)', n).group(1)) for n in names)
        by_cross.setdefault(key, {'separated': 0, 'equal': 0, 'equal_up_to_sign': 0, 'partly_equal': 0})
        by_cross[key][cl] += 1

    tot = sum(counts.values())
    print()
    print(f'over the tables ({tot} groups):')
    for k in ('separated', 'equal', 'equal_up_to_sign', 'partly_equal'):
        print(f'  {k:16s} {counts[k]:4d}   {100.0*counts[k]/tot:5.1f} %')
    print()
    print('by crossing number of the largest member:')
    for k in sorted(by_cross):
        d = by_cross[k]
        n = sum(d.values())
        print(f'  {k:3d}: {n:4d} groups   separated {d["separated"]:4d} '
              f'({100.0*d["separated"]/n:5.1f} %)   equal {d["equal"]:3d}   '
              f'equal up to sign {d["equal_up_to_sign"]:3d}   partly {d["partly_equal"]:2d}')
    le12 = sum(v for k, v in by_cross.items() if k <= 12 for v in [sum(v.values())]) if False else None
    print()
    print('non-separated, with names and values (this is the list to look at):')
    for k in ('equal', 'equal_up_to_sign', 'partly_equal'):
        for names, vals in rec[k]:
            print(f'  [{k}] {names} -> {vals}')

    json.dump({'groups': named, 'values': {nm: [list(V[nm][0]), str(V[nm][1]), V[nm][2]] for g in named for nm in g},
               'class': {k: rec[k] for k in rec}, 'counts': counts, 'by_cross': by_cross},
              open(OUT, 'w'), indent=1)
    print(f'\nwrote {OUT}')
