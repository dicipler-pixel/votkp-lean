# SCRIPT: DRAWING-TORUS-02
# Task 3, precise version. As DRAWING-TORUS-01 but every converged solution is POLISHED (extra least-squares passes) and kept only
# if residual cost < 1e-26 (|residual| ~ 1e-13), so Re V0 is good to ~1e-10 and the p/q test uses tolerance 1e-8 (q <= 120).
# Non-degenerate = all ratios z_p/z_q have min(|r|,|1-r|) > 1e-6 and |r| < 1e6.  Second PD: SnapPy backtrack(3) of the same oriented knot.
import numpy as np, sys, time, random, warnings, snappy, database_knotinfo as d
from fractions import Fraction
from scipy.optimize import least_squares
warnings.filterwarnings('ignore')
import drawing_robust_01 as R
import drawing_robust_03 as R3
P2=R.P2
KI={r['name']:r for r in d.link_list()}
def run(pd,starts,seed=1):
    cr,n=R.crossings_from_pd(pd); T=R.terms(cr); f,jac,split=R.residual_and_jac(T,n); rng=np.random.default_rng(seed)
    good=[];bad=[];nconv=0
    for s in range(starts):
        x0=R3.draw_start2(rng,n)
        try:
            r=least_squares(f,x0,jac=jac,method='trf',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=300)
            if r.cost<1e-18:
                for _ in range(3): r=least_squares(f,r.x,jac=jac,method='lm',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=200)
        except Exception: continue
        if r.cost<1e-26:
            z=split(r.x); nconv+=1
            try: v=R.V0(T,z,n)
            except Exception: continue
            if np.isfinite(v): (good if R.good(T,z) else bad).append(v)
    return n,nconv,good,bad
def rat(x):
    t=(x%P2)/P2; fr=Fraction(t).limit_denominator(120); return fr,abs(float(fr)-t)*P2
def report(label,pd,starts):
    t=time.time(); n,nconv,good,bad=run(pd,starts)
    print('%s: %d sides, %d starts, %.0fs, converged(polished) %d, non-degenerate %d, degenerate %d'%(label,n,starts,time.time()-t,nconv,len(good),len(bad)))
    reps=[]
    for v in good:
        k=(v.imag,v.real%P2)
        for r in reps:
            if abs(r[0][0]-k[0])<1e-7 and abs(((r[0][1]-k[1])+P2/2)%P2-P2/2)<1e-7: r[1]+=1; break
        else: reps.append([k,1])
    reps.sort(key=lambda r:r[0][1])
    print('  non-degenerate distinct (Im V0, Re V0 mod pi^2) [count], Re V0/pi^2 as p/q (|err| in Re V0):')
    for (im,re),c in reps:
        fr,e=rat(re); print('    (%+.2e, %.9f) x%-4d  Re/pi^2 = %s  err %.1e  %s'%(im,re,c,fr,e,'RATIONAL' if e<1e-8 else 'not rational q<=120'))
    print('  degenerate (non-constant-family / run-away) solutions: %d, Im V0 range [%.3f, %.3f]'%(len(bad),min([v.imag for v in bad],default=0),max([v.imag for v in bad],default=0)))
if __name__=='__main__':
    S={'3_1':1500,'5_1':1500,'7_1':1500,'8_19':800,'10_124':500}
    for nm,st in S.items():
        pd=eval(KI[nm]['pd_notation']); report(nm+' KnotInfo PD, %d crossings'%len(pd),pd,st)
    for nm in ['3_1','5_1']:
        random.seed(3); L=snappy.Link(eval(KI[nm]['pd_notation'])); L.backtrack(3); pd=[tuple(x) for x in L.PD_code()]
        report(nm+' second PD (backtrack), %d crossings'%len(pd),pd,1500)
