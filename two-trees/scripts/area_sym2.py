# SCRIPT: AREA-SYM2
# KILL CONDITIONS (written before the run):
#  K9  Sigma = g^-1 K (g=(aW)^-1) satisfies Sigma p_k = p_{k+m} for o on l, and Sigma^2 = identity as an isometry (a reflection in the perpendicular bisector of o and aW.o): dies if either error > 1e-25.
#  K10 Zero set of A on a grid (v>0, 4_1 and trefoil): sign changes of A occur only across l (A odd under the reflection). Dies if a sign change is found on a grid edge whose two endpoints lie on the SAME side of l.
#  K11 (3_1 etc.) the general-q statement: for q odd, e_{p-i}=e_i for all (p,q) with p<=60 (palindrome). Dies on any exception.
#  K12 a knot at larger size (13,5) passes K2-K5 at dps 100.
import sys, random
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from q2_lib import *
from math import gcd
mp.mp.dps = 100
# K11
bad = 0; cnt = 0
for p in range(3, 61, 2):
    for q in range(1, p, 2):
        if gcd(p, q) != 1: continue
        e = eps(p, q); cnt += 1
        if any(e[i-1] != e[p-i-1] for i in range(1, p)): bad += 1
print("K11 palindrome e_{p-i}=e_i for odd q: %d pairs (p<=59), failures %d" % (cnt, bad))
def area(M, rel, o):
    pts = orbit(M, rel, o); A, E = poly_area_turn(pts); return A
def side(v, z): return abs(z)**2*v - 1   # >0 outside l (|z|>1/sqrt v)
for nm, (p, q), x in [('3_1', (3, 1), '1.0'), ('4_1', (5, 3), '1.2'), ('5_2', (7, 3), '1.2')]:
    fs = riley_coeff_funcs(p, q); rel, W = letters(p, q); m = len(W) + 1; N = 2*m
    s = mp.e**mp.mpf(x)
    for v in real_roots(fs, s):
        if v <= 0: continue
        M = mats(s, v); a = M[('a', 1)]; Wm = prod(M, W); g = (a*Wm)**-1
        o = mp.sqrt(1/v)*mp.mpc(mp.cos(0.8), mp.sin(0.8))
        # Sigma z = g^-1 (K z), K z = 1/(v conj z)
        Sg = lambda z: mobius(g**-1, 1/(v*mp.conj(z)))
        pts = orbit(M, rel, o)
        e1 = max(abs(Sg(pts[k]) - pts[(k+m) % N]) for k in range(N))
        z = mp.mpc(0.37, 0.9); e2 = abs(Sg(Sg(z)) - z)
        print("K9 %s x=%s v=%s: max|Sigma p_k - p_{k+m}| = %s ; |Sigma^2 z - z| = %s" % (nm, x, mp.nstr(v, 6), mp.nstr(e1, 3), mp.nstr(e2, 3)))
        # K10 grid
        mp.mp.dps = 40
        xs = [mp.mpf(-1.5) + mp.mpf(3)*i/16 for i in range(17)]; ys = [mp.mpf('0.15') + mp.mpf('2.2')*j/16 for j in range(17)]
        G = [[area(M, rel, mp.mpc(xx, yy)) for xx in xs] for yy in ys]
        viol = 0; chg = 0; zero_near = 0
        for j in range(17):
            for i in range(17):
                for (di, dj) in [(1, 0), (0, 1)]:
                    i2, j2 = i+di, j+dj
                    if i2 > 16 or j2 > 16: continue
                    if G[j][i]*G[j2][i2] < 0:
                        chg += 1
                        s1 = side(v, mp.mpc(xs[i], ys[j])); s2 = side(v, mp.mpc(xs[i2], ys[j2]))
                        if s1*s2 > 0: viol += 1
        print("K10 %s v=%s: grid edges with a sign change of A = %d; of these with both ends on the same side of l = %d; A range [%s, %s]" % (nm, mp.nstr(v, 5), chg, viol, mp.nstr(min(min(r) for r in G), 4), mp.nstr(max(max(r) for r in G), 4)))
        mp.mp.dps = 100
# K12
p, q = 13, 5
fs = riley_coeff_funcs(p, q); rel, W = letters(p, q)
for x in ['1.2', '2.0']:
    s = mp.e**mp.mpf(x)
    for v in real_roots(fs, s):
        if v <= 0: continue
        M = mats(s, v)
        try:
            ls = []
            for th in ['0.5', '1.1', '2.2']:
                oo = mp.sqrt(1/v)*mp.mpc(mp.cos(mp.mpf(th)), mp.sin(mp.mpf(th)))
                ls.append(abs(area(M, rel, oo)))
            off = area(M, rel, mp.mpc(0.4, 1.3))
            print("K12 (13,5) x=%s v=%s: max|A| on l = %s ; A off l = %s" % (x, mp.nstr(v, 6), mp.nstr(max(ls), 3), mp.nstr(off, 6)))
        except Exception as ex:
            print("K12 x=%s v=%s exception %r" % (x, mp.nstr(v, 6), ex))
