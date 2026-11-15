# SCRIPT: c2_cubic2
"""C2. The cubic coefficient a in  D = V0 - c|G|^2 + a Re(G^3) + O(|G|^4), to 25 digits.

Along the real G axis (Im(G^3) contributes nothing), a(r) = (V0 - c r^2 - D)/r^3 -> a
with error O(r). Extrapolate by fitting a polynomial in r through the smallest radii and
evaluating at r = 0 (Lagrange), which is exact for the truncation series to the fitted
order.
"""
import mpmath as mp
mp.mp.dps = 70
w, wb = mp.expjpi(mp.mpf(1)/3), mp.expjpi(-mp.mpf(1)/3)
def D(z):  return mp.im(mp.polylog(2, z)) + mp.arg(1 - z)*mp.log(abs(z))
def zG(g): return (w - g*wb)/(1 - g)
V0 = D(w); c = 3*mp.sqrt(3)/4
a = lambda r: (V0 - c*r*r - D(zG(r)))/r**3

rs = [mp.mpf(2)**(-k) for k in range(6, 20)]
vals = [a(r) for r in rs]
print(f"{'r':>12s} {'a(r)':>32s} {'a(r) + sqrt3/4':>16s}")
for r, v in zip(rs, vals):
    print(f"{mp.nstr(r,8):>12s} {mp.nstr(v, 32):>32s} {mp.nstr(v + mp.sqrt(3)/4, 8):>16s}")

def lagrange_zero(xs, ys):
    """Value at 0 of the interpolating polynomial through (xs, ys)."""
    tot = mp.mpf(0)
    for i, xi in enumerate(xs):
        wgt = mp.mpf(1)
        for j, xj in enumerate(xs):
            if i != j: wgt *= (0 - xj)/(xi - xj)
        tot += ys[i]*wgt
    return tot

print()
print("Lagrange extrapolation to r = 0, using increasing numbers of the smallest radii:")
for k in [4, 5, 6, 7, 8]:
    ex = lagrange_zero(rs[:k], vals[:k])
    print(f"  {k} points: a = {mp.nstr(ex, 30):>32s}   a + sqrt(3)/4 = {mp.nstr(ex + mp.sqrt(3)/4, 6)}")
print()
print("-sqrt(3)/4 =", mp.nstr(-mp.sqrt(3)/4, 30))
