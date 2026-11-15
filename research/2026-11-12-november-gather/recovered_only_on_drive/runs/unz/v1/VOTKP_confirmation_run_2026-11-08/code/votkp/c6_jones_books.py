# SCRIPT: c6_jones_books
"""C6. Two books read off the Jones string.

Let t = exp(i theta) run once round the unit circle and follow V_K(t).
  climb := Mahler measure of V_K (a function of the coefficients alone).
  turn  := signed area swept by V_K(t) divided by the mean of |V_K|^2.

Pre-registered rules (thresholds taken from the exploratory run, so this is a test of
those exact numbers):
  R1  Spearman(climb, volume) >= 0.80  -> CONFIRMED as "about 0.85"
  R2  climb carries volume beyond log det: partial Spearman(climb, vol | log det) >= 0.4,
      and linear R^2 rises from ~0.708 (log det alone) to ~0.810 (both).
  R3  Spearman(turn, |signature|) >= 0.75 -> CONFIRMED as "about 0.83"
  R4  neither book carries Chern-Simons: |Spearman| <= 0.25 for both against CS.
A quantity that does not reach its threshold on this data set is reported as refuted,
not rounded up.
"""
import sys, math, json, os, csv, ast
sys.path.insert(0,'code')
import numpy as np
import sympy as sp
from scipy.stats import spearmanr
import snappy

t = sp.symbols('t')
CSV = '.scratch/venv/lib/python3.12/site-packages/database_knotinfo/csv_data/knotinfo_data_complete.csv'

def parse_jones(s):
    s = s.replace(' ', '').replace('^', '**')
    return sp.sympify(s)

def to_poly(p):
    """Clear negative powers. M(t^N * e) = M(e) since M(t^N) = 1, so the shift is free."""
    e = sp.expand(p)
    for N in (40, 120, 400):
        try:
            return sp.Poly(sp.expand(e*t**N), t)
        except sp.PolynomialError:
            continue
    raise ValueError('could not clear negative powers')

def mahler(p):
    """Mahler measure, from the numeric roots of the (shifted) coefficient list."""
    c = np.array([float(x) for x in to_poly(p).all_coeffs()], dtype=float)
    if len(c) == 1: return abs(c[0])
    rts = np.roots(c)
    return float(abs(c[0])*np.prod(np.maximum(1.0, np.abs(rts))))

def turn(p):
    """Signed area swept by V(e^{i theta}) round the circle, / mean|V|^2, by quadrature."""
    f = sp.lambdify(t, p, 'numpy')
    th = np.linspace(0, 2*np.pi, 40001)
    with np.errstate(all='ignore'):
        vals = np.asarray(f(np.exp(1j*th)), dtype=complex)
    x, y = vals.real, vals.imag
    area = 0.5*np.sum(x[:-1]*y[1:] - x[1:]*y[:-1])          # shoelace, signed
    mean2 = np.mean(np.abs(vals)**2)
    return float(area/mean2)

def collect(fams):
    out = []
    csv.field_size_limit(10**9)
    want = set()
    import knotnames
    for f in fams: want |= set(knotnames.names_in(f))
    for r in csv.DictReader(open(CSV), delimiter='|'):
        nm = r['name']
        if nm not in want: continue
        if not r['jones_polynomial'] or not r['volume']: continue
        try:
            vol = float(r['volume']); sig = int(r['signature']); det = abs(int(r['determinant']))
        except Exception:
            continue
        if vol <= 0: continue                    # hyperbolic only
        out.append(dict(knot=nm, jones=r['jones_polynomial'], vol=vol, sig=sig, det=det))
    return out

if __name__ == '__main__':
    fams = sys.argv[1:] or ['4','5','6','7','8']
    rows = collect(fams)
    print(f'hyperbolic knots with a Jones polynomial: {len(rows)}')
    for r in rows:
        p = parse_jones(r['jones'])
        r['climb'] = mahler(p)
        r['turn'] = turn(p)
    # Chern-Simons, for R4
    import snappy
    for r in rows:
        try:
            import re
            m = re.match(r'^(\d+)([an])_(\d+)$', r['knot'])
            nm = f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else r['knot']
            M = snappy.Link(nm).exterior()
            cv = M.complex_volume()
            r['cs'] = float(cv.imag)
        except Exception:
            r['cs'] = None
    C = np.array([r['climb'] for r in rows]); V = np.array([r['vol'] for r in rows])
    T = np.array([r['turn'] for r in rows]); S = np.array([abs(r['sig']) for r in rows])
    D = np.log([r['det'] for r in rows])
    print(f"R1 Spearman(climb, volume)      = {spearmanr(C,V).statistic:+.4f}")
    print(f"R3 Spearman(turn, |signature|)  = {spearmanr(T,S).statistic:+.4f}")
    # partial correlation of climb and vol given log det
    import numpy.linalg as la
    def resid(a, b):
        A = np.vstack([np.ones_like(b), b]).T
        coef, *_ = la.lstsq(A, a, rcond=None)
        return a - A@coef
    pr = spearmanr(resid(C, D), resid(V, D)).statistic
    print(f"R2 partial Spearman(climb, vol | log det) = {pr:+.4f}")
    def r2(X, y):
        A = np.vstack([np.ones(len(y))] + list(X)).T
        coef, *_ = la.lstsq(A, y, rcond=None)
        pred = A@coef
        return 1 - np.sum((y-pred)**2)/np.sum((y-y.mean())**2)
    print(f"   R^2 log det alone      = {r2([D], V):.4f}")
    print(f"   R^2 log det + climb    = {r2([D,C], V):.4f}")
    have = [r for r in rows if r.get('cs') is not None]
    if len(have) > 10:
        Cs = np.array([r['cs'] for r in have]); Ch = np.array([r['climb'] for r in have])
        Tu = np.array([r['turn'] for r in have])
        print(f"R4 Spearman(climb, CS) = {spearmanr(Ch,Cs).statistic:+.4f}   "
              f"Spearman(turn, CS) = {spearmanr(Tu,Cs).statistic:+.4f}   (n={len(have)})")
    json.dump(rows, open('.scratch/c6_rows.json','w'))
