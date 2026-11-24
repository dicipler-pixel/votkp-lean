# SCRIPT: HYDROGEN-EXACT-RUNGS-01
# Exact rungs -1 to -6 for the hydrogen ground state, by solving the ladder equations in closed form.
# (H0 - E0) acting on the angular-momentum-one radial channel:  L u = -u''/2 + u/r^2 - u/r + u/2.
# G0 = r*u0 with u0 = 2 r exp(-r);  L G1 = G0;  L G2 = G1;  L G3 = G2.  Rungs: S(-1) = (2/3)<G0|G0>, S(-2) = (2/3)<G0|G1>,
# S(-3) = (2/3)<G1|G1>, S(-4) = (2/3)<G1|G2>, S(-5) = (2/3)<G2|G2>, S(-6) = (2/3)<G2|G3>.
# KILL LINE: the claimed values 9673/144 and 297541/1728 must come out exactly; otherwise they failed this way.
import sympy as sp
r = sp.symbols('r', positive=True)
L = lambda u: -sp.diff(u, r, 2)/2 + u/r**2 - u/r + u/2
def solve(rhs_poly, deg):
    c = sp.symbols('c2:%d' % (deg + 1)); P = sum(ci*r**(i + 2) for i, ci in enumerate(c))
    eq = sp.expand(sp.simplify(L(P*sp.exp(-r))*sp.exp(r)) - rhs_poly)
    sol = sp.solve(sp.Poly(eq, r).all_coeffs(), c, dict=True)[0]
    return sp.expand(P.subs(sol))
G = [2*r**2]
for k in range(3): G.append(solve(G[-1], sp.degree(G[-1], r) + 1))
ip = lambda a, b: sp.Rational(2, 3)*sp.integrate(a*b*sp.exp(-2*r), (r, 0, sp.oo))
vals = {-1: ip(G[0], G[0]), -2: ip(G[0], G[1]), -3: ip(G[1], G[1]), -4: ip(G[1], G[2]), -5: ip(G[2], G[2]), -6: ip(G[2], G[3])}
for k in sorted(vals, reverse=True): print('S(%d) = %s = %.9f' % (k, vals[k], float(vals[k])))
print('claimed: 9673/144 ->', vals[-5] == sp.Rational(9673, 144), '   297541/1728 ->', vals[-6] == sp.Rational(297541, 1728))
