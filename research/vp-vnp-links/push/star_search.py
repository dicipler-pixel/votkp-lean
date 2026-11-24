# SCRIPT: VP-PUSH-STAR-01
# The best placement in the ball looked like a star: a centre cluster and equal legs. Here the star is made exact.
# A star placement: each matrix goes to the centre or to the end of one of L unit legs.
# Squared distances: 0 (same place), 1 (centre to leg end), 4 (two different leg ends).  A star is a tree, so it has
# nonpositive curvature, and the ratio is an exact rational number.
# KILL LINE: if no star placement exceeds the flat maximum (1.5 for mu = 2, 1.75 for mu = 3), "trees beat flat" failed this way.
import numpy as np, itertools, sys
from fractions import Fraction
rng = np.random.default_rng(4)
def setup(mu):
    n = mu*mu; vec = np.array(list(itertools.product((0, 1), repeat=n)), dtype=np.int64); N = len(vec)
    def rank2(M):
        M = M.copy(); r = 0
        for c in range(mu):
            p = next((i for i in range(r, mu) if M[i, c]), None)
            if p is None: continue
            M[[r, p]] = M[[p, r]]
            for i in range(mu):
                if i != r and M[i, c]: M[i] ^= M[r]
            r += 1
        return r
    code = vec @ (1 << np.arange(n)); rk = np.array([rank2(v.reshape(mu, mu)) for v in vec])
    X = code[:, None] ^ code[None, :]; lut = np.zeros(N, dtype=np.int64); lut[code] = rk
    R = lut[X]; return N, (R == 1), (R == mu)
def ratio_exact(lab, A1, Am):
    c = lab == 0; same = lab[:, None] == lab[None, :]; cl = c[:, None] ^ c[None, :]   # centre-to-leg pairs
    d2 = np.where(same, 0, np.where(cl, 1, 4))
    return Fraction(int(d2[Am].sum()), int(Am.sum())) / Fraction(int(d2[A1].sum()), int(A1.sum()))
def anneal(N, A1, Am, L, iters, seed):
    r = np.random.default_rng(seed); lab = r.integers(0, L + 1, size=N)
    def score(lab):
        c = lab == 0; same = lab[:, None] == lab[None, :]; cl = c[:, None] ^ c[None, :]
        d2 = np.where(same, 0.0, np.where(cl, 1.0, 4.0)); s1 = d2[A1].mean()
        return d2[Am].mean()/s1 if s1 > 0 else 0.0
    cur = score(lab); best = (cur, lab.copy())
    for it in range(iters):
        T = 0.02*(1 - it/iters) + 1e-4; i = r.integers(N); old = lab[i]; lab[i] = r.integers(0, L + 1); new = score(lab)
        if new >= cur or r.random() < np.exp((new - cur)/T):
            cur = new
            if cur > best[0]: best = (cur, lab.copy())
        else: lab[i] = old
    return best
for mu, flat, iters in ((2, Fraction(3, 2), 6000), (3, Fraction(7, 4), 2500)):
    N, A1, Am = setup(mu); top = (0, None, None)
    for L in ((2, 3, 4, 5, 6) if mu == 2 else (3, 4, 6, 8)):
        for seed in range(6 if mu == 2 else 2):
            b = anneal(N, A1, Am, L, iters, seed)
            if b[0] > top[0]: top = (b[0], b[1], L)
    lab = top[1]; ex = ratio_exact(lab, A1, Am); sizes = sorted(np.bincount(lab)[1:][np.bincount(lab)[1:] > 0].tolist(), reverse=True)
    print('mu = %d: best star ratio %s = %.6f  (flat maximum %s = %.4f, ceiling %d); centre holds %d of %d, legs hold %s'
          % (mu, ex, float(ex), flat, float(flat), mu, int((lab == 0).sum()), N, sizes)); sys.stdout.flush()
    np.save('best_star_mu%d.npy' % mu, lab)
