# SCRIPT: HIDDEN-G-02
# Q4, knot side: the sign of the hidden level g in  z(a) = kappa - g/(a - d)  fitted on tetrahedron shapes along
# Dehn-filling families (SnapPy), a = the filling integer.
import snappy, warnings, numpy as np, sys
warnings.filterwarnings('ignore')
from scipy.optimize import least_squares
print('''WHAT IS FITTED
 A two-cusped link complement is filled along the slope (1, a) on one cusp; the triangulation is kept, so each
 tetrahedron j has a shape z_j(a) for every integer a.  L5a1 (Whitehead link) with (1, a) gives the twist knots
 6_1, 8_1, 10_1, ... (identified by SnapPy for a = 2, 3, 4).  Family = (link, cusp, slope type, tetrahedron).
 Model H (one hidden level, 3 complex numbers): z(a) = kappa - g/(a - d).   Model L (2 complex numbers): z = alpha + beta a.
WHY THIS CHECK DECIDES IT
 VOTKP 5.3 with one hidden level: g = -BC; a Hermitian coupling needs g NEGATIVE REAL.  A complex g means the level is
 not Hermitian-coupled (an open channel).  The sign is meaningful only if H predicts held-out fillings better than L.
 Independent check of the pole: if the one-pole form is the first-order response to the filling, d is fixed by the
 cusp shape tau of the unfilled cusp alone (d = -1/tau for slopes (1,a), d = -tau for slopes (a,1)); tau is read from
 SnapPy and is not fitted.
KILL CONDITION (written before the run)
 a = -40..-3 and 3..40 where SnapPy reports a geometric solution; fit on index mod 4 != 2, predict index mod 4 == 2.
 A family COUNTS only if held-out RMS(H) <= 0.5 * held-out RMS(L).
 Claim under test: "g is negative real" (|Im g| <= 0.05 |g| and Re g < 0) in every counted family. One counted family
 with g not negative real kills it.
OPPOSITE (same kill): the reversed slope (a, 1) (meridian and longitude exchanged).
SECOND SETUP: three other links (L6a2, L7a5, L7a6), both cusps.
''')
def shapes(name,cusp,a,kind):
    M=snappy.Manifold(name); M.dehn_fill((1,a) if kind=='(1,a)' else (a,1),cusp)
    st=M.solution_type()
    if st not in ('all tetrahedra positively oriented','contains negatively oriented tetrahedra'): return None
    return np.array([complex(z) for z in M.tetrahedra_shapes('rect')]),st
def fitH(a,z):
    M=np.c_[a,z,np.ones_like(a)].astype(complex); kap,dd,c=np.linalg.lstsq(M,z*a,rcond=None)[0]; g=-(c+kap*dd)
    def f(p):
        k,g_,d_=p[0]+1j*p[1],p[2]+1j*p[3],p[4]+1j*p[5]; r=(k-g_/(a-d_))-z; return np.r_[r.real,r.imag]
    try:
        s=least_squares(f,[kap.real,kap.imag,g.real,g.imag,dd.real,dd.imag],method='lm',max_nfev=4000).x
        return s[0]+1j*s[1],s[2]+1j*s[3],s[4]+1j*s[5]
    except Exception: return kap,g,dd
tot=dict(fam=0,counts=0,negreal=0,reneg=0); allrows=[]
def family(name,cusp,kind):
    M0=snappy.Manifold(name); tau=complex(M0.cusp_info(cusp)['shape']); kap0=np.array([complex(z) for z in M0.tetrahedra_shapes('rect')])
    A=[a for a in list(range(-40,-2))+list(range(3,41))]; data=[]
    for a in A:
        r=shapes(name,cusp,a,kind)
        if r is not None and r[1]=='all tetrahedra positively oriented': data.append((a,r[0]))
    if len(data)<24: print('\n%s cusp %d slopes %s: only %d geometric fillings, skipped'%(name,cusp,kind,len(data))); return
    a=np.array([d[0] for d in data],float); Z=np.array([d[1] for d in data]); n=len(a)
    tr=np.array([i for i in range(n) if i%4!=2]); te=np.array([i for i in range(n) if i%4==2])
    dpred=-1/tau if kind=='(1,a)' else -tau
    print('\n%s cusp %d slopes %s: %d fillings, cusp shape tau = %.4f%+.4fi, predicted pole d = %.4f%+.4fi'%(name,cusp,kind,n,tau.real,tau.imag,dpred.real,dpred.imag))
    print('   tet   kappa (fit)        cusped shape        g                   arg g/pi   d (fit)            |d-dpred|   RMS H     RMS L    counts  g negative real')
    for j in range(Z.shape[1]):
        z=Z[:,j]; kap,g,dd=fitH(a[tr],z[tr]); pH=kap-g/(a[te]-dd); cL=np.polyfit(a[tr],z[tr],1); pL=np.polyval(cL,a[te])
        rH=np.sqrt(np.mean(abs(pH-z[te])**2)); rL=np.sqrt(np.mean(abs(pL-z[te])**2)); counts=rH<=0.5*rL
        neg=(abs(g.imag)<=0.05*abs(g)) and g.real<0
        tot['fam']+=1; tot['counts']+=counts; tot['negreal']+=(counts and neg); tot['reneg']+=(counts and g.real<0)
        allrows.append((name,cusp,kind,j,g,dd,dpred,counts))
        print('   %d   %.4f%+.4fi   %.4f%+.4fi   %+.4f%+.4fi   %+.3f    %.3f%+.3fi   %.3f      %.1e  %.1e  %s   %s'%(j,kap.real,kap.imag,kap0[j].real,kap0[j].imag,g.real,g.imag,np.angle(g)/np.pi,dd.real,dd.imag,abs(dd-dpred),rH,rL,counts,neg))
for name,cusp in (('L5a1',1),('L5a1',0)): family(name,cusp,'(1,a)')
print('\n===== OPPOSITE: slopes (a,1)')
for name,cusp in (('L5a1',1),('L5a1',0)): family(name,cusp,'(a,1)')
print('\n===== SECOND SETUP: other links')
for name in ('L6a2','L7a5','L7a6'):
    for cusp in (0,1): family(name,cusp,'(1,a)')
print('\nTOTAL: (family, tetrahedron) fits %d ; counted %d ; counted with g negative real %d ; counted with Re g < 0: %d, Re g > 0: %d'%(tot['fam'],tot['counts'],tot['negreal'],tot['reneg'],tot['counts']-tot['reneg']))
c=[r for r in allrows if r[7]]
print('pole check on counted fits: median |d - d_pred| = %.3f ; within 0.15 of d_pred: %d of %d'%(np.median([abs(r[5]-r[6]) for r in c]),sum(abs(r[5]-r[6])<0.15 for r in c),len(c)))
print('arg(g)/pi over counted fits: min %.3f max %.3f'%(min(np.angle(r[4])/np.pi for r in c),max(np.angle(r[4])/np.pi for r in c)))
