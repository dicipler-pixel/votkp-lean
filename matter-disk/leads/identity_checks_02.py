# SCRIPT: LEADS_IDENTITY_CHECKS_02
import numpy as np
rng=np.random.default_rng(3)
# Thomas complexified: Re theta = pi/2 iff |Gamma|=1
for r in [0.5,0.9,1.0,1.1,1.5]:
    g=r*np.exp(1j*rng.uniform(-1,1)); th=2*np.arctan(g*g); print('|Gamma|',r,'Re theta/(pi/2)',th.real/(np.pi/2))
# E-/E+ constant sensitivity on random graph D+A
def rand_unitary(r):
    X=rng.normal(size=(r,r))+1j*rng.normal(size=(r,r)); Q,_=np.linalg.qr(X); return Q
n,r=4,2
edges=[(0,1),(1,2),(2,3),(3,0),(0,2)]
H=np.zeros((n*r,n*r),complex)
for i in range(n):
    X=rng.normal(size=(r,r))+1j*rng.normal(size=(r,r)); H[i*r:(i+1)*r,i*r:(i+1)*r]=X+X.conj().T
for (i,j) in edges:
    U=rand_unitary(r); H[i*r:(i+1)*r,j*r:(j+1)*r]=U; H[j*r:(j+1)*r,i*r:(i+1)*r]=-U.conj().T
def books(H): 
    Hs=H.conj().T
    return np.linalg.norm(H@Hs-Hs@H)**2/8, np.linalg.norm(H@H-Hs@Hs)**2/8
print('books H',books(H)); print('books H+0.7I',books(H+0.7*np.eye(n*r)))
Em,Ep=books(H)
D=np.zeros_like(H);A=H.copy()
for i in range(n): D[i*r:(i+1)*r,i*r:(i+1)*r]=H[i*r:(i+1)*r,i*r:(i+1)*r]; A[i*r:(i+1)*r,i*r:(i+1)*r]=0
print('budget',Em+Ep,2*np.linalg.norm(D@A)**2, 'diff',Em-Ep,2*np.trace(D@A@D@A).real)
# Bloch 4 det g = Omega^2 : g = 1/4(dth^2+sin^2 dph^2), Omega_{th,ph}=1/2 sin th
th=0.9; print(4*(0.25*0.25*np.sin(th)**2),(0.5*np.sin(th))**2)
# Fermi-Dirac ladder
for L in [1,2,3]:
    z=5**L; nu=1/(1+z); print(L,'Gamma_L',(z-1)/(z+1),'1-2nFD',1-2*nu)
