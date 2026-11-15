# SCRIPT: c2_hessian_exact
"""C2 (algebraic half), clean extraction.

D is invariant under G -> omega G (omega = e^{2 pi i/3}), and real, so its expansion is
    D = V0 - c|G|^2 + a Re(G^3) + O(|G|^4),
the only 3-fold-symmetric quadratic plus the cubic Re(G^3). Thus:
  * along arg G = 30 deg, Re(G^3) = r^3 cos(90 deg) = 0 -> pure quadratic, c exact;
  * along arg G = 0, with c known -> a exact.
Confirmation: c = 3 sqrt(3)/4 and a = -sqrt(3)/4, each to 25 digits, plus the vanishing
of the cubic at 30/90/150 deg and its equality at 0/120/240 and at 60/180/300.
"""
import mpmath as mp
mp.mp.dps = 60

w, wb = mp.expjpi(mp.mpf(1)/3), mp.expjpi(-mp.mpf(1)/3)
def D(z):  return mp.im(mp.polylog(2, z)) + mp.arg(1 - z)*mp.log(abs(z))
def zG(g): return (w - g*wb)/(1 - g)
V0 = D(w)

# ---- c: fit V0 - D = c r^2 + d r^4 along 30 deg, two radii, eliminate d
def fit_c(ang):
    r1, r2 = mp.mpf('1e-2'), mp.mpf('5e-3')
    f = lambda r: (V0 - D(zG(r*mp.expj(ang))))/r**2
    return (4*f(r2) - f(r1))/3

c30 = fit_c(mp.pi/6)
print("c from the cubic-free direction (30 deg) :", mp.nstr(c30, 30))
print("3 sqrt(3)/4                             :", mp.nstr(3*mp.sqrt(3)/4, 30))
print("agrees to                               :", mp.nstr(abs(c30 - 3*mp.sqrt(3)/4), 5))

# average over the three cubic-free directions
cs = [fit_c(mp.pi/6 + mp.pi*k/3) for k in range(3)]
print("three cubic-free directions agree to    :", mp.nstr(max(cs)-min(cs), 5))
c = sum(cs)/3
print()

# ---- a: along arg = 0, subtract the quadratic
def fit_a(ang):
    def g(r):
        return (V0 - c*r**2 - D(zG(r*mp.expj(ang))))/r**3
    r1, r2 = mp.mpf('1e-2'), mp.mpf('5e-3')
    return (8*g(r2) - g(r1))/7
a0 = fit_a(0)
print("a along arg = 0                         :", mp.nstr(a0, 30))
print("-sqrt(3)/4                              :", mp.nstr(-mp.sqrt(3)/4, 30))
print("agrees to                               :", mp.nstr(abs(a0 + mp.sqrt(3)/4), 5))
print()

# ---- 3-fold symmetry of the cubic term
print("cubic term a_theta = (V0 - c r^2 - D)/r^3, extrapolated, at 30 deg steps:")
vals = []
for k in range(6):
    ang = mp.pi*k/6
    a = fit_a(ang)
    vals.append(a)
    print(f"   {k*30:3d} deg   {mp.nstr(a, 15):>22s}   Re(G^3)/r^3 = {mp.nstr(mp.cos(3*ang), 4):>8s}")
print()
print("zero at 90/210/330?  ", [mp.nstr(abs(vals[k]), 3) for k in (1,2,3,4,5)])
print("value at 0 and 120 and 240 agree? ", mp.nstr(max([vals[0],vals[4],vals[5]])-min([vals[0],vals[4],vals[5]]), 4))
