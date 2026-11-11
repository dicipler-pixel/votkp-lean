# SCRIPT: DRAWING-ROBUST-03
# Solver v2: ROBUST-01 plus (i) two more start families found useful on 8_20 ('walk': consecutive sides related by modest ratios;
# 'lattice': sixth-roots phases) and (ii) complex-conjugation symmetry: the equations exp(z dV/dz)=1 have real coefficients, so
# conj(z) solves them whenever z does; V0(conj z) is evaluated directly (not assumed). This doubles the chance of reaching the
# geometric family (the +vol and -vol copies are found independently by the random search).
import numpy as np
from scipy.optimize import least_squares
import drawing_robust_01 as R
P2=R.P2
def draw_start2(rng,n):
    m=n-1; k=rng.integers(0,5)
    if k<3: return R.draw_start(rng,n)
    if k==3: z=np.cumprod(np.exp(rng.normal(0,0.8,m)+1j*rng.normal(0,0.8,m)))
    else: z=np.exp(1j*np.pi/3*rng.integers(0,6,m))*np.exp(rng.integers(-2,3,m)*0.5+rng.normal(0,0.1,m))
    return np.concatenate([z.real,z.imag])
def solve2(crossings,n,starts=200,seed=1,stop=None,tol=1e-18):
    T=R.terms(crossings); f,jac,split=R.residual_and_jac(T,n); rng=np.random.default_rng(seed); out=[]; bad=0
    for s in range(starts):
        x0=draw_start2(rng,n)
        try: r=least_squares(f,x0,jac=jac,method='trf',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=300)
        except Exception: continue
        if r.cost<tol:
            z=split(r.x)
            if R.good(T,z):
                v=R.V0(T,z,n); out.append((v,z)); zc=np.conj(z); vc=R.V0(T,zc,n); out.append((vc,zc))
                if abs(vc.imag+v.imag)>1e-7 or abs(((vc.real-v.real)+P2/2)%P2-P2/2)>1e-7: bad+=1
        if stop and (s+1)%20==0 and stop([v for v,_ in out]): break
    solve2.conj_mismatch=getattr(solve2,'conj_mismatch',0)+bad
    return out,s+1
