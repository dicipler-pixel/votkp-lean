# SCRIPT: TWIN-SHAPES-DIAGONAL-01
# Part 1: the cube diagonal. Why the slope is 1/sqrt3, and where the offset c = d - L/sqrt3 comes from.
# Kill lines, written before the run:
#  K1a (exact bookkeeping) the three-term split  curvature gain + arm noise + heading lag  must reproduce d - L/sqrt3
#      to 1e-9 at every mark, or the decomposition is wrong.
#  K1b (prediction P1, random-arm model) c_pred = mean c over 200 chains with the TRUE step sizes r_n and arms drawn
#      uniformly at random. Killed if |c_pred - c_measured| > 0.01.
#  K1c (prediction P2, exact start + transient theory) run the real chain to a0 (1e3 and 1e4), then predict the rest
#      with no arm information: averaged heading flow + curvature gain + heading-lag cost of the noise (equations in
#      REPORT.md, Part 1). Killed if the predicted change c(1e9) - c(a0) misses the measured change by more than 0.01.
import numpy as np, math, twinlib as t
T = t.twin_starts(); A = t.arms_digit(T); E = np.eye(3); s3 = math.sqrt(3)
marks = np.array([30, 100, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 9.99e8])
rec = t.run_chain(T, A, E, marks, 0)
print('Measured on the real chain (arms by end digit 1,7,9 -> x,y,z):')
print('   a\'          L         d        c=d-L/sqrt3   start     curv.gain  arm-noise  heading-lag   split-check')
for x in rec:
    c = x[2] - x[1] / s3; sp = x[15] + x[16] + x[17] + x[22]
    print('   %-10d %8.4f %9.5f %+.5f    %+.5f  %+.5f   %+.5f   %+.5f      %.1e' % (x[0], x[1], x[2], c, x[22], x[15], x[16], x[17], abs(c - sp)))
cm = rec[-1, 2] - rec[-1, 1] / s3
print('K1a worst split error %.1e -> %s' % (max(abs(x[2] - x[1] / s3 - x[15] - x[16] - x[17] - x[22]) for x in rec),
      'PASS' if max(abs(x[2] - x[1] / s3 - x[15] - x[16] - x[17] - x[22]) for x in rec) < 1e-9 else 'FAIL'))

# P1: random arms, true step sizes
rng = np.random.default_rng(11); cs = []
T8 = T[T <= 10 ** 8]; m8 = np.array([9.99e7])
for _ in range(200):
    Ar = rng.integers(0, 3, len(T8)).astype(np.int64)
    x = t.run_chain(T8, Ar, E, m8, 0)[0]; cs.append(x[2] - x[1] / s3)
cs = np.array(cs)
c8 = [x for x in rec if x[0] >= 1e8][0]; c8 = c8[2] - c8[1] / s3
print('P1 random-arm model to 1e8: mean c = %.4f, sd %.4f, 2.5-97.5%% [%.4f, %.4f]; real c(1e8) = %.4f' % (
    cs.mean(), cs.std(), *np.percentile(cs, [2.5, 97.5]), c8))
print('   rank of real c among the 200: %d/200' % (cs < c8).sum())
print('K1b |c_pred - c_meas| = %.4f -> %s' % (abs(cs.mean() - c8), 'survives' if abs(cs.mean() - c8) <= 0.01 else 'KILLED'))

# P2: exact start to a0, then the transient theory with averaged arms
P = np.ones(3) / 3; Pn = 1 / s3
def tail_model(a0):
    i0 = np.searchsorted(T, a0)
    x = t.run_chain(T[:i0 + 1], A[:i0 + 1], E, np.array([float(T[i0])]), 0)[0]
    d = x[2]; n = x[3:6]; R = x[6:15].reshape(3, 3); u = R.T @ n; L = x[1]
    c0 = d - L / s3; V = 0.0
    r = np.log(T[i0 + 1:] / T[i0:-1])
    for rr in r:
        th = math.tanh(d / 2)
        uP = u @ P
        sin2 = 1 - (u @ u) / 3                      # mean over arms of 1 - (u.e_s)^2, |u| = 1
        d += rr * uP + rr * rr * (0.5 * sin2 / math.tanh(d)) - Pn * rr * V / 2
        u = u + rr * th * (P - uP * u); u /= np.linalg.norm(u)
        V = V * (1 - 2 * rr * th * Pn) + rr * rr * th * th * (2 / 3)
        L += rr
    return c0, d - L / s3
for a0 in (1e3, 1e4):
    c0, cp = tail_model(a0)
    meas_change = cm - c0; pred_change = cp - c0
    print('P2 exact to %.0e (c there %.4f): predicted change to 1e9 %+.4f, measured change %+.4f, predicted c %.4f vs %.4f' % (
        a0, c0, pred_change, meas_change, cp, cm))
    print('K1c miss %.4f -> %s' % (abs(pred_change - meas_change), 'survives' if abs(pred_change - meas_change) <= 0.01 else 'KILLED'))
