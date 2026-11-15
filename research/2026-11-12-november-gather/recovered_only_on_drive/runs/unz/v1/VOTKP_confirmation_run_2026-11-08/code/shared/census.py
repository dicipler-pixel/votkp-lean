#!/usr/bin/env python3
"""The theta census past ten crossings.

For every prime knot in a family (11a, 11n, 12a, 12n) we read a braid word from
SnapPy, build the upright long-knot diagram of the braid closure, and evaluate
theta at rational points.

Why a braid word.  A braid on m strands drawn with all strands ascending has
every crossing upright and every braid segment flat, so all the rotation sits in
the m-1 closure arcs: Sum phi = -(m-1).  The closed diagram is a genuine upright
diagram of the knot, which is the hypothesis theta_general needs.  No choice of
phi is left open (that was the dead end of the PD-code route).

Parity is automatic, and is checked anyway.  If the closure of a braid word of
length L on m strands is a knot then its permutation is an m-cycle, whose sign
is (-1)^(m-1); the sign of a word of length L is (-1)^L, so L = m-1 (mod 2), and
the writhe w = L (mod 2).  Hence Sum phi + w = -(m-1) + w is even and the
normalisation exponent (-Sum phi - w)/2 is an integer.

Gates before any invariant is believed:
  * single-cycle permutation (asserted inside braid_drawing.diagram);
  * 2L visits, m-1 closure arcs, Sum phi + w even;
  * Alexander: T^e det A at T=3 equals Delta(3) up to a unit.

Points.  theta = D * theta_0 with D = Delta(T1)Delta(T2)Delta(T1T2), and theta_0
is built from A^{-1}, so a point where det A = 0 is a pole of the formula and is
skipped for that knot (6_1 has Delta(2)=0, for instance).  We walk a pool of
points until either a nonzero value appears -- which proves theta is not
identically zero -- or three distinct points have been evaluated with value 0.
"""
import sys; sys.path.insert(0,'code')
import json, os, time, multiprocessing as mp
from fractions import Fraction as Fr
import braid_drawing as bd, theta_general as tg

POOL  = [(2,3), (2,5), (3,5), (5,7), (7,11), (3,7), (5,3), (4,5), (5,4)]
ALEXPTS = (3, 5, 7)
MIN_ZERO_POINTS = 3

def alex_number(X, n, x=3):
    """det A at T=x (exact)."""
    size = 2*n+1
    A = [[Fr(int(i==j)) for j in range(size)] for i in range(size)]
    for s,i,j in X:
        A[i-1][i] -= Fr(x)**s
        A[i-1][j] -= (1 - Fr(x)**s)
        A[j-1][j] -= 1
    _, d = tg.inverse_and_det(A)
    return d

def seifert_delta_at(nm, x=3):
    import snappy, sympy as sp
    V = sp.Matrix(snappy.Link(snappy_name(nm)).seifert_matrix())
    g = V.rows//2
    M = sp.Matrix(V.rows, V.rows, lambda i,j: V[i,j] - x*V[j,i])
    return Fr(int(sp.det(M)), x**g)

def is_unit_pow2(r):
    r = abs(Fr(r))
    if r == 1: return True
    if r == 0: return False
    n, d = r.numerator, r.denominator
    return (n & (n-1) == 0) and (d & (d-1) == 0)

def snappy_name(nm):
    """KnotInfo writes 11a_5, SnapPy writes 11a5; <=10 crossings agree."""
    m = __import__('re').match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def diagram_of(nm):
    import snappy
    word = list(snappy.Link(snappy_name(nm)).braid_word())
    m = max(abs(x) for x in word) + 1
    X, phi, n, info = bd.diagram(word, m)
    return word, m, X, phi, n, info

def census_one(nm, do_alex=True):
    t0 = time.time()
    rec = {'knot': nm}
    try:
        word, m, X, phi, n, info = diagram_of(nm)
    except Exception as e:
        rec['error'] = f'diagram {type(e).__name__}: {e}'; return rec
    S, w = info['sum_phi'], info['w']
    rec.update({'m': m, 'n': n, 'w': w, 'sum_phi': S, 'arcs': info['arcs'],
                'parity': (S - w) % 2 == 0,
                'visits_ok': info['V'] == 2*len(word) == 2*n})
    if not rec['parity']:
        rec['error'] = 'parity failed'; return rec
    e = Fr(-S - w, 2)
    if do_alex:
        ok = None
        for x in ALEXPTS:
            try:
                ok = is_unit_pow2(Fr(x)**int(e) * alex_number(X, n, x) / seifert_delta_at(nm, x))
            except Exception:
                continue
            break
        rec['alex'] = ok
    vals = []
    for (q1,q2) in POOL:
        try:
            v, _ = tg.theta(X, phi, n, q1, q2, verify=False)
        except ValueError:
            continue                      # det A = 0 at this point: a pole
        vals.append((q1, q2, str(v)))
        if v != 0:
            break
        if len(vals) >= MIN_ZERO_POINTS:
            break
    if not vals:
        rec['error'] = 'all points singular'; return rec
    rec['tested'] = vals
    rec['zero'] = all(Fr(v) == 0 for _,_,v in vals) and len(vals) >= MIN_ZERO_POINTS
    rec['secs'] = round(time.time()-t0, 2)
    return rec

def worker(nm):
    return census_one(nm)

def run(names, out, procs=4):
    done = set()
    if os.path.exists(out):
        for line in open(out):
            line = line.strip()
            if line:
                try: done.add(json.loads(line)['knot'])
                except Exception: pass
    todo = [n for n in names if n not in done]
    print(f'{len(names)} knots, {len(done)} done, {len(todo)} to go', flush=True)
    t0 = time.time()
    with mp.Pool(procs) as pool, open(out, 'a') as fh:
        for k, rec in enumerate(pool.imap_unordered(worker, todo, chunksize=2), 1):
            fh.write(json.dumps(rec) + '\n'); fh.flush()
            if k % 50 == 0 or k == len(todo):
                el = time.time()-t0
                print(f'  {k}/{len(todo)}  {el:6.0f}s  eta {el/k*(len(todo)-k):6.0f}s', flush=True)

if __name__ == '__main__':
    import knotnames
    fam = sys.argv[1]; out = sys.argv[2]
    names = knotnames.names_in(fam) if fam != 'upto10' else knotnames.names_upto(10)
    run(names, out)
