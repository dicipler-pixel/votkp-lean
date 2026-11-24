# SCRIPT: VP-PUSH-EXACT-01
# Exact flat-space values of two quantities from "VP != VNP over every field" (appendix D and F).
# (A) On Mat_mu(F2): ratio D(mu)^2 / D(1)^2 = mean squared distance over rank-mu steps / over rank-1 steps.
#     Their bound for every price: ratio <= mu.  Contracting hypothesis: ratio <= s^2 < mu for all prices.
#     For Euclidean placements both means are quadratic forms that share the characters of the additive group,
#     so the largest ratio is the largest ratio of the two character eigenvalues.
#     KILL LINE: predicted maximum 2 - 2^(1-mu); if the computed maximum differs, the derivation failed this way.
# (B) On U_h (upper unitriangular h x h over F2), generators x_j = 1 + E_{j,j+1}:
#     mean over g,a of |f(a) - f(ga)|^2  <=  C * sum over j of mean over a of |f(a) - f(x_j a)|^2.
#     For Euclidean targets the best C is 1 / (smallest nonzero eigenvalue of sum_j (I - P_j)).
#     KILL LINE: the paper says C stays bounded in h; if the computed C grows without bound, the reading failed this way.
import numpy as np, itertools
from scipy.sparse import coo_matrix, identity
from scipy.sparse.linalg import eigsh
def rank2(M):
    M = M.copy() % 2; r = 0; rows, cols = M.shape
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i, c]), None)
        if p is None: continue
        M[[r, p]] = M[[p, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        r += 1
    return r
print('=== (A) flat ceiling on Mat_mu(F2)')
for mu in (2, 3, 4):
    n = mu*mu; mats = [np.array(b, dtype=np.int64).reshape(mu, mu) for b in itertools.product((0, 1), repeat=n)]
    ranks = np.array([rank2(M) for M in mats]); vec = np.array([M.ravel() for M in mats])
    W1 = vec[ranks == 1]; Wm = vec[ranks == mu]; best = 0; arg = None; byrank = {}
    for B, rB in zip(vec[1:], ranks[1:]):
        l1 = 1 - np.mean(1 - 2*((W1 @ B) % 2)); lm = 1 - np.mean(1 - 2*((Wm @ B) % 2)); r = lm/l1
        byrank.setdefault(int(rB), set()).add(round(r, 6))
        if r > best: best, arg = r, int(rB)
    print('mu = %d: %d matrices, %d of rank 1, %d of rank mu; largest flat ratio %.6f (character of rank %d); predicted %.6f; ceiling for prices %d'
          % (mu, len(mats), len(W1), len(Wm), best, arg, 2 - 2.0**(1 - mu), mu))
    print('        ratio by rank of the character:', {k: sorted(v) for k, v in sorted(byrank.items())})
print('=== (B) flat Poincare constant on U_h')
for h in range(2, 7):
    pos = [(i, j) for i in range(h) for j in range(i + 1, h)]; m = len(pos); N = 1 << m; idx = {p: t for t, p in enumerate(pos)}
    codes = np.arange(N, dtype=np.int64); bits = {p: (codes >> idx[p]) & 1 for p in pos}
    rows_all = []; cols_all = []
    for j in range(h - 1):            # left multiplication by 1 + E_{j,j+1}: row j += row j+1
        new = codes.copy()
        for k in range(j + 2, h):     # entry (j,k) ^= entry (j+1,k)
            new ^= (bits[(j + 1, k)] << idx[(j, k)])
        new ^= (1 << idx[(j, j + 1)]) # entry (j,j+1) ^= 1 (diagonal of row j+1)
        rows_all.append(codes); cols_all.append(new)
    P = coo_matrix((np.ones(N*(h - 1)), (np.concatenate(rows_all), np.concatenate(cols_all))), shape=(N, N)).tocsr()
    L = (h - 1)*identity(N) - P
    if N <= 2048: ev = np.sort(np.linalg.eigvalsh(L.toarray())); lam = ev[1]
    else: lam = np.sort(eigsh(L, k=3, sigma=-0.01, which='LM', return_eigenvectors=False))[1]
    print('h = %d: group order %d; smallest nonzero eigenvalue %.6f; flat constant C = %.4f' % (h, N, lam, 1/lam))
