# SCRIPT: c8_verdicts
"""C8: the verdict for every mutant group, from the stored common-point values.

The run (c8_common_point.py) evaluated every member of every one of Stoimenow's 865 mutant
groups at six points, all members of a group at the same point, and stored the values. This
script applies the rule to them; it computes no theta itself, so the arithmetic is fixed and
re-runnable.

The rule, corrected here and fixed before this pass: a group refutes "theta is a mutation
invariant" iff its members do not all share ONE value UP TO SIGN. The sign has to be allowed for,
because the knot tables do not fix a chirality for a name: two members whose values are exact
negatives are the same chiral class as far as the tables can say, and matching the chirality
flips one of them. The Jones polynomial decides which pairs are mirror-named (see
c8_mutant_tables.py and the report), and it agrees with the sign test on every pair. So at the
first point where every member is finite:

    one distinct value        -> not separated at this point, try the next point
    more than one value       -> separated

Within the separated groups, two sub-cases are separated out because they mean different
things:

    sign      every value equal in absolute value, both signs present. theta(mirror K) =
              -theta(K) exactly (verified directly: theta of a negated braid word is minus
              theta of the word, on every knot tried), and the knot tables do not fix a
              chirality for a name, so this difference is a naming artefact, not information
              about mutation.
    partly    some members agree and others do not - theta sees part of the class.
"""
import json, collections, re, sys
from fractions import Fraction as F

R = json.load(open('.scratch/c8_common_point.json'))
cross = lambda n: int(re.match(r'^(\d+)', n).group(1))
POOL = [(2, 3), (2, 5), (3, 5), (5, 7), (2, 7), (3, 7)]

for r in R:
    if r.get('error'):
        r['verdict'] = 'error'
        continue
    r['verdict'] = 'equal'
    for q in POOL:
        if f'{q[0]},{q[1]}' not in r['values']:
            break            # the run stopped earlier: it had already found distinct values
        col = r['values'][f'{q[0]},{q[1]}']
        if any(v is None for v in col.values()):
            continue
        vals = [F(col[nm]) for nm in r['group']]
        if len(set(abs(v) for v in vals)) == 1:
            continue                      # equal up to sign here; try the next point
        r['at'] = list(q)
        r['distinct'] = len(set(vals))
        r['n'] = len(vals)
        signs = {v > 0 for v in vals}
        if len(set(abs(v) for v in vals)) == 1 and len(signs) > 1:
            r['verdict'] = 'sign'
        elif len(set(vals)) < len(vals):
            r['verdict'] = 'partly'
        else:
            r['verdict'] = 'separated'
        break

for r in R:
    r['mutation_verdict'] = ('not separated' if r.get('verdict') in ('equal', 'sign')
                             else 'separated')
    # inside the unseparated, say whether the value is shared exactly or only up to sign
    if r['mutation_verdict'] == 'not separated':
        for q in POOL:
            col = r['values'][f'{q[0]},{q[1]}']
            if any(v is None for v in col.values()):
                continue
            vals = [F(col[nm]) for nm in r['group']]
            r['share'] = 'identical' if len(set(vals)) == 1 else 'up to sign'
            break
c = collections.Counter(r['verdict'] for r in R)
print('up to chirality:', dict(collections.Counter(r['mutation_verdict'] for r in R)))
print(f'groups {len(R)}, knot positions {sum(len(r["group"]) for r in R)}')
print('verdicts:', dict(c))
print()
rows = [('all 865', R),
        ('pairs', [r for r in R if len(r['group']) == 2]),
        ('triples', [r for r in R if len(r['group']) == 3]),
        ('quads/6', [r for r in R if len(r['group']) > 3]),
        ('<=12 crossings', [r for r in R if all(cross(n) <= 12 for n in r['group'])]),
        ('13 crossings', [r for r in R if not all(cross(n) <= 12 for n in r['group'])])]
print('| range | groups | separated | partly | sign only | equal | refutes invariance |')
for label, sel in rows:
    d = collections.Counter(r['verdict'] for r in sel)
    n = len(sel)
    ref = d['separated'] + d['partly']
    print(f'{label:16s} {n:5d}  {d["separated"]:5d} {d["partly"]:4d} {d["sign"]:5d} {d["equal"]:5d}'
          f'   {ref:4d} = {100.0*ref/n:5.1f} %')
print()
print('points at which groups separated:', dict(collections.Counter(tuple(r['at']) for r in R if r.get('at'))))
eq = [r for r in R if r['verdict'] == 'equal']
sg = [r for r in R if r['verdict'] == 'sign']
pt = [r for r in R if r['verdict'] == 'partly']
print('unseparated, split:', dict(collections.Counter(r.get('share') for r in R
                                                      if r['mutation_verdict'] == 'not separated')))
print(f'equal {len(eq)} (sizes {dict(collections.Counter(len(r["group"]) for r in eq))}), '
      f'sign {len(sg)}, partly {len(pt)} (sizes {dict(collections.Counter(len(r["group"]) for r in pt))})')
print()
print('groups with no value at any pooled point?', sum(1 for r in R if r['verdict'] == 'error'))
with open('.scratch/c8_equal_list.txt', 'w') as fh:
    for label, sel in (('equal at every point tried', eq), ('differing only by the mirror sign', sg),
                       ('partly separated', pt)):
        fh.write(f'\n{label} ({len(sel)} groups)\n')
        for r in sel:
            fh.write('  ' + ', '.join(r['group']) + '\n')
json.dump(R, open('.scratch/c8_verdicts.json', 'w'), indent=1)
print('wrote .scratch/c8_verdicts.json and .scratch/c8_equal_list.txt')
