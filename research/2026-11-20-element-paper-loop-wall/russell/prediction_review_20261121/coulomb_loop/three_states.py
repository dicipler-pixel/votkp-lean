"""Gauge-invariant three-state cyclic overlaps for scaled hydrogenic 1s/2s/2p."""
from fractions import Fraction as F
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_genlaguerre, gammaln
from math import exp,log
def B(a,b,c,state):
    # The product of the three positive square-root scale factors is rational.
    t=F(8*a*b*c,(a+b)*(b+c)*(c+a))
    f=lambda u,v:1-3*F((u-v),(u+v))**2
    return {'1s':t**3,'2p':t**5,'2s':t**3*f(a,b)*f(b,c)*f(c,a)}[state]

def radial(n,l,alpha,r):
    x=2*alpha*r/n
    normal=(2*alpha/n)**1.5*exp((gammaln(n-l)-log(2*n)-gammaln(n+l+1))/2)
    return normal*exp(-x/2)*x**l*eval_genlaguerre(n-l-1,2*l+1,x)

def overlap(n,l,a,b):
    return quad(lambda r:r*r*radial(n,l,a,r)*radial(n,l,b,r),0,np.inf,epsabs=1e-12)[0]

for name,n,l in [('1s',1,0),('2s',2,0),('2p',2,1)]:
    for p in [(1,2,4),(1,2,6),(1,1,3),(2,5,11),(4,2,1)]:
        ab,bc,ca=[overlap(n,l,p[i],p[(i+1)%3]) for i in range(3)]
        expected=B(*p,name)
        assert abs(ab*bc*ca-float(expected))<5e-12
        if p==(1,2,4): print(name,'cycle permutation expectation',expected,float(expected),'ancilla + probability',(1+float(expected))/2)
for sign in (1,-1):
    # Gauge-invariant relative sign while all three pairwise fidelities are 1/9.
    gram=np.array([[1,1/3,sign/3],[1/3,1,1/3],[sign/3,1/3,1]])
    states=np.linalg.cholesky(gram)
    projectors=[np.outer(row,row) for row in states]
    assert np.isclose(np.trace(projectors[0]@projectors[1]@projectors[2]),sign/27)
    for i in range(3):assert np.isclose(np.trace(projectors[i]@projectors[(i+1)%3]),1/9)
    print('equal pairwise fidelities 1/9, triple trace:',sign,'/27, det Gram',round(np.linalg.det(gram),9))
