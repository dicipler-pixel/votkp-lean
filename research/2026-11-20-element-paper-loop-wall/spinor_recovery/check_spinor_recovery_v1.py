# SCRIPT: CHECK-SPINOR-PEEL-RECOVERY-01
# Numerical checks of the recovered spinor-peel / SARNS-coupling statements (hbar = 1, J = 1).
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(1)
# 1. peel identity: i^dag A^2 i - (i^dag A i)^2 = (Q A i)^dag (Q A i)
n, k = 6, 2
M = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); A = M + M.conj().T
iota = np.linalg.qr(rng.normal(size=(n, k)) + 1j*rng.normal(size=(n, k)))[0]
Q = np.eye(n) - iota @ iota.conj().T
lhs = iota.conj().T @ A @ A @ iota - (iota.conj().T @ A @ iota) @ (iota.conj().T @ A @ iota)
print('1 peel identity error', np.abs(lhs - (Q@A@iota).conj().T @ (Q@A@iota)).max())
# 2. three-mode loop
def H(phi): return np.array([[0, 1, np.exp(-1j*phi)], [1, 0, 1], [np.exp(1j*phi), 1, 0]])
for phi in (0.7, -0.7):
    h = H(phi); W = h[0,1]*h[1,2]*h[2,0]
    print('2 phi', phi, 'eigs', np.round(np.linalg.eigvalsh(h), 6), 'charpoly', np.round(np.poly(h).real, 6), '-2cos', round(-2*np.cos(phi), 6), 'W', np.round(W, 6))
# 3. directional difference at small tau vs 2 Im(W) tau^3
for phi in (0.7, -0.7):
    h = H(phi); W = h[0,1]*h[1,2]*h[2,0]
    for tau in (0.01, 0.05):
        U = expm(-1j*h*tau); d = abs(U[1,0])**2 - abs(U[0,1])**2
        print('3 phi', phi, 'tau', tau, 'P(1->2)-P(2->1)', d, ' 2ImW tau^3', 2*W.imag*tau**3)
# 4. perfect cycling at phi = +-pi/2, tau = 2 pi / (3 sqrt 3)
tau = 2*np.pi/(3*np.sqrt(3))
for phi in (np.pi/2, -np.pi/2):
    U = expm(-1j*H(phi)*tau); print('4 phi', round(phi, 4), '|U|^2 =\n', np.round(abs(U)**2, 6))
# 5. Schur elimination of mode 3 at energy E
E, phi = 0.37, 0.7; h = H(phi)
Heff = h[:2,:2] + h[:2,2:] @ np.linalg.inv(E*np.eye(1) - h[2:,2:]) @ h[2:,:2]
print('5 J_eff', np.round(Heff[0,1], 6), 'formula', np.round(1 + np.exp(-1j*phi)/E, 6), 'diag shift', np.round(Heff[0,0].real, 6), 'J^2/E', round(1/E, 6))
# eigen-consistency: eigenvalue of full H solves det(E - Heff(E)) = 0
lam = np.linalg.eigvalsh(h)[2]
He = h[:2,:2] + h[:2,2:] @ np.linalg.inv(lam*np.eye(1) - h[2:,2:]) @ h[2:,:2]
print('5 det(lam - Heff(lam)) at a true eigenvalue', abs(np.linalg.det(lam*np.eye(2) - He)))
# 6. memory equation: integrate full system, compare retained amplitudes with the memory form
from scipy.integrate import solve_ivp
A = h[:2,:2]; B = h[:2,2:]; C = h[2:,2:]
T = 3.0; ts = np.linspace(0, T, 3001)
full = np.array([expm(-1j*h*t) @ np.array([1,0,0]) for t in ts])
x = full[:, :2]; dt = ts[1]-ts[0]
err = 0
for i in range(1, len(ts)-1):
    xdot = (x[i+1]-x[i-1])/(2*dt)
    integ = sum(((B @ expm(-1j*C*(ts[i]-ts[j])) @ B.conj().T) @ x[j]) * (dt if 0<j<i else dt/2) for j in range(i+1)) if i % 300 == 0 else None
    if integ is not None:
        r = 1j*xdot - (A @ x[i] - 1j*integ); err = max(err, abs(r).max())
print('6 memory-equation residual (sampled)', err)
# 7. torus Dirac: D = 2pi[(m+a) s1 + (n+b) s2], eta pairing
s1 = np.array([[0,1],[1,0]]); s2 = np.array([[0,-1j],[1j,0]]); s3 = np.diag([1,-1])
D = 2*np.pi*((0+0.5)*s1 + (0+0)*s2)
print('7 D^2 =', np.round(D@D, 6).real.diagonal(), ' s3 D + D s3 =', np.abs(s3@D + D@s3).max(), ' smallest |lambda| at (1/2,0):', round(np.pi, 6))
