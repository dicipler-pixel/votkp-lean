# SCRIPT: TWIN-TURN-CONV-CHECKS-01
# Checks for the proof, each written so it can fail:
#  C1 increment law: appending a small boost r along body direction e to L = Boost(D n) R turns the frame by
#     omega = r (w x n) * (1 + O(e^-D) + O(r)), w = R e  (the step is bent toward the heading). Fail if rel. error > 1e-2 at D=6, r=1e-4.
#  C2 endpoint: d = L/sqrt3 + c with c constant. Fail if c drifts by more than 0.01 between 1e5 and 1e9 (harness values).
#  C3 hypothesis H3 numerically: S_s(x) = sum r_n (1[s_n=s] - 1/3) settles (decade changes shrink) up to 1e8.
#  C4 hypothesis H2: sum r_n^2 settles (from the probe: 1.1917, 1.2543, 1.2664, 1.2683, 1.2685).
import numpy as np, math
rng=np.random.default_rng(3)
def boost_vec(v,r):
    v=np.asarray(v,float); v=v/np.linalg.norm(v); B=np.eye(4); c,s=math.cosh(r),math.sinh(r)
    B[0,0]=c; B[0,1:]=B[1:,0]=s*v; B[1:,1:]=np.eye(3)+(c-1)*np.outer(v,v); return B
def polar(L):
    v=L[:,0]; g=v[0]; d=math.acosh(g); n=v[1:]/math.sqrt(g*g-1)
    return d,n,(np.linalg.inv(boost_vec(n,d))@L)[1:,1:]
def rotvec(Rm):
    ang=math.acos(max(-1,min(1,(np.trace(Rm)-1)/2)))
    ax=np.array([Rm[2,1]-Rm[1,2],Rm[0,2]-Rm[2,0],Rm[1,0]-Rm[0,1]])/(2*math.sin(ang)); return ang*ax
worst=0
for _ in range(200):
    n=rng.normal(size=3); n/=np.linalg.norm(n); q=rng.normal(size=4); q/=np.linalg.norm(q)
    a,b,c,d_=q; R=np.array([[1-2*(c*c+d_*d_),2*(b*c-a*d_),2*(b*d_+a*c)],[2*(b*c+a*d_),1-2*(b*b+d_*d_),2*(c*d_-a*b)],[2*(b*d_-a*c),2*(c*d_+a*b),1-2*(b*b+c*c)]])
    R4=np.eye(4); R4[1:,1:]=R; D=6.0; r=1e-4; e=np.eye(3)[rng.integers(3)]
    L=boost_vec(n,D)@R4; L2=L@np.block([[np.eye(1),np.zeros((1,3))],[np.zeros((3,1)),np.eye(3)]])@boost_vec(e,r)
    _,_,R1=polar(L); _,_,R2=polar(L2)
    om=rotvec(R2@R1.T); w=R@e; pred=r*np.cross(w,n)
    if np.linalg.norm(pred)>1e-7: worst=max(worst,np.linalg.norm(om-pred)/np.linalg.norm(pred))
print('C1 worst relative error of omega = r (w x n) over 200 random frames at D=6, r=1e-4: %.2e'%worst,'PASS' if worst<1e-2 else 'FAIL')
for D in (2,4,8):
    n=np.array([0,0,1.]); R4=np.eye(4); e=np.array([1,0,0.]); L=boost_vec(n,D); r=1e-5
    _,_,R2=polar(L@boost_vec(e,r)); print('   D=%d: |omega|/(r sin theta) = %.6f   tanh(D/2) = %.6f'%(D,np.linalg.norm(rotvec(R2))/r,math.tanh(D/2)))
# C2 from harness numbers (cut-off a', d/L)
rows=[(100151,0.5893),(1000037,0.5869),(10000139,0.5853),(100000037,0.5847),(1000000007,0.5833)]
for a,q in rows:
    Lp=math.log(a/11); print('C2 a=%.0e  L=%.3f  d - L/sqrt3 = %.4f'%(a,Lp,q*Lp-Lp/math.sqrt(3)))
# C3 from the sieve
N=10**8
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
arm=np.searchsorted([1,7,9],T%10); r=np.log(T[1:]/T[:-1]); a1=arm[1:]
for k in range(3,9):
    m=T[1:]<=10**k
    S=[float((r[m]*((a1[m]==j)-1/3)).sum()) for j in range(3)]
    print('C3 up to 1e%d: S_i,S_j,S_k = %+.4f %+.4f %+.4f   (path L = %.2f)'%(k,*S,float(r[m].sum())))
