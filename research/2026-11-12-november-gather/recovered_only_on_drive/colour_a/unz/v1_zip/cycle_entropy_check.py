# SCRIPT: CYCLE-ENTROPY-01
# What the Present Keeps §8.4 states a cycle-entropy identity whose printed form came through garbled. Candidate,
# reconstructed from the readable pieces: with h(x) = -x log x - (1-x) log(1-x) and the average
#   s_l = (1/l) sum_{j=0}^{l-1} h(sin^2(pi j / l)),   D_l = 2 log 2 - 1 - s_l,
#   D_l = sum_{m >= 1, l | 2m} 1 / (m (4 m^2 - 1)).
# Why this checks it: the continuum average of h(sin^2 theta) over a period is 2 log 2 - 1; sampling at l points
# aliases the Fourier coefficients of h(sin^2 theta) onto multiples of l, which is what the sum over l | 2m encodes.
# KILL: any l in 2..40 where the two sides differ by more than 1e-10.
import numpy as np
def h(x):
    x = np.clip(x, 1e-300, 1); y = np.clip(1 - x, 1e-300, 1); return -x * np.log(x) - y * np.log(y)
worst = 0.0
for l in range(2, 41):
    s = np.mean(h(np.sin(np.pi * np.arange(l) / l)**2)); D = 2 * np.log(2) - 1 - s
    rhs = sum(1.0 / (m * (4 * m * m - 1)) for m in range(1, 200001) if (2 * m) % l == 0)
    worst = max(worst, abs(D - rhs))
print('largest |D_l - sum| over l = 2..40: %.2e' % worst)
cont = 2 * np.log(2) - 1; print('continuum average 2 log 2 - 1 = %.12f' % cont)
