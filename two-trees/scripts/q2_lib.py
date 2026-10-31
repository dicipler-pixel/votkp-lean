# SCRIPT: Q2-LIB
# Library for the relator-loop computations: real Riley branches, canonical lifts to PSL~(2,R), relator polygon area and turning.
import sys, math, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import sympy as sp, mpmath as mp
from census_lib import riley_poly, eps, S_, V_
mp.mp.dps = 120
PI = mp.pi

def riley_coeff_funcs(p, q):
    R = sp.Poly(riley_poly(p, q), V_)
    cs = R.all_coeffs()            # highest power of v first
    fs = [sp.lambdify(S_, c, 'mpmath') for c in cs]
    return fs

def real_roots(fs, s):
    co = [f(s) for f in fs]
    # drop leading zeros
    while co and abs(co[0]) < mp.mpf(10)**(-40) * max(abs(c) for c in co): co = co[1:]
    rts = mp.polyroots(co, maxsteps=500, extraprec=400)
    out = []
    for r in rts:
        if abs(mp.im(r)) < mp.mpf(10)**(-25) * (1 + abs(r)): out.append(mp.re(r))
    return sorted(out)

def letters(p, q):
    """relator a W b^-1 W^-1 as a list of (generator, +-1), W the Riley word for (p,q)."""
    e = eps(p, q); W = []
    for i, x in enumerate(e):
        g = 'b' if i % 2 == 0 else 'a'
        W.append((g, 1 if x > 0 else -1))
    Winv = [(g, -s) for g, s in reversed(W)]
    return [('a', 1)] + W + [('b', -1)] + Winv, W

def mats(s, v):
    a = mp.matrix([[s, 1], [0, 1/s]]); b = mp.matrix([[s, 0], [-v, 1/s]])
    return {('a', 1): a, ('a', -1): a**-1, ('b', 1): b, ('b', -1): b**-1}

def prod(M, lst):
    P = mp.eye(2)
    for l in lst: P = P * M[l]
    return P

def relation_residual(M, W):
    a, b = M[('a', 1)], M[('b', 1)]
    Wm = prod(M, W)
    d = a*Wm - Wm*b
    aw = a*Wm
    return max(abs(d[i, j]) for i in range(2) for j in range(2)) / max(abs(aw[i, j]) for i in range(2) for j in range(2))

def wrap(x):
    # to (-pi, pi]
    y = mp.fmod(x + PI, 2*PI)
    if y <= 0: y += 2*PI
    return y - PI

def lift_apply(Mt, th):
    """canonical lift (fixed-point lift) of the hyperbolic SL2(R) matrix Mt acting on vector angles"""
    v = mp.matrix([mp.cos(th), mp.sin(th)]); w = Mt * v
    return th + wrap(mp.atan2(w[1], w[0]) - th)

def lift_class(M, rel, th0=mp.mpf('0.3')):
    """apply the lifted relator word to angle th0 (rightmost letter first); return shift / pi (an integer for a relation)"""
    th = th0
    for l in reversed(rel): th = lift_apply(M[l], th)
    return (th - th0) / PI

# ---- hyperbolic geometry on the upper half plane, via the hyperboloid <X,X> = X0^2 - X1^2 - X2^2 = 1
def mobius(Mt, z):
    return (Mt[0, 0]*z + Mt[0, 1]) / (Mt[1, 0]*z + Mt[1, 1])
def hyp(z):
    x, y = mp.re(z), mp.im(z); r2 = x*x + y*y
    return mp.matrix([(r2 + 1)/(2*y), (r2 - 1)/(2*y), x/y])
def Q(U, V): return U[0]*V[0] - U[1]*V[1] - U[2]*V[2]
def det3(A, B, C):
    return (A[0]*(B[1]*C[2]-B[2]*C[1]) - A[1]*(B[0]*C[2]-B[2]*C[0]) + A[2]*(B[0]*C[1]-B[1]*C[0]))

def orbit(M, rel, o):
    pts = [o]; P = mp.eye(2)
    for l in rel:
        P = P * M[l]; pts.append(mobius(P, o))
    return pts

def tri_area(X, Y, Z, sgn):
    c = Q(X, Y) + Q(Y, Z) + Q(Z, X)
    return sgn * 2 * mp.atan(det3(X, Y, Z) / (1 + c))

def calibrate():
    # counterclockwise triangle in the upper half plane (Euclidean orientation): i, 2+i, 1+2i
    z = [mp.mpc(0, 1), mp.mpc(2, 1), mp.mpc(1, 2)]
    X = [hyp(t) for t in z]
    d = det3(*X)
    return 1 if d > 0 else -1
SG = calibrate()

def poly_area_turn(pts):
    """signed (winding-weighted) area by the fan from pts[0]; exterior-angle sum; closed polygon pts[0..n] with pts[n] ~ pts[0]"""
    X = [hyp(t) for t in pts[:-1]]; n = len(X)
    A = mp.mpf(0)
    for k in range(1, n - 1): A += tri_area(X[0], X[k], X[k+1], SG)
    # exterior angles
    def tangent_to(Xp, Xq):
        c = Q(Xp, Xq); T = Xq - c*Xp; return T / mp.sqrt(c*c - 1)
    E = mp.mpf(0)
    for k in range(n):
        Xk = X[k]; Xp = X[(k-1) % n]; Xn = X[(k+1) % n]
        U = -tangent_to(Xk, Xp)       # incoming direction at Xk
        V = tangent_to(Xk, Xn)        # outgoing direction
        cs = -Q(U, V) / mp.sqrt(Q(U, U) * Q(V, V))
        sn = SG * det3(Xk, U, V) / mp.sqrt(Q(U, U) * Q(V, V))
        E += mp.atan2(sn, cs)
    return A, E
