# SCRIPT: c2_constant
"""C2d(ii): the constant c = 3 sqrt3 / 4 from the tetrahedron's geometry, not from the dilogarithm's Hessian.

The Hessian route (C2a) differentiates D twice at w. This route never differentiates the dilogarithm.
It uses the classical identity that the volume of an ideal tetrahedron is a sum of three Lobachevsky
functions of its three dihedral angles,

    D(z) = Lam(t1) + Lam(t2) + Lam(t3),      Lam(t) = -int_0^t log|2 sin u| du,
    t1 = arg z,   t2 = arg(1/(1-z)),   t3 = arg((z-1)/z),   t1 + t2 + t3 = pi,

and expands. Everything that follows is geometry: the curvature of Lam at the regular angle, the
rate at which the three angles turn in the quotient coordinate G, and the fact that the three are
permuted by the 3-cycle.

  * first order vanishes because t1 + t2 + t3 = pi identically -- no linear term, derived;
  * second order is (Lam''(pi/3)/2) * sum_i (dt_i)^2 with Lam''(pi/3) = -cot(pi/3) = -1/sqrt3;
  * each dt_i = Im(c_i G) + O(G^2) with c_i = d/dG log(ratio_i) at G = 0, so as a function of
    (G, Gbar) we have dt_i = alpha_i G + conj(alpha_i) Gbar with alpha_i = c_i/(2i);
  * hence the G*Gbar coefficient of D is -(1/sqrt3) sum_i |alpha_i|^2, i.e.

        c = (1/sqrt3) sum_i |alpha_i|^2 = (1/(4 sqrt3)) sum_i |c_i|^2.

  * the three c_i have modulus sqrt3 and sum to zero -- they are the 3-cycle acting on the three
    angles -- so sum |c_i|^2 = 9 and c = 9/(4 sqrt3) = 3 sqrt3 / 4.

The geometry reads: sqrt3 is |dz/dG| at the branch point of the quotient (so |c_i| = sqrt3 is how
fast an angle turns per unit of the disk coordinate), the 3 is the number of angles, and
cot(pi/3) is the second derivative of the volume with respect to a dihedral angle at the regular
tetrahedron.
"""
import sys, json
sys.path.insert(0, 'code')
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
I = sp.I
w = sp.Rational(1, 2) + sp.sqrt(3)*I/2
wb = sp.Rational(1, 2) - sp.sqrt(3)*I/2
g = sp.symbols('g')
z = (w - g*wb)/(1 - g)

out = {}

# ---- the three dihedral angles and their logarithmic derivatives at G = 0 ------------------
ratios = {'arg z': z,
          'arg 1/(1-z)': 1/(1 - z),
          'arg (z-1)/z': (z - 1)/z}
c = []
for name, r in ratios.items():
    ci = sp.simplify(sp.diff(sp.log(r), g).subs(g, 0))
    c.append(ci)
    print(f'  c for {name:14s} = {sp.nsimplify(sp.simplify(ci))}   modulus {sp.simplify(sp.Abs(ci))}'
          f'   modulus^2 {sp.simplify(sp.Abs(ci)**2)}')
out['log_derivs'] = [str(sp.nsimplify(sp.simplify(x))) for x in c]
out['modulus_squared_each'] = str(sp.simplify(sp.Abs(c[0])**2))
assert all(sp.simplify(sp.Abs(ci)**2 - 3) == 0 for ci in c), 'the three moduli are not all 3'
out['sum_of_log_derivs'] = str(sp.simplify(sum(c)))
out['sum_of_modulus_squared'] = str(sp.simplify(sum(sp.Abs(ci)**2 for ci in c)))
assert sp.simplify(sum(c)) == 0

# the angles are permuted by the 3-cycle: under G -> omega G the three c_i rotate into one another
omega = sp.Rational(-1, 2) + sp.sqrt(3)*I/2
rot = [sp.simplify(omega*ci) for ci in c]
print('  the three c_i sum to', sp.simplify(sum(c)), ', each of modulus', sp.simplify(sp.Abs(c[0])),
      '-- i.e. they sit 120 degrees apart, as the 3-cycle requires')

# ---- the constant ----------------------------------------------------------------------------
cot = sp.simplify(1/sp.tan(sp.pi/3))
Lam2 = sp.simplify(-cot)                       # Lam''(pi/3) = -cot(pi/3)
c_star = sp.simplify(-Lam2/(4) * sum(sp.Abs(ci)**2 for ci in c))
out['Lam_second_at_regular'] = str(Lam2)
out['c_derived'] = str(sp.nsimplify(sp.simplify(c_star)))
out['c_derived_numeric'] = str(sp.N(c_star, 20))
print(f"\n  Lam''(pi/3) = {Lam2} = -1/sqrt3;   sum_i |c_i|^2 = {sp.simplify(sum(sp.Abs(ci)**2 for ci in c))}")
print(f"  c = -Lam''(pi/3)/4 * sum |c_i|^2 = {sp.nsimplify(sp.simplify(c_star))} = {sp.N(c_star, 20)}")
print(f"  the Hessian value 3 sqrt3/4          = {sp.N(3*sp.sqrt(3)/4, 20)}")
print('  agree:', sp.simplify(c_star - 3*sp.sqrt(3)/4) == 0)
out['c_hessian'] = str(sp.nsimplify(3*sp.sqrt(3)/4))
out['agree'] = bool(sp.simplify(c_star - 3*sp.sqrt(3)/4) == 0)

# ---- numerical confirmation from the Lobachevsky route, with no dilogarithm anywhere -------
def Lam_num(t):
    return -mp.quad(lambda u: mp.log(abs(2*mp.sin(u))), [0, t])


def D_from_angles(zz):
    t1 = mp.arg(zz)
    t2 = -mp.arg(1 - zz)
    t3 = mp.pi - t1 - t2
    return Lam_num(t1) + Lam_num(t2) + Lam_num(t3), (t1, t2, t3)


Ws = mp.expjpi(mp.mpf(1)/3)          # the same point, in mpmath
Wbs = mp.expjpi(-mp.mpf(1)/3)


def z_of(G):
    return (Ws - G*Wbs)/(1 - G)


# the identity D = sum of three Lobachevsky terms
worst = mp.mpf(0)
for zz in [mp.mpc(2j), mp.mpc(0.3, 1.7), mp.mpc(-1.4, 0.8), Ws, mp.mpc(3, 0.2)]:
    s, _ = D_from_angles(zz)
    ref = mp.im(mp.polylog(2, zz)) + mp.arg(1 - zz)*mp.log(abs(zz))
    worst = max(worst, abs(s - ref))
out['identity_worst_difference'] = mp.nstr(worst, 5)
print(f'\n  D = Lam(t1)+Lam(t2)+Lam(t3): largest difference from the dilogarithm {mp.nstr(worst, 4)}')

# the coefficients of the expansion, computed from the Lobachevsky route
def coeffs(radii=(0.02, 0.04, 0.08), nang=12):
    """Least squares for V0, -c, cubic, quartic from D(polar form), using several radii so that
    the constant and the rho^4 column are distinguishable."""
    import math
    rows, rhs = [], []
    for rho in radii:
        for k in range(nang):
            th = 2*math.pi*k/nang
            G = mp.mpf(rho)*mp.expj(th)
            val, _ = D_from_angles(z_of(G))
            rows.append([mp.mpf(1), mp.mpf(rho)**2, mp.mpf(rho)**3*mp.cos(3*th), mp.mpf(rho)**4])
            rhs.append(val)
    A = mp.matrix(rows)
    b = mp.matrix(rhs)
    At = A.T
    return mp.lu_solve(At*A, At*b)


sol = coeffs()
print(f'  from the Lobachevsky route:  V0 = {mp.nstr(sol[0], 14)}   -c = {mp.nstr(sol[1], 14)}'
      f'   cubic = {mp.nstr(sol[2], 12)}   quartic = {mp.nstr(sol[3], 12)}')
out['numeric_c_from_angles'] = mp.nstr(-sol[1], 14)
out['numeric_cubic_from_angles'] = mp.nstr(sol[2], 12)
out['numeric_quartic_from_angles'] = mp.nstr(sol[3], 12)
out['numeric_V0_from_angles'] = mp.nstr(sol[0], 14)
# the third column is the coefficient of rho^3 cos 3 theta, i.e. of Re(G^3), which is sqrt3/4
print(f'  known:            V0 = {mp.nstr(mp.im(mp.polylog(2, Ws)), 12)}'
      f'   -c = {mp.nstr(-3*mp.sqrt(3)/4, 14)}   cubic = {mp.nstr(mp.sqrt(3)/4, 12)}'
      f'   quartic = {mp.nstr(3*mp.sqrt(3)/16, 12)}')
out['known_cubic_rho3cos3'] = mp.nstr(mp.sqrt(3)/4, 12)
out['known_quartic'] = mp.nstr(3*mp.sqrt(3)/16, 12)
out['known_minus_c'] = mp.nstr(-3*mp.sqrt(3)/4, 14)

# Lam at the regular angle is V0/3, so V0 = 3 Lam(pi/3)
out['Lam_at_regular'] = mp.nstr(Lam_num(mp.pi/3), 16)
out['V0_over_3'] = mp.nstr(mp.im(mp.polylog(2, Ws))/3, 16)
print(f'  Lam(pi/3) = {out["Lam_at_regular"]},  V0/3 = {out["V0_over_3"]}')

json.dump(out, open('.scratch/c2_constant.json', 'w'), indent=1)
print('\nwrote .scratch/c2_constant.json')
