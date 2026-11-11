# SCRIPT: KNOT-VOLUME-03
# Second opposite for the turn book: count the turn not by roots, but by the signed area the Jones string sweeps
# (the geometric part, as on the Smith disk), scaled by the string's own size (mean |V|^2). Test against volume and |signature|,
# then against the volume left after log det and the Jones climb.
import numpy as np, database_knotinfo as d
from scipy.stats import spearmanr
th=np.linspace(0,2*np.pi,4097)[:-1]; t=np.exp(1j*th)
X=[]
for r in d.link_list():
    if not r['jones_polynomial_vector']: continue
    try: vol=float(r['volume']); sig=int(r['signature'])
    except (ValueError,TypeError): continue
    if vol<=0: continue
    v=eval(r['jones_polynomial_vector']); c=np.array(v[2:],float); p=np.polyval(c[::-1],t)*t**v[0]
    dz=np.roll(p,-1)-p; area=0.5*np.sum(p.real*dz.imag-p.imag*dz.real)
    X.append((vol,abs(sig),area/np.mean(np.abs(p)**2),np.mean(np.log(np.abs(p))),np.log(int(r['determinant']))))
vol,asig,ta,mj,ldet=np.array(X).T
print('turn as swept area / size:  vs volume rho=%.3f   vs |signature| rho=%.3f'%(spearmanr(ta,vol)[0],spearmanr(np.abs(ta),asig)[0]))
A=np.column_stack([ldet,mj,np.ones_like(vol)]); c,*_=np.linalg.lstsq(A,vol,rcond=None); res=vol-A@c
print('vs volume left after log det + climb: rho=%.3f'%spearmanr(ta,res)[0])
