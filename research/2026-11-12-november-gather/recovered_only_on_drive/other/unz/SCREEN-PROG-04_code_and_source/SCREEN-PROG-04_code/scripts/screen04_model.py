# SCRIPT: screen04_model
# Shared forward model for SCREEN-PROG-04: penetration factor R(E,U) = exp(-sqrt(EG/(E+U))), EG = 986000 eV (CM).
import numpy as np
EG = 986000.0
SCAN = np.array([6000, 5000, 4000, 3250, 2500, 2000, 1600, 1250.])
def lnR(E, U): return -np.sqrt(EG/(E+U))
def campaign(Uf, Es=SCAN, point=False, nodes=2000):
    n = len(Es); out = []
    for i, E in enumerate(Es):
        if point: out.append(lnR(E, Uf(i/(n-1)))); continue
        f = (i + (np.arange(nodes)+0.5)/nodes)/n
        out.append(np.log(np.mean(np.exp(lnR(E, Uf(f))))))
    return np.array(out)
def fit_const(lY, Es=SCAN, fixed=False):
    from scipy.optimize import minimize_scalar
    def cost(U):
        r = lY - lnR(Es, U); m = 0.0 if fixed else r.mean(); return np.sum((r-m)**2)
    return minimize_scalar(cost, bounds=(0, 2000), method='bounded', options={'xatol':1e-6}).x
# lognormal spread, Gauss-Hermite in z
z, wz = np.polynomial.hermite_e.hermegauss(80); wz = wz/wz.sum()
def lnYmix(E, mu, s):
    if s < 1e-9: return lnR(E, mu)
    v = np.log(1+(s/mu)**2); m = np.log(mu) - v/2
    return np.log(np.sum(wz*np.exp(lnR(E, np.exp(m+np.sqrt(v)*z)))))
def count_err(E, k=1.0):   # log-log interpolation 0.020 at 2 keV -> 0.005 at 6 keV, scaled by k
    return k*np.exp(np.interp(np.log(E), np.log([2000, 6000]), np.log([0.020, 0.005])))
SYS_IND = np.sqrt(0.004**2 + 0.002**2 + 0.006**2 + 0.005**2)   # gain, dead time, spot, background
STOP = 0.010
