# SCRIPT: VP-PUSH-STAR-IN-BALL-01
# The exact 5/3 star, drawn in the ball: centre at the origin, three legs of length l at 120 degrees.
# Leg end to leg end in hyperbolic space: cosh d = cosh^2 l - sinh^2 l * cos(120 degrees).
# KILL LINE: the ratio must rise from the flat value (small l) toward 5/3 (large l) and never pass 2.
import numpy as np, itertools
src = open('star_search.py').read().split('for mu, flat, iters in')[0]; ns = {}; exec(src, ns)
N, A1, Am = ns['setup'](2)
vec = np.array(list(itertools.product((0, 1), repeat=4))); lab = np.zeros(16, dtype=int)
for t, v in enumerate(vec):
    M = v.reshape(2, 2); det = (M[0, 0]*M[1, 1] - M[0, 1]*M[1, 0]) % 2
    if M.any() and not det: lab[t] = 1 + int(str(int(M[0].any())) + str(int(M[1].any())), 2)
c = lab == 0; same = lab[:, None] == lab[None, :]; cl = c[:, None] ^ c[None, :]; ll = (~same) & (~cl)
cnt = lambda A: (int((A & cl).sum())//2, int((A & ll).sum())//2, int((A & same).sum() - (16 if A is None else 0))//2)
n1 = cnt(A1); n2 = cnt(Am)
print('rank-1 pairs (72): centre-to-leg %d, leg-to-leg %d, same place %d' % n1)
print('rank-2 pairs (48): centre-to-leg %d, leg-to-leg %d, same place %d' % n2)
for l in (0.01, 0.5, 1, 2, 4, 8, 16, 40):
    dll = np.arccosh(np.cosh(l)**2 + 0.5*np.sinh(l)**2)
    r = ((n2[0]*l*l + n2[1]*dll*dll)/48)/((n1[0]*l*l + n1[1]*dll*dll)/72)
    print('leg length %6.2f: leg-end to leg-end %8.3f (tree value %8.3f); ratio %.6f' % (l, dll, 2*l, r))
print('flat value of the same shape (legs at 120 degrees in a plane): %.6f ; tree value: %.6f' % (((n2[0] + 3*n2[1])/48)/((n1[0] + 3*n1[1])/72), ((n2[0] + 4*n2[1])/48)/((n1[0] + 4*n1[1])/72)))
