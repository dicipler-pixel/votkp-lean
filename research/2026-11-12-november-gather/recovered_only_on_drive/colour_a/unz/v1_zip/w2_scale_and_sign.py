# SCRIPT: WEIGHT-SCALE-SIGN-01
# Two follow-ups, both drawn from his own papers:
#   (a) FOFT "taring" remark (i): commutator / gap / off-diagonal readings are blind to K -> K + cI; Dirac Time 9.4:
#       projector geometry is blind to H -> sH (s > 0). So light's map is blind to the whole affine change sH + cI.
#       What happens at s < 0 (the clock run backwards)?
#   (b) Offset paper: Tr K_A = log-odds of empty against full. Does running the clock backwards (H -> -H) flip it?
# CONTROL for (b): the incommensurate-block Rice-Mele offset |Tr h_A| = 2 artanh(v / sqrt(Emin Emax)) at
#   t1 = 0.6, t2 = 1.0, v = 0.4 must come out as 0.88115707603717 (to 1e-8 on a long open chain).
# KILL CONDITIONS (written before the run):
#   Ka: if the projector or IQGT tensor moves by > 1e-12 under sH + cI with s > 0, "light is blind to the affine
#       pair" dies.
#   Kb: if Tr h_A under H -> -H is not exactly -Tr h_A (to 1e-10), "the offset's sign is the clock's direction" dies.
import numpy as np
rng = np.random.default_rng(11)
def herm(n):
    X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (X + X.conj().T) / 2
def proj_low(H, k):
    w, V = np.linalg.eigh(H); return V[:, :k] @ V[:, :k].conj().T
def tangent(Hm, V, k):
    w, Vec = np.linalg.eigh(Hm); X = Vec.conj().T @ V @ Vec; T = np.zeros_like(X)
    for a in range(k):
        for b in range(k, len(w)):
            T[a, b] = X[a, b] / (w[a] - w[b]); T[b, a] = X[b, a] / (w[a] - w[b])
    return Vec @ T @ Vec.conj().T
def Q(Hm, V1, V2, k):
    P = proj_low(Hm, k); d1, d2 = tangent(Hm, V1, k), tangent(Hm, V2, k)
    return P, np.array([[np.trace(P @ x @ y) for y in (d1, d2)] for x in (d1, d2)])

n, k = 6, 2
H0, H1, H2 = herm(n), herm(n), herm(n)
P0, Q0 = Q(H0, H1, H2, k)
for s, c in [(3.0, 0.0), (0.2, 5.0), (7.0, -11.0)]:
    # the family s(H0 + a H1 + b H2) + c(a, b) I: its tangents are s H1 + c_a I and s H2 + c_b I
    P1, Q1 = Q(s * H0 + c * np.eye(n), s * H1 + 2.0 * np.eye(n), s * H2 - 3.0 * np.eye(n), k)
    print('(a) s = %4.1f c = %6.1f: projector change %.1e, IQGT tensor change %.1e' % (s, c, abs(P1 - P0).max(), abs(Q1 - Q0).max()))
Pm = proj_low(-H0, n - k)
print('(a) s = -1: the lowest %d levels of -H are the highest %d of H; occupied and empty swap: %.1e'
      % (n - k, n - k, abs(Pm - (np.eye(n) - P0)).max()))

# (b) Rice-Mele chain, open, half filled; block of odd length in the middle. The block's occupation eigenvalues sit
# exponentially close to 0 and 1, so the correlation matrix is built at 60 digits (mpmath), not in floating point.
import mpmath as mp
mp.mp.dps = 60
def rice_mele(N, t1, t2, v):
    H = mp.zeros(N, N)
    for i in range(N - 1):
        H[i, i + 1] = H[i + 1, i] = -(t1 if i % 2 == 0 else t2)
    for i in range(N):
        H[i, i] = v * (1 if i % 2 == 0 else -1)
    return H
def offset_from(E, V, a, L, N):
    occ = [j for j in range(N) if E[j] < 0]               # filled levels (half filling, zero is mid-gap)
    C = mp.zeros(L, L)
    for x in range(L):
        for y in range(L):
            C[x, y] = mp.fsum(V[a + x, j] * V[a + y, j] for j in occ)
    nu = mp.eigsy(C, eigvals_only=True)
    return mp.fsum(mp.log((1 - n_) / n_) for n_ in nu)     # Tr h_A with C_A = 1/(e^h + 1)
t1, t2, v = mp.mpf('0.6'), mp.mpf('1.0'), mp.mpf('0.4')
Emin, Emax = mp.sqrt((t1 - t2)**2 + v**2), mp.sqrt((t1 + t2)**2 + v**2)
target = 2 * mp.atanh(v / mp.sqrt(Emin * Emax))
N = 120
H = rice_mele(N, t1, t2, v)
E, V = mp.eigsy(H)
Em, Vm = mp.eigsy(-H)
for L in [9, 13, 17]:
    a = N // 2 - L // 2
    fwd = offset_from(E, V, a, L, N); bwd = offset_from(Em, Vm, a, L, N)
    print('(b) block L = %d: Tr h_A = %s  (|Tr| - closed form = %.1e)   clock reversed, H -> -H: %s   sum %.1e'
          % (L, mp.nstr(fwd, 15), float(abs(fwd) - target), mp.nstr(bwd, 15), float(fwd + bwd)))
print('    closed form 2 artanh(v / sqrt(Emin Emax)) = %s' % mp.nstr(target, 15))
