# SCRIPT: BOWL-LAW-TETRA-01
# Per-tetrahedron check of the truncated Taylor laws on the Smith disk (uniform samples, 40000 points): mean |D - law| by radius for
# L0 = V0 - k2|G|^2 ; L1 = L0 + (sqrt3/4)Re G^3 ; L1b = L1 + (3 sqrt3/16)|G|^4. Shows at which radius the cubic term helps alone and when it needs the quartic.
import numpy as np
from scipy.special import spence
w=np.exp(1j*np.pi/3); V0=1.0149416064096536; k2=3*np.sqrt(3)/4
def D(z): return np.imag(spence(1-z))+np.angle(1-z)*np.log(abs(z))
rng=np.random.default_rng(0); N=40000
g=np.sqrt(rng.uniform(0,1,N))*np.exp(1j*rng.uniform(0,2*np.pi,N)); z=(w-np.conj(w)*g)/(1-g); a=abs(g)
dv=D(z); L0=V0-k2*a**2; L1=L0+np.sqrt(3)/4*(g**3).real; L1b=L1+3*np.sqrt(3)/16*a**4
print('radius bin     mean|D-L0|  mean|D-L1|  mean|D-L1b|   (cubic helps alone if L1<L0)')
for lo,hi in [(0,.2),(.2,.4),(.4,.6),(.6,.8),(.8,.9),(.9,1)]:
    m=(a>=lo)&(a<hi); print('%.1f-%.1f  n=%5d   %.5f     %.5f     %.5f'%(lo,hi,m.sum(),*[np.mean(abs(dv[m]-L[m])) for L in (L0,L1,L1b)]))
# in the knot data: typical |G| of pieces
R=np.load('/home/claude/votkp_research/bowl_law_knots_01.npy'); print('knot data: max|G| of the knots (median %.2f)'%np.median(R[:,-1]))
# angular structure: error of L0 and L1 vs angle at |G|=0.5
th=np.linspace(0,2*np.pi,13)[:-1]; gg=0.5*np.exp(1j*th); zz=(w-np.conj(w)*gg)/(1-gg)
print('|G|=0.5: D - L0 vs angle (units 1e-3):',np.round(1e3*(D(zz)-(V0-k2*0.25)),2)); print('          (sqrt3/4)Re G^3                 :',np.round(1e3*np.sqrt(3)/4*(gg**3).real,2))
