# SCRIPT: ROOTS-LADDER-02
# Task 3 refinement of ROOTS-LADDER-01 (same root finder). Adds per-solution structure: n_out = number of tetrahedra with |G|>1 (reversed orientation, Im z<0),
# flat = all shapes real (volume 0, on the rim), and an orientation-aware law: each piece contributes eps*[V0 - k2*|Gt|^2] with Gt = G inside the disk,
# 1/conj(G) outside (mirror piece), eps=+1 inside / -1 outside. Scores per knot: Spearman(S,V) [raw sum|G|^2, ties handled], Spearman(Vlaw,V), max |Vlaw-V|,
# and counts of rung inversions (pairs with S_i<S_j but V_i<V_j-1e-6), classified by whether the lower-S member is flat / has n_out>0.
# Why: ROOTS-LADDER-01 showed breaks only below the geometric rung; this tells whether they come from the rim (flat) solutions and mixed-orientation solutions
# (where |G|^2 alone cannot see orientation), i.e. whether an orientation-aware law restores the ladder.
import numpy as np, snappy, warnings, re, database_knotinfo as d, sys, json
sys.path.insert(0,'/home/claude/votkp_research')
from roots_ladder_01 import solve_all, D, w
from scipy.stats import spearmanr
from multiprocessing import Pool
V0=1.0149416064096536; k2=3*np.sqrt(3)/4
def work(nm):
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': return None
    zg=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); sols=solve_all(M)
    if not any(np.max(abs(s-zg))<1e-6 for s in sols): sols.append(zg)
    out=[]
    for s in sols:
        G=(s-w)/(s-np.conj(w)); a=abs(G); inside=a<1-1e-9; outside=a>1+1e-9
        Gt=np.where(outside,1/np.conj(G),G); eps=np.where(outside,-1.0,1.0); eps=np.where(abs(a-1)<=1e-9,0.0,eps)
        out.append(dict(S=float(np.sum(a**2)),V=float(np.sum(D(s))),Vlaw=float(np.sum(eps*(V0-k2*abs(Gt)**2))),nout=int(np.sum(outside)),flat=bool(np.all(abs(s.imag)<1e-9)),
                        geo=bool(np.max(abs(s-zg))<1e-6)))
    return dict(name=nm,n=len(zg),sols=out)
if __name__=='__main__':
    MAXC=int(sys.argv[1]) if len(sys.argv)>1 else 7
    names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=MAXC]
    with Pool() as p: res=[r for r in p.map(work,names,chunksize=1) if r]
    json.dump(res,open('/home/claude/votkp_research/roots_ladder_02_c%d.json'%MAXC,'w'))
    print('hyperbolic knots (<=%d crossings): %d ; total solutions %d'%(MAXC,len(res),sum(len(r['sols']) for r in res)))
    geo_ok=sum(1 for r in res if min(r['sols'],key=lambda x:x['S'])['geo']); print('geometric = argmin S: %d of %d ; = argmax V: %d'%(geo_ok,len(res),sum(1 for r in res if max(r['sols'],key=lambda x:x['V'])['geo'])))
    rows=[]; inv=[0,0,0,0]   # inversions: total, involving flat, involving nout>0 (not flat), neither
    for r in res:
        S=np.array([x['S'] for x in r['sols']]); V=np.array([x['V'] for x in r['sols']]); VL=np.array([x['Vlaw'] for x in r['sols']])
        if len(S)>=3: rows.append((r['name'],len(S),spearmanr(S,V)[0],spearmanr(VL,V)[0],np.max(abs(VL-V)),np.max(abs(VL-V)[[i for i,x in enumerate(r['sols']) if not x['flat']]]) if any(not x['flat'] for x in r['sols']) else 0))
        for i in range(len(S)):
            for j in range(len(S)):
                if S[i]<S[j]-1e-6 and V[i]<V[j]-1e-6:
                    inv[0]+=1; xi=r['sols'][i]
                    if xi['flat'] or r['sols'][j]['flat']: inv[1]+=1
                    elif xi['nout']>0 or r['sols'][j]['nout']>0: inv[2]+=1
                    else: inv[3]+=1
    A=np.array([[x[2],x[3],x[4]] for x in rows])
    print('knots with >=3 solutions: %d'%len(rows))
    print('raw  Spearman(sum|G|^2, V): min %.3f median %.3f ; exactly -1 in %d'%(A[:,0].min(),np.median(A[:,0]),np.sum(A[:,0]<-1+1e-9)))
    print('law  Spearman(V_law, V):    min %.3f median %.3f ; exactly +1 in %d'%(A[:,1].min(),np.median(A[:,1]),np.sum(A[:,1]>1-1e-9)))
    print('orientation-aware law max |V_law - V| over solutions: median %.3f worst %.3f (knot %s)'%(np.median(A[:,2]),A[:,2].max(),rows[int(np.argmax(A[:,2]))][0]))
    print('rung inversions (S_i<S_j but V_i<V_j): total %d ; involving a flat solution %d ; mixed-orientation (nout>0) %d ; neither %d'%tuple(inv))
    print('\nknot  nsol  rawSpearman  lawSpearman  max|Vlaw-V|  max|Vlaw-V| (non-flat)')
    for x in rows: print('%-6s %3d  %9.3f  %9.3f  %9.3f  %9.3f'%x)
    # pooled over non-flat all-inside..., classes
    cls={}
    for r in res:
        for x in r['sols']:
            k=('flat' if x['flat'] else ('geometric-type (nout=0)' if x['nout']==0 else ('mirror-type (nout=n)' if x['nout']==r['n'] else 'mixed')))
            cls.setdefault(k,[]).append((x['V'],x['Vlaw'],x['S']))
    for k,v in cls.items():
        v=np.array(v); print('class %-24s n=%4d  V range %.2f..%.2f ; median |Vlaw-V| %.3f ; S range %.2f..%.3g'%(k,len(v),v[:,0].min(),v[:,0].max(),np.median(abs(v[:,1]-v[:,0])),v[:,2].min(),v[:,2].max()))
