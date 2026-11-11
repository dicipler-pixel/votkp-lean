# SCRIPT: B189-CONSTANT-06
# One plaquette, H = kappa C2 + lam (3 - Re chi). Is c in gap = 2 sqrt(kappa lam) - c kappa + ... a constant, or does it
# depend on kappa*lam? Run kappa*lam = 16, 64, 256 at kappa -> 0. Kill (for "constant"): the small-kappa limits of
# c differ by more than 0.02 between the three values of kappa*lam.
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh
def gap(kap,lam,N):
    ss=[(p,s-p) for s in range(N+1) for p in range(s+1)]; ix={s:i for i,s in enumerate(ss)}
    H=lil_matrix((len(ss),)*2)
    for i,(p,q) in enumerate(ss):
        H[i,i]=kap*(p*p+q*q+p*q+3*p+3*q)/3+3*lam
        for t in ((p+1,q),(p-1,q+1),(p,q-1),(p,q+1),(p+1,q-1),(p-1,q)):
            j=ix.get(t)
            if j is not None: H[i,j]=-lam/2
    w=np.sort(eigsh(H.tocsr(),k=2,which='SA')[0]); return w[1]-w[0]
for P in (16,64,256):
    print(f"kappa*lam = {P}")
    for kap in (0.0625,0.125,0.25,0.5,1,2):
        lam=P/kap; N=int(14+7*(lam/kap)**0.5*0.5+10); N=min(N,220)
        g=gap(kap,lam,N); g2=gap(kap,lam,N+20)
        print(f"   kappa={kap:7.4f} lam={lam:8.2f} N={N:3d}  gap={g:.6f}  c=(2sqrt(P)-gap)/kappa={(2*P**0.5-g)/kap:.5f}  dN={abs(g-g2):.1e}")
