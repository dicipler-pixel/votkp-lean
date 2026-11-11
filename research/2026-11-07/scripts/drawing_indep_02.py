# SCRIPT: DRAWING-INDEP-02
# Task 2: diagram independence. For each knot take the KnotInfo PD (D0) and two other PDs of the SAME oriented knot made by
# SnapPy: D1 = backtrack(k)+simplify('global'), D2 = backtrack(k) (more crossings, no simplification).
# Same placement rule (a,b,c,d)=(l,i,j,k) for X[i,j,k,l] (SnapPy PD_code uses the KnotTheory convention; checked by the top value).
# Search per drawing: random starts in chunks of 100 until the top matches SnapPy for that very drawing AND STAB further
# starts bring no new (decay,direction) cluster, or CAP starts. Then compare the full cluster sets between drawings.
import numpy as np, snappy, sys, time, json, random, warnings, database_knotinfo as d
from multiprocessing import Pool
warnings.filterwarnings('ignore')
import drawing_robust_01 as R
import drawing_robust_03 as R3
P2=R.P2; STAB=600; CAP=4000
KI={r['name']:r for r in d.link_list()}
def dcs(a,b): return abs(((a-b)+P2/2)%P2-P2/2)
def spectrum(pd,cv,seed0):
    cr,n=R.crossings_from_pd(pd); allv=[]; used=0; seed=seed0; last_new=0; ncl=0; topok=False
    while used<CAP:
        out,ns=R3.solve2(cr,n,starts=100,seed=seed); seed+=1; used+=ns; allv+=[v for v,_ in out]
        cl=R.cluster(allv)
        if len(cl)>ncl: ncl=len(cl); last_new=used
        topok=any(abs(v.imag-cv.real)<1e-6 and dcs(-v.real,cv.imag)<1e-5 for v in allv)
        if topok and used-last_new>=STAB: break
    return n,used,topok,[k for k,c in R.cluster(allv)]
def same(s1,s2,tol=1e-5):
    def inn(a,B): return any(abs(a[0]-b[0])<tol and dcs(a[1],b[1])<tol for b in B)
    return all(inn(a,s2) for a in s1) and all(inn(b,s1) for b in s2), [a for a in s1 if not inn(a,s2)], [b for b in s2 if not inn(b,s1)]
def kinkfree(pd): return all(len(set(X))==4 for X in pd)   # an R1 kink has a repeated label -> ratio 1 -> Li2/log singular
def make(L,k,simp,seedbase,avoid):
    for t in range(200):
        random.seed(seedbase+t); LL=L.copy(); LL.backtrack(k)
        if simp: LL.simplify('global')
        pd=[tuple(x) for x in LL.PD_code()]
        if kinkfree(pd) and len(pd)<=11 and True:
            try: dt=LL.DT_code()
            except Exception: dt=0
            if (len(pd),str(dt)) not in avoid: return LL,(len(pd),str(dt))
    return None,None
def one(name):
    pd0=eval(KI[name]['pd_notation']); L=snappy.Link(pd0); cv0=complex(L.exterior().complex_volume())
    try: dt0=L.DT_code()
    except Exception: dt0=0
    avoid={(len(pd0),str(dt0))}
    L1,k1=make(L,5,True,100,avoid); avoid.add(k1); L2,k2=make(L,3,False,500,avoid)
    res=dict(name=name,drawings=[])
    S=[]
    for lab,LL in [(a,b) for a,b in (('D0 KnotInfo',L),('D1 backtrack+simplify',L1),('D2 backtrack',L2)) if b is not None]:
        pd=[tuple(x) for x in LL.PD_code()]; cv=complex(LL.exterior().complex_volume()); t=time.time()
        n,used,topok,spec=spectrum(pd,cv,11)
        S.append(spec); res['drawings'].append(dict(label=lab,crossings=len(pd),sides=n,starts=used,top_ok=topok,time=round(time.time()-t),spectrum=[(round(a,5),round(b,5)) for a,b in spec],snappy_cv=(cv.real,float(((cv.imag+P2/2)%P2)-P2/2))))
    for j in range(1,len(S)):
        ok,a,b=same(S[0],S[j]); res['D%d_vs_D0'%j]=dict(equal=bool(ok),only_in_D0=[(round(p[0],5),round(p[1],5)) for p in a],only_in_Dj=[(round(p[0],5),round(p[1],5)) for p in b])
    return res
if __name__=='__main__':
    names=sys.argv[1].split(',')
    with Pool(2) as p:
        for r in p.imap(one,names): print(json.dumps(r),flush=True)
