# SCRIPT: DRAWING-TORUS-01
# Task 3: drawing potential on torus knots 3_1 5_1 7_1 8_19 10_124 (zero hyperbolic volume).
# Prediction under test (untested before this run): solutions exist with decay Im V0 = 0 and a definite direction Re V0.
# For every converged solution (residual < 1e-18) record V0; separate those passing the non-degeneracy filter
# (all ratios z_p/z_q away from 0, 1, infinity) from degenerate ones. Directions are tested against p/q*pi^2, q<=120.
import numpy as np, sys, time, warnings, snappy, database_knotinfo as d
from fractions import Fraction
from scipy.optimize import least_squares
warnings.filterwarnings('ignore')
import drawing_robust_01 as R
P2=R.P2
KI={r['name']:r for r in d.link_list()}
def run(pd,starts,seed=1):
    cr,n=R.crossings_from_pd(pd); T=R.terms(cr); f,jac,split=R.residual_and_jac(T,n); rng=np.random.default_rng(seed)
    good=[];bad=[];nconv=0
    for s in range(starts):
        x0=R.draw_start(rng,n)
        try: r=least_squares(f,x0,jac=jac,method='trf',xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=300)
        except Exception: continue
        if r.cost<1e-18:
            z=split(r.x); nconv+=1
            try: v=R.V0(T,z,n)
            except Exception: continue
            if not np.isfinite(v): continue
            (good if R.good(T,z) else bad).append(v)
    return n,nconv,good,bad
def rat(x):
    t=((x)%P2)/P2; fr=Fraction(t).limit_denominator(120); return fr,abs(float(fr)-t)*P2
def report(label,pd,starts):
    t=time.time(); n,nconv,good,bad=run(pd,starts)
    print('%s: %d sides, %d starts, %.0fs, converged %d, non-degenerate %d, degenerate %d'%(label,n,starts,time.time()-t,nconv,len(good),len(bad)))
    for name,vals in (('non-degenerate',good),('degenerate',bad)):
        if not vals: continue
        reps=[]
        for v in vals:
            k=(round(v.imag,5),round(v.real%P2,5))
            for r in reps:
                if abs(r[0][0]-k[0])<2e-5 and abs(((r[0][1]-k[1])+P2/2)%P2-P2/2)<2e-5: r[1]+=1; break
            else: reps.append([k,1])
        reps.sort(key=lambda r:(-r[0][0],r[0][1]))
        print('  %s distinct (Im V0, Re V0 mod pi^2) [count] and Re V0/pi^2 as fraction (err):'%name)
        for (im,re),c in reps:
            fr,e=rat(re); print('    (%9.5f, %9.5f) x%-4d  Re/pi^2 = %s  (|err| %.1e)'%(im,re,c,fr,e))
if __name__=='__main__':
    starts=int(sys.argv[1])
    for nm in ['3_1','5_1','7_1','8_19','10_124']:
        pd=eval(KI[nm]['pd_notation']); report(nm+' (KnotInfo PD)',pd,starts)
