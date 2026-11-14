# SCRIPT: CHK-10-UNEQUAL (T15 pair law: g, turn 4acos g / run 4acosh g from the 4x4 commutator trace; whole-number g=1 search; sense flip on swap)
import numpy as np, math
from mpmath import mp, mpf, matrix, acos, acosh, sqrt, cosh, sinh, pi
mp.dps=40
def boostm(u,r):
    c,s=mp.cosh(r),mp.sinh(r); B=mp.zeros(4,4); B[0,0]=c
    for i in range(3): B[0,i+1]=s*u[i]; B[i+1,0]=s*u[i]
    for i in range(3):
        for j in range(3): B[i+1,j+1]=(1 if i==j else 0)+(c-1)*u[i]*u[j]
    return B
def g(z1,z2): return (z1-1)*(z2-1)/(4*mp.sqrt(z1*z2))
worst=0
for z1,z2 in [(2,3),(3,5),(3,7),(4,7),(5,5),(5,7),(7,7),(4,11),(3,13),(mpf('2.8900536383'),5),(4,9),(6,6)]:
    z1=mpf(z1); z2=mpf(z2)
    A=boostm([1,0,0],mp.log(z1)); B=boostm([0,1,0],mp.log(z2)); C=A*B*A**-1*B**-1
    tr=sum(C[i,i] for i in range(4)); gg=g(z1,z2)
    pred=(2-4*gg**2)**2
    if gg<1:
        phi=mp.acos((tr-2)/2); alpha=mp.acos(gg); fold=(4*alpha*180/mp.pi)%360; fold=min(fold,360-fold)
        print(float(z1),float(z2),"g",float(gg),"turn",float(phi*180/mp.pi),"4acos g folded",float(fold),"tr-pred",float(abs(tr-pred)))
        worst=max(worst,abs(phi*180/mp.pi-fold))
    else:
        tau=mp.acosh((tr-2)/2); print(float(z1),float(z2),"g",float(gg),"run",float(tau),"4acosh g",float(4*mp.acosh(gg)) if gg>1 else 0.0,"tr-pred",float(abs(tr-pred)))
print("worst turn mismatch (deg)",float(worst))
hits=[(a,b) for a in range(2,301) for b in range(a,301) if (a-1)**2*(b-1)**2==16*a*b]
h2=[(a,b) for a in range(2,301) for b in range(a,301) if (a-1)**2*(b-1)**2==4*a*b]
h3=[(a,b) for a in range(2,301) for b in range(a,301) if (a-1)**2*(b-1)**2==8*a*b]
print("whole-number g=1:",hits," g=1/2:",h2," g^2=1/2:",h3)
# sense flip: rotation about fixed point; sign of axis dot k for C and C' = B A B^-1 A^-1 (z=5,5)
def axis(C):
    Cn=np.array(C.tolist(),dtype=float); N=np.linalg.svd(Cn-np.eye(4))[2][-2:]
    eta=np.diag([1,-1,-1,-1.]); p=None
    # fixed point in ij plane
    M=(Cn-np.eye(4))[np.ix_([0,1,2],[0,1,2])]; p3=np.linalg.svd(M)[2][-1]; q=p3[0]**2-p3[1]**2-p3[2]**2; p3=p3/math.sqrt(q)
    if p3[0]<0: p3=-p3
    p=np.array([p3[0],p3[1],p3[2],0.0])
    # rotation sense: image of a tangent vector e=(0,x?,..) compute orientation via det of [p, v, Cv, k] with v tangent in plane
    v=np.array([0,-p3[2],p3[1],0.0]); v=v-(v@eta@p)*p/(p@eta@p) if abs(v@eta@p)>1e-12 else v
    w=Cn@np.array([p[0]+0.0, *(p[1:]+1e-3*v[1:])])-p  # small displacement mapped
    return np.sign(np.linalg.det(np.array([p, v, w-0*v, [0,0,0,1.0]])))
for z in (5,3):
    r=mp.log(z); A=boostm([1,0,0],r); B=boostm([0,1,0],r)
    C1=A*B*A**-1*B**-1; C2=B*A*B**-1*A**-1
    print("z",z,"sense(AB A^-1 B^-1)",axis(C1)," sense(BA B^-1 A^-1)",axis(C2))
