# SCRIPT: W14-EQUALITY (watcher) does the offset speed limit tau'^2 <= 4 g S have a saturating case? WPMK Theorem 8: equality iff Pdot = lam [P,[P,F]], F = E W E^dag, W = -(C(I-C))^-1.
# Why it matters: the lineage's driven runs reach only 0.02 of the bound, so they could not catch a factor-of-5 error in tau-dot. A check that CAN fail must be able to reach 1.
import numpy as np
rng = np.random.default_rng(7); n=6; k=2
X = rng.normal(size=(n,k))+1j*rng.normal(size=(n,k)); Q,_ = np.linalg.qr(X); P = Q@Q.conj().T
E = np.zeros((n,2)); E[0,0]=1; E[1,1]=1
# make C interior: mix so that 0<C<I
C = E.T@P@E; print('eig C', np.linalg.eigvalsh(C))
I2 = np.eye(2); W = -np.linalg.inv(C@(I2-C)); F = E@W@E.T
def comm(a,b): return a@b-b@a
Pd = comm(P, comm(P, F)); Pd = (Pd+Pd.conj().T)/2   # lam = 1, real
Cd = E.T@Pd@E; taud = -np.trace(np.linalg.inv(C@(I2-C))@Cd).real
g = 0.5*np.linalg.norm(Pd)**2; S = np.trace(np.linalg.inv(C@(I2-C))).real
print('equality direction: tau-dot^2/(4 g S) = %.12f (theorem: 1 at equality)' % (taud**2/(4*g*S)))
# random direction tangent at P for comparison
H = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); H=(H+H.conj().T)/2; Pd2 = -1j*comm(H,P); C2 = E.T@Pd2@E; t2 = -np.trace(np.linalg.inv(C@(I2-C))@C2).real; g2=0.5*np.linalg.norm(Pd2)**2
print('random driven direction: ratio %.4f' % (t2**2/(4*g2*S)))
# tau-dot formula vs finite difference of log det(I-C) - log det C along equality flow
def tau(Pm): Cm=E.T@Pm@E; return np.log(np.linalg.det(I2-Cm).real)-np.log(np.linalg.det(Cm).real)
from scipy.linalg import expm
# P(s) = U P U^dag with U = exp(-i s Hgen), Pd = -i[Hgen,P] -> Hgen = i*Pd-generator: solve Hgen = i [P,Pd]... use Hgen = -i [Pd, P]? check numerically
Hg = 1j*comm(Pd,P)  # candidate; verify it generates Pd
print('generator check |-i[Hg,P] - Pd| = %.2e' % np.linalg.norm(-1j*comm(Hg,P)-Pd))
e=1e-6; Pp=expm(-1j*e*Hg)@P@expm(1j*e*Hg); Pm=expm(1j*e*Hg)@P@expm(-1j*e*Hg); print('finite-difference tau-dot %.8f vs formula %.8f' % ((tau(Pp)-tau(Pm))/(2*e), taud))
