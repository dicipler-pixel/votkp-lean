# SCRIPT: QUANTUM-PENDULUM-GAP-02
# U(1) one-link toy: H = kappa*n^2 + lam*(1 - cos theta), charge basis n = -N..N.
# Compares the exact gap E1-E0 with the harmonic sqrt estimate w = sqrt(2*kappa*lam)
# and with the first anharmonic correction w - kappa/2.
# Kill: if gap/w does not tend to 1 as lam grows, the sqrt-lam picture is wrong for this toy.
import numpy as np
N=200; n=np.arange(-N,N+1); kappa=1.0
for lam in [0.5,2,8,32,128,512]:
    H=np.diag(kappa*n**2+lam*1.0)-0.5*lam*(np.eye(2*N+1,k=1)+np.eye(2*N+1,k=-1))
    e=np.linalg.eigvalsh(H); w=np.sqrt(2*kappa*lam)
    print(f"lam={lam:6g}  gap={e[1]-e[0]:.6f}  w={w:.6f}  gap/w={(e[1]-e[0])/w:.6f}  gap-(w-k/2)={e[1]-e[0]-(w-kappa/2):+.2e}")
