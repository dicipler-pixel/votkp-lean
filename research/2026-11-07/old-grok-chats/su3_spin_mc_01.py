# SCRIPT: SU3-SPIN-MC-01
# Metropolis Monte Carlo of the 3D SU(3) spin model (traced Polyakov loops), mu = 0:
#   S = - sum_x [ sum_k tau (P_x P*_{x+k} + c.c.) + kappa (P_x + P*_x) ],  P = e^{i a} + e^{i b} + e^{-i(a+b)}
# with the reduced Haar measure |Vandermonde|^2 on the eigenvalue angles.
# Why this checks the old chat: it quoted (tau_c, kappa_c) ~ (0.133, 0.015); the published endpoint is
# (0.1331(1), 0.016(2)) (Delgado Mercado & Gattringer). At kappa = 0.016 the susceptibility chi_P must peak near
# tau = 0.133 if the quoted numbers belong to this model.  Keep if the peak lies within 0.128-0.138 on L = 12.
import numpy as np, sys
rng = np.random.default_rng(7)
L = int(sys.argv[1]) if len(sys.argv) > 1 else 12
def P_of(a, b): return np.exp(1j*a) + np.exp(1j*b) + np.exp(-1j*(a+b))
def haar(a, b):
    z = np.stack([np.exp(1j*a), np.exp(1j*b), np.exp(-1j*(a+b))])
    return (np.abs(z[0]-z[1])*np.abs(z[0]-z[2])*np.abs(z[1]-z[2]))**2
X, Y, Z = np.indices((L, L, L)); par = (X + Y + Z) % 2
def run(tau, kappa, therm=300, meas=600):
    a = rng.uniform(-np.pi, np.pi, (L, L, L)); b = rng.uniform(-np.pi, np.pi, (L, L, L))
    if tau > 0.13: a[:] = 0.1; b[:] = -0.1           # hot start for the ordered side helps a first-order line
    Ms = []
    for sweep in range(therm + meas):
        for c in (0, 1):
            P = P_of(a, b); nb = sum(np.roll(P, s, ax) for ax in range(3) for s in (1, -1))
            an = a + rng.normal(0, 0.9, a.shape); bn = b + rng.normal(0, 0.9, b.shape)
            Pn = P_of(an, bn)
            dS = -2*tau*np.real((Pn - P)*np.conj(nb)) - 2*kappa*np.real(Pn - P)
            acc = (rng.random(a.shape) < haar(an, bn)/np.maximum(haar(a, b), 1e-300)*np.exp(-dS)) & (par == c)
            a = np.where(acc, an, a); b = np.where(acc, bn, b)
        if sweep >= therm: Ms.append(P_of(a, b).mean())
    M = np.abs(np.array(Ms)); V = L**3
    return M.mean(), V*(np.mean(M**2) - M.mean()**2)
print('L =', L, ' kappa = 0.016, mu = 0')
res = []
for tau in np.round(np.arange(0.118, 0.1485, 0.003), 4):
    m, chi = run(tau, 0.016); res.append((tau, m, chi)); print('tau %.4f  <|P|> %.4f  chi_P %.3f' % (tau, m, chi), flush=True)
t, m, chi = max(res, key=lambda r: r[2]); print('peak of chi_P at tau = %.4f' % t)
