# SCRIPT: DRAWING-POLY-06
# Write the decay-direction polynomial out in full for small knots, from the drawing alone.
# Root per geometry: r = exp(lam*V0) with lam = 2i/pi, so |r| = exp(-2 vol/pi) (decay) and arg r = -2 cs/pi (direction);
# the pi^2 period of cs maps to one full turn. P_K(x) = prod (x - r), expanded.
import numpy as np, snappy, warnings, sys
warnings.filterwarnings('ignore')
from drawing_poly_01 import build, solve, V0
from drawing_poly_02 import crossings_from
R=('under',0,1); P2=np.pi**2; lam=2j/np.pi
for nm in (sys.argv[1:] or ['4_1','5_2']):
    cr,n=crossings_from(nm,R,R); T=build(cr); sols=solve(T,n,starts=400,seed=7)
    spec=[]
    for z in sols:
        v=V0(T,z,n); vol=v.imag; cs=((-v.real+P2/2)%P2)-P2/2
        key=(round(vol,6),round(cs,6))
        if key not in spec: spec.append(key)
    spec.sort(reverse=True)
    roots=[np.exp(lam*complex(-cs,vol)) for vol,cs in spec]
    coef=np.poly(roots)
    cv=complex(snappy.Manifold(nm).complex_volume())
    print('KNOT',nm,'| SnapPy vol %.6f cs %.6f'%(cv.real,((cv.imag+P2/2)%P2)-P2/2))
    for (vol,cs),r in zip(spec,roots):
        print('  geometry: decay(vol)=%+.6f direction(cs)=%+.6f  root=%.6f%+.6fi  |r|=%.6f  turn=%+.6f'%(vol,cs,r.real,r.imag,abs(r),np.angle(r)/(2*np.pi)))
    print('  coefficients (x^%d first):'%len(roots),' '.join('%.6f%+.6fi'%(c.real,c.imag) for c in coef))
