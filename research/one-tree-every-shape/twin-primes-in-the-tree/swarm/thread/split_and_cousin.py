# SCRIPT: TWIN-SPLIT-79-01 + COUSIN-THREAD-01
# Kill conditions: SPLIT_COUSIN_PREREG.md (from twin_chain_v1 Predictions 6 and 7).
import numpy as np, math, time, os
def base_primes(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.nonzero(s)[0]
def pair_starts(lo,hi,g):
    # p in [lo,hi) with p and p+g prime (segmented sieve)
    base=base_primes(int(math.isqrt(hi+g))+1); out=[]; seg=2*10**7
    for a in range(lo,hi,seg):
        b=min(a+seg,hi); m=np.ones(b-a+g,bool)
        for p in base:
            if p*p>=b+g: break
            st=max(p*p,((a+p-1)//p)*p); m[st-a::p]=False
        if a<2: m[:2-a]=False
        k=b-a; out.append(np.nonzero(m[:k]&m[g:g+k])[0]+a)
    return np.concatenate(out).astype(np.int64)
def devG(T,lo,hi,classes,nblk=30):
    # T sorted pair starts; use starts x in (lo,hi], gap back to previous start
    i=np.searchsorted(T,lo,side='right'); x=T[i:][T[i:]<=hi]; prev=T[i-1:i-1+len(x)]; gap=x-prev
    cls=np.searchsorted(classes,x%30); assert np.all(np.array(classes)[cls]==x%30)
    def one(x_,g_,c_):
        G=g_.mean(); return np.array([(g_[c_==j].sum()/g_.sum()-np.mean(c_==j))*G for j in range(3)])
    full=one(x,gap,cls); idx=np.array_split(np.arange(len(x)),nblk)
    bl=np.array([one(x[k],gap[k],cls[k]) for k in idx]); se=bl.std(0,ddof=1)/math.sqrt(nblk)
    # block estimates use each block's own G; se is for the full-range value
    return full,se,gap.mean(),len(x)
t0=time.time()
TW=np.load('../shapes/twins_1000000000.npy').astype(np.int64)
d,se,G,n=devG(TW,1e8,1e9,[11,17,29])
print('method check twins (1e8,1e9]: dev*G %s se %s  (v1: -0.924 0.839 0.085, se 0.041 0.034 0.054)'%(np.round(d,3),np.round(se,3)))
ok=np.max(np.abs(d-np.array([-0.924,0.839,0.085])))<=0.002; print('method check','PASS' if ok else 'FAIL')
# ---- prediction 6: sieve (1e9 - 1000, 1e10]
f='twins_1e9_1e10.npy'
if os.path.exists(f): T2=np.load(f)
else: T2=pair_starts(10**9-10**4,10**10+1,2); np.save(f,T2)
print('twin starts in (1e9-1e4, 1e10]: %d   (%.0fs)'%(len(T2),time.time()-t0))
d2,se2,G2,n2=devG(T2,1e9,1e10,[11,17,29])
pred=np.array([-0.945,0.809,0.136]); walk=np.array([None,0.72,0.20],dtype=object)
print('direct gap-weighted count (1e9,1e10]: dev*G %s se %s  G %.1f  n %d'%(np.round(d2,3),np.round(se2,3),G2,n2))
print('prediction (full product) %s ; walk split (7,9) = (+0.72, +0.20)'%pred)
closer_walk=[abs(d2[k]-[0,0.72,0.20][k])<abs(d2[k]-pred[k]) for k in (1,2)]
print('digit 7 closer to walk: %s, digit 9 closer to walk: %s ->'%tuple(closer_walk),'KILL (split is in the primes)' if all(closer_walk) else 'PASS (split offset is the walk weighting)')
print('z of direct count vs prediction (1,7,9):',np.round((d2-pred)/se2,1))
# ---- prediction 7: cousins
C=np.load('../../agent_new/pairs_g4_1000000000.npy').astype(np.int64); C=C[C>=7]
dc,sec,Gc,nc=devG(C,1e8,1e9,[7,13,19])
print('cousins real (1e8,1e9] classes 7,13,19: dev*G %s se %s G %.1f n %d'%(np.round(dc,3),np.round(sec,3),Gc,nc))
def run(Pmax,rho,H,shift,classes):
    h=np.arange(1,H+1); logF=np.zeros(H)
    for p in base_primes(Pmax):
        if p<7: continue
        r=np.stack([np.zeros(H,int),np.full(H,(-shift)%p),h%p,(h-shift)%p],1); r.sort(1); nu=1+(np.diff(r,axis=1)!=0).sum(1)
        logF+=np.log(p*(p-nu)/(p-2)**2)
    F=np.exp(logF); E=[]
    for j in classes:
        lam=rho*F*np.isin((j-h)%30,classes)*10.0
        surv=np.exp(-np.concatenate([[0],np.cumsum(lam)[:-1]])); P=lam*surv; E.append((h*P).sum()/P.sum())
    E=np.array(E); return (E/E.sum()-1/3)*E.mean(), E.mean()
C2=0.6601618158; N=math.sqrt(1e8*1e9)
dt,_=run(1000,2*C2/math.log(N)**2,8000,2,[11,17,29]); print('construction reproduces twin prediction (v1: -0.939 0.820 0.119):',np.round(dt,3))
pc,Gp=run(1000,2*C2/math.log(N)**2,8000,4,[7,13,19])
z=(dc-pc)/sec
print('cousin prediction (full product) %s  G %.1f ; z (7,13,19) %s ->'%(np.round(pc,3),Gp,np.round(z,1)),'PASS' if np.all(abs(z[:2])<2) else 'KILL')
