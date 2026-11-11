# SCRIPT: COLKNOT-A2
# Task A(ii). Thin film (air | n=1.5 film of thickness d | element), reflection r(lambda,d) on the Smith disk.
#  (a) integer windings of r around the centre G=0 across 380-780 nm as d grows 0..1000 nm
#      - W_real = unwrapped phase change / 2pi ; W_closed = winding number of the loop r(380->780) closed by a straight chord (an exact integer)
#      - theory: |r12|>|r01| (substrate index outside 1..n_f^2) gives winding = 2 n_f d (1/380-1/780) = d/247 nm (+ dispersion)
#  (b) does film colour split into a continuous part (bulk |Gamma|: lightness, mean reflectance) and an integer part (windings: chroma/hue)?
#      Variance decomposition of within-element colour variation over d, with element dummies + integer-order dummies vs fractional-phase bins.
#  (c) is the integer visible in the spectrum? count fringe maxima of R(lambda) vs W_closed.
import numpy as np, colour, warnings; warnings.filterwarnings('ignore')
from scipy.stats import spearmanr
import cknot_common as C
lam1=np.arange(380,781,1.0); sh=colour.SpectralShape(380,780,1)
cm=colour.MSDS_CMFS['CIE 1931 2 Degree Standard Observer'].copy().align(sh).values; il=colour.SDS_ILLUMINANTS['D65'].copy().align(sh).values
M=(il[:,None]*cm)*100/np.sum(il*cm[:,1])/100
Wp=colour.CCS_ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['D65']
def LCh(R):
    lab=colour.XYZ_to_Lab(R@M,Wp); return lab[:,0],np.hypot(lab[:,1],lab[:,2]),lab[:,1],lab[:,2]
S=__import__('ri_load').element_sets(); E1={}
for el,d in S.items():
    o=np.argsort(d['lam']); E1[el]=np.interp(lam1/1000,d['lam'][o],d['n'][o])+1j*np.interp(lam1/1000,d['lam'][o],d['k'][o])
dd=np.arange(0,1001,5.0); nf=1.5
print('theory: windings across 380-780 per nm of film = 2*%.1f*(1/380-1/780) = %.5f  -> %.1f nm per winding'%(nf,2*nf*(1/380-1/780),1/(2*nf*(1/380-1/780))))
rows={}; peaks={}
W_closed={}; W_real={}; dev=0
for el,N in E1.items():
    r=C.film_r(N,dd,nf,lam1)                                    # (nd,401)
    ph=np.unwrap(np.angle(r),axis=1); Wr=-(ph[:,-1]-ph[:,0])/(2*np.pi)
    tot=-(ph[:,-1]-ph[:,0]+np.angle(r[:,0]/r[:,-1]))/(2*np.pi)   # sign: phase falls with lambda; add the chord's turning
    # closing chord turning: from r(780) back to r(380) is angle(r380/r780); sum must be a multiple of 2pi
    tot=(-(ph[:,-1]-ph[:,0])-np.angle(r[:,0]/r[:,-1]))/(2*np.pi); Wc=np.round(tot); dev=max(dev,np.abs(tot-Wc).max())
    W_closed[el]=Wc; W_real[el]=Wr
    R=np.abs(r)**2
    pk=((R[:,1:-1]>R[:,:-2])&(R[:,1:-1]>R[:,2:])).sum(1); peaks[el]=pk
    L,Ch,a,b=LCh(R); rows[el]=(L,Ch,a,b,np.angle(r[:,0]) )
print('(a) closed-loop winding is an integer: max |x - round(x)| over all elements and d = %.2e'%dev)
i1000=-1
print('\n el   substrate N(550nm)   |r12|>|r01|?   W_closed at d=250,500,1000 nm   W_real(1000)   theory d/247 (1000)=%.2f'%(1000/247.3))
for el in sorted(E1,key=lambda e:W_real[e][-1]):
    N=E1[el][170]; r12=abs((nf-N)/(nf+N)); 
    print(' %-3s  %6.2f%+6.2fi        %-5s            %2d  %2d  %2d                %6.2f'%(el,N.real,N.imag,r12>0.2,W_closed[el][50],W_closed[el][100],W_closed[el][200],W_real[el][-1]))
allW=np.array([W_closed[e] for e in E1]); allWr=np.array([W_real[e] for e in E1])
print('  W_closed at 1000 nm over 41 elements: counts',dict(zip(*np.unique(allW[:,-1],return_counts=True))))
print('  W_real at d=0 (the bare substrate track, turns across band): min %.3f max %.3f ; excess of W_real(1000) over theory 4.049 = substrate phase: Rb %.2f, Cs %.2f, K %.2f, Ag %.2f'%(allWr[:,0].min(),allWr[:,0].max(),*[W_real[x][-1]-4.049 for x in ['Rb','Cs','K','Ag']]))
print('  W_real vs d is linear? per-element slope (windings per 1000 nm) median %.3f, range %.3f..%.3f'%tuple(np.r_[np.median(allWr[:,-1]),allWr[:,-1].min(),allWr[:,-1].max()]))
# (c) fringe count vs windings
pk=np.array([peaks[e] for e in E1]); print('\n(c) fringe maxima of R(lambda) in band vs W_closed: Spearman %.3f ; exact match %.3f ; within +-1 %.3f (all elements, d=0..1000)'%(spearmanr(pk.ravel(),allW.ravel())[0],np.mean(pk==allW),np.mean(abs(pk-allW)<=1)))
# (b) colour decomposition
els=list(E1); nd=len(dd); K=len(els)
Y={k:np.concatenate([rows[e][i] for e in els]) for i,k in enumerate(['L','C','a','b'])}
elid=np.repeat(np.arange(K),nd); dcol=np.tile(dd,K)
Wtot=np.concatenate([W_real[e] for e in els]); n_int=np.floor(Wtot).astype(int); f_span=Wtot-np.floor(Wtot)
# fractional phase of r at lambda=550 (the film's own phase there, continuous in d) and its integer part (order at 550)
i550=170
ord550=[];f550=[]
for e in els:
    r=C.film_r(E1[e][i550],dd,nf,lam1[i550]).ravel(); ph=-np.unwrap(np.angle(r)); ph=ph-ph[0]; ord550.append(np.floor(ph/(2*np.pi)).ravel()); f550.append(((ph/(2*np.pi))%1).ravel())
ord550=np.concatenate(ord550).astype(int); f550=np.concatenate(f550)
def dummies(v): u=np.unique(v); return (v[:,None]==u[None,:]).astype(float)
def bins(f,nb=12): return dummies(np.minimum((f*nb).astype(int),nb-1))
def r2(y,X): c,*_=np.linalg.lstsq(X,y,rcond=None); return 1-((y-X@c)**2).sum()/((y-y.mean())**2).sum()
DE=dummies(elid)
print('\n(b) within-element colour variation over thickness: share of variance explained (R^2 beyond element dummies, as fraction of what is left)')
print('   outcome   elem-only R^2 | + integer order n(span) | + frac phase f(span) | + both | + order at 550 | + frac at 550 | + both(550) | + d-bins(40) [ceiling]')
dbins=dummies(np.minimum((dcol/1000*40).astype(int),39))
for k,lab in [('L','L* lightness'),('C','C* chroma'),('a','a*'),('b','b*')]:
    y=Y[k]; r0=r2(y,DE); fr=lambda X:(r2(y,np.column_stack([DE,X]))-r0)/(1-r0)
    print('   %-13s %.3f      %.3f                   %.3f               %.3f     %.3f          %.3f          %.3f      %.3f'%(lab,r0,fr(dummies(n_int)),fr(bins(f_span)),fr(np.column_stack([dummies(n_int),bins(f_span)])),fr(dummies(ord550)),fr(bins(f550)),fr(np.column_stack([dummies(ord550),bins(f550)])),fr(dbins)))
# per-element Spearman of chroma/lightness with integer order
rc=[spearmanr(rows[e][1],np.floor(W_real[e]))[0] for e in els if W_real[e][-1]>1]; rl=[spearmanr(rows[e][0],np.floor(W_real[e]))[0] for e in els if W_real[e][-1]>1]
print('\n   across d, per element: Spearman(C*, n) median %.2f (IQR %.2f..%.2f) ; Spearman(L*, n) median %.2f (IQR %.2f..%.2f)'%(np.median(rc),*np.percentile(rc,[25,75]),np.median(rl),*np.percentile(rl,[25,75])))
# chroma by order, pooled
print('   mean C* and L* by integer order n (span), pooled over elements:')
for n in np.unique(n_int): m=n_int==n; print('     n=%d  count %5d   C*=%6.2f  L*=%6.2f  (sd of L* across elements-at-d %.2f)'%(n,m.sum(),Y['C'][m].mean(),Y['L'][m].mean(),Y['L'][m].std()))
# continuous part: bulk |Gamma| -> lightness across elements, at fixed d
Rb=np.array([np.abs(C.smithG(E1[e]))**2 for e in els]); Lb,Cb,ab,bb=LCh(Rb)
meanR=Rb.mean(1)
print('\n   continuous part across elements at fixed d: Spearman of film L* with bulk L* / bulk mean|Gamma|^2 / bulk C*')
for d0 in [50,100,250,500,1000]:
    i=int(d0/5); Lf=np.array([rows[e][0][i] for e in els]); Cf=np.array([rows[e][1][i] for e in els])
    print('     d=%4d nm:  L*film~L*bulk %.2f | ~meanR %.2f | C*film~C*bulk %.2f'%(d0,spearmanr(Lf,Lb)[0],spearmanr(Lf,meanR)[0],spearmanr(Cf,Cb)[0]))
Lmean=np.array([rows[e][0][20:].mean() for e in els]); print('     element-mean film L* (d>=100) vs bulk L*: rho %.2f ; vs bulk mean|G|^2: rho %.2f'%(spearmanr(Lmean,Lb)[0],spearmanr(Lmean,meanR)[0]))
# continuity across integer steps (is the integer a jump in colour?)
jump_at=[];jump_else=[]
for e in els:
    L,Ch,a,b,_=rows[e]; lab=np.column_stack([L,a,b]); step=np.sqrt((np.diff(lab,axis=0)**2).sum(1)); st=np.diff(np.floor(W_real[e]))!=0
    jump_at+=list(step[st]); jump_else+=list(step[~st])
print('\n   colour step per 5 nm of film: at an integer-winding step mean %.2f (max %.2f) vs elsewhere mean %.2f (max %.2f) (CIELAB units) -> no jump at integers'%(np.mean(jump_at),np.max(jump_at),np.mean(jump_else),np.max(jump_else)))
