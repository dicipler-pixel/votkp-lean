# SCRIPT: ATLAS-NEXT-CENSUSLIB
# Two-bridge knots up to 8 crossings: Riley words, Riley polynomial, longitude, Alexander polynomial,
# Seifert matrix (independent, from a diagram), name and volume (SnapPy).
import warnings; warnings.filterwarnings('ignore')
import numpy as np, sympy as sp
from math import gcd

def cf(p, q):
    out = []
    while q:
        out.append(p // q); p, q = q, p % q
    return out

def census(maxc=8):
    seen = {}
    for p in range(3, 400, 2):
        for q in range(1, p):
            if gcd(p, q) != 1 or sum(cf(p, q)) > maxc: continue
            qi = pow(q, -1, p)
            cands = [x for x in (q, p - q, qi, p - qi)]
            qq = min(x for x in cands if x % 2 == 1)          # odd representative (mirror allowed)
            key = (p, min(cands))
            if key not in seen: seen[key] = (qq, sum(cf(p, q)))
    return sorted((p, v[0], v[1]) for (p, _), v in seen.items())

def eps(p, q):
    return [(-1) ** ((i * q) // p) for i in range(1, p)]

T = sp.symbols('t')
def alexander(p, q):
    e = eps(p, q); ex = [0]
    for x in e: ex.append(ex[-1] + x)
    D = sum((-1) ** k * T ** ex[k] for k in range(p))
    D = sp.expand(D * T ** (-min(ex)))
    if sp.Poly(D, T).LC() < 0: D = -D
    return sp.expand(D)

def riley_mats(s, v):
    a = np.array([[s, 1], [0, 1 / s]], complex); b = np.array([[s, 0], [-v, 1 / s]], complex)
    return a, b

def word(p, q, a, b):
    e = eps(p, q); W = np.eye(2, dtype=complex); ai, bi = np.linalg.inv(a), np.linalg.inv(b)
    for i, x in enumerate(e):
        g = (b if x > 0 else bi) if i % 2 == 0 else (a if x > 0 else ai)
        W = W @ g
    return W

def word_rev(p, q, a, b):
    e = eps(p, q); W = np.eye(2, dtype=complex); ai, bi = np.linalg.inv(a), np.linalg.inv(b)
    for i, x in reversed(list(enumerate(e))):
        g = (b if x > 0 else bi) if i % 2 == 0 else (a if x > 0 else ai)
        W = W @ g
    return W

S_, V_ = sp.symbols('s v')
_rcache = {}
def riley_poly(p, q):
    """Riley polynomial in v with coefficients polynomial in s (symbolic, exact)."""
    if (p, q) in _rcache: return _rcache[(p, q)]
    a = sp.Matrix([[S_, 1], [0, 1 / S_]]); b = sp.Matrix([[S_, 0], [-V_, 1 / S_]])
    ai, bi = a.inv(), b.inv(); W = sp.eye(2)
    for i, x in enumerate(eps(p, q)):
        W = W * ((b if x > 0 else bi) if i % 2 == 0 else (a if x > 0 else ai))
        W = W.applyfunc(sp.expand)
    E = sp.together(sp.expand((a * W - W * b)[0, 1]))   # a w = w b  <=>  this entry vanishes (Riley)
    R = sp.expand(sp.numer(E))
    R = sp.expand(R / S_ ** min(m[0] for m in sp.Poly(R, S_).monoms()))
    _rcache[(p, q)] = R
    return R

def longitude(p, q, s, v):
    a, b = riley_mats(s, v)
    w = word(p, q, a, b); wr = word_rev(p, q, a, b)
    e = sum(eps(p, q))
    return w @ wr @ np.linalg.matrix_power(np.linalg.inv(a) if e > 0 else a, 2 * abs(e))   # commutes with a (checked)

def seifert_V(p, q):
    import spherogram
    target = sp.Poly(alexander(p, q), T)
    for args in [(q, p), (p, q), (p - q, p), (p, p - q)]:
        for clos in ['denominator_closure', 'numerator_closure']:
            try:
                K = getattr(spherogram.RationalTangle(*args), clos)()
            except Exception:
                continue
            if len(K.link_components) != 1: continue
            V = np.array(K.seifert_matrix(), dtype=float)
            D = sp.Matrix(V.astype(int)) - T * sp.Matrix(V.astype(int)).T
            d = sp.expand(D.det())
            if d == 0: continue
            d = sp.Poly(sp.expand(d / T ** min(m[0] for m in sp.Poly(d, T).monoms())), T)
            if d.LC() < 0: d = -d
            if d == target: return V, K
    return None, None

def lt_sig(V, x):
    om = np.exp(2j * np.pi * x)
    H = (1 - om) * V + (1 - np.conj(om)) * V.T
    ev = np.linalg.eigvalsh(H)
    return int(np.sum(ev > 1e-7) - np.sum(ev < -1e-7))
