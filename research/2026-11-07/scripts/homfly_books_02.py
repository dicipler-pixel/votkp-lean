# SCRIPT: HOMFLY-BOOKS-02
# Opposite of HOMFLY-BOOKS-01. The knot-theory surface inside HOMFLY is not |v|=|z|=1: the sl(N) lines are
# v = q^-N... in KnotInfo's convention the Jones line is v = t^-1, z = t^1/2 - t^-1/2 (checked in -01). So the sl(N) line is
# v = t^-(N/2)... use v = t^(-s/2), z = t^1/2 - t^-1/2 with s = N (s=2 Jones; s=0 Alexander, Conway z), t = e^{i theta}.
# (1) climb on each line s = 0..8 vs volume and beyond log det + Jones climb; (2) the whole surface (s continuous 0..8,
# and the 'light surface' v = e^{ia}, z = 2i sin(b/2)) as a 2-D climb.
import numpy as np, sympy as sp, database_knotinfo as d, warnings
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
v,z=sp.symbols('v z')
th=np.linspace(1e-3,2*np.pi-1e-3,1025); t=np.exp(1j*th); sl=np.exp(0.5j*th); Zt=sl-1/sl
A=np.linspace(0,2*np.pi,97)[:-1]; Va,Bb=np.meshgrid(np.exp(1j*A),A,indexing='ij'); Zs=2j*np.sin(Bb/2)
S=np.arange(0,9)
rows=[]
for r in d.link_list():
    if not r['homfly_polynomial']: continue
    try: vol=float(r['volume']); det=int(r['determinant'])
    except (ValueError,TypeError): continue
    if vol<=0: continue
    f=sp.lambdify((v,z),sp.sympify(r['homfly_polynomial'].replace('^','**')),'numpy')
    lines=[np.mean(np.log(np.abs(f(np.exp(-0.5j*s*th),Zt))+1e-300)) for s in S]
    surf=np.mean(np.log(np.abs(f(Va,Zs))+1e-300))
    rows.append([vol,np.log(det),surf]+lines)
R=np.array(rows); vol,ld,surf=R[:,0],R[:,1],R[:,2]; L=R[:,3:]
def r2(cols):
    X=np.column_stack(cols+[np.ones_like(vol)]); c,*_=np.linalg.lstsq(X,vol,rcond=None); p=X@c; return 1-np.sum((vol-p)**2)/np.sum((vol-vol.mean())**2)
jones=L[:,2]
print('knots',len(R))
print(' sl(N) line  climb vs vol   R^2 with log det   R^2 with log det + Jones climb')
for i,s in enumerate(S): print('   N=%d        %+.3f          %.3f             %.3f'%(s,spearmanr(L[:,i],vol)[0],r2([ld,L[:,i]]),r2([ld,jones,L[:,i]])))
print('all lines N=0..8 together with log det: R^2 %.3f'%r2([ld]+[L[:,i] for i in range(len(S))]))
print('light surface (v on circle, z = 2i sin(b/2)) climb vs vol rho=%.3f ; R^2 with log det %.3f ; with log det + Jones %.3f'%(spearmanr(surf,vol)[0],r2([ld,surf]),r2([ld,jones,surf])))
