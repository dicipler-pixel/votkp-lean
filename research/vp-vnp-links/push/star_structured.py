# SCRIPT: VP-PUSH-STAR-02
# Name the structure of the best star at mu = 2, then carry it to mu = 3 and mu = 4.
# Candidate: centre = the zero matrix and every matrix of rank 2 or more; one leg for each nonzero column vector x,
# holding the rank-1 matrices x (tensor) y.  Squared distances 0 / 1 / 4 as before.
# KILL LINE: at mu = 2 the candidate must give exactly 5/3 (the best found by search); otherwise the description is wrong.
import numpy as np, itertools, sys
from fractions import Fraction
src = open('star_search.py').read().split('for mu, flat, iters in')[0]; ns = {}; exec(src, ns)
setup, ratio_exact, anneal = ns['setup'], ns['ratio_exact'], ns['anneal']
def candidate(mu):
    n = mu*mu; vec = np.array(list(itertools.product((0, 1), repeat=n)), dtype=np.int64); lab = np.zeros(len(vec), dtype=np.int64)
    for t, v in enumerate(vec):
        M = v.reshape(mu, mu); rows = [tuple(r) for r in M if r.any()]
        if rows and len(set(rows)) == 1:                 # rank 1: all nonzero rows equal (over the two-element field)
            x = tuple(int(r.any()) for r in M); lab[t] = 1 + int(''.join(map(str, x)), 2)
    return lab
for mu in (2, 3, 4):
    N, A1, Am = setup(mu); lab = candidate(mu); ex = ratio_exact(lab, A1, Am)
    print('mu = %d: structured star ratio %s = %.6f ; flat maximum %.4f ; ceiling %d ; centre %d of %d, %d legs of %d'
          % (mu, ex, float(ex), 2 - 2.0**(1 - mu), mu, int((lab == 0).sum()), N, len(set(lab)) - 1, int((lab == 1).sum()) if (lab == 1).any() else int(np.bincount(lab)[1:].max())))
    sys.stdout.flush()
    if mu == 3:
        # improve by local search starting from the structured star
        def score(lab):
            c = lab == 0; same = lab[:, None] == lab[None, :]; cl = c[:, None] ^ c[None, :]
            d2 = np.where(same, 0.0, np.where(cl, 1.0, 4.0)); return d2[Am].mean()/d2[A1].mean()
        r = np.random.default_rng(1); cur = score(lab); L = lab.max(); improved = 0
        for it in range(12000):
            i = r.integers(N); old = lab[i]; lab[i] = r.integers(0, L + 1); new = score(lab)
            if new > cur + 1e-12: cur = new; improved += 1
            else: lab[i] = old
        print('        after 12000 single-point moves from that start: %s = %.6f (%d improving moves); centre %d' % (ratio_exact(lab, A1, Am), cur, improved, int((lab == 0).sum())))
