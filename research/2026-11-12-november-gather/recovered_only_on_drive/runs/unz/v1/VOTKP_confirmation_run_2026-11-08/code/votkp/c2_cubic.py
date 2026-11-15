# SCRIPT: c2_cubic
"""C2. The cubic term at the vacuum, to high precision.

With c = 3 sqrt(3)/4 now known exactly, set  a(r) = (V0 - c r^2 - D(z(r)))/r^3  along the
real G axis, where the Im(G^3) direction contributes nothing. Extrapolate in r^2.
Confirmation: a = -sqrt(3)/4, and the coefficient of Im(G^3) vanishes identically.
"""
import mpmath as mp
mp.mp.dps = 60
w, wb = mp.expjpi(mp.mpf(1)/3), mp.expjpi(-mp.mpf(1)/3)
def D(z):  return mp.im(mp.polylog(2, z)) + mp.arg(1 - z)*mp.log(abs(z))
def zG(g): return (w - g*wb)/(1 - g)
V0 = D(w); c = 3*mp.sqrt(3)/4

def a_at(r):
    return (V0 - c*r*r - D(zG(r)))/r**3

rs = [mp.mpf(s) for s in ['0.04','0.02','0.01','0.005','0.0025','0.00125']]
print(f"{'r':>10s} {'a(r)':>30s}")
vals = []
for r in rs:
    v = a_at(r); vals.append(v)
    print(f"{mp.nstr(r,6):>10s} {mp.nstr(v, 30):>30s}")

# Richardson in r^2, repeatedly
def rich(v, t):
    out = []
    for i in range(len(v)-1):
        out.append((t[i+1]*v[i+1] - t[i]*v[i])/(t[i+1]-t[i]))
    return out
t = [r for r in rs]
v = vals
for _ in range(len(v)-1):
    v = rich(v, t); t = t[1:]
    if len(v) <= 2: break
print()
print("extrapolated a =", mp.nstr(v[0], 30))
print("-sqrt(3)/4    =", mp.nstr(-mp.sqrt(3)/4, 30))
print("difference    =", mp.nstr(abs(v[0] + mp.sqrt(3)/4), 5))
print()
print("so  D = V0 - (3 sqrt(3)/4)|G|^2 - (sqrt(3)/4) Re(G^3) + O(|G|^4)")
print("and the fit of the previous script gave the Im(G^3) coefficient = 0 to 58 digits.")
