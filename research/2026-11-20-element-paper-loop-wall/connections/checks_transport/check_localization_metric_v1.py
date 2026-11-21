# SCRIPT: WTK-LOOPWALL-LOCALIZATION-METRIC-01
"""
Connection: the element paper's third reading, Var(X) = (1/2) sum_ij ||P_ij||^2 (x_i - x_j)^2,
is WTK's projector metric g = (1/2) Tr[(dP)^2] (Proposition 9) taken along the position
twist P(s) = e^{-isX} P e^{isX}, and the small-s limit of WTK section 6's distance
(1/2)||P(s) - P||_F^2. The junction sum rule is the zeroth moment of the same weights.

Why this check proves what it claims:
 - Algebra: dP/ds at s = 0 is -i[X, P]. For an orthogonal projector P (P = P^2 = P*),
   (1/2) Tr[(i[X,P])^2] = Tr(P X (1-P) X), and with X diagonal on sites this equals
   (1/2) sum_ij |P_ij|^2 (x_i - x_j)^2. If a random rank-k orthogonal projector on n sites,
   with sites grouped into blocks, gives all four numbers equal to machine precision
   (including a finite-difference derivative and the finite-s WTK distance divided by s^2),
   the identity holds on that example and the algebra above is the proof.
 - Sum rule: sum_{j != i} ||P_ij||^2 = Tr(C_i - C_i^2) for every block i must hold to
   machine precision; it uses only P^2 = P.
 - Negative control (WTK assumption A5: "the positive Hilbert-Schmidt metric is asserted
   only for orthogonal projectors"): for an oblique idempotent the same three expressions
   must DISAGREE. If they do, the identity is tied to the orthogonal case, as WTK says.
 - Two-level check of WTK Proposition 9: H = (Delta/2)(cos t sz + sin t sx), D = d sz.
   The ground-state diagonal weight <g|D|g>^2/d^2 = cos^2 t and the transition weight
   |<e|D|g>|^2/d^2 = sin^2 t sum to one. Reading Gamma = cos t, these are the element
   paper's R = Gamma^2 and T = 1 - Gamma^2, and the wall R = T falls at t = pi/4.
"""
import numpy as np
rng = np.random.default_rng(7)
n_sites, orb, k = 6, 2, 5
n = n_sites*orb
M = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
Q, _ = np.linalg.qr(M); V = Q[:, :k]; P = V @ V.conj().T
xs = rng.normal(size=n_sites)*2.0
X = np.diag(np.repeat(xs, orb))
blk = lambda i: slice(i*orb, (i+1)*orb)

def U(s): return np.diag(np.exp(-1j*s*np.diag(X)))
def Ps(s): return U(s) @ P @ U(s).conj().T
comm = -1j*(X @ P - P @ X)
g_comm = 0.5*np.trace(comm @ comm).real
h = 1e-5; dP = (Ps(h) - Ps(-h))/(2*h); g_fd = 0.5*np.trace(dP @ dP).real
var = np.trace(P @ X @ (np.eye(n) - P) @ X).real
w = 0.5*sum(np.linalg.norm(P[blk(i), blk(j)])**2*(xs[i]-xs[j])**2 for i in range(n_sites) for j in range(n_sites))
s = 1e-3; dist = 0.5*np.linalg.norm(Ps(s) - P)**2/s**2
print('orthogonal projector, rank', k, 'on', n_sites, 'sites x', orb, 'orbitals')
print(f'  (1/2)Tr[(dP)^2] commutator  = {g_comm:.12f}')
print(f'  (1/2)Tr[(dP)^2] finite diff = {g_fd:.12f}')
print(f'  Tr(P X (1-P) X)             = {var:.12f}')
print(f'  (1/2) sum |P_ij|^2 (xi-xj)^2 = {w:.12f}')
print(f'  WTK distance (1/2)||P(s)-P||^2 / s^2 at s=1e-3 = {dist:.12f}')
sr = max(abs(sum(np.linalg.norm(P[blk(i), blk(j)])**2 for j in range(n_sites) if j != i)
             - np.trace(P[blk(i), blk(i)] - P[blk(i), blk(i)] @ P[blk(i), blk(i)]).real) for i in range(n_sites))
print(f'  sum rule max error over sites = {sr:.2e}')

# oblique idempotent: same column space, different row space
Wl = Q[:, :k] + 0.6*rng.normal(size=(n, k))
Pi = V @ np.linalg.inv(Wl.conj().T @ V) @ Wl.conj().T
print('\nnegative control, oblique idempotent (||Pi^2 - Pi|| = %.1e, ||Pi - Pi*|| = %.3f)' % (np.linalg.norm(Pi@Pi-Pi), np.linalg.norm(Pi-Pi.conj().T)))
c2 = -1j*(X @ Pi - Pi @ X)
print(f'  (1/2)Tr[(dPi)^2] = {0.5*np.trace(c2 @ c2).real:.6f}')
print(f'  Tr(Pi X (1-Pi) X) = {np.trace(Pi @ X @ (np.eye(n)-Pi) @ X).real:.6f}')
print(f'  (1/2) sum |Pi_ij|^2 (xi-xj)^2 = {0.5*sum(np.linalg.norm(Pi[blk(i), blk(j)])**2*(xs[i]-xs[j])**2 for i in range(n_sites) for j in range(n_sites)):.6f}')

print('\nWTK Proposition 9 two-level reading, Gamma = cos t')
sz = np.diag([1., -1.]); sx = np.array([[0., 1.], [1., 0.]])
for t in [np.pi/8, np.pi/4, np.arccos(0.70873), np.arccos(0.70622)]:
    H = 0.5*(np.cos(t)*sz + np.sin(t)*sx); e, v = np.linalg.eigh(H); gs, ex = v[:, 0], v[:, 1]
    Rr = (gs @ sz @ gs)**2; Tt = (ex @ sz @ gs)**2
    print(f'  t = {np.degrees(t):8.4f} deg: <g|D|g>^2 = {Rr:.6f} (cos^2 t = {np.cos(t)**2:.6f}), |<e|D|g>|^2 = {Tt:.6f}, sum = {Rr+Tt:.6f}, outside(R>T)={Rr>Tt}')
