# SCRIPT: DRAWING-ROBUST-01
# Robust, vectorised core for the drawing potential (same potential and placement rule as drawing_poly_01/02):
#   one variable per side; crossing (a,b,c,d) adds Li2(zb/za)-Li2(zb/zc)+Li2(zd/zc)-Li2(zd/za);
#   equations exp(z_k dV/dz_k)=1 (branch-free); V0 = V - sum (z_k dV/dz_k) log z_k.
# Differences from drawing_poly_01: analytic Jacobian, scipy spence for Li2 (checked against mpmath in the self-test),
# mixed start distributions (gaussian at several scales, log-polar), filter against degenerate and run-away solutions.
import numpy as np, warnings
from scipy.special import spence
from scipy.optimize import least_squares
warnings.filterwarnings('ignore')
P2=np.pi**2
def li2(u): return spence(1-u)
def terms(crossings):
    E=[];Pp=[];Q=[]
    for a,b,c,d in crossings:
        for e,p,q in [(1,b,a),(-1,b,c),(1,d,c),(-1,d,a)]: E.append(e);Pp.append(p);Q.append(q)
    return np.array(E,float),np.array(Pp),np.array(Q)
def gvec(T,z,n):
    E,p,q=T; L=np.log(1-z[p]/z[q]); g=np.zeros(n,complex)
    np.add.at(g,p,-E*L); np.add.at(g,q,E*L); return g
def V0(T,z,n):
    E,p,q=T; V=np.sum(E*li2(z[p]/z[q])); return V-np.sum(gvec(T,z,n)*np.log(z))
def residual_and_jac(T,n):
    E,p,q=T
    def split(x): return np.concatenate([[1.0+0j],x[:n-1]+1j*x[n-1:]])
    def f(x):
        z=split(x); h=np.exp(gvec(T,z,n))-1; return np.concatenate([h.real,h.imag])
    def jac(x):
        z=split(x); g=gvec(T,z,n); eg=np.exp(g)
        A=1/(z[q]-z[p]); B=A-1/z[q]
        J=np.zeros((n,n),complex)
        np.add.at(J,(p,p),E*A); np.add.at(J,(p,q),-E*B); np.add.at(J,(q,p),-E*A); np.add.at(J,(q,q),E*B)
        J=(eg[:,None]*J)[:,1:]
        return np.block([[J.real,-J.imag],[J.imag,J.real]])
    return f,jac,split
def good(T,z):
    E,p,q=T; r=z[p]/z[q]
    if not np.all(np.isfinite(r)): return False
    return (np.min(np.minimum(np.abs(r),np.abs(1-r)))>1e-6) and (np.max(np.abs(r))<1e6)
def draw_start(rng,n):
    k=rng.integers(0,3)
    if k==0: s=rng.choice([0.5,1,2,4]); return rng.normal(0,s,2*(n-1))
    if k==1:
        mag=np.exp(rng.uniform(-2.5,2.5,n-1)); ph=rng.uniform(-np.pi,np.pi,n-1); z=mag*np.exp(1j*ph); return np.concatenate([z.real,z.imag])
    mag=np.exp(rng.normal(0,0.7,n-1)); ph=rng.normal(0,1.2,n-1); z=mag*np.exp(1j*ph); return np.concatenate([z.real,z.imag])
def solve(crossings,n,starts=200,seed=1,stop=None,tol=1e-18):
    """returns list of (V0, z). stop: callable(list of V0)->bool checked every 20 starts."""
    T=terms(crossings); f,jac,split=residual_and_jac(T,n); rng=np.random.default_rng(seed); out=[]
    for s in range(starts):
        x0=draw_start(rng,n)
        try: r=least_squares(f,x0,jac=jac,method='trf',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=300)
        except Exception: continue
        if r.cost<tol:
            z=split(r.x)
            if good(T,z): out.append((V0(T,z,n),z))
        if stop and (s+1)%20==0 and stop([v for v,_ in out]): break
    return out,s+1
def key(v): return (v.imag,((-v.real+P2/2)%P2)-P2/2)   # (decay, direction = cs mod pi^2)
def cluster(vals,tol=1e-5):
    """distinct (decay,direction) pairs; direction compared mod pi^2"""
    reps=[]
    for v in vals:
        k=key(v)
        for i,(r,c) in enumerate(reps):
            dd=abs(((k[1]-r[1])+P2/2)%P2-P2/2)
            if abs(k[0]-r[0])<tol and dd<tol: reps[i][1]+=1; break
        else: reps.append([k,1])
    reps.sort(key=lambda t:(-t[0][0],t[0][1])); return reps
def crossings_from_pd(pd):
    # placement rule ('under',0,1): (b,d)=(i,k), (a,c)=(l,j)  ->  (a,b,c,d)=(l,i,j,k)
    labels=sorted({e for X in pd for e in X}); idx={e:t for t,e in enumerate(labels)}
    return [(idx[l],idx[i],idx[j],idx[k]) for i,j,k,l in pd],len(labels)
