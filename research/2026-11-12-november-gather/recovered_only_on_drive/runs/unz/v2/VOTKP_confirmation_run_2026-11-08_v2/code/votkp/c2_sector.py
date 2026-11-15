# SCRIPT: c2_sector
"""C2d: the sector lemma -- why the bowl law has the form it has, proved rather than fitted.

The claim. Write D for the Bloch-Wigner dilogarithm, w = e^{i pi/3}, G(z) = (z-w)/(z-wbar) and
t(z) = 1/(1-z). Then

  (i)   t^3 = id and G(t(z)) = omega G(z), omega = e^{2 pi i/3};
  (ii)  D(t(z)) = D(z) identically on the upper half plane;
  (iii) hence every Taylor coefficient c_ab of D in powers of G and Gbar vanishes unless
        a = b (mod 3), and the monomials that survive are exactly (|G|^2)^m (G^3)^p (Gbar^3)^q.

(ii) is proved without any dilogarithm identity, as follows. Treat D as a function of z and Z = zbar.
Differentiating the defining expression gives, exactly,

        dD/dZ = v/(2 i Z) + u/(2 i (1-Z)),      u = log|z|,  v = log|1-z|,
        dD/dz = -[ v/(2 i z) + u/(2 i (1-z)) ],

so dD/dz = conjugate(dD/dZ), as it must be for a real function. Now compose with t, whose
coefficients are real, so that conj(t(z)) = t(Z) and conj(t'(z)) = 1/(1-Z)^2. The substitutions
u -> u - v, v -> -v, Z -> 1/(1-Z) give

        (dD/dZ)(t(z), t(Z)) * conj(t'(z)) = u/(2 i (1-Z)) + v/(2 i Z) = dD/dZ (z, Z),

an identity of the same expression, which this script checks symbolically. Hence dbar(D o t - D) = 0,
and d(D o t - D) = 0 by conjugation; a function with both derivatives zero is locally constant on the
connected set H, and the constant is 0 because D and D o t both tend to 0 as z -> i infinity. So
D o t = D. No five-term relation, no branch choice: u and v are real logarithms.

(iii) is then algebra: rho f (G, Gbar) = f(omega G, omega bar G) acts on G^a Gbar^b by omega^(a-b),
and omega^(a-b) = 1 exactly when a = b (mod 3).

The gap. rho has order 3 and is unitary, so its spectrum lies in {1, omega, omega^2}; the Riesz
projector onto the +1 sector is P = (1 + rho + rho^2)/3 and the gap separating that sector from the
other two is |1 - omega| = sqrt 3. The +1 sector still contains Im(G^3); the reflection in
c2_closed_form.py removes it.
"""
import sys, json
sys.path.insert(0, 'code')
import sympy as sp

z, Z, u, v = sp.symbols('z Z u v', positive=False)
I = sp.I
w = sp.Rational(1, 2) + sp.sqrt(3)*I/2
wb = sp.Rational(1, 2) - sp.sqrt(3)*I/2
omega = sp.Rational(-1, 2) + sp.sqrt(3)*I/2


def G(zz):
    return (zz - w)/(zz - wb)


def t(zz):
    return 1/(1 - zz)


out = {}

# ---- (i) the 3-cycle and the G coordinate ------------------------------------------------
assert sp.simplify(t(t(t(z))) - z) == 0, 't^3 != id'
assert sp.simplify(t(t(z)) - (1 - 1/z)) == 0
r1 = sp.simplify(sp.expand(sp.simplify(G(t(z))/G(z))))
r2 = sp.simplify(sp.expand(sp.simplify(G(t(t(z)))/G(z))))
cub = lambda x: sp.simplify(x**3 - 1) == 0 and sp.simplify(x - 1) != 0
out['t3_is_id'] = True
out['G_circ_t_over_G'] = str(sp.nsimplify(r1))
out['primitive_cube_root_1'] = bool(cub(r1))
out['primitive_cube_root_2'] = bool(cub(r2))
print('(i)  t^3 = id;  G(t z)/G(z) =', r1, ' primitive cube root:', cub(r1))
print('     G(t(t z))/G(z) =', r2, ' primitive cube root:', cub(r2))

# ---- (ii) dD/dZ and dD/dz, then the invariance identity ----------------------------------
# The derivative formulas above, written as functions of (z, Z, u, v).
def dD_dZ(zz, ZZ, uu, vv):
    return vv/(2*I*ZZ) + uu/(2*I*(1 - ZZ))


def dD_dz(zz, ZZ, uu, vv):
    return -(vv/(2*I*zz) + uu/(2*I*(1 - zz)))


# composition with t:  the image point has  log|zeta| = -v  and  log|1-zeta| = u - v,
# and conj(t'(z)) = 1/(1-Z)^2
Zt = t(Z)
compose = sp.simplify(dD_dZ(t(z), Zt, -v, u - v) * (1/(1 - Z)**2))
target = sp.simplify(dD_dZ(z, Z, u, v))
resid = sp.simplify(sp.expand(compose - target))
out['invariance_residual'] = str(resid)
out['invariance_holds'] = bool(resid == 0)
print('(ii) [dD/dZ o t] * conj(t\') - dD/dZ  simplifies to', resid)

# the same identity for d/dz, which follows by conjugation but is checked directly
compose2 = sp.simplify(dD_dz(t(z), Zt, -v, u - v) * (1/(1 - z)**2))
resid2 = sp.simplify(sp.expand(compose2 - sp.simplify(dD_dz(z, Z, u, v))))
out['invariance_residual_z'] = str(resid2)
out['invariance_holds_z'] = bool(resid2 == 0)
print('     the same for d/dz:', resid2)

# the derivative formula itself: differentiate the defining expression, using Li2' = -log(1-w)/w,
# then rewrite log(1-Z) = 2v - log(1-z) and log Z = 2u - log z and check that the log(1-z) and
# log z terms cancel -- i.e. that the result depends only on u and v
Li2 = sp.Function('Li2')
Lz, LZ = sp.log(z), sp.log(Z)
D_expr = (Li2(z) - Li2(Z))/(2*I) + (sp.log(1 - z) - sp.log(1 - Z))*(Lz + LZ)/(4*I)
dZ_direct = sp.diff(D_expr, Z).subs(sp.Derivative(Li2(Z), Z), -sp.log(1 - Z)/Z)
dZ_direct = sp.expand(sp.simplify(dZ_direct))
subbed = sp.expand(dZ_direct.subs({sp.log(1 - Z): 2*v - sp.log(1 - z), LZ: 2*u - Lz}))
res = sp.simplify(sp.expand(subbed - dD_dZ(z, Z, u, v)))
out['derivative_formula_residual'] = str(res)
out['derivative_formula_holds'] = bool(res == 0)
print('     d/dZ of the defining expression, with Li2\' and the real-log rewrites, minus the'
      ' stated formula:', res)

# ---- (iii) the sector statement -----------------------------------------------------------
# rho acts on G^a Gbar^b by omega^(a-b); it is the identity exactly when a = b (mod 3).
bad = []
for a in range(0, 41):
    for b in range(0, 41 - a):
        lam = sp.simplify(omega**(a - b))
        invariant = (a - b) % 3 == 0
        if (sp.simplify(lam - 1) == 0) != invariant:
            bad.append((a, b))
out['sector_misclassified'] = bad
out['sector_rule_ok'] = not bad
print('(iii) monomials misclassified by the a = b (mod 3) rule:', bad)

# the coefficient file: every survivor lies in the +1 sector, none elsewhere
T = json.load(open('.scratch/c2_taylor_S.json'))
coeffs = {tuple(int(x) for x in k.split(',')) for k in T['coeffs']}
out['coefficients_computed'] = len(coeffs)
out['in_plus_sector'] = sum(1 for a, b in coeffs if (a - b) % 3 == 0)
out['off_sector'] = sum(1 for a, b in coeffs if (a - b) % 3 != 0)
out['max_degree'] = max(a + b for a, b in coeffs)
print(f'      coefficients computed to degree {out["max_degree"]}: '
      f'{out["in_plus_sector"]} in the +1 sector, {out["off_sector"]} elsewhere')

# ---- the gap ------------------------------------------------------------------------------
P_on_1 = sp.nsimplify(sp.simplify((1 + 1 + 1)/3))            # P acts as 1 on the invariant sector
P_on_omega = sp.nsimplify(sp.simplify((1 + omega + omega**2)/3))  # and as 0 on the other two
out['P_on_invariant'] = str(P_on_1)
out['P_on_other'] = str(P_on_omega)
print('     P = (1 + rho + rho^2)/3 acts as', P_on_1, 'on the +1 sector and as', P_on_omega,
      'on the other two')
gap = sp.simplify(sp.Abs(1 - omega))
out['gap'] = str(gap)
out['gap_squared'] = str(sp.simplify(gap**2))
print('     gap |1 - omega| =', sp.simplify(gap), '=', sp.nsimplify(sp.sqrt(3)))
# the coefficients are (sqrt 3)^3 times rationals -- an observation, not a derivation
g3 = sp.sqrt(3)**3
for name, val in [('quadratic', 3*sp.sqrt(3)/4), ('cubic', sp.sqrt(3)/8), ('quartic', 3*sp.sqrt(3)/16)]:
    print(f'     {name:9s} {sp.nsimplify(val)} = (sqrt3)^3 * {sp.nsimplify(sp.radsimp(val/g3))}')

json.dump(out, open('.scratch/c2_sector.json', 'w'), indent=1)
print('wrote .scratch/c2_sector.json')
