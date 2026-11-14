# SCRIPT: WEIGHT-CONSTANT-01
# Question: where does a constant (the "weight" candidate: H -> H + c I, the trace part of a generator) show up?
# Four readers are put side by side on the same random operators:
#   (L) light / projector geometry: spectral projectors Pi and the IQGT tensor Q = Tr(Pi dPi dPi) of a family
#   (C) the connection book  (1/8)||[H,H*]||^2         (Non-normality is connection energy)
#   (O) the opposite book    (1/8)||H^2 - H*^2||^2
#   (T) time: the evolution e^{-iHt}; one branch alone vs. two branches whose constants differ
# KILL CONDITIONS (written before the run):
#   K1 "light is blind to the weight" dies if Pi or Q changes by more than 1e-10 when a constant (even one that moves
#      along the family, c(lambda)) is added.
#   K2 "the whole constant lands in the opposite book" dies if the connection book moves by more than 1e-10, or the
#      opposite book's change differs from the predicted 4c^2 r |E| + 4c sum_edges Re Tr(D_i + U D_j U*) form... stated
#      here simply: if (O' - O) differs from the edge-sum formula by more than 1e-10 relative.
#   K3 "time sees only differences of the constant" dies if (a) any single-branch expectation value moves when c is
#      added, or (b) the relative phase of two branches with constants c1, c2 differs from (c1 - c2) t.
import numpy as np
rng = np.random.default_rng(7)
fro2 = lambda X: float(np.real(np.vdot(X, X)))
def herm(n):
    X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (X + X.conj().T) / 2
def unitary(r):
    Q, R = np.linalg.qr(rng.normal(size=(r, r)) + 1j * rng.normal(size=(r, r))); return Q * (np.diag(R) / abs(np.diag(R)))
def proj(H, k):
    w, V = np.linalg.eigh(H); P = V[:, :k]; return P @ P.conj().T

# (L) projector geometry under H(l) = H0 + l H1 + c(l) I, with c(l) = 3 + 5 l + 7 l^2
n, k, eps = 6, 2, 1e-6
H0, H1, H2 = herm(n), herm(n), herm(n)
def fam(a, b, with_c):
    c = (3 + 5 * a + 7 * a * a - 4 * b) if with_c else 0.0
    return H0 + a * H1 + b * H2 + c * np.eye(n)
def Q_of(with_c):
    P = lambda a, b: proj(fam(a, b, with_c), k)
    P0 = P(0, 0); d1 = (P(eps, 0) - P(-eps, 0)) / (2 * eps); d2 = (P(0, eps) - P(0, -eps)) / (2 * eps)
    return P0, np.array([[np.trace(P0 @ x @ y) for y in (d1, d2)] for x in (d1, d2)])
P_a, Q_a = Q_of(False); P_b, Q_b = Q_of(True)
print('(L) finite differences: projector change %.1e, IQGT tensor change %.1e (difference-step noise)' % (np.abs(P_a - P_b).max(), np.abs(Q_a - Q_b).max()))
# exact tangent (Kato/Riesz first order): dPi = sum_{a occ, b empty} (|a><a|V|b><b| + h.c.)/(E_a - E_b); a constant
# direction V = c' I has <a|I|b> = 0 for a != b, so it cannot enter. Computed, not assumed:
def tangent(Hm, V, k):
    w, Vec = np.linalg.eigh(Hm); X = Vec.conj().T @ V @ Vec; T = np.zeros_like(X)
    for a in range(k):
        for b in range(k, len(w)):
            T[a, b] = X[a, b] / (w[a] - w[b]); T[b, a] = X[b, a] / (w[a] - w[b])
    return Vec @ T @ Vec.conj().T
for with_c, V1, V2 in [(False, H1, H2), (True, H1 + 5 * np.eye(n), H2 - 4 * np.eye(n))]:
    Hm = fam(0, 0, with_c); P0 = proj(Hm, k); d1, d2 = tangent(Hm, V1, k), tangent(Hm, V2, k)
    Qx = np.array([[np.trace(P0 @ x @ y) for y in (d1, d2)] for x in (d1, d2)])
    if not with_c: Qref = Qx
print('(L) exact tangents: IQGT tensor change with the moving constant %.1e' % np.abs(Qx - Qref).max())

# (C)/(O) graph operator H = D + A, constant added to every vertex field: D_i -> D_i + c I
nv, r = 5, 2
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2)]
Ds = [herm(r) for _ in range(nv)]; U = {e: unitary(r) for e in edges}
def build(c):
    D = np.zeros((nv * r, nv * r), complex); A = np.zeros_like(D)
    for i in range(nv): D[i*r:(i+1)*r, i*r:(i+1)*r] = Ds[i] + c * np.eye(r)
    for (i, j) in edges:
        A[i*r:(i+1)*r, j*r:(j+1)*r] = U[(i, j)]; A[j*r:(j+1)*r, i*r:(i+1)*r] = -U[(i, j)].conj().T
    return D + A, A
for c in [0.0, 0.5, 2.0]:
    H, A = build(c); Hs = H.conj().T
    Cb = fro2(H @ Hs - Hs @ H) / 8; Ob = fro2(H @ H - Hs @ Hs) / 8
    pred_O = sum(fro2(Ds[i] + U[e] @ Ds[j] @ U[e].conj().T + 2 * c * np.eye(r)) for e in edges for (i, j) in [e])
    print('(C,O) c = %.1f: connection book %.10f   opposite book %.6f   (edge formula with D_i + U D_j U* + 2c I: %.6f)' % (c, Cb, Ob, pred_O))

# (T) time
H = herm(4); psi = rng.normal(size=4) + 1j * rng.normal(size=4); psi /= np.linalg.norm(psi); Obs = herm(4)
def evolve(Hm, t):
    w, V = np.linalg.eigh(Hm); return V @ np.diag(np.exp(-1j * w * t)) @ V.conj().T
t = 2.7
ev = lambda Hm: np.vdot(evolve(Hm, t) @ psi, Obs @ evolve(Hm, t) @ psi).real
print('(T) single branch: expectation with c = 0: %.12f, with c = 9.3: %.12f' % (ev(H), ev(H + 9.3 * np.eye(4))))
c1, c2 = 9.3, 4.1
amp = np.vdot(evolve(H + c2 * np.eye(4), t) @ psi, evolve(H + c1 * np.eye(4), t) @ psi)
print('(T) two branches: relative phase %.12f, predicted -(c1 - c2) t = %.12f (mod 2pi)' %
      (np.angle(amp), np.angle(np.exp(-1j * (c1 - c2) * t))))

# the same constant as a clock rate: rest energy = h f_C (Compton frequency), so a mass is a frequency
h, cl, u = 6.62607015e-34, 2.99792458e8, 1.66053906660e-27
for name, m in [('electron', 9.1093837015e-31), ('cesium-133 atom', 132.905451961 * u), ('1 kg', 1.0)]:
    print('mass %-16s Compton frequency m c^2 / h = %.4e Hz' % (name, m * cl**2 / h))
