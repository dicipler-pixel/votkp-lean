# SCRIPT: CHECK-GRAVITY-05-SCALE-RECORD
# Gravity paper against the Loop Wall element paper: scale, the additive record, and the crossing class.
# (a) Gravity Edition 6/7 Prop 30: under K -> alpha K the projector and its metric are unchanged and
#     the selected trace-log shifts by k log alpha. Element analogue: a common rescaling of every
#     ionization energy (any unit change) leaves every z, every Gamma and every wall call unchanged,
#     while the ladder record sum_k ln IE_k shifts by n ln alpha. The peel ratio is the scale-free
#     part of the trace-log of the ladder (ln z_k = ln IE_{k+1} - ln IE_k; the half-step telescopes).
# (b) Record additive, reflection bounded: ln z adds under composition of steps while Gamma composes by
#     Einstein addition, Gamma(A) (+) Gamma(B) = Gamma(AB) (Two Trees gam_mul) and stays inside (-1, 1).
# (c) Crossing class (gravity final_v3 Result 16): the loop-wall margin 1 - 2 Gamma^2 has a simple zero
#     at z* = 3 + 2 sqrt2 (transverse crossing, sign change), and the soft eigenvalue 1 - |w| of the
#     two-face Hermitian form vanishes linearly, so its square root has exponent 1/2 (the indefinite,
#     crossing class), while the real-part form [[1, G],[G, 1]] never reaches zero (G^2 < 1).
# (d) Negative check: the Two Trees ln 5 commutator (cos phi = -527/625) against gravity Prop 12's wrap:
#     eigenvalues 1, 1, e^{+-i phi} give winding sum 0, so the wrap carries no integer here.
#
# WHY THIS PROVES WHAT IT CLAIMS. (a) recomputes every adjacent ratio in the archive at alpha = 1 and
# at alpha = 1/27.211386 (eV -> hartree) and alpha = 1000 and compares exactly (Fractions), so any
# change of a single wall call would show. (b) compares both sides of the composition law on random
# ratios. (c) fits the exponent of sqrt(1 - |w|) on a path through the wall. (d) computes the wrap
# directly. Kill conditions (before the run): any changed call in (a); residual > 1e-12 in (b);
# exponent outside 0.50 +- 0.02 in (c).
import gzip, json, sys, math
from fractions import Fraction as F
import numpy as np

d = json.load(gzip.open(sys.argv[1])); rec = {r['Z']: r for r in d['records']}
def gam(z): return (z - 1) / (z + 1)
def outside(z): return z > 3 and (z - 3) * (z - 3) > 8

# (a)
steps = []; records = []
for Z, r in rec.items():
    th = sorted(r['thresholds'], key=lambda t: t['q'])
    E = [F(repr(t['IE_eV'])) for t in th]
    qs = [t['q'] for t in th]
    for (qa, a), (qb, b) in zip(zip(qs, E), zip(qs[1:], E[1:])):
        if qb == qa + 1: steps.append((Z, a, b))
    records.append(E)
changed = 0
for alpha in (F(1, 1) / F('27.211386245981'), F(1000)):
    for Z, a, b in steps:
        if gam(b / a) != gam((alpha * b) / (alpha * a)) or outside(b / a) != outside((alpha * b) / (alpha * a)): changed += 1
nout = sum(1 for Z, a, b in steps if outside(b / a))
print('(a) adjacent steps in archive:', len(steps), '; outside:', nout, '; Gamma or wall call changed by rescaling:', changed)
# record shift: sum ln(alpha E) - sum ln E = n ln alpha ; telescoping sum ln z_k = ln(E_last/E_first)
alpha = 1000.0; worst_shift = 0.0; worst_tel = 0.0
for E in records:
    Ef = [float(x) for x in E]
    worst_shift = max(worst_shift, abs(sum(math.log(alpha * x) for x in Ef) - sum(math.log(x) for x in Ef) - len(Ef) * math.log(alpha)))
    if len(Ef) > 1:
        tel = sum(math.log(b / a) for a, b in zip(Ef, Ef[1:]))
        worst_tel = max(worst_tel, abs(tel - math.log(Ef[-1] / Ef[0])))
print('    record shift residual (n ln alpha):', f'{worst_shift:.1e}', '; telescoping residual:', f'{worst_tel:.1e}')

# (b)
rng = np.random.default_rng(3); worst = 0.0
for _ in range(10000):
    A, B = rng.uniform(1, 50, 2)
    ga, gb = (A - 1) / (A + 1), (B - 1) / (B + 1)
    worst = max(worst, abs((ga + gb) / (1 + ga * gb) - (A * B - 1) / (A * B + 1)))
print('(b) Einstein addition Gamma(A)(+)Gamma(B) = Gamma(AB): worst residual', f'{worst:.1e}')

# (c)
zs = 3 + 2 * math.sqrt(2)
dG2 = 4 * (zs - 1) / (zs + 1) ** 3          # d(Gamma^2)/dz at z*
print('(c) d(Gamma^2)/dz at z* =', round(dG2, 9), '(nonzero: simple zero, transverse crossing)')
eps = np.logspace(-8, -2, 13); soft = []
for e in eps:
    G = math.tanh(0.5 * math.log(zs * (1 - e)))       # approach from inside along the equal-face diagonal
    w = complex(G, G); soft.append(math.sqrt(1 - abs(w)))
expo = np.polyfit(np.log(eps), np.log(soft), 1)[0]
print('    exponent of sqrt(soft eigenvalue) approaching the wall =', round(expo, 5),
      '; real-part form min eigenvalue at the wall 1 - G =', round(1 - math.tanh(0.5 * math.log(zs)), 6))

# (d)
cphi = F(-527, 625); c_half = F(7, 25)
assert 2 * c_half * c_half - 1 == cphi
phi = math.acos(float(cphi)); ev = np.array([1, 1, np.exp(1j * phi), np.exp(-1j * phi)])
w = sum(np.angle(ev)) / (2 * math.pi)
print('(d) ln 5 commutator: det =', round(abs(np.prod(ev)), 12), ' winding sum =', round(w, 12),
      '; branch distance g = min|lambda+1| =', round(min(abs(ev + 1)), 6), '= 14/25 =', 14 / 25)
