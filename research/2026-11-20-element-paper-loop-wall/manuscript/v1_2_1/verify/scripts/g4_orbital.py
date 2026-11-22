# SCRIPT: G4_ORBITAL
from fractions import Fraction as F
from sympy import sqrt, nsimplify, simplify, Rational, N, integrate, symbols, exp, oo, sqrt as sq, pi, expand
a=F(3,5) # z=4 -> beta/alpha=2, a=(2-1)/(2+1)=1/3
a=F(1,3); t=1-a*a
print('z=4 a',a,'t',t)
print('1s',t**3, float(t**3)); print('2s',t**3*(1-3*a*a)**2, float(t**3*(1-3*a*a)**2)); print('2p',t**5,float(t**5))
# wall
import sympy as sp
a=sp.sqrt(2)-1; t=1-a**2
print('t',sp.simplify(t), float(t))
for n,e in (('1s',t**3),('2s',t**3*(1-3*a**2)**2),('2p',t**5)):
    print(n, sp.simplify(sp.expand(e)), float(e))
print(sp.simplify(8*(sp.sqrt(2)-1)**3-8*(5*sp.sqrt(2)-7)))
# independent quadrature: radial orbitals with exponent scale
import mpmath as mp
mp.mp.dps=30
def R1s(k): return 2*k**1.5*mp.e**(-k*r) if False else None
def ov(alpha,beta,kind):
    if kind=='1s':
        f=lambda r: 2*alpha**1.5*mp.e**(-alpha*r)*2*beta**1.5*mp.e**(-beta*r)*r*r
    if kind=='2s':
        R=lambda k,r: (k**1.5/(2*mp.sqrt(2)))*(2-k*r)*mp.e**(-k*r/2)
        f=lambda r:R(alpha,r)*R(beta,r)*r*r
    if kind=='2p':
        R=lambda k,r: (k**1.5/(2*mp.sqrt(6)))*(k*r)*mp.e**(-k*r/2)
        f=lambda r:R(alpha,r)*R(beta,r)*r*r
    return mp.quad(f,[0,mp.inf])**2
for z,b in ((4,2),(None,1+mp.sqrt(2))):
    al=1; 
    for k in ('1s','2s','2p'): print(z,k,ov(al,b,k))
