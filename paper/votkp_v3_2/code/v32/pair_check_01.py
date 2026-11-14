# SCRIPT: PAIR-ACROSS-WALL-01
# WHY: Section 25.1 states that two steps with Gamma*Gamma' = 1/2 share K and the angle between fixed directions, and that
# z = 5 and z = 7 are such a pair with K = 9 and cosh(lambda/4) = 9/7. These are computed here from the loop matrix itself.
# KILL LINE: any difference above 1e-10 between the pair's K, or between K and the closed forms, on 200 random pairs.
import numpy as np
from scipy.linalg import expm
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]])
B=lambda s,r: expm(0.5*r*s); loop=lambda r: B(sx,r)@B(sy,r)@B(sx,-r)@B(sy,-r)
def K(z):
    w,V=np.linalg.eig(loop(np.log(z))); a=V[:,0]/np.linalg.norm(V[:,0]); b=V[:,1]/np.linalg.norm(V[:,1]); return 1/(1-abs(np.vdot(a,b))**2)
G=lambda z:(z-1)/(z+1); zof=lambda g:(1+g)/(1-g)
rng=np.random.default_rng(7); worst=0
for g in rng.uniform(0.52,0.70,200):
    g2=0.5/g; k1,k2=K(zof(g)),K(zof(g2)); worst=max(worst,abs(k1-k2)/k1,abs(k1-1/(1-2*g*g))/k1,abs(k2-2*g2*g2/(2*g2*g2-1))/k2)
print('pairs worst rel diff',worst)
print('G5*G7',G(5)*G(7),'K5',K(5),'K7',K(7))
r=np.log(7); tr=np.trace(loop(r)).real; lam=2*np.arccosh(-tr/2); print('cosh(lambda/4) at 7:',np.cosh(lam/4),'9/7 =',9/7)
print('K at z=1e6 (toward the rim):',K(1e6))
