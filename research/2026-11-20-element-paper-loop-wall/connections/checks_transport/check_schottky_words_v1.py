# SCRIPT: WTK-LOOPWALL-SCHOTTKY-WORDS-01
"""
Connection (backwards, through the Two Trees paper): above Gamma^2 = 1/2 the two
perpendicular steps generate a Schottky group. In WTK's language that should mean every
cumulative transport built from the two steps is strictly dominated, so WTK Theorem 2
selects a line for every word; below the wall some words turn (no selected line).

Why this check proves what it claims (finite evidence, not a proof):
 - A word's powers have a WTK-selected line iff the word is hyperbolic, |tr| > 2 (strict
   modal dominance, WTK Theorem 2); |tr| < 2 is a turn (WTK's rotating-line control).
 - We enumerate EVERY reduced word up to length 10 in A, B, A^-1, B^-1 (equal faces,
   half-step h = (1/2) ln z) and count elliptic words. If the count is zero outside the
   wall (carbon's helium-core opening ratio on both faces) and positive inside it
   (nitrogen's), and the smallest margin |tr| - 2 outside is the commutator's, the
   wall is the selection threshold for the whole two-step transport, not just the loop.
   Finite length means this is evidence; the Schottky ping-pong argument (circles of
   radius 1/sinh h disjoint iff sinh h >= 1) is what proves it for all lengths.
"""
import numpy as np, math, itertools
def gens(z):
    h = 0.5*math.log(z)
    A = np.array([[math.exp(h), 0], [0, math.exp(-h)]]); B = np.array([[math.cosh(h), math.sinh(h)], [math.sinh(h), math.cosh(h)]])
    return {'A': A, 'a': np.linalg.inv(A), 'B': B, 'b': np.linalg.inv(B)}
inv = {'A': 'a', 'a': 'A', 'B': 'b', 'b': 'B'}
def words(L):
    out = [[]]
    frontier = [[]]
    for _ in range(L):
        new = []
        for w in frontier:
            for g in 'AaBb':
                if w and inv[w[-1]] == g: continue
                new.append(w + [g])
        out += new; frontier = new
    return [w for w in out if w]
W = words(10)
print('reduced words up to length 10:', len(W))
for name, z in [('nitrogen K opening (inside)', 552.06741/97.8901), ('the wall 3+2sqrt2', 3+2*math.sqrt(2)),
                ('carbon K opening (outside)', 392.09056/64.49352)]:
    G = gens(z); ell = 0; minmarg = 1e9; argmin = None
    for w in W:
        M = np.eye(2)
        for g in w: M = M @ G[g]
        t = abs(np.trace(M))
        if t < 2 - 1e-9: ell += 1
        elif t - 2 < minmarg: minmarg, argmin = t - 2, ''.join(w)
    print(f'  {name:30s} elliptic words: {ell:6d}   smallest |tr|-2 among the rest: {minmarg:.3e} at {argmin}')
