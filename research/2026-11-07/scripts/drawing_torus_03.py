# SCRIPT: DRAWING-TORUS-03
# Task 3 follow-up: second, kink-free PDs (SnapPy backtrack, same oriented knot) of the torus knots 3_1, 5_1, 7_1.
# (A first attempt with a PD containing a Reidemeister-I kink, i.e. a crossing X[i,j,j,l], is singular: the term Li2(z_d/z_c) has ratio 1.)
import random, snappy, warnings, database_knotinfo as d
warnings.filterwarnings('ignore')
from drawing_torus_02 import report, KI
for nm,st in [('3_1',1500),('5_1',1500),('7_1',800)]:
    for seed in range(300):
        random.seed(1000+seed); L=snappy.Link(eval(KI[nm]['pd_notation'])); L.backtrack(3); pd=[tuple(x) for x in L.PD_code()]
        if all(len(set(X))==4 for X in pd) and len(pd)>len(eval(KI[nm]['pd_notation'])): break
    report(nm+' second PD (backtrack, kink-free), %d crossings'%len(pd),pd,st)
