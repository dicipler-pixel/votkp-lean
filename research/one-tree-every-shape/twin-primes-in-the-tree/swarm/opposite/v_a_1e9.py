# SCRIPT: OPPOSITE-ALLPRIMES-1E9-01
# Segmented sieve to 1e9, all primes p>5, arms by end digit 1/3/7/9. Runs a-i (tetrahedron) and a-ii (SO(1,4)) to 1e9,
# plus path-share bias per decade. Kill lines: PREDICTIONS.md second round (P1, P2, P3).
import numpy as np, math, os
from owalk import *
N=10**9; f=os.path.join(HERE,'primes_1e9.npy')
if os.path.exists(f): Q=np.load(f)
else:
    base=primes_upto(10**5); base=base[base<=int(N**.5)+1]; out=[]; seg=10**7
    for lo in range(0,N+1,seg):
        hi=min(lo+seg,N+1); s=np.ones(hi-lo,dtype=bool)
        if lo==0: s[:2]=False
        for p in base:
            if p*p>=hi: break
            st=max(p*p,((lo+p-1)//p)*p); s[st-lo::p]=False
        out.append(np.nonzero(s)[0].astype(np.int64)+lo)
    Q=np.concatenate(out); np.save(f,Q)
print('primes to 1e9:',Q.size)
Q=Q[Q>5]; r=np.log(Q[1:]/Q[:-1]); nx=Q[1:]; a=np.searchsorted([1,3,7,9],nx%10)
cuts=[10**k for k in range(3,10)]
tet=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/math.sqrt(3)
rows=report('a-i tetra to 1e9',nx,r,a,tet,cuts,np.zeros(3))
print(' decade changes of d',np.round(np.diff([x['d'] for x in rows]),4))
rows=report('a-ii SO(1,4) to 1e9',nx,r,a,np.eye(4),cuts,np.ones(4)/4); verdict(rows,0.5)
fine=[10**(k/2) for k in range(12,19)]
rec=np.array([np.searchsorted(nx,x,side='right')-1 for x in fine]); D,Nn,RR,_=walk(r,a,np.eye(4),rec); Lc=np.cumsum(r)[rec]
for j in range(1,len(fine)):
    ang=rot_angles(RR[j]@RR[j-1].T); g=math.sqrt(sum(t*t for t in ang))
    print('  a-ii frame %.1e->%.1e: increment %.4f deg, rate %.4f deg/unit L, rate*L^2 %.1f'%(fine[j-1],fine[j],g,g/(Lc[j]-Lc[j-1]),g/(Lc[j]-Lc[j-1])*((Lc[j]+Lc[j-1])/2)**2))
for k in (8,9):
    w=(nx>10**(k-1))&(nx<=10**k); Lm=math.log(10**(k-0.5)/7)
    q=np.array([r[w&(a==s)].sum() for s in range(4)])/r[w].sum()-0.25
    print('  share bias 1e%d-1e%d: dev %s  dev*L %s'%(k-1,k,np.round(q,4),np.round(q*Lm,3)))
