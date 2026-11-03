# SCRIPT: MATTER-DISK-S07  the boundary census on the Smith disk, closed, warm and opened
# WHY THIS CHECK PROVES WHAT IT CLAIMS
# For a one-body correlation matrix C split into a region A and the rest B, block multiplication gives
#   C_A - C_A^2 = (C - C^2)_A + X_A,   X_A = C_AB C_BA.
# In a pure state C^2 = C, so X_A = C_A(1 - C_A): its eigenvalues are nu(1 - nu) = (1 - Gamma^2)/4 with
# Gamma = 1 - 2nu, the section-1 disk coordinate. So the boundary coordinate Gamma_b = sqrt(1 - 4 lambda(X_A))
# is the same point on the disk as |Gamma|, and the count lambda >= eps(1-eps) is the disk window
# |Gamma_b| <= 1 - 2eps. In a warm state C^2 != C: the local mixing term (C - C^2)_A pulls raw Gamma toward
# the centre without any correlation across the cut; X_A keeps only what crosses the cut.
# KILL (written before the run):
#  (a) the identity fails by more than 1e-12 on 32 random Hermitian contractions;
#  (b) disconnected sites C = 0.3 I give a nonzero boundary count;
#  (c) at T = 0 the boundary count differs from the raw count, or |Gamma_b| differs from |Gamma| by > 1e-8;
#  (d) the 128-site ring table (region 64, eps = 0.1) differs from the 3 Nov review table by more than
#      1e-5 in Tr X_A or mutual information, or by any integer in the counts;
#  (e) on the opened non-Hermitian SSH chain (biorthogonal C) C^2 = C or the identity fails by > 1e-8.
import numpy as np
from numpy.linalg import eigvalsh, eigvals, eigh
rng=np.random.default_rng(7)
def blocks(C,nA): return C[:nA,:nA],C[:nA,nA:],C[nA:,:nA]
def ident_err(C,nA):
    CA,CAB,CBA=blocks(C,nA); CC=C@C
    return np.max(np.abs((CA-CA@CA)-((C-CC)[:nA,:nA]+CAB@CBA)))
# (a) random Hermitian contractions 0 <= C <= I
worst=0
for s in range(32):
    n=24; M=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); U,_=np.linalg.qr(M)
    C=U@np.diag(rng.uniform(0,1,n))@U.conj().T; worst=max(worst,ident_err(C,10))
print('(a) block identity, worst error on 32 random Hermitian contractions:',f'{worst:.2e}', 'PASS' if worst<1e-12 else 'FAIL')
eps=0.1; thr=eps*(1-eps)
def counts(C,nA):
    CA,CAB,CBA=blocks(C,nA); nu=eigvalsh(CA); X=CAB@CBA; lam=eigvalsh((X+X.conj().T)/2)
    raw=int(np.sum((nu>=eps)&(nu<=1-eps))); bnd=int(np.sum(lam>=thr))
    return raw,bnd,np.trace(X).real,nu,lam
# (b) disconnected sites
C=0.3*np.eye(64); raw,bnd,tx,_,_=counts(C,32)
print(f'(b) disconnected C=0.3 I, region 32: raw count {raw}, boundary count {bnd}, Tr X_A {tx:.3f}',
      'PASS' if bnd==0 else 'FAIL')
# (c,d) the 128-site antiperiodic ring
def ring(tA,tB,N=128):
    H=np.zeros((N,N))
    for j in range(N):
        t=tA if j%2==0 else tB; s=-1.0 if j==N-1 else 1.0
        H[j,(j+1)%N]=H[(j+1)%N,j]=-t*s
    return H
def thermal(H,T):
    e,V=eigh(H)
    f=(e<0).astype(float) if T==0 else 1/(1+np.exp(e/T))
    return (V*f)@V.T
def Sg(nu):
    nu=np.clip(nu,1e-15,1-1e-15); return -np.sum(nu*np.log(nu)+(1-nu)*np.log(1-nu))
review={('uniform',0):(2,2,0.605657,3.923714),('uniform',0.5):(24,0,0.170835,0.949562),('uniform',2):(64,0,0.027779,0.116547),
        ('gapped alternating',0):(0,0,0.029017,0.345837),('gapped alternating',0.5):(10,0,0.024935,0.188891),('gapped alternating',2):(64,0,0.006484,0.028357)}
okd=True; okc=True
print('(d) ring N=128 antiperiodic, mu=0, region 64, eps=0.1   [ours | 3 Nov review]')
for name,(tA,tB) in [('uniform',(1,1)),('gapped alternating',(1.5,0.5))]:
    H=ring(tA,tB)
    for T in [0,0.5,2]:
        C=thermal(H,T); raw,bnd,tx,nu,lam=counts(C,64)
        MI=Sg(eigvalsh(C[:64,:64]))+Sg(eigvalsh(C[64:,64:]))-Sg(eigvalsh(C))
        r=review[(name,T)]
        good=(raw==r[0])and(bnd==r[1])and abs(tx-r[2])<1e-5 and abs(MI-r[3])<1e-5; okd&=good
        print(f'    {name:19s} T={T:<3} raw {raw:3d}|{r[0]:3d}  boundary {bnd:2d}|{r[1]:2d}  TrX {tx:.6f}|{r[2]:.6f}  MI {MI:.6f}|{r[3]:.6f}  {"MATCH" if good else "DIFFER"}')
        G=np.sort(np.abs(1-2*nu)); Gb=np.sort(np.sqrt(np.clip(1-4*lam,0,1)))
        if T==0:
            dg=np.max(np.abs(G-Gb)); okc&=(raw==bnd) and dg<1e-8
            print(f'        (c) T=0 disk check: max | |Gamma| - |Gamma_b| | = {dg:.1e}')
        else:
            print(f'        warm: levels inside the window by raw Gamma {raw}, by boundary Gamma_b {bnd}; innermost |Gamma| {G[0]:.3f}, innermost |Gamma_b| {Gb[0]:.3f}')
print('(c) T=0 boundary census = original census on the disk:', 'PASS' if okc else 'FAIL')
print('(d) review table reproduced:', 'PASS' if okd else 'DIFFER (see rows)')
# (e) opened matter: biorthogonal C of the non-Hermitian SSH chain
def bands(v,w,u,k):
    Hk=np.array([[1j*u, v+w*np.exp(-1j*k)],[v+w*np.exp(1j*k), -1j*u]])
    ev,R=np.linalg.eig(Hk); o=np.argsort(ev.real); ev,R=ev[o],R[:,o]; L=np.linalg.inv(R).conj().T
    return ev,R,L
def corr(v,w,u,N,Lc):
    ks=2*np.pi*(np.arange(N)+0.5)/N; C=np.zeros((2*Lc,2*Lc),complex)
    for k in ks:
        ev,R,L=bands(v,w,u,k); P=np.outer(R[:,0],L[:,0].conj()); ph=np.exp(1j*k*np.arange(Lc))
        C+=np.kron(np.outer(ph,ph.conj()),P)
    return C/N
oke=True
print('(e) opened chain, full ring of 200 cells (C is the whole system), block of 40 cells')
for v,u,tag in [(0.3,0.5,'opened, inside the disk'),(0.5,0.5,'opened, critical')]:
    C=corr(v,1.0,u,200,200); idem=np.max(np.abs(C@C-C)); ie=ident_err(C,80)
    CA,CAB,CBA=blocks(C,80); pure=np.max(np.abs(CAB@CBA-(CA-CA@CA)))
    oke&=idem<1e-8 and ie<1e-8 and pure<1e-8
    print(f'    v={v} u={u} ({tag}): |C^2 - C| = {idem:.1e}, identity error {ie:.1e}, |X_A - C_A(1-C_A)| = {pure:.1e}')
print('(e) opened matter keeps the boundary identity:', 'PASS' if oke else 'FAIL')
