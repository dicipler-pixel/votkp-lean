# SCRIPT: TWIN-SHAPES-369-01
# Part 5: the three-fold turn. The 120 deg turn C about the cube diagonal sends x -> y -> z -> x (the arms 1 -> 7 -> 9 -> 1).
# Questions: (a) is the chain law itself C-equivariant (relabel the arms cyclically: the frame is conjugated by C)?
#            (b) does the heading lock sit on the C-axis, and where does its small tilt point?
#            (c) does the frame limit sit in a C-symmetric position (rotation axis along the diagonal)?
#            (d) the 3-6-9 rule proper: twin starts above 3 are 2 mod 3, so mod 9 they are 2, 5, 8 = 2 + {0,3,6}; the shift
#                by 3 mod 9 is fixed-point free and cycles the three classes. Hang the arms on p mod 9 instead of the
#                end digit and read the chain again.
# Kill lines, written before the run:
#  K5a relabelled chain: |turn angle change| > 1e-9 deg or axis not equal to C(axis) to 1e-9 -> code / law not equivariant
#  K5b 'frame limit is 3-fold symmetric' dies if the frame axis is more than 10 deg off the diagonal at 1e9
#  K5c 'the frame axis prefers the diagonal' dies if the real angle is not below the 10th percentile of 200 i.i.d.-arm chains
#  K5d 'the tilt of the heading points along the arm imbalance' dies if the angle between the heading tilt (across the
#      diagonal) and the book-imbalance direction S exceeds 30 deg at 1e8 and 1e9
#  K5e mod-9 arms: slope law must hold (|slope - 1/sqrt3| <= 0.005), else dead; turn and offset reported, no prediction
import numpy as np, math, twinlib as t
T = t.twin_starts(); A = t.arms_digit(T); E = np.eye(3); s3 = math.sqrt(3); us = np.ones(3) / s3
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)   # x -> y -> z -> x
marks = np.array([1e5, 1e6, 1e7, 1e8, 9.99e8])
rec = t.run_chain(T, A, E, marks, 0)
recC = t.run_chain(T, ((A + 1) % 3).astype(np.int64), E, marks, 0)
wa = 0; wx = 0
for x, y in zip(rec, recC):
    a1, ax1 = t.rot_angle_axis(x[6:15].reshape(3, 3)); a2, ax2 = t.rot_angle_axis(y[6:15].reshape(3, 3))
    wa = max(wa, abs(math.degrees(a1 - a2))); wx = max(wx, np.abs(C @ ax1 - ax2).max())
print('K5a relabel x->y->z: worst turn change %.1e deg, worst |C axis - axis\'| %.1e ->' % (wa, wx), 'PASS' if wa < 1e-9 and wx < 1e-9 else 'FAIL')
def inplane(v):
    w = v - (v @ us) * us; return w
e_proj = [inplane(E[k]) / np.linalg.norm(inplane(E[k])) for k in range(3)]
def plane_angle(w):   # angle of an across-diagonal vector, measured from the x-arm's projection, in degrees
    b1 = e_proj[0]; b2 = np.cross(us, b1); return math.degrees(math.atan2(w @ b2, w @ b1)) % 360
r = np.log(T[1:] / T[:-1]); a1 = A[1:]
X = np.zeros((len(r), 3)); X[np.arange(len(r)), a1] = r; X = np.cumsum(X, 0)
print('arm projections sit at 0, 120, 240 deg in the plane across the diagonal (x, y, z)')
print('   a\'        frame turn  axis-to-diagonal  heading tilt  tilt dir  imbalance S dir  |S|     angle(tilt, S)')
for x in rec:
    R = x[6:15].reshape(3, 3); ang, ax = t.rot_angle_axis(R)
    adiag = math.degrees(math.acos(min(1, abs(ax @ us))))
    u = x[27:30]; tilt = math.degrees(math.acos(min(1, u @ us))); w = inplane(u)
    i = np.searchsorted(T[1:], x[0]); S = X[i] - X[i].sum() / 3
    ts = math.degrees(math.acos(max(-1, min(1, (w @ S) / (np.linalg.norm(w) * np.linalg.norm(S))))))
    print('   %-10d %7.3f    %7.3f           %6.3f      %6.1f     %6.1f        %.4f   %6.1f' % (x[0], math.degrees(ang), adiag, tilt, plane_angle(w), plane_angle(S), np.linalg.norm(S), ts))
x = rec[-1]; ang, ax = t.rot_angle_axis(x[6:15].reshape(3, 3)); adiag = math.degrees(math.acos(min(1, abs(ax @ us))))
print('K5b frame axis to diagonal at 1e9 = %.2f deg ->' % adiag, 'survives' if adiag <= 10 else 'KILLED')
rng = np.random.default_rng(9); T8 = T[T <= 10 ** 8]; nul = []
for _ in range(200):
    y = t.run_chain(T8, rng.integers(0, 3, len(T8)).astype(np.int64), E, np.array([9.99e7]), 0)[0]
    a_, ax_ = t.rot_angle_axis(y[6:15].reshape(3, 3)); nul.append(math.degrees(math.acos(min(1, abs(ax_ @ us)))))
nul = np.array(nul); x8 = rec[3]; a8, ax8 = t.rot_angle_axis(x8[6:15].reshape(3, 3)); ad8 = math.degrees(math.acos(min(1, abs(ax8 @ us))))
print('   null (200 i.i.d.-arm chains to 1e8): axis-to-diagonal 10th/50th/90th percentile %.1f / %.1f / %.1f deg; real %.1f deg (rank %d/200)' % (
    *np.percentile(nul, [10, 50, 90]), ad8, (nul < ad8).sum()))
print('   (a uniformly random axis has median 60 deg to a fixed line)')
print('K5c ->', 'survives' if ad8 < np.percentile(nul, 10) else 'KILLED')
# K5d: tilt vs imbalance
bad = []
for x in rec[3:]:
    u = x[27:30]; w = inplane(u); i = np.searchsorted(T[1:], x[0]); S = X[i] - X[i].sum() / 3
    bad.append(math.degrees(math.acos(max(-1, min(1, (w @ S) / (np.linalg.norm(w) * np.linalg.norm(S)))))))
print('K5d tilt-vs-imbalance angles at 1e8, 1e9: %.1f, %.1f deg ->' % tuple(bad), 'survives' if max(bad) <= 30 else 'KILLED')
# (d) mod 9 arms
A9 = ((T % 9) // 3).astype(np.int64)    # 2 -> 0, 5 -> 1, 8 -> 2
print('twin starts mod 9 classes present:', sorted(set((T % 9).tolist())), ' counts', np.bincount(A9))
r9 = t.run_chain(T, A9, E, marks, 0)
for x in r9:
    ang, ax = t.rot_angle_axis(x[6:15].reshape(3, 3)); u = x[27:30]
    print('   mod-9 arms  a\'=%-10d d/L=%.5f  c=%+.5f  frame turn %.3f deg  axis-to-diagonal %.2f deg  heading tilt %.3f deg' % (
        x[0], x[2] / x[1], x[2] - x[1] / s3, math.degrees(ang), math.degrees(math.acos(min(1, abs(ax @ us)))), math.degrees(math.acos(min(1, u @ us)))))
sl = (r9[-1, 2] - r9[0, 2]) / (r9[-1, 1] - r9[0, 1])
print('K5e mod-9 slope 1e5->1e9 %.5f ->' % sl, 'survives' if abs(sl - 1 / s3) <= 0.005 else 'KILLED')
M9 = np.zeros((3, 3)); np.add.at(M9, (A9[:-1], A9[1:]), 1); print('   mod-9 class transitions (2,5,8):\n', M9.astype(int), '\n   repeat rate %.4f' % (np.trace(M9) / M9.sum()))
