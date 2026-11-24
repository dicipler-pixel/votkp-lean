# SCRIPT: VP-PUSH-STRUCTURE-01  what does the best placement in the ball look like?
import numpy as np, itertools, importlib.util, io, contextlib
from scipy.optimize import minimize
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
src = open('ball_search.py').read().split("print('=== B2 best ratio found')")[0]
ns = {}; exec(src, ns)
rng = np.random.default_rng(11); make = ns['make']; d2_batch = ns['d2_batch']; iu = ns['iu']; m1 = ns['m1']; m2 = ns['m2']; mats = ns['mats']; R = ns['R']
shape, P, ratio_batch, fg = make(1, 3); best = (0, None)
for scale in (3.0, 5.0, 8.0):
    for rep in range(8):
        x0 = scale*rng.normal(size=P)/np.sqrt(3)
        res = minimize(lambda x: tuple(-np.asarray(t) for t in fg(ratio_batch, x)), x0, jac=True, method='L-BFGS-B', options=dict(maxiter=1500))
        if -res.fun > best[0]: best = (-res.fun, res.x)
print('best ratio in the ball this run: %.6f' % best[0])
D = np.sqrt(d2_batch(best[1].reshape((1,) + shape), 1)[0]); Dm = squareform(D); scale = np.median(D)
lab = fcluster(linkage(D, 'average'), 0.05*scale, 'distance'); k = lab.max()
print('clusters (points closer than 5 percent of the median distance):', k)
names = [''.join(map(str, M.ravel())) for M in mats]
for c in range(1, k + 1): print('  cluster', c, [names[i] for i in np.where(lab == c)[0]])
C = np.array([[Dm[np.ix_(lab == a, lab == b)].mean() for b in range(1, k + 1)] for a in range(1, k + 1)])/scale
np.set_printoptions(precision=2, suppress=True, linewidth=200); print('cluster-to-cluster distances / median:'); print(C)
# four-point (tree) test on cluster centres: for every four, the two largest of the three pair-sums must be equal
worst = 0
for a, b, c, d in itertools.combinations(range(k), 4):
    s = sorted([C[a, b] + C[c, d], C[a, c] + C[b, d], C[a, d] + C[b, c]]); worst = max(worst, (s[2] - s[1])/s[2])
print('largest relative failure of the tree (four-point) condition among cluster centres: %.4f' % worst)
np.save('best_ball.npy', best[1]); np.save('best_ball_labels.npy', lab)
