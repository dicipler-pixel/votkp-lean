# SCRIPT: SHAPE-DISK-01
# What VOTKP seeks, on the Smith disk. Each hyperbolic knot complement is glued from ideal tetrahedra; each has a shape z
# (a cross-ratio, Im z > 0) and contributes Bloch-Wigner volume D(z). Put every shape on a Smith disk centred on the
# regular tetrahedron w = e^{i pi/3}:  G = (z - w)/(z - conj(w)).
# Why this tests the picture:
#  (1) the axis switches z -> 1/(1-z) -> 1-1/z should become exact 120-degree turns of G about the centre, with D unchanged
#      (racket: axis switches, the conserved quantity stays);
#  (2) the regular tetrahedron (max volume 1.01494) sits at the vacuum point G = 0 and flat ones (z real) on the rim;
#  (3) the climb book (hyperbolic distance of G from the centre) should then carry each tetrahedron's volume, and the
#      knot's volume should be read from how close its pieces sit to the vacuum.
# Also: the turn book (angle of G) against the Chern-Simons half, per knot (snappy complex volume).
import numpy as np, snappy, warnings, database_knotinfo as d, re
from mpmath import polylog
from scipy.stats import spearmanr
warnings.filterwarnings('ignore')
w=np.exp(1j*np.pi/3)
def D(z): return float(np.imag(complex(polylog(2,z))))+np.angle(1-z)*np.log(abs(z))
def G(z): return (z-w)/(z-np.conj(w))
# (1),(2)
z=0.3+1.1j; zs=[z,1/(1-z),1-1/z]
print('(1) D on the three axis labels:',[round(D(x),10) for x in zs])
print('    angles of G (deg):',[round(np.degrees(np.angle(G(x))),6) for x in zs],' radii:',[round(abs(G(x)),10) for x in zs])
print('(2) regular tetrahedron: G =',abs(G(w)),' D =',round(D(w),6),' ; nearly flat z=2+1e-6i: |G| =',round(abs(G(2+1e-6j)),6))
# (3) per tetrahedron and per knot
pts=[]; knots=[]
names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=10]
for nm in names:
    try:
        M=snappy.Manifold(nm)
        if M.solution_type()!='all tetrahedra positively oriented': continue
        sh=[complex(s) for s in M.tetrahedra_shapes('rect')]; cv=complex(M.complex_volume())
    except Exception: continue
    g=np.array([G(s) for s in sh]); dist=2*np.arctanh(np.abs(g)); dv=np.array([D(s) for s in sh])
    for a,b in zip(dist,dv): pts.append((a,b))
    knots.append((nm,cv.real,cv.imag,len(sh),dist,dv,g))
P=np.array(pts)
print('(3) tetrahedra:',len(P),' from',len(knots),'knots')
print('    per tetrahedron: distance from vacuum vs volume  rho=%.3f'%spearmanr(P[:,0],P[:,1])[0])
for lo,hi in [(0,0.5),(0.5,1),(1,1.5),(1.5,2.5),(2.5,9)]:
    m=(P[:,0]>=lo)&(P[:,0]<hi)
    if m.sum(): print('      distance %.1f-%.1f: n=%4d  volume %.3f..%.3f (mean %.3f)'%(lo,hi,m.sum(),P[m,1].min(),P[m,1].max(),P[m,1].mean()))
vol=np.array([k[1] for k in knots]); cs=np.array([k[2] for k in knots]); nt=np.array([k[3] for k in knots])
fill=np.array([np.sum(np.cos(np.arctan(0.5*k[4]))**2) for k in knots])     # placeholder radial weight, tested below
rad=np.array([np.sum(1-np.abs(k[6])**2) for k in knots])                     # how much of each piece is 'vacuum'
print('    per knot: volume vs number of pieces rho=%.3f ; vs summed (1-|G|^2) rho=%.3f'%(spearmanr(nt,vol)[0],spearmanr(rad,vol)[0]))
print('    volume / summed (1-|G|^2): mean %.4f  spread (std/mean) %.3f'%(np.mean(vol/rad),np.std(vol/rad)/np.mean(vol/rad)))
turn=np.array([np.sum(np.angle(k[6]**3)) for k in knots])                    # 3-fold-invariant angle of each piece
print('(4) turn: summed 3-fold angle vs CS  rho=%.3f ; |.| vs |CS| rho=%.3f'%(spearmanr(turn,cs)[0],spearmanr(abs(turn),abs(cs))[0]))
# (5) the vacuum-well law at knot level: Vol ~ sum over pieces of [V0 - (3 sqrt3/4)|G|^2]  (no fitting)
V0=1.0149416064096536; k2=3*np.sqrt(3)/4
pred=np.array([np.sum(V0-k2*np.abs(k[6])**2) for k in knots])
err=(pred-vol)/vol
print('(5) well law, no fit: median |error| %.2f%%, 90th pct %.2f%%, worst %.2f%% (%s)'%(100*np.median(abs(err)),100*np.percentile(abs(err),90),100*abs(err).max(),knots[int(np.argmax(abs(err)))][0]))
print('    pieces at full volume alone (n*V0): median |error| %.2f%%'%(100*np.median(abs(nt*V0-vol)/vol)))
