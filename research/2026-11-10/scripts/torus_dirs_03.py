# SCRIPT: TORUS-DIRS-03
# Why this check proves the claim: Dirac Time Thm 13.1(3) gives the two end steps of arc (a,b) as
# k = u*a*q + v*b*p and k = u*a*q - v*b*p with u*q + v*p = 1. The vacuum-disk paper's direction is
# -k^2/(pq) mod 1. If both end steps of every arc give the same direction, the direction belongs to the arc.
# Listing it arc by arc then says exactly which directions the root search should find.
# Kill condition (written before the run): any arc whose two ends give different directions.
from fractions import Fraction as F
from math import gcd
def uv(p,q):
    for u in range(-p*q,p*q):
        if (1-u*q)%p==0: return u,(1-u*q)//p
bad=0
for p in range(2,13):
    for q in range(p+1,20):
        if gcd(p,q)!=1: continue
        u,v=uv(p,q)
        for a in range(1,p):
            for b in range(1,q):
                if (a-b)%2: continue
                k1,k2=u*a*q+v*b*p,u*a*q-v*b*p
                if (k1*k1-k2*k2)%(p*q): bad+=1
print('arcs whose two ends disagree:',bad)
for name,p,q in [('3_1',2,3),('5_1',2,5),('7_1',2,7),('8_19',3,4),('10_124',3,5),('T(4,5)',4,5)]:
    u,v=uv(p,q); out=[]
    for a in range(1,p):
        for b in range(1,q):
            if (a-b)%2: continue
            k=u*a*q+v*b*p; out.append(((a,b),sorted({abs(k)%(2*p*q),abs(u*a*q-v*b*p)%(2*p*q)}),F(-k*k,p*q)%1))
    print(name,'arcs',len(out),'distinct directions',len({o[2] for o in out}),'|',' ; '.join('arc%s ends k=%s dir=%s'%(o[0],o[1],o[2]) for o in out))
