#!/usr/bin/env python3
# SCRIPT: WEIGHT-TEST-1
"""Test 1: is the electron's weight a non-modal surge?
Kill conditions, written before the run:
  K1  if the free Dirac generator is non-normal (||[H,H^dag]|| > 0), a non-modal surge is built in; if it is normal,
      no transient growth is possible in the free electron and the strict 'surge' reading of the free electron dies.
  K2  the cross-term reading lives only if the connection energy of H across the chiral split, E_c = ||[H,P_L]||_F^2,
      equals a fixed multiple of m^2 at EVERY momentum (no p dependence) and vanishes exactly when m = 0.
  K3  a zig (pure left-handed) start must move into zag at amplitude m^2/E^2: P_R(t) = (m^2/E^2) sin^2(E t).
  K4  the opposite (his rule): open the electron to light that leaks away. If any passive leak (anti-Hermitian part <= 0)
      gives norm growth, a surge exists without a pump. Then try it WITH gain (pumped light).
Why these prove what they claim: K1 is the textbook criterion (transient growth needs non-normality); K2 measures
the off-diagonal (cross) block directly; K3 is the observable zig-zag; K4 checks d||psi||^2/dt = 2<psi|Im-part|psi>."""
import numpy as np
from scipy.linalg import expm
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
I2 = np.eye(2); Z = np.zeros((2, 2))
def dirac_chiral(p, m):
    sp = sum(p[i] * s[i] for i in range(3))
    return np.block([[-sp, m * I2], [m * I2, sp]])        # Weyl basis: (left, right)
PL = np.block([[I2, Z], [Z, Z]])
rng = np.random.default_rng(1)
print('K1  non-normality ||[H,H^dag]|| of the free Dirac generator, 200 random (p, m):',
      max(np.linalg.norm(H @ H.conj().T - H.conj().T @ H) for H in [dirac_chiral(rng.normal(size=3) * 3, abs(rng.normal())) for _ in range(200)]))
print('K2  connection energy across the chiral split, E_c = ||[H,P_L]||_F^2, divided by m^2:')
for m in [0.0, 0.5, 1.0, 2.0]:
    vals = [np.linalg.norm(dirac_chiral(rng.normal(size=3) * 5, m) @ PL - PL @ dirac_chiral(np.zeros(3), m)) for _ in range(1)]
    Ec = [np.linalg.norm(H @ PL - PL @ H) ** 2 for H in [dirac_chiral(rng.normal(size=3) * 5, m) for _ in range(100)]]
    print(f'     m = {m}: E_c over 100 random momenta: min {min(Ec):.12f}  max {max(Ec):.12f}   E_c/m^2 = ' + (f'{max(Ec) / m**2:.12f}' if m else 'n/a (E_c = 0)'))
print('K3  zig start (left-handed, helicity matched), probability in zag vs (m^2/E^2) sin^2(E t):')
for m, pz in [(1.0, 0.5), (0.3, 2.0), (2.0, 1.0)]:
    p = np.array([0, 0, pz]); H = dirac_chiral(p, m); E = np.hypot(pz, m)
    psi0 = np.array([0, 1, 0, 0], complex)                 # left-handed spinor component along -sigma_z p
    err = 0
    for t in np.linspace(0, 10, 101):
        ps = expm(-1j * H * t) @ psi0; PR = np.vdot(ps[2:], ps[2:]).real
        err = max(err, abs(PR - (m / E) ** 2 * np.sin(E * t) ** 2))
    print(f'     m = {m}, p = {pz}: max |P_R - (m^2/E^2) sin^2 Et| = {err:.2e}   peak zag share m^2/E^2 = {(m / E) ** 2:.4f}')
print('K4  opposite: electron (level 0) coupled at g to a light mode (level w) that leaks at rate k (passive) or is pumped (gain)')
def growth(g, w, k, T=40, n=4000):
    H = np.array([[0, g], [g, w - 0.5j * k]]); best = 0
    for t in np.linspace(0, T, n):
        best = max(best, np.linalg.norm(expm(-1j * H * t), 2))
    return best, np.linalg.norm(H @ H.conj().T - H.conj().T @ H)
for g, w, k in [(0.5, 0.2, 1.0), (1.0, 0.0, 3.0), (0.2, 1.0, 0.5)]:
    G, nn = growth(g, w, k); print(f'     passive leak k = {k}: non-normality {nn:.3f}, largest ||e^(-iHt)|| over t = {G:.6f}  (> 1 would be a surge)')
for g, w, k in [(0.5, 0.2, -0.3), (1.0, 0.0, -0.5)]:
    G, nn = growth(g, w, k, T=10); print(f'     pumped (gain {-k}): non-normality {nn:.3f}, largest ||e^(-iHt)|| over t <= 10 = {G:.4f}')
# a non-normal surge: transient growth above 1 while every mode DECAYS (all Im eigenvalues < 0)
H = np.array([[-0.05j, 3.0], [0, -0.1j]]); ev = np.linalg.eigvals(H)
G = max(np.linalg.norm(expm(-1j * H * t), 2) for t in np.linspace(0, 60, 3000))
print(f'     non-normal but every mode decaying (Im eig {ev.imag.round(3)}): largest ||e^(-iHt)|| = {G:.3f}; its anti-Hermitian part has eigenvalues',
      np.linalg.eigvalsh((H - H.conj().T) / 2j).round(3), '(a positive one = gain hidden in the cross term)')
