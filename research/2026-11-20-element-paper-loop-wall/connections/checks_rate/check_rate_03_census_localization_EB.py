# SCRIPT: RATE-WEIGHT-CENSUS-LOCALIZATION-03
# Connections tested between The Offset Speed Limit / The Weight Between and The Loop Wall, section 7:
#  (a) the junction sum rule  sum_{j != i} ||P_ij||^2 = Tr(C_i - C_i^2)  is the census identity
#      C - C^2 = P12 P12^dagger of The Offset Speed Limit (Census.lean projector_block_coupling) with the
#      accessible block E = the orbitals of site i;
#  (b) the localization second moment  Var(X) = Tr(P X (1-P) X) = (1/2) sum_ij ||P_ij||^2 (x_i - x_j)^2
#      is the coupling energy E_B = ||P X (1-P)||_F^2 of The Weight Between with the position operator X
#      in place of H, hence equal to g = (1/2)||[X, P]||_F^2 (Proposition 5) -- the projector speed under
#      the twist P(s) = exp(-i s X) P exp(i s X);
#  (c) consequence of Theorem 1 + (b): for ANY accessible block E, the offset of that block moves under
#      the twist no faster than |d tau/ds| <= 2 sqrt(Var(X) * S_E); a block made of whole sites is frozen.
# WHY THE CHECK PROVES IT: (a) and (b) are finite algebraic identities -- (a) is the (i,i) block of P^2 = P,
# (b) is Tr(PX(1-P)X) = Tr((PX(1-P))(PX(1-P))^dagger) plus X diagonal; they are checked on random
# projectors in random site partitions to machine precision, with a deliberate non-projector control that
# must break them. (c) is Theorem 1 applied to a specific one-parameter family; the check confirms the
# inequality and the frozen case numerically.
# KILL CONDITIONS (before running):
#   K1 any relative residual of (a) or (b) above 1e-10 on projectors;
#   K2 the non-projector control satisfies (a) to better than 1e-3 (the check would then be blind).
#      Run 1 used a 0.05 perturbation and K2 fired (smallest residual 5e-4); run 2 uses 0.3.
#   K3 any twist case with tau_dot^2 / (4 Var(X) S) > 1 + 1e-6;
#   K4 a whole-site block whose offset moves under the twist by more than 1e-9.
import numpy as np
from scipy.linalg import expm, logm

rng = np.random.default_rng(1121)

def rand_proj(n, r):
    A = rng.normal(size=(n, r)) + 1j * rng.normal(size=(n, r))
    Q, _ = np.linalg.qr(A)
    return Q @ Q.conj().T

def offset(C):
    w = np.linalg.eigvalsh(C)
    return float(np.sum(np.log(1 - w) - np.log(w)))

worst_a = worst_b = 0.0
ctrl = 1e9
worst_twist = 0.0
worst_frozen = 0.0
for trial in range(300):
    nsites = rng.integers(3, 7)
    sizes = rng.integers(1, 4, size=nsites)
    n = int(sizes.sum())
    r = int(rng.integers(1, n))
    P = rand_proj(n, r)
    idx = np.split(np.arange(n), np.cumsum(sizes)[:-1])
    xs = rng.normal(size=nsites)
    X = np.diag(np.concatenate([np.full(len(I), xs[k]) for k, I in enumerate(idx)]))
    # (a)
    for i, I in enumerate(idx):
        Ci = P[np.ix_(I, I)]
        lhs = sum(np.linalg.norm(P[np.ix_(I, J)]) ** 2 for j, J in enumerate(idx) if j != i)
        rhs = np.trace(Ci - Ci @ Ci).real
        worst_a = max(worst_a, abs(lhs - rhs) / max(1e-12, abs(rhs)))
    # (b)
    var = np.trace(P @ X @ (np.eye(n) - P) @ X).real
    EB = np.linalg.norm(P @ X @ (np.eye(n) - P)) ** 2
    g = 0.5 * np.linalg.norm(X @ P - P @ X) ** 2
    pair = 0.5 * sum(np.linalg.norm(P[np.ix_(I, J)]) ** 2 * (xs[i] - xs[j]) ** 2
                     for i, I in enumerate(idx) for j, J in enumerate(idx))
    worst_b = max(worst_b, max(abs(var - EB), abs(var - g), abs(var - pair)) / max(1e-12, var))
    # control: a Hermitian non-projector
    M = P + 0.3 * (lambda B: (B + B.conj().T) / 2)(rng.normal(size=(n, n)))
    I0 = idx[0]
    lhs = sum(np.linalg.norm(M[np.ix_(I0, J)]) ** 2 for j, J in enumerate(idx) if j != 0)
    C0 = M[np.ix_(I0, I0)]
    rhs = np.trace(C0 - C0 @ C0).real
    ctrl = min(ctrl, abs(lhs - rhs) / max(1e-12, abs(rhs)))
    # (c) twist: a random accessible block (random isometry E, m modes) and a whole-site block
    m = int(rng.integers(1, max(2, n // 2) + 1))
    E, _ = np.linalg.qr(rng.normal(size=(n, m)) + 1j * rng.normal(size=(n, m)))
    def Pof(s):
        U = expm(-1j * s * X)
        return U @ P @ U.conj().T
    C = E.conj().T @ P @ E
    wv = np.linalg.eigvalsh(C)
    if wv.min() > 1e-3 and wv.max() < 1 - 1e-3:
        ds = 1e-5
        td = (offset(E.conj().T @ Pof(ds) @ E) - offset(E.conj().T @ Pof(-ds) @ E)) / (2 * ds)
        S = float(np.sum(1 / (wv * (1 - wv))))
        worst_twist = max(worst_twist, td * td / (4 * var * S))
    I = idx[0]
    Cs = P[np.ix_(I, I)]
    ws = np.linalg.eigvalsh(Cs)
    if ws.min() > 1e-3 and ws.max() < 1 - 1e-3:
        Cs1 = Pof(0.7)[np.ix_(I, I)]
        worst_frozen = max(worst_frozen, abs(offset(Cs1) - offset(Cs)))
print(f'(a) census = junction sum rule, worst relative residual over 300 projectors: {worst_a:.2e}')
print(f'    non-projector control: smallest relative residual {ctrl:.2e} (must be large)')
print(f'(b) Var(X) = E_B[X] = (1/2)||[X,P]||^2 = (1/2) sum ||P_ij||^2 (x_i-x_j)^2, worst relative residual: {worst_b:.2e}')
print(f'(c) twist offset speed: largest tau_dot^2/(4 Var(X) S) over random blocks = {worst_twist:.6f}')
print(f'    whole-site block offset change under a finite twist: {worst_frozen:.2e}')

# half-filled chain, as in the element paper: per-site census 1/4, nearest share 8/pi^2
L = 400
k = 2 * np.pi * np.arange(L) / L
occ = np.cos(k) < 0  # half filling, H = -cos k convention irrelevant for the share
# P_{0,R} = (1/L) sum_occ e^{ikR}
R = np.arange(L)
P0R = np.array([np.sum(np.exp(1j * k[occ] * r)) / L for r in R])
budget = np.sum(np.abs(P0R[1:]) ** 2)
near = 2 * abs(P0R[1]) ** 2
print(f'half-filled ring L={L}: C_ii = {P0R[0].real:.4f}, census C-C^2 = {P0R[0].real - P0R[0].real**2:.4f}, '
      f'off-site budget = {budget:.4f}, nearest share = {near/budget:.4f} (8/pi^2 = {8/np.pi**2:.4f})')
print('KILL K1', 'FIRED' if max(worst_a, worst_b) > 1e-10 else 'not fired',
      '| K2', 'FIRED' if ctrl < 1e-3 else 'not fired',
      '| K3', 'FIRED' if worst_twist > 1 + 1e-6 else 'not fired',
      '| K4', 'FIRED' if worst_frozen > 1e-9 else 'not fired')
