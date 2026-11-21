"""Full return of four passive, real, linear polarization filters with specified contrasts."""
from fractions import Fraction as F
from math import sqrt
from map_precision import commutator,multiply

def filters(a,b):
    # Square-root of each intensity extinction ratio is a or b.
    A=[[F(1),F(0)],[F(0),1/a]]
    Aop=[[1/a,F(0)],[F(0),F(1)]]
    p=(1+1/b)/2
    m=(1-1/b)/2
    B=[[p,m],[m,p]]
    Bop=[[p,-m],[-m,p]]
    return multiply(multiply(multiply(A,B),Aop),Bop)

def measure(a,b):
    K=filters(a,b)
    W=commutator(a,b)
    assert all(K[i][j]*a*b==W[i][j] for i in range(2) for j in range(2))
    det=K[0][0]*K[1][1]-K[0][1]*K[1][0]
    tr=K[0][0]+K[1][1]
    assert det==1/(a*b)**2
    invariant=tr**2/det
    # Extremal transmitted fractions, squared singular values of K.
    fro2=sum(v*v for row in K for v in row)
    high=(float(fro2)+sqrt(float(fro2**2-4*det**2)))/2
    low=float(det**2)/high
    assert 0<low<=high<1
    # For a real passive map the sign of the spectral-type discriminator
    # can be obtained without keeping the sign of the Jones matrix.
    return float(invariant),high,low,float(fro2/2)

for name,a,b in [('equal 35/6',F(35,6),F(35,6)),('Be Rb',F('153.896205')/F('18.21115'),F('18305.886')/F('4356.865')),('Si Ag',F('8.15168')/F('1.3895212'),F('7.576234')/F('1.30447')),('inside',F(4),F(4)),('tangent',F(9),F(4))]:
    print(name,'J, max, min, unpolarized intensity fractions',*(f'{x:.10f}' for x in measure(a,b)))
