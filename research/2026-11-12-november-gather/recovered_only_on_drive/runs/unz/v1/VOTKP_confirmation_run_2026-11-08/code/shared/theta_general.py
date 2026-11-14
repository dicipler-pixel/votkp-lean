#!/usr/bin/env python3
"""
theta_general.py -- theta on an ARBITRARY upright long-knot diagram, and on
connected sums built from diagram data.

Implements Bar-Natan & van der Veen, arXiv:2509.18456v4, Eqs. (2)-(6):

  A = I - sum_c ( T^s E_{i,i+1} + (1-T^s) E_{i,j+1} + E_{j,j+1} )
  Delta = T^((-phi(D)-w(D))/2) det(A),   w(D)=sum s_c,  phi(D)=sum_k phi_k
  G = A^{-1}
  theta_0 = sum_c F_1(c) + sum_{c0,c1} F_2(c0,c1) + sum_k F_3(k)
  theta   = Delta_1 Delta_2 Delta_3 theta_0,   T_3 = T_1 T_2,  Delta_nu = Delta|_{T->T_nu}

The diagram enters ONLY through  X = {(s,i,j)}  and  phi = {k: phi_k}.
F_1, F_2, F_3 are transcribed verbatim from the authors' published formulas;
they are the ones the handoff's 05_run_tests_amended.py already calibrated
against the authors' table at eight points.

NEW here:
  * theta() takes (X, phi, n) as arguments instead of hard-coding the
    two-strand braid family;
  * connect_sum() composes two upright LONG-knot diagrams.  As long knots,
    stacking K1 above K2 and joining end-to-end IS the connected sum, so the
    composite is a genuine diagram, not a formula.  Edge labels: K1 keeps
    1..2n1+1; K2's edge e becomes 2n1+e.  So K1's closing edge 2n1+1 and K2's
    opening edge 1 merge, K2's closing edge becomes the composite's, and the
    rotation numbers add on the merged edge.
"""
from fractions import Fraction as F
from collections import Counter
import json, sys

# ---------------------------------------------------------------- linear algebra
def inverse_and_det(a):
    n = len(a)
    a = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    det = F(1)
    for col in range(n):
        row = next((r for r in range(col, n) if a[r][col]), None)
        if row is None:
            raise ValueError('singular matrix')
        if row != col:
            a[col], a[row] = a[row], a[col]
            det = -det
        p = a[col][col]
        det *= p
        a[col] = [v / p for v in a[col]]
        for r in range(n):
            if r != col and a[r][col]:
                c = a[r][col]
                a[r] = [x - c * y for x, y in zip(a[r], a[col])]
    return [row[n:] for row in a], det

# ---------------------------------------------------------------- the invariant
def theta(xs, phi, n, T1, T2, verify=True):
    """theta of an upright long-knot diagram.  xs = [(s,i,j)], phi = {edge: rot}."""
    t1, t2 = F(T1), F(T2)
    t3 = t1 * t2
    size = 2 * n + 1
    w = sum(s for s, _, _ in xs)
    exponent = F(-sum(phi.values()) - w, 2)
    if exponent.denominator != 1:
        raise ValueError('nonintegral normalisation exponent %s' % exponent)
    G, deltas = [], []
    for q in (t1, t2, t3):
        A = [[F(i == j) for j in range(size)] for i in range(size)]
        for s, i, j in xs:
            i -= 1
            j -= 1
            A[i][i + 1] -= q ** s
            A[i][j + 1] -= (1 - q ** s)
            A[j][j + 1] -= 1
        inv, det = inverse_and_det(A)
        if verify:
            for i in range(size):
                for j in range(size):
                    assert sum(A[i][k] * inv[k][j] for k in range(size)) == int(i == j)
        G.append(inv)
        deltas.append(q ** int(exponent) * det)

    def g(nu, i, j):
        return G[nu - 1][i - 1][j - 1]

    f1 = F(0); f2 = F(0); f3 = F(0)
    for s, i, j in xs:
        q2s = t2 ** s; q3s = t3 ** s; q1s = t1 ** s
        f1 += s * (F(1, 2) - g(3, i, i) + q2s * g(1, i, i) * g(2, j, i) - q2s * g(3, j, j) * g(2, j, i)
                   - (q2s - 1) * g(3, i, i) * g(2, j, i) + (q3s - 1) * g(2, j, i) * g(3, j, i)
                   - g(1, i, i) * g(2, j, j) + 2 * g(3, i, i) * g(2, j, j)
                   + g(1, i, i) * g(3, j, j) - g(2, i, i) * g(3, j, j))
        f1 += F(s, 1) / (q2s - 1) * ((q1s - 1) * q2s * (g(3, j, j) * g(1, j, i) - g(2, j, j) * g(1, j, i)
                                                        + q2s * g(1, j, i) * g(2, j, i))
                                      + (q3s - 1) * g(3, j, i) * (1 - q2s * g(1, i, i) + g(2, i, j)
                                                                  + (q2s - 2) * g(2, j, j)
                                                                  - (q1s - 1) * (q2s + 1) * g(1, j, i)))
    for s0, i0, j0 in xs:
        for s1, i1, j1 in xs:
            f2 += F(s1, 1) * (t1 ** s0 - 1) * (t3 ** s1 - 1) * g(1, j1, i0) * g(3, j0, i1) / (t2 ** s1 - 1) \
                  * (t2 ** s0 * g(2, i1, i0) + g(2, j1, j0) - t2 ** s0 * g(2, j1, i0) - g(2, i1, j0))
    for k, v in phi.items():
        f3 += (g(3, k, k) - F(1, 2)) * v
    return deltas[0] * deltas[1] * deltas[2] * (f1 + f2 + f3), tuple(deltas)

# ---------------------------------------------------------------- diagrams
def braid(n, mirror=False):
    """The handoff's family: long closure of the positive two-strand n-braid."""
    xs = []
    for k in range(1, n + 1):
        i, j = (k, n + k) if k % 2 else (n + k, k)
        s = 1
        if mirror:
            i, j, s = j, i, -1
        xs.append((s, i, j))
    return xs, {n + 1: -1}, n          # rotation on edge n+1, total -1

def mirror_data(xs, phi, n):
    """Mirror: switch all over/under on the same planar immersion; edge
    rotations are unchanged (the handoff's amendment)."""
    return [( -s, j, i) for (s, i, j) in xs], dict(phi), n

def connect_sum(d1, d2):
    """K1 # K2 as long knots, stacked.  K2's labels shift by 2*n1."""
    (x1, p1, n1), (x2, p2, n2) = d1, d2
    off = 2 * n1
    xs = list(x1) + [(s, i + off, j + off) for (s, i, j) in x2]
    phi = Counter()
    for k, v in p1.items():
        phi[k] += v                                  # K1 keeps 1..2n1+1
    for k, v in p2.items():
        phi[k + off] += v                            # K2 edge 1 -> 2n1+1 (merges)
    return xs, dict(phi), n1 + n2

def iterated_sum(d, times):
    out = d
    for _ in range(times - 1):
        out = connect_sum(out, d)
    return out

# ---------------------------------------------------------------- facts we test against
def alex_2n1(t):
    """Delta of T(2,m) as a Laurent dict, m odd."""
    m = t
    return {j - (m - 1) // 2: (-1 if j % 2 else 1) for j in range(m)}

def delta_eval(lam, x):
    x = F(x)
    return sum(c * x ** k for k, c in lam.items() if c)

def D_of(lam, T1, T2):
    """D = Delta(T1) Delta(T2) Delta(T1 T2)."""
    return delta_eval(lam, T1) * delta_eval(lam, T2) * delta_eval(lam, T1 * T2)
