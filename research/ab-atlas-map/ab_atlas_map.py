# SCRIPT: AB-ATLAS-MAP-01
# Kill lines, written before the run:
#  K1: weak value of the upper-arm projector differs from (1+Gamma)/2, Gamma=(z-1)/(z+1), z=exp(i*Phi), by more than 1e-12
#  K2: B158 bound p0*|Aw|^2 <= <i|P^2|i> is violated anywhere
#  K3: on an odd ring the signless Laplacian spectrum differs from the half-flux (antiperiodic) Laplacian spectrum by more than 1e-12
#  K4: Dirac-type level on the flat torus sqrt(twisted Laplacian min) differs from 2*pi*dist(holonomy, Z^2) (card B8)
#  K5: ring bundle zeta 1/det(I-uB) differs from 1 - 2cos(Phi) u^N + u^(2N)
import numpy as np
rng=np.random.default_rng(7)
w=0;wb=0
for Phi in np.linspace(-3.0,3.0,61):
    i=np.array([1,1])/np.sqrt(2); f=np.array([1,np.exp(1j*Phi)])/np.sqrt(2)
    P=np.diag([1.0,0.0]); ov=np.vdot(f,i); Aw=np.vdot(f,P@i)/ov
    z=np.exp(1j*Phi); G=(z-1)/(z+1)
    w=max(w,abs(Aw-(1+G)/2)); wb=max(wb,abs(ov)**2*abs(Aw)**2-np.vdot(i,P@P@i).real)
print('K1 worst |Aw-(1+Gamma)/2| =',w); print('K2 worst (lhs-rhs), must be <=0 :',wb)
print('   Gamma is pure imaginary on the rim: Gamma = i*tan(Phi/2); example Phi=1 ->',(np.exp(1j)-1)/(np.exp(1j)+1), 1j*np.tan(0.5))
def ring(N,flux,sign=-1):
    L=2*np.eye(N,dtype=complex)
    for k in range(N):
        j=(k+1)%N; ph=np.exp(1j*flux/N)
        L[k,j]+=sign*ph; L[j,k]+=sign*np.conj(ph)
    return np.sort(np.linalg.eigvalsh(L))
for N in (3,5,7,4,6):
    lap0=ring(N,0.0); sgl=ring(N,0.0,sign=+1); half=ring(N,np.pi)
    print('K3 N=%d  |signless - halfflux| = %.2e   |signless - zeroflux| = %.2e   min zeroflux %.4f  min halfflux %.4f'%(N,abs(sgl-half).max(),abs(sgl-lap0).max(),lap0[0],half[0]))
w4=0
for _ in range(2000):
    a,b=rng.random(2)
    n=np.arange(-3,4); lam=min(np.sqrt((x+a)**2+(y+b)**2) for x in n for y in n)*2*np.pi
    d=2*np.pi*np.hypot(min(a,1-a),min(b,1-b)); w4=max(w4,abs(lam-d))
print('K4 worst |level - 2pi*dist| =',w4,'; zero level only at lattice points; at (1/2,0):',2*np.pi*0.5,' at (1/2,1/2):',2*np.pi*np.sqrt(0.5))
w5=0
for N in (3,4,5):
  for Phi in (0.0,0.7,np.pi,2.1):
    # directed edge (non-backtracking) matrix on a ring: 2N directed edges
    B=np.zeros((2*N,2*N),dtype=complex); ph=np.exp(1j*Phi/N)
    for k in range(N):
        B[(k+1)%N,k]=ph            # clockwise edge k -> k+1
        B[N+k,N+(k+1)%N]=np.conj(ph) # anticlockwise
    for u in (0.3,0.6+0.2j):
        w5=max(w5,abs(np.linalg.det(np.eye(2*N)-u*B)-(1-2*np.cos(Phi)*u**N+u**(2*N))))
print('K5 worst |det(I-uB) - (1-2cos(Phi)u^N+u^2N)| =',w5)
