# SCRIPT: BRANCH-CUT-01c
# Opposed fusion K # mirror(K): scalar signature is 0. Does the positive projector still carry K's hand?
# Probe Z = +1 on K's block, -1 on the mirror block. Read Tr(P+ Z) against the signature of K alone.
import numpy as np
def seifert_T2(n):
    m=n-1; V=np.zeros((m,m))
    for i in range(m): V[i,i]=-1
    for i in range(m-1): V[i+1,i]=1
    return V
knots={'3_1':seifert_T2(3),'5_1':seifert_T2(5),'7_1':seifert_T2(7),'4_1':np.array([[-1.,1.],[0.,1.]])}
def H(V,w): return (1-w)*V+(1-np.conj(w))*V.T
def bsum(A,B):
    n,m=A.shape[0],B.shape[0]; C=np.zeros((n+m,n+m)); C[:n,:n]=A; C[n:,n:]=B; return C
grid=np.linspace(0.01,np.pi-0.01,400)
for k,V in knots.items():
    n=V.shape[0]; opp=bsum(V,-V.T); Z=np.diag([1.]*n+[-1.]*n)
    agree=0; tot=0; scal=set()
    for a in grid:
        w=np.exp(1j*a); e,U=np.linalg.eigh(H(opp,w))
        if np.min(np.abs(e))<1e-9: continue
        Q=U[:,e>0]; P=Q@Q.conj().T
        probe=round(float(np.real(np.trace(P@Z))))
        eK=np.linalg.eigvalsh(H(V,w)); sK=int(np.sum(eK>0)-np.sum(eK<0))
        scal.add(int(np.sum(e>0)-np.sum(e<0)))
        tot+=1; agree+= (probe==sK)
    print(k,' scalar signature of the opposed fusion at all phases:',sorted(scal),' | projector probe Tr(P+ Z) = signature of K at',agree,'of',tot,'phases')
