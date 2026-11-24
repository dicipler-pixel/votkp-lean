# SCRIPT: GAPS-CAP-GRAM-03 (profile g as a parameter; face numerator stored as three region matrices so the hybrid lambda is free) (exact FLINT convolution; version 01 used float64 FFT, which was 8% off)
# Independent rebuild (own code, float64 FFT) of the cap quadratic forms in OpenAI's gap-186 certificate,
# assembled as two Gram matrices over the 77 trial descriptors (signature, radial degree):
#   I_H(c) = c^T A c   (outer norm, k coordinates)
#   J(c)   = c^T B c   (hybrid face numerator J0 + (a+b) J+ + b Jt, k-1 retained coordinates)
# so the best trial at any k is a generalized eigenvalue problem: max rho* c^T B c / c^T A c.
# The geometry (S, T0, T1, rho, ladders, shells, caps, Dickman fragment measure, hybrid constants)
# is copied from the paper's stated formulas, not from their code.
# CHECK (written before the run): at k = 40 with their 77 coefficients this must give
#   I_H = 2.36853178e-14 (to 1e-6 relative) and cap quotient 1.000206 (to 2e-6), else the rebuild is wrong.
import numpy as np, math, sys
from fractions import Fraction as F
from collections import Counter, defaultdict
from itertools import product
from math import comb, prod
from functools import lru_cache

SIGS=[(),(2,),(3,),(4,),(5,),(6,),(2,2),(2,3),(2,4),(3,3),(2,2,2)]
CINT=[[10000000000,-264598476112,834262268474,-3540575351215,5377491111325,116705356572254,121730820431102],
[71070047507,7222861788586,-48747932657986,290976672545723,-1136422724027134,-2058910631434711,1375878942948547],
[6457252424873,-61201446212885,28811649792090,-2058803084231281,9970156747759406,38278849934023144,34806920812932737],
[-16779263512274,128033707910825,169290603857215,7359669931312727,-35090795379920588,-120997133235510923,-141527585901304670],
[28114161526671,-276375633435566,-690482702304933,-15120456749385986,47650276584638031,372137534144492224,2191913505882230103],
[-21150553032771,379875924448266,-929062247569514,-13967219843969236,168416050564605519,-248058724714138769,-4161797957833172083],
[-19004216224617,136674974139652,-183344485344333,1114879023072977,1119583327002910,-47568062965320963,2537631525616777],
[31171802814567,-97428388152051,526635309233054,1222047580792220,15846796161434448,-165623953461271580,-2358019996221938729],
[-53602626608739,329397902441121,1613505134333316,13893066541430270,-126262434123562668,239934302929501943,-1506861482386002243],
[27653330903418,-290549334488305,-1847330641348475,28351866831729468,-61505472221886320,-424266003419714347,2585236507449911535],
[12374547113901,-244168600145684,1603694896120437,-21603130476787649,-30285492734943698,381987976419637874,3605516061450295448]]
DESC=[(s,d) for s in SIGS for d in range(7)]
C_THEIRS=np.array([v*1e-10 for row in CINT for v in row])

# ---------- geometry from the paper (1.13)-(1.18) ----------
def ladder(T,eps,limit,cs,S,rho,gap):
    prev=F(0); E=rho*(S+T)-F(1,2); rows=[]
    for idx in range(100):
        order=min(idx//12+1,3); c,slope=cs[order-1]
        om=min(limit,(c-eps-E+2*prev-gap)/slope); delta=c-slope*om-eps
        B=(F(1,2)+2*prev)/rho; xi=delta/rho
        rows.append(dict(a=B-T,b=B-S,B=B))
        if om==limit: return rows
        prev=om
def geometry():
    gap,tau=F(1,10**7),F(1,10**10); rho=F(1,4)+F(12499,10**6); rs=rho-gap
    S,T1=F(2742997,10**7)/rs,F(251,1000)/rs; T0=2-F(3,1000)-S
    e,zeta=gap/rho,F(19037,100000)/rho
    s0,sm=F(100001,10**6),F(1,2)-F(40481,100000)+tau
    oc=(((1-5*s0)/15,F(18,5)),((1-4*s0)/16,F(7,2)),(F(3,80),F(3)))
    nc=(((1-5*sm)/15,F(18,5)),((1-4*sm)/16,F(7,2)),((1-2*sm)/20,F(16,5)))
    old=ladder(T0,F(1,10**6),F(12499,10**6),oc,S,rho,gap); new=ladder(T1,F(1,10**7),F(253,20000),nc,S,rho,gap)
    sh=dict(outer=[(new[0]['a'],zeta),(new[24]['a'],(S+e)/2),(S,S+e/2-23*(T1+e/2)/40)],
            base=[(old[12]['b'],zeta),(old[24]['b'],(T0+e)/2),(T0,63*(T0+e/2)/160)],
            enlarged=[(new[12]['b'],zeta),(new[24]['b'],(T1+e)/2),(T1,63*(T1+e/2)/160)],
            full=[(S,zeta)])
    return S,rs,sh,(len(old),len(new))

def aligned_shells(pairs,hq):
    prev,prevcap,out=F(0),None,[]
    for up,cap in pairs:
        al=(cap//hq)*hq
        lower=out.pop()[0] if out and out[-1][2]==al else prev
        out.append((lower,up,al)); prev,prevcap=up,al
    return out

# ---------- combinatorics (power sums) ----------
@lru_cache(None)
def block_partitions(sig):
    if not sig: return (((),1),)
    q,ans=sig[-1],defaultdict(int)
    for blocks,m in block_partitions(sig[:-1]):
        ans[tuple(sorted(blocks+(q,)))]+=m
        for v,cp in Counter(blocks).items():
            j=list(blocks); j.remove(v); ans[tuple(sorted(j+[v+q]))]+=m*cp
    return tuple(ans.items())
def moment_terms(count,sig):
    return [(b,m*prod(range(count-len(b)+1,count+1))) for b,m in block_partitions(tuple(sorted(sig))) if len(b)<=count]
@lru_cache(None)
def fiber_splits(sig):
    cnt=tuple(sorted(Counter(sig).items())); out=[]
    for ch in product(*(range(c+1) for _,c in cnt)):
        rem,ex,mu=[],0,1
        for (pw,c),s in zip(cnt,ch):
            rem+= [pw]*(c-s); ex+=pw*s; mu*=comb(c,s)
        out.append((tuple(rem),ex,mu))
    return tuple(out)

# ---------- numerics ----------
import exactconv
def fftmul(a,b,n): return exactconv.conv(a,b,n)
def fftmul_float(a,b,n):
    L=1<<int(math.ceil(math.log2(2*n)))
    r=np.fft.irfft(np.fft.rfft(a,L)*np.fft.rfft(b,L),L)[:n]
    return r
def dickman_surv(M,n):
    # cell masses per unit h of rho(t/c), c=M h; trapezoid on grid u_j=j/M
    m=max(n+1,M+1); rho=np.ones(m+1)
    for j in range(M,m):
        # rho(u_{j+1}) = rho(u_j) - int_{u_j}^{u_{j+1}} rho(v-1)/v dv  (trapezoid)
        rho[j+1]=rho[j]-0.5*(rho[j-M]/j+rho[j+1-M]/(j+1))
    rho=np.clip(rho,0,1)
    s=np.ones(n); jj=np.arange(n); hi=jj>=M
    s[hi]=0.5*(rho[jj[hi]]+rho[jj[hi]+1])
    return s

class Engine:
    def __init__(self,k=40,N=98304,mix=(0.105,0.01,181.4)):
        self.k,self.N=k,N; S,rs,sh,self.ladders=geometry(); self.S,self.rs=S,rs
        self.hq=S/N; self.h=float(self.hq); self.n=N-40   # convolution length fixed as in the paper
        self.outer=aligned_shells(sh['outer'],self.hq)
        self.inner={lab:aligned_shells(sh[lab],self.hq) for lab in ('base','enlarged','full')}
        caps=sorted({c for s in self.outer for c in [s[2]]}|{s[2] for lab in self.inner for s in self.inner[lab]})
        self.caps=caps+[None]
        n=self.n; t=(np.arange(n)+0.5)*self.h; self.t=t
        w0,sl,fa=mix; g=w0/(1+sl*t)+(1-w0)/(1+fa*t); self.g=g; self.Z=(g*g).sum()
        self.w=g*g/self.Z
        self._surv={}; self._mom={}; self._pow={}; self._blk={}
    def surv(self,cap):
        if cap is None: return np.ones(self.n)
        M=int(cap/self.hq)
        if M not in self._surv: self._surv[M]=dickman_surv(M,self.n)
        return self._surv[M]
    def weighted(self,cap,e): return self.w*self.surv(cap)*self.t**e
    def ppow(self,cap,cnt):
        key=(cap,cnt)
        if key not in self._pow:
            if cnt==0: v=np.zeros(self.n); v[0]=1.0
            elif cnt==1: v=self.weighted(cap,0)
            else:
                hf=self.ppow(cap,cnt//2); v=fftmul(hf,hf,self.n)
                if cnt&1: v=fftmul(v,self.weighted(cap,0),self.n)
            self._pow[key]=v
        return self._pow[key]
    def blocks(self,cap,bl):
        key=(cap,bl)
        if key not in self._blk:
            if not bl: v=np.zeros(self.n); v[0]=1.0
            elif len(bl)==1: v=self.weighted(cap,bl[0])
            else: v=fftmul(self.blocks(cap,bl[:-1]),self.weighted(cap,bl[-1]),self.n)
            self._blk[key]=v
        return self._blk[key]
    def moment(self,cap,cnt,sig):
        key=(cap,cnt,tuple(sorted(sig)))
        if key not in self._mom:
            a=np.zeros(self.n)
            for bl,co in moment_terms(cnt,sig):
                a+=co*fftmul(self.ppow(cap,cnt-len(bl)),self.blocks(cap,bl),self.n)
            self._mom[key]=a
        return self._mom[key]
    def mask(self,lower,upper,count):
        idx=np.arange(self.n)+count
        return (idx>int(lower//self.hq))&(idx<=int(upper//self.hq))
    def gram(self):
        k,n,h=self.k,self.n,self.h; P=len(DESC)
        x=(np.arange(n)+k/2)*h-0.9
        # --- A (outer norm) ---
        A=np.zeros((P,P))
        for lo,up,cap in self.outer:
            m=self.mask(lo,up,k)
            cache={}
            for i,(si,di) in enumerate(DESC):
                for j in range(i,P):
                    sj,dj=DESC[j]; eta=tuple(sorted(si+sj))
                    if eta not in cache: cache[eta]=self.moment(cap,k,eta)*m
                    v=(x**(di+dj)*cache[eta]).sum()
                    A[i,j]+=v
                    if j!=i: A[j,i]+=v
        # --- B (hybrid face numerator) ---
        m0=F(49999,50000); lam=F(1,125); K=F(17,50)
        a=float(m0*m0-m0*lam); b=float((1-m0/lam)*(1-m0)*K)
        regw=[1.0,a+b,b]
        # affine rows per outer shell: row[(desc idx, split)] (39-sum index)
        shellrows=[]
        for lo,up,cap in self.outer:
            m=self.mask(lo,up,k); rows={}
            for p,(s,d) in enumerate(DESC):
                rad=(x**d)*m
                for rem,ex,mu in fiber_splits(s):
                    fib=self.g*self.surv(cap)*self.t**ex
                    corr=fftmul(rad,fib[::-1].copy(),2*n-1)[n-1:2*n-1]
                    rows[(p,rem)]=rows.get((p,rem),0)+mu*corr
            shellrows.append((cap,rows))
        B=np.zeros((3,P,P))
        for li,cap in enumerate(self.caps):
            allowed=[]
            for lab in ('base','enlarged','full'):
                al=np.zeros(n,bool)
                for lo,up,c in self.inner[lab]:
                    if c is None or (cap is not None and cap<=c): al|=self.mask(lo,up,k-1)
                allowed.append(al)
            masks=[allowed[0],allowed[1]&~allowed[0],allowed[2]&~allowed[1]]
            W=np.stack([mk.astype(float) for mk in masks])
            if not W.any(): continue
            rows={}
            for scap,sr in shellrows:
                if scap is None or (cap is not None and cap<=scap):
                    for key,v in sr.items(): rows[key]=rows.get(key,0)+v
            if not rows: continue
            keys=list(rows)
            mcache={}
            def dmom(eta):
                if eta not in mcache:
                    v=self.moment(cap,k-1,eta)
                    if li: v=v-self.moment(self.caps[li-1],k-1,eta)
                    mcache[eta]=v[None,:]*W
                return mcache[eta]
            for i1,(p,rp) in enumerate(keys):
                for (q,rq) in keys[i1:]:
                    eta=tuple(sorted(rp+rq))
                    v=(dmom(eta)*(rows[(p,rp)]*rows[(q,rq)])[None,:]).sum(axis=1)
                    B[:,p,q]+=v
                    if (q,rq)!=(p,rp): B[:,q,p]+=v
            # release caches of other caps
            self._mom={kk:vv for kk,vv in self._mom.items() if kk[0]==cap}
        B*=k*h/self.Z
        return A,B

if __name__=='__main__':
    k=int(sys.argv[1]) if len(sys.argv)>1 else 40; N=int(sys.argv[2]) if len(sys.argv)>2 else 98304
    mix=tuple(map(float,sys.argv[3].split(','))) if len(sys.argv)>3 else (0.105,0.01,181.4)
    E=Engine(k,N,mix); print('ladders',E.ladders,'outer shells',[(float(a),float(b),float(c)) for a,b,c in E.outer],'caps',len(E.caps))
    A,B3=E.gram(); tag='_'.join(f'{v:g}' for v in mix); np.save(f'gram3_k{k}_N{N}_{tag}.npy',np.concatenate([A[None],B3]))
    a_,b_=0.9919601604,-0.000843183; B=B3[0]+(a_+b_)*B3[1]+b_*B3[2]
    c=C_THEIRS; I=c@A@c; J=c@B@c; rs=float(E.rs)
    print('k',k,'N',N,'I_H %.10e'%I,'J %.10e'%J,'cap quotient %.8f'%(rs*J/I))
