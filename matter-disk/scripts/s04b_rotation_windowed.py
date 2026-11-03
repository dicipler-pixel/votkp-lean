# SCRIPT: MATTER-PEEL-03b  windowed census rotation and disk exit vs block size
import numpy as np
exec(open('nhssh_lib_and_s03a_occupations.py').read().split('w=1.0')[0]); w=1.0
def census(v,u,N,Lc,d=1e-9):
    nu=np.linalg.eigvals(corr(v,w,u,N,Lc)).astype(complex)
    keep=(np.abs(nu)>d)&(np.abs(1-nu)>d); nu=nu[keep]
    W=np.log((1-nu)/nu); G=1-2*nu
    return (np.max(np.abs(W.imag))/np.pi if len(nu) else 0.0), np.max(np.abs(G)) if len(nu) else 0.0
u=0.5
for (N,Lc) in [(2000,40),(2000,80),(4000,160)]:
    print(f'block Lc={Lc}, ring N={N}')
    for v in [0.3,0.4,0.45,0.47,0.48,0.49,0.495,0.5,1.505,1.51,1.52,1.55]:
        r,g=census(v,u,N,Lc)
        print(f'   v={v:5.3f}  max rotation={r:.4f} pi   max|Gamma|={g:.4f} {"OUT" if g>1+1e-6 else "in"}')
