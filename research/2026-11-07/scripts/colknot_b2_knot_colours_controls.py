# SCRIPT: COLKNOT-B2
# Controls for B. (1) Is the colour more than a one-number summary of |V|?  Compare 5-fold CV R^2 for volume of
#     [log det + colour L,C,cos h,sin h] against [log det + Mahler], [log det + mean |V|/(1+|V|)], [log det + several |V| moments].
# (2) Is colour-vs-volume just crossing number?  Spearman within each crossing number 8..12, and partial on crossing number.
# (3) Two more Smith-type maps that keep the string passive:  M7 fold (N = |Re V| + i Im V),  M8 real Smith of |V| (Gamma=(|V|-1)/(|V|+1)), R=Gamma^2.
import numpy as np, database_knotinfo as dk, warnings; warnings.filterwarnings('ignore')
from scipy.stats import spearmanr
import cknot_common as C
th=2*np.pi*(C.LAM-380)/400.0; t=np.exp(1j*th)
rows=[]
for r in dk.link_list():
    try: cn=int(r['crossing_number']); vol=float(r['volume']); sig=int(r['signature']); det=int(r['determinant'])
    except (ValueError,TypeError): continue
    if cn>12 or vol<=0 or not r['jones_polynomial_vector']: continue
    v=eval(r['jones_polynomial_vector']); c=np.array(v[2:],float); rows.append((vol,sig,det,cn,np.polyval(c[::-1],t)*t**v[0]))
vol=np.array([x[0] for x in rows]); sig=np.array([x[1] for x in rows]); ldet=np.log([x[2] for x in rows]); cn=np.array([x[3] for x in rows]); V=np.array([x[4] for x in rows]); aV=np.abs(V)
den=V+1; den=np.where(np.abs(den)<1e-9,1e-9,den); G=(V-1)/den; aG=np.abs(G)
def cv_r2(X,y,k=5,seed=0):
    idx=np.random.default_rng(seed).permutation(len(y)); folds=np.array_split(idx,k); pr=np.zeros_like(y); X1=np.column_stack([X,np.ones(len(y))])
    for f in folds:
        tr=np.setdiff1d(idx,f); b,*_=np.linalg.lstsq(X1[tr],y[tr],rcond=None); pr[f]=X1[f]@b
    return 1-((y-pr)**2).sum()/((y-y.mean())**2).sum()
Nf=np.abs(V.real)+1j*V.imag; Gf=(Nf-1)/(Nf+1); Gr=(aV-1)/(aV+1)
maps={'M1 clipped |G|^2':np.minimum(aG**2,1),'M3b |V|/(1+|V|)':aV/(1+aV),'M7 fold |G_fold|^2':np.abs(Gf)**2,'M8 real Smith (|V|-1)^2/(|V|+1)^2':Gr**2}
def feats(R):
    L,Ch,h=C.LCh(R); return np.column_stack([L,Ch,np.cos(np.radians(h)),np.sin(np.radians(h))]),L,Ch,h
mah=np.mean(np.log(aV[:,:-1]),axis=1); sq=np.mean(aV/(1+aV),axis=1)
print('(1) CV R^2 for hyperbolic volume (n=%d knots)'%len(vol))
for lab,X in [('log det',ldet[:,None]),('log det + Mahler of Jones',np.column_stack([ldet,mah])),('log det + mean |V|/(1+|V|)',np.column_stack([ldet,sq])),
              ('log det + mean|V|, mean log|V|, max|V|, std|V|',np.column_stack([ldet,aV.mean(1),mah,aV.max(1),aV.std(1)])),('crossing number only',cn[:,None].astype(float)),('log det + crossing number',np.column_stack([ldet,cn]))]:
    print('   %-52s %.3f'%(lab,cv_r2(X,vol)))
for k,R in maps.items():
    X,L,Ch,h=feats(R); print('   colour only (L,C,cos h,sin h)  %-36s %.3f   | log det + colour %.3f | + Mahler too %.3f'%(k,cv_r2(X,vol),cv_r2(np.column_stack([X,ldet]),vol),cv_r2(np.column_stack([X,ldet,mah]),vol)))
X3,L3,C3,h3=feats(maps['M3b |V|/(1+|V|)']); print('   corr(L* of M3b, mean |V|/(1+|V|)) rho = %.3f  (not the same number: L* is a CMF-weighted summary of the whole spectrum)'%spearmanr(L3,sq)[0])
print('\n(2) within crossing number: Spearman with volume (M3b L*, log det, M1 L*, M8 L*)  and partial (volume residual after log det)')
LM1=feats(maps['M1 clipped |G|^2'])[1]; L8=feats(maps['M8 real Smith (|V|-1)^2/(|V|+1)^2'])[1]
A=np.column_stack([ldet,np.ones_like(ldet)]); c,*_=np.linalg.lstsq(A,vol,rcond=None); vres=vol-A@c
for n in range(8,13):
    m=cn==n; print('   cn=%2d (n=%4d): M3b L* %.3f | log det %.3f | M1 L* %.3f | M8 L* %+.3f || M3b L* vs vol-resid %.3f | M1 L* vs vol-resid %.3f'%(n,m.sum(),spearmanr(L3[m],vol[m])[0],spearmanr(ldet[m],vol[m])[0],spearmanr(LM1[m],vol[m])[0],spearmanr(L8[m],vol[m])[0],spearmanr(L3[m],vres[m])[0],spearmanr(LM1[m],vres[m])[0]))
print('\n(3) the extra Smith-type maps, forward (reversal is identical for |.|-maps):  rho with volume / log det / vol resid / |sig|   for L*, C*')
for k in ['M7 fold |G_fold|^2','M8 real Smith (|V|-1)^2/(|V|+1)^2']:
    X,L,Ch,h=feats(maps[k]); print('   %-36s L*: %+.3f %+.3f %+.3f %+.3f | C*: %+.3f %+.3f %+.3f %+.3f'%(k,spearmanr(L,vol)[0],spearmanr(L,ldet)[0],spearmanr(L,vres)[0],spearmanr(L,abs(sig))[0],spearmanr(Ch,vol)[0],spearmanr(Ch,ldet)[0],spearmanr(Ch,vres)[0],spearmanr(Ch,abs(sig))[0]))
print('\n(4) how much of the string lies outside the passive half-plane Re V>0 (where Gamma leaves the unit disk): fraction of the circle, by crossing number')
for n in range(3 if False else 4,13):
    m=cn==n
    if m.sum(): print('   cn=%2d: %.3f   (volume vs this fraction rho %.2f)'%(n,np.mean(V[m].real<0),spearmanr(np.mean(V[m].real<0,axis=1),vol[m])[0] if m.sum()>5 else np.nan))
print('   all: volume vs fraction outside passive half-plane rho = %.3f ; vs log det residual rho = %.3f'%(spearmanr(np.mean(V.real<0,axis=1),vol)[0],spearmanr(np.mean(V.real<0,axis=1),vres)[0]))
