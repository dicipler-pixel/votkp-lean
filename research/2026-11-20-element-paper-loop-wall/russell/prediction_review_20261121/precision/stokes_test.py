"""Predict a directly observable intensity contrast for a coherent, real Jones return."""
from fractions import Fraction as F
from pathlib import Path
from math import sqrt
# Keep passive_optics.py importable without replaying its text output.
from map_precision import commutator

def calc(a,b):
    K=[[j/(a*b) for j in row] for row in commutator(a,b)]
    (p,q),(r,s)=K
    det=p*s-q*r
    # Stokes order I,Q,U,V. All quantities in units of incident intensity.
    I0=(p*p+q*q+r*r+s*s)/2
    Qq=(p*p-q*q-r*r+s*s)/2
    Uu=p*s+q*r
    Vv=det
    contrast=I0+Qq+Uu-3*Vv
    assert contrast==(p+s)**2-4*det
    return I0,Qq,Uu,Vv,contrast
if __name__=='__main__':
    for name,a,b in [('35/6',F(35,6),F(35,6)),('Be/Rb',F('153.896205')/F('18.21115'),F('18305.886')/F('4356.865')),('Si/Ag',F('8.15168')/F('1.3895212'),F('7.576234')/F('1.30447')),('tangent',F(9),F(4)),('inside',F(4),F(4))]:
        v=calc(a,b)
        print(name,'I0 Qq Uu Vv contrast contrast/I0 equal-error-limit:',*(f'{float(x):.12f}' for x in (*v,v[-1]/v[0],abs(v[-1])/6)))
