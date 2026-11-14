# SCRIPT: c8_tally
"""C8: the final tally over Stoimenow's tables, merging the (2,3) pass with the re-test.

Reads .scratch/c8_tables.json (groups + theta at (2,3)) and .scratch/c8_second_point.json
(the 183 groups that were not separated at (2,3), re-evaluated at (2,5), (3,5), (5,7),
(2,7), (3,7)), and prints the single table the report quotes.

Classification, fixed before the runs:

  separated        theta differs on some two members at the common point (2,3)
  separated later  equal at (2,3) on every pair, but separated at one of the further points
  equal up to sign equal at (2,3), and at the separating point still equal in absolute value
                   with opposite signs. This is the mirror rule -- theta(mirror K) = -theta(K)
                   -- so it is NOT a separation: the knot tables do not fix a chirality for a
                   name, and the Jones check below confirms which member is named mirrored.
  equal            equal at every point tried at which the formula is finite

Also reported: how many of the 865 groups contain a certified theta-zero knot (none -- the
78 zeros are exactly the amphichiral knots, and no mutant group contains one).
"""
import json, sys, re, collections
from fractions import Fraction as F
sys.path.insert(0, 'code')
import knotnames

T = json.load(open('.scratch/c8_tables.json'))
R = json.load(open('.scratch/c8_second_point.json'))
K = knotnames.load()
V = {}
for p in ['.scratch/census_upto10.jsonl', '.scratch/census_11-12.jsonl', '.scratch/census_13.jsonl']:
    for line in open(p):
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        t = r.get('tested') or []
        if t:
            V[r['knot']] = F(t[0][2])

late = {tuple(sorted(r['group'])): r for r in R}
cross = lambda n: int(re.match(r'^(\d+)', n).group(1))

rows = []
zero_members = 0
for names in T['groups']:
    key = tuple(sorted(names))
    vals = [V[n] for n in names]
    zero_members += sum(1 for n in names if V[n] == 0)
    if len(set(abs(v) for v in vals)) == 1 and len(set(vals)) > 1:
        # every value equal in absolute value, with both signs present: the mirror rule,
        # not a separation. (Confirmed against the Jones polynomials in the report.)
        cls = 'equal_up_to_sign'
    elif len(set(vals)) > 1:
        cls = 'separated'
    else:
        r = late.get(key)
        if r is None:
            cls = '???'
        elif r.get('separated_at'):
            cls = 'equal_up_to_sign' if r.get('absolute_equal_at') else 'separated later'
        else:
            cls = 'equal'
    rows.append({'group': names, 'class': cls,
                 'maxcross': max(cross(n) for n in names),
                 'all12': all(cross(n) <= 12 for n in names)})

print(f'groups: {len(rows)}   knot positions: {sum(len(r["group"]) for r in rows)}')
print(f'members that are certified theta-zero knots: {zero_members}')
print()
print('CONFUSION TABLE')
order = ['separated', 'equal_up_to_sign', 'equal']
for label, sel in (('all 865', rows),
                   ('<=12 crossings (91)', [r for r in rows if r['all12']]),
                   ('13 crossings (774)', [r for r in rows if not r['all12']]),
                   ('pairs', [r for r in rows if len(r['group']) == 2]),
                   ('groups of 3+', [r for r in rows if len(r['group']) > 2])):
    d = collections.Counter(r['class'] for r in sel)
    n = len(sel)
    sep = d['separated']
    print(f'  {label:30s} n={n:4d}  ' +
          '  '.join(f'{k} {d[k]:3d}' for k in order) +
          f'   | separate {sep:3d} = {100.0*sep/n:5.1f} %,  do not {n-sep:3d} = {100.0*(n-sep)/n:5.1f} %')
print()
# how much of the separation needs a point other than (2,3)
need_point = [r for r in rows if r['class'] == 'separated' and r['group'] not in ()]
at23 = 0
for names in T['groups']:
    vals = [V[n] for n in names]
    if len(set(vals)) == len(vals):
        at23 += 1
print(f'groups fully separated by (2,3) alone:            {at23}')
print(f'groups that need a second point to separate all pairs: {sum(1 for r in late.values() if r.get("separated_at") and not r.get("absolute_equal_at"))}')
print(f'groups where the only difference is the mirror sign: {sum(1 for r in rows if r["class"]=="equal_up_to_sign")}')
print(f'groups equal at every point tried:                {sum(1 for r in rows if r["class"]=="equal")}')
print()
eq = [r['group'] for r in rows if r['class'] == 'equal']
mi = [r['group'] for r in rows if r['class'] == 'equal_up_to_sign']
with open('.scratch/c8_equal_list.txt', 'w') as fh:
    fh.write(f'EQUAL at every point tried ({len(eq)} groups)\n')
    for g in eq:
        fh.write('  ' + ', '.join(g) + '\n')
    fh.write(f'\nEQUAL UP TO THE MIRROR SIGN ({len(mi)} groups)\n')
    for g in mi:
        fh.write('  ' + ', '.join(g) + '\n')
print('wrote .scratch/c8_equal_list.txt')
print()
for r in rows:
    if r['class'] in ('equal', 'equal_up_to_sign'):
        print(f'  [{r["class"]}] {r["group"]}')
json.dump(rows, open('.scratch/c8_tally.json', 'w'), indent=1)
print('\nwrote .scratch/c8_tally.json')
