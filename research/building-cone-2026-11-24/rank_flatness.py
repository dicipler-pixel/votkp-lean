# SCRIPT: RANK-FLATNESS-01
# Question: can ANY placement of the 16 matrices as projectors (chordal distance, the IQGT metric)
# have squared distance = a function of rank(a - b) with value ratio f(2)/f(1) = 2 (the building cone)?
# KILL LINE (written before the run): the squared distance "rank" is flat (embeds in a Hilbert space).
# WHY THE CHECK TESTS THE CLAIM.  Chordal distance ||P_a - P_b|| is a Hilbert-space distance.  A
# squared distance F(a - b) on the group F_2^4 embeds in a Hilbert space exactly when its Fourier
# coefficients at every nonzero character are <= 0 (Schoenberg).  Exact whole-number arithmetic.
from fractions import Fraction as Fr
from itertools import product
mats=[tuple(b) for b in product((0,1),repeat=4)]
def rk(m):
    a,b,c,d=m
    return 0 if not any(m) else (2 if (a*d-b*c)%2 else 1)
def coeff(f1,f2):
    out={}
    for s in mats:
        if not any(s): continue
        v=sum({0:0,1:f1,2:f2}[rk(x)]*(-1)**(sum(p*q for p,q in zip(s,x))%2) for x in mats)
        out.setdefault(rk((s[0],s[2],s[1],s[3])),set()).add(v)     # character labelled by the rank of s
    return out
print('squared distance = rank (1 on rank 1, 2 on rank 2): Fourier coefficients by character rank:',coeff(1,2))
c=coeff(1,Fr(3,2)); print('squared distance 1 on rank 1, 3/2 on rank 2:',{k:[str(v) for v in s] for k,s in c.items()})
# general: coefficient at rank-1 characters = 1 - 2 f2/f1 ; at rank-2 characters = -3 + 2 f2/f1
print('coefficients as functions of t = f(2)/f(1): rank-1 characters 1 - 2t, rank-2 characters -3 + 2t')
for t in (Fr(1),Fr(3,2),Fr(5,3),Fr(2)):
    print('  t =',t,' ->',1-2*t,',',-3+2*t,'  flat' if -3+2*t<=0 else '  NOT flat')
flat=all(v<=0 for s in coeff(1,2).values() for v in s)
print('KILL LINE fired: rank is flat' if flat else 'KILL LINE did not fire: squared distance = rank is not flat; the flat range ends exactly at t = 3/2')
