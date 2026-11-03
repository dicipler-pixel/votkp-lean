# SCRIPT: MATTER-PEEL-02A  constant peel step on the measured c=1/2 entanglement ladder
import numpy as np
def binary_H(x):
    x=np.clip(x,1e-15,1-1e-15); return -(x*np.log(x)+(1-x)*np.log(1-x))
def ladder(h,N,mult=6):
    xi=1/np.log(h); L=int(mult*xi)
    k=2*np.pi*(np.arange(N)+0.5)/N
    e=np.sqrt((h-np.cos(k))**2+np.sin(k)**2); ex=((h-np.cos(k))-1j*np.sin(k))/e
    l=np.arange(-L,L+1); gr=np.array([(ex*np.exp(1j*k*ll)).sum().real/N for ll in l])
    G=np.zeros((2*L,2*L)); ar=np.arange(L)
    for m in range(L):
        G[2*m,1::2]=gr[L-m:L-m+L]; G[2*m+1,0::2]=-gr[L+m-ar]
    nu=np.sort(np.abs(np.linalg.eigvalsh(1j*G)))[::2][::-1]
    p=np.clip((1+nu)/2,0.5,1-1e-15); em=np.sort(np.log(p/(1-p))); em=em[em>1e-10]
    return xi,em
op=lambda u,v:(u+v)/(1+u*v)
for h,N in [(1.05,8192),(1.02,8192),(1.008,16384)]:
    xi,em=ladder(h,N)
    lev=em[::2][:4]        # distinct levels (endpoint doublets): eps0,3eps0,5eps0,7eps0
    e0=lev[0]
    unif=np.max(np.abs(lev/e0-np.array([1,3,5,7])))
    Gm=np.tanh(lev/2); step=np.tanh(e0)
    res=[abs(Gm[j+1]-op(Gm[j],step)) for j in range(3)]
    print(f'xi={xi:7.1f} eps0={e0:.4f} Gamma levels={np.round(Gm,5)} peel step tanh(eps0)={step:.5f}')
    print(f'   ladder uniformity dev {unif:.4f} | max |Gamma_j+1 - (Gamma_j (+) step)| = {max(res):.2e}  (rel to step {max(res)/step:.2e})')
