# SCRIPT: AREA-SYM
# KILL CONDITIONS (written before the run):
#  K1  tau(X)=D X^T D^-1 (D=diag(1,-v)) swaps a,b: dies if |tau(a)-b| or |tau(b)-a| > 1e-30.
#  K2  tau(W)=W for the Riley word of every tested (p,q), q odd: dies if residual > 1e-30 (projective) for any knot/branch.
#  K3  K=[[0,1],[v,0]] acts as z -> 1/(v conj z): orientation-reversing iff v>0, mirror l = {|z|=1/sqrt(v)}; dies if for some v>0 branch K a^-1 K^-1 != b or K W^-1 K^-1 != W.
#  K4  Vertex identity: K p_k(o) = g p_{k+m}(o) for o on l (g=(aW)^-1, m=|W|+1, indices mod 2m): dies if error > 1e-30.
#  K5  A(o)=0 for o on l, ANY point, v>0, including branches where the axes do NOT cross (trefoil): dies if |A| > 1e-30 at any tested point.
#  K6  A(K o) = -A(o) for random o, v>0 (odd under the reflection): dies if error > 1e-30.
#  K7  For v<0, K is a half-turn: A(K o)=+A(o) holds, and A is NOT identically 0 (dies if A=0 at all random points tested on v<0 branches, i.e. the opposite conclusion).
#  K8  o* lies on l exactly when axes cross (o* is crossing point); where they do not cross, o* is off l and A(o*) != 0.
import sys, random
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from q2_lib import *
mp.mp.dps = 50
random.seed(7)

def pm(X, Y):  # projective distance in PGL2 (X ~ cY), normalise by determinant sign-free ratio
    d = mp.mpf(0)
    i0 = max(((i, j) for i in range(2) for j in range(2)), key=lambda t: abs(Y[t[0], t[1]]))
    c = X[i0[0], i0[1]] / Y[i0[0], i0[1]]
    return max(abs(X[i, j] - c*Y[i, j]) for i in range(2) for j in range(2)) / max(abs(X[i, j]) for i in range(2) for j in range(2))

def Kact(v, z):  # isometry z -> 1/(v conj z) (v>0), and half-turn z -> 1/(v z)?? for v<0: matrix [[0,1],[v,0]] acts as Mobius z->1/(v z)
    if v > 0: return 1/(v*mp.conj(z))
    return 1/(v*z)

def area(M, rel, o):
    pts = orbit(M, rel, o); A, E = poly_area_turn(pts); return A

knots = {'3_1': (3, 1), '4_1': (5, 3), '5_2': (7, 3), '6_2': (11, 3), '6_1': (9, 7), '7_?(13,5)': (13, 5)}
import time
for nm, (p, q) in knots.items():
    t0 = time.time()
    try:
        fs = riley_coeff_funcs(p, q)
    except Exception as ex:
        print(nm, 'riley failed', ex); continue
    rel, W = letters(p, q); m = len(W) + 1
    print("=== %s (p,q)=(%d,%d), |W|=%d, relator length %d  (setup %.1fs)" % (nm, p, q, len(W), len(rel), time.time()-t0))
    for x in ['0.7', '1.2', '2.0', '3.5']:
        s = mp.e**mp.mpf(x)
        for v in real_roots(fs, s):
            if abs(v) < mp.mpf('1e-12'): continue
            M = mats(s, v); a, b = M[('a', 1)], M[('b', 1)]
            D = mp.matrix([[1, 0], [0, -v]]); Kmat = mp.matrix([[0, 1], [v, 0]])
            tau = lambda X: D * X.T * D**-1
            k1 = max(max(abs(tau(a)[i, j] - b[i, j]) for i in range(2) for j in range(2)), max(abs(tau(b)[i, j] - a[i, j]) for i in range(2) for j in range(2)))
            Wm = prod(M, W)
            k2 = max(abs(tau(Wm)[i, j] - Wm[i, j]) for i in range(2) for j in range(2)) / max(abs(Wm[i, j]) for i in range(2) for j in range(2))
            k3a = pm(Kmat * a**-1 * Kmat**-1, b); k3b = pm(Kmat * Wm**-1 * Kmat**-1, Wm)
            g = (a*Wm)**-1
            xa = s/(1-s*s); xb = (1-s*s)/(s*v); cross = (xb < xa < 0)
            line = 'v>0 reflection' if v > 0 else 'v<0 half-turn'
            # K4: vertices, base points on l (v>0) or arbitrary (v<0 uses half-turn K)
            if v > 0:
                R0 = 1/mp.sqrt(v); th = mp.mpf('0.9')
                o = R0*mp.mpc(mp.cos(th), mp.sin(th))
            else:
                o = mp.mpc(0.3, 1.1)
            pts = orbit(M, rel, o); N = len(pts) - 1
            Ko = Kact(v, o)
            k4 = max(abs(Kact(v, pts[k]) - mobius(g, pts[(k + m) % N])) for k in range(N)) if abs(Ko - o) < mp.mpf(10)**-40 else None
            # K5: A on l at several angles
            Aon = []
            if v > 0:
                for thv in ['0.2', '0.6', '1.0', '1.4', '2.0', '2.8']:
                    oo = R0*mp.mpc(mp.cos(mp.mpf(thv)), mp.sin(mp.mpf(thv)))
                    Aon.append(abs(area(M, rel, oo)))
            # K6/K7: random off-line points
            e6 = mp.mpf(0); Aoff = []
            for _ in range(3):
                oo = mp.mpc(random.uniform(-2, 2), random.uniform(0.3, 2.5))
                A1 = area(M, rel, oo); A2 = area(M, rel, Kact(v, oo)); Aoff.append(A1)
                e6 = max(e6, abs(A2 + A1) if v > 0 else abs(A2 - A1))
            # K8: o*
            line8 = ''
            if xa*xb > 0 or True:
                ystar2 = xa*(xb - xa)
                if cross:
                    ostar = mp.mpc(xa, mp.sqrt(ystar2))
                    onl = abs(abs(ostar)**2 - 1/v)
                    line8 = "o* crossing pt: ||o*|^2-1/v| = %s, A(o*) = %s" % (mp.nstr(onl, 3), mp.nstr(abs(area(M, rel, ostar)), 3))
                else:
                    ostar = mp.mpc(xa, mp.sqrt(abs(xa*(xa - xb))))
                    line8 = "axes do not cross (v>(s-1/s)^2 or v<0): o* off l, A(o*) = %s ; |o*|^2-1/v = %s" % (mp.nstr(area(M, rel, ostar), 8), mp.nstr(abs(ostar)**2 - 1/v, 4))
            print(" x=%s v=%s [%s%s] K1=%s K2=%s K3=%s,%s K4=%s" % (x, mp.nstr(v, 6), line, ', axes cross' if cross else '', mp.nstr(k1, 2), mp.nstr(k2, 2), mp.nstr(k3a, 2), mp.nstr(k3b, 2), mp.nstr(k4, 2) if k4 is not None else 'n/a'))
            if v > 0:
                print("      K5 max|A| on l (6 pts) = %s ; K6 max|A(Ko)+A(o)| = %s ; A off l = %s" % (mp.nstr(max(Aon), 3), mp.nstr(e6, 3), [mp.nstr(t, 5) for t in Aoff]))
            else:
                print("      K7 max|A(Ko)-A(o)| = %s ; A at random pts = %s" % (mp.nstr(e6, 3), [mp.nstr(t, 5) for t in Aoff]))
            print("      " + line8)
