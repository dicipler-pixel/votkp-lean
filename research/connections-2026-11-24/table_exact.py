# SCRIPT: CONNECT-TABLE-EXACT-01
# Lead L3 and the table / moment-ladder / Smith-disc joins.
# Derivation tested: pairs of periods (left-step order) end at Z = 4, 20, 56, 120 = (2n)(2n+1)(2n+2)/6, every second
# tetrahedral number. So 6Z = m^3 - m with m = 2n+1 odd: in the coordinate m(Z) (real root of m^3 - m = 6Z) the pair
# ends sit exactly on 3, 5, 7, 9 and the wavelength is exactly 2; the cube-root coordinate is m - 1/(3m) - ...
# KILL LINES (written before the run):
#  T1 m(4), m(20), m(56), m(120) not equal to 3, 5, 7, 9 -> the derivation is wrong.
#  T2 for at least 3 of the 5 passing properties the best pair wavelength in the coordinate m must lie in 1.95..2.05,
#     otherwise "exact wavelength 2 in the tetrahedral coordinate" failed.
#  T3 a synthetic pure pair sawtooth (linear in Z inside each true pair, Z = 1..86) fitted the same way in (6Z)^(1/3)
#     must itself come out above 2.05; otherwise the excess 2.13 is not explained by finite-Z counting.
#  T4 polarizability against ionization energy: the fitted pair waves must be in antiphase (correlation of the two fitted
#     periodic parts below -0.8); otherwise "polarizability carries the same wave with opposite sign" failed.
#  T5 neighbour Gamma of first ionization energy, Gamma = (I(Z+1)-I(Z))/(I(Z+1)+I(Z)): pair-wave share must exceed the 99th
#     percentile of 300 shuffles; otherwise "the neighbour Gamma is not a wave" stands (as the earlier README found).
import numpy as np, warnings; warnings.filterwarnings('ignore')
from mendeleev import element
E=[element(z) for z in range(1,87)]; Z=np.arange(1,87,dtype=float)
def col(f):
    o=[]
    for e in E:
        try: v=f(e)
        except Exception: v=None
        o.append(np.nan if v is None else float(v))
    return np.array(o)
IE=col(lambda e:e.ionenergies[1]); AL=col(lambda e:e.dipole_polarizability)
props={'log ionization energy':np.log(IE),'electronegativity':col(lambda e:e.en_pauling),'log covalent radius':np.log(col(lambda e:e.covalent_radius_pyykko)),
       'log polarizability':np.log(AL),'log melting point':np.log(col(lambda e:e.melting_point))}
def mco(z): 
    return np.array([max(np.roots([1,0,-1,-6*q]).real[np.abs(np.roots([1,0,-1,-6*q]).imag)<1e-9]) for q in np.atleast_1d(z)])
print('T1 m(Z) at Z = 4, 20, 56, 120:',np.round(mco([4,20,56,120]),10),'; cube-root coordinate there:',np.round((6*np.array([4,20,56,120.]))**(1/3),4),'spacings',np.round(np.diff((6*np.array([4,20,56,120.]))**(1/3)),4))
print('   noble gases 2, 18, 54, 118 in the cube-root coordinate:',np.round((6*np.array([2,18,54,118.]))**(1/3),4),'spacings',np.round(np.diff((6*np.array([2,18,54,118.]))**(1/3)),4))
print('   mid-pair noble gases 10, 36, 86:',np.round((6*np.array([10,36,86.]))**(1/3),4),'spacings',np.round(np.diff((6*np.array([10,36,86.]))**(1/3)),4))
H=3; lam=np.arange(1.60,2.801,0.005)
def design(u,L): return np.hstack([np.c_[np.ones_like(u),u]]+[np.c_[np.sin(2*np.pi*h*u/L),np.cos(2*np.pi*h*u/L)] for h in range(1,H+1)])
def fit(u,y,L):
    A0=np.c_[np.ones_like(u),u]; r0=y-A0@np.linalg.lstsq(A0,y,rcond=None)[0]
    A=design(u,L); c=np.linalg.lstsq(A,y,rcond=None)[0]; r=y-A@c; return 1-(r@r)/(r0@r0), A[:,2:]@c[2:]
def best(u,y):
    v=[fit(u,y,L)[0] for L in lam]; k=int(np.argmax(v)); return v[k],lam[k]
coords={'cube root (6Z)^(1/3)':lambda z:(6*z)**(1/3),'tetrahedral m(Z)':mco,'tetrahedral m(Z+2)':lambda z:mco(z+2)}
print('\nbest pair wave: share of variance and wavelength, in three coordinates')
inband=0
for name,yy in props.items():
    m=~np.isnan(yy); out=[]
    for cn,cf in coords.items():
        r,L=best(cf(Z[m]),yy[m]); out.append('%s: %.3f at %.3f'%(cn,r,L))
        if cn=='tetrahedral m(Z)': inband+=(1.95<=L<=2.05); 
    r2fix=fit(mco(Z[m]),yy[m],2.0)[0]
    print('  %-24s'%name,' | '.join(out),' | m(Z) with wavelength fixed at 2: %.3f'%r2fix)
print('T2 properties with m-coordinate wavelength inside 1.95..2.05:',inband,'of 5','HELD' if inband>=3 else 'FIRED')
# T3 synthetic sawtooth
ends=[0,4,20,56,120]
def phase(z,shift=0):
    z=z+shift
    for a,b in zip(ends[:-1],ends[1:]):
        if a<z<=b: return (z-a)/(b-a)
    return 0.0
for sh,lab in ((0,'pair ends at alkaline earths (4, 20, 56)'),(2,'pair ends at noble gases (2, 18, 54)')):
    y=np.array([phase(z,sh) for z in Z]); r,L=best((6*Z)**(1/3),y); r2,L2=best(mco(Z),y)
    print('T3 synthetic sawtooth,',lab,': cube-root coordinate wavelength %.3f (share %.3f); m coordinate %.3f (share %.3f)'%(L,r,L2,r2), ('HELD' if L>2.05 else 'FIRED'))
# T4 phase and shape sharing at the fixed exact wavelength 2 in m
u=mco(Z); waves={}
for name,yy in props.items():
    m=~np.isnan(yy); A=design(u[m],2.0); c=np.linalg.lstsq(A,yy[m],rcond=None)[0]; waves[name]=design(u,2.0)[:,2:]@c[2:]
names=list(waves); print('\ncorrelation between the fitted pair waves (wavelength 2 in m), all 86 positions')
for i in range(5):
    print('  %-24s'%names[i],' '.join('%+.2f'%np.corrcoef(waves[names[i]],waves[names[j]])[0,1] for j in range(5)))
c=np.corrcoef(waves['log ionization energy'],waves['log polarizability'])[0,1]; print('T4 ionization energy against polarizability: %.3f'%c,'HELD' if c<-0.8 else 'FIRED')
sv=np.linalg.svd(np.array([w/np.linalg.norm(w) for w in waves.values()]),compute_uv=False); print('   one common shape carries %.3f of the five normalised waves (singular values %s)'%(sv[0]**2/(sv**2).sum(),np.round(sv,3)))
# first-harmonic phases
for name,yy in props.items():
    m=~np.isnan(yy); c=np.linalg.lstsq(design(u[m],2.0),yy[m],rcond=None)[0]; print('   first-harmonic phase of %-22s %7.1f degrees, amplitude %.3f'%(name,np.degrees(np.arctan2(c[2],c[3])),np.hypot(c[2],c[3])))
# slopes: moment-ladder reading alpha = S(-2)
la,li,lr=np.log(AL),np.log(IE),props['log covalent radius']
for x,xn in ((li,'log ionization energy'),(lr,'log covalent radius')):
    A=np.c_[np.ones(86),x]; c=np.linalg.lstsq(A,la,rcond=None)[0]; r=la-A@c; print('   log polarizability = %.2f + (%.3f) x %s ; share explained %.3f'%(c[0],c[1],xn,1-(r@r)/((la-la.mean())@(la-la.mean()))))
# T5 neighbour Gamma
G=(IE[1:]-IE[:-1])/(IE[1:]+IE[:-1]); zg=Z[:-1]+0.5; rng=np.random.default_rng(7)
for cn,cf in (('cube root',lambda z:(6*z)**(1/3)),('m',mco)):
    r,L=best(cf(zg),G); sh=[best(cf(zg),rng.permutation(G))[0] for _ in range(300)]; q=np.percentile(sh,99)
    print('T5 neighbour Gamma of ionization energy,',cn,'coordinate: share %.3f at wavelength %.3f ; 99th percentile of shuffles %.3f'%(r,L,q),'HELD' if r>q else 'FIRED')
# Gamma between pair-partners: element Z against the element one true period-pair-half later is not defined uniformly; skipped.
