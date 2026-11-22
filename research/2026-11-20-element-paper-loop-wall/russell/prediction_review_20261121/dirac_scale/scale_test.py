"""Point-Coulomb Dirac comparison: same binding ratio, different absolute binding."""
from math import exp,expm1,lgamma,log,sqrt
from scipy.optimize import brentq
from scipy.integrate import quad
ALPHA=1/137.035999177
def params(e):
    assert 0<e<1
    g=1-e
    k=sqrt(e*(2-e))
    s=k/(1+g)
    return g,k,s
def overlap(e1,e2):
    a,ka,sa=params(e1);b,kb,sb=params(e2)
    na=(a+.5)*log(2*ka)-.5*(lgamma(2*a+1)+log(1+sa*sa))
    nb=(b+.5)*log(2*kb)-.5*(lgamma(2*b+1)+log(1+sb*sb))
    return exp(na+nb+log(1+sa*sb)+lgamma(1+a+b)-(1+a+b)*log(ka+kb))
def check_quad(e1,e2):
    a,ka,sa=params(e1);b,kb,sb=params(e2)
    def radial(x,g,k,s):
        return exp((g+.5)*log(2*k)-.5*(lgamma(2*g+1)+log(1+s*s))+g*log(x)-k*x)
    return quad(lambda x:radial(x,a,ka,sa)*radial(x,b,kb,sb)*(1+sa*sb),0,float('inf'),epsabs=1e-11)[0]
z=35/6
for e2 in (.0001,.02,.07,.15,.25,.35,.45,.50):
    e1=e2/z
    B=overlap(e1,e2)**2
    assert abs(B-check_quad(e1,e2)**2)<1e-9
    assert abs(overlap(e1,e2)-overlap(e2,e1))<1e-12
    print('higher binding/mc²',e2,'continuous charge pair',*(round(params(e)[1]/ALPHA,4) for e in (e1,e2)), 'fidelity',round(B,9))
upper=brentq(lambda e:overlap(e/z,e)**2-.5,.0001,.5)
print('one bracketed equal-half example at identical z; upper binding/mc²',upper,'charges',params(upper/z)[1]/ALPHA,params(upper)[1]/ALPHA)
