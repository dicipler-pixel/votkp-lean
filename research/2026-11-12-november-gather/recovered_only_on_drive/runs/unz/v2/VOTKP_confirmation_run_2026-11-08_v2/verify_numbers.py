#!/usr/bin/env python3
"""Check the report's headline numbers against the shipped data. Standard library only.

Run from the archive root:   python3 verify_numbers.py

Every check prints the value the report states and the value recomputed from the data files,
and PASS or FAIL. The point is that a reader does not have to trust either the report or the
scripts: the numbers in the report are recomputed here from the records the scripts wrote.

Nothing here recomputes theta from a knot; that needs SnapPy and the KnotInfo table and is what
code/ is for. What is checked is every number the report quotes as coming from one of the data
files, plus the census totals the census part of the project rests on.
"""
import json
import math
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
# the scripts read and write under .scratch/; the archive ships that tree as scratch/
for cand in ('.scratch', 'scratch'):
    D = os.path.join(BASE, cand)
    if os.path.isdir(D):
        break
else:
    sys.exit('no scratch/ or .scratch/ directory next to this script')

fails = []


def check(name, got, want, tol=0):
    if isinstance(want, float) and isinstance(got, float):
        ok = abs(got - want) <= tol
    else:
        ok = got == want
    print(f'  {"PASS" if ok else "FAIL"}  {name}: report {want!r}, data {got!r}')
    if not ok:
        fails.append(name)


def lines(name):
    p = os.path.join(D, name)
    with open(p) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def load(name):
    with open(os.path.join(D, name)) as fh:
        return json.load(fh)


def median(xs):
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    sa = math.sqrt(sum((x - ma) ** 2 for x in a))
    sb = math.sqrt(sum((x - mb) ** 2 for x in b))
    return sum((a[i] - ma) * (b[i] - mb) for i in range(n)) / (sa * sb)


def spearman(a, b):
    return pearson(ranks(a), ranks(b))


def r2(y, cols):
    """R^2 of the least-squares fit of y on [1] + cols, by the normal equations."""
    k = len(cols) + 1
    X = [[1.0] + [c[i] for c in cols] for i in range(len(y))]
    A = [[sum(X[m][p] * X[m][q] for m in range(len(y))) for q in range(k)] for p in range(k)]
    b = [sum(X[m][p] * y[m] for m in range(len(y))) for p in range(k)]
    # Gauss-Jordan
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(k):
        piv = max(range(c, k), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]
        d = M[c][c]
        M[c] = [v / d for v in M[c]]
        for r in range(k):
            if r != c and M[r][c]:
                f = M[r][c]
                M[r] = [M[r][j] - f * M[c][j] for j in range(k + 1)]
    coef = [M[i][k] for i in range(k)]
    ys = sum(y) / len(y)
    sst = sum((v - ys) ** 2 for v in y)
    ssr = sum((y[m] - sum(coef[p] * X[m][p] for p in range(k))) ** 2 for m in range(len(y)))
    return 1 - ssr / sst


print('THE CENSUS  (data it writes: census_*.jsonl)')
C = lines('census_upto10.jsonl') + lines('census_11-12.jsonl') + lines('census_13.jsonl')
have = [r for r in C if r.get('tested')]
check('prime knots with a theta value', len(have), 12965)
check('certified theta-zero knots', sum(1 for r in have if r.get('zero')), 78)
fam = {}
for r in have:
    nm = r['knot']
    f = nm.split('_')[0]
    fam[f] = fam.get(f, 0) + 1
for f, n in [('3', 1), ('4', 1), ('5', 2), ('6', 3), ('7', 7), ('8', 21), ('9', 49),
             ('10', 165), ('11a', 367), ('11n', 185), ('12a', 1288), ('12n', 888),
             ('13a', 4878), ('13n', 5110)]:
    check(f'family {f} size', fam.get(f, 0), n)
check('knots whose census value is at (2,3)', sum(1 for r in have if tuple(r['tested'][0][:2]) == (2, 3)), 12577)
check('knots whose census value is at (3,5)', sum(1 for r in have if tuple(r['tested'][0][:2]) == (3, 5)), 388)

print('\nC1 and C2a  THE SYMBOLIC CLAIMS  (scratch/c1_all.txt, scratch/c2a_all.txt)')
c1 = open(os.path.join(D, 'c1_all.txt')).read()
for probe in ['equals exp(2 pi i /3): True', 'equals exp(4 pi i/3): True',
              'is a primitive cube root (value^3 = 1, value != 1): True True',
              't(t(z)) = 1 - 1/z check: True', 'identically 1: True',
              '-> |G| = 1 exactly on Im z = 0']:
    check(f'c1 output has "{probe[-32:]}"', probe in c1, True)
c2a = open(os.path.join(D, 'c2a_all.txt')).read()
for probe in ['equals -sqrt(3)/4 ? True', 'equal exactly: True', 'c = lam / |G\'(w)|^2 = 3*sqrt(3)/4']:
    check(f'c2a output has "{probe[-32:]}"', probe in c2a, True)

print('\nC8  THE MUTANT BENCHMARK  (scratch/c8_verdicts.json)')
V = load('c8_verdicts.json')
check('mutant groups', len(V), 865)
check('knot positions', sum(len(r['group']) for r in V), 1841)
for k, n in [('separated', 682), ('partly', 38), ('equal', 145)]:
    check(f'groups "{k}"', sum(1 for r in V if r['verdict'] == k), n)
check('unseparated: value shared exactly', sum(1 for r in V if r.get('share') == 'identical'), 124)
check('unseparated: value shared up to sign', sum(1 for r in V if r.get('share') == 'up to sign'), 21)
check('groups whose members theta distinguishes', sum(1 for r in V if r['verdict'] in ('separated', 'partly')), 720)
cross = lambda n: int(''.join(ch for ch in n.split('_')[0] if ch.isdigit()))
le12 = [r for r in V if all(cross(n) <= 12 for n in r['group'])]
check('groups through 12 crossings', len(le12), 91)
check('  of those, distinguished', sum(1 for r in le12 if r['verdict'] in ('separated', 'partly')), 86)
check('unseparated groups that are pairs', sum(1 for r in V if r['verdict'] == 'equal' and len(r['group']) == 2), 145)
check('unseparated groups of size > 2', sum(1 for r in V if r['verdict'] == 'equal' and len(r['group']) > 2), 0)
Z = {r['knot'] for r in have if r.get('zero')}
check('group members that are theta-zero knots', sum(1 for r in V for n in r['group'] if n in Z), 0)

print('\nC2b  THE BOWL LAW BY ORDER  (scratch/c2_orders.jsonl)')
O = lines('c2_orders.jsonl')
check('knots with a triangulation', len(O), 12941)
for key, med, worst, wknot in [('e0', 11.510, 98.792, '12a_803'), ('e2', 0.265, 19.895, '12a_803'),
                               ('e3', 0.524, 27.208, '13a_3143'), ('e4', 0.107, 11.376, '11a_247')]:
    check(f'median error at order {key[1]} (%)', round(median([100 * r[key] for r in O]), 3), med)
    check(f'  worst error at order {key[1]} (%)', round(max(100 * r[key] for r in O), 3), worst)
    top = max(O, key=lambda r: r[key])
    check(f'  worst knot at order {key[1]}', top['knot'], wknot)

print('\nC2c  THE CERTIFIED BOUND  (scratch/c2_certify.jsonl)')
Q = lines('c2_certify.jsonl')
check('knots certified', len(Q), 12942)
for lim, n in [(0.01, 11585), (0.05, 12907), (0.001, 485)]:
    check(f'error proved below {lim:.1%}', sum(1 for r in Q if r['bound'] < lim), n)
check('median certified bound (%)', round(median([100 * r['bound'] for r in Q]), 3), 0.419)
check('the constant recorded in the file', {r.get('C') for r in Q}, {0.7})

print('\nC2c  THE BALL-ARITHMETIC ENCLOSURE  (scratch/c2_arb_enclosure.json)')
ARB = load('c2_arb_enclosure.json')
check('proved constant', ARB['C'], 0.7)
check('radius covered', ARB['rho1'], 0.9999)
check('cells below 1/2', ARB['region_A_cells'], 14806)
check('squares above 1/2', ARB['region_B_squares'], 606204)
check('squares unresolved', ARB['region_B_unresolved'], 0)
check('largest census shape inside the proved radius', max(r['rho'] for r in Q) <= ARB['rho1'], True)

print('\nC2d  THE CLOSED FORM  (scratch/c2_closed_form.json)')
CF = load('c2_closed_form.json')
check('exact through degree 4', CF['exact_through_degree_4'], True)
check('pairs checked', CF['pairs_checked'], 860)
check('closed form matches the series, difference < 1e-30', CF['max_difference'] < 1e-30, True)
check('nonzero coefficients off the sector', CF['nonzero_off_sector'], 0)
check('imaginary part of every coefficient < 1e-30', CF['max_imaginary_part'] < 1e-30, True)
check('reflection invariance', CF['reflection_invariance'], True)
check('G reflects to its conjugate', CF['G_reflects_to_conj'], True)
check('Gram spectrum of the 3-cycle', CF['gram_spectrum'], ['0', '3', '3'])
check('c = |1-omega|^3/4', CF['c_equals_gap_cubed_over_4'], True)

print('\nC2d  THE SECTOR LEMMA  (scratch/c2_sector.json)')
SEC = load('c2_sector.json')
check('t^3 = id', SEC['t3_is_id'], True)
check('G(t z)/G(z) is a primitive cube root', SEC['primitive_cube_root_1'], True)
check('G(t(t z))/G(z) is a primitive cube root', SEC['primitive_cube_root_2'], True)
check('the derivative formula for dD/dzbar is exact (residual)', SEC['derivative_formula_residual'], '0')
check('the invariance identity in dzbar is exact (residual)', SEC['invariance_residual'], '0')
check('the invariance identity in dz is exact (residual)', SEC['invariance_residual_z'], '0')
check('monomials the a = b mod 3 rule misclassifies', SEC['sector_misclassified'], [])
check('coefficients computed', SEC['coefficients_computed'], 209)
check('  of those, in the +1 sector', SEC['in_plus_sector'], 209)
check('  off the +1 sector', SEC['off_sector'], 0)
check('  to total degree', SEC['max_degree'], 40)
check('the gap |1 - omega| (exact)', SEC['gap'], 'sqrt(3)')
check('  its square', SEC['gap_squared'], '3')
check('the projector acts as 1 on the invariants', SEC['P_on_invariant'], '1')
check('the projector acts as 0 on the other two sectors', SEC['P_on_other'], '0')

print('\nC2d  THE CONSTANT FROM THE GEOMETRY  (scratch/c2_constant.json)')
CON = load('c2_constant.json')
check('c derived from the Lobachevsky sum (exact)', CON['c_derived'], '3*sqrt(3)/4')
check('  its value', round(float(CON['c_derived_numeric']), 12), 1.299038105677)
check('  equal to the Hessian value', CON['agree'], True)
check('Lam second derivative at the regular angle', CON['Lam_second_at_regular'], '-sqrt(3)/3')
check('sum of |c_i|^2 over the three angles', CON['sum_of_modulus_squared'], '9')
check('  each |c_i|^2', CON['modulus_squared_each'], '3')
check('  the three c_i sum to', CON['sum_of_log_derivs'], '0')
check('the identity D = sum of three Lobachevsky terms, worst difference < 1e-25',
      abs(float(CON['identity_worst_difference'])) < 1e-25, True)
check('Lam(pi/3) = V0/3', CON['Lam_at_regular'], CON['V0_over_3'])
check('  -c from the Lobachevsky fit to 5 dp (a fit, not the exact value)',
      round(float(CON['numeric_c_from_angles']), 5), round(float(CON['c_derived_numeric']), 5))

print('\nC2c  THE CERTIFIED BOUND THROUGH THE MUTANT TABLES  (scratch/c2c_mutant_benchmark.json)')
CB = load('c2c_mutant_benchmark.json')
check('mutant groups', len(CB), 865)
check('knot positions', sum(r['n'] for r in CB), 1841)
check('groups proved below 5 % for every member', sum(1 for r in CB if r['uniform5']), 865)
check('groups proved below 1 % for every member', sum(1 for r in CB if r['uniform1']), 709)
check('groups proved below 0.1 % for every member', sum(1 for r in CB if r['uniform01']), 10)
check('groups straddling the 1 % line', sum(1 for r in CB if r['straddle1']), 146)
check('groups with an identical certificate', sum(1 for r in CB if r['equal']), 24)
check('positions in groups proved below 1 %', sum(r['n'] for r in CB if r['uniform1']), 1499)
check('median within-group spread, 3 dp', round(median([r['ratio'] for r in CB]), 3), 1.737)
check('worst within-group spread, 3 dp', round(max(r['ratio'] for r in CB), 3), 58.458)
groups = {n for r in CB for n in r['group']}
over = [r['knot'] for r in Q if r['bound'] >= 0.05]
check('knots of the census the certificate does not reach at 5 %', len(over), 35)
check('  of those, inside a mutant group', sum(1 for k in over if k in groups), 0)

print('\nC5  THE DEFECT  (scratch/c5_defect.jsonl)')
F = lines('c5_defect.jsonl')
check('knots tested', len(F), 8)
check('knots where the continuous part fails', sum(1 for r in F if not r['cont_ok']), 8)
check('knots with a real defect', sorted(r['knot'] for r in F if r['defect_real']), ['4_1', '5_2', '6_3', '8_3'])
check('  of those, k an integer', sorted(r['knot'] for r in F if r['defect_real'] and abs(r['k_re'] - round(r['k_re'])) < 1e-6), ['4_1', '5_2'])
check('  k for 4_1 and 5_2', [round(r['k_re'], 4) for r in F if r['knot'] in ('4_1', '5_2')], [1.0, 3.0])
check('  k for 6_3, 8_3, 3 dp', [round(r['k_re'], 3) for r in F if r['knot'] in ('6_3', '8_3')], [2.916, 2.889])
check('knots with a complex defect', sorted(r['knot'] for r in F if not r['defect_real']), ['6_1', '6_2', '8_1', '8_2'])

print('\nC3/C4  THE SOLUTIONS  (scratch/c3_results.json)')
S = load('c3_results.json')
check('knots solved', len(S), 11)
bad_inside = bad_real = bad_min = 0
rholist = []
for k, sols in S.items():
    inside = [s for s in sols if s['inside']]
    if len(inside) != 1:
        bad_inside += 1
    if inside and min(sols, key=lambda s: s['S']) is not inside[0]:
        bad_min += 1
    for s in sols:
        if s['allreal'] and abs(s['S'] - s['n']) > 1e-9:
            bad_real += 1
    if len(sols) > 2:
        rholist.append(spearman([s['S'] for s in sols], [s['vol'] for s in sols]))
check('knots where the geometric solution is not the only one inside the disk', bad_inside, 0)
check('knots where the geometric solution is not the smallest S', bad_min, 0)
check('all-real solutions with S != n', bad_real, 0)
check('knots with negative rho(S, vol)', sum(1 for r in rholist if r < 0), len(rholist))
check('  median rho, 3 dp', round(median(rholist), 3), -0.988)
flat = [s for s in S['7_7'] if abs(s['vol']) < 1e-9 and not s['allreal']]
finite = [s for s in flat if all(abs(complex(z)) < 1e3 for z in s['z'])]
check('7_7 flat non-real solutions', len(flat), 2)
check('  of those, with all shapes finite', len(finite), 1)
check('  its S, 6 dp', round(finite[0]['S'], 6), 18.113021)
check('  the other one blows up (max |z| > 1e10)', all(abs(complex(z)) > 1e10 for s in flat if s not in finite for z in [max(s['z'], key=lambda w: abs(complex(w)))]), True)

print('\nC3  THE ELEVEN-KNOT TABLE  (scratch/c3_results.json)')
TBL = {'4_1': (2, 2, 0.000000, +2.029883, None),
       '5_2': (3, 3, 0.172214, +2.828122, 52.2605),
       '6_1': (4, 4, 0.741111, +3.163963, 5.0996),
       '6_2': (5, 5, 0.522509, +4.400833, 6.5917),
       '6_3': (6, 4, 0.311978, +5.693021, 9.4749),
       '7_2': (4, 5, 0.604146, +3.331744, 5.0150),
       '7_3': (5, 5, 0.384998, +4.592126, 4.2306),
       '7_4': (6, 5, 0.720319, +5.137941, 4.5905),
       '7_5': (7, 7, 0.505668, +6.443537, 5.0045),
       '7_6': (8, 9, 0.814691, +7.084926, 6.1588),
       '7_7': (8, 8, 0.363464, +7.643375, 6.9744)}
check('the eleven knots of the table are in the file', sorted(S), sorted(TBL))
for k, (n, nsol, Sg, Vg, nextS) in TBL.items():
    if k not in S:
        continue
    sols = S[k]
    geo = [x for x in sols if x['inside']][0]
    got = (geo['n'], len(sols), round(geo['S'], 6), round(geo['vol'], 6))
    want = (n, nsol, Sg, Vg)
    check(f'{k}: n, solutions, geometric S, geometric volume', got, want)
    if nextS is not None:
        out = [x['S'] for x in sols if not x['inside'] and x['vol'] != 0 and x['S'] < 1e6]
        check(f'  {k}: closest non-geometric S, 4 dp', round(min(out), 4), nextS)

print('\nC7  THE CIRCUIT POLYNOMIAL  (scratch/c7_all.txt, the script\'s own output)')
txt = open(os.path.join(D, 'c7_all.txt')).read().splitlines()[0]
check('first line of c7_all.txt', txt.split('Q(1)=det:')[0].strip(), 'alternating knots tested: 6729')
check('  Q(1) = det on', int(txt.split('Q(1)=det:')[1].split()[0]), 6727)
check('  mismatches', int(txt.split('mismatches:')[1].strip()), 2)
check('  and they are', sorted(l.split("'")[1] for l in open(os.path.join(D, 'c7_all.txt')) if 'MISMATCH' in l), ['10_83', '10_86'])

print('\nC6  THE TWO BOOKS, thirteen-crossing column  (scratch/c6_rows.json)')
R = load('c6_rows.json')
check('rows', len(R), 9985)
vol = [r['vol'] for r in R]
climb = [r['climb'] for r in R]
turn = [abs(r['turn']) for r in R]
sig = [abs(float(r['sig'])) for r in R]
cs = [r['cs'] for r in R]
ld = [math.log(float(r['det'])) for r in R]
check('rho(climb, volume), 4 dp', round(spearman(climb, vol), 4), 0.8542)
def resid(y, x):
    n = len(y)
    mx, my = sum(x) / n, sum(y) / n
    sxx = sum((v - mx) ** 2 for v in x)
    b = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / sxx
    return [y[i] - (my + b * (x[i] - mx)) for i in range(n)]

check('partial rho(climb, volume | log det), 4 dp', round(spearman(resid(climb, ld), resid(vol, ld)), 4), 0.6224)
check('R^2 of log det alone, 4 dp', round(r2(vol, [ld]), 4), 0.6323)
check('R^2 with both, 4 dp', round(r2(vol, [ld, climb]), 4), 0.7842)
check('rho(|turn|, |signature|), 4 dp', round(spearman(turn, sig), 4), 0.7887)
check('rho(climb, CS), 3 dp', round(spearman(climb, cs), 3), 0.032)
check('rho(turn, CS), 3 dp', round(spearman([r['turn'] for r in R], cs), 3), -0.020)

print('\nC2b  THE ELEVEN KNOTS, all four orders  (scratch/c2_orders.jsonl)')
BY = {r['knot']: r for r in O}
TABLE = {'4_1': (0.000, 0.000, 0.000, 0.000), '5_2': (7.662, 0.248, 0.097, 0.017),
         '6_1': (28.313, 2.115, 3.241, 0.499), '6_2': (15.312, 0.111, 0.574, 0.112),
         '6_3': (6.967, 0.152, 0.087, 0.006), '7_2': (21.851, 1.704, 0.687, 0.254),
         '7_3': (10.509, 0.382, 0.759, 0.078), '7_4': (18.523, 0.311, 1.202, 0.417),
         '7_5': (10.259, 0.065, 0.864, 0.378), '7_6': (14.603, 0.335, 0.505, 0.028),
         '7_7': (6.230, 0.052, 0.117, 0.019)}
bad = []
for k, want in TABLE.items():
    got = tuple(round(100 * BY[k][f'e{i}'], 3) for i in (0, 2, 3, 4))
    if got != want:
        bad.append((k, got, want))
check('eleven knots whose four orders do not match the table', bad, [])
med = tuple(round(median([100 * BY[k][f'e{i}'] for k in TABLE]), 3) for i in (0, 2, 3, 4))
check('  the median row', med, (10.509, 0.248, 0.574, 0.078))
check('knots where order 3 is worse than order 2', sum(1 for k in TABLE if BY[k]['e3'] > BY[k]['e2']), 7)
check('knots where order 4 is better than order 2', sum(1 for k in TABLE if BY[k]['e4'] < BY[k]['e2']), 7)

print('\nC2b  THE TRIANGULATION COMPARISON  (scratch/c2_tri.jsonl)')
T = lines('c2_tri.jsonl')
by = {}
for r in T:
    if 'rel' in r and 'meanG2' in r:          # some rows record a failed construction instead
        by.setdefault(r['which'], []).append(r)
for which, n, med_, p90, worst, meanG in [('default', 68, 0.360, 0.972, 8.431, 0.094),
                                          ('canonical', 62, 1.446, 8.869, 56.169, 0.236),
                                          ('random', 68, 0.361, 1.231, 8.431, 0.098)]:
    rows = by[which]
    errs = sorted(100 * r['rel'] for r in rows)
    check(f'{which}: knots', len(rows), n)
    check(f'  median (%)', round(median(errs), 3), med_)
    check(f'  90th pct (%)', round(errs[int(0.9 * len(errs)) - 1], 3), p90)
    check(f'  worst (%)', round(errs[-1], 3), worst)
    check(f'  mean |G|^2', round(sum(r['meanG2'] for r in rows) / len(rows), 3), meanG)
rand = {r['knot']: r for r in by['random']}
dfl = {r['knot']: r for r in by['default']}
worse = sum(1 for r in by['canonical'] if r['knot'] in dfl and r['rel'] > dfl[r['knot']]['rel'])
check('canonical worse than the default on n of 62 knots', worse, 52)
allr = by['default'] + by['canonical'] + by['random']
check('pairs in the correlation', len(allr), 198)
check('Spearman(mean |G|^2, error), 3 dp', round(spearman([r['meanG2'] for r in allr], [r['rel'] for r in allr]), 3), 0.750)

print('\nC8  THE COLLISIONS OF THETA ON THE CENSUS  (scratch/c8_collisions.json)')
CO = load('c8_collisions.json')
check('knots at (2,3)', CO['knots_at_23'], 12577)
check('nonzero values', CO['nonzero_at_23'], 12499)
check('distinct values', CO['distinct_values'], 12343)
check('collision classes', CO['collision_classes'], 153)
check('knots in them', CO['knots_in_classes'], 309)
rows = CO['classes']
check('classes that are exactly one equal mutant group', sum(1 for r in rows if r['is_one_equal_group']), 94)
other = [r for r in rows if not r['contains_equal_groups']]
check('classes with no mutant group inside', len(other), 58)
check('  knots in those', sum(len(r['knots']) for r in other), 117)
check('  of those, sharing volume+Alexander+Jones', sum(1 for r in other if r['share_volume_alex_jones']), 43)

print()

if fails:
    print(f'{len(fails)} CHECK(S) FAILED: ' + '; '.join(fails))
    sys.exit(1)
print('every check passed: the numbers in the report are the numbers in the data files.')
