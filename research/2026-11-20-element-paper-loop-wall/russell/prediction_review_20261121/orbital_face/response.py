from fractions import Fraction as F
from math import sqrt
z=F(35,6)
for share in (F(1,4),F(3,4)):
    # Squared matrix elements at fixed channel energies in arbitrary units
    e1,e2=F(1),z
    d1,d2=share/e1,(1-share)/e2
    weighted=e1*d1,e2*d2
    assert sum(weighted)==1
    print('ratio',z,'weights',*weighted,'first dominates',weighted[0]>weighted[1])
gamma=lambda v:(v-1)/(v+1)
survival=lambda u:(1-gamma(u)**2)**3
assert survival(F(2))==F(512,729)
w=3+2*sqrt(2);u=sqrt(float(z))
print('z=35/6: ground survival',survival(u),'port reflection',float(gamma(z)**2))
print('wall: ground survival',survival(sqrt(w)))
half=sqrt(1-2**(-1/3))
print('half ground-survival in energy ratio z',((1+half)/(1-half))**2)
