# SCRIPT: ONE-PLAQUETTE-PHASE-01
# Single SU(3) plaquette, kappa=1: H = C2 + lam(3 - Re chi), class-function (character) basis, as in the repo's
# su3_character_certificate.matrix_entries (diag C2+3lam, neighbour coupling -lam/2). Float diagonalisation, cutoff N.
# Measures, against lam:
#  (a) gap E1-E0 against the weak-coupling oscillator prediction 2*sqrt(lam) (8 modes, omega=sqrt(lam), class functions
#      need two quanta in a singlet). Kill: gap/(2 sqrt lam) not tending to 1.
#  (b) ground-state weight above the electric cutoffs used by the certificates (C2 > 8, > 40/3): the share of the
#      vacuum that an electric-cutoff retained space leaves outside.
#  (c) convergence in N (kill: E0, E1 move by > 1e-8 between N and N+10).
import numpy as np
def build(N,lam):
    ss=[(p,s-p) for s in range(N+1) for p in range(s+1)]; ix={s:i for i,s in enumerate(ss)}
    H=np.zeros((len(ss),len(ss)))
    for i,(p,q) in enumerate(ss):
        H[i,i]=(p*p+q*q+p*q+3*p+3*q)/3+3*lam
        for t in ((p+1,q),(p-1,q+1),(p,q-1),(p,q+1),(p+1,q-1),(p-1,q)):
            j=ix.get(t)
            if j is not None: H[i,j]=-lam/2
    return ss,H
print(" lam      E0         E1        gap    gap/2sqrt(lam)  w(C2>8)   w(C2>40/3)  <C2>    dN")
for lam in [0.5,1,2,4,8,16,32,64,128,256]:
    N=int(12+6*lam**0.5)
    ss,H=build(N,lam); w,v=np.linalg.eigh(H)
    ss2,H2=build(N+10,lam); w2=np.linalg.eigvalsh(H2)
    c2=np.array([(p*p+q*q+p*q+3*p+3*q)/3 for p,q in ss]); g=v[:,0]**2
    print(f"{lam:5g} {w[0]:10.5f} {w[1]:10.5f} {w[1]-w[0]:8.5f} {((w[1]-w[0])/(2*lam**0.5)):10.5f} {g[c2>8].sum():10.5f} {g[c2>40/3].sum():10.5f} {g@c2:8.3f} {max(abs(w2[0]-w[0]),abs(w2[1]-w[1])):.1e}")
