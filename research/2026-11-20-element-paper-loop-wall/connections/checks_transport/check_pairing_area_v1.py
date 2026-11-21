# SCRIPT: WTK-LOOPWALL-PAIRING-AREA-01
"""
Connection: WTK Theorem 3's conserved pairing l^T x (x -> A x, l -> A^-T l) for the
determinant-one steps of the loop, and the element paper's screw sign chi = (d0 x d1).d2.

Why this check proves what it claims:
 - For any 2x2 A with det A = 1, A^-T = J A J^-1 with J = [[0,1],[-1,0]] (Cayley-Hamilton
   identity). Sympy must reduce A^-T - J A J^-1 to zero for symbolic entries with
   ad - bc = 1. Then WTK's dual covector can be taken as l = J y with y transported like x,
   and the kept pairing l^T x = y^T J^T x is the oriented area det[x, y].
 - Orientation test: conjugating a step by a mirror M = diag(1, -1) must flip the sign of
   that area for the mirrored vectors, while reversing the order of the two vectors also
   flips it. The screw sign is a 3x3 determinant det[d0, d1, d2]: it flips under a mirror
   but is unchanged when the path is reversed (d_i -> -d_{2-i}), because reversing three
   vectors is an odd permutation times three sign changes (two odd factors). Both facts
   are checked numerically on the selenium-type helix. So WTK's 2D pairing and chi are the
   same KIND of object (an oriented volume, mirror-odd), but they respond differently to
   reversal: STRUCTURAL, not exact.
"""
import sympy as sp, numpy as np, math
a, b, c = sp.symbols('a b c', nonzero=True)
d = (1 + b*c)/a
A = sp.Matrix([[a, b], [c, d]]); Jm = sp.Matrix([[0, 1], [-1, 0]])
print('A^-T - J A J^-1 =', sp.simplify(A.inv().T - Jm*A*Jm.inv()))
rng = np.random.default_rng(3)
h = 0.9; Am = np.array([[math.exp(h), 0], [0, math.exp(-h)]]) @ np.array([[math.cosh(0.4), math.sinh(0.4)], [math.sinh(0.4), math.cosh(0.4)]])
x, y = rng.normal(size=2), rng.normal(size=2)
area = lambda u, v: u[0]*v[1] - u[1]*v[0]
print('area before / after transport:', round(area(x, y), 12), round(area(Am @ x, Am @ y), 12))
M = np.diag([1., -1.])
print('mirror flips area:', round(area(M @ x, M @ y), 12), ' swapping the two vectors flips it:', round(area(y, x), 12))
# helix (screw) path, three bond vectors
R, p, n = 1.0, 1.2, 3
pts = [np.array([R*math.cos(2*math.pi*k/n), R*math.sin(2*math.pi*k/n), p*k/n]) for k in range(4)]
dv = [pts[k+1] - pts[k] for k in range(3)]
chi = lambda d0, d1, d2: float(np.dot(np.cross(d0, d1), d2))
M3 = np.diag([1., 1., -1.])
print('chi forward =', round(chi(*dv), 9), ' reversed path =', round(chi(-dv[2], -dv[1], -dv[0]), 9),
      ' mirrored =', round(chi(*(M3 @ v for v in dv)), 9))
