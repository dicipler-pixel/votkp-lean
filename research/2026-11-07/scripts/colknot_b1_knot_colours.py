# SCRIPT: COLKNOT-B1
# Task B. Knots as colours.  V(e^{i theta}), theta 0..2pi  ->  lambda 380..780 nm (81 samples, 5 nm), theta=0 at 380 nm.
# Smith map Gamma=(V-1)/(V+1).  V(1)=1 -> Gamma=0 at both ends (vacuum point).  |Gamma| can exceed 1 (Re V<0), so a passive reflectance needs a choice:
#   M1  R = min(|Gamma|^2, 1)                      (clipped)            theta forward
#   (per-knot max-normalisation of |Gamma| was tried and dropped: Gamma has an exact pole at theta=pi/2, 3pi/2 for every knot with V(i)=-1, i.e. Arf invariant 1, half the table)
#   M2b R = |Gamma|^2/(1+|Gamma|^2)                (soft squash, no clipping, no per-knot normalisation)
#   M3  R = |V| / max|V|   and M3b R = |V|/(1+|V|)  (the opposite: |V| instead of Gamma)
#   M4  R = (1 + Im Gamma/(1+|Gamma|))/2          (phase-bearing; M5 R=(arg V+pi)/2pi ; M6 R=(1+Im V/(1+|V|))/2 : the only families that can see handedness)
#   theta reversed for every map (spectrum flipped in lambda). Because the coefficients are real, V(e^{-i theta}) = conj V(e^{i theta}): |.| maps are exactly palindromic, so reversal is identical for M1-M3 (checked numerically).
# Colour: CIE 1931 2 deg, D65, reflectance*illuminant, Lab -> L*, C*, h.
# Targets: hyperbolic volume (KnotInfo), signature, log det baseline; knots to 12 crossings with volume>0.
import numpy as np, database_knotinfo as dk, warnings; warnings.filterwarnings('ignore')
from scipy.stats import spearmanr
import cknot_common as C
th=2*np.pi*(C.LAM-380)/400.0; t=np.exp(1j*th)
rows=[]; names=[]
for r in dk.link_list():
    try:
        cn=int(r['crossing_number']); vol=float(r['volume']); sig=int(r['signature']); det=int(r['determinant'])
    except (ValueError,TypeError): continue
    if cn>12 or vol<=0 or not r['jones_polynomial_vector']: continue
    v=eval(r['jones_polynomial_vector']); c=np.array(v[2:],float); V=np.polyval(c[::-1],t)*t**v[0]
    rows.append((vol,sig,det,cn,V)); names.append(r['name'])
vol=np.array([x[0] for x in rows]); sig=np.array([x[1] for x in rows]); ldet=np.log([x[2] for x in rows]); cn=np.array([x[3] for x in rows]); V=np.array([x[4] for x in rows])
print('hyperbolic knots to 12 crossings:',len(vol),' | check torus-like omitted (volume 0). V(1) max error',np.abs(V[:,0]-1).max(),np.abs(V[:,-1]-1).max())
den=V+1; pole=np.abs(den)<1e-9; print('samples with V=-1 exactly (Gamma pole): %d in %d knots (floored |V+1| at 1e-9)'%(pole.sum(),pole.any(1).sum())); den=np.where(pole,1e-9,den)
G=(V-1)/den; aG=np.abs(G)
print('|Gamma|>1 somewhere on the circle for %.1f%% of knots; mean fraction of the circle with |Gamma|>1: %.3f'%(100*np.mean((aG>1).any(1)),np.mean(aG>1)))
mah=np.mean(np.log(np.abs(V[:,:-1])),axis=1)
maps={
 'M1 clipped |G|^2':np.minimum(aG**2,1),
 'M2b |G|^2/(1+|G|^2)':aG**2/(1+aG**2),
 'M3 |V|/max|V|':np.abs(V)/np.max(np.abs(V),axis=1,keepdims=True),
 'M3b |V|/(1+|V|)':np.abs(V)/(1+np.abs(V)),
 'M4 (1+Im G/(1+|G|))/2':0.5*(1+G.imag/(1+aG)),
 'M5 (arg V+pi)/2pi':(np.angle(V)+np.pi)/(2*np.pi),
 'M6 (1+Im V/(1+|V|))/2':0.5*(1+V.imag/(1+np.abs(V))),
}
def feats(R):
    L,Ch,h=C.LCh(R); return dict(L=L,C=Ch,cosh=np.cos(np.radians(h)),sinh=np.sin(np.radians(h)),h=h,Y=C.XYZ(R)[:,1])
F={k:feats(R) for k,R in maps.items()}
Fr={k:feats(R[:,::-1]) for k,R in maps.items()}
for k in maps: print('  reversed vs forward colour, max |dLab| (%s): %.2e'%(k,np.abs(C.Lab(maps[k])-C.Lab(maps[k][:,::-1])).max()))
def circ_lin(h,x):                                      # Mardia circular-linear correlation
    c,s=np.cos(np.radians(h)),np.sin(np.radians(h)); rcx=np.corrcoef(c,x)[0,1]; rsx=np.corrcoef(s,x)[0,1]; rcs=np.corrcoef(c,s)[0,1]
    return np.sqrt(max((rcx**2+rsx**2-2*rcx*rsx*rcs)/(1-rcs**2),0))
A=np.column_stack([ldet,np.ones_like(ldet)]); cc,*_=np.linalg.lstsq(A,vol,rcond=None); vres=vol-A@cc
print('\nbaselines: rho(log det, volume)=%.3f   R^2(volume~log det)=%.3f   rho(Mahler of Jones, volume)=%.3f   rho(log det,|sig|)=%.3f'%(spearmanr(ldet,vol)[0],1-vres.var()/vol.var(),spearmanr(mah,vol)[0],spearmanr(ldet,abs(sig))[0]))
def cv_r2(X,y,k=5,seed=0):
    idx=np.random.default_rng(seed).permutation(len(y)); folds=np.array_split(idx,k); pr=np.zeros_like(y)
    X1=np.column_stack([X,np.ones(len(y))])
    for f in folds:
        tr=np.setdiff1d(idx,f); b,*_=np.linalg.lstsq(X1[tr],y[tr],rcond=None); pr[f]=X1[f]@b
    return 1-((y-pr)**2).sum()/((y-y.mean())**2).sum()
for tag,FF in [('THETA FORWARD',F),('THETA REVERSED',Fr)]:
    print('\n=== %s ==='%tag)
    print(' map                     feature |  rho vs volume | rho vs log det | rho vs vol resid(after log det) | rho vs |sig| | rho vs signed sig | rho vs Mahler')
    for k,f in FF.items():
        for nm_ in ['L','C','h']:
            x=f[nm_]
            if nm_=='h':
                print(' %-23s h(circ r)|  %.3f          | %.3f          | %.3f                          | %.3f       | %.3f             | %.3f'%(k,circ_lin(x,vol),circ_lin(x,ldet),circ_lin(x,vres),circ_lin(x,abs(sig)),circ_lin(x,sig),circ_lin(x,mah)))
            else:
                print(' %-23s %-7s | %+.3f         | %+.3f         | %+.3f                          | %+.3f      | %+.3f            | %+.3f'%(k,nm_,spearmanr(x,vol)[0],spearmanr(x,ldet)[0],spearmanr(x,vres)[0],spearmanr(x,abs(sig))[0],spearmanr(x,sig)[0],spearmanr(x,mah)[0]))
print('\n=== regression: 5-fold CV R^2 for volume, |signature|, signed signature (features L, C, cos h, sin h) ===')
print(' map                       volume: colour | logdet | logdet+colour | colour+logdet gain || |sig|: colour | logdet | both || signed sig: colour (fwd) | colour (fwd+rev avg pair) ')
for k,f in F.items():
    X=np.column_stack([f['L'],f['C'],f['cosh'],f['sinh']]); Xl=ldet[:,None]; Xb=np.column_stack([X,Xl])
    print(' %-25s  %.3f  | %.3f | %.3f         | %+.3f              ||  %.3f | %.3f | %.3f  ||  %.3f'%(k,cv_r2(X,vol),cv_r2(Xl,vol),cv_r2(Xb,vol),cv_r2(Xb,vol)-cv_r2(Xl,vol),cv_r2(X,abs(sig).astype(float)),cv_r2(Xl,abs(sig).astype(float)),cv_r2(Xb,abs(sig).astype(float)),cv_r2(X,sig.astype(float))))
# mirror test with the phase-bearing maps: colour of V minus colour of its mirror V(1/t) (= theta reversed) against the signature
arf=np.array([int(r['arf_invariant']) if r['arf_invariant'] not in ('',None) else -1 for r in dk.link_list() if (lambda x:(x.get('crossing_number','').isdigit() and int(r['crossing_number'])<=12 and r['volume'] not in ('',None) and (lambda v:(v.replace('.','',1).isdigit() and float(v)>0))(r['volume']) and bool(r['jones_polynomial_vector']) and r['signature'] not in ('',None)))(r)])
print('\nArf invariant check: knots with a Gamma pole at theta=pi/2 vs Arf=1: ',end='')
if len(arf)==len(vol): print('agree on %.3f of %d knots'%(np.mean((np.abs(V[:,20]+1)<1e-9)==(arf==1)),len(arf)))
else: print('(table length mismatch %d vs %d)'%(len(arf),len(vol)))
nz=sig!=0
for k in [x for x in maps if x.startswith(('M4','M5','M6'))]:
    f,fr=F[k],Fr[k]; Lab_f=C.Lab(maps[k]); Lab_r=C.Lab(maps[k][:,::-1]); dd_=Lab_f-Lab_r
    r_=[spearmanr(dd_[nz,i],sig[nz])[0] for i in range(3)]
    X=np.column_stack([dd_,np.ones(len(vol))]); 
    print('%s mirror contrast dL,da,db vs signed signature (n=%d): rho %+.3f %+.3f %+.3f ; 5-fold CV R^2 of signature from (dL,da,db): %.3f ; vs |sig| from |d|: %.3f'%(k,nz.sum(),*r_,cv_r2(dd_,sig.astype(float)),cv_r2(np.abs(dd_),abs(sig).astype(float))))
# direct colour of a few
print('\nsamples (M1): name   vol  sig  L*  C*  h')
for nm in ['4_1','5_2','6_1','7_2','8_18','10_139','12n_242']:
    if nm in names:
        i=names.index(nm); f=F['M1 clipped |G|^2']; print('  %-8s %.3f %3d  %5.1f %5.1f %6.1f'%(nm,vol[i],sig[i],f['L'][i],f['C'][i],f['h'][i]))
np.save('out/colknot_b1_M1_lch.npy',np.column_stack([F['M1 clipped |G|^2']['L'],F['M1 clipped |G|^2']['C'],F['M1 clipped |G|^2']['h'],vol,sig,ldet]))
