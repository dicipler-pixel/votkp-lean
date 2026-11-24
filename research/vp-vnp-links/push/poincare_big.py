# SCRIPT: VP-PUSH-POINCARE-02   flat Poincare constant on U_h for h = 6, 7, matrix-free (the shift-invert run in
# VP-PUSH-EXACT-01 was too slow at h = 6 and was stopped; h = 2..5 from that run stand).
import numpy as np, sys
from scipy.sparse.linalg import LinearOperator, eigsh
for h in (6, 7):
    pos = [(i, j) for i in range(h) for j in range(i + 1, h)]; m = len(pos); N = 1 << m; idx = {p: t for t, p in enumerate(pos)}
    codes = np.arange(N, dtype=np.int64); perms = []
    for j in range(h - 1):
        new = codes.copy()
        for k in range(j + 2, h): new ^= (((codes >> idx[(j + 1, k)]) & 1) << idx[(j, k)])
        new ^= (1 << idx[(j, j + 1)]); perms.append(new)
    def mv(x):
        x = np.asarray(x).ravel(); y = (h - 1)*x
        for p in perms: y = y - x[p]
        return y - 0.0          # L = sum_j (I - P_j); each P_j is an involution, so symmetric
    def mv_defl(x):             # push the constant vector up so the smallest eigenvalue found is the nonzero one
        x = np.asarray(x).ravel(); return mv(x) + 10.0*x.mean()*np.ones(N)
    lam = eigsh(LinearOperator((N, N), matvec=mv_defl, dtype=float), k=1, which='SA', tol=1e-7, maxiter=20000, return_eigenvectors=False)[0]
    print('h = %d: group order %d; smallest nonzero eigenvalue %.6f; flat constant C = %.4f' % (h, N, lam, 1/lam)); sys.stdout.flush()
