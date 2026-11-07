# SCRIPT: DRAWING-POLY-04
# Which per-crossing quantity is fixed along each solution family (so it can be a root of a polynomial)?
# Candidates per crossing: the four ratios, and the cross-ratio X = z_b z_d/(z_a z_c). Measured spread within the family
# of the geometric solution (all solutions with Im V0 = vol) for 4_1 and 5_2.
import numpy as np, warnings
warnings.filterwarnings('ignore')
from drawing_poly_01 import build, solve, V0
from drawing_poly_02 import crossings_from
R=('under',0,1)
for nm,vol in [('4_1',2.0298832128),('5_2',2.8281220883)]:
    cr,n=crossings_from(nm,R,R); T=build(cr); sols=solve(T,n,starts=120)
    geo=[z for z in sols if abs(V0(T,z,n).imag-vol)<1e-6]
    print(nm,'geometric-family solutions:',len(geo))
    for ci,(a,b,c,dd) in enumerate(cr):
        cand={'zb/za':[z[b]/z[a] for z in geo],'zd/zc':[z[dd]/z[c] for z in geo],'X=zb zd/(za zc)':[z[b]*z[dd]/(z[a]*z[c]) for z in geo]}
        print('  crossing %d spread:'%ci,{k:'%.1e'%np.ptp(np.abs(np.array(v)-np.array(v)[0])) for k,v in cand.items()},' X =',np.round(cand['X=zb zd/(za zc)'][0],6))
