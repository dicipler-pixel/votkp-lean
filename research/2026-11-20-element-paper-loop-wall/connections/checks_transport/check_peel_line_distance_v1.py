# SCRIPT: WTK-LOOPWALL-PEEL-LINE-DISTANCE-01
"""
Connection: WTK section 6 (||P_v - P_w||_F^2 = 2 sin^2 theta, the projective separation
used by the capacity census, Proposition 8) and the element paper's returned power Gamma^2.

Why this check proves what it claims:
 - Encode a peel step a -> b (z = b/a) as the real line through (sqrt b, sqrt a); its
   reverse b -> a is the line through (sqrt a, sqrt b), the mirror image under the swap.
   The first line makes angle alpha with tan alpha = 1/sqrt z, the second 90 deg - alpha,
   so the projective angle between them is theta = 90 deg - 2 alpha and
   sin^2 theta = cos^2(2 alpha) = ((z-1)/(z+1))^2 = Gamma^2 (exact trigonometry).
   Sympy must reduce (1/2)||P_fwd - P_rev||_F^2 - Gamma^2 to zero.
 - Then the wall Gamma^2 = 1/2 is WTK's separation threshold epsilon = 1/2 (theta = 45 deg),
   the boundary-safe census value at which the real projective line holds exactly 4 lines.
   The sign of Gamma is the orientation of the turn from the reversed line to the forward
   one; the WTK distance itself cannot see it (it is symmetric in the two lines).
 - Archive spot check: silicon's anion rung (outside) and silver's (inside) must sit on
   opposite sides of separation 1/2.
"""
import sympy as sp, numpy as np, math
a, b = sp.symbols('a b', positive=True)
def P(v):
    v = sp.Matrix(v); return v*v.T/(v.T*v)[0]
Pf = P([sp.sqrt(b), sp.sqrt(a)]); Pr = P([sp.sqrt(a), sp.sqrt(b)])
D = Pf - Pr
half_frob = sp.simplify(sum(D[i, j]**2 for i in range(2) for j in range(2))/2)
print('(1/2)||P_fwd - P_rev||_F^2 =', sp.factor(half_frob))
print('minus Gamma^2 = ((b-a)/(b+a))^2  ->', sp.simplify(half_frob - ((b - a)/(b + a))**2))
print('WTK capacity of RP^1 at epsilon = 1/2: floor(pi/arcsin(sqrt(1/2))) =', sp.floor(sp.pi/sp.asin(sp.sqrt(sp.Rational(1, 2)))))
def sep(IEb, IEa):
    vf = np.array([math.sqrt(IEb), math.sqrt(IEa)]); vr = vf[::-1]
    pf = np.outer(vf, vf)/vf.dot(vf); pr = np.outer(vr, vr)/vr.dot(vr)
    return 0.5*np.linalg.norm(pf - pr)**2
for name, IE, EA in [('silicon anion rung', 8.15168, 1.3895212), ('silver anion rung', 7.576234, 1.30447)]:
    s = sep(IE, EA)
    print(f'  {name}: separation = {s:.8f}  ({"above" if s > 0.5 else "below"} 1/2)')
