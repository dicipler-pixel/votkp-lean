# SCRIPT: T15-BALL-TESTS
# One-ball picture, unequal steps.  Placement: Two Trees in One Ball v4, Def 4.1 (hyperboloid, o=(1,0,0,0),
# step of ratio z along unit axis u = boost of rapidity ln z).  boost() is reused from
# /home/claude/onenotes/cell_check_01.py (ONE-BALL-CELL-CHECK-01).  All kill lines below were written before the run.
import numpy as np, math, itertools, json, sys
from fractions import Fraction
import mpmath as mp, sympy as sp
mp.mp.dps = 40
eta = np.diag([1., -1, -1, -1])
def boost(u, r):
    c, s = math.cosh(r), math.sinh(r); B = np.eye(4); u = np.array(u, float)
    B[0, 0] = c; B[0, 1:] = s*u; B[1:, 0] = s*u; B[1:, 1:] = np.eye(3)+(c-1)*np.outer(u, u); return B
def mink(p, q): return float(p@eta@q)
E = np.eye(3); o = np.array([1., 0, 0, 0])
ZCL = 2.8900536383
def gof(z1, z2): return math.sinh(math.log(z1)/2)*math.sinh(math.log(z2)/2)
def fold(deg):
    d = deg % 360.0
    return d if d <= 180 else 360-d
OUT = {}; TAB = {}
def P(*a):
    print(*a); sys.stdout.flush()
base = [2, 3, 4, 5, 7, 11, 13]
PAIRS = [(a, b) for a, b in itertools.combinations(base, 2)] + [(ZCL, 5), (3, 3)]
EXTRA = [(5, 5), (7, 7), (ZCL, ZCL)]   # not in the task list; added because expected.json uses them
ALLP = PAIRS + EXTRA
def zs(z): return ('%g' % z) if float(z).is_integer() else ('%.10f' % z)

# ---------------------------------------------------------------------------------------------------------
# T1  UNEQUAL WALLS
# WHY THIS DECIDES: the walls are built here from the verbal definition only (midpoint m = B_u(h) o of the arm,
# h = ln z / 2, and the two directions perpendicular to the arm carried to m), never from n = (sinh h, cosh h u).
# (a) if the walls are apart, the smallest hyperbolic distance between a point of wall 1 and a point of wall 2
#     IS the separation; it is found by a 4-parameter minimisation from several random starts and compared with arccosh g.
# (b) if they cross, a point lying on both walls is solved for, checked to be equidistant from O and each
#     neighbour (that is what "halfway wall" means), and the angle is measured there between the two tangent
#     vectors (one in each wall, perpendicular to the crossing line, pointing along the part of the wall that
#     bounds the cell holding O).  That angle is the corner angle of O's cell and is compared with arccos g.
# KILL LINE: any mismatch above 1e-6 (radians for the angle, natural units for the distance).
# ---------------------------------------------------------------------------------------------------------
def wall(u, z):
    h = math.log(z)/2; u = np.array(u, float)
    m = boost(u, h)@o
    perp = [v for v in E if abs(v@u) < 1e-12]
    es = [boost(u, h)@np.concatenate([[0.], v]) for v in perp]
    return m, es[0], es[1]
def wp(W, a, b):
    m, e1, e2 = W; s = math.sqrt(1+a*a+b*b)
    p = s*m+a*e1+b*e2
    da = (a/s)*m+e1; db = (b/s)*m+e2
    daa = (1/s-a*a/s**3)*m; dbb = (1/s-b*b/s**3)*m; dab = (-a*b/s**3)*m
    return p, da, db, daa, dbb, dab
def FGH(W1, W2, x):
    p1, a1, b1, aa1, bb1, ab1 = wp(W1, x[0], x[1]); p2, a2, b2, aa2, bb2, ab2 = wp(W2, x[2], x[3])
    F = mink(p1, p2)
    g = np.array([mink(a1, p2), mink(b1, p2), mink(p1, a2), mink(p1, b2)])
    H = np.zeros((4, 4))
    H[0, 0] = mink(aa1, p2); H[1, 1] = mink(bb1, p2); H[0, 1] = H[1, 0] = mink(ab1, p2)
    H[2, 2] = mink(p1, aa2); H[3, 3] = mink(p1, bb2); H[2, 3] = H[3, 2] = mink(p1, ab2)
    for i, d1 in enumerate((a1, b1)):
        for j, d2 in enumerate((a2, b2)):
            H[i, 2+j] = H[2+j, i] = mink(d1, d2)
    return F, g, H
def mindist(W1, W2, x0):
    x = np.array(x0, float); lam = 1e-3; F, g, H = FGH(W1, W2, x)
    for it in range(500):
        try: step = -np.linalg.solve(H+lam*np.eye(4), g)
        except np.linalg.LinAlgError: lam *= 10; continue
        F2, g2, H2 = FGH(W1, W2, x+step)
        if F2 <= F:
            x = x+step; F, g, H = F2, g2, H2; lam = max(lam/10, 1e-14)
            if np.abs(g).max() < 1e-14: break
        else:
            lam *= 10
            if lam > 1e12: break
    return F, x, np.abs(g).max()
def nullspace(A, k):
    U, S, Vt = np.linalg.svd(A); return Vt[-k:].T, S
def angle_at_common_point(z1, z2):
    u1, u2, u3 = E[0], E[1], E[2]
    W1, W2 = wall(u1, z1), wall(u2, z2)
    I = boost(u1, math.log(z1))@o; J = boost(u2, math.log(z2))@o
    # common point: solve <p,o>=<p,I>, <p,o>=<p,J> inside span(o,u1,u2), then scale onto the hyperboloid
    A = np.array([(eta@(o-I))[:3], (eta@(o-J))[:3]])
    N, S = nullspace(A, 1); p3 = N[:, 0]
    p = np.array([p3[0], p3[1], p3[2], 0.]); nn = mink(p, p)
    if nn <= 0: return None
    p = p/math.sqrt(nn); p = p if p[0] > 0 else -p
    eq = max(abs(mink(p, o)-mink(p, I)), abs(mink(p, o)-mink(p, J)))
    def tangent(W):
        M = np.array(W).T                       # 4x3, columns m,e1,e2 : the wall is the hyperboloid cut by this 3-space
        row = np.array([[mink(M[:, k], p) for k in range(3)]])
        C, _ = nullspace(row, 2); return M@C, np.linalg.matrix_rank(M)
    T1, _ = tangent(W1); T2, _ = tangent(W2)
    # is p really in both wall 3-spaces?  residual of p against each span
    res = max(np.linalg.lstsq(np.array(W).T, p, rcond=None)[1].sum() if True else 0 for W in (W1, W2))
    C, S = nullspace(np.hstack([T1, -T2]), 1); L = T1@C[:2, 0]
    G = -eta
    def perp_in(T):
        a, b = T[:, 0], T[:, 1]
        # vector in span(a,b) orthogonal to L in the (positive) tangent metric
        ca, cb = L@G@a, L@G@b
        t = cb*a-ca*b; t = t/math.sqrt(t@G@t); return t
    t1, t2 = perp_in(T1), perp_in(T2)
    # orient t1 along the part of wall 1 lying on O's side of wall 2 (closer to O than to J), same for t2
    eps = 1e-4
    def side(t, Nb):
        q = math.cosh(eps)*p+math.sinh(eps)*t
        return 1.0 if mink(q, o) < mink(q, Nb) else -1.0
    t1 = t1*side(t1, J); t2 = t2*side(t2, I)
    cosang = max(-1.0, min(1.0, t1@G@t2))
    b = p[1:]/(1+p[0])
    return math.acos(cosang), eq, float(np.sqrt(res)) if res > 0 else 0.0, b, abs(L@G@np.array([0, 0, 0, 1.]))/math.sqrt(L@G@L)
P('T1  unequal walls')
rows = []; t1max = 0.0; rng = np.random.default_rng(15)
for (z1, z2) in ALLP:
    g = gof(z1, z2)
    if g > 1:
        W1, W2 = wall(E[0], z1), wall(E[1], z2)
        vals = []
        for st in range(6):
            F, x, gn = mindist(W1, W2, rng.normal(0, 1.0, 4) if st else np.zeros(4))
            vals.append(math.acosh(max(1.0, F)))
        d = min(vals); spread = max(vals)-min(vals); claim = math.acosh(g); err = abs(d-claim)
        rows.append((zs(z1), zs(z2), '%.9f' % g, 'gap', 'delta = %.9f' % claim, 'min dist = %.9f' % d, '%.1e' % err, 'starts spread %.1e' % spread))
        t1max = max(t1max, err, spread)
    else:
        ang, eq, res, b, Lk = angle_at_common_point(z1, z2); claim = math.acos(g); err = abs(ang-claim)
        rows.append((zs(z1), zs(z2), '%.9f' % g, 'overlap', 'alpha = %.6f deg' % math.degrees(claim), 'angle = %.6f deg' % math.degrees(ang), '%.1e' % err,
                     'common pt (%.6f, %.6f, 0); equidist err %.0e' % (b[0], b[1], eq)))
        t1max = max(t1max, err, eq)
    P(*rows[-1])
TAB['T1'] = (['z1', 'z2', 'g', 'kind', 'claimed', 'measured (independent)', 'mismatch (rad or dist)', 'note'], rows)
OUT['T1'] = dict(max_mismatch=t1max, kill_hit=bool(t1max > 1e-6)); P('T1 max mismatch', t1max, 'KILL HIT' if t1max > 1e-6 else 'kill line not hit')

# ---------------------------------------------------------------------------------------------------------
# T2  UNEQUAL SQUARE  c = B_a B_b B_a^-1 B_b^-1
# WHY THIS DECIDES: c moves only the (t, a, b) part and leaves the third axis alone, so its 4x4 trace is
# 2 + 2 cos phi if it is a turn about a point and 2 + 2 cosh tau if it is a run along a line; (tr-2)/2 below 1
# or above 1 tells which, and gives the size with no reference to g.  That measured size is compared with
# 4 arccos g (folded to [0,180]) or 4 arccosh g.  Done at 40 digits (mpmath) so the arccos near 0 or 180 is safe.
# KILL LINE: mismatch above 1e-7 (radians for phi, natural units for tau), or measured kind disagreeing with g<1 / g>1.
# Half-trace: for 2x2 lifts A = diag(e^(r1/2), e^(-r1/2)), B = [[ch, sh],[sh, ch]] (r2/2), perpendicular axes
# through one point, tr(A B A^-1 B^-1) = 2 - 4 g^2 is DERIVED symbolically below (sympy), and the relation
# 4x4 trace = (2 - 4 g^2)^2 is both derived symbolically and MEASURED on each pair.
# ---------------------------------------------------------------------------------------------------------
def mboost(axis, r):
    c, s = mp.cosh(r), mp.sinh(r); B = mp.eye(4)
    B[0, 0] = c; B[0, axis+1] = s; B[axis+1, 0] = s; B[axis+1, axis+1] = c; return B
def square_mp(z1, z2):
    r1, r2 = mp.log(mp.mpf(repr(z1)) if not float(z1).is_integer() else mp.mpf(int(z1))), mp.log(mp.mpf(repr(z2)) if not float(z2).is_integer() else mp.mpf(int(z2)))
    C = mboost(0, r1)*mboost(1, r2)*mboost(0, -r1)*mboost(1, -r2)
    tr = sum(C[i, i] for i in range(4)); g = mp.sinh(r1/2)*mp.sinh(r2/2)
    A = mp.matrix([[mp.exp(r1/2), 0], [0, mp.exp(-r1/2)]]); B = mp.matrix([[mp.cosh(r2/2), mp.sinh(r2/2)], [mp.sinh(r2/2), mp.cosh(r2/2)]])
    K = A*B*A**-1*B**-1
    return tr, g, K[0, 0]+K[1, 1]
P('T2  unequal square')
Z1, Z2 = sp.symbols('z1 z2', positive=True)
def sboost(axis, z, inv=False):
    c = (z+1/z)/2; s = (z-1/z)/2*(-1 if inv else 1); B = sp.eye(4); B[0, 0] = c; B[0, axis+1] = s; B[axis+1, 0] = s; B[axis+1, axis+1] = c; return B
Cs = sboost(0, Z1)*sboost(1, Z2)*sboost(0, Z1, True)*sboost(1, Z2, True)
g2 = (Z1-1)**2*(Z2-1)**2/(16*Z1*Z2)
d4 = sp.simplify(Cs.trace()-(2-4*g2)**2)
s1, s2 = sp.sqrt(Z1), sp.sqrt(Z2)
As = sp.Matrix([[s1, 0], [0, 1/s1]]); Bs = sp.Matrix([[(s2+1/s2)/2, (s2-1/s2)/2], [(s2-1/s2)/2, (s2+1/s2)/2]])
d2 = sp.simplify((As*Bs*As.inv()*Bs.inv()).trace()-(2-4*g2))
P('symbolic: 4x4 trace - (2-4g^2)^2 =', d4, ';  2x2 commutator trace - (2-4g^2) =', d2)
rows = []; t2max = mp.mpf(0); t2tr = mp.mpf(0); kindbad = 0
for (z1, z2) in ALLP:
    tr, g, k2 = square_mp(z1, z2); x = (tr-2)/2
    t2tr = max(t2tr, abs(tr-(2-4*g*g)**2)/max(1, abs(tr)), abs(k2-(2-4*g*g)))
    if x < 1:
        phi = mp.acos(x); claim = 4*mp.acos(g); cd = fold(float(mp.degrees(claim))); err = abs(mp.degrees(phi)-mp.mpf(fold(float(mp.degrees(claim)))))
        claimf = mp.radians(mp.mpf(1))*0+abs(phi-(lambda c: c if c <= mp.pi else 2*mp.pi-c)(claim % (2*mp.pi)))
        if not g < 1: kindbad += 1
        rows.append((zs(z1), zs(z2), '%.9f' % float(g), 'turn', 'phi = %.9f deg' % float(mp.degrees(phi)), '4 alpha = %.6f -> %.9f deg' % (float(mp.degrees(claim)), cd), '%.1e' % float(claimf), '%.9f' % float(2-4*g*g)))
        t2max = max(t2max, claimf)
    else:
        tau = mp.acosh(x); claim = 4*mp.acosh(g); err = abs(tau-claim)
        if not g > 1: kindbad += 1
        rows.append((zs(z1), zs(z2), '%.9f' % float(g), 'run', 'tau = %.9f' % float(tau), '4 delta = %.9f' % float(claim), '%.1e' % float(err), '%.9f' % float(2-4*g*g)))
        t2max = max(t2max, err)
    P(*rows[-1])
TAB['T2'] = (['z1', 'z2', 'g', 'kind (measured from trace)', 'measured', 'claimed', 'mismatch', '2 - 4 g^2 (= 2x2 commutator trace)'], rows)
OUT['T2'] = dict(max_mismatch=float(t2max), kind_disagreements=kindbad, max_trace_relation_err=float(t2tr), symbolic_4x4=str(d4), symbolic_2x2=str(d2), kill_hit=bool(t2max > 1e-7 or kindbad > 0))
P('T2 max mismatch', float(t2max), 'kind disagreements', kindbad, 'trace relation err', float(t2tr), 'KILL HIT' if (t2max > 1e-7 or kindbad) else 'kill line not hit')

# ---------------------------------------------------------------------------------------------------------
# T3  REVERSAL
# WHY THIS DECIDES: size is read from the trace as in T2 for all 8 variants (sign of a, sign of b, order).
# Sense of a turn: c fixes a point p (the eigenvector of eigenvalue 1 with no part along the third axis); take a
# tangent vector v at p in the a-b plane; the sign of det[p, v, c v, W], W = axis u_a x u_b, is the sign of sin(phi)
# (at p = o this is the ordinary "counter-clockwise seen from W").  So it is the turn direction as seen from W.
# Sense of a run: the attracting end e+ and repelling end e- on the rim of the ball (null eigenvectors, x/t);
# the run goes from e- to e+; sign of W.(e- x e+) says which way round O the line passes.
# Convention: order=+1 is the matrix product A B A^-1 B^-1 with A = B_a^(s_a), B = B_b^(s_b); order=-1 is B A B^-1 A^-1.
# KILL LINE: any size change above 1e-9 inside a pair, or a sense pattern that is not
#   sense = K * s_a * s_b * order, K = the sense of the all-plus variant of that pair.
# K itself is recorded for each pair (a literal reading with K fixed to +1 for every pair is reported separately).
# Extra check, recorded not killed: signed angle theta against  K0 * s_a*s_b*order * 4 alpha  (mod 360), one K0 for all pairs.
# Pairs (5,5), (3,5), (3,7) are the task's; (5,7) and (7,7) are added because the task's three are all turns
# and the run branch would otherwise go untested.
# ---------------------------------------------------------------------------------------------------------
P('T3  reversal')
Wax = np.array([0, 0, 0, 1.])
def analyse(C):
    x = (np.trace(C)-2)/2
    if x < 1:
        N, S = nullspace(C-np.eye(4), 2)
        # remove the W part
        a, b = N[:, 0], N[:, 1]
        p = b[3]*a-a[3]*b if abs(a[3])+abs(b[3]) > 1e-12 else (a if abs(mink(a, a)) > 1e-9 and mink(a, a) > 0 else b)
        p = p/math.sqrt(mink(p, p)); p = p if p[0] > 0 else -p
        e = np.array([0, 1., 0, 0]); v = e-mink(e, p)*p
        sgn = np.sign(np.linalg.det(np.column_stack([p, v, C@v, Wax])))
        return 'turn', math.degrees(math.acos(max(-1, min(1, x)))), sgn, p[1:]/(1+p[0]), None
    w, V = np.linalg.eig(C); w = w.real; V = V.real
    ep = V[:, np.argmax(w)]; em = V[:, np.argmin(w)]
    ep = ep[1:]/ep[0]; em = em[1:]/em[0]
    return 'run', math.acosh(x), np.sign(np.cross(em, ep)[2]), ep, em
rows = []; t3size = 0.0; t3pat = 0; Ks = {}; signedres = 0.0; K0 = None
for (z1, z2) in [(5, 5), (3, 5), (3, 7), (5, 7), (7, 7)]:
    r1, r2 = math.log(z1), math.log(z2); g = gof(z1, z2); sizes = []; K = None
    for order in (1, -1):
        for sa in (1, -1):
            for sb in (1, -1):
                A = boost(E[0], sa*r1); B = boost(E[1], sb*r2); Ai = boost(E[0], -sa*r1); Bi = boost(E[1], -sb*r2)
                C = A@B@Ai@Bi if order == 1 else B@A@Bi@Ai
                kind, size, sgn, q1, q2 = analyse(C); sizes.append(size)
                if K is None: K = sgn
                pred = K*sa*sb*order; ok = (sgn == pred); t3pat += (not ok)
                if kind == 'turn':
                    al4 = 4*math.degrees(math.acos(g))
                    if K0 is None: K0 = sgn*(1 if (al4 % 360) < 180 else -1)
                    res = ((sgn*size-K0*sa*sb*order*al4+180) % 360)-180; signedres = max(signedres, abs(res))
                    rows.append((zs(z1), zs(z2), '%+d' % sa, '%+d' % sb, 'a first' if order == 1 else 'b first', '%.9f' % g, 'turn', '%.9f deg' % size, '%+d' % sgn, '%+d' % pred,
                                 'centre (%.6f, %.6f, %.0f)' % (q1[0], q1[1], abs(q1[2]))))
                else:
                    rows.append((zs(z1), zs(z2), '%+d' % sa, '%+d' % sb, 'a first' if order == 1 else 'b first', '%.9f' % g, 'run', '%.9f' % size, '%+d' % sgn, '%+d' % pred,
                                 'runs toward (%.6f, %.6f, %.0f), from (%.6f, %.6f, %.0f)' % (q1[0], q1[1], abs(q1[2]), q2[0], q2[1], abs(q2[2]))))
                P(*rows[-1])
    Ks[zs(z1)+','+zs(z2)] = int(K)
    t3size = max(t3size, (max(sizes)-min(sizes))*(math.pi/180 if kind == 'turn' else 1))
TAB['T3'] = (['z_a', 'z_b', 's_a', 's_b', 'order', 'g', 'kind', 'size (abs phi or tau)', 'sense measured', 'K*s_a*s_b*order', 'centre of turn / ends of run (ball)'], rows)
OUT['T3'] = dict(max_size_change=t3size, pattern_violations=int(t3pat), K_per_pair=Ks, signed_4alpha_residual_deg=signedres, K0=int(K0), kill_hit=bool(t3size > 1e-9 or t3pat > 0))
P('T3 size change', t3size, 'pattern violations', t3pat, 'K per pair', Ks, 'signed 4alpha residual (deg)', signedres, 'K0', K0)

# ---------------------------------------------------------------------------------------------------------
# T4  WHOLE-NUMBER TABLE and exact searches
# WHY THIS DECIDES: g^2 = (z1-1)^2 (z2-1)^2 / (16 z1 z2) is a ratio of whole numbers for whole z, so
# g = 1, g = 1/2, g^2 = 1/2 are whole-number equations that are tested exactly (no rounding):
#   g = 1    <=> (z1-1)^2 (z2-1)^2 = 16 z1 z2
#   g = 1/2  <=> (z1-1)^2 (z2-1)^2 =  4 z1 z2
#   g^2 = 1/2 <=> (z1-1)^2 (z2-1)^2 =  8 z1 z2
# A pair either satisfies the identity exactly or does not.  No kill line (a census); range 2..300 as asked,
# also 2..5000 with plain integers as an added range.
# ---------------------------------------------------------------------------------------------------------
P('T4  whole-number table')
rows = []
for z1 in range(2, 14):
    for z2 in range(z1, 14):
        g = gof(z1, z2); ge = sp.Rational((z1-1)**2*(z2-1)**2, 16*z1*z2)
        if g < 1:
            a = math.degrees(math.acos(g)); rows.append((z1, z2, '%.9f' % g, str(ge), 'overlap', 'alpha = %.6f deg' % a, 'phi = %.6f deg' % fold(4*a)))
        else:
            d = math.acosh(g); rows.append((z1, z2, '%.9f' % g, str(ge), 'gap', 'delta = %.9f' % d, 'tau = %.9f' % (4*d)))
TAB['T4'] = (['z1', 'z2', 'g', 'g^2 exact', 'kind', 'alpha or delta', 'phi or tau'], rows)
search = {}
for name, k in (('g=1', 16), ('g=1/2', 4), ('g^2=1/2', 8)):
    hits = []
    for z1 in range(2, 301):
        for z2 in range(z1, 301):
            if sp.Integer(z1-1)**2*sp.Integer(z2-1)**2 == k*sp.Integer(z1)*sp.Integer(z2): hits.append((z1, z2))
    big = [(a, b) for a in range(2, 5001) for b in range(a, 5001) if (a-1)**2*(b-1)**2 == k*a*b]
    search[name] = dict(hits_2_300=hits, hits_2_5000=big); P(name, 'hits 2..300:', hits, ' hits 2..5000:', big)
    for (a, b) in hits:
        P('   check', (a, b), 'g =', sp.nsimplify(sp.sinh(sp.log(a)/2)*sp.sinh(sp.log(b)/2)), ' numeric', gof(a, b))
OUT['T4'] = search

# ---------------------------------------------------------------------------------------------------------
# T5  DO THREE UNEQUAL STEPS CLOSE?
# WHY THIS DECIDES (as far as it goes): a lattice of balls keeps a positive smallest distance between distinct
# points however deep the words go; if the smallest distance between distinct points keeps dropping with depth,
# the points are piling up and this placement is not a lattice at these steps.  ALL non-backtracking words are
# enumerated (no pruning at repeated points, because with unequal steps a repeated point need not have the same
# continuations).  Points are deduped at 1e-7 in ball coordinates as asked; for whole-number steps the points are
# also carried as exact fractions (the boosts are rational), deduped exactly, and the smallest pair is re-evaluated
# exactly, so a tiny distance cannot be a rounding artefact.  Distances use cosh d - 1 = -<p-q,p-q>/2 (stable for near points).
# KILL LINE (control only): the closing step z = 2.8900536383 on all three axes must keep smallest distance
# >= ln z - 1e-6 at depth 5.  Others: reported, falling or holding.
# ---------------------------------------------------------------------------------------------------------
P('T5  orbit growth')
AX6 = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]
def words(depth):
    lev = [()]; out = [[()]]
    for d in range(depth):
        lev = [w+(g,) for w in lev for g in range(6) if not (w and g == (w[-1] ^ 1))]; out.append(lev)
    return out
def minpair(Pf):
    n = len(Pf); best = (9e9, -1, -1)
    for s in range(0, n, 800):
        A = Pf[s:s+800]; D = np.zeros((len(A), n))
        for k in range(4):
            d = A[:, k][:, None]-Pf[:, k][None, :]; D += (-1 if k == 0 else 1)*d*d   # = -<p-q,p-q> = 2(cosh d - 1)
        for i in range(len(A)): D[i, :s+i+1] = np.inf
        j = np.argmin(D); i, jj = divmod(j, n)
        if D[i, jj] < best[0]: best = (D[i, jj], s+i, jj)
    return best
def balldedupe(Pf):
    Bc = Pf[:, 1:]/(1+Pf[:, :1]); n = len(Bc); keep = np.ones(n, bool)
    for s in range(0, n, 800):
        A = Bc[s:s+800]; D = np.zeros((len(A), n))
        for k in range(3):
            d = A[:, k][:, None]-Bc[:, k][None, :]; D += d*d
        for i in range(len(A)):
            if (D[i, :s+i] < 1e-14).any(): keep[s+i] = False
    return keep
def fboost(axis, z, sign):
    z = Fraction(z); c = (z+1/z)/2; s = (z-1/z)/2*sign
    B = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
    B[0][0] = c; B[0][axis+1] = s; B[axis+1][0] = s; B[axis+1][axis+1] = c; return B
def fmul(A, B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def orbit(tr, depth=5, exact=False):
    W = words(depth); res = []
    if exact:
        G = [fboost(a, tr[a], s) for a, s in AX6]; I4 = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
    else:
        G = [boost(E[a]*s, math.log(tr[a])) for a, s in AX6]; I4 = np.eye(4)
    mats = {(): I4}; pts = []; seen = {}
    for d in range(depth+1):
        new = {}
        for w in W[d]:
            if d: M = fmul(mats[w[:-1]], G[w[-1]]) if exact else mats[w[:-1]]@G[w[-1]]
            else: M = I4
            new[w] = M
            p = tuple(M[i][0] for i in range(4)) if exact else M[:, 0].copy()
            if exact:
                if p not in seen: seen[p] = w; pts.append(p)
            else: pts.append(p)
        mats = new
        if d == 0: continue
        if exact:
            Pf = np.array([[float(c) for c in p] for p in pts])
            if len(Pf) > 6000: res.append((d, len(Pf), None, None)); continue
            cands = []
            v, i, j = minpair(Pf)
            ip = sum((1 if k == 0 else -1)*pts[i][k]*pts[j][k] for k in range(4))
            dex = float(mp.acosh(mp.mpf(ip.numerator)/mp.mpf(ip.denominator)))
            res.append((d, len(Pf), dex, (seen[pts[i]], seen[pts[j]])))
        else:
            Pf = np.array(pts); keep = balldedupe(Pf); Pk = Pf[keep]
            if len(Pk) > 6000: res.append((d, len(Pk), None, None)); continue
            v, i, j = minpair(Pk); res.append((d, len(Pk), math.acosh(1+max(0.0, v)/2), None))
    return res
names = 'iIjJkK'
rows = []; OUT['T5'] = {}
zexact = (math.sqrt(math.cos(2*math.pi/5))+math.sqrt(1+math.cos(2*math.pi/5)))**2
for label, tr, ex in (('control (closing step, 10 digits)', (ZCL,)*3, False), ('control (closing step, full precision %.15f)' % zexact, (zexact,)*3, False),
                      ('(5,5,5)', (5, 5, 5), True), ('(3,5,7)', (3, 5, 7), True), ('(2,3,5)', (2, 3, 5), True), ('(5,7,11)', (5, 7, 11), True), ('(7,7,7)', (7, 7, 7), True)):
    rf = orbit(tr, 5, False); re_ = orbit(tr, 5, True) if ex else None
    lnz = [math.log(t) for t in tr]
    for k, (d, n, m, _) in enumerate(rf):
        if ex:
            de, ne, me, wp_ = re_[k]; ws = ' / '.join(''.join(names[g] for g in w) or 'O' for w in wp_)
            rows.append((label, d, n, '%.9f' % m, ne, '%.9f' % me, ws, '%.9f' % min(lnz)))
        else:
            rows.append((label, d, n, '%.9f' % m, '-', '-', '-', '%.9f' % min(lnz)))
        P(*rows[-1])
    OUT['T5'][label] = dict(float=[(d, n, m) for d, n, m, _ in rf], exact=[(d, n, m) for d, n, m, _ in re_] if ex else None, ln_z_min=min(lnz))
ctl = OUT['T5']['control (closing step, 10 digits)']['float'][-1]
OUT['T5']['kill_hit'] = bool(ctl[2] < math.log(ZCL)-1e-6); P('T5 control depth-5 smallest', ctl[2], 'ln z', math.log(ZCL), 'KILL HIT' if OUT['T5']['kill_hit'] else 'kill line not hit')
TAB['T5'] = (['triple', 'depth', 'distinct points (1e-7 ball dedupe)', 'smallest distance (float)', 'distinct points (exact fractions)', 'smallest distance (exact pair)', 'closest pair of words (i,j,k forward; I,J,K back)', 'smallest ln z'], rows)

# ---------------------------------------------------------------------------------------------------------
# T6  THE FOUR BALLS
# WHY THIS DECIDES: distances are read straight off the points, cosh d = <p,q>; the claim for two neighbours on
# perpendicular arms is cosh d = cosh r1 cosh r2 (hyperbolic Pythagoras, right angle at O), and O-neighbour = ln z.
# KILL LINE: any of the six distances off its claimed value by more than 1e-12.
# ---------------------------------------------------------------------------------------------------------
P('T6  four balls')
rows = []; t6 = 0.0
def four(tr):
    r = [math.log(t) for t in tr]; N = [boost(E[a], r[a])@o for a in range(3)]
    d0 = [math.acosh(mink(o, n)) for n in N]
    dn = {'IJ': math.acosh(mink(N[0], N[1])), 'JK': math.acosh(mink(N[1], N[2])), 'IK': math.acosh(mink(N[0], N[2]))}
    cl = {'IJ': math.acosh(math.cosh(r[0])*math.cosh(r[1])), 'JK': math.acosh(math.cosh(r[1])*math.cosh(r[2])), 'IK': math.acosh(math.cosh(r[0])*math.cosh(r[2]))}
    bc = [n[1:]/(1+n[0]) for n in N]
    return r, d0, dn, cl, bc
for tr in ((5, 5, 5), (3, 5, 7), (2, 3, 5), (7, 7, 7), (5, 7, 11)):
    r, d0, dn, cl, bc = four(tr)
    err = max(max(abs(d0[a]-r[a]) for a in range(3)), max(abs(dn[k]-cl[k]) for k in dn)); t6 = max(t6, err)
    rows.append((str(tr), ' / '.join('%.9f' % x for x in d0), ' / '.join('%.9f' % x for x in r), ' / '.join('%.9f' % dn[k] for k in ('IJ', 'JK', 'IK')),
                 ' / '.join('%.9f' % cl[k] for k in ('IJ', 'JK', 'IK')), '%.1e' % err, 'I (%.9f,0,0)  J (0,%.9f,0)  K (0,0,%.9f)' % (bc[0][0], bc[1][1], bc[2][2]),
                 ' / '.join('%.9f' % ((t-1)/(t+1)) for t in tr)))
    P(*rows[-1])
TAB['T6'] = (['triple', 'O-I / O-J / O-K measured', 'ln z', 'I-J / J-K / I-K measured', 'arccosh(cosh r1 cosh r2)', 'max mismatch', 'ball coordinates', 'Smith Gamma = (z-1)/(z+1) per arm'], rows)
OUT['T6'] = dict(max_mismatch=t6, kill_hit=bool(t6 > 1e-12)); P('T6 max mismatch', t6)

# ---------------------------------------------------------------------------------------------------------
# expected.json  (key dIJ in every pair entry = distance between the two neighbour balls OF THAT PAIR; values from the laws checked in T1, T2, T6; every pair used here is in the T1/T2 run list)
# ---------------------------------------------------------------------------------------------------------
exp = []
for tr in ((5, 5, 5), (3, 5, 7), (7, 7, 7), (ZCL, ZCL, ZCL), (2, 3, 5), (5, 7, 11)):
    ent = {'triple': list(tr), 'pairs': {}}
    for nm, (a, b) in (('IJ', (0, 1)), ('JK', (1, 2)), ('IK', (0, 2))):
        z1, z2 = tr[a], tr[b]; g = gof(z1, z2); d = math.acosh(math.cosh(math.log(z1))*math.cosh(math.log(z2)))
        covered = any({float(z1), float(z2)} == {float(x), float(y)} for x, y in ALLP); assert covered
        if g < 1:
            al = math.degrees(math.acos(g)); ent['pairs'][nm] = {'g': round(g, 9), 'kind': 'overlap', 'alpha_deg': round(al, 9), 'square': 'turn', 'phi_deg': round(fold(4*al), 9), 'dIJ': round(d, 9)}
        else:
            de = math.acosh(g); ent['pairs'][nm] = {'g': round(g, 9), 'kind': 'gap', 'delta': round(de, 9), 'square': 'run', 'tau': round(4*de, 9), 'dIJ': round(d, 9)}
    exp.append(ent)
json.dump(exp, open('expected.json', 'w'), indent=1)
json.dump(OUT, open('results.json', 'w'), indent=1, default=str)
with open('tables.md', 'w') as f:
    for k in ('T1', 'T2', 'T3', 'T4', 'T5', 'T6'):
        h, rows = TAB[k]; f.write('### %s\n\n| ' % k+' | '.join(h)+' |\n|'+'---|'*len(h)+'\n')
        for r in rows: f.write('| '+' | '.join(str(x) for x in r)+' |\n')
        f.write('\n')
P('done')
