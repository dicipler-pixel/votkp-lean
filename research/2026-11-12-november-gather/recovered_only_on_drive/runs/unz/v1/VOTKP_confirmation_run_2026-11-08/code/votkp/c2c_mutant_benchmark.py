# SCRIPT: c2c_mutant_benchmark
"""C2c, run through the mutant benchmark: on which knots can the bowl law be PROVED?

C8 asked whether theta separates the members of a mutant group. The same 865 groups are put to
the certified bound of C2c, and the question is a different one, because `bound` is not a knot
invariant and cannot be: it is a function of the tetrahedron shapes of a particular
triangulation, and mutation does not preserve triangulations. Volume, which mutants share, does
not enter except as the denominator.

So two questions are asked, and they are kept apart.

  (i)  UNIFORM CERTIFICATION. On how many groups can the law be proved for every member, at
       1 %, 5 % and 0.1 %? This is the question the certificate is built to answer, and it is a
       property of a family of knots, not of an invariant.

  (ii) THE INVARIANCE TEST, applied anyway, as C8 applied it to theta. Is the certified error
       equal across the members of a group (to the last bit), and if not, by how much does it
       vary? A large spread is the measure of how much of the certificate is diagrammatic. This
       is the honest way to say that the bound is not an invariant: not "it fails", but "here
       is how far apart two mutants' certificates are".

Rule, fixed before the run: `bound` is the certified relative error C sum_j |G_j|^5 / Vol with
C = 0.685556567092, as computed by c2_certify_census.py. A group is uniformly certified at eps
iff every member has bound < eps. A group is "equal" iff max bound / min bound < 1 + 1e-12.
"""
import json, statistics as st, collections, sys

V = json.load(open('.scratch/c8_verdicts.json'))
B = {}
for line in open('.scratch/c2_certify.jsonl'):
    line = line.strip()
    if line:
        r = json.loads(line)
        B[r['knot']] = r

groups = [r['group'] for r in V]
print(f'mutant groups: {len(groups)}, knot positions: {sum(len(g) for g in groups)}')
missing = [n for g in groups for n in g if n not in B]
print(f'positions with no certificate: {len(missing)}')

rows = []
for g in groups:
    bs = {n: B[n]['bound'] for n in g if n in B}
    if len(bs) < len(g):
        continue
    lo, hi = min(bs.values()), max(bs.values())
    rows.append({'group': g, 'lo': lo, 'hi': hi, 'n': len(g),
                 'uniform1': hi < 0.01, 'uniform5': hi < 0.05, 'uniform01': hi < 0.001,
                 'equal': (hi / lo if lo else 1.0) < 1 + 1e-12,
                 'ratio': (hi / lo) if lo else float('inf'),
                 'straddle1': lo < 0.01 <= hi})

n = len(rows)
print()
print('| | groups | share |')
for key, label in [('uniform1', 'law proved for every member below 1 %'),
                   ('uniform5', 'law proved for every member below 5 %'),
                   ('uniform01', 'law proved for every member below 0.1 %'),
                   ('equal', 'certified error identical across the group'),
                   ('straddle1', 'members straddle the 1 % line')]:
    c = sum(1 for r in rows if r[key])
    print(f'| {label} | {c} | {100.0 * c / n:.1f} % |')

ratios = [r['ratio'] for r in rows if r['ratio'] != float('inf')]
print()
print(f'within-group spread max/min: median {st.median(ratios):.3f}, '
      f'90th pct {sorted(ratios)[int(0.9 * len(ratios)) - 1]:.3f}, worst {max(ratios):.1f}')
worst = max((r for r in rows if r['ratio'] != float('inf')), key=lambda r: r['ratio'])
print(f'  widest group: {worst["group"]}  bound {worst["lo"]:.3e} vs {worst["hi"]:.3e}')
tight = min(rows, key=lambda r: r['ratio'] if r['ratio'] else 9e9)
print(f'  narrowest group: {tight["group"]}  ratio {tight["ratio"]:.6f}')

# the knots the certificate cannot reach
allb = sorted(B.values(), key=lambda r: -r['bound'])
print()
print('the census:')
for eps in (0.001, 0.01, 0.05):
    print(f'  proved below {eps:.1%}: {sum(1 for r in B.values() if r["bound"] < eps)} of {len(B)}')
print(f'  median certified bound {100 * st.median([r["bound"] for r in B.values()]):.3f} %')
print()
print('the knots the certificate does not reach at 5 %:')
for r in allb:
    if r['bound'] >= 0.05:
        print(f'  {r["knot"]:9s} bound {100 * r["bound"]:8.2f} %   measured {100 * r["meas"]:6.2f} %   n={r["n"]:3d}  vol {r["vol"]:.4f}')
print()
print('the twenty worst inside 5 %:')
for r in [x for x in allb if x['bound'] < 0.05][:20]:
    print(f'  {r["knot"]:9s} bound {100 * r["bound"]:8.3f} %   measured {100 * r["meas"]:6.3f} %   n={r["n"]:3d}')

json.dump(rows, open('.scratch/c2c_mutant_benchmark.json', 'w'), indent=1)
print('\nwrote .scratch/c2c_mutant_benchmark.json')
