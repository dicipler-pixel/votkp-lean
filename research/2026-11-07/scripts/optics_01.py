# SCRIPT: OPTICS-01
# Exploratory, on published optical constants (refractiveindex.info, one widest tabulated n,k set per element; 41 elements).
# (X02) Quantum metric of the occupied subspace from absorption (Souza-Wilkens-Martin / Resta):
#   localization spread ~ int Re sigma / w dw = eps0 * int eps2 dw,  eps2 = 2 n k.
#   Read how I(w_low) = int_{w_low}^{w_max} eps2 dw grows as the lower cut moves into the infrared:
#   slope d ln I / d ln w_low near -2 (Drude eps2 ~ 1/w^3): the metric diverges -> conductor; near 0: it settles -> insulator.
# (P3) Schottky line |Gamma|^2 = 1/2 on the Smith disk: mean visible |Gamma|^2 of each element against its metal label.
import sys, numpy as np
sys.path.insert(0,'/home/claude/votkp_research'); import ri_load
S=ri_load.element_sets()
nonmetal={'B','C','Ge','Se','Si','Te'}
rows=[]
for el,d in S.items():
    lam,n,k=d['lam'],d['n'],d['k']; w=1.23984/lam; o=np.argsort(w); w,n,k=w[o],n[o],k[o]
    eps2=2*n*k
    # visible Smith data
    vis=(lam>=0.38)&(lam<=0.78); N=n[np.argsort(o)][vis] if False else None
    lv=np.linspace(0.38,0.78,81); nv=np.interp(lv,lam[np.argsort(lam)],(n[np.argsort(o)] if False else d['n'][np.argsort(d['lam'])])); kv=np.interp(lv,np.sort(d['lam']),d['k'][np.argsort(d['lam'])])
    G=(1-(nv+1j*kv))/(1+(nv+1j*kv)); R=np.abs(G)**2
    argN=np.angle(nv+1j*kv)
    slope=np.nan; wl=np.nan
    if w.min()<0.3:
        cuts=np.geomspace(max(w.min(),1e-3)*1.05, min(0.3, w.max()/10), 8)
        I=[np.trapezoid(eps2[w>=c],w[w>=c]) for c in cuts]
        if min(I)>0:
            slope=np.polyfit(np.log(cuts),np.log(I),1)[0]; wl=cuts[0]
    rows.append((el,'nonmetal' if el in nonmetal else 'metal',R.mean(),argN.mean(),slope,wl,d['file']))
print('element  label     mean|G|^2   above 1/2   mean argN   IR slope of int eps2 (lowest cut eV)   dataset')
for r in sorted(rows,key=lambda x:x[2]):
    print(f'{r[0]:<4} {r[1]:<9} {r[2]:9.3f}   {"yes" if r[2]>0.5 else "no ":>5}     {r[3]:7.3f}     {r[4]:7.3f}  ({r[5]:.3g})        {r[6]}')
m=[r for r in rows if r[1]=='metal']; nm=[r for r in rows if r[1]=='nonmetal']
print('\nP3 Schottky line: metals above 1/2:',sum(r[2]>0.5 for r in m),'of',len(m),'| nonmetals above 1/2:',sum(r[2]>0.5 for r in nm),'of',len(nm))
sl=[r for r in rows if not np.isnan(r[4])]
print('X02: elements with infrared data below 0.3 eV:',len(sl))
for lab in ['metal','nonmetal']:
    v=[r[4] for r in sl if r[1]==lab]; print(f'   {lab}: n={len(v)} slopes',np.round(sorted(v),2))
