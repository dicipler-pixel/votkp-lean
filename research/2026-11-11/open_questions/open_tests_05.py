# SCRIPT: OPEN-TESTS-05
# Batch tests of open items. Each block states its kill line before computing.
import numpy as np, itertools
from scipy.sparse import diags, lil_matrix
from scipy.sparse.linalg import eigsh

def plaq(N,kap,lam):
    ss=[(p,s-p) for s in range(N+1) for p in range(s+1)]; ix={s:i for i,s in enumerate(ss)}
    H=lil_matrix((len(ss),)*2)
    for i,(p,q) in enumerate(ss):
        H[i,i]=kap*(p*p+q*q+p*q+3*p+3*q)/3+3*lam
        for t in ((p+1,q),(p-1,q+1),(p,q-1),(p,q+1),(p+1,q-1),(p-1,q)):
            j=ix.get(t)
            if j is not None: H[i,j]=-lam/2
    return np.sort(eigsh(H.tocsr(),k=4,which='SA')[0])
def lev(kap,lam,k=4):
    N=min(160,int(14+7*(lam/max(kap,1e-9))**0.5)); return plaq(N,kap,lam)[:k]

print("T1  B75 + Ky Fan on one plaquette, H(kappa) = kappa C2 + lam(3 - Re chi), lam = 8.")
print("    Kill: E0 not concave in kappa, or E0+E1 not concave (both are theorems for H linear in kappa).")
print("    Question: is E1 alone concave? B75 says the middle level need not be.")
lam=8.0; ks=np.linspace(0.2,3.0,57); h=ks[1]-ks[0]
E=np.array([lev(k,lam,3) for k in ks])
d2=lambda f:(f[2:]-2*f[1:-1]+f[:-2])/h**2
print(f"    max d2 E0 = {d2(E[:,0]).max():.3e}   max d2 (E0+E1) = {d2(E[:,0]+E[:,1]).max():.3e}   max d2 E1 = {d2(E[:,1]).max():.3e}   min d2 E1 = {d2(E[:,1]).min():.3e}")
print("T2  Ky Fan secant gap bound on one plaquette: gap(k) >= chord(E0+E1)(k) - 2 E0(k), endpoints k=0.5 and k=2.")
print("    (Uses exact E0 here as the 'upper bound'; it measures how much the chord loses.) Kill: bound > true gap anywhere.")
ka,kb=0.5,2.0; Sa=sum(lev(ka,lam,2)); Sb=sum(lev(kb,lam,2)); bad=0
for k in (0.75,1.0,1.25,1.5,1.75):
    e=lev(k,lam,2); ch=Sa+(Sb-Sa)*(k-ka)/(kb-ka); lb=ch-2*e[0]
    bad+= lb>e[1]-e[0]+1e-9
    print(f"    k={k:.2f} true gap {e[1]-e[0]:.4f}  Ky Fan chord bound {lb:.4f}")
print(f"    violations: {bad}")
print("T3  B160 scaling window, one plaquette (kappa=1): ratio r=(E2-E0)/(E1-E0) vs lam.")
print("    Prediction (oscillator, class functions): singlet levels at 2w (2 quanta), 3w (d_abc), 4w ... so r -> 3/2.")
print("    Kill: r not settling as lam grows.")
for lam in (2,8,32,128,512):
    e=lev(1.0,lam,3); print(f"    lam={lam:5d}  r={(e[2]-e[0])/(e[1]-e[0]):.5f}")
print("T4  B189 boost reading: gap at fixed kappa*lam = 64 across kappa (rapidity 0.5 ln(kappa/lam)).")
print("    Prediction: gap = 2 sqrt(kappa lam) - c*kappa + ...; kill if gap - 2sqrt(kappa lam) is not ~ linear in kappa at small kappa.")
for kap in (0.25,0.5,1,2,4):
    l=64/kap; e=lev(kap,l,2); g=e[1]-e[0]; print(f"    kappa={kap:5.2f} lam={l:7.2f}  gap={g:.5f}  gap-16={g-16:+.5f}  (gap-16)/kappa={(g-16)/kap:+.5f}")
print("T5  U(1) two squares and U(1) 1x3 strip: large-lam gap vs the small-field box gap sqrt(2 lam mu_min).")
print("    E = n^T (B B^T) n (integer plaquette fluxes), magnetic lam sum (1 - cos theta_p). Kill: ratio not -> 1.")
def u1(Bt,lam,M):
    P=Bt.shape[0]; K=Bt
    grid=list(itertools.product(range(-M,M+1),repeat=P)); ix={g:i for i,g in enumerate(grid)}
    H=lil_matrix((len(grid),)*2)
    for i,g in enumerate(grid):
        n=np.array(g); H[i,i]=n@K@n+lam*P
        for p in range(P):
            for s in (1,-1):
                g2=list(g); g2[p]+=s; j=ix.get(tuple(g2))
                if j is not None: H[i,j]=-lam/2
    w=eigsh(H.tocsr(),k=3,which='SA')[0]; return np.sort(w)
for name,K in (('two squares',np.array([[4.,-1],[-1,4]])),('1x3 strip',np.array([[4.,-1,0],[-1,4,-1],[0,-1,4]]))):
    mu=np.linalg.eigvalsh(K).min()
    for lam in (4,16,64,256):
        M=int(6+1.2*lam**0.25*3) if K.shape[0]==2 else int(5+lam**0.25*2)
        w=u1(K,lam,M); g=w[1]-w[0]; print(f"    {name:11s} mu_min={mu:.4f} lam={lam:4d} M={M:2d}  gap={g:.5f}  sqrt(2 lam mu)={np.sqrt(2*lam*mu):.5f}  ratio={g/np.sqrt(2*lam*mu):.5f}")
