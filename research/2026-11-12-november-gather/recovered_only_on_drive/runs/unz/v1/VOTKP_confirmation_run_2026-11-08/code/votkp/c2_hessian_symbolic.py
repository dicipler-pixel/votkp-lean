# SCRIPT: c2_hessian_symbolic
"""C2 (algebraic half). The Hessian of D at w, derived exactly.

Write D in terms of z and its conjugate Z as independent variables:
    D = (Li2(z) - Li2(Z))/(2i) + (Log(1-z) - Log(1-Z)) (Log z + Log Z)/(4i).
Since D is real-analytic and the quadratic part is forced isotropic by 3-fold symmetry,
the Hessian is determined by the single mixed derivative  lam = -d^2 D/dz dZ at z = w.
We compute lam in closed form and then convert to the G coordinate, where
    D = V0 - c|G|^2 + ...,  c = lam / |G'(w)|^2.
"""
import sympy as sp

z, Z = sp.symbols('z Z')
I = sp.I
w  = sp.Rational(1,2) + I*sp.sqrt(3)/2
wb = sp.Rational(1,2) - I*sp.sqrt(3)/2

D = (sp.polylog(2, z) - sp.polylog(2, Z))/(2*I) \
    + (sp.log(1-z) - sp.log(1-Z))*(sp.log(z) + sp.log(Z))/(4*I)

mixed = sp.diff(D, z, Z)
print("d^2 D / dz dZ  =", sp.simplify(mixed))
val = sp.simplify(mixed.subs({z: w, Z: wb}))
print("at z = w       =", sp.nsimplify(sp.simplify(val)))
print("   numeric     =", complex(sp.N(val, 30)))
print("   equals -sqrt(3)/4 ?", sp.simplify(val + sp.sqrt(3)/4) == 0)
lam = -val
print("lam = -d^2D/dz dZ at w =", sp.simplify(lam), " =", sp.N(lam, 20))
print()

# G'(w): G(z) = (z-w)/(z-wb), G'(z) = (w-wb)/(z-wb)^2
Gp = (w - wb)/(w - wb)**2
Gp = sp.simplify(Gp)
print("G'(w) =", Gp, "   |G'(w)| =", sp.N(sp.Abs(Gp), 20))
print("1/|G'(w)|^2 =", sp.simplify(1/sp.Abs(Gp)**2))
c = sp.simplify(lam * sp.Abs(Gp)**2)   # lam / |G'(w)|^2 with |G'|^2 = 1/3 -> c = 3 lam
c = sp.simplify(lam / sp.Abs(Gp)**2)
print()
print("c = lam / |G'(w)|^2 =", c, "=", sp.N(c, 25))
print("3 sqrt(3)/4         =", sp.N(3*sp.sqrt(3)/4, 25))
print("equal exactly:", sp.simplify(c - 3*sp.sqrt(3)/4) == 0)
print()
print("So in the z coordinate:  D = V0 - (sqrt(3)/4)|z-w|^2 + O(|z-w|^3)")
print("and in the G coordinate: D = V0 - (3 sqrt(3)/4)|G|^2 + O(|G|^3)")
