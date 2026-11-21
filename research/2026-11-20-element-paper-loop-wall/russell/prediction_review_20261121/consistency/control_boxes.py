"""Exact independent-input boxes for the two analogue controls."""
import itertools
from fractions import Fraction as F
def power(z):
    return ((z-1)/(z+1))**2
def margins(a,b,t):
    x,y=power(a),power(b)
    return x+y-1,x+y-2*t,x*y*(1-t)**2-t*t*(1-x)*(1-y)
def run(label,a,b):
    ts=[F(50051,100000),F(50054,100000)]
    rows=[margins(i,j,t) for i,j,t in itertools.product(a,b,ts)]
    intervals=[(min(vals),max(vals)) for vals in zip(*rows)]
    print(label,*(f'[{float(l):+.12g},{float(h):+.12g}]' for l,h in intervals))
    assert intervals[0][0]>0 and intervals[1][1]<0
    if label=='equal':
        assert intervals[2][1]<0
    else:
        assert intervals[2][0]>0
if __name__=='__main__':
    run('equal',[F('5.832'),F('5.835')],[F('5.832'),F('5.835')])
    run('unequal',[F('2.9999'),F('3.0001')],[F('13.9899'),F('13.9901')])
