# SCRIPT: DRAWING-POLY-03
# Validate the drawing rule (positive and negative crossings: (b,d) = under pair, a,c from the over pair reversed) on
# more knots, alternating and non-alternating, and then read OUR POLYNOMIAL off the drawing: the values of one crossing
# ratio u = z_b/z_a across all solutions are the roots of a polynomial. Self-check: if every root was found, the monic
# polynomial built from them has rational coefficients (tested by rounding a scaled version to integers).
import numpy as np, snappy, warnings, database_knotinfo as d
from fractions import Fraction
warnings.filterwarnings('ignore')
from drawing_poly_01 import build, solve, V0
from drawing_poly_02 import crossings_from
R=('under',0,1)
names=['4_1','5_2','6_1','6_2','6_3','7_2','7_4','8_20','8_21','8_5']
w=np.exp(1j*np.pi/3)
for nm in names:
    cr,n=crossings_from(nm,R,R); T=build(cr); sols=solve(T,n,starts=150)
    vals=[V0(T,z,n) for z in sols]
    if not vals: print(nm,'no solutions'); continue
    best=max(vals,key=lambda v:v.imag); cv=complex(snappy.Manifold(nm).complex_volume())
    dcs=((-best.real-cv.imag)+np.pi**2/2)%np.pi**2-np.pi**2/2
    a,b,c,dd=cr[0]; us=[]
    for z in sols:
        u=z[b]/z[a]
        if not any(abs(u-x)<1e-7 for x in us): us.append(u)
    coef=np.poly(us)                                    # monic polynomial with these roots
    def ratl(x):
        f=Fraction(x).limit_denominator(1000); return f, abs(float(f)-x)
    rc=[ratl(cf.real) for cf in coef]; ok=all(e<1e-6 for _,e in rc) and np.max(abs(coef.imag))<1e-6
    print('%-5s sides %2d | vol %.6f vs %.6f  cs miss %.1e | ratio roots %d | rational poly: %s %s'%(
        nm,n,best.imag,cv.real,abs(dcs),len(us),ok,[str(f) for f,_ in rc] if ok and len(us)<=8 else ''))
