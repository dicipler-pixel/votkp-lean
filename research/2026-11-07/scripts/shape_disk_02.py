# SCRIPT: SHAPE-DISK-02
# How exact is "volume = how close each piece sits to the vacuum point"? Per tetrahedron, compare D(z) with
# V0*(1-|G|^2)^p (V0 = 1.01494, regular tetrahedron) across the whole disk, then the best power p, then the knot totals.
import numpy as np
from mpmath import polylog
w=np.exp(1j*np.pi/3); V0=1.0149416064096536
def D(z): return float(np.imag(complex(polylog(2,z))))+np.angle(1-z)*np.log(abs(z))
rng=np.random.default_rng(0)
g=np.sqrt(rng.uniform(0,1,4000))*np.exp(1j*rng.uniform(0,2*np.pi,4000))      # uniform over the disk
z=(w-np.conj(w)*g)/(1-g)                                                     # inverse of G = (z-w)/(z-conj w)
dv=np.array([D(x) for x in z]); f=1-np.abs(g)**2
for r0,r1 in [(0,.3),(.3,.6),(.6,.8),(.8,.95),(.95,1)]:
    m=(abs(g)>=r0)&(abs(g)<r1); q=dv[m]/(V0*f[m])
    print('|G| %.2f-%.2f  D/(V0(1-|G|^2)) = %.4f .. %.4f'%(r0,r1,q.min(),q.max()))
m=abs(g)<0.9; A=np.column_stack([np.log(f[m]),np.ones(m.sum())]); c,*_=np.linalg.lstsq(A,np.log(dv[m]),rcond=None)
print('best power law over |G|<0.9: D ~ %.4f (1-|G|^2)^%.4f'%(np.exp(c[1]),c[0]))
# second-order: D near the centre in terms of |G|^2 (exact Taylor check)
for e in (1e-2,1e-3):
    gg=e*np.exp(1j*np.linspace(0,2*np.pi,12,endpoint=False)); zz=(w-np.conj(w)*gg)/(1-gg)
    print('near centre |G|=%g: (V0-D)/|G|^2 over 12 angles = %.6f .. %.6f'%(e,min((V0-D(x))/e**2 for x in zz),max((V0-D(x))/e**2 for x in zz)))
print('compare: V0 = %.6f, 3*sqrt(3)/2 = %.6f, sqrt(3) = %.6f'%(V0,3*np.sqrt(3)/2,np.sqrt(3)))
