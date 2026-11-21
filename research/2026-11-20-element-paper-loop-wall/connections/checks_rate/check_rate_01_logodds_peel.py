# SCRIPT: RATE-WEIGHT-LOGODDS-PEEL-01
# Connection tested: the per-eigenvalue offset of The Offset Speed Limit, tau_nu = log((1-nu)/nu),
# with asymmetry 1 - 2nu = tanh(tau_nu/2) (its eq. (10), Appendix B), and the peel step of
# The Loop Wall, z = b/a, Gamma = (z-1)/(z+1) = tanh(h), h = (1/2) ln z.
#
# WHY THIS PROVES IT. Put nu := a/(a+b) (the lower threshold's share of the pair). Then
# (1-nu)/nu = b/a = z identically, so tau_nu = ln z = 2h, and every other identity follows by algebra.
# Part A checks each identity symbolically with sympy: an expression that simplifies to exactly 0
# for symbolic positive a, b is an identity for all positive inputs, not a numerical coincidence.
# Part B is an implementation check: classifying every archive step by the offset-paper variables
# (census nu(1-nu) against 1/8, or S = 1/(nu(1-nu)) against 8) must give exactly the same calls as
# the element paper's z against 3 + 2 sqrt2. Part B proves nothing new; it guards against a slip.
#
# KILL CONDITIONS (written before running):
#   K1 any sympy residual not identically 0;
#   K2 any archive step or anion rung whose call differs between the two languages;
#   K3 the count of ordinary outside steps from hydrogen to astatine differs from 8 (the paper's count).
import sys, gzip, json, math
import sympy as sp

a, b = sp.symbols('a b', positive=True)
z = b / a
nu = a / (a + b)
Gam = (z - 1) / (z + 1)
h = sp.log(z) / 2
checks = {
    'tau_nu = ln z = 2h': sp.log((1 - nu) / nu) - 2 * h,
    'asymmetry 1-2nu = Gamma': (1 - 2 * nu) - Gam,
    'census nu(1-nu) = (1-Gamma^2)/4': nu * (1 - nu) - (1 - Gam**2) / 4,
    'S = 1/(nu(1-nu)) = 4 cosh^2 h': 1 / (nu * (1 - nu)) - 4 * sp.cosh(h)**2,
    'complement nu->1-nu is z->1/z (Gamma -> -Gamma)': (1 - 2 * (1 - nu)) + Gam,
    'sinh^2 h = Gamma^2/(1-Gamma^2)': sp.sinh(h)**2 - Gam**2 / (1 - Gam**2),
}
print('Part A: symbolic identities (residual must be 0)')
bad = 0
for name, expr in checks.items():
    r = sp.simplify(sp.expand(sp.expand_log((expr.rewrite(sp.exp)), force=True)))
    r = sp.simplify(r)
    ok = (r == 0)
    bad += not ok
    print(f'  {name:52s} residual = {r}')

# the wall in the offset variables
G2 = sp.Rational(1, 2)
print('  at Gamma^2 = 1/2: census nu(1-nu) =', sp.nsimplify((1 - G2) / 4),
      '(half of the half-filling maximum 1/4); S =', 4 / (1 - G2),
      '; tau = ln(3+2sqrt2) =', sp.nsimplify(sp.log(3 + 2 * sp.sqrt(2))), '=', float(sp.log(3 + 2 * sp.sqrt(2))),
      '; 2 asinh(1) =', float(2 * sp.asinh(1)))
print('  wall nu = (1 - 1/sqrt2)/2 =', float((1 - 1 / sp.sqrt(2)) / 2),
      '; 4 nu(1-nu) = (1-2nu)^2 there:', sp.simplify(4 * ((1 - 1/sp.sqrt(2))/2) * ((1 + 1/sp.sqrt(2))/2) - (1/sp.sqrt(2))**2) == 0)

# Part B: archive
d = json.load(gzip.open(sys.argv[1]))
rec = {r['Z']: r for r in d['records']}
W = 3 + 2 * math.sqrt(2)
n_steps = n_out = n_dis = 0
outs = []
minS_in, maxS_out = 0, 1e9
for Z in range(1, 86):
    th = sorted(rec[Z]['thresholds'], key=lambda x: x['q'])
    E = [x['IE_eV'] for x in th if x.get('IE_eV') is not None]
    for k in range(len(E) - 1):
        A, B = E[k], E[k + 1]
        zz = B / A
        v = A / (A + B)
        S = 1 / (v * (1 - v))
        side_z = zz > W
        side_census = v * (1 - v) < 1 / 8
        side_S = S > 8
        n_steps += 1
        n_dis += (side_z != side_census) or (side_z != side_S)
        if side_z:
            n_out += 1
            outs.append((rec[Z]['name'], k + 1, round(zz, 6), round(S, 4)))
print(f'Part B: {n_steps} ordinary steps H..At, outside {n_out}, disagreements between languages {n_dis}')
for o in outs:
    print('   outside:', o[0], 'step', o[1], 'z', o[2], 'S', o[3])

EA = {'H':0.754195,'Li':0.618049,'B':0.279723,'C':1.2621226,'O':1.4611136,'F':3.4011898,'Na':0.547926,
      'Al':0.43283,'Si':1.3895212,'P':0.746609,'S':2.0771042,'Cl':3.612725,'K':0.501459,'Ca':0.02455,
      'Sc':0.17938,'Ti':0.07554,'V':0.52766,'Cr':0.675928,'Fe':0.153236,'Co':0.662255,'Ni':1.157368,'Cu':1.23578,
      'Ga':0.301166,'Ge':1.2326764,'As':0.804486,'Se':2.020667,'Br':3.363588,'Rb':0.485916,'Sr':0.05206,
      'Y':0.31129,'Zr':0.433283,'Nb':0.91740,'Mo':0.74723,'Tc':0.636,'Ru':1.046270,'Rh':1.14273,
      'Pd':0.56214,'Ag':1.30447,'In':0.38392,'Sn':1.112070,'Sb':1.047401,'Te':1.970875,'I':3.0590465,'Cs':0.471626}
na = nd = 0
rows = []
for Z in range(1, 56):
    s = rec[Z]['symbol']
    if s not in EA:
        continue
    I = {x['q']: x['IE_eV'] for x in rec[Z]['thresholds']}[0]
    A = EA[s]
    v0 = A / (I + A)
    S0 = 1 / (v0 * (1 - v0))
    eta, chi = (I - A) / 2, (I + A) / 2
    omega = chi * chi / (2 * eta)
    na += 1
    nd += ((I / A > W) != (S0 > 8)) or ((S0 > 8) != (omega < eta))
    rows.append((S0, rec[Z]['name'], I / A, omega / eta, 4 * chi * chi / (chi * chi - eta * eta)))
print(f'Part B anions: {na} bound anions H..Cs (same affinities as check_hardness_electrophilicity_v1), disagreements {nd}')
for r in sorted(rows)[:14]:
    print(f'   {r[1]:10s} S0 = {r[0]:8.4f}  (4chi^2/(chi^2-eta^2) = {r[4]:8.4f})  z0 {r[2]:7.4f}  omega/eta {r[3]:.4f}')
print('KILL K1', 'FIRED' if bad else 'not fired', '| K2', 'FIRED' if (n_dis or nd) else 'not fired',
      '| K3', 'FIRED' if n_out != 8 else 'not fired')
