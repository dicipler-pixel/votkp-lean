# SCRIPT: DRAWING-POLY-05
# From the drawing alone: the spectrum of V0 values, one per solution family = one per boundary-parabolic geometry of the
# knot. Each value is decay (Im V0 = volume of that geometry) + direction (Re V0 = -cs mod pi^2). The largest decay is the
# knot's own volume (Cho). Compare with SnapPy's geometric complex volume and with the ROOTS-DISK volume ladder.
import numpy as np, snappy, warnings
warnings.filterwarnings('ignore')
from drawing_poly_01 import build, solve, V0
from drawing_poly_02 import crossings_from
R=('under',0,1); P2=np.pi**2
for nm in ['4_1','5_2','6_1','6_2','6_3']:
    cr,n=crossings_from(nm,R,R); T=build(cr); sols=solve(T,n,starts=220,seed=7)
    spec=[]
    for z in sols:
        v=V0(T,z,n); key=(round(v.imag,5),round(((-v.real+P2/2)%P2)-P2/2,4))
        if key not in spec: spec.append(key)
    spec.sort(reverse=True); cv=complex(snappy.Manifold(nm).complex_volume())
    print('%-4s from the drawing, (decay = vol, direction = cs) per geometry:'%nm, spec, '| SnapPy: (%.5f, %.4f)'%(cv.real,((cv.imag+P2/2)%P2)-P2/2))
