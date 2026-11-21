# SCRIPT: CHECK-LOCALIZATION-WEIGHTS-01
# Independent re-read of Codex's supplied site-to-site weights X_R (no Codex code imported).
# For each file: sum rule sum_R X_R = nu, off-site budget B = nu - X_0, nearest-shell share,
# and the site-centre second moment per electron per direction, Tr(Lambda)/3 = (1/(2 nu)) sum_R X_R |R|^2 / 3,
# with R taken as the shortest periodic image (all tied images averaged; |R|^2 is the same for each).
import sys, glob, os, itertools, math
import numpy as np
def read(f):
    L = open(f).read().split('\n')
    m = int(L[0].split(',')[1]); nu = float(L[1].split(',')[1])
    A = np.array([[float(x) for x in L[i].split(',')[1:]] for i in (2, 3, 4)])
    rows = [l.split(',') for l in L[6:] if l.strip()]
    return m, nu, A, [((int(a), int(b), int(c)), float(x)) for a, b, c, x in rows]
for f in sorted(glob.glob(sys.argv[1] + '/*.csv')):
    m, nu, A, W = read(f)
    tot = sum(x for _, x in W); X0 = dict(W)[(0, 0, 0)]; B = nu - X0
    d2 = {}
    for (i, j, k), x in W:
        best = min(np.sum(((np.array([i, j, k]) + m*np.array(s)) @ A)**2) for s in itertools.product((-1, 0, 1), repeat=3))
        d2[(i, j, k)] = best
    nonzero = sorted(set(round(v, 6) for v in d2.values() if v > 1e-9))
    near = sum(x for key, x in W if abs(d2[key] - nonzero[0]) < 1e-6)
    lam = sum(x*d2[key] for key, x in W) / (2*nu) / 3
    print(f'{os.path.basename(f):14s} mesh {m:2d}  sum-rule error {tot-nu:+.2e}  nearest share {near/B:.6f}  Tr(Lambda)/3 {lam:.6f} A^2')
