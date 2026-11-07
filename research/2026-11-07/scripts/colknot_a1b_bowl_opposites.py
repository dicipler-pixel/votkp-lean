# SCRIPT: COLKNOT-A1B
# Opposites for A(i). (1) which radial form fits each fullness: linear in |G|, |G|^2, d, d^2, or cosh d - 1 (hyperbolic disk area)?
# (2) re-centre the disk: the film medium (n=1.5) moves the matching point; scan the centre n0 in 1..3 for the best quadratic well.
# (3) 'emptiness' reading for turn/climb (they grow toward the rim, so test them as a rising bowl, F = c*(cosh d - 1)).
import numpy as np, colour, warnings; warnings.filterwarnings('ignore')
from scipy.stats import spearmanr
import cknot_common as C
E=C.elements(); els=list(E); nm_=C.NONMETAL; tt=np.arange(10,301,10.0)
def r2(F,x):
    A=np.column_stack([np.ones_like(x),x]); c,*_=np.linalg.lstsq(A,F,rcond=None); return 1-(F-A@c).var()/F.var()
def feats(n0):
    out={}
    for el in els:
        N=E[el]; g=(n0-N)/(n0+N)                                   # Smith point relative to a reference medium n0
        out[el]=g
    return out
# fullness candidates that do not depend on n0 (computed once)
F={}
for el in els:
    Rb=np.abs(C.smithG(E[el]))**2; Lb,Cb,hb=C.LCh(Rb)
    Lf=C.Lab(np.abs(C.film_r(E[el],tt))**2); Lbb=C.Lab(Rb)
    dE=np.array(colour.delta_E(Lf,np.repeat(Lbb,len(tt),0),method='CIE 2000')).mean()
    a=0.2; r12=np.abs((1.5-E[el])/(1.5+E[el])); mod=((r12+a)/(1+a*r12))**2; modm=((r12-a)/(1-a*r12))**2
    F[el]=dict(Fe=dE,Fm=np.mean((mod-modm)/(mod+modm)),L=float(np.mean(Lb)))
names={'Fe':'film excursion dE2000','Fm':'film modulation depth','L':'bulk lightness L*'}
print('(1) R^2 of F against each radial form, centre = vacuum (N=1); G averaged over 380-780 nm per element')
g1=feats(1.0); xs={e:np.mean(np.abs(g1[e])**2) for e in els}
forms={'|G|':lambda g:np.mean(np.abs(g)),'|G|^2':lambda g:np.mean(np.abs(g)**2),'d':lambda g:np.mean(C.hdist(g)),'d^2':lambda g:np.mean(C.hdist(g)**2),'cosh d -1':lambda g:np.mean(np.cosh(C.hdist(g))-1)}
print('  F                          '+'  '.join('%9s'%k for k in forms))
for k,lab in names.items():
    Fv=np.array([F[e][k] for e in els]); print('  %-26s'%lab+'  '.join('%9.3f'%r2(Fv,np.array([f(g1[e]) for e in els])) for f in forms.values()))
print('\n(2) recentre: R^2 of F vs mean |G_n0|^2 where G_n0=(n0-N)/(n0+N); best centre in bold-ish (max)')
n0s=np.round(np.arange(1.0,3.01,0.25),2)
print('  n0:                        '+'  '.join('%6.2f'%v for v in n0s))
for k,lab in names.items():
    Fv=np.array([F[e][k] for e in els]); rr=[r2(Fv,np.array([np.mean(np.abs(feats(n0)[e])**2) for e in els])) for n0 in n0s]
    print('  %-26s'%lab+'  '.join('%6.3f'%v for v in rr)+'   best n0=%.2f'%n0s[int(np.argmax(rr))])
print('(3) turn and climb as a rising hyperbolic bowl; per-element mean d from the vacuum')
import ri_load
S=ri_load.element_sets(); lv=np.linspace(0.38,0.78,401)
def area_green(z):
    zc=np.append(z,z[0]); A=0
    for a,b in zip(zc[:-1],zc[1:]):
        t=np.linspace(0,1,41); ww=a+(b-a)*t; mm=(ww[1:]+ww[:-1])/2; d=np.diff(ww); A+=np.sum(2*(mm.real*d.imag-mm.imag*d.real)/(1-abs(mm)**2))
    return A
def geodesic(a,b,n=200):
    phi=lambda z:(z-a)/(1-np.conj(a)*z); inv=lambda ww:(ww+a)/(1+np.conj(a)*ww)
    B=phi(b); return inv(np.tanh(np.linspace(0,1,n)*np.arctanh(abs(B)))*B/abs(B))
T=[];Cl=[];dm=[];dmax=[];dmin=[]
for el in els:
    d=S[el]; o=np.argsort(d['lam']); G4=C.smithG(np.interp(lv,d['lam'][o],d['n'][o])+1j*np.interp(lv,d['lam'][o],d['k'][o]))
    cl=np.concatenate([G4,geodesic(G4[-1],G4[0])[1:-1]]); T.append(abs(area_green(cl)))
    Cl.append(np.sum(2*np.arctanh(abs((G4[1:]-G4[:-1])/(1-np.conj(G4[:-1])*G4[1:]))))); h=C.hdist(G4); dm.append(h.mean()); dmax.append(h.max()); dmin.append(h.min())
T,Cl,dm,dmax,dmin=map(np.array,(T,Cl,dm,dmax,dmin))
print('  |turn| vs:  d_mean R^2 %.3f | d_mean^2 %.3f | cosh(d_mean)-1 %.3f | e^{d_mean} %.3f | log|turn| vs d_mean slope R^2 %.3f'%(r2(T,dm),r2(T,dm**2),r2(T,np.cosh(dm)-1),r2(T,np.exp(dm)),r2(np.log(T+1e-6),dm)))
print('  climb vs:   d_mean R^2 %.3f | d_mean^2 %.3f | cosh(d_mean)-1 %.3f | e^{d_mean} %.3f'%(r2(Cl,dm),r2(Cl,dm**2),r2(Cl,np.cosh(dm)-1),r2(Cl,np.exp(dm))))
print('  turn vs climb: rho %.2f ;  turn vs d_min rho %.2f ; turn vs d_max rho %.2f'%(spearmanr(T,Cl)[0],spearmanr(T,dmin)[0],spearmanr(T,dmax)[0]))
nmask=np.array([e in nm_ for e in els]); print('  nonmetals |turn|:',dict(zip(np.array(els)[nmask],np.round(T[nmask],3))),' (near the vacuum point -> ~0)')
