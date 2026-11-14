# SCRIPT: s16_checks
# Re-derives the remaining quoted numbers of SCREEN-PROG-04 from screen04_model.
# (1) Schedules under an uneven error profile, log-linear from 2% at 6 keV to 30% at 1.25 keV, at fixed fluence.
# (2) A fake width from opposite 1% distortions of the two ratios on a homogeneous 340 eV target.
# (3) Monte Carlo of the profile likelihood ratio (s free vs s = 0) at 2, 3.5, 6 keV over six steps.
import numpy as np
from scipy.optimize import minimize, minimize_scalar
from screen04_model import *
from s14_identifiability import fisher
prof = lambda Es: np.exp(np.interp(np.log(Es), np.log([1250, 6000]), np.log([0.30, 0.02])))
DU = np.concatenate([SCAN, SCAN[::-1]]); BB = np.concatenate([SCAN, SCAN])
print('(1) uneven profile, sd U0: down-up %.1f  two blocks %.1f  one sweep %.1f' % (fisher(DU, prof(DU)*np.sqrt(2))[0], fisher(BB, prof(BB)*np.sqrt(2))[0], fisher(SCAN, prof(SCAN))[0]))
rat = lambda mu, s, E3=3500.: np.array([lnYmix(2000,mu,s)-lnYmix(6000,mu,s), lnYmix(E3,mu,s)-lnYmix(6000,mu,s)])
d = rat(340, 0) + np.array([0.01, -0.01])
r = minimize(lambda p: np.sum((rat(p[0], abs(p[1])) - d)**2), [340, 80], method='Nelder-Mead', options={'xatol':1e-5,'fatol':1e-18,'maxiter':4000})
print('(2) opposite 1%% distortions: fitted mu %.1f, width %.1f eV' % (r.x[0], abs(r.x[1])))
# (3) Monte Carlo
k = np.sqrt(1.5); c2, c3, c6 = count_err(2000,k), count_err(3500,k), count_err(6000,k)
A = np.array([[c2**2+c6**2+SYS_IND**2, c6**2],[c6**2, c3**2+c6**2+SYS_IND**2]])
mus = np.linspace(150, 600, 451); ss = np.linspace(0, 400, 401)
tab = np.array([[rat(m, s) for s in ss] for m in mus[::5]])   # coarse grid, refined below
def prof_fit(dbar, Ci, n):
    # profile over mu on a fine 1D grid for each s on the coarse table, then refine locally
    best_null = minimize_scalar(lambda m: n*((dbar-rat(m,0))@Ci@(dbar-rat(m,0))), bounds=(100,800), method='bounded').fun
    best_alt = min(best_null, minimize(lambda p: n*((dbar-rat(p[0],abs(p[1])))@Ci@(dbar-rat(p[0],abs(p[1])))), [340,150], method='Nelder-Mead', options={'xatol':1e-3,'fatol':1e-10,'maxiter':600}).fun)
    return best_null - best_alt
rng = np.random.default_rng(20261028)
for mode in ['indep', 'shared_unrelated']:
    Astep = A + (np.diag([STOP**2]*2) if mode=='indep' else 0); B = np.zeros((2,2)) if mode=='indep' else np.diag([STOP**2]*2)
    n = 6; Ci = np.linalg.inv(Astep + n*B)
    for s_true, N in [(150, 1000), (0, 400)]:
        mean = rat(340, s_true); q = []
        for _ in range(N):
            common = rng.multivariate_normal(np.zeros(2), B) if mode != 'indep' else 0
            steps = mean + common + rng.multivariate_normal(np.zeros(2), Astep, size=n)
            q.append(max(0, prof_fit(steps.mean(0), np.linalg.inv(Astep/n + B)/n, n)))
        q = np.array(q)
        if s_true: print('(3) %-16s s=150: median sqrt(q) %.2f, P(q>9) %.3f' % (mode, np.median(np.sqrt(q)), np.mean(q>9)))
        else: print('(3) %-16s s=0:   P(q>2.71) %.3f (N=%d)' % (mode, np.mean(q>2.7055), N))
