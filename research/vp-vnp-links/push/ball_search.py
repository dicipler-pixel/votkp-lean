# SCRIPT: VP-PUSH-BALL-01
# The 16 matrices of Mat_2(F2) placed in hyperbolic space (the ball, and higher dimensions, and products).
# ratio = mean squared distance over the 48 rank-2 pairs / mean squared distance over the 72 rank-1 pairs.
# Known: flat (Euclidean) maximum is exactly 1.5; every nonpositively curved space has ratio <= 2 (their quadrilateral rule).
# KILL LINES (written before the run):
#  B1 any placement with ratio > 2 + 1e-9 means the code is wrong.
#  B2 the question: can the ball beat 1.5?  If the best ratio found is <= 1.5 + 1e-6 at every scale and dimension,
#     "curvature lifts the ratio above flat" failed this way (for these searches).
#  B3 embedding test: the target with squared distances 1 (rank 1) and t (rank 2). Relative misfit below 1e-10 counts as embedded.
import numpy as np, itertools, sys
from scipy.optimize import minimize
rng = np.random.default_rng(2)
mats = [np.array(b).reshape(2, 2) for b in itertools.product((0, 1), repeat=4)]
def rk(M): 
    d = (M[0, 0]*M[1, 1] - M[0, 1]*M[1, 0]) % 2
    return 2 if d else (1 if M.any() else 0)
R = np.array([[rk((A + B) % 2) for B in mats] for A in mats]); iu = np.triu_indices(16, 1); r_pairs = R[iu]
m1, m2 = r_pairs == 1, r_pairs == 2; assert m1.sum() == 72 and m2.sum() == 48
def d2_batch(V, nfac):       # V: (B,16,nfac,n) tangent coordinates; product of nfac hyperbolic spaces, l2 product metric
    r = np.linalg.norm(V, axis=-1, keepdims=True) + 1e-300
    x0 = np.cosh(r)[..., 0]; xs = np.sinh(r)*V/r
    inner = x0[:, :, None, :]*x0[:, None, :, :] - np.einsum('bifn,bjfn->bijf', xs, xs)
    d = np.arccosh(np.maximum(inner, 1.0)); return (d**2).sum(-1)[:, iu[0], iu[1]]
def make(nfac, n):
    shape = (16, nfac, n); P = 16*nfac*n
    def ratio_batch(X): D = d2_batch(X.reshape((-1,) + shape), nfac); return D[:, m2].mean(1)/D[:, m1].mean(1)
    def fg(f_batch, x, h=1e-6):
        Xp = np.vstack([x[None, :], x[None, :] + h*np.eye(P), x[None, :] - h*np.eye(P)]); F = f_batch(Xp)
        return F[0], (F[1:P + 1] - F[P + 1:])/(2*h)
    return shape, P, ratio_batch, fg
print('=== B2 best ratio found')
best_cfg = {}
for nfac, n in ((1, 3), (1, 6), (1, 15), (2, 3), (3, 3), (2, 8)):
    shape, P, ratio_batch, fg = make(nfac, n); best = (0, None, None)
    for scale in (0.05, 0.5, 1.5, 3.0, 5.0):
        for rep in range(4 if P < 200 else 2):
            x0 = scale*rng.normal(size=P)/np.sqrt(n)
            res = minimize(lambda x: tuple(-np.asarray(t) for t in fg(ratio_batch, x)), x0, jac=True, method='L-BFGS-B', options=dict(maxiter=600))
            val = -res.fun
            if val > best[0]: best = (val, scale, res.x)
    V = best[2].reshape(shape); rad = np.linalg.norm(V, axis=-1).mean()
    D = d2_batch(best[2].reshape((1,) + shape), nfac)[0]
    print('%d factor(s) of hyperbolic %2d-space: best ratio %.6f  (start scale %.2f, mean radius %.2f; rank-1 distances %.3f to %.3f, rank-2 %.3f to %.3f)'
          % (nfac, n, best[0], best[1], rad, np.sqrt(D[m1].min()), np.sqrt(D[m1].max()), np.sqrt(D[m2].min()), np.sqrt(D[m2].max()))); sys.stdout.flush()
    best_cfg[(nfac, n)] = best[2]
print('=== B3 can the target with ratio exactly t sit in these spaces?')
for nfac, n in ((1, 3), (1, 15), (2, 8)):
    shape, P, ratio_batch, fg = make(nfac, n)
    for t in (1.5, 1.6, 1.75, 2.0):
        T = np.where(m1, 1.0, t)
        def misfit_batch(X):
            D = d2_batch(X.reshape((-1,) + shape), nfac); lam = (D*T).sum(1)/(T*T).sum()
            return ((D - lam[:, None]*T)**2).sum(1)/((lam[:, None]*T)**2).sum(1)
        bestm = 1e9
        for scale in (0.3, 1.5, 4.0):
            for rep in range(3 if P < 200 else 2):
                x0 = scale*rng.normal(size=P)/np.sqrt(n)
                res = minimize(lambda x: fg(misfit_batch, x), x0, jac=True, method='L-BFGS-B', options=dict(maxiter=1500, ftol=1e-15, gtol=1e-12))
                bestm = min(bestm, res.fun)
        print('%d factor(s) of hyperbolic %2d-space, target ratio %.2f: smallest relative misfit %.3e' % (nfac, n, t, bestm)); sys.stdout.flush()
