# SCRIPT: OPPOSITE-SHARE-DRIFT-01
# Why do some chains lock slowly? Per decade, the path-weighted arm share  q_s = sum_{decade} r 1[s] / sum_{decade} r  minus 1/m.
# If the deviation falls like 1/L (L = path at the decade's middle), dev*L stays constant and the noise sum grows like ln L (H3 fails, turn drifts like ln L).
# If it falls like 1/L^2 (the HL expectation for k-tuples, mean gap ~ ln^2 x), dev*L^2 stays constant and everything converges.
# Kill line for the "gap-before-class bias" explanation: for all primes, dev*L must be steady (within 25%) over the last three decades.
import numpy as np, math
from owalk import primes_upto
N=10**8; P=primes_upto(N); isp=np.zeros(N+7,dtype=bool); isp[P]=True
def chain(gap):
    S=P[(P>5)&(P+gap<=N)]; return S[isp[S+gap]]
sets={'all primes (1,3,7,9)':(P[P>5],[1,3,7,9]),'twins (1,7,9)':(chain(2),[1,7,9]),'cousins (3,7,9)':(chain(4),[3,7,9]),'sexy (1,3,7)':(chain(6),[1,3,7])}
for name,(S,digs) in sets.items():
    r=np.log(S[1:]/S[:-1]); nx=S[1:]; a=np.searchsorted(digs,nx%10); Lc=np.cumsum(r); m=len(digs)
    print('==',name)
    for k in range(4,9):
        w=(nx>10**(k-1))&(nx<=10**k); Lm=np.log(10**(k-0.5)/S[0])
        q=np.array([r[w&(a==s)].sum() for s in range(m)])/r[w].sum()-1/m
        cnt=np.array([(w&(a==s)).sum() for s in range(m)])/w.sum()-1/m
        print('  1e%d-1e%d  L~%.2f  path-share dev %s  dev*L %s  dev*L^2 %s  | count-share dev %s'%(k-1,k,Lm,np.round(q,4),np.round(q*Lm,3),np.round(q*Lm**2,2),np.round(cnt,4)))
