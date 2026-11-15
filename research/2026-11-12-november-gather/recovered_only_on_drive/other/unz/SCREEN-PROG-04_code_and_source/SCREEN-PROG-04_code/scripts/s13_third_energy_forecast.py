# SCRIPT: s13_third_energy_forecast
# Why this check proves what it claims: the question is whether a spread s can be told apart from s = 0.
# So the zero-spread model (mean refitted) is fitted to the noise-free expectation at spread s, and the
# chi-square gap q gives the expected (Asimov) separation sqrt(q). A local error at s = 150 cannot answer
# that question, because the bend grows steeply with s.
# Covariance: counting errors scaled by sqrt(3/2) (three energies share the time two had), the shared 6 keV
# reference couples the two ratios, independent residual terms per ratio, and the stopping residual 0.010
# either independent at every step, or common to all six steps (two cases: unrelated between the two ratios,
# or one smooth stopping-power error that moves the E3/6 ratio by 0.49 of the 2/6 ratio).
import numpy as np
from scipy.optimize import minimize_scalar
from screen04_model import *
def Z(s, E3=3500., mode='indep', mu=340., n=6):
    k = np.sqrt(1.5); c2, c3, c6 = count_err(2000,k), count_err(E3,k), count_err(6000,k)
    A = np.array([[c2**2+c6**2+SYS_IND**2, c6**2],[c6**2, c3**2+c6**2+SYS_IND**2]])
    if mode == 'indep': A = A + np.diag([STOP**2, STOP**2]); B = np.zeros((2,2))
    elif mode == 'shared_unrelated': B = np.diag([STOP**2, STOP**2])
    elif mode == 'shared_smooth': B = STOP**2*np.array([[1,0.49],[0.49,0.49**2]])
    d = np.array([lnYmix(2000,mu,s)-lnYmix(6000,mu,s), lnYmix(E3,mu,s)-lnYmix(6000,mu,s)])
    Ci = np.linalg.inv(A + n*B)     # identical expectation in every step: chi2 = n * r^T (A + n B)^-1 r
    def q(m0):
        r = d - np.array([lnR(2000,m0)-lnR(6000,m0), lnR(E3,m0)-lnR(6000,m0)]); return n*(r@Ci@r)
    return np.sqrt(minimize_scalar(q, bounds=(50,900), method='bounded', options={'xatol':1e-6}).fun)
print('E3 = 3.5 keV, s = 150 eV, six steps')
for m in ['indep','shared_unrelated','shared_smooth']: print('  %-17s Z = %.2f'%(m, Z(150, mode=m)))
print('E3 = 3.0 keV: indep %.2f  shared_unrelated %.2f'%(Z(150,3000.), Z(150,3000.,'shared_unrelated')))
print('spread dependence (independent stopping), E3 = 3.5 keV')
for s in [50,100,150,200,250]: print('  s = %3d eV  Z = %.2f'%(s, Z(s)))
