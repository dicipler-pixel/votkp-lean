# SCRIPT: RATE-WEIGHT-DIMER-06
# A LEAD made concrete: is there a projector whose block offset IS the peel log-ratio?
# Construction (mine, not in either paper): for an ordered pair of removal energies a, b put
#   v = (sqrt a, sqrt b),  H = v v^T = [[a, sqrt(ab)], [sqrt(ab), b]]   (a two-site dimer whose hopping is the
#   geometric mean of the two site energies).  H has eigenvalues 0 and a + b.  Let P be the projector on the
#   zero mode, u = (sqrt b, -sqrt a)/sqrt(a+b).  Then the site-1 block of P is C1 = b/(a+b) and site 2 is
#   C2 = a/(a+b), so the offset of site 2 is tau = ln((1-C2)/C2) = ln(b/a) = ln z = 2h, the peel rapidity,
#   and the site imbalance 1 - 2 C2 = (b-a)/(a+b) = Gamma.
# In ordinary dimer language the imbalance Delta/sqrt(Delta^2 + 4t^2) with Delta = b - a, t = sqrt(ab) gives
# Delta^2 + 4t^2 = (a+b)^2, which is why Gamma comes out.  The wall Gamma^2 = 1/2 is |Delta| = 2t.
# WHY THE CHECK PROVES THE CONSTRUCTION: sympy verifies each statement as an identity in positive a, b.
# It does NOT show that this dimer is physical for an atom; that is the open part of the lead.
# KILL CONDITION: any residual not identically zero.
import sympy as sp

a, b = sp.symbols('a b', positive=True)
H = sp.Matrix([[a, sp.sqrt(a * b)], [sp.sqrt(a * b), b]])
u = sp.Matrix([sp.sqrt(b), -sp.sqrt(a)]) / sp.sqrt(a + b)
P = u * u.T
res = {
    'H u = 0': sp.simplify(H * u),
    'eigenvalues': H.eigenvals(),
    'P^2 - P': sp.simplify(P * P - P),
    'C2 - a/(a+b)': sp.simplify(P[1, 1] - a / (a + b)),
    'offset(site 2) - ln(b/a)': sp.simplify(sp.expand_log(sp.log((1 - P[1, 1]) / P[1, 1]) - sp.log(b / a), force=True)),
    'imbalance - Gamma': sp.simplify((1 - 2 * P[1, 1]) - (b / a - 1) / (b / a + 1)),
    'census C - C^2 = |P12|^2': sp.simplify(P[1, 1] - P[1, 1] ** 2 - P[0, 1] ** 2),
    'Delta^2 + 4t^2 - (a+b)^2': sp.simplify((b - a) ** 2 + 4 * a * b - (a + b) ** 2),
}
for k, v in res.items():
    print(f'{k:28s} {v}')
z = sp.symbols('z', positive=True)
wall = sp.solve(sp.Eq((z - 1) ** 2, 4 * z), z)
print('wall |Delta| = 2t with a = 1, b = z  ->  (z-1)^2 = 4z  ->  z =', wall, [float(w) for w in wall])
bad = any(v not in (0, sp.zeros(2, 1), sp.zeros(2, 2)) for k, v in res.items() if k != 'eigenvalues')
print('KILL', 'FIRED' if bad else 'not fired')
