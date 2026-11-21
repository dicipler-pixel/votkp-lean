# SCRIPT: CHECK-QUANTUM-CHEMISTRY-LINKS-01
# Checks of the side-agents' derived claims before they go in the paper.
# 1. Second-moment identity: for an idempotent P with site-diagonal position X,
#    Var(X) = Tr(P X (1-P) X) = 1/2 sum_ij |P_ij|^2 (x_i - x_j)^2.
# 2. Half-filled 1D chain: the nearest-neighbour share of the off-site budget is 8/pi^2.
# 3. Crossing of S and sigma from the leading Dirac term: Z* = (4 sigma^2 / alpha^2)^(1/4).
import numpy as np, math
rng = np.random.default_rng(7)
n, k = 40, 17
Q = np.linalg.qr(rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)))[0][:, :k]
P = Q @ Q.conj().T; x = rng.normal(size=n); X = np.diag(x)
lhs = np.trace(P @ X @ (np.eye(n) - P) @ X).real
rhs = 0.5*sum(abs(P[i, j])**2*(x[i]-x[j])**2 for i in range(n) for j in range(n))
print('1 second-moment identity', lhs, rhs, 'difference', abs(lhs - rhs))
N = 4000
H = -(np.eye(N, k=1) + np.eye(N, k=-1)); H[0, -1] = H[-1, 0] = -1
w, v = np.linalg.eigh(H); occ = v[:, :N//2]; Pc = occ @ occ.T
i = N//2; budget = Pc[i, i] - Pc[i, i]**2; nn = Pc[i, i+1]**2 + Pc[i, i-1]**2
print('2 half-filled chain nearest share', nn/budget, ' 8/pi^2', 8/math.pi**2)
alpha = 1/137.035999
print('3 Z* for sigma = 0.617:', (4*0.617**2/alpha**2)**0.25)
