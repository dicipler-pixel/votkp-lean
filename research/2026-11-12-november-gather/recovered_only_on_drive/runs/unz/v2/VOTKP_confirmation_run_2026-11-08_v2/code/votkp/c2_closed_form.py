# SCRIPT: c2_closed_form
"""C2d: every Taylor coefficient of D in (G, Gbar), in closed form, on the 3-cycle's displacements.

With omega = exp(2 pi i/3):  log z = i pi/3 + sum (1-conj(omega)^n)/n G^n,
log(1-z) = -i pi/3 + sum (1-omega^n)/n G^n, and for a, b >= 1

    c[a,b] = Im[(1-omega^a)(1-omega^b)] / (2ab),
    c[n,0] = (1/(4 i n)) sum_{j=1}^{n-1} (2j-n)(1-omega^j)(1-conj(omega)^(n-j)) / (j(n-j)),
    c[0,n] = conj c[n,0].

Checks: exact (sympy) through degree 4 against the bowl law; ball arithmetic against the Arb
coefficients of c2_arb_enclosure.py for all 861 pairs through degree 40; the reflection
z -> 1 - conj(z) that makes every coefficient real; the Gram spectrum of the 3-cycle.

    python3 code/votkp/c2_closed_form.py    (needs python-flint and sympy)
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from flint import acb, arb, ctx
import c2_arb_enclosure as A

out = {}
# ---- exact, degree <= 4 -----------------------------------------------------------------------
om = sp.Rational(-1, 2) + sp.sqrt(3)*sp.I/2
omb = sp.conjugate(om)
def mixed(a, b):
    return sp.im(sp.expand((1 - om**a)*(1 - om**b)))/(2*a*b)
def pure(n):
    if n == 1:
        return sp.Integer(0)
    s = sum((2*j - n)*(1 - om**j)*(1 - omb**(n - j))/(j*(n - j)) for j in range(1, n))
    return sp.simplify(sp.expand(s)/(4*sp.I*n))
P = {(1, 1): -3*sp.sqrt(3)/4, (2, 2): 3*sp.sqrt(3)/16, (3, 0): sp.sqrt(3)/8, (0, 3): sp.sqrt(3)/8}
res = []
for k in range(1, 5):
    for a in range(k + 1):
        b = k - a
        v = mixed(a, b) if a and b else (pure(a) if a else sp.conjugate(pure(b)))
        res.append(sp.simplify(v - P.get((a, b), 0)))
out['exact_through_degree_4'] = all(r == 0 for r in res)
print('exact through degree 4:', out['exact_through_degree_4'])

# ---- ball arithmetic, degree <= 40 ------------------------------------------------------------
ctx.prec = 120
w3 = acb(arb(-1)/2, A.s3/2)
I = acb(0, 1)
mx = 0.0
nonzero = 0
offsector = 0
imag = 0.0
for (a, b), v in A.c.items():
    if a == 0 and b == 0:
        continue
    if a and b:
        f = acb(((1 - w3**a)*(1 - w3**b)).imag/(2*a*b))
    else:
        n = a or b
        s = acb(0)
        for j in range(1, n):
            s += (2*j - n)*(1 - w3**j)/j*(1 - w3.conjugate()**(n - j))/(n - j)
        f = s/(4*I*n)
        if b:
            f = f.conjugate()
    mx = max(mx, float((v - f).abs_upper()))
    if float(v.abs_upper()) > 1e-20:
        nonzero += 1
        offsector += (a - b) % 3 != 0
        imag = max(imag, abs(float(v.imag.mid())))
out['pairs_checked'] = len(A.c) - 1
out['max_difference'] = mx
out['nonzero'] = nonzero
out['nonzero_off_sector'] = offsector
out['max_imaginary_part'] = imag
print(out)

# ---- the reflection: D(1 - conj z) = D(z), G(1 - conj z) = conj G(z) ---------------------------
z, Z, u, v = sp.symbols('z Z u v')
dDdZ = lambda zz, ZZ, uu, vv: vv/(2*sp.I*ZZ) + uu/(2*sp.I*(1 - ZZ))
dDdz = lambda zz, ZZ, uu, vv: -(vv/(2*sp.I*zz) + uu/(2*sp.I*(1 - zz)))
# zeta = 1 - Z, conj zeta = 1 - z, log|zeta| = v, log|1-zeta| = u; d zeta/dZ = -1
out['reflection_invariance'] = sp.simplify(-dDdz(1 - Z, 1 - z, v, u) - dDdZ(z, Z, u, v)) == 0
w = sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2
wb = sp.conjugate(w)
Gz = (z - w)/(z - wb)
GbarZ = (Z - wb)/(Z - w)
out['G_reflects_to_conj'] = sp.simplify(((1 - Z) - w)/((1 - Z) - wb) - GbarZ) == 0
print('reflection:', out['reflection_invariance'], out['G_reflects_to_conj'])

# ---- the 3-cycle's displacement Gram ----------------------------------------------------------
C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Gram = (sp.eye(3) - C).T*(sp.eye(3) - C)
out['gram_spectrum'] = sorted(str(k) for k, m in Gram.eigenvals().items() for _ in range(m))
out['c_equals_gap_cubed_over_4'] = sp.simplify(sp.Abs(1 - om)**3/4 - 3*sp.sqrt(3)/4) == 0
print('Gram spectrum of the 3-cycle:', out['gram_spectrum'], ' c = |1-omega|^3/4:', out['c_equals_gap_cubed_over_4'])
json.dump(out, open('.scratch/c2_closed_form.json', 'w'), indent=1, default=bool)
print('wrote .scratch/c2_closed_form.json')
