# SCRIPT: TWIN-SHAPES-PLATONIC-ARMS-01
# Part 2: hang the three arms (end digit 1,7,9) on other Platonic directions and read the chain again.
# Every triple used is symmetric: three unit arms with one common pairwise angle gamma, so
#     e_s = a u* + b w_s,  w_s 120 deg apart in the plane across u*,  a^2 = (1 + 2 cos gamma)/3 = |P|^2 .
# Derived predictions, written before the run:
#   slope        d/L -> |P| = sqrt((1 + 2 cos gamma)/3)
#   pair turn    tan(eps/2) = G1 G2 sin(gamma) / (1 + G1 G2 cos(gamma)),  G = tanh(r/2) = (z-1)/(z+1)
#   step turn    |omega|/r = tanh(d/2) sin(theta), and at the lock cos(theta) = |P|, so -> sqrt(1 - |P|^2)
#   pair wall    tr[A,B] = 2 - 4 sinh^2(r1/2) sinh^2(r2/2) sin^2(gamma); equal steps reach -2 at G^2 = 1/(1 + sin gamma)
# Kill lines:
#   K2a pair-turn formula off the 4x4 polar split by more than 1e-10 on any triple            -> formula dead
#   K2b wall trace formula off the 2x2 matrix commutator by more than 1e-10                    -> formula dead
#   K2c measured slope (d(1e9)-d(1e5))/(L(1e9)-L(1e5)) off |P| by more than 0.005              -> slope law dead for that shape
#   K2d measured mean |omega|/r after 1e8 off sqrt(1-|P|^2) by more than 2%                    -> step-turn law dead for that shape
#   K2e |P| = 0 loop: d grows by more than 0.3 between 1e5 and 1e9                                -> 'no drift, bounded' dead
import numpy as np, math, twinlib as t
s3 = math.sqrt(3); us = np.ones(3) / s3
w1 = np.array([2, -1, -1]) / math.sqrt(6)            # projection of x across the diagonal
w2 = np.cross(us, w1)
def triple(cg):
    a = math.sqrt(max((1 + 2 * cg) / 3, 0)); b = math.sqrt(1 - a * a)
    return np.array([a * us + b * (math.cos(2 * math.pi * k / 3) * w1 + math.sin(2 * math.pi * k / 3) * w2) for k in range(3)])
phi = (1 + 5 ** .5) / 2
SHAPES = [
    ('cube axes = octahedron face vertices', 0.0),
    ('tetrahedron: three face normals', -1 / 3),
    ('icosahedron: vertices of one face (= dodecahedron: normals of 3 faces at a vertex)', 1 / 5 ** .5),
    ('dodecahedron: three vertices next to a vertex', 5 ** .5 / 3),
    ('icosahedron: edges of one face, head to tail (closed loop)', -0.5),
]
E0 = triple(0.0); print('cube triple reproduces the axes:', np.allclose(np.sort(E0.ravel()), np.sort(np.eye(3).ravel())))
# --- K2a: pair turn vs polar split
def pairturn(e1, e2, r1, r2):
    _, _, R = t.polar(t.boost4(e1, r1) @ t.boost4(e2, r2)); return t.rot_angle_axis(R)[0]
worst = 0
for _, cg in SHAPES:
    E = triple(cg); g = math.acos(max(-1, min(1, E[0] @ E[1])))
    for r1, r2 in [(0.4353, 0.5341), (0.1, 0.3), (1.2, 2.0), (1e-3, 2e-3)]:
        G = math.tanh(r1 / 2) * math.tanh(r2 / 2)
        pred = 2 * math.atan2(G * math.sin(g), 1 + G * math.cos(g)); worst = max(worst, abs(pred - pairturn(E[0], E[1], r1, r2)))
print('K2a worst |pair turn formula - polar split| = %.1e ->' % worst, 'PASS' if worst < 1e-10 else 'FAIL')
# --- K2b: wall trace
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
def sl2(e, r): return math.cosh(r / 2) * np.eye(2) + math.sinh(r / 2) * (e[0] * sx + e[1] * sy + e[2] * sz)
worst = 0
for _, cg in SHAPES:
    E = triple(cg); g = math.acos(max(-1, min(1, E[0] @ E[1])))
    for r1, r2 in [(0.3, 0.7), (1.76, 1.76), (2.5, 0.2)]:
        A_, B_ = sl2(E[0], r1), sl2(E[1], r2)
        tr = np.trace(A_ @ B_ @ np.linalg.inv(A_) @ np.linalg.inv(B_)).real
        worst = max(worst, abs(tr - (2 - 4 * math.sinh(r1 / 2) ** 2 * math.sinh(r2 / 2) ** 2 * math.sin(g) ** 2)))
print('K2b worst |trace formula - matrix| = %.1e ->' % worst, 'PASS' if worst < 1e-10 else 'FAIL')
T = t.twin_starts(); A = t.arms_digit(T)
marks = np.array([1e5, 1e7, 1e8, 9.99e8])
r1, r2 = math.log(17 / 11), math.log(29 / 17)
print()
for name, cg in SHAPES:
    E = triple(cg); g = math.degrees(math.acos(max(-1, min(1, E[0] @ E[1])))); Pn = math.sqrt(max((1 + 2 * cg) / 3, 0))
    G2w = 1 / (1 + math.sin(math.radians(g))); zw = (1 + math.sqrt(G2w)) / (1 - math.sqrt(G2w))
    G = math.tanh(r1 / 2) * math.tanh(r2 / 2); eps1 = 2 * math.degrees(math.atan2(G * math.sin(math.radians(g)), 1 + G * math.cos(math.radians(g))))
    rec = t.run_chain(T, A, E, marks, 1e8)
    print('== %s ==' % name)
    print('   angle between arms %.3f deg; predicted |P| = %.5f; predicted late |omega|/r = %.4f' % (g, Pn, math.sqrt(1 - Pn * Pn)))
    print('   first change (11->17 then 17->29) pair turn %.3f deg; small steps: eps ~ r1 r2 sin(gamma)/2' % eps1)
    print('   pair wall at G^2 = %.4f (z = %.3f)' % (G2w, zw))
    for x in rec:
        R = x[6:15].reshape(3, 3); ang, ax = t.rot_angle_axis(R); u = R.T @ x[3:6]
        lock = math.degrees(math.acos(max(-1, min(1, u @ us)))) if Pn > 0 else float('nan')
        print('   a\'=%.2e  L=%.4f  d=%.5f  d/L=%.5f  c=d-|P|L=%+.5f  net frame turn %.3f deg  body heading to u*: %.3f deg' % (
            x[0], x[1], x[2], x[2] / x[1], x[2] - Pn * x[1], math.degrees(ang), lock))
    sl = (rec[-1, 2] - rec[0, 2]) / (rec[-1, 1] - rec[0, 1])
    if Pn > 0:
        print('   K2c slope 1e5->1e9 = %.5f vs %.5f, miss %.1e ->' % (sl, Pn, abs(sl - Pn)), 'survives' if abs(sl - Pn) <= 0.005 else 'KILLED')
        om = rec[-1, 19]; ompath = rec[-1, 20]
        print('   K2d mean |omega|/r after 1e8 = %.4f; C1 law along the path %.4f; lock value %.4f; miss vs lock %.2f%% ->' % (
            om, ompath, math.sqrt(1 - Pn * Pn), 100 * abs(om / math.sqrt(1 - Pn * Pn) - 1)), 'survives' if abs(om / math.sqrt(1 - Pn * Pn) - 1) <= 0.02 else 'KILLED')
    else:
        print('   K2e d grew by %.4f between 1e5 and 1e9 ->' % (rec[-1, 2] - rec[0, 2]), 'survives' if rec[-1, 2] - rec[0, 2] <= 0.3 else 'KILLED')
        print('   mean |omega|/r after 1e8 = %.4f (no lock: heading free, C1 law along the path %.4f)' % (rec[-1, 19], rec[-1, 20]))
