# SCRIPT: EDGE-SUPPORT-01
# Edge support functionals (Alman, Li, Pratt, arXiv 2604.01386, Theorem 1.1): universal
# spectral points over EVERY field, for tensors with three parties, weights theta = (rho, 1-rho, 0).
# Their value on a matrix multiplication tensor <a,b,c> is a^rho * b * c^(1-rho); that tensor is
# three wires round the triangle, so a wire between parties i and j is priced q^(theta_i+theta_j):
# exponents rho+(1-rho) = 1, (1-rho)+0, rho+0, matching the formula.
# Metric on three parties: d(1,2) = 1, d(1,3) = rho, d(2,3) = 1-rho.  Party 3 lies ON the segment
# from 1 to 2.  Pulled back to the 16 matrices (Definition A.4 of the release): every matrix sits
# at one of three points of a straight line, at positions 0, rho, 1.
#
# WHY THE ANSWER IS FORCED: three points on a line are a Euclidean configuration, and the flat
# maximum on the 16 matrices is 3/2 (proved by character count, retest R2).  So no edge support
# functional can exceed 3/2.  This run is a check of that argument, not the proof.
#
# KILL LINE (written before the run): any edge support price above 5/3.
# SHARPER LINE: any above 3/2 means the collinear argument is wrong.
from itertools import product
import numpy as np
mats=[tuple(b) for b in product((0,1),repeat=4)]
def rank(m):
    a,b,c,d=m
    if not any(m): return 0
    return 2 if (a*d-b*c)%2 else 1
X=np.array([[rank(tuple(p^q for p,q in zip(x,y))) for y in mats] for x in mats])
A1,A2=(X==1),(X==2)
rhos=np.linspace(0,1,201)
def best(lab):
    top=0
    for rho in rhos:
        pos=np.array([0.0,1.0,rho])[lab]; d2=(pos[:,None]-pos[None,:])**2
        den=d2[A1].mean()
        if den>1e-12: top=max(top,d2[A2].mean()/den)
    return top
rng=np.random.default_rng(3); ends=[]
for s in range(60):
    lab=rng.integers(0,3,16); cur=best(lab)
    while True:
        bv,bl=cur,None
        for i in range(16):
            for g in range(3):
                if g==lab[i]: continue
                new=lab.copy(); new[i]=g; v=best(new)
                if v>bv+1e-9: bv,bl=v,new
        if bl is None: break
        lab,cur=bl,bv
    ends.append(round(cur,6))
print('60 greedy climbs over groupings into three collinear points, rho on a 201-point grid')
print('largest ratio:',max(ends),' distinct end values:',sorted(set(ends),reverse=True)[:6])
print('flat maximum 3/2 = 1.5 ; star value 5/3 =',round(5/3,6))
print('KILL LINE fired' if max(ends)>5/3+1e-6 else 'KILL LINE did not fire')
print('SHARPER LINE fired' if max(ends)>1.5+1e-6 else 'SHARPER LINE did not fire: nothing above 3/2')
