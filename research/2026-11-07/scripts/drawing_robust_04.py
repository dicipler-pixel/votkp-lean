# SCRIPT: DRAWING-ROBUST-04
# Task 1: match the top of the drawing spectrum to SnapPy's complex volume on every hyperbolic knot 4-9 crossings (KnotInfo PD).
# Reference = SnapPy complex volume of the exterior of the KnotInfo PD itself (the same drawing); also compared with Manifold(name).
# (v2 of ROBUST-02: solver ROBUST-03 = more start families + conjugation symmetry; run on the knots ROBUST-02 missed and on 9 crossings)
# Search: random multi-scale starts (drawing_robust_01.solve), stopped as soon as the top matches (vol 1e-6, cs mod pi^2 1e-5).
import numpy as np, snappy, sys, time, json, warnings, database_knotinfo as d
from multiprocessing import Pool
warnings.filterwarnings('ignore')
import drawing_robust_01 as R
import drawing_robust_03 as R3
P2=R.P2
KI={r['name']:r for r in d.link_list()}
def dcs(a,b): return abs(((a-b)+P2/2)%P2-P2/2)
def one(args):
    name,budget=args; pd=eval(KI[name]['pd_notation']); cr,n=R.crossings_from_pd(pd)
    cvL=complex(snappy.Link(pd).exterior().complex_volume()); cvM=complex(snappy.Manifold(name).complex_volume())
    def hit(vals,cv=cvL):
        return any(abs(v.imag-cv.real)<1e-6 and dcs(-v.real,cv.imag)<1e-5 for v in vals)
    t=time.time(); allv=[]; used=0; seed=1
    while used<budget:
        out,ns=R3.solve2(cr,n,starts=min(100,budget-used),seed=seed); seed+=1; used+=ns; allv+=[v for v,_ in out]
        if hit(allv): break
    ok=hit(allv); okM=hit(allv,cvM)
    best=max(allv,key=lambda v:v.imag) if allv else None
    return dict(name=name,cr=KI[name]['crossing_number'],sides=n,ok=ok,okM=okM,starts=used,time=round(time.time()-t,1),
                ref=(cvL.real,float(((cvL.imag+P2/2)%P2)-P2/2)),
                best=None if best is None else (best.imag,float(((-best.real+P2/2)%P2)-P2/2)),nsol=len(allv),mism=getattr(R3.solve2,'conj_mismatch',0))
if __name__=='__main__':
    lo,hi,budget=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
    names=[nm for nm in KI if nm.count('_')==1 and not nm.startswith('L') and KI[nm]['crossing_number'] in [str(c) for c in range(lo,hi+1)]]
    names=[nm for nm in names if snappy.Manifold(nm).volume()>0.5]
    if len(sys.argv)>4: names=sys.argv[4].split(',')
    names.sort(key=lambda s:(int(s.split('_')[0]),int(s.split('_')[1])))
    res=[]
    with Pool(2) as p:
        for r in p.imap(one,[(nm,budget) for nm in names]):
            res.append(r); print(json.dumps(r),flush=True)
    print('conj mismatches (V0(conj z) != conj V0(z)), total over knots:',sum(r['mism'] for r in res))
    print('MATCHED %d / %d'%(sum(r['ok'] for r in res),len(res)))
    print('FAILED:',[(r['name'],r['best'],r['ref']) for r in res if not r['ok']])
