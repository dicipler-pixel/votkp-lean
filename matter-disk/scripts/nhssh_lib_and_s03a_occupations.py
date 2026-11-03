# SCRIPT: MATTER-PEEL-02B  opened matter: NH SSH  h(k)=[[iu, v+w e^{-ik}],[v+w e^{ik}, -iu]]
import numpy as np
def bands(v,w,u,k):
    H=np.array([[1j*u, v+w*np.exp(-1j*k)],[v+w*np.exp(1j*k), -1j*u]])
    ev,R=np.linalg.eig(H); o=np.argsort(ev.real); ev,R=ev[o],R[:,o]
    L=np.linalg.inv(R).conj().T          # columns: left vectors with <L_m|R_n>=delta
    return ev,R,L
def corr(v,w,u,N,Lc):
    ks=2*np.pi*(np.arange(N)+0.5)/N
    C=np.zeros((2*Lc,2*Lc),complex)
    for k in ks:
        ev,R,L=bands(v,w,u,k)
        P=np.outer(R[:,0],L[:,0].conj())   # occupied lower band, biorthogonal projector
        ph=np.exp(1j*k*np.arange(Lc))
        C+=np.kron(np.outer(ph,ph.conj()),P)
    return C/N
def S_of(nu):
    nu=nu.astype(complex); return -np.sum(nu*np.log(nu)+(1-nu)*np.log(1-nu))
w=1.0
print('B1/B2: biorthogonal occupations -> Gamma=1-2nu, entropy slope')
for (v,u,tag) in [(0.5,0.0,'Hermitian gapped control'),(1.0,0.0,'Hermitian critical control (c=1)'),(0.5,0.3,'NH gapped (|v-w|>u)'),(0.5,0.5,'NH critical |v-w|=u (EP)')]:
    N=2000; Ls=[20,40,80,160]; Ss=[]; worst=0; maxim=0
    for Lc in Ls:
        nu=np.linalg.eigvals(corr(v,w,u,N,Lc)); G=1-2*nu
        worst=max(worst,np.max(np.abs(G))); maxim=max(maxim,np.max(np.abs(G.imag)))
        Ss.append(S_of(nu))
    x=np.log(N/np.pi*np.sin(np.pi*np.array(Ls)/N))
    sl=np.polyfit(x,np.real(Ss),1)[0]
    print(f'  {tag:36s} max|Gamma|={worst:9.3e} max|Im Gamma|={maxim:8.2e}  c=3*slope={3*sl:+.3f}  S(Im)~{np.max(np.abs(np.imag(Ss))):.1e}')
