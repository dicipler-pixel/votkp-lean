# SCRIPT: MATTER-PEEL-03d  predict the disk-exit line from mean Petermann = 2, then measure
import numpy as np
exec(open('s05a_exit_line.py').read().split("print(' u ")[0])
def P(v,u,k):
    H=np.array([[1j*u, v+w*np.exp(-1j*k)],[v+w*np.exp(1j*k), -1j*u]])
    ev,R=np.linalg.eig(H); o=np.argsort(ev.real); R=R[:,o]; L=np.linalg.inv(R).conj().T
    return np.outer(R[:,0],L[:,0].conj())
ks=2*np.pi*(np.arange(4000)+0.5)/4000
def meanK(v,u): return np.mean([np.linalg.norm(P(v,u,k),2)**2 for k in ks])
def vpred(u):
    lo,hi=0.0,1-u-1e-9
    for _ in range(40):
        m=(lo+hi)/2
        if meanK(m,u)<2: lo=m
        else: hi=m
    return (lo+hi)/2
print(' u     predicted (mean K = 2)   measured census exit   difference')
for u in [0.25,0.45,0.65]:
    vp=vpred(u); vm=vexit(u)
    print(f' {u:.2f}   {vp:.7f}            {vm:.7f}          {vm-vp:+.2e}')
