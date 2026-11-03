# SCRIPT: MATTER-PEEL-02B3b  signature map with the rank pre-check (degenerate-plane artifact gated)
import numpy as np
exec(open('s03c_metric_raw.py').read().split('def scan')[0])
def classify(v,u,k,tol=1e-9):
    a,b,c=form(v,u,k); d=a*c-b*b; s=a*a+c*c+2*b*b
    if abs(d)<=tol*s: return 0       # rank-one / degenerate: no verdict
    return -1 if d<0 else 1
ks=np.linspace(0.02,2*np.pi-0.02,180); vs=np.linspace(0.05,1.95,96)
for u in (0.0,0.5):
    M=np.array([[classify(v,u,k) if abs(abs(v+w*np.exp(1j*k))**2-u**2)>1e-6 else 0 for k in ks] for v in vs])
    brk=np.array([[abs(v+w*np.exp(1j*k))<u for k in ks] for v in vs])
    print(f'u={u}: Lorentzian {np.mean(M==-1):.3f}  definite {np.mean(M==1):.3f}  degenerate {np.mean(M==0):.3f}')
    if (M==-1).any():
        idx=np.argwhere(M==-1); kk=ks[idx[:,1]]; vv=vs[idx[:,0]]
        print(f'   Lorentzian: k in [{kk.min():.2f},{kk.max():.2f}] v in [{vv.min():.2f},{vv.max():.2f}]; nearest to EP {np.min(np.hypot(kk-np.pi,vv-0.5)):.3f}')
        print(f'   fraction of Lorentzian cells in PT-broken zone {np.mean(brk[M==-1]):.3f}; PT-broken cells Lorentzian {np.mean((M==-1)[brk]) if brk.any() else float("nan"):.3f}')
    np.save(f'sig_u{u}.npy',M)
# radial look at the EP: signature along k=pi as v crosses 0.5, u=0.5
print('along k=pi:')
for v in [0.2,0.4,0.45,0.49,0.51,0.55,0.6,0.8,1.2,1.49,1.51,1.8]:
    a,b,c=form(v,0.5,np.pi); print(f'  v={v:4.2f} a={a:+.3e} b={b:+.3e} c={c:+.3e} det={a*c-b*b:+.3e}')
