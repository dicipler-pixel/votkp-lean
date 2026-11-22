"""Compare direct radial integration to the equal-n face formula (same mass and l,m)."""
import math
from fractions import Fraction as F
from scipy.integrate import quad
from scipy.special import eval_genlaguerre, gammaln

def radial(n,l,alpha,r):
    x=2*alpha*r/n
    pref=(2*alpha/n)**1.5*math.exp((gammaln(n-l)-math.log(2*n)-gammaln(n+l+1))/2)
    return pref*math.exp(-x/2)*x**l*eval_genlaguerre(n-l-1,2*l+1,x)

def brute(n,l,a,b):
    f=lambda r:r*r*radial(n,l,a,r)*radial(n,l,b,r)
    return quad(f,0,math.inf,epsabs=2e-12,epsrel=2e-12,limit=300)[0]**2

largest=0; samples=0
for u in (.3,.5,.9,1,1.5,2,1+math.sqrt(2),2+math.sqrt(3),5,7):
    x=(u-1)/(u+1);t=1-x*x
    for n,l in [(1,0),(2,0),(2,1),(3,2),(4,3),(5,4),(6,5)]:
        pred=t**(2*n+1) if n==l+1 else t**3*(1-3*x*x)**2
        delta=abs(brute(n,l,1,u)-pred)
        assert delta<3e-11, (u,n,l,delta)
        largest=max(largest,delta);samples+=1
print('Independent quadrature tests',samples,'max discrepancy',largest)
x=F(1,3);t=1-x*x
print('energy ratio z=4; 1s, 2s, 2p fidelities:',t**3,t**3*(1-3*x*x)**2,t**5)
for u in (2,1+math.sqrt(2),2+math.sqrt(3)):
    print('radius-scale ratio',f'{u:.9f}','binding energy ratio',f'{u*u:.9f}','1s / 2s / 2p',*(f'{brute(n,l,1,u):.9f}' for n,l in [(1,0),(2,0),(2,1)]))
