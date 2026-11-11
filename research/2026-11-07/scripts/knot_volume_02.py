# SCRIPT: KNOT-VOLUME-02
# Opposites for KNOT-VOLUME-01. (a) The turn book may carry handedness rather than volume: test it against |signature|.
# (b) Climb on the Alexander side (Mahler measure of Delta) against volume. (c) Both climbs plus log det together: how much volume do they hold?
import numpy as np, database_knotinfo as d, re
from scipy.stats import spearmanr
th=np.linspace(0,2*np.pi,4097)[:-1]; t=np.exp(1j*th)
def books(v):
    lo,hi,c=v[0],v[1],np.array(v[2:],float); p=np.polyval(c[::-1],t)
    return np.mean(np.log(np.abs(p))), int(np.sum(np.abs(np.roots(c[::-1]))<1-1e-9)), len(c)-1
X=[]
for r in d.link_list():
    if not r['jones_polynomial_vector'] or not r['alexander_polynomial_vector']: continue
    try: vol=float(r['volume']); sig=int(r['signature'])
    except (ValueError,TypeError): continue
    if vol<=0: continue
    mj,ij,sj=books(eval(r['jones_polynomial_vector'])); ma,ia,sa=books(eval(r['alexander_polynomial_vector']))
    X.append((vol,abs(sig),mj,ij/sj,ma,np.log(int(r['determinant'])),int(re.match(r'(\d+)',r['name']).group(1)),ij-sj/2))
vol,asig,mj,ish,ma,ldet,cr,iexc=np.array(X).T
print('n=',len(vol))
print('(a) turn share (Jones roots inside/span) vs |signature|: rho=%.3f'%spearmanr(ish,asig)[0])
print('    roots inside minus half the span vs |signature|:     rho=%.3f'%spearmanr(np.abs(iexc),asig)[0])
print('(b) Alexander climb (Mahler of Delta) vs volume:         rho=%.3f'%spearmanr(ma,vol)[0])
print('    Jones climb vs volume:                                rho=%.3f'%spearmanr(mj,vol)[0])
from numpy.linalg import lstsq
for nm,cols in [('log det',[ldet]),('Jones climb',[mj]),('log det + Jones climb',[ldet,mj]),('log det + Jones climb + Alexander climb',[ldet,mj,ma])]:
    A=np.column_stack(cols+[np.ones_like(vol)]); c,*_=lstsq(A,vol,rcond=None); p=A@c
    print('(c) linear fit %-42s R^2=%.3f  rms=%.3f'%(nm,1-np.sum((vol-p)**2)/np.sum((vol-vol.mean())**2),np.sqrt(np.mean((vol-p)**2))),' coeffs',np.round(c,3))
