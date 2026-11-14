# SCRIPT: CHK-02-FIXEDPOINT (fixed point and axis of the commutator at several z; compare with R3 table in feed_loop_01.out)
import numpy as np, math
def boost(u, r):
    u=np.array(u,float); c,s=math.cosh(r),math.sinh(r); B=np.zeros((4,4)); B[0,0]=c; B[0,1:]=s*u; B[1:,0]=s*u
    B[1:,1:]=np.eye(3)+(c-1)*np.outer(u,u); return B
def comm(z):
    r=math.log(z); A=boost([1,0,0],r); B=boost([0,1,0],r); return A@B@np.linalg.inv(A)@np.linalg.inv(B)
eta=np.diag([1,-1,-1,-1.])
for z in (1.5,2,3,4,5,5.5,5.8):
    C=comm(z); N=np.linalg.svd(C-np.eye(4))[2][-2:]   # null space of C-I (2-dim)
    # timelike vector in the null space
    p=None
    for t in np.linspace(0,math.pi,4001):
        v=math.cos(t)*N[0]+math.sin(t)*N[1]; q=v@eta@v
        if q>1e-9: p=v/math.sqrt(q); break
    if p[0]<0: p=-p
    rad=math.tanh(math.acosh(p[0])/2); ball=p[1:]/(1+p[0])
    print("z",z,"fixed point ball coords",np.round(ball,6)," ball radius",round(rad,6)," |C p - p|",np.linalg.norm(C@p-p))
