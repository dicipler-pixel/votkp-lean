# SCRIPT: D-MOVERS-PEEL-01-BASELINE
# Runs D-MOVERS-PEEL-01 from the archive and computes the exact chance baseline by enumeration.
# Kill condition (written before the run, 22 Nov 2026): within each d row, one cutoff on the first
# peel step z1 = IE2/IE1 must separate the movers (higher z1), with at most one error per row.
import json, gzip, itertools
from fractions import Fraction
R = json.load(gzip.open('../../../../data/element_thresholds_20261011.json.gz'))['records']
IE = {r['Z']: [t['IE_eV'] for t in r['thresholds']] for r in R}
SYM = {r['Z']: r['symbol'] for r in R}
ROWS = [('3d', list(range(21, 31))), ('4d', list(range(39, 49))), ('5d', [57] + list(range(72, 80)))]
MOVERS = {24, 29, 41, 42, 44, 45, 46, 47, 78, 79}
def best_errors(zs, ms):
    # min over cutoffs c of #elements misclassified by "mover iff z1 > c"
    vals = sorted(set(zs))
    cuts = [vals[0] - 1] + vals
    return min(sum(1 for z, m in zip(zs, ms) if (z > c) != m) for c in cuts)
rows = []; joint = Fraction(1)
for nm, Zs in ROWS:
    z1 = [IE[Z][1] / IE[Z][0] for Z in Zs]
    ms = [Z in MOVERS for Z in Zs]
    obs = best_errors(z1, ms)
    k = sum(ms); n = len(Zs); hits = 0; tot = 0
    for S in itertools.combinations(range(n), k):
        e = best_errors(z1, [i in S for i in range(n)]); tot += 1; hits += (e <= obs)
    p = Fraction(hits, tot); joint *= p
    rows.append({'row': nm, 'n': n, 'k': k, 'errors': obs, 'hits': hits, 'total': tot, 'p': float(p),
                 'pts': [{'Z': Z, 'sym': SYM[Z], 'z1': round(z, 4), 'mover': m} for Z, z, m in zip(Zs, z1, ms)]})
    print(f'{nm}: movers {k} of {n}, best errors {obs}; random sets doing as well or better: {hits} of {tot} = {float(p):.4f}')
print(f'joint (all three rows at once): {float(joint):.6f} = {joint}')
# total-errors baseline: random sets in all rows together with total errors <= observed total
tot_obs = sum(r['errors'] for r in rows)
from collections import Counter
dists = []
for nm, Zs in ROWS:
    z1 = [IE[Z][1] / IE[Z][0] for Z in Zs]; k = sum(Z in MOVERS for Z in Zs); n = len(Zs)
    dists.append(Counter(best_errors(z1, [i in S for i in range(n)]) for S in itertools.combinations(range(n), k)))
num = 0; den = 1
for d in dists: den *= sum(d.values())
for a in dists[0]:
    for b in dists[1]:
        for c in dists[2]:
            if a + b + c <= tot_obs: num += dists[0][a] * dists[1][b] * dists[2][c]
print(f'total errors {tot_obs}; random sets with total errors <= {tot_obs}: {num} of {den} = {num/den:.6f}')
json.dump({'rows': rows, 'joint': float(joint), 'joint_frac': str(joint), 'total_obs': tot_obs, 'total_hits': num, 'total_den': den},
          open('moves_test.json', 'w'), indent=1)
