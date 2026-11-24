# SCRIPT: VP-LINKS-01
# Four checks linking the "VP != VNP over every field" proof (anthropics/formal-math, vp-vnp) to existing work.
# Their Theorem thm_cn: every price obeys the Bruhat-Tits inequality; its four-point form (lem_toolkit_b) is
#   diag1^2 + diag2^2 <= side1^2 + side2^2 + side3^2 + side4^2   for every quadrilateral, equality for Euclidean rectangles.
# KILL LINES (written before the run):
#  V1 hyperbolic ball: any violation in 300000 random quadrilaterals -> "the ball passes their curvature rule" failed this way.
#  V2 tetrahedron's own (Hilbert) distance: no violation in 300000 random quadrilaterals -> "the flat reader breaks it" failed this way.
#  V3 permutations with Hamming distance (already a squared flat distance): any violation of
#     Ham(a,c) + Ham(b,d) <= Ham(a,b) + Ham(b,c) + Ham(c,d) + Ham(d,a), exhaustive on Sym(3), random on Sym(7) -> failed this way.
#  V4 complete graph on k points: degree-zero expansion must be ceil(k/2), and the fewest wires across a balanced cut
#     must be at least 2k^2/9; degree-one constant with two-element coefficients must be 2 at k = 4 and k/3 at k = 5, 6.
import numpy as np, itertools
rng = np.random.default_rng(5)
def quad_excess(D):      # D: 4x4 distances of points a,b,c,d in cyclic order; positive = violation
    return D[0, 2]**2 + D[1, 3]**2 - (D[0, 1]**2 + D[1, 2]**2 + D[2, 3]**2 + D[3, 0]**2)
# V1 hyperbolic three-space (the ball), hyperboloid model
def hyp_pts(n, scale):
    v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]; rho = rng.exponential(scale, size=n)
    return np.c_[np.cosh(rho), np.sinh(rho)[:, None]*v]
def hyp_d(x, y): return np.arccosh(np.maximum(1.0, x[0]*y[0] - x[1:] @ y[1:]))
worst = -np.inf; viol = 0
for trial in range(300000):
    P = hyp_pts(4, rng.choice([0.05, 0.5, 2.0])); D = np.array([[hyp_d(p, q) for q in P] for p in P]); e = quad_excess(D)
    worst = max(worst, e/ (D**2).sum()); viol += e > 1e-9
print('V1 ball: violations %d of 300000; largest (diagonals - sides)/total = %.3e' % (viol, worst))
# V2 the tetrahedron's own distance: half the spread of the log ratios of barycentric coordinates
def simp_d(x, y): r = np.log(x/y); return 0.5*(r.max() - r.min())
viol = 0; worst = -np.inf; ex = None
for trial in range(300000):
    P = rng.dirichlet(np.ones(4)*rng.choice([0.7, 2.0, 8.0]), size=4); D = np.array([[simp_d(p, q) for q in P] for p in P]); e = quad_excess(D)
    viol += e > 1e-9
    if e/(D**2).sum() > worst: worst = e/(D**2).sum(); ex = (D[0, 2]**2 + D[1, 3]**2, D[0, 1]**2 + D[1, 2]**2 + D[2, 3]**2 + D[3, 0]**2)
print('V2 tetrahedron reader: violations %d of 300000; worst case diagonals^2 = %.4f against sides^2 = %.4f' % (viol, ex[0], ex[1]))
# V3 permutations, Hamming distance = number of points where they differ
def ham(a, b): return sum(x != y for x, y in zip(a, b))
S3 = list(itertools.permutations(range(3))); viol = 0; eq = 0; tot = 0
for a, b, c, d in itertools.product(S3, repeat=4):
    lhs = ham(a, c) + ham(b, d); rhs = ham(a, b) + ham(b, c) + ham(c, d) + ham(d, a); tot += 1; viol += lhs > rhs
    eq += (lhs == rhs and len({a, b, c, d}) == 4)
print('V3 Sym(3), all %d quadrilaterals: violations %d; equality with four distinct corners: %d' % (tot, viol, eq))
viol = 0
for trial in range(200000):
    a, b, c, d = (tuple(rng.permutation(7)) for _ in range(4)); viol += ham(a, c) + ham(b, d) > ham(a, b) + ham(b, c) + ham(c, d) + ham(d, a)
print('V3 Sym(7), 200000 random quadrilaterals: violations %d' % viol)
n = 6; a, b = rng.permutation(n), rng.permutation(n); Pa, Pb = np.eye(n)[a], np.eye(n)[b]
print('V3 identity: Hamming = half the squared Frobenius distance of the permutation matrices:', ham(a, b), 0.5*np.sum((Pa - Pb)**2))
# V4 the complete graph and complex
for k in range(4, 10):
    best0 = min((len(S)*(k - len(S)))/min(len(S), k - len(S)) for r in range(1, k) for S in [range(r)])
    bal = [s for s in range(1, k) if k/3 <= s <= 2*k/3]; cross = min(s*(k - s) for s in bal)
    print('V4 k = %d: degree-zero constant %.1f (ceil(k/2) = %d); fewest wires across a balanced cut %d (2k^2/9 = %.2f)' % (k, best0, -(-k//2), cross, 2*k*k/9))
def h1_F2(k):
    V = range(k); E = list(itertools.combinations(V, 2)); T = list(itertools.combinations(V, 3)); idx = {e: i for i, e in enumerate(E)}
    cob = set()
    for bits in itertools.product((0, 1), repeat=k - 1):
        g = (0,) + bits; cob.add(tuple(g[u] ^ g[v] for u, v in E))
    cob = np.array(sorted(cob)); best = None
    for f in itertools.product((0, 1), repeat=len(E)):
        fa = np.array(f); N = sum(f[idx[(u, v)]] ^ f[idx[(v, w)]] ^ f[idx[(u, w)]] for u, v, w in T)
        if N == 0: continue
        Dm = int((cob ^ fa).sum(1).min()); r = N/Dm; best = r if best is None else min(best, r)
    return best
for k in (4, 5, 6): print('V4 degree-one constant, two-element coefficients, k = %d: %.4f   (k/3 = %.4f)' % (k, h1_F2(k), k/3))
