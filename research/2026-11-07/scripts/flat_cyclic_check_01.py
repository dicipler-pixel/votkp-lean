# SCRIPT: FLAT-CYCLIC-CHECK-01
# Record of two facts used in STRONG-FLAT-02:
# (1) R(z';q,r) - R(z;p,q) = (1+3q) pi^2/6 for every z (r=-1-p-q): Neumann's R is not invariant under relabelling the three edge pairs of one tetrahedron,
#     so the sum over an UNORDERED triangulation (snappy's) is off by multiples of pi^2/6 (this was the 'weak flattening' ambiguity of WINDING-CS-01).
# (2) the lifted five-term relation holds exactly for this R (so R itself is the right function; only the labelling matters).
import numpy as np
from mpmath import polylog, mpc
def R(z,p,q):
    lz=np.log(z); l1=np.log(1-z)
    return complex(polylog(2,mpc(z)))+0.5*lz*l1+0.5j*np.pi*(q*lz+p*l1)-np.pi**2/6
u=np.pi**2/6; rng=np.random.default_rng(5); worst=0
for _ in range(200):
    z=complex(rng.normal(0.5,1),abs(rng.normal(0,1))+.05); p,q=[int(x) for x in rng.integers(-4,5,2)]; r=-1-p-q
    worst=max(worst,abs((R(1/(1-z),q,r)-R(z,p,q)).real/u-(1+3*q)),abs((R(1-1/z,r,p)-R(1/(1-z),q,r)).real/u-(1+3*r)))
print('(1) max deviation of cyclic difference from (1+3q) in units pi^2/6 over 200 random (z,p,q): %.2e'%worst)
bad=0; tot=0
for _ in range(300):
    x=complex(rng.uniform(0.2,0.8),rng.uniform(0.3,1.2)); y=complex(rng.uniform(0.2,0.8),rng.uniform(1.5,2.5))
    xs=[x,y,y/x,(1-1/x)/(1-1/y),(1-x)/(1-y)]
    if not all(abs(v.imag)>0 and v.imag>0 for v in xs): continue
    p0,p1,q0,q1,q2=[int(v) for v in rng.integers(-3,4,5)]
    pq=[(p0,q0),(p1,q1),(p1-p0,q2),(p1-p0+q1-q0,q2-q1),(q1-q0,q2-q1-p0)]
    s=sum((-1)**i*R(xs[i],*pq[i]) for i in range(5)); tot+=1; bad+= abs(s)>1e-9
print('(2) lifted five-term relation (all five shapes in the upper half plane): %d tested, %d violations'%(tot,bad))
