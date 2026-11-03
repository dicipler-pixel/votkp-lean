# SCRIPT: MATTER-PEEL-02B3  signature of the round-trip form on the (k, v) plane, NH SSH
import numpy as np
w=1.0
def Hm(v,u,k): return np.array([[1j*u, v+w*np.exp(-1j*k)],[v+w*np.exp(1j*k), -1j*u]])
def form(v,u,k):
    H=Hm(v,u,k); ev,R=np.linalg.eig(H); o=np.argsort(ev.real); ev,R=ev[o],R[:,o]
    L=np.linalg.inv(R).conj().T
    dk=np.array([[0,-1j*w*np.exp(-1j*k)],[1j*w*np.exp(1j*k),0]]); dv=np.array([[0,1],[1,0]],complex)
    def Q(V): return (L[:,1].conj()@V@R[:,0])*(L[:,0].conj()@V@R[:,1])/(ev[1]-ev[0])**2
    a=Q(dk).real; c=Q(dv).real; b=Q((dk+dv)/np.sqrt(2)).real-(a+c)/2
    return a,b,c
def scan(u):
    ks=np.linspace(0.02,2*np.pi-0.02,180); vs=np.linspace(0.05,1.95,96)
    lor=np.zeros((len(vs),len(ks)),bool); defin=np.zeros_like(lor)
    for i,v in enumerate(vs):
        for j,k in enumerate(ks):
            if abs(v+w*np.exp(1j*k))**2-u**2 < 1e-6: continue   # skip exceptional points themselves
            a,b,c=form(v,u,k); d=a*c-b*b
            lor[i,j]=d<0; defin[i,j]=d>0
    return ks,vs,lor,defin
for u in (0.0,0.5):
    ks,vs,lor,defin=scan(u)
    print(f'u={u}: Lorentzian fraction {lor.mean():.3f}  definite fraction {defin.mean():.3f}')
    if lor.any():
        idx=np.argwhere(lor); kk=ks[idx[:,1]]; vv=vs[idx[:,0]]
        dist=np.min(np.hypot(kk-np.pi, vv-0.5))
        print(f'   Lorentzian cells span k in [{kk.min():.2f},{kk.max():.2f}], v in [{vv.min():.2f},{vv.max():.2f}]; nearest to EP (pi,0.5): {dist:.3f}')
        # PT-broken region |v+w e^{ik}|<u
        brk=np.array([[abs(v+w*np.exp(1j*k))<u for k in ks] for v in vs])
        print(f'   Lorentzian cells inside PT-broken zone: {np.mean(brk[lor]):.3f};  PT-broken cells that are Lorentzian: {np.mean(lor[brk]) if brk.any() else float("nan"):.3f}')
        np.save('lor_u05.npy',lor); np.save('brk_u05.npy',brk)
