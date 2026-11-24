# SCRIPT: TWIN-SHAPES-FLAT-READER-01
# Part 4: the twin chain in flat readers (commuting moves: no wall, no turn), and what the ball adds.
# In any flat reader the moves commute, so the chain's point is the book vector X = (L_x, L_y, L_z) (sum of r over each
# arm) and the reading is a norm N(X). Three flat readers:
#   per-edge sum ('lengths add', the diamond's per-edge reading): N1 = L_x + L_y + L_z = L exactly (all r > 0)
#   flat Euclidean (the ball's own small-scale geometry, no curvature): NE = |X|
#   tetrahedron (Hilbert reading of the simplex, arms on three face books, book s scaled by e^{2r} so one step reads r):
#       NT = 1/2 (max - min) of (2L_x, 2L_y, 2L_z, 0) = max(L_x, L_y, L_z)
# Derived: d/L -> N(P), P = (1/3,1/3,1/3): 1, 1/sqrt3, 1/3. So 1/sqrt3 is the Euclidean norm of the mean arm (a flat
# fact); curvature does not make it.
# Curvature test by scaling: a space of curvature -K reads the same chain as the unit ball reads the chain with every
# step multiplied by lam = sqrt(K) (distances divided by lam). So c_K = c(lam)/lam, frame turn psi_K = psi(lam).
# Gauss-Bonnet prediction for small K: the frame turn is curvature x the flat vector area of the chain's loop (closed by
# the straight chord):  psi -> K |Avec|,  Avec = 1/2 sum X_{n-1} x (r_n e_{s_n}).
# Kill lines, written before the run:
#  K4a per-edge reader: |N1 - L| > 1e-9 at any mark -> 'lengths add' reading wrong
#  K4b flat Euclidean slope NE/L at 1e9 off 1/sqrt3 by more than 0.002 -> '1/sqrt3 is flat' dead
#  K4c psi(lam)/(lam^2 |A|) at the smallest lam (1/16) off 1 by more than 5% -> 'turn = curvature x flat area' dead
#  K4d c_K at the smallest lam off the flat Euclidean offset by more than 0.01 -> 'c is the curvature excess over flat' dead
import numpy as np, math, twinlib as t
T = t.twin_starts(); A = t.arms_digit(T); s3 = math.sqrt(3); E = np.eye(3)
r = np.log(T[1:] / T[:-1]); a1 = A[1:]
X = np.zeros((len(r), 3)); X[np.arange(len(r)), a1] = r; X = np.cumsum(X, 0)
Lp = np.cumsum(r)
Xprev = np.vstack([np.zeros(3), X[:-1]]); step = np.zeros((len(r), 3)); step[np.arange(len(r)), a1] = r
Acum = 0.5 * np.cumsum(np.cross(Xprev, step), 0)
marks = [1e4, 1e5, 1e6, 1e7, 1e8, 9.99e8]
idx = [np.searchsorted(T[1:], m) for m in marks]
print('flat readers of the twin chain (the ball for comparison):')
print('   a\'          L        N1-L      NE        NE/L     cE=NE-L/sqrt3   NT=max book  NT/L   cT=NT-L/3   |Avec|')
rec = t.run_chain(T, A, E, np.array(marks), 0)
w1 = 0
for i, x in zip(idx, rec):
    N1 = X[i].sum(); NE = np.linalg.norm(X[i]); NT = X[i].max(); w1 = max(w1, abs(N1 - Lp[i]))
    print('   %-10d %8.4f  %+.1e  %8.5f  %.5f   %+.5f        %8.5f   %.5f  %+.5f   %.5f' % (T[i + 1], Lp[i], N1 - Lp[i], NE, NE / Lp[i], NE - Lp[i] / s3, NT, NT / Lp[i], NT - Lp[i] / 3, np.linalg.norm(Acum[i])))
print('   ball at the same marks: c = d - L/sqrt3 =', ' '.join('%+.5f' % (x[2] - x[1] / s3) for x in rec))
print('K4a worst |N1 - L| = %.1e ->' % w1, 'PASS' if w1 < 1e-9 else 'FAIL')
i = idx[-1]; sl = np.linalg.norm(X[i]) / Lp[i]
print('K4b flat Euclidean slope at 1e9 %.5f vs %.5f ->' % (sl, 1 / s3), 'survives' if abs(sl - 1 / s3) <= 0.002 else 'KILLED')
# imbalance vector: X - (L/3)(1,1,1) lies across the diagonal; cE = |S|^2/(NE + L/sqrt3)
S = X[i] - Lp[i] / 3; print('   book imbalance S = X - (L/3)(1,1,1) at 1e9 = (%+.4f, %+.4f, %+.4f), sum %.1e (lies in the plane across the diagonal)' % (*S, S.sum()))
# curvature scaling
T8 = T[T <= 10 ** 8]; A8 = A[:len(T8)]; i8 = len(T8) - 2
cE8 = np.linalg.norm(X[i8]) - Lp[i8] / s3; Aabs = np.linalg.norm(Acum[i8]); Adir = Acum[i8] / Aabs
print('curvature scaling to 1e8 (flat: cE = %+.5f, |Avec| = %.5f, Avec direction (%.3f, %.3f, %.3f)):' % (cE8, Aabs, *Adir))
print('   lam=sqrt(K)  frame turn psi(deg)  psi/(lam^2 |A|)  axis . Adir   c_K = c(lam)/lam   c_K - cE')
out = []
for lam in (2, 1, 0.5, 0.25, 0.125, 0.0625):
    # scale every step: replace T by a sequence with log-ratios lam*r (exact: T'_n = 11 * exp(lam * L_n))
    Ts = 11.0 * np.exp(lam * np.concatenate([[0], np.cumsum(np.log(T8[1:] / T8[:-1]))]))
    x = t.run_chain(Ts, A8, E, np.array([Ts[-1]]), 0)[0]
    R = x[6:15].reshape(3, 3); ang, ax = t.rot_angle_axis(R)
    cK = (x[2] - x[1] / s3) / lam
    out.append((lam, ang, cK))
    print('   %-10.4f   %10.4f          %.4f          %+.4f       %+.5f          %+.5f' % (lam, math.degrees(ang), ang / (lam * lam * Aabs), ax @ Adir, cK, cK - cE8))
lam, ang, cK = out[-1]
q = ang / (lam * lam * Aabs)
print('K4c smallest-lam ratio %.4f ->' % q, 'survives' if abs(q - 1) <= 0.05 else 'KILLED')
print('K4d smallest-lam c_K - cE = %+.4f ->' % (cK - cE8), 'survives' if abs(cK - cE8) <= 0.01 else 'KILLED')
