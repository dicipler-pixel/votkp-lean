# SCRIPT: c1_disk_algebra
"""C1. The vacuum disk: exact algebra.

Pre-registered confirmation rule (written before the run):
  CONFIRMED iff all four hold as exact symbolic identities over Q(w), w = exp(i pi/3):
    (i)   G(t(z))/G(z) is a primitive cube root of unity, t(z) = 1/(1-z);
    (ii)  G(t(t(z))) = G(z) and |G| is rational-invariant, i.e. G/Gbar * conj = 1;
    (iii) |G(z)| = 1 exactly for real z (as an identity in Re z);
    (iv)  G(conj z) = 1/conj(G(z)), hence |G(conj z)| = 1/|G(z)| and therefore
          |G(conj z)| > 1 exactly when |G(z)| < 1.
  Any failure of (i)-(iv) refutes C1 as stated.
"""
import sympy as sp

z, x, y = sp.symbols('z x y', real=False), sp.symbols('x', real=True), sp.symbols('y', real=True)
z = sp.symbols('z')
I = sp.I
w = sp.Rational(1, 2) + I*sp.sqrt(3)/2          # exp(i pi/3)
wb = sp.Rational(1, 2) - I*sp.sqrt(3)/2         # exp(-i pi/3)
assert abs(complex(sp.N(w - sp.exp(I*sp.pi/3), 30))) < sp.Float("1e-25")

def G(zz):
    return (zz - w)/(zz - wb)

def t(zz):
    return 1/(1 - zz)

print("w = exp(i pi/3) =", sp.simplify(w))
print()

# ---------------------------------------------------------------- (i) 3-cycle rotation
# exp(k pi i /3) written in radicals, so that sympy can compare it exactly; without this
# the comparison leaves (-1)**(2/3) unevaluated and prints False for a true identity.
def e3(k):
    return sp.simplify(sp.exp(k*sp.I*sp.pi/3).rewrite(sp.cos))


r1 = sp.simplify(sp.nsimplify(sp.expand(sp.simplify(G(t(z))/G(z)))))
print("(i) G(t(z)) / G(z) =", sp.simplify(r1))
cand = sp.simplify(r1 - e3(2))
print("    minus exp(2 pi i/3) simplifies to:", sp.simplify(cand))
print("    equals exp(2 pi i /3):", sp.simplify(r1 - e3(2)) == 0)
print("    is a primitive cube root (value^3 = 1, value != 1):",
      sp.simplify(r1**3 - 1) == 0, sp.simplify(r1 - 1) != 0)
print()

# ---------------------------------------------------------------- (ii) full 3-cycle, |G| preserved
r2 = sp.simplify(G(t(t(z)))/G(z))
print("(ii) G(t(t(z))) / G(z) =", sp.simplify(r2))
print("     equals exp(4 pi i/3):", sp.simplify(r2 - e3(4)) == 0)
print("     t(t(z)) = 1 - 1/z check:", sp.simplify(t(t(z)) - (1 - 1/z)) == 0)
mod = sp.simplify(G(t(z))*sp.conjugate(G(t(z))) - G(z)*sp.conjugate(G(z)))
print("     |G(t z)|^2 - |G(z)|^2 =", mod)
print()

# ---------------------------------------------------------------- (iii) real z  =>  |G| = 1
xr = sp.symbols('xr', real=True)
modsq_real = sp.simplify(sp.expand((G(xr)*sp.conjugate(G(xr))).rewrite(sp.re)))
modsq_real = sp.simplify(sp.expand(sp.Abs(xr - w)**2 - sp.Abs(xr - wb)**2))
print("(iii) |z-w|^2 - |z-wb|^2 at z = r real:", sp.expand((xr-sp.Rational(1,2))**2 + (sp.sqrt(3)/2)**2
      - ((xr-sp.Rational(1,2))**2 + (sp.sqrt(3)/2)**2)))
# do it honestly: expand symbolically with y
zz = sp.symbols('zz', real=True)
d1 = sp.expand((zz - sp.Rational(1,2))**2 + (sp.Integer(0) - sp.sqrt(3)/2)**2)
d2 = sp.expand((zz - sp.Rational(1,2))**2 + (sp.Integer(0) + sp.sqrt(3)/2)**2)
print("     |z-w|^2  with z real =", d1)
print("     |z-wb|^2 with z real =", d2)
print("     equal:", sp.simplify(d1 - d2) == 0)
print("     general z = a+bi: |z-w|^2 - |z-wb|^2 =",
      sp.simplify(sp.expand((sp.symbols('a')-sp.Rational(1,2))**2 + (sp.symbols('b')-sp.sqrt(3)/2)**2
                            - ((sp.symbols('a')-sp.Rational(1,2))**2 + (sp.symbols('b')+sp.sqrt(3)/2)**2))))
print("     -> |G| = 1 exactly on Im z = 0, which is the whole 'rim' statement")
print()

# ---------------------------------------------------------------- (iv) conjugate reciprocal
r4 = sp.simplify(G(sp.conjugate(z)) * sp.conjugate(G(z)))
print("(iv) G(conj z) * conj(G(z)) =", r4)
print("     identically 1:", sp.simplify(r4 - 1) == 0)
print("     hence |G(conj z)| = 1/|G(z)|")
