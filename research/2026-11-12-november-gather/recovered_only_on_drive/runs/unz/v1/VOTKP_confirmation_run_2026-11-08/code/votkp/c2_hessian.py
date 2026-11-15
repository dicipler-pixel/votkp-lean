# SCRIPT: c2_hessian
"""C2 (algebraic half). The Hessian of D at the vacuum, in the G coordinate.

Pre-registered confirmation rule (written before the run):
  CONFIRMED iff, to 25 significant digits,
    (i)   V0 = D(w) equals 1.0149416064096536... (the regular ideal tetrahedron volume);
    (ii)  D(z(G)) = V0 - c |G|^2 + O(|G|^3) with c isotropic (same in every direction)
          and c = 3 sqrt(3)/4 = 1.29903810567...;
    (iii) the cubic term is 3-fold symmetric: it vanishes along three directions and
          takes one value on the others, and is identified explicitly.
  Failure of (ii) in particular refutes the "3 sqrt(3)/4" coefficient.
"""
import mpmath as mp
mp.mp.dps = 40

w  = mp.expjpi(mp.mpf(1)/3)
wb = mp.expjpi(-mp.mpf(1)/3)

def D(z):
    """Bloch-Wigner dilogarithm (tetrahedron volume)."""
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z)*mp.log(abs(z))

def z_from_G(g):
    """Inverse of G(z) = (z-w)/(z-wb):  z = (w - g*wb)/(1-g)."""
    return (w - g*wb)/(1 - g)

V0 = D(w)
print("V0 = D(w)               =", mp.nstr(V0, 25))
print("regular tetra volume    = 1.0149416064096536250212025...")
print("match to 25 digits:", abs(V0 - mp.mpf('1.0149416064096536250212025')) < mp.mpf('1e-24'))
print()

# ---------------------------------------------------------------- isotropic quadratic coefficient
c_est = []
for ang in [0, mp.pi/6, mp.pi/3, mp.pi/2, 2*mp.pi/3, 5*mp.pi/6, mp.pi, 4*mp.pi/3]:
    r = mp.mpf('1e-3')
    g = r*mp.expj(ang)
    val = D(z_from_G(g))
    # D = V0 - c r^2 + O(r^3); extract c by (V0 - val)/r^2, then Richardson on r
    est = []
    for rr in [mp.mpf('1e-2'), mp.mpf('5e-3'), mp.mpf('2e-3'), mp.mpf('1e-3')]:
        gg = rr*mp.expj(ang)
        est.append((V0 - D(z_from_G(gg)))/rr**2)
    c_est.append((ang, est))
print("(V0 - D)/|G|^2 for shrinking |G|, by direction:")
for ang, est in c_est:
    print(f"  arg G = {float(ang):7.4f} rad   {[mp.nstr(e, 12) for e in est]}")

# Richardson-extrapolate in r^2
def coeff(ang):
    r1, r2 = mp.mpf('2e-3'), mp.mpf('1e-3')
    f = lambda r: (V0 - D(z_from_G(r*mp.expj(ang))))/r**2
    return (4*f(r2) - f(r1))/3      # cancels the O(r^2) term in the quotient

cs = [coeff(a) for a in [0, mp.pi/6, mp.pi/3, mp.pi/2, 2*mp.pi/3, 5*mp.pi/6, mp.pi]]
print()
print("Richardson-extrapolated coefficient by direction:")
for a, c in zip([0, mp.pi/6, mp.pi/3, mp.pi/2, 2*mp.pi/3, 5*mp.pi/6, mp.pi], cs):
    print(f"  arg = {float(a):7.4f}  c = {mp.nstr(c, 18)}")
spread = max(cs) - min(cs)
print("spread across directions:", mp.nstr(spread, 6), " -> isotropic:", spread < mp.mpf('1e-15'))
target = 3*mp.sqrt(3)/4
print("3 sqrt(3)/4             =", mp.nstr(target, 18))
print("measured                =", mp.nstr(sum(cs)/len(cs), 18))
print("relative difference     =", mp.nstr(abs(sum(cs)/len(cs) - target)/target, 6))
print()

# ---------------------------------------------------------------- cubic term
print("cubic term: (V0 - c|G|^2 - D)/|G|^3 as |G| -> 0, by direction")
def cubic(ang):
    r = mp.mpf('2e-3')
    g = r*mp.expj(ang)
    res = (V0 - target*r**2 - D(z_from_G(g)))/r**3
    r2 = mp.mpf('1e-3')
    g2 = r2*mp.expj(ang)
    res2 = (V0 - target*r2**2 - D(z_from_G(g2)))/r2**3
    return (8*res2 - res)/7
for k in range(12):
    a = mp.pi*k/6
    print(f"  arg = {mp.nstr(a,6):>9s}  ({k*30:3d} deg)   cubic = {mp.nstr(cubic(a), 12)}")
