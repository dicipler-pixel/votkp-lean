# SCRIPT: MATTER-PEEL-01
# Joins Matter at a Scale (census ladder), VOTKP (Smith/peel coordinate) and the Cone (indefinite NH metric).
import numpy as np
from scipy.integrate import quad
print('='*78); print('MATTER-PEEL-01'); print('='*78)
# (1) identity Gamma = 1-2nu = tanh(eps/2), eps = ln((1-nu)/nu)
nus=np.array([1e-6,0.01,0.2,0.37,0.5,0.73,0.999])
z=(1-nus)/nus; G=(z-1)/(z+1)
print('(1) max|Gamma-(1-2nu)| =',np.max(abs(G-(1-2*nus))),' max|Gamma-tanh(ln z/2)| =',np.max(abs(G-np.tanh(np.log(z)/2))))
# (2) entropy over peel rapidity
H=lambda e: np.log(1+np.exp(e))-e*np.exp(e)/(1+np.exp(e)) if e<30 else np.exp(-e)*(1+e)
def Hg(e):
    g=np.tanh(e/2); a,b=(1+g)/2,(1-g)/2
    return -sum(p*np.log(p) for p in (a,b) if p>0)
val,_=quad(Hg,-80,80,limit=500,epsabs=1e-13)
print('(2) int H d(eps) over rapidity =',val,' pi^2/3 =',np.pi**2/3,' diff',abs(val-np.pi**2/3))
