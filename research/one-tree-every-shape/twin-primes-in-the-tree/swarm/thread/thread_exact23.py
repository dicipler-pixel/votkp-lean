# SCRIPT: TWIN-THREAD-EXACT-23
# Same exact screw model as TWIN-THREAD-EXACT-01, cut one prime deeper (P <= 23), decade 1e8-1e9 only.
# Tail cut at K = 20/p_slot (dropped weight about e^-20).
# KILL (written before the run): convergence fails if the P<=23 values of digits 1 or 7 leave
# 2 standard errors of the real 1e8-1e9 values (-0.924 +- 0.041, +0.839 +- 0.034).
import numpy as np, math, time
t=time.time()
ps=[2,3,5,7,11,13,17,19,23]; W=math.prod(ps)
cop=np.ones(W,bool)
for p in ps: cop[::p]=False
s=np.nonzero(cop&np.roll(cop,-2))[0].astype(np.int64); M=len(s)
N=math.sqrt(1e8*1e9); q=(W/np.prod([p-1 for p in ps]))/math.log(N); pr=q*q; K=int(20/pr)+1
Eg=np.zeros(M); w=pr; ext=np.concatenate([s[-K-1:]-W,s])
for k in range(1,K+1):
    Eg+=(s-ext[K+1-k:K+1-k+M])*w; w*=1-pr
G=Eg.mean(); c=s%10
d=np.array([Eg[c==x].sum()/Eg.sum()-1/3 for x in (1,7,9)])*G
z=(np.array([-0.924,0.839])-d[:2])/np.array([0.041,0.034])
print('P<=23 slots',M,' dev*G (1,7,9)',np.round(d,3),' z(1,7)',np.round(z,1),' PASS' if np.all(abs(z)<2) else ' KILL','  %.0fs'%(time.time()-t))
