# SCRIPT: HIDDEN-G-03
# Q4 knot side, second setup for the two things HIDDEN-G-02 killed: (i) g negative real, (ii) pole d = -1/tau.
print('''WHY: HIDDEN-G-02 fitted |a| = 3..40. If g or d found there were artefacts of the small fillings, they would move when
only large fillings |a| = 20..100 are used.  If they stay put, the complex g and the per-tetrahedron pole are properties
of the family, and both kills stand.
KILL (for "the kills were artefacts"): g and d from |a| = 20..100 agree with those from |a| = 3..40 to 5% of |g| and 0.1 in d.
Also printed: -g * tau/(2 pi i), which is dz/du at the cusp if z = kappa + (dz/du) u + ..., u = 2 pi i/(1 + a tau).''')
import snappy, warnings, numpy as np
warnings.filterwarnings('ignore')
from scipy.optimize import least_squares
def fitH(a,z):
    M=np.c_[a,z,np.ones_like(a)].astype(complex); kap,dd,c=np.linalg.lstsq(M,z*a,rcond=None)[0]; g=-(c+kap*dd)
    def f(p):
        k,g_,d_=p[0]+1j*p[1],p[2]+1j*p[3],p[4]+1j*p[5]; r=(k-g_/(a-d_))-z; return np.r_[r.real,r.imag]
    s=least_squares(f,[kap.real,kap.imag,g.real,g.imag,dd.real,dd.imag],method='lm',max_nfev=4000,xtol=1e-15,ftol=1e-15).x
    return s[0]+1j*s[1],s[2]+1j*s[3],s[4]+1j*s[5]
same=tot=0
for name,cusp in (('L5a1',1),('L7a6',0),('L7a5',1)):
    M0=snappy.Manifold(name); tau=complex(M0.cusp_info(cusp)['shape']); res={}
    for lab,A in (('3..40',[a for a in range(-40,41) if abs(a)>=3]),('20..100',[a for a in range(-100,101) if abs(a)>=20])):
        Z=[]
        for a in A:
            M=snappy.Manifold(name); M.dehn_fill((1,a),cusp); Z.append([complex(z) for z in M.tetrahedra_shapes('rect')])
        Z=np.array(Z); a=np.array(A,float); res[lab]=[fitH(a,Z[:,j]) for j in range(Z.shape[1])]
    print('\n%s cusp %d, tau = %.4f%+.4fi, -1/tau = %.4f%+.4fi'%(name,cusp,tau.real,tau.imag,(-1/tau).real,(-1/tau).imag))
    for j,(r1,r2) in enumerate(zip(res['3..40'],res['20..100'])):
        ok=abs(r1[1]-r2[1])<=0.05*abs(r1[1]) and abs(r1[2]-r2[2])<=0.1; tot+=1; same+=ok
        c1=-r2[1]*tau/(2j*np.pi)
        print('   tet %d: g %+.4f%+.4fi | %+.4f%+.4fi   d %.3f%+.3fi | %.3f%+.3fi   stable %s   dz/du = %+.4f%+.4fi'%(j,r1[1].real,r1[1].imag,r2[1].real,r2[1].imag,r1[2].real,r1[2].imag,r2[2].real,r2[2].imag,ok,c1.real,c1.imag))
print('\nstable fits: %d of %d'%(same,tot))
