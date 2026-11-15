# SCRIPT: s14_identifiability
# Why: if a drift model were structurally unidentifiable, its Fisher matrix would be singular and no precision
# would help. If it is only ill-conditioned, the errors shrink in proportion to the precision and a different
# energy order breaks the correlation. Fisher matrix of (a, U0, dU) for a linear drift, bin-integrated yields.
import numpy as np
from screen04_model import *
def fisher(Es, sig, U0=200., dU=300., h=0.05):
    th = np.array([0., U0, dU])
    def model(t): return t[0] + campaign(lambda f: t[1]+t[2]*f, Es, nodes=200)
    J = np.array([(model(th+h*e)-model(th-h*e))/(2*h) for e in np.eye(3)]).T
    C = np.linalg.inv(J.T @ np.diag(1/sig**2) @ J); sd = np.sqrt(np.diag(C))
    return sd[1], sd[2], C[1,2]/(sd[1]*sd[2]), np.linalg.matrix_rank(J), np.linalg.cond(J)
for p in [0.02, 0.002]:
    a,b,r,rk,cn = fisher(SCAN, np.full(8,p)); print('descending, %.1f%%: sd U0 %.2f, sd dU %.2f, corr %.4f, rank %d'%(100*p,a,b,r,rk))
DU = np.concatenate([SCAN, SCAN[::-1]]); BB = np.concatenate([SCAN, SCAN])
print('fixed total fluence, 16 exposures, errors x sqrt2, 2%%: down-up sd U0 %.2f ; two descending blocks %.2f'%(fisher(DU, np.full(16,0.02*np.sqrt(2)))[0], fisher(BB, np.full(16,0.02*np.sqrt(2)))[0]))
