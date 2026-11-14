# SCRIPT: c8_collisions
"""C8: the classes of knots that share a theta value at (2,3), for the census-wide paragraph.

The report says, of the 12,577 knots whose census value is at (2,3): 12,499 are nonzero, they
take 12,343 distinct values, so 153 classes of knots share a value; 94 of those classes are
exactly one of the equal mutant pairs and one more is two pairs merged; the other 58 classes
(121 knots) are in none of Stoimenow's groups, and 43 of those classes agree in volume,
Alexander polynomial and Jones polynomial.

This script writes those classes and the flags the report states, so that verify_numbers.py can
check the paragraph without needing the KnotInfo table (which is not redistributed).
"""
import json, csv, sys, collections
from fractions import Fraction as Fr
sys.path.insert(0, 'code')
import knotnames

K = knotnames.load()
CSV = '.scratch/venv/lib/python3.12/site-packages/database_knotinfo/csv_data/knotinfo_data_complete.csv'
P = {}
csv.field_size_limit(10**9)
for r in csv.DictReader(open(CSV), delimiter='|'):
    P[r['name']] = ((r['alexander_polynomial'] or '').replace(' ', ''),
                    (r['jones_polynomial'] or '').replace(' ', ''))

rec = {}
for p in ['.scratch/census_upto10.jsonl', '.scratch/census_11-12.jsonl', '.scratch/census_13.jsonl']:
    for line in open(p):
        line = line.strip()
        if not line:
            continue
        j = json.loads(line)
        t = j.get('tested') or []
        if t:
            rec[j['knot']] = (tuple(t[0][:2]), Fr(t[0][2]))

at23 = {k: v[1] for k, v in rec.items() if v[0] == (2, 3)}
nonzero = {k: v for k, v in at23.items() if v != 0}
byval = collections.defaultdict(list)
for k, v in nonzero.items():
    byval[v].append(k)
classes = [tuple(sorted(ns)) for v, ns in byval.items() if len(ns) > 1]

V = json.load(open('.scratch/c8_verdicts.json'))
equal = {tuple(sorted(r['group'])) for r in V if r['verdict'] == 'equal'}

rows = []
for c in classes:
    vols = {round(float(K[n]['volume']), 7) if K[n]['volume'] else None for n in c}
    share_vol = len(vols) == 1 and None not in vols
    share_all = share_vol and len({P[n][0] for n in c}) == 1 and len({P[n][1] for n in c}) == 1
    inside = [g for g in equal if set(g) <= set(c)]
    rows.append({'knots': list(c), 'value': str(nonzero[c[0]]),
                 'is_one_equal_group': c in equal, 'contains_equal_groups': len(inside),
                 'share_volume': share_vol, 'share_volume_alex_jones': share_all})

out = {'knots_at_23': len(at23), 'nonzero_at_23': len(nonzero), 'distinct_values': len(byval),
       'collision_classes': len(classes), 'knots_in_classes': sum(len(c) for c in classes),
       'classes': rows}
json.dump(out, open('.scratch/c8_collisions.json', 'w'), indent=1)

exact = sum(1 for r in rows if r['is_one_equal_group'])
merged = sum(1 for r in rows if not r['is_one_equal_group'] and r['contains_equal_groups'])
other = [r for r in rows if not r['contains_equal_groups']]
print(f'knots at (2,3) {len(at23)}, nonzero {len(nonzero)}, distinct values {len(byval)}')
print(f'collision classes {len(classes)} over {sum(len(c) for c in classes)} knots')
print(f'  exactly one equal mutant group: {exact}')
print(f'  several such groups inside:     {merged}')
print(f'  no mutant group inside:         {len(other)} classes, {sum(len(r["knots"]) for r in other)} knots')
print(f'  of those, sharing volume+Alexander+Jones: {sum(1 for r in other if r["share_volume_alex_jones"])}')
print('wrote .scratch/c8_collisions.json')
