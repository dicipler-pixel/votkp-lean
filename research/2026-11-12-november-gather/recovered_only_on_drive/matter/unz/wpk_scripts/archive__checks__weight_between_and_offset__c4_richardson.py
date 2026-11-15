archive/checks/weight_between_and_offset/c4_richardson.py

\# SCRIPT: C4-RICHARDSON-01 \# C4 of WEIGHT-BETWEEN-CORE-01 fired at 3.1e-6 against a 1e-6 limit. If the cause is the central-difference step \# (truncation \~ h^2), a Richardson-extrapolated derivative must shrink the deviation by orders of magnitude; if the \# equality claim were false the deviation would stay. KILL: worst |ratio - 1| stays above 1e-7 with Richardson. import numpy as np from scipy.linalg import expm rng = np.random.default_rng(2610) fro2 = lambda X: float(np.real(np.vdot(X, X))) def rand_proj(n, k):

Q, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j \* rng.normal(size=(n, n))); V = Q\[:, :k\]; return V @ V.conj().T def offset(C): nu = np.linalg.eigvalsh(C); return float(np.sum(np.log((1 - nu) / nu))) worst_cd = worst_r = 0.0 for trial in range(50):

n = rng.integers(4, 9); m = rng.integers(1, n // 2 + 1); k = rng.integers(m, n - m + 1) while True:

P = rand_proj(n, k); E = np.eye(n)\[:, :m\]; C = E.T @ P @ E; nu = np.linalg.eigvalsh(C) if nu.min() \> 1e-3 and nu.max() \< 1 - 1e-3: break W = -np.linalg.inv(C @ (np.eye(m) - C)); F = E @ W @ E.T; T = P @ (P @ F - F @ P) - (P @ F - F @ P) @ P S = float(np.real(np.trace(-W))); Heq = 1j \* 0.37 \* (T @ P - P @ T) tau = lambda t: offset(E.T @ (expm(-1j \* Heq \* t) @ P @ expm(1j \* Heq \* t)) @ E) d = lambda h: (tau(h) - tau(-h)) / (2 \* h) h = 1e-4; cd = d(h); rich = (4 \* d(h / 2) - d(h)) / 3 g = 0.5 \* fro2(-1j \* (Heq @ P - P @ Heq)) worst_cd = max(worst_cd, abs(cd\*\*2 / (4 \* g \* S) - 1)); worst_r = max(worst_r, abs(rich\*\*2 / (4 \* g \* S) - 1)) print('step 1e-4 central difference: worst |ratio - 1| = %.1e; Richardson: %.1e' % (worst_cd, worst_r))


