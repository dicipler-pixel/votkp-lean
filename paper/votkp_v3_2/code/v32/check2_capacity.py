# SCRIPT: LOOP2-CHECK2-KICK-CIRCLE-CAPACITY
# WHY THIS DECIDES IT: N(n,eps) is computed by an exact circular greedy (validated against brute force on small n), on
# the actual points Bloch(U^k psi0) from his own matrices (feed_loop_02.anatomy, exec'd read-only), so the cap is tested
# against the real orbit and not against a model of it.
# DERIVATION OF THE PREDICTED CAP (before the run):
#   Own frame: pass k sits on the circle of Euclidean radius R = sin(phi) (unit Bloch sphere) at azimuth k*theta.
#   Two points with azimuth difference D (circular, in [0,pi]) have Bloch chord 2 R sin(D/2); the Frobenius distance is
#   ||P-Q||_F^2 = |v-w|^2/2 = 2 R^2 sin^2(D/2). Distinguishable iff 2 sin^2(phi) sin^2(D/2) >= eps, i.e.
#   sin(D/2) >= s := sqrt(eps/2)/sin(phi).  If s>1: cap = 1. Else minimum azimuth gap D_min = 2 arcsin(s) and
#   CAP = floor(2 pi / D_min) = floor(pi / arcsin(s)).   (Brief's wording "arcs of chord sqrt(eps)" would be this with
#   the chord measured as |v-w|/sqrt2, the Hilbert-Schmidt chord; the formula above is the one used.)
#   Lab frame: S is a Moebius map of the sphere, so the orbit lies on another circle, of Euclidean radius rho_c (fitted
#   from the points); the same formula with sin(phi) -> rho_c gives CAP_lab; the points are NOT evenly spaced on it.
# KILL LINE (before the run): (i) N(n,eps) > CAP for any n, any case -> kill; (ii) N(2000,eps) < CAP-1 when theta/2pi is
# irrational -> kill; (iii) greedy disagrees with brute force on any small test -> instrument kill.
# Opposite/second setup if (ii) fails: a different starting azimuth (0 -> 1.234 rad) and k=0..n-1 indexing.
import numpy as np, json, itertools
src=open('/home/claude/mixer_v2/feed_loop_02.py').read().split('out={}; k1=k2=k4=0')[0]; exec(src)
from fractions import Fraction
TWO=2*np.pi
def cap_formula(rho,eps):
    s=np.sqrt(eps/2)/rho
    if s>1+1e-15: return 1
    s=min(s,1.0)
    return int(np.floor(np.pi/np.arcsin(s)+1e-9))
def maxset(t,rho,eps):
    """largest set among angles t (on circle radius rho) with 2 rho^2 sin^2(D/2) >= eps pairwise."""
    s=np.sqrt(eps/2)/rho
    if s>1+1e-15: return 1
    s=min(s,1.0); dmin=2*np.arcsin(s)
    t=np.sort(np.mod(t,TWO)); n=len(t); p2=np.concatenate([t,t+TWO]); tol=1e-12
    nxt=np.searchsorted(p2,p2+dmin-tol,side='left')
    idx=np.arange(n); cnt=np.ones(n,int); alive=np.ones(n,bool); lim=p2[:n]+TWO-dmin+tol
    cur=idx.copy()
    for _ in range(n):
        nj=nxt[cur]; ok=alive&(nj<2*n)&(p2[np.minimum(nj,2*n-1)]<=lim)
        if not ok.any(): break
        cnt[ok]+=1; cur=np.where(ok,nj,cur); alive=ok
    return int(cnt.max())
def brute(t,rho,eps):
    s=np.sqrt(eps/2)/rho
    if s>1: return 1
    n=len(t); best=1
    def d(a,b):
        D=abs(a-b)%TWO; D=min(D,TWO-D); return 2*rho*rho*np.sin(D/2)**2
    for mask in range(1,1<<n):
        pts=[t[i] for i in range(n) if mask>>i&1]
        if len(pts)<=best: continue
        if all(d(a,b)>=eps-1e-12 for a,b in itertools.combinations(pts,2)): best=len(pts)
    return best
# ---- instrument validation against brute force
rng=np.random.default_rng(3); bad=0
for trial in range(60):
    t=rng.uniform(0,TWO,14); rho=rng.uniform(0.4,1); eps=rng.choice([0.5,0.1,0.3,0.7])
    if maxset(t,rho,eps)!=brute(t,rho,eps): bad+=1
print('greedy vs brute force mismatches (60 trials, 14 pts):',bad)
def orbit(a,phi,psi0=0.0,k0=1,n=2000):
    ax=a['axis']; d=a['d']; e1=d-np.dot(d,ax)*ax; e1/=np.linalg.norm(e1); e2=np.cross(ax,e1)
    p0=np.cos(phi)*ax+np.sin(phi)*(np.cos(psi0)*e1+np.sin(psi0)*e2)
    P=0.5*(I2+sum(p0[i]*SIG[i] for i in range(3))); w,V=np.linalg.eigh(P); psi=V[:,1]
    own=[];lab=[]; Ut=np.linalg.matrix_power(a['U'],k0); v=Ut@psi
    for k in range(n):
        own.append(bloch(v)); lab.append(bloch(a['S']@v)); v=a['U']@v; v/=np.linalg.norm(v)
    return np.array(own),np.array(lab),ax,e1,e2
def fit_circle(P):
    A=np.hstack([P,-np.ones((len(P),1))]); u,s,vh=np.linalg.svd(A); x=vh[-1]; nrm=np.linalg.norm(x[:3]); n=x[:3]/nrm; h=x[3]/nrm
    if h<0: n,h=-n,-h
    res=np.max(abs(P@n-h)); rho=np.sqrt(max(1-h*h,0)); c=h*n
    e1=P[0]-c; e1-=np.dot(e1,n)*n; e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
    t=np.arctan2((P-c)@e2,(P-c)@e1); return n,h,rho,t,res
NG=sorted(set([10,50,200,1000,2000]+list(range(1,41))+[int(x) for x in np.unique(np.geomspace(40,2000,50).astype(int))]))
def first_reach(t,rho,eps,target,nmax):
    if maxset(t[:nmax],rho,eps)<target: return None
    lo,hi=1,nmax
    while lo<hi:
        mid=(lo+hi)//2
        if maxset(t[:mid],rho,eps)>=target: hi=mid
        else: lo=mid+1
    return lo
results=[]; viol=0; short=0
EPS=[0.5,0.1,0.02,0.005]
for z in [2,3,4,5,5.5,5.8]:
    a=anatomy(float(z)); G2=a['G']**2
    for label,s2 in [('1',1.0),('2G^2',2*G2),('0.301',0.301)]:
        phi=np.arcsin(np.sqrt(min(s2,1.0)))
        own,lab,ax,e1,e2=orbit(a,phi,0.0)
        # own azimuth from data (checks k*theta)
        t_own=np.arctan2(own@e2,own@e1); R_own=np.sqrt(1-(own@ax)**2).mean()
        n_l,h_l,rho_l,t_lab,res_l=fit_circle(lab)
        for eps in EPS:
            capo=cap_formula(np.sin(phi),eps); capl=cap_formula(rho_l,eps)
            No=[maxset(t_own[:n],np.sin(phi),eps) for n in NG]
            Nl=[maxset(t_lab[:n],rho_l,eps) for n in NG]
            vo=max(No)>capo; vl=max(Nl)>capl; viol+=vo+vl
            so=No[-1]<capo-1; sl=Nl[-1]<capl-1; short+=so+sl
            fo=first_reach(t_own,np.sin(phi),eps,capo,2000); fo1=first_reach(t_own,np.sin(phi),eps,capo-1,2000) if capo>1 else None
            fl=first_reach(t_lab,rho_l,eps,capl,2000)
            results.append(dict(z=z,sin2phi=round(float(np.sin(phi)**2),6),label=label,eps=eps,cap_own=capo,N_own_at={n:No[NG.index(n)] for n in (10,50,200,1000,2000)},
               own_first_cap=fo,own_first_cap_minus1=fo1,rho_lab=round(float(rho_l),6),rho_lab_sq=round(float(rho_l**2),6),cap_lab=capl,
               N_lab_at={n:Nl[NG.index(n)] for n in (10,50,200,1000,2000)},lab_first_cap=fl,viol_own=bool(vo),viol_lab=bool(vl),short_own=bool(so),short_lab=bool(sl),circle_fit_resid=float(res_l),own_radius_err=float(abs(R_own-np.sin(phi)))))
for r in results: print(json.dumps(r))
print('VIOLATIONS (N>cap):',viol,' SHORT (N(2000)<cap-1):',short)
json.dump(results,open('check2_capacity.out','w'),indent=1)
