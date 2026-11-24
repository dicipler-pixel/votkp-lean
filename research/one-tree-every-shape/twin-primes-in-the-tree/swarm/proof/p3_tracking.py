# SCRIPT: TWIN-PROOF-TRACKING-01
# Claim under test (REPORT.md Step 3'): the body heading u does not sit on the cube diagonal; it tracks the LOCAL
# gap-weighted arm mean P(L) (shares of path in the last unit of path), and this is why the theorem only needs P(L)
# to have bounded variation, not to equal (1/3,1/3,1/3).
# Kill, written before the run: at 1e7, 1e8, 1e9 compare the off-diagonal part of u with the off-diagonal part of
# P_loc/|P_loc| (P_loc from the window of path (L-1, L]). If at any mark cos(angle between the two off-diagonal
# vectors) < 0.8, or their length ratio is outside [0.6, 1.6], the tracking claim dies.
# Also proved-by-algebra check: every component of the velocity v = tanh(d) u stays >= 0 (octant invariance).
import numpy as np, math
X = 10**9; M = X//2 + 2
s = np.ones(M, dtype=bool); s[0] = False
for i in range(1, int(math.isqrt(2*M+1))//2 + 1):
    if s[i]:
        p = 2*i+1; s[(p*p)//2::p] = False
tw = np.nonzero(s[:-1] & s[1:])[0]; T = 2*tw+1; T = T[(T > 5) & (T <= X)]; del s
arm = np.searchsorted([1,7,9], T % 10); r = np.log(T[1:]/T[:-1]); sn = arm[1:]; a_next = T[1:]; L = np.cumsum(r)
marks = {int(np.searchsorted(a_next, 10**k, side='right')): k for k in (6,7,8,9)}
diag = np.ones(3)/math.sqrt(3); offd = lambda v: v - (v@diag)*diag
Y = [1.0, 0.0, 0.0, 0.0]; minv = 0.0; rl = r.tolist(); sl = sn.tolist()
for n in range(len(rl)):
    rr = rl[n]; j = sl[n] + 1; c = math.cosh(rr); sh = math.sinh(rr)
    t_, x_ = Y[0], Y[j]; Y[0] = c*t_ + sh*x_; Y[j] = sh*t_ + c*x_
    m = min(Y[1], Y[2], Y[3])
    if m < minv: minv = m
    if (n+1) in marks:
        k = marks[n+1]; y = np.array(Y[1:]); u = y/np.linalg.norm(y)
        w = (L > L[n]-1) & (np.arange(len(L)) <= n)
        Ploc = np.array([r[w][sn[w]==q].sum() for q in range(3)]); Ploc /= Ploc.sum(); Pn = Ploc/np.linalg.norm(Ploc)
        a, b = offd(u), offd(Pn); cs = float(a@b)/np.linalg.norm(a)/np.linalg.norm(b); ratio = np.linalg.norm(a)/np.linalg.norm(b)
        print('1e%d: angle(u,diag)=%.3f deg  angle(P_loc,diag)=%.3f deg  cos(offdiag dirs)=%.3f  length ratio=%.2f  P_loc=%s' %
              (k, math.degrees(math.asin(np.linalg.norm(a))), math.degrees(math.asin(np.linalg.norm(b))), cs, ratio, np.round(Ploc,4)),
              'PASS' if cs >= 0.8 and 0.6 <= ratio <= 1.6 else 'KILL')
print('octant invariance: min component of the body velocity vector along the whole chain = %.3e' % minv, 'PASS' if minv >= 0 else 'KILL')
