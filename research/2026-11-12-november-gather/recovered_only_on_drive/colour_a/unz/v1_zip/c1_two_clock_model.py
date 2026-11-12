# SCRIPT: TWO-CLOCK-MODEL-01
# Two clocks of different kinds side by side: a strontium optical lattice clock (electron-shell transition) and a
# thorium-229 nuclear clock (nuclear transition). Each clock's fractional frequency reading is modelled as
#     y_i(t) = u(t) + K_i * a(t) + n_i(t)
#   u(t) : the universal part, the same for every clock (gravitational potential / time dilation: U/c^2)
#   a(t) : a non-universal part, here a change of the fine-structure constant, d(alpha)/alpha
#   K_i  : each clock's sensitivity to alpha: Sr +0.06 (QSNET table, arXiv:2112.10618), Th-229 5900 +- 2300
#          (Beeks et al., arXiv:2407.17300)
#   n_i  : the clock's own noise, white, per one-day point
# Noise inputs (stated, not fitted): Sr 1e-18 per day (the JILA systematic floor is 8e-19); Th-229 now 1e-15 per day
# (continuous feedback-loop clock, arXiv:2606.04997, "approaching 1e-15 over 1 day"); Th-229 target 1e-18.
# Three questions, each with its kill condition written before the run:
#   Q1 timekeeping: does averaging the two beat Sr alone? Dies (for "two beat one") if the best weighted average has
#      error >= Sr alone.
#   Q2 separation: with an unknown alpha drift present, one clock reads u + K a and cannot tell them apart; two clocks
#      solve a 2x2 system. Dies if the two-clock estimate of u is no better than Sr alone with the drift present.
#   Q3 universality: the ratio y_Th - y_Sr cancels u exactly. If gravity coupled to alpha (a = k_alpha * U/c^2), the
#      ratio would swing with the Sun's potential over the year (Earth's orbit, eccentricity 0.0167). How small a
#      k_alpha can one year resolve? Control: inject k_alpha and recover it.
import numpy as np
rng = np.random.default_rng(2026)
G, Msun, c, AU, e = 6.674e-11, 1.989e30, 2.998e8, 1.496e11, 0.0167
KSr, KTh, dKTh = 0.06, 5900.0, 2300.0
days = np.arange(365)
phase = 2 * np.pi * days / 365.25
U_sun = G * Msun / (c**2 * AU) * (1 + e * np.cos(phase))       # U/c^2 from the Sun, about 9.9e-9
dU = U_sun - U_sun.mean()
print('solar potential at Earth U/c^2 = %.3e, annual swing peak-to-peak %.2e' % (U_sun.mean(), dU.max() - dU.min()))

for label, sTh in [('Th-229 today (1e-15/day)', 1e-15), ('Th-229 target (1e-18/day)', 1e-18)]:
    sSr = 1e-18
    print('\n== %s, Sr 1e-18/day ==' % label)
    # Q1: inverse-variance average of the universal part, no alpha drift
    w = np.array([1 / sSr**2, 1 / sTh**2]); w /= w.sum()
    comb = np.sqrt(w[0]**2 * sSr**2 + w[1]**2 * sTh**2)
    print('Q1 timekeeping: Sr alone %.2e, best average %.2e  -> gain factor %.3f' % (sSr, comb, sSr / comb))
    # Q2: with an unknown alpha drift a(t) (random walk, 1e-20 per day steps), estimate u(t) daily
    trials = 400; err1, err2 = [], []
    for _ in range(trials):
        a = np.cumsum(rng.normal(0, 1e-20, 365)); u = 1e-17 * np.sin(phase * 3)
        ySr = u + KSr * a + rng.normal(0, sSr, 365); yTh = u + KTh * a + rng.normal(0, sTh, 365)
        u_one = ySr                                            # one clock: drift is read as time
        a_hat = (yTh - ySr) / (KTh - KSr)                      # two clocks: solve the 2x2 system each day
        u_two = ySr - KSr * a_hat
        err1.append(np.sqrt(np.mean((u_one - u)**2))); err2.append(np.sqrt(np.mean((u_two - u)**2)))
    print('Q2 reading u with an unknown alpha drift present: Sr alone rms %.3e, two clocks %.3e' % (np.mean(err1), np.mean(err2)))
    print('   alpha drift recovered per day to %.2e (in d(alpha)/alpha)' % (np.sqrt(sTh**2 + sSr**2) / (KTh - KSr)))
    # Q3: ratio over one year, least-squares amplitude of the annual swing -> k_alpha
    A = dU * (KTh - KSr)
    sig_k = np.sqrt(sTh**2 + sSr**2) / np.sqrt(np.sum(A**2))
    k_true = 50 * sig_k
    yR = k_true * A + rng.normal(0, np.sqrt(sTh**2 + sSr**2), 365)
    k_fit = np.sum(yR * A) / np.sum(A**2)
    print('Q3 one year of the Th/Sr ratio resolves k_alpha to 1 sigma = %.2e  (K_Th uncertainty adds %.0f%% to that scale)'
          % (sig_k, 100 * dKTh / KTh))
    print('   control: injected k_alpha = %.3e, recovered %.3e' % (k_true, k_fit))
