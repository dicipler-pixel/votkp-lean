# SCRIPT: HOMFLY-BOOKS-01
# HOMFLY P(v,z), the two-variable parent of Alexander and Jones, read with light running over a TORUS of two phases
# v = e^{i a}, z = e^{i b} instead of one circle. Two books:
#   climb = two-variable Mahler measure m(P) = mean of log|P| over the torus;
#   turn  = mean over a of the signed area swept by P(e^{ia}, e^{ib}) as b runs once round, divided by mean |P|^2.
# Why this tests it: Jones' climb carried volume beyond log det (R^2 0.708 -> 0.810). If HOMFLY holds more than Jones,
# its climb must add to log det + Jones climb; if not, it adds nothing. Also an opposite slice: the Jones line inside
# HOMFLY (v = t^-1, z = t^1/2 - t^-1/2) must reproduce the Jones climb, which checks the parsing.
import numpy as np, sympy as sp, database_knotinfo as d, re, warnings
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
v,z=sp.symbols('v z')
A=np.linspace(0,2*np.pi,97)[:-1]; Va,Zb=np.meshgrid(np.exp(1j*A),np.exp(1j*A),indexing='ij')
th=np.linspace(0,2*np.pi,2049)[:-1]; t=np.exp(1j*th)
rows=[]
for r in d.link_list():
    if not r['homfly_polynomial'] or not r['jones_polynomial_vector']: continue
    try: vol=float(r['volume']); sig=int(r['signature']); det=int(r['determinant'])
    except (ValueError,TypeError): continue
    if vol<=0: continue
    P=sp.sympify(r['homfly_polynomial'].replace('^','**')); f=sp.lambdify((v,z),P,'numpy')
    G=f(Va,Zb); m2=np.mean(np.log(np.abs(G)+1e-300))
    dz=np.roll(G,-1,axis=1)-G; turn=np.mean(0.5*np.sum(G.real*dz.imag-G.imag*dz.real,axis=1))/np.mean(np.abs(G)**2)
    jv=eval(r['jones_polynomial_vector']); J=np.polyval(np.array(jv[2:],float)[::-1],t)*t**jv[0]
    mj=np.mean(np.log(np.abs(J)))
    sl=np.sqrt(t); Jh=f(1/t,sl-1/sl)                                   # Jones line inside HOMFLY (check)
    rows.append((vol,sig,np.log(det),m2,turn,mj,np.mean(np.log(np.abs(Jh)+1e-300))))
R=np.array(rows); vol,sig,ld,m2,tu,mj,mjh=R.T
print('knots',len(R),'| check: Jones climb from HOMFLY slice vs direct, max diff %.2e'%np.max(abs(mjh-mj)))
print('climb (HOMFLY 2-var Mahler) vs volume rho=%.3f  | Jones climb %.3f | log det %.3f'%(spearmanr(m2,vol)[0],spearmanr(mj,vol)[0],spearmanr(ld,vol)[0]))
def r2(cols):
    X=np.column_stack(cols+[np.ones_like(vol)]); c,*_=np.linalg.lstsq(X,vol,rcond=None); p=X@c; return 1-np.sum((vol-p)**2)/np.sum((vol-vol.mean())**2)
print('R^2: log det %.3f | +Jones climb %.3f | +HOMFLY climb %.3f | all three %.3f'%(r2([ld]),r2([ld,mj]),r2([ld,m2]),r2([ld,mj,m2])))
X=np.column_stack([ld,mj,np.ones_like(vol)]); c,*_=np.linalg.lstsq(X,vol,rcond=None); res=vol-X@c
print('HOMFLY climb vs volume left after log det + Jones climb: rho=%.3f'%spearmanr(m2,res)[0])
print('turn (HOMFLY) vs signature rho=%.3f ; |turn| vs |sig| rho=%.3f'%(spearmanr(tu,sig)[0],spearmanr(abs(tu),abs(sig))[0]))
