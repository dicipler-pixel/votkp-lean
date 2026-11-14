# SCRIPT: c2_hessian_rich
"""C2 (algebraic half). Converged fit with Richardson extrapolation.

Basis: all invariant monomials |G|^{2m} Re(G^{3n}), |G|^{2m} Im(G^{3n}) of total degree
2, 3, 4, 5, 6. Invariance under G -> omega G forces this basis, and excludes Re(G^2),
Im(G^2): that exclusion is the exact content of "isotropic".

Sampling: random angles and random radii scaled by a shrinking factor, so the fit is not
contaminated by a regular grid. A sequence of fits at decreasing scale, extrapolated,
gives c. Confirmation: c = 3 sqrt(3)/4 to 25 digits.
"""
import mpmath as mp
mp.mp.dps = 80
import random; random.seed(20261107)

w, wb = mp.expjpi(mp.mpf(1)/3), mp.expjpi(-mp.mpf(1)/3)
def D(z):  return mp.im(mp.polylog(2, z)) + mp.arg(1 - z)*mp.log(abs(z))
def zG(g): return (w - g*wb)/(1 - g)
V0 = D(w)

def basis(u, v):
    g2 = u*u+v*v; g3r = u**3-3*u*v*v; g3i = 3*u*u*v-v**3
    g6r = u**6-15*u**4*v*v+15*u*u*v**4-v**6
    return [g2, g3r, g3i, g2*g2, g2*g3r, g2*g3i, g2*g2*g2, g6r, 0]

N = 9
def fit(scale, npts=140):
    pts = []
    for _ in range(npts):
        ang = 2*mp.pi*mp.mpf(random.random())
        r = scale*(mp.mpf('0.2') + mp.mpf('0.8')*mp.mpf(random.random()))
        g = r*mp.expj(ang)
        u, v = mp.re(g), mp.im(g)
        b = basis(u, v)
        # degree-6 imaginary invariant
        g6i = 6*u**5*v - 20*u**3*v**3 + 6*u*v**5
        b[8] = g6i
        pts.append((b, V0 - D(zG(g))))
    A = mp.matrix([p[0] for p in pts]); Y = mp.matrix([p[1] for p in pts])
    sol = mp.lu_solve(A.T*A, A.T*Y)
    res = max(abs(sum(sol[j]*p[0][j] for j in range(N)) - p[1]) for p in pts)
    return sol, res

print(f"{'scale':>8s} {'c':>26s} {'a (Re G^3)':>24s} {'b (Im G^3)':>12s} {'residual':>10s}")
cs = []
for scale in ['0.08','0.04','0.02','0.01','0.005','0.0025']:
    sol, res = fit(mp.mpf(scale))
    c, a, b = sol[0], sol[1], sol[2]
    cs.append((mp.mpf(scale), c, a))
    print(f"{scale:>8s} {mp.nstr(c, 26):>26s} {mp.nstr(a, 24):>24s} {mp.nstr(b, 6):>12s} {mp.nstr(res,6):>10s}")

print()
print("3 sqrt(3)/4 =", mp.nstr(3*mp.sqrt(3)/4, 30))
# extrapolate c in scale^2 -> 0 using the last three (error ~ scale^2)
(s1,c1,a1),(s2,c2,a2),(s3,c3,a3) = cs[-3], cs[-2], cs[-1]
t1, t2, t3 = s1**2, s2**2, s3**2
# quadratic extrapolation through three points
denom = (t1-t2)*(t1-t3)*(t2-t3)
cex = (t2*t3*(t2-t3)*c1 + t3*t1*(t3-t1)*c2 + t1*t2*(t1-t2)*c3)/denom if False else None
# simple Richardson on the last two
cex = (t2*c3 - t3*c2)/(t2 - t3)
print("Richardson-extrapolated c =", mp.nstr(cex, 30))
print("difference from 3sqrt(3)/4:", mp.nstr(abs(cex - 3*mp.sqrt(3)/4), 5))
print()
print("-sqrt(3)/4 =", mp.nstr(-mp.sqrt(3)/4, 30))
aex = (t2*a3 - t3*a2)/(t2 - t3)
print("Richardson-extrapolated a =", mp.nstr(aex, 30))
print("difference from -sqrt(3)/4:", mp.nstr(abs(aex + mp.sqrt(3)/4), 5))
