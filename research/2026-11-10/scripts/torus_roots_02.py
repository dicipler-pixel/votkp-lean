# SCRIPT: TORUS-ROOTS-02
# Follow-up to TORUS-ROOTS-01. The predicted second direction of 8_19 is 2/3, on the component (a,b) = (2,2).
# On that component the image of y (y^4 central) has eigenvalues +-i, so y^2 is central: the representation may be one the
# drawing potential can only reach as a DEGENERATE solution (some side ratio 0, 1 or infinite), which the paper's filter drops.
# Check: among converged solutions that the filter calls degenerate, list those with Im V0 = 0 and rational Re V0/pi^2.
# If 2/3 (8_19) or 11/15 (10_124) appear only there, the missing roots are missing because of the filter, not the search.
import sys, numpy as np, collections
from fractions import Fraction
sys.path.insert(0,'/home/claude/up/vd5/votkp_vacuum_disk_v5/scripts')
import snappy, drawing_torus_02 as D
R=D.R; P2=R.P2
def tally(label,pd,starts):
    n,nconv,good,bad=D.run(pd,starts,seed=5)
    def cls(vals):
        c=collections.Counter()
        for v in vals:
            if abs(v.imag)<1e-8:
                fr,e=D.rat(v.real); c[str(fr) if e<1e-7 else 'irrational']+=1
            else: c['Im V0 != 0']+=1
        return dict(c)
    print(label,'converged',nconv); print('   kept (non-degenerate):',cls(good)); print('   dropped (degenerate) :',cls(bad)); sys.stdout.flush()
tally('8_19 KnotInfo PD',eval(D.KI['8_19']['pd_notation']),1500)
tally('10_124 KnotInfo PD',eval(D.KI['10_124']['pd_notation']),1200)
