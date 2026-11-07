# SCRIPT: BOWL-LAW-KNOTS-02 (same as -01 with max crossing number as argument, 13 reproduces the 12,9xx-knot run)
# Task 2b: knot-level volume law on all hyperbolic KnotInfo knots up to 12 crossings (snappy all-positive shapes), with and without the exact cubic term.
# Per tetra (G=(z-w)/(z-conj w), w=e^{i pi/3}): D = V0 - (3 sqrt3/4)|G|^2 + (sqrt3/4) Re(G^3) + (3 sqrt3/16)|G|^4 + O(|G|^5)  [BOWL-CUBIC-01, exact c3=sqrt3/8, phi=0].
# Laws (no fitting): L0 = sum [V0 - k2|G|^2]; L1 = L0 + (sqrt3/4) sum Re(G^3); L1b = L1 + (3 sqrt3/16) sum |G|^4;
# opposite (hyperbolic distance instead of |G|): with s = artanh|G| (= half the disk distance): H0 = sum [V0 - k2 s^2]; H1 = H0 + (sqrt3/4) sum s^3 cos(3 theta).
# Why this tests the cubic term: a true local Taylor term must reduce the knot-level error where 3-fold-asymmetric pieces dominate (worst case 12a_803);
# if it only moved error around, the median would not improve. Kill condition: L1 not better than L0 in median AND worst -> cubic term rejected at knot level.
import numpy as np, snappy, warnings, re, database_knotinfo as d, sys
from scipy.special import spence
warnings.filterwarnings('ignore')
w=np.exp(1j*np.pi/3); V0=1.0149416064096536; k2=3*np.sqrt(3)/4
def D(z): z=np.asarray(z,complex); return np.imag(spence(1-z))+np.angle(1-z)*np.log(abs(z))
# sanity vs mpmath
from mpmath import polylog
zt=0.3+1.1j; assert abs(D(zt)-(float(np.imag(complex(polylog(2,zt))))+np.angle(1-zt)*np.log(abs(zt))))<1e-12
MAXC=int(sys.argv[1]) if len(sys.argv)>1 else 12
names=[r['name'] for r in d.link_list() if re.match(r'^\d+[an]?_\d+$',r['name'] or '') and int(re.match(r'^(\d+)',r['name']).group(1))<=MAXC]
print('KnotInfo knot names (<=12 crossings):',len(names)); sys.stdout.flush()
rows=[]; skipped=0
for nm in names:
    cand=[nm] if re.match(r'^\d+_\d+$',nm) else ['K'+nm.replace('_','')]
    M=None
    for c in cand+['K'+nm.replace('_','')]:
        try: M=snappy.Manifold(c); break
        except Exception: M=None
    if M is None: skipped+=1; continue
    try:
        if M.solution_type()!='all tetrahedra positively oriented': skipped+=1; continue
        z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); vol=float(M.volume())
    except Exception: skipped+=1; continue
    g=(z-w)/(z-np.conj(w)); a=abs(g); s=np.arctanh(np.minimum(a,1-1e-15)); th=np.angle(g)
    sumD=float(np.sum(D(z)))
    L0=np.sum(V0-k2*a**2); c3=np.sqrt(3)/4*np.sum((g**3).real); L1=L0+c3; L1b=L1+3*np.sqrt(3)/16*np.sum(a**4)
    H0=np.sum(V0-k2*s**2); H1=H0+np.sqrt(3)/4*np.sum(s**3*np.cos(3*th))
    rows.append((nm,len(z),vol,sumD,L0,L1,L1b,H0,H1,a.max()))
print('hyperbolic with positive shapes:',len(rows),'; skipped (non-geometric / not parsed):',skipped)
R=np.array([r[2:] for r in rows],float); vol=R[:,0]
print('sum of D over pieces equals snappy volume: max |diff| = %.2e'%np.max(abs(R[:,1]-vol)))
labels=['L0  bowl (as before)','L1  + exact cubic','L1b + cubic + |G|^4','H0  hyperbolic-distance bowl','H1  hyperbolic-distance + cubic']
print('\n%-34s %9s %9s %9s %9s  worst knot'%('law (no fit)','median%','mean%','90th%','worst%'))
for j,lab in enumerate(labels):
    e=abs(R[:,2+j]-vol)/vol*100; k=int(np.argmax(e))
    print('%-34s %9.3f %9.3f %9.3f %9.2f  %s (n=%d)'%(lab,np.median(e),np.mean(e),np.percentile(e,90),e.max(),rows[k][0],rows[k][1]))
for tgt in ['12a_803']:
    r=[x for x in rows if x[0]==tgt]
    if r:
        r=r[0]; v=r[2]; print('\n%s: n=%d vol=%.6f ; max|G|=%.4f'%(tgt,r[1],v,r[9]))
        for j,lab in enumerate(labels): print('   %-34s predicted %.6f  error %+.2f%%'%(lab,r[4+j],100*(r[4+j]-v)/v))
# improvement count
e0=abs(R[:,2]-vol); e1=abs(R[:,3]-vol); e1b=abs(R[:,4]-vol)
print('\nknots where cubic term lowers the error: %d of %d (%.1f%%); where it raises it: %d'%(np.sum(e1<e0),len(e0),100*np.mean(e1<e0),np.sum(e1>e0)))
print('knots where cubic+quartic lowers the error vs L0: %d of %d'%(np.sum(e1b<e0),len(e0)))
# error vs max|G| (where is the law bad?)
mg=R[:,-1]
for lo,hi in [(0,.5),(.5,.8),(.8,.95),(.95,1.01)]:
    m=(mg>=lo)&(mg<hi)
    if m.sum(): print('max|G| in [%.2f,%.2f): n=%5d  median err L0 %.3f%% -> L1 %.3f%% -> L1b %.3f%% ; H0 %.3f%% H1 %.3f%%'%(lo,hi,m.sum(),*[100*np.median(abs(R[m,2+j]-vol[m])/vol[m]) for j in (0,1,2,3,4)]))
np.save('/home/claude/votkp_research/bowl_law_knots_01_c%d.npy'%MAXC+'',R)
import json; json.dump([r[0] for r in rows],open('/home/claude/votkp_research/bowl_law_knots_01_names_c%d.json'%MAXC+'','w'))
