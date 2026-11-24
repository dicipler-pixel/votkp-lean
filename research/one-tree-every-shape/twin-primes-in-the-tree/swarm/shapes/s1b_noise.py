# SCRIPT: TWIN-SHAPES-OFFSET-SOURCE-01
# Part 1b: why the random-arm model over-predicts c. The arm-noise term sum r u.(e - P) has mean zero when the next arm
# is independent of the past; on the real chain (first step booked apart) it is -0.409. Hypothesis: consecutive twin starts avoid repeating their
# end digit (a Lemke Oliver - Soundararajan type bias), and the heading leans toward the LAST arm, so the next arm sits
# away from the heading and the noise term goes negative.
# Kill lines, written before the run:
#  K1d if the real chain repeats its end digit at a rate within 1 point of 1/3 below 1e9, the hypothesis is dead.
#  K1e Markov model (arms drawn with the real chain's measured 3x3 digit-transition matrix, true r_n): if its mean
#      noise term is not closer to the real -0.409 than the i.i.d. model's mean is, the hypothesis is dead.
#  K1f prediction of c by the Markov model: killed if |mean c - 0.1085| > 0.01 (expected killed anyway: the spread of one
#      chain is large, so this is reported, not leaned on).
import numpy as np, math, twinlib as t
T = t.twin_starts(); A = t.arms_digit(T); E = np.eye(3); s3 = math.sqrt(3)
r = np.log(T[1:] / T[:-1])
M = np.zeros((3, 3))
np.add.at(M, (A[:-1], A[1:]), 1)
print('digit-transition counts (row = end digit of a_n, column = end digit of a_{n+1}), 1,7,9:')
print(M.astype(int))
Pm = M / M.sum(1, keepdims=True)
print('transition probabilities:\n', np.round(Pm, 4))
rep = np.trace(M) / M.sum(); print('repeat rate %.4f (1/3 = 0.3333)' % rep)
# gap-weighted repeat rate where it matters (early steps carry most of the path)
w = r[1:]; rp = (A[1:-1] == A[2:])
for hi in (1e3, 1e4, 1e5, 1e9):
    m = T[2:] <= hi; print('   r-weighted repeat rate up to %.0e: %.4f   plain: %.4f' % (hi, (w[m] * rp[m]).sum() / w[m].sum(), rp[m].mean()))
print('K1d ->', 'KILLED' if abs(rep - 1 / 3) < 0.01 else 'survives (repeat rate differs from 1/3 by %.3f)' % (1 / 3 - rep))
T8 = T[T <= 10 ** 8]; m8 = np.array([9.99e7]); rng = np.random.default_rng(5)
def ens(gen, k=200):
    out = []
    for _ in range(k):
        Ar = gen(len(T8)); x = t.run_chain(T8, Ar, E, m8, 0)[0]; out.append([x[2] - x[1] / s3, x[22], x[15], x[16], x[17]])
    return np.array(out)
def iid(n): return rng.integers(0, 3, n).astype(np.int64)
cum = np.cumsum(Pm, 1)
def markov(n):
    a = np.empty(n, np.int64); a[0] = A[0]; u = rng.random(n)
    for i in range(1, n): a[i] = np.searchsorted(cum[a[i - 1]], u[i])
    return a
real = t.run_chain(T8, A[:len(T8)], E, m8, 0)[0]; realv = [real[2] - real[1] / s3, real[22], real[15], real[16], real[17]]
I = ens(iid); Mk = ens(markov)
print('                      c        start      curv.gain  arm-noise  heading-lag')
print('real chain        %+.4f   %+.4f   %+.4f   %+.4f   %+.4f' % tuple(realv))
print('i.i.d. arms mean  %+.4f   %+.4f   %+.4f   %+.4f   %+.4f   (sd of c %.4f)' % (*I.mean(0), I[:, 0].std()))
print('Markov arms mean  %+.4f   %+.4f   %+.4f   %+.4f   %+.4f   (sd of c %.4f)' % (*Mk.mean(0), Mk[:, 0].std()))
print('real arm-noise rank among i.i.d. chains: %d/200 (i.i.d. sd %.4f); among Markov: %d/200' % ((I[:, 3] < realv[3]).sum(), I[:, 3].std(), (Mk[:, 3] < realv[3]).sum()))
print('K1e ->', 'survives' if abs(Mk[:, 3].mean() - realv[3]) < abs(I[:, 3].mean() - realv[3]) else 'KILLED')
print('K1f Markov prediction miss %.4f ->' % abs(Mk[:, 0].mean() - realv[0]), 'survives' if abs(Mk[:, 0].mean() - realv[0]) <= 0.01 else 'KILLED')
# where c is built: the real chain's first steps
print('first 14 steps: a -> a\', arm, r, running c')
L = np.eye(4); path = 0
for i in range(14):
    rr = r[i]; L = L @ t.boost4(E[A[i + 1]], rr); path += rr; d = math.acosh(L[0, 0])
    print('   %4d -> %4d  arm %s  r %.4f  d %.4f  c %+.4f' % (T[i], T[i + 1], 'xyz'[A[i + 1]], rr, d, d - path / s3))
