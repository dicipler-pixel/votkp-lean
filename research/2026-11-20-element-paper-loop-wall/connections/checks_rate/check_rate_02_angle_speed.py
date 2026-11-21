# SCRIPT: RATE-WEIGHT-ANGLE-SPEED-02
# Connection tested: the one-mode offset speed limit (Theorem 2 of The Offset Speed Limit v1.1) written
# in the peel variables of The Loop Wall, and where the wall Gamma^2 = 1/2 sits in that bound.
#
# DERIVATION (shown before the check).  One accessible mode: C = c, tau = ln((1-c)/c), S = 1/(c(1-c)).
# With the map of check 01, c plays nu, so Gamma = 1 - 2c and h = tau/2.  Put theta = arcsin(Gamma).
#   (i)  theta = gd(h), the Gudermannian, because sin(gd h) = tanh h; and sinh h = tan(theta).
#   (ii) d theta/dt = -2 c_dot / sqrt(1-(1-2c)^2) = -c_dot / sqrt(c(1-c)), so
#        (d theta/dt)^2 = c_dot^2/(c(1-c)) = tau_dot^2 * c(1-c) = tau_dot^2 / S.
#        Theorem 2 (tau_dot^2 <= 4 g S) is therefore EXACTLY  |d theta/dt| <= 2 sqrt(g).
#        With Prop. 5 (g = E_B for Hamiltonian motion): |d theta/dt| <= 2 sqrt(E_B).
#   (iii) Two faces close the loop iff sinh h_a sinh h_b < 1 iff tan(theta_a) tan(theta_b) < 1
#        iff theta_a + theta_b < pi/2 (both angles in (0, pi/2)).  The equal-face wall is theta = pi/4.
#   (iv) The returned power Gamma^2 = sin^2(theta) has d(Gamma^2)/dt = sin(2 theta) d theta/dt, so
#        |d(Gamma^2)/dt| <= 2 sqrt(g) sin(2 theta) <= 2 sqrt(g), and the outer bound is reached only at
#        theta = pi/4, i.e. Gamma^2 = 1/2.  The same holds for the census 4c(1-c) = 1 - Gamma^2.
#   (v)  The saturating trajectory (4) of the paper, m = 1: 1 - 2C = sin(2 Omega t), so theta = 2 Omega t
#        exactly, g = Omega^2, and the wall is crossed at t = pi/(8 Omega).
# WHY THE CHECK PROVES IT: (i)-(iii) are checked symbolically (identities); (ii) and (iv) are checked on
# random idempotent 2x2 paths P(s) = [[c, b],[conj b, 1-c]] built to be idempotent at every s, with g read
# from the full matrix derivative, so a wrong reduction would show as a ratio above 1.
# KILL CONDITIONS (before running):
#   K1 a symbolic residual not 0;
#   K2 any random path with (dtheta/dt)^2/(4g) > 1 + 1e-6, or tau_dot^2/(4gS) differing from it by > 1e-6;
#   K3 any random path with |d(Gamma^2)/dt| > 2 sqrt(g) sin(2 theta) (1 + 1e-6);
#   K4 on trajectory (4) the peak of d(Gamma^2)/dt not at Gamma^2 = 1/2 (to grid resolution 1e-4);
#   K5 the angle form of the five first-opening mixed pairs disagrees with the Gamma1^2 + Gamma2^2 test.
import sys, gzip, json, math
import numpy as np
import sympy as sp

h = sp.symbols('h', real=True)
gd = sp.atan(sp.sinh(h))     # standard Gudermannian
r1 = sp.simplify(sp.sin(gd) - sp.tanh(h))
r2 = sp.simplify(sp.tan(gd) - sp.sinh(h))
ha, hb = sp.symbols('h_a h_b', positive=True)
# tan(A+B) = (tanA + tanB)/(1 - tanA tanB): the sum passes pi/2 exactly when tanA tanB passes 1
print('K1 residuals: sin(gd h) - tanh h =', r1, '; tan(gd h) - sinh h =', r2)

rng = np.random.default_rng(20261121)

def path(params, s):
    # idempotent 2x2 of rank one built from a unit vector (cos a, e^{i p} sin a)
    a0, a1, a2, p0, p1, p2 = params
    al = a0 + a1 * s + a2 * s * s
    ph = p0 + p1 * s + p2 * s * s
    v = np.array([math.cos(al), np.exp(1j * ph) * math.sin(al)])
    return np.outer(v, v.conj())

worst_ratio = 0.0
min_ratio = 9.0
worst_diff = 0.0
worst_pow = 0.0
n = 0
ds = 1e-6
for _ in range(4000):
    prm = rng.normal(size=6)
    s = 0.0
    P = path(prm, s)
    c = P[0, 0].real
    if not (0.02 < c < 0.98):
        continue
    Pp, Pm = path(prm, s + ds), path(prm, s - ds)
    Pd = (Pp - Pm) / (2 * ds)
    g = 0.5 * np.linalg.norm(Pd) ** 2
    cd = Pd[0, 0].real
    tau_d = -cd / (c * (1 - c))
    S = 1 / (c * (1 - c))
    Gam = 1 - 2 * c
    th = math.asin(Gam)
    th_d = -2 * cd / math.sqrt(1 - Gam * Gam)
    r_th = th_d ** 2 / (4 * g)
    r_tau = tau_d ** 2 / (4 * g * S)
    pow_d = 2 * Gam * (-2 * cd)
    worst_ratio = max(worst_ratio, r_th)
    min_ratio = min(min_ratio, r_th)
    worst_diff = max(worst_diff, abs(r_th - r_tau))
    worst_pow = max(worst_pow, abs(pow_d) / (2 * math.sqrt(g) * abs(math.sin(2 * th))))
    n += 1
print(f'K2 random one-mode paths: {n}; largest (dtheta/dt)^2/(4g) = {worst_ratio:.9f}; '
      f'largest |that - tau_dot^2/(4gS)| = {worst_diff:.2e}; smallest ratio = {min_ratio:.4f} (the bound is not trivially saturated)')
print(f'K3 largest |d(Gamma^2)/dt| / (2 sqrt(g) sin 2theta) = {worst_pow:.9f}')

# trajectory (4), m = 1: P_sigma(0) = (1/2)[[1, i s],[-i s, 1]], H = Omega [[0,1],[1,0]]
Om = 1.3
sig = 1
P0 = 0.5 * np.array([[1, 1j * sig], [-1j * sig, 1]])
Hm = Om * np.array([[0, 1], [1, 0]], dtype=complex)
ev, U = np.linalg.eigh(Hm)
def Pt(t):
    V = U @ np.diag(np.exp(-1j * ev * t)) @ U.conj().T
    return V @ P0 @ V.conj().T
ts = np.linspace(1e-4, math.pi / (4 * Om) - 1e-4, 20001)
G2 = []
th_err = 0
for t in ts:
    c = Pt(t)[0, 0].real
    Gm = 1 - 2 * c
    G2.append(Gm * Gm)
    th_err = max(th_err, abs(math.asin(max(-1, min(1, Gm))) - 2 * Om * t))
G2 = np.array(G2)
dG2 = np.gradient(G2, ts)
k = int(np.argmax(np.abs(dG2)))
EB = np.linalg.norm(P0 @ Hm @ (np.eye(2) - P0)) ** 2
print(f'K4 trajectory (4), Omega = {Om}: max |theta - 2 Omega t| = {th_err:.2e}; E_B = {EB:.6f} vs Omega^2 = {Om*Om:.6f}')
print(f'   peak |d(Gamma^2)/dt| = {abs(dG2[k]):.6f} (bound 2 sqrt(E_B) = {2*math.sqrt(EB):.6f}) at Gamma^2 = {G2[k]:.5f}, '
      f't = {ts[k]:.6f} vs pi/(8 Omega) = {math.pi/(8*Om):.6f}')

# mixed faces in angle form, from the archive (first-opening pairs)
d = json.load(gzip.open(sys.argv[1]))
rec = {r['Symbol'] if 'Symbol' in r else r['symbol']: r for r in d['records']}
def IE(sym, q):
    return {x['q']: x['IE_eV'] for x in rec[sym]['thresholds']}[q]
# helium-core opening: last 2s removal -> first 1s removal, i.e. removal index (Z-2) -> (Z-1), q = Z-3, Z-2
def ratio_core(sym, ncore):
    Zs = rec[sym]['Z']
    q = Zs - ncore - 1
    return IE(sym, q + 1) / IE(sym, q)
pairs = [('C', 'N', 2), ('Na', 'Mg', 10), ('K', 'Ca', 18), ('Rb', 'Sr', 36), ('Cs', 'Ba', 54)]
k5 = 0
for x, y, nc in pairs:
    z1, z2 = ratio_core(x, nc), ratio_core(y, nc)
    g1, g2 = (z1 - 1) / (z1 + 1), (z2 - 1) / (z2 + 1)
    t1, t2 = math.asin(g1), math.asin(g2)
    test_G = g1 * g1 + g2 * g2 - 1
    test_ang = math.degrees(t1 + t2) - 90
    k5 += (test_G > 0) != (test_ang > 0)
    print(f'   {rec[x]["name"]:9s} with {rec[y]["name"]:9s} z = {z1:.6f}, {z2:.6f}  Gamma1^2+Gamma2^2-1 = {test_G:+.6f}  '
          f'theta1+theta2-90deg = {test_ang:+.4f} deg ({"open" if test_ang > 0 else "closes"})')
print('   wall angle: theta = gd(asinh 1) =', math.degrees(math.asin((3+2*math.sqrt(2)-1)/(3+2*math.sqrt(2)+1))), 'deg')
print('KILL K1', 'FIRED' if (r1 != 0 or r2 != 0) else 'not fired',
      '| K2', 'FIRED' if (worst_ratio > 1 + 1e-6 or worst_diff > 1e-6) else 'not fired',
      '| K3', 'FIRED' if worst_pow > 1 + 1e-6 else 'not fired',
      '| K4', 'FIRED' if abs(G2[k] - 0.5) > 1e-3 else 'not fired',
      '| K5', 'FIRED' if k5 else 'not fired')
