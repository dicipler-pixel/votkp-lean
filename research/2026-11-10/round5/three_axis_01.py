# SCRIPT: THREE-AXIS-01
# Independent numerical check of the note's three-axis floor: for traceless Hermitian 3x3 X,
#   sum over axes of ||X - R X R^T||_F^2 >= 8 g^2/(1+g^2) ||X||_F^2,  rotations with cos = (1-g^2)/(1+g^2).
# Why this decides it: the smallest ratio over 200,000 random traceless Hermitian X must not fall below the floor, and a
# direct minimisation (smallest eigenvalue of the quadratic form on the 8 real dimensions) must equal it.
# KILL: any sampled ratio below the floor, or the smallest eigenvalue differing from the floor by more than 1e-10.
# Opposite: one axis only must have a zero direction.
import numpy as np
rng=np.random.default_rng(2)
def rots(g):
    c=(1-g*g)/(1+g*g); s=2*g/(1+g*g)
    return [np.array([[1,0,0],[0,c,-s],[0,s,c]]),np.array([[c,0,s],[0,1,0],[-s,0,c]]),np.array([[c,-s,0],[s,c,0],[0,0,1]])]
gm=[np.array(m,dtype=complex) for m in ([[0,1,0],[1,0,0],[0,0,0]],[[0,-1j,0],[1j,0,0],[0,0,0]],[[1,0,0],[0,-1,0],[0,0,0]],[[0,0,1],[0,0,0],[1,0,0]],[[0,0,-1j],[0,0,0],[1j,0,0]],[[0,0,0],[0,0,1],[0,1,0]],[[0,0,0],[0,0,-1j],[0,1j,0]],np.diag([1,1,-2])/np.sqrt(3))]
def form(Rs):
    L=np.zeros((8,8))
    for i,a in enumerate(gm):
        for j,b in enumerate(gm):
            L[i,j]=sum(np.trace((a-R@a@R.T).conj().T@(b-R@b@R.T)).real for R in Rs)/2
    return L
for g,name in ((2/3,'32/13'),(3/4,'72/25'),(1/3,'k=1'),(1/5,'k=2'),(1.0,'g=1')):
    Rs=rots(g); floor=8*g*g/(1+g*g); ev=np.linalg.eigvalsh(form(Rs))
    X=rng.standard_normal((200000,8)); Xm=np.einsum('nk,kij->nij',X,np.array(gm))
    E=sum(np.linalg.norm(Xm-R@Xm@R.T,axis=(1,2))**2 for R in Rs); r=(E/np.linalg.norm(Xm,axis=(1,2))**2).min()
    one=np.linalg.eigvalsh(form(Rs[:1]))
    print('g=%.4f (%s): floor %.8f | smallest eigenvalue %.8f | spectrum %s | smallest sampled ratio %.6f | one axis: smallest eigenvalue %.1e'%(g,name,floor,ev[0],np.round(ev,5).tolist(),r,abs(one[0])))
