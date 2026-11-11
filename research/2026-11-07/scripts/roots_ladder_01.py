# SCRIPT: ROOTS-LADDER-01
# Task 3: volume ladder. For every hyperbolic knot with crossing number <= MAXC (argv[1], default 7), find ALL solutions of the gluing equations
# (n-1 edge equations + meridian completeness; damped Newton from 3000 random starts, as ROOTS-DISK-02), then WITHIN each knot rank the solutions by
# S = sum |G_j|^2 (distance from the vacuum on the Smith disk) and by volume V = sum D(z_j). Prediction (bowl law): V is a decreasing function of S, so the
# Spearman correlation inside each knot is -1 and the geometric solution (the one snappy returns) is the argmin of S.
# Why this tests it: ROOTS-DISK-02 only checked the top of the ladder (geometric = nearest vacuum). Here every rung is scored. Kill condition: any knot
# with Spearman > -1 (ladder break) or geometric != argmin S is reported with its numbers.
import numpy as np, snappy, warnings, re, database_knotinfo as d, sys, json
from scipy.special import spence
from scipy.stats import spearmanr
from multiprocessing import Pool
warnings.filterwarnings('ignore')
w=np.exp(1j*np.pi/3)
def D(z): z=np.asarray(z,complex); return np.imag(spence(1-z))+np.angle(1-z)*np.log(abs(z))
def solve_all(M,starts=3000,seed=0):
    g=M.gluing_equations('rect'); A=np.array([r[0] for r in g],float); B=np.array([r[1] for r in g],float); c=np.array([r[2] for r in g],complex)
    n=A.shape[1]; rows=list(range(n-1))+[n]
    A,B,c=A[rows],B[rows],c[rows]
    def F(z): return np.exp(A@np.log(z)+B@np.log(1-z))-c
    def J(z):
        f=np.exp(A@np.log(z)+B@np.log(1-z)); return f[:,None]*(A/z[None,:]-B/(1-z)[None,:])
    rng=np.random.default_rng(seed); sols=[]
    for _ in range(starts):
        sc=rng.choice([0.3,1,3,10]); z=rng.normal(0.5,sc,n)+1j*rng.normal(0,sc,n)
        for it in range(120):
            try: dz=np.linalg.solve(J(z),-F(z))
            except np.linalg.LinAlgError: break
            st=min(1.0,0.5/max(1e-12,np.max(abs(dz))/max(1,np.max(abs(z))))); z=z+st*dz
            if np.max(abs(dz))<1e-13: break
        if np.all(np.isfinite(z)) and np.max(abs(F(z)))<1e-9 and np.min(abs(z))>1e-6 and np.min(abs(1-z))>1e-6:
            if not any(np.max(abs(z-s))<1e-7 for s in sols): sols.append(z)
    return sols
def work(nm):
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': return None
    zg=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); sols=solve_all(M)
    if not any(np.max(abs(s-zg))<1e-6 for s in sols): sols.append(zg)
    S=np.array([np.sum(abs((s-w)/(s-np.conj(w)))**2) for s in sols]); V=np.array([np.sum(D(s)) for s in sols])
    gi=[i for i,s in enumerate(sols) if np.max(abs(s-zg))<1e-6][0]
    return dict(name=nm,n=len(zg),nsol=len(sols),S=S.tolist(),V=V.tolist(),geo=gi)
if __name__=='__main__':
    MAXC=int(sys.argv[1]) if len(sys.argv)>1 else 7
    names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=MAXC]
    with Pool() as p: res=[r for r in p.map(work,names,chunksize=1) if r]
    json.dump(res,open('/home/claude/votkp_research/roots_ladder_01_c%d.json'%MAXC,'w'))
    print('hyperbolic knots (<=%d crossings): %d'%(MAXC,len(res)))
    ns=[r['nsol'] for r in res]; print('solutions per knot: min %d median %d max %d'%(min(ns),int(np.median(ns)),max(ns)))
    near=sum(1 for r in res if int(np.argmin(r['S']))==r['geo']); big=sum(1 for r in res if int(np.argmax(r['V']))==r['geo'])
    print('geometric = nearest vacuum (argmin S): %d of %d ; geometric = max volume: %d of %d'%(near,len(res),big,len(res)))
    rho=[];brk=[]
    for r in res:
        if r['nsol']>=3:
            s=spearmanr(r['S'],r['V'])[0]; rho.append((s,r['name'],r['nsol']))
            if s>-1+1e-9: brk.append((r['name'],round(s,4),r['nsol']))
    rr=np.array([x[0] for x in rho]); print('knots with >=3 solutions: %d ; Spearman(S,V): min %.4f median %.4f max %.4f ; exactly -1: %d'%(len(rr),rr.min(),np.median(rr),rr.max(),np.sum(rr<-1+1e-9)))
    for lo,hi in [(-1.0001,-0.9999),(-0.9999,-0.95),(-0.95,-0.8),(-0.8,0),(0,1.01)]:
        print('   Spearman in (%.3f,%.3f]: %d knots'%(lo,hi,np.sum((rr>lo)&(rr<=hi))))
    print('ladder breaks (Spearman > -1):',brk[:40])
    bad=[(r['name'],r['nsol'],round(r['S'][r['geo']],3),round(min(r['S']),3)) for r in res if int(np.argmin(r['S']))!=r['geo']]
    print('geometric != nearest vacuum:',bad)
    # pooled: S vs V over all solutions
    allS=np.concatenate([r['S'] for r in res]); allV=np.concatenate([r['V'] for r in res])
    print('pooled over all solutions of all knots: Spearman(S,V)=%.3f'%spearmanr(allS,allV)[0])
    # table of the first knots
    print('\nknot  n nsol  geometric(S,V)  | next rung up (S,V) | Spearman')
    for r in res[:12]:
        o=np.argsort(r['S']); print('%-5s %2d %3d  (%.3f, %.3f)  | %s | %s'%(r['name'],r['n'],r['nsol'],r['S'][r['geo']],r['V'][r['geo']],[(round(r['S'][i],2),round(r['V'][i],2)) for i in o[1:4]],round(spearmanr(r['S'],r['V'])[0],3) if r['nsol']>=3 else 'n/a'))
