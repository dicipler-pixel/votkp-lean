# SCRIPT: GEO-PHASE-01
# Exploratory. Splits each element's Smith track Gamma(lambda), 380-780 nm, into two books:
#  climb = hyperbolic length of the track on the Smith (Poincare) disk, the dynamic part;
#  turn  = signed hyperbolic area between the track and the geodesic closing it, the geometric part
#          (Bargmann invariant of SU(1,1) coherent states, so this is the Berry/Montgomery-type term).
# Then: does the geometric part sort metals, does it follow the space between, and does it explain the alkali film outliers?
import sys, csv, numpy as np, warnings; warnings.filterwarnings('ignore')
from scipy.stats import spearmanr
sys.path.insert(0,'/home/claude/votkp_research'); import ri_load
S=ri_load.element_sets(); nonmetal={'B','C','Ge','Se','Si','Te'}
R={r['element']:r for r in csv.DictReader(open('/home/claude/recover/RECOVERED_ELEMENT_DATA_20261106.csv',encoding='utf-8-sig'))}
lv=np.linspace(0.38,0.78,401)
def area_green(z):            # integral of 2(x dy - y dx)/(1-r^2) around the closed path; curvature -1 area
    zc=np.append(z,z[0]); A=0
    for a,b in zip(zc[:-1],zc[1:]):
        t=np.linspace(0,1,41); w=a+(b-a)*t; m=(w[1:]+w[:-1])/2; d=np.diff(w)
        A+=np.sum(2*(m.real*d.imag-m.imag*d.real)/(1-abs(m)**2))
    return A
def geodesic(a,b,n=200):      # Poincare geodesic a->b, via the Mobius map sending a to 0
    phi=lambda z:(z-a)/(1-np.conj(a)*z); inv=lambda w:(w+a)/(1+np.conj(a)*w)
    B=phi(b); return inv(np.tanh(np.linspace(0,1,n)*np.arctanh(abs(B)))*B/abs(B))
def hlen(z): return np.sum(2*np.arctanh(abs((z[1:]-z[:-1])/(1-np.conj(z[:-1])*z[1:]))))
# check the area routine on a geodesic triangle: area = pi - angle sum
a,b,c=0.3+0.1j,-0.2+0.4j,-0.1-0.5j
tri=np.concatenate([geodesic(a,b),geodesic(b,c),geodesic(c,a)])
def ang(p,q,r):
    def tang(u,v): g=geodesic(u,v,2001); return g[1]-g[0]
    t1=tang(p,q); t2=tang(p,r); return abs(np.angle(t2/t1))
print('check: Green area %.5f  vs  pi - angle sum %.5f'%(abs(area_green(tri)),np.pi-ang(a,b,c)-ang(b,c,a)-ang(c,a,b)))
out=[]
for el,d in S.items():
    o=np.argsort(d['lam']); N=np.interp(lv,d['lam'][o],d['n'][o])+1j*np.interp(lv,d['lam'][o],d['k'][o])
    G=(1-N)/(1+N); closed=np.concatenate([G,geodesic(G[-1],G[0])[1:-1]])
    out.append((el,el not in nonmetal,area_green(closed),hlen(G),float(R[el]['space_between_E']),float(np.mean(np.abs(G)))))
out.sort(key=lambda r:r[2])
print('\n el  metal   turn=signed area   climb=length   space_between   mean|Gamma|')
for r in out: print(' %-3s %-5s   %+9.4f         %7.3f        %.3f        %.3f'%r)
A=np.array([r[2] for r in out]); L=np.array([r[3] for r in out]); Ev=np.array([r[4] for r in out]); met=np.array([r[1] for r in out]); g=np.array([r[5] for r in out])
print('\nmetals: turn range %+.4f..%+.4f | nonmetals: %+.4f..%+.4f'%(A[met].min(),A[met].max(),A[~met].min(),A[~met].max()))
print('metals: climb range %.3f..%.3f | nonmetals: %.3f..%.3f'%(L[met].min(),L[met].max(),L[~met].min(),L[~met].max()))
print('metals only: turn vs space between rho=%.2f p=%.3f ; climb vs space between rho=%.2f p=%.3f'%(*spearmanr(A[met],Ev[met]),*spearmanr(L[met],Ev[met])))
print('metals only: turn vs climb rho=%.2f ; |turn| vs mean|Gamma| rho=%.2f'%(spearmanr(A[met],L[met])[0],spearmanr(abs(A[met]),g[met])[0]))
