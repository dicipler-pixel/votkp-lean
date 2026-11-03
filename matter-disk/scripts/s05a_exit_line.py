# SCRIPT: MATTER-PEEL-03c  locate the disk-exit line v_exit(u) and the rotation at the critical point
import numpy as np
exec(open('nhssh_lib_and_s03a_occupations.py').read().split('w=1.0')[0]); w=1.0
def census(v,u,N=2000,Lc=40,d=1e-9):
    nu=np.linalg.eigvals(corr(v,w,u,N,Lc)).astype(complex)
    keep=(np.abs(nu)>d)&(np.abs(1-nu)>d); nu=nu[keep]
    W=np.log((1-nu)/nu); return np.max(np.abs(W.imag))/np.pi
def vexit(u):
    lo,hi=0.0,1-u      # rotation <1/2 at v=0 (check), critical at v=1-u
    if census(lo,u)>=0.5: return None
    for _ in range(30):
        m=(lo+hi)/2
        if census(m,u)<0.5: lo=m
        else: hi=m
    return (lo+hi)/2
print(' u      v_exit     crit=1-u   gap at exit |v-w|-u   ratio u/(w-v_exit)   rot at critical')
for u in [0.2,0.3,0.4,0.5,0.6,0.7]:
    ve=vexit(u); rc=census(1-u,u)
    if ve is None: print(f' {u:.2f}  rotation already >= 1/2 at v=0; rot at critical {rc:.4f}'); continue
    print(f' {u:.2f}  {ve:.6f}   {1-u:.3f}     {abs(ve-w)-u:.6f}          {u/(w-ve):.6f}          {rc:.5f} pi')
