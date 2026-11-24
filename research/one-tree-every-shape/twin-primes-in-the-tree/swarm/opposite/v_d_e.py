# SCRIPT: OPPOSITE-RANDOM-ADVERSARIAL-FIXED-01
# d-cram: Cramer random twins (candidates m = 5 mod 6, probability 12*C2/ln^2 m), arms iid uniform on x,y,z; 5 realisations.
# d-blk: real twin steps, arms set by path blocks: arm = floor(L/Lambda) mod 3 (Lambda = 0.25, 1, 4), and geometric blocks (boundaries at 1.5^k).
# e-fix: every step r = ln 5, arms = real twin end-digit sequence (and an iid-arm control).
# Kill lines: PREDICTIONS.md.
import numpy as np, math
from owalk import *
C2=0.6601618158468696
N=10**8; P=primes_upto(N); tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
r=np.log(T[1:]/T[:-1]); nxt=T[1:]; arm=np.searchsorted([1,7,9],nxt%10)
cuts=[10**k for k in range(3,9)]; Pv=np.ones(3)/3; E=np.eye(3)
for seed in range(5):
    rng=np.random.default_rng(100+seed)
    m=np.arange(11,N+1,6,dtype=np.int64)
    keep=rng.random(m.size)<12*C2/np.log(m.astype(float))**2
    S=np.concatenate([[11],m[keep][m[keep]>11]])
    rr=np.log(S[1:]/S[:-1]); aa=rng.integers(0,3,rr.size)
    rows=report('d-cram realisation %d (%d starts)'%(seed,S.size),S[1:],rr,aa,E,cuts,Pv)
    verdict(rows,1/math.sqrt(3))
Lc=np.cumsum(r)
for lab,blk in (('Lambda=0.25',np.floor(Lc/0.25)),('Lambda=1',np.floor(Lc/1.0)),('Lambda=4',np.floor(Lc/4.0)),('geometric 1.5^k',np.floor(np.log(Lc)/math.log(1.5)))):
    aa=(blk.astype(np.int64))%3
    rows=report('d-blk '+lab,nxt,r,aa,E,cuts,Pv)
    verdict(rows,1/math.sqrt(3))
# e: fixed ratio
ns=len(r); rf=np.full(ns,math.log(5))
idxcuts=[np.searchsorted(nxt,x,side='right') for x in cuts]   # same step counts as the twin cut-offs
fake_end=np.arange(1,ns+1)                                      # cut by step number
for lab,aa in (('e-fix ln5, twin digit arms',arm),('e-fix ln5, iid arms (control)',np.random.default_rng(9).integers(0,3,ns))):
    rows=report(lab,fake_end,rf,aa,E,idxcuts,Pv,'(cut column = step count)')
    verdict(rows,1/math.sqrt(3))
