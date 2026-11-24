# SCRIPT: TWIN-SHAPES-369-CHIRALITY-01
# Part 5b: the arm walk is a walk on the three-fold turn group. Consecutive twin starts step their end digit
# forward (1->7->9->1, = x->y->z->x, the 120 deg turn C), backward (C^-1), or repeat. In the mod-9 reading the step is
# exactly the shift by gap mod 9 in {0,3,6}. A forward pair x then y turns the frame about e_x x e_y = e_z; the three forward
# pairs turn about z, x, y, which add along the diagonal (1,1,1). So an excess of forward over backward steps predicts a
# frame-turn component ALONG the diagonal with a fixed sign; repeats and the in-plane parts do not.
# Kill lines, written before the run:
#  K5f the sign of the ball frame's diagonal turn component must equal the sign predicted from the forward excess
#      (sign of the pair turn x-then-y read off the polar split, times sign of forward - backward). Mismatch -> dead.
#  K5g in 200 i.i.d.-arm chains (no chirality) the diagonal component must average to zero within 2 standard errors;
#      if not, the diagonal component is not a chirality effect -> dead.
#  K5h the chirality sum Q = 1/2 sum r_n r_{n+1} (e_n x e_{n+1}).diag (consecutive pairs only, flat formula) must give
#      the diagonal component to within 30% for the real chain at 1e9, else the 'local pairs carry it' reading dies.
import numpy as np, math, twinlib as t
T = t.twin_starts(); A = t.arms_digit(T); E = np.eye(3); s3 = math.sqrt(3); us = np.ones(3) / s3
r = np.log(T[1:] / T[:-1]); a1 = A[1:]
fwd = ((a1[1:] - a1[:-1]) % 3 == 1); bwd = ((a1[1:] - a1[:-1]) % 3 == 2); rep = a1[1:] == a1[:-1]
print('steps of the arm walk on the 3-fold group: forward %.4f  backward %.4f  repeat %.4f' % (fwd.mean(), bwd.mean(), rep.mean()))
w = r[1:] * r[:-1]
print('r r\'-weighted: forward %.4f backward %.4f repeat %.4f' % ((w * fwd).sum() / w.sum(), (w * bwd).sum() / w.sum(), (w * rep).sum() / w.sum()))
_, _, Rxy = t.polar(t.boost4(E[0], 0.1) @ t.boost4(E[1], 0.1)); axy, axxy = t.rot_angle_axis(Rxy)
sgn_pair = np.sign(axxy @ E[2]); print('pair turn x-then-y: axis . e_z = %+.3f (rotation vector = %+d x angle x e_z)' % (axxy @ E[2], sgn_pair))
def rotvec(x):
    ang, ax = t.rot_angle_axis(x[6:15].reshape(3, 3)); return ang * ax
cr = np.cross(E[a1[:-1]], E[a1[1:]]) @ us
def Qsum(upto):
    m = T[2:] <= upto; return 0.5 * (r[1:][m] * r[:-1][m] * cr[m]).sum()
marks = np.array([1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 9.99e8])
rec = t.run_chain(T, A, E, marks, 0)
print('   a\'          frame turn  diagonal part (rad)  in-plane part (rad)   Q (consecutive pairs, sign-adjusted)')
for x in rec:
    v = rotvec(x); dg = v @ us; ip = np.linalg.norm(v - dg * us); Q = sgn_pair * Qsum(x[0])
    print('   %-10d  %7.3f deg   %+.5f              %.5f               %+.5f' % (x[0], math.degrees(np.linalg.norm(v)), dg, ip, Q))
v = rotvec(rec[-1]); dg = v @ us
pred_sign = sgn_pair * np.sign(fwd.sum() - bwd.sum())
print('K5f predicted sign %+d, ball diagonal component %+.5f ->' % (pred_sign, dg), 'survives' if np.sign(dg) == pred_sign else 'KILLED')
rng = np.random.default_rng(13); T8 = T[T <= 10 ** 8]; dd = []
for _ in range(200):
    y = t.run_chain(T8, rng.integers(0, 3, len(T8)).astype(np.int64), E, np.array([9.99e7]), 0)[0]; dd.append(rotvec(y) @ us)
dd = np.array(dd); se = dd.std() / math.sqrt(len(dd))
print('K5g i.i.d. arms: mean diagonal component %+.5f (s.e. %.5f, sd %.5f); real at 1e8 %+.5f ->' % (dd.mean(), se, dd.std(), rotvec(rec[5]) @ us),
      'survives' if abs(dd.mean()) <= 2 * se else 'KILLED')
print('   real chain rank among i.i.d. by diagonal component: %d/200' % (dd < rotvec(rec[5]) @ us).sum())
Q = sgn_pair * Qsum(9.99e8)
print('K5h Q = %+.5f vs diagonal component %+.5f, ratio %.3f ->' % (Q, dg, dg / Q), 'survives' if abs(dg / Q - 1) <= 0.3 else 'KILLED')
# mod-9 reading: step = gap mod 9
A9 = ((T % 9) // 3).astype(np.int64); g = (T[1:] - T[:-1]) % 9
print('mod-9 reading: the class step equals gap mod 9 / 3:', bool(np.all(((A9[1:] - A9[:-1]) % 3) == g // 3)), ' gap mod 9 shares {0,3,6}:', [round(float((g == k).mean()), 4) for k in (0, 3, 6)])
r9 = t.run_chain(T, A9, E, np.array([9.99e8]), 0)[0]; v9 = rotvec(r9)
f9 = ((A9[2:] - A9[1:-1]) % 3 == 1).sum(); b9 = ((A9[2:] - A9[1:-1]) % 3 == 2).sum()
print('   mod-9 arms: forward-backward excess %+d steps; frame diagonal component %+.5f, in-plane %.5f; predicted sign %+d' % (
    f9 - b9, v9 @ us, np.linalg.norm(v9 - (v9 @ us) * us), sgn_pair * np.sign(f9 - b9)))
