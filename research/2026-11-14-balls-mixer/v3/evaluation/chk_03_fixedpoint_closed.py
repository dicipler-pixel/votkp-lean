# SCRIPT: CHK-03-FIXEDPOINT-CLOSED (ij-plane fixed point of the commutator vs closed form rho^2=(1-s)/(1+s), s=sqrt(1-2R))
import numpy as np, math
def boost(u, r):
    u=np.array(u,float); c,s=math.cosh(r),math.sinh(r); B=np.zeros((4,4)); B[0,0]=c; B[0,1:]=s*u; B[1:,0]=s*u
    B[1:,1:]=np.eye(3)+(c-1)*np.outer(u,u); return B
eta=np.diag([1,-1,-1,-1.])
for z in (1.5,2,3,4,5,5.5,5.8):
    r=math.log(z); A=boost([1,0,0],r); B=boost([0,1,0],r); C=A@B@np.linalg.inv(A)@np.linalg.inv(B)
    # solve for fixed point inside ij plane: restrict to coords (t,x,y)
    M=(C-np.eye(4))[np.ix_([0,1,2],[0,1,2])]
    p3=np.linalg.svd(M)[2][-1]; q=p3[0]**2-p3[1]**2-p3[2]**2; p3=p3/math.sqrt(q)
    if p3[0]<0: p3=-p3
    ball=p3[1:]/(1+p3[0]); rad=math.hypot(*ball)
    R=((z-1)/(z+1))**2; s=math.sqrt(1-2*R); rho2=(1-s)/(1+s)
    print("z",z,"plane fixed point radius",round(rad,8)," closed form rho",round(math.sqrt(rho2),8)," diff",abs(rad-math.sqrt(rho2)))
