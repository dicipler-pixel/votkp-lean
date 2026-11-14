# SCRIPT: c8_final
"""C8: the final tally, from the common-point run alone.

One input: .scratch/c8_common_point.json, which holds, for every one of Stoimenow's 865
mutant groups, theta on every member at each of six points (2,3), (2,5), (3,5), (5,7), (2,7),
(3,7), or "pole" where det A = 0.

Verdicts.
  separated          all members finite at one point and all values distinct there
  separated (sign)   as above, but at that point the values are equal in absolute value with
                     both signs present: this is theta(mirror K) = -theta(K), and since the
                     knot tables do not fix a chirality for a name, it carries no information
                     about mutation. Counted separately, never as a separation.
  equal              no point in the pool separates the group.
"""
import json, re, collections, sys
sys.path.insert(0, 'code')
import knotnames

R = json.load(open('.scratch/c8_common_point.json'))
K = knotnames.load()
cross = lambda n: int(re.match(r'^(\d+)', n).group(1))

for r in R:
    if r.get('error'):
        continue
    p = r.get('separated_at')
    if p is None:
        r['verdict'] = 'equal'
        continue
    vals = [r['values'][f'{p[0]},{p[1]}'][nm] for nm in r['group']]
    from fractions import Fraction as F
    F_ = [F(v) for v in vals]
    both_signs = len(set(F_)) > 1 and len(set(abs(v) for v in F_)) == 1
    r['verdict'] = 'separated (sign)' if both_signs else 'separated'
    r['at'] = p

print(f'groups: {len(R)}   knot positions: {sum(len(r["group"]) for r in R)}')
c = collections.Counter(r['verdict'] for r in R)
print('verdicts:', dict(c))
print()
print('| crossing range | groups | separated | separated (sign) | equal |')
for label, sel in (('all', R),
                   ('pairs', [r for r in R if len(r['group']) == 2]),
                   ('3 or more', [r for r in R if len(r['group']) > 2]),
                   ('<=12', [r for r in R if all(cross(n) <= 12 for n in r['group'])]),
                   ('13', [r for r in R if not all(cross(n) <= 12 for n in r['group'])])):
    d = collections.Counter(r['verdict'] for r in sel)
    n = len(sel)
    print(f'{label:10s} | {n:4d} | {d["separated"]:4d} ({100.0*d["separated"]/n:5.1f} %) | '
          f'{d["separated (sign)"]:3d} | {d["equal"]:3d} ({100.0*d["equal"]/n:5.1f} %)')
print()
pts = collections.Counter(tuple(r['at']) for r in R if r.get('at'))
print('points at which a group was separated:', dict(pts))
eq = [r for r in R if r['verdict'] == 'equal']
print(f'equal groups: {len(eq)}, sizes {collections.Counter(len(r["group"]) for r in eq)}')
print('  members that are certified theta-zero knots:',
      sum(1 for r in eq for nm in r['group'] if nm in ZERO)) if False else None
print()
print('value samples of the equal groups (first point where all are finite):')
for r in eq[:12]:
    p = next((q for q in r['points'] if all(v is not None for v in
              (r['values'][f'{q[0]},{q[1]}'][nm] for nm in r['group']))), None)
    v = r['values'][f'{p[0]},{p[1]}'][r['group'][0]] if p else '?'
    print(f'  {r["group"]}  {v}')
with open('.scratch/c8_equal_list.txt', 'w') as fh:
    fh.write(f'equal at every point tried ({len(eq)} groups)\n')
    for r in eq:
        fh.write('  ' + ', '.join(r['group']) + '\n')
    sg = [r for r in R if r['verdict'] == 'separated (sign)']
    fh.write(f'\ndiffering only by the mirror sign ({len(sg)} groups)\n')
    for r in sg:
        fh.write('  ' + ', '.join(r['group']) + '\n')
print('\nwrote .scratch/c8_equal_list.txt')
json.dump(R, open('.scratch/c8_final.json', 'w'), indent=1)
print('wrote .scratch/c8_final.json')
