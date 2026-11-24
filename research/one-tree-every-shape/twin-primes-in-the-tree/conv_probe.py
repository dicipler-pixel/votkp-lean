# SCRIPT: TWIN-TURN-CONV-PROBE-01
# Probe the mechanism before choosing a proof route:
#  (a) does the heading v_n (direction of the chain's position) freeze? (predicted: change ~ r/sinh d, summable)
#  (b) does the frame carry the mean arm direction m=(1,1,1)/sqrt3 onto the heading (R_n m -> v)? (the attractor that kills the systematic drift)
#  (c) is the increment's projected sum a centred walk: compare sum r_n against sqrt(sum r_n^2)
import numpy as np, math
N=10**8
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
arm=np.searchsorted([1,7,9],T%10)
def boost(u,r):
    B=np.eye(4); c,sh=math.cosh(r),math.sinh(r); B[0,0]=c; B[0,u+1]=B[u+1,0]=sh; B[u+1,u+1]=c; return B
def polar(L):
    v=L[:,0]; g=v[0]; d=math.acosh(g); n=v[1:]/math.sqrt(g*g-1)
    Bst=np.eye(4); Bst[0,0]=g; Bst[0,1:]=Bst[1:,0]=math.sinh(d)*n; Bst[1:,1:]=np.eye(3)+(g-1)*np.outer(n,n)
    return d,n,(np.linalg.inv(Bst)@L)[1:,1:]
m=np.ones(3)/math.sqrt(3)
L=np.eye(4); marks=[10**k for k in range(3,9)]; mi=0; prev=None; s2=0.0
for idx in range(len(T)-1):
    r=math.log(T[idx+1]/T[idx]); s2+=r*r
    L=L@boost(arm[idx+1],r)
    if idx%2000==0:  # re-orthonormalise numerically via polar recomposition
        pass
    if mi<len(marks) and T[idx+1]>=marks[mi]:
        d,n,R=polar(L); Rm=R@m
        ang=math.degrees(math.acos(max(-1,min(1,float(n@Rm)))))
        dv=None if prev is None else math.degrees(math.acos(max(-1,min(1,float(n@prev)))))
        print(f'a>={marks[mi]:.0e}: d={d:.3f}  heading moved {dv} deg since last mark;  angle(heading, R m) = {ang:.3f} deg;  sum r^2 so far = {s2:.5f}')
        prev=n; mi+=1
