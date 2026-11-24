# SCRIPT: OPPOSITE-PRIMES-COUSIN-SEXY-01
# a-i all primes p>5, four arms (end digit 1,3,7,9) on tetrahedron vertices in R^3 (sum zero): predicted d bounded/convergent.
# a-ii same arms, four orthogonal axes, SO(1,4): |P| = 1/2.
# b cousin starts (p+4 prime; end digit 3/7/9) and sexy starts (p+6 prime; end digit 1/3/7), three orthogonal arms, |P| = 1/sqrt3.
import numpy as np, math
from owalk import *
N=10**8; P=primes_upto(N)
cuts=[10**k for k in range(3,9)]
Q=P[P>5]; r=np.log(Q[1:]/Q[:-1]); nxt=Q[1:]; arm=np.searchsorted([1,3,7,9],nxt%10)
print('a: all primes, steps',len(r),' r-weighted shares',(np.array([r[arm==s].sum() for s in range(4)])/r.sum()).round(5))
tet=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/math.sqrt(3)
rows=report('a-i all primes, tetrahedron arms (P=0)',nxt,r,arm,tet,cuts+[2*10**8] if False else cuts,np.zeros(3),'(lock column undefined)')
dl=[x['d'] for x in rows]; print(' a-i decade changes of d:',np.round(np.diff(dl),5),' slope last two decades',(rows[-1]['d']-rows[-3]['d'])/(rows[-1]['L']-rows[-3]['L']))
# weighted noise vector sum_n r_n e_{s_n} (should converge since tetra sum is zero)
for x in cuts:
    m=nxt<=x; v=(r[m,None]*tet[arm[m]]).sum(0); print('   first-order vector sum r e_s up to %.0e: %s  |.|=%.5f'%(x,v.round(5),np.linalg.norm(v)))
rows=report('a-ii all primes, 4 orthogonal arms SO(1,4)',nxt,r,arm,np.eye(4),cuts,np.ones(4)/4)
verdict(rows,0.5)
for name,gap,digs in (('b-cousin (p,p+4)',4,[3,7,9]),('b-sexy (p,p+6)',6,[1,3,7])):
    isp=np.zeros(N+7,dtype=bool); isp[P]=True
    S=P[(P>5)&isp[np.minimum(P+gap,N+6)]&(P+gap<=N)]
    rr=np.log(S[1:]/S[:-1]); nx=S[1:]; d10=nx%10
    print(name,'starts',len(S),' end digits seen',np.unique(d10))
    a_=np.searchsorted(digs,d10)
    print('   r-weighted shares',(np.array([rr[a_==s].sum() for s in range(3)])/rr.sum()).round(4))
    rows=report(name,nx,rr,a_,np.eye(3),cuts,np.ones(3)/3)
    verdict(rows,1/math.sqrt(3))
