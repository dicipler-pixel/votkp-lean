# SCRIPT: COLKNOT-A1
# Task A(i). ONE frame for elements and knots: the Poincare/Smith disk with the vacuum point at the centre.
#   elements: G = (1-N)/(1+N)  (N = n+ik, centre G=0 is N=1, vacuum matching)
#   knots   : G = (z-w)/(z-conj w), w=e^{i pi/3}, centre = regular ideal tetrahedron
# Hyperbolic distance from the centre d = 2 artanh|G|.  Part 1: where do the two populations sit.  Part 2: bowl law.
# Bowl law = some fullness F is  F0 - c |G|^2  (quadratic well in d near the centre) with a fixed coefficient.
import sys, csv, numpy as np, snappy, re, warnings, database_knotinfo as dk
from scipy.special import spence
from scipy.stats import spearmanr
from scipy.optimize import curve_fit
import cknot_common as C
warnings.filterwarnings('ignore')
w=np.exp(1j*np.pi/3); V0=1.0149416064096536; K2=3*np.sqrt(3)/4
def Dbw(z): z=np.asarray(z,complex); return np.imag(spence(1-z))+np.angle(1-z)*np.log(np.abs(z))
def Gk(z): return (z-w)/(z-np.conj(w))
def z_of_G(g): return (w-np.conj(w)*g)/(1-g)               # inverse map: optical point -> tetrahedron shape
from mpmath import polylog
zt=0.3+1.1j; print('check D (scipy vs mpmath): %.12f %.12f'%(Dbw(zt),float(np.imag(complex(polylog(2,zt))))+np.angle(1-zt)*np.log(abs(zt))))
print('check z_of_G round trip:',abs(Gk(z_of_G(0.3-0.2j))-(0.3-0.2j)))
# ---------- knot tetrahedra (4-10 crossings, as SHAPE-DISK-01)
kd=[]; dists=[]
names=[r['name'] for r in dk.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=10]
for nm in names:
    try:
        M=snappy.Manifold(nm)
        if M.solution_type()!='all tetrahedra positively oriented': continue
        sh=np.array([complex(s) for s in M.tetrahedra_shapes('rect')])
    except Exception: continue
    g=Gk(sh); kd.append((np.abs(g),Dbw(sh)))
Gk_abs=np.concatenate([a for a,_ in kd]); Dk=np.concatenate([b for _,b in kd]); dk_=2*np.arctanh(Gk_abs)
print('\nPART 1  populations on the one disk  (distance d from the vacuum point; Schottky radius |G|^2=1/2 is d=%.3f)'%(2*np.arctanh(np.sqrt(.5))))
E=C.elements(); nm_=C.NONMETAL
G={el:C.smithG(N) for el,N in E.items()}
dm=np.array([np.median(C.hdist(G[e])) for e in E if e not in nm_]); dn=np.array([np.median(C.hdist(G[e])) for e in E if e in nm_])
def q(x): return ' '.join('%.2f'%v for v in np.percentile(x,[5,25,50,75,95]))
print('  population                      n       d at 5/25/50/75/95 pct       frac beyond Schottky radius')
rs=2*np.arctanh(np.sqrt(.5))
print('  knot tetrahedra            %6d      %s          %.3f'%(len(dk_),q(dk_),np.mean(dk_>rs)))
allm=np.concatenate([C.hdist(G[e]) for e in E if e not in nm_]); alln=np.concatenate([C.hdist(G[e]) for e in E if e in nm_])
print('  element points, metals     %6d      %s          %.3f'%(len(allm),q(allm),np.mean(allm>rs)))
print('  element points, nonmetals  %6d      %s          %.3f'%(len(alln),q(alln),np.mean(alln>rs)))
print('  per-element median d: metals %.2f..%.2f (median %.2f); nonmetals %.2f..%.2f'%(dm.min(),dm.max(),np.median(dm),dn.min(),dn.max()))
print('  knot pieces within d<%.2f: %.3f ; nonmetal element points within same: %.3f ; metal points: %.4f'%(rs,np.mean(dk_<rs),np.mean(alln<rs),np.mean(allm<rs)))
# ---------- the knot bowl, as the yardstick
x=Gk_abs**2; m=x<0.25
for lab,mask in [('all pieces',np.ones_like(x,bool)),('|G|^2<0.25',m)]:
    A=np.column_stack([np.ones(mask.sum()),-x[mask]]); (a,c),*_=np.linalg.lstsq(A,Dk[mask],rcond=None); res=Dk[mask]-A@[a,c]
    print('  knot yardstick (%s): D = %.4f - %.4f |G|^2   R^2=%.5f  (V0=%.4f, 3sqrt3/4=%.4f)'%(lab,a,c,1-res.var()/Dk[mask].var(),V0,K2))
def powfit(d,F):                                             # F = F0 - c d^p
    try:
        f=lambda d,F0,c,p: F0-c*d**p; (F0,c,p),_=curve_fit(f,d,F,p0=[F.max(),(F.max()-F.min())/max(d.max(),1)**2,2],maxfev=20000)
        r=F-f(d,F0,c,p); return p,1-r.var()/F.var()
    except Exception: return np.nan,np.nan
p,r2=powfit(dk_[m],Dk[m]); print('  knot yardstick free exponent (|G|^2<0.25): p=%.3f R^2=%.5f'%(p,r2))
# ---------- elements: fullness candidates
lv=np.linspace(0.38,0.78,401)
S=__import__('ri_load').element_sets()
def area_green(z):
    zc=np.append(z,z[0]); A=0
    for a,b in zip(zc[:-1],zc[1:]):
        t=np.linspace(0,1,41); ww=a+(b-a)*t; mm=(ww[1:]+ww[:-1])/2; d=np.diff(ww); A+=np.sum(2*(mm.real*d.imag-mm.imag*d.real)/(1-abs(mm)**2))
    return A
def geodesic(a,b,n=200):
    phi=lambda z:(z-a)/(1-np.conj(a)*z); inv=lambda ww:(ww+a)/(1+np.conj(a)*ww)
    B=phi(b); return inv(np.tanh(np.linspace(0,1,n)*np.arctanh(abs(B)))*B/abs(B))
rows={}
tt=np.arange(10,301,10.0)
for el in E:
    d=S[el]; o=np.argsort(d['lam']); N4=np.interp(lv,d['lam'][o],d['n'][o])+1j*np.interp(lv,d['lam'][o],d['k'][o]); G4=C.smithG(N4)
    closed=np.concatenate([G4,geodesic(G4[-1],G4[0])[1:-1]]); turn=abs(area_green(closed)); climb=np.sum(2*np.arctanh(abs((G4[1:]-G4[:-1])/(1-np.conj(G4[:-1])*G4[1:]))))
    g=G[el]; x=np.mean(np.abs(g)**2); dmed=np.median(C.hdist(g))
    Rb=np.abs(g)**2; Lb,Cb,hb=C.LCh(Rb)
    fr=np.abs(C.film_r(E[el],tt))**2; Lf=C.Lab(fr); Lbb=C.Lab(Rb)
    dE=np.array(__import__('colour').delta_E(Lf,np.repeat(Lbb,len(tt),0),method='CIE 2000')); 
    r01=(1-1.5)/(1+1.5); r12=np.abs((1.5-E[el])/(1.5+E[el])); a_=np.abs(r01); mod=((r12+a_)/(1+a_*r12))**2; modm=((r12-a_)/(1-a_*r12))**2
    Fm=np.mean((mod-modm)/(mod+modm))
    Dm=np.mean(Dbw(z_of_G(g)))
    rows[el]=dict(x=x,d=dmed,T=1-x,A=turn,Cl=climb,Fe=dE.mean(),Fm=Fm,L=Lb[0] if False else float(np.mean(Lb)),Ch=float(np.mean(Cb)),D=Dm)
els=list(E); X=np.array([rows[e]['x'] for e in els]); Dd=np.array([rows[e]['d'] for e in els]); met=np.array([e not in nm_ for e in els])
print('\nPART 2  bowl law on the elements  (x = mean |G|^2 over 380-780 nm; d = median hyperbolic distance)')
print('  fullness F                                   rho(F,x)   lin R^2   slope c (F=F0-c x)   F0     c/F0    free p (F=F0-c d^p)  R^2   | metals-only rho  lin R^2')
names={'T':'1-<|G|^2> (tautology, c=1 by construction)','A':'|turn| (enclosed hyperbolic area)','Cl':'climb (hyperbolic track length)','Fe':'film excursion (mean dE2000 film vs bulk, 10-300nm)','Fm':'film modulation depth (Rmax-Rmin)/(Rmax+Rmin)','L':'bulk lightness L*','Ch':'bulk chroma C*','D':'Bloch-Wigner D of the optical point read as a tetrahedron'}
for k,lab in names.items():
    F=np.array([rows[e][k] for e in els]); rho=spearmanr(X,F)[0]
    A=np.column_stack([np.ones_like(X),-X]); (a,c),*_=np.linalg.lstsq(A,F,rcond=None); r2=1-(F-A@[a,c]).var()/F.var()
    p,r2p=powfit(Dd,F)
    Fm_=F[met]; Xm=X[met]; Am=np.column_stack([np.ones_like(Xm),-Xm]); cm,*_=np.linalg.lstsq(Am,Fm_,rcond=None); r2m=1-(Fm_-Am@cm).var()/Fm_.var()
    print('  %-52s %+.2f   %.3f    %+9.3f       %8.3f %+7.3f    %6.2f   %.3f  |  %+.2f   %.3f'%(lab,rho,r2,c,a,c/a if a else np.nan,p,r2p,spearmanr(Xm,Fm_)[0],r2m))
# pointwise pooled over (element, wavelength): the transplanted knot law
g_all=np.concatenate([G[e] for e in els]); xg=np.abs(g_all)**2; Dg=Dbw(z_of_G(g_all))
mm=xg<0.25
if mm.sum()>20:
    A=np.column_stack([np.ones(mm.sum()),-xg[mm]]); (a,c),*_=np.linalg.lstsq(A,Dg[mm],rcond=None)
    print('\n  pooled element points with |G|^2<0.25 (n=%d): D(z(G)) = %.4f - %.4f |G|^2  (same map, so this is the identity of the knot law, not a new test)'%(mm.sum(),a,c))
print('  elements with any point inside |G|^2<0.25:',sorted({e for e in els if (np.abs(G[e])**2<0.25).any()}))
# the shifted vacuum: the film medium (n=1.5) moves the matching point
print('\n  film shifts the centre: with a n=1.5 film, matching is N=1.5. Smith centre for substrate N relative to film medium is Gf=(1.5-N)/(1.5+N).')
