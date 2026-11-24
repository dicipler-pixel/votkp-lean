# SCRIPT: GAPS-RECENTER-SCAN-01
# Recenter the k = 39 setup before judging it.
# Free settings scanned:
#   - the hybrid lambda (no rebuild needed);
#   - the profile g = w/(1 + slow t) + (1 - w)/(1 + fast t) (one rebuild per setting).
# Run on the coarse grid N = 12288. Its best quotient sits 0.00147 below the full grid at both
# k = 40 and k = 39, so differences carry over.
# KILL (written before the run): recentering fails to rescue k = 39 if no setting reaches a coarse
# best quotient of 0.99871 (full-grid equivalent 1.00018, the loss charge seen at k = 40).
import numpy as np, subprocess, sys, os
from fractions import Fraction as F
rs=2624989/10**7; m0=49999/50000; K=17/50
def best(A,B):
    d=1/np.sqrt(np.diag(A)); As=A*d[:,None]*d[None,:]; Bs=B*d[:,None]*d[None,:]
    w,V=np.linalg.eigh(As); keep=w>w.max()*1e-14; W=V[:,keep]/np.sqrt(w[keep])
    return rs*np.linalg.eigvalsh(W.T@Bs@W)[-1]
def lam_scan(path):
    G=np.load(path); A,B0,Bp,Bt=G
    out=[]
    for lam in [1/1000,1/500,1/250,1/125,1/60,1/30,1/15,0.1,0.2,0.4,0.7,0.95]:
        a=m0*m0-m0*lam; b=(1-m0/lam)*(1-m0)*K
        if 1-4*rs*abs(b)<=0: continue
        out.append((best(A,B0+(a+b)*Bp+b*Bt),lam))
    return max(out),out
mixes=[(0.105,0.01,181.4),(0.105,0.01,90),(0.105,0.01,360),(0.05,0.01,181.4),(0.2,0.01,181.4),
       (0.105,0.5,181.4),(0.105,2,181.4),(0.3,0.5,60),(0.0,0.01,181.4),(1.0,0.01,181.4)]
for mix in mixes:
    tag='_'.join(f'{v:g}' for v in mix); path=f'gram3_k39_N12288_{tag}.npy'
    if not os.path.exists(path):
        subprocess.run([sys.executable,'capgram2.py','39','12288',','.join(map(str,mix))],check=True,capture_output=True)
    (q,lam),_=lam_scan(path)
    print('mix w=%g slow=%g fast=%g  best quotient %.6f at lambda %.4g   %s'%(*mix,q,lam,'REACHES 0.99871' if q>=0.99871 else ''),flush=True)
