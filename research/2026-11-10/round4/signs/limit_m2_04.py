# SCRIPT: LIMIT-M2-04  (LIMIT-M2-03 stopped on a missing import before any result; this is the same check with the import)
# LIMIT-M2-02 listed 9 "mismatches" of the two-term rule, all p/3 with m = 13..16. Its matcher only searched m <= 12,
# so these are a search-cap artefact unless shown otherwise. Here the type-B limit polynomial of each is compared
# EXACTLY with the prediction for r = 3: the single limit 4 sin^2(pi/6)/m^2 = 1/m^2, i.e. P_B proportional to 1 - m^2 k.
print('WHY: exact integer polynomial identity, no matcher.  KILL: P_B(k) is not a constant multiple of (1 - m^2 k) times a power of k.')
import sys, sympy as sp
from sympy.polys.rings import ring
from sympy import ZZ
from math import gcd
sys.path.insert(0,'/home/claude/work/agent_signs')
exec(open('/home/claude/work/agent_signs/limit_m2_01.py').read().split('mp.mp.dps=60')[0].split('# ---------- exact limits')[1])
k_=sp.Symbol('k'); ok=0; n=0
for p in range(77,102,2):
    for sg in (1,-1):
        if (p-sg)%6==0:
            m=(p-sg)//6; PA,PB=limits(riley(p,3)); e=sp.factor_list(PB.as_expr())
            fl=[(sp.expand(h),mult) for h,mult in e[1]]; good=any(sp.expand(h-(m*m*k_-1))==0 or sp.expand(h+(m*m*k_-1))==0 for h,mult in fl) and all(h==k_ or sp.Poly(h,k_).degree()==1 for h,mult in fl)
            n+=1; ok+=good; print('  %d/3  m = %d  P_B = %s   %s'%(p,m,sp.factor(PB.as_expr()),'matches 1/m^2' if good else 'MISMATCH'))
print('exact matches: %d of %d'%(ok,n))
