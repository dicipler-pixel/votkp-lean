# SCRIPT: OPPOSITE-FRAME-FINE-01
# Frame increments on a fine grid (cut-offs 10^(k/2)), and the body-frame axis of each increment,
# for all primes (SO(1,4)), sexy, twins. Kill for "turn converges": half-decade increments must shrink by >=25% per decade over 1e5..1e8.
import numpy as np, math
from owalk import *
N=10**8; P=primes_upto(N); isp=np.zeros(N+7,dtype=bool); isp[P]=True
def chain(gap):
    S=P[(P>5)&(P+gap<=N)]; return S[isp[S+gap]]
cuts=[10**(k/2) for k in range(8,17)]
def logm_axis(Rm):
    # rotation generator (antisymmetric) of Rm via eig-free log for small rotations
    A=(Rm-Rm.T)/2; return A
for name,S,digs,E in (('all primes SO(1,4)',P[P>5],[1,3,7,9],np.eye(4)),('sexy',chain(6),[1,3,7],np.eye(3)),('twins',chain(2),[1,7,9],np.eye(3)),('cousins',chain(4),[3,7,9],np.eye(3))):
    r=np.log(S[1:]/S[:-1]); nx=S[1:]; a=np.searchsorted(digs,nx%10)
    rec=np.array([np.searchsorted(nx,x,side='right')-1 for x in cuts])
    D,Nn,RR,TOT=walk(r,a,E,rec); Lc=np.cumsum(r)[rec]
    print('==',name)
    for j in range(1,len(cuts)):
        inc=RR[j]@RR[j-1].T; ang=rot_angles(inc); A=logm_axis(RR[j-1].T@RR[j])  # body-frame generator
        g=A[np.triu_indices(E.shape[1],1)]; g=g/np.linalg.norm(g)
        print('  %.1e->%.1e  dL=%.3f  frame increment %.4f deg   rate %.4f deg/unit L   body generator %s   total turning %.1f deg'%(cuts[j-1],cuts[j],Lc[j]-Lc[j-1],math.sqrt(sum(t*t for t in ang)),math.sqrt(sum(t*t for t in ang))/(Lc[j]-Lc[j-1]),np.round(g,2),math.degrees(TOT[j])))
