# SCRIPT: LIMIT-REAL-04
# Q2 part 5 redone. LIMIT-REAL-03 reported "no real branch" for 17/3 = 8_2, whose real limit 1/9 is printed in Two
# Trees census 8.8. Cause found: never_turn_02.riley_coeffs trims leading coefficients below 1e-25 of the largest;
# at x = 12 the true leading coefficients are far smaller, so every branch with v ~ s^2 (type B) was dropped.
# This run uses exact integer coefficients (riley_exact.py). LIMIT-REAL-03 is kept as the record of the failure.
print('''WHY: the exact limit polynomials (LIMIT-M2-01) list every candidate limit; a candidate is a limit of the real
slice only if its branch is real. Real branches are found at x = 12 with 200 digits and exact coefficients; the limit
is approached to ~e^-24, so agreement to 8 digits is the test.  Control: 17/3 must show 1/9 (printed in the paper).
KILL: the control fails; or a real branch with 1e-6 < k < 4 that is not at an exact limit value.''')
import sys, pickle, mpmath as mp
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact import *
rows={(p,q):F for p,q,F in pickle.load(open('/home/claude/work/agent_signs/limit_m2_01.pkl','rb'))}
tests=[(17,3),(23,3),(29,5),(27,7),(41,7),(23,17),(35,29),(39,29),(13,5),(25,9),(31,13),(21,13),(47,3),(59,29),(11,7),(17,7),(23,13)]
tot=collections=None
nreal=nvals=0
for p,q in tests:
    br=branches(riley(p,q),12,200); bandk=sorted(k for v,t,k,real in br if real and mp.mpf(10)**-6<k<4)
    ex=[]
    for nm in 'AB':
        for idn,e in rows[(p,q)][nm]:
            if not isinstance(idn[0],str):
                d,m,js=idn; ex+=[(nm,d,m,j,e,4*mp.sin(mp.pi*j/d)**2/m**2) for j in js]
    print('%d/%d cf %s  roots %d, real %d, real with k in (1e-6,4): %d'%(p,q,cf(p,q),len(br),sum(1 for b in br if b[3]),len(bandk)))
    for nm,d,m,j,e,val in ex:
        hit=[k for k in bandk if abs(k-val)<mp.mpf(10)**-8]; nvals+=1; nreal+=bool(hit)
        print('      %s: 4 sin^2(%d pi/%d)/%d^2 = %-12s multiplicity %d : %s'%(nm,j,d,m,mp.nstr(val,8),e,'REAL x%d'%len(hit) if hit else 'no real branch'))
    stray=[mp.nstr(k,10) for k in bandk if not any(abs(k-val)<mp.mpf(10)**-8 for *_,val in ex)]
    print('      real band branches not at an exact limit value:',stray,flush=True)
print('exact limit values tested: %d ; reached by a real branch: %d'%(nvals,nreal))
