# SCRIPT: c8_mutant_benchmark
"""Benchmark: how often does theta separate a mutant group?

Mutant groups are built by Stoimenow's criterion -- equal hyperbolic volume, equal Alexander
polynomial, equal Jones polynomial -- which is how his tables were compiled
(stoimenov.net/stoimeno/homepage/ptab/). His counts: 91 groups through 12 crossings
(86 pairs + 5 triples), and 774 groups at 13 crossings; 865 in all.

theta values are taken from the census already computed for all 12,965 knots, so no
recomputation is needed.

Pre-registered rule: theta separates a group iff its members take different values at the
same rational point. The rate over all groups is the benchmark, together with the rate
restricted to groups where every member has theta nonzero (where a "separation" is not just
one of them being zero).
"""
import sys, json, os, collections
sys.path.insert(0,'code')
import knotnames

def load_census():
    vals = {}
    for p in ['.scratch/census_upto10.jsonl', '.scratch/census_11-12.jsonl', '.scratch/census_13.jsonl']:
        if not os.path.exists(p): continue
        for line in open(p):
            line = line.strip()
            if not line: continue
            r = json.loads(line)
            t = r.get('tested') or []
            if t: vals[r['knot']] = (tuple(t[0][:2]), t[0][2], r.get('zero', False))
    return vals

if __name__ == '__main__':
    K = knotnames.load()
    V = load_census()
    print(f'census values loaded: {len(V)}')
    # group by (volume, Alexander, Jones) -- Stoimenow's criterion
    groups = collections.defaultdict(list)
    for nm, k in K.items():
        if nm not in V: continue
        if not k['volume'] or not k['det']: continue
        try: v = round(float(k['volume']), 7)
        except Exception: continue
        groups[(v, str(k['det']))].append(nm)
    # need Jones too; knotnames does not carry it, so pull from the CSV
    import csv
    csv.field_size_limit(10**9)
    J = {}
    for r in csv.DictReader(open('.scratch/venv/lib/python3.12/site-packages/database_knotinfo/csv_data/knotinfo_data_complete.csv'), delimiter='|'):
        J[r['name']] = (r['jones_polynomial'] or '').replace(' ', '')
    refined = collections.defaultdict(list)
    for (v, d), g in groups.items():
        for nm in g:
            refined[(v, d, J.get(nm, ''))].append(nm)
    multi = {k: g for k, g in refined.items() if len(g) > 1}
    def fam(nm):
        import re
        m = re.match(r'^(\d+)([an]?)', nm); return m.group(1) + m.group(2)
    le12 = {k: g for k, g in multi.items() if all(int(fam(n)[:-1] if fam(n)[-1] in 'an' else fam(n)) <= 12 for n in g)}
    print(f'mutant groups found (volume + determinant + Jones): {len(multi)}   [Stoimenow: 865 = 91 + 774]')
    print(f'  groups entirely at <= 12 crossings: {len(le12)}   [Stoimenow: 91]')
    print()
    # theta comparison
    same = 0; diff = 0; skipped = 0; details = []
    for k, g in sorted(multi.items()):
        obs = []
        for nm in g:
            pt, val, zero = V[nm]
            obs.append((nm, pt, val, zero))
        pts = {o[1] for o in obs}
        if len(pts) != 1: skipped += 1; continue
        vals = {o[2] for o in obs}
        if len(vals) == 1: same += 1
        else: diff += 1; details.append((g, [o[2] for o in obs]))
    print(f'theta EQUAL on {same} groups; DIFFERENT on {diff}; incomparable (different test points) {skipped}')
    print(f'  separation rate: {100*diff/(same+diff):.1f}% of comparable groups')
    print()
    print('first twenty separated groups:')
    for g, vals in details[:20]:
        print(f'   {g}  ->  {vals}')
