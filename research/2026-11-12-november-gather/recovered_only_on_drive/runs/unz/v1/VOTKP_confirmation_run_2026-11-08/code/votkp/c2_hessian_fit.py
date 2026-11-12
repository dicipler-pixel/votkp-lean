# SCRIPT: c2_hessian_fit
"""C2 (algebraic half). A 2D fit of D(V0 - D) near the vacuum in the G coordinate.

Why a 2D fit: D is real-analytic in (G, conj G) and invariant under G -> omega G with
omega = e^{2 pi i/3}. The quadratic monomials Re(G^2), Im(G^2) pick up omega^2 and are
therefore excluded, so the quadratic part is FORCED to be c|G|^2 -- the isotropy is a
symmetry statement, not a measurement. The cubic invariants are Re(G^3) and Im(G^3);
both must be fitted, which is what a single-direction extraction cannot do.

Pre-registered confirmation rule: CONFIRMED iff, with quartic terms included, the
fitted c equals 3 sqrt(3)/4 to 25 significant digits and the fit residual is smaller
than the smallest retained term by at least 10^6.
"""
import mpmath as mp
mp.mp.dps = 60

w, wb = mp.expjpi(mp.mpf(1)/3), mp.expjpi(-mp.mpf(1)/3)
def D(z):  return mp.im(mp.polylog(2, z)) + mp.arg(1 - z)*mp.log(abs(z))
def zG(g): return (w - g*wb)/(1 - g)
V0 = D(w)

def basis(u, v):
    g2 = u*u + v*v
    return [ g2,                       # |G|^2      (quadratic, invariant)
             u**3 - 3*u*v*v,           # Re G^3     (cubic, invariant)
             3*u*u*v - v**3,           # Im G^3     (cubic, invariant)
             g2*g2,                    # |G|^4
             g2*(u**3 - 3*u*v*v),      # |G|^2 Re G^3
             g2*(3*u*u*v - v**3) ]     # |G|^2 Im G^3

# sample: radii chosen so the largest retained term is |G|^4 ~ 1e-6
pts = []
for k in range(24):
    ang = 2*mp.pi*k/24
    for r in [mp.mpf('0.02'), mp.mpf('0.03'), mp.mpf('0.045'), mp.mpf('0.06'),
              mp.mpf('0.08'), mp.mpf('0.10')]:
        g = r*mp.expj(ang)
        u, v = mp.re(g), mp.im(g)
        y = V0 - D(zG(g))
        pts.append((basis(u, v), y, r))

n = len(basis(mp.mpf(0), mp.mpf(0)))
A = mp.matrix(len(pts), n); Y = mp.matrix(len(pts), 1)
for i, (b, y, r) in enumerate(pts):
    for j in range(n): A[i, j] = b[j]
    Y[i] = y
# normal equations
ATA = A.T*A; ATY = A.T*Y
sol = mp.lu_solve(ATA, ATY)
c, a, b, d, e, f = [sol[i] for i in range(n)]

print("fitted coefficients of  V0 - D  in the G coordinate")
print("  |G|^2        c =", mp.nstr(c, 32))
print("  Re G^3       a =", mp.nstr(a, 32))
print("  Im G^3       b =", mp.nstr(b, 32))
print("  |G|^4        d =", mp.nstr(d, 20))
print("  |G|^2 Re G^3 e =", mp.nstr(e, 20))
print("  |G|^2 Im G^3 f =", mp.nstr(f, 20))
print()
print("3 sqrt(3)/4   =", mp.nstr(3*mp.sqrt(3)/4, 32))
print("c - 3sqrt(3)/4 =", mp.nstr(c - 3*mp.sqrt(3)/4, 5))
print("relative      =", mp.nstr(abs(c - 3*mp.sqrt(3)/4)/(3*mp.sqrt(3)/4), 5))
print()
# candidate closed forms for the cubic coefficients
for name, val in [('a', a), ('b', b)]:
    for lbl, cand in [('-sqrt3/4', -mp.sqrt(3)/4), ('+sqrt3/4', mp.sqrt(3)/4),
                      ('-1/2', mp.mpf(-1)/2), ('+1/2', mp.mpf(1)/2),
                      ('-sqrt3/2', -mp.sqrt(3)/2), ('+sqrt3/2', mp.sqrt(3)/2)]:
        if abs(val - cand) < mp.mpf('1e-20'):
            print(f"  cubic {name} = {lbl} exactly (to 20 digits)")
print()
res = max(abs(sum(sol[j]*pts[i][0][j] for j in range(n)) - pts[i][1]) for i in range(len(pts)))
print("max residual of the fit:", mp.nstr(res, 5))
print("smallest retained term at r=0.02: |G|^2 * c =", mp.nstr(c*mp.mpf('0.02')**2, 5))
print("residual / that term   :", mp.nstr(res/(c*mp.mpf('0.02')**2), 5))
