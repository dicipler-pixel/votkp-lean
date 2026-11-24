# SCRIPT: OPPOSITE-WALK-LIB-01
# Shared pieces for the "try the opposite" variants.
# Walker: the chain L_n = B(e_s1, r1) ... B(e_sn, rn) in SO(1,k), kept in polar form L = Boost(d n) R
# (distance d, heading n, frame R) so it never overflows. One step appends B(e_s, r):
#   w = R e_s, c = n.w
#   cosh d' = cosh d (cosh r + tanh d sinh r c)                       (exact)
#   n' ~ sinh r w/cosh d + (1-1/cosh d) c sinh r n + tanh d cosh r n  (exact, spatial part of Boost(dn)(cosh r, sinh r w))
#   R' = W R, W = rotation in the (n,w) plane carrying w toward n by eps,
#   tan(eps/2) = sin th / (coth(d/2) coth(r/2) + cos th)              (exact Wigner-Thomas angle)
# check_walker() compares this against plain 4x4 / (k+1)x(k+1) matrix products (must agree to 1e-9).
import numpy as np, math, os
from numba import njit
HERE=os.path.dirname(os.path.abspath(__file__))

def primes_upto(N):
    f=os.path.join(HERE,'primes_%d.npy'%N)
    if os.path.exists(f): return np.load(f)
    s=np.ones(N+1,dtype=bool); s[:2]=False
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=False
    P=np.nonzero(s)[0].astype(np.int64); np.save(f,P); return P

@njit(cache=True)
def _walk(r,arm,E,rec_idx,renorm=20000):
    k=E.shape[1]; d=0.0; n=np.zeros(k); R=np.eye(k)
    nrec=rec_idx.shape[0]; D=np.zeros(nrec); N=np.zeros((nrec,k)); RR=np.zeros((nrec,k,k)); TOT=np.zeros(nrec)
    j=0; tot=0.0
    for i in range(r.shape[0]):
        ri=r[i]; w=R@E[arm[i]]
        if ri<0.0:
            ri=-ri; w=-w
        if d==0.0:
            d=ri; n=w/np.sqrt(w@w)
        else:
            c=n@w
            if c>1.0: c=1.0
            if c<-1.0: c=-1.0
            ch=math.cosh(ri); sh=math.sinh(ri); td=math.tanh(d)
            Y=ch+td*sh*c
            if d<15.0:
                x=math.cosh(d)*Y
                dn=math.acosh(x) if x>1.0 else 0.0
            else:
                base=d+math.log(Y)+math.log1p(math.exp(-2*d))
                dn=base
                for _ in range(3):
                    dn=base-math.log1p(math.exp(-2*dn))
            icd=1.0/math.cosh(d) if d<700 else 0.0
            sp=sh*icd*w+((1.0-icd)*c*sh+td*ch)*n
            nn=sp/math.sqrt(sp@sp)
            perp=w-c*n; s=math.sqrt(perp@perp)
            if s>1e-15:
                a1=perp/s; a2=n
                eps=2.0*math.atan2(s,1.0/(math.tanh(d/2)*math.tanh(ri/2))+c)
                tot+=eps
                ce=math.cos(eps)-1.0; se=math.sin(eps)
                p1=a1@R; p2=a2@R
                R=R+ce*(np.outer(a1,p1)+np.outer(a2,p2))+se*(np.outer(a2,p1)-np.outer(a1,p2))
            d=dn; n=nn
        if (i+1)%renorm==0:
            Q,Rr=np.linalg.qr(R)
            for q in range(k):
                if Rr[q,q]<0: Q[:,q]=-Q[:,q]
            R=Q
        while j<nrec and rec_idx[j]==i:
            D[j]=d; N[j]=n; RR[j]=R; TOT[j]=tot; j+=1
    return D,N,RR,TOT

def walk(r,arm,E,rec_idx):
    return _walk(np.ascontiguousarray(r,dtype=np.float64),np.ascontiguousarray(arm,dtype=np.int64),
                 np.ascontiguousarray(E,dtype=np.float64),np.ascontiguousarray(rec_idx,dtype=np.int64))

def boostmat(v,r):
    k=len(v); B=np.eye(k+1); c,s=math.cosh(r),math.sinh(r)
    B[0,0]=c; B[0,1:]=B[1:,0]=s*v; B[1:,1:]=np.eye(k)+(c-1)*np.outer(v,v); return B

def check_walker(r,arm,E,nsteps=3000):
    k=E.shape[1]; L=np.eye(k+1)
    for i in range(nsteps):
        v=E[arm[i]]*(1 if r[i]>0 else -1); L=L@boostmat(v,abs(r[i]))
    g=L[0,0]; d=math.acosh(g); n=L[1:,0]/math.sinh(d)
    R=(np.linalg.inv(boostmat(n,d))@L)[1:,1:]
    D,N,RR,_=walk(r[:nsteps],arm[:nsteps],E,np.array([nsteps-1]))
    return abs(D[0]-d),np.abs(N[0]-n).max(),np.abs(RR[0]-R).max(),d

def rot_angles(R):
    """principal rotation angles (degrees) of an orthogonal matrix, largest first"""
    ev=np.linalg.eigvals(R); a=np.sort(np.abs(np.angle(ev)))[::-1]
    out=[]; i=0
    while i<len(a):
        if a[i]>1e-12: out.append(a[i]); i+=2
        else: i+=1
    return [math.degrees(x) for x in out] or [0.0]

def ang(u,v):
    return math.degrees(math.acos(max(-1.0,min(1.0,float(u@v)/(np.linalg.norm(u)*np.linalg.norm(v))))))

def report(name,a_end,r,arm,E,cuts,Pvec,extra=''):
    """a_end: value (e.g. next start) attached to each step, used for cut-offs. Prints the standard table."""
    rec=[]; used=[]
    for x in cuts:
        idx=np.searchsorted(a_end,x,side='right')-1
        if idx>=0 and (not rec or idx>rec[-1]): rec.append(idx); used.append(x)
    rec=np.array(rec)
    D,N,RR,TOT=walk(r,arm,E,rec)
    Lc=np.cumsum(np.abs(r))[rec]; S2=np.cumsum(r*r)[rec]
    Pn=np.linalg.norm(Pvec); Pu=Pvec/Pn if Pn>0 else None
    print('=== %s  |P| = %.6f  %s'%(name,Pn,extra))
    print(' cut      steps       L        d        d/L     d-|P|L   sum r^2   turn(deg)   dFrame(deg)  lock(deg)')
    prevR=None; rows=[]
    for j,x in enumerate(used):
        ta=rot_angles(RR[j]); turn=math.sqrt(sum(t*t for t in ta)) if len(ta)>1 else ta[0]
        dF=float('nan') if prevR is None else (lambda q: math.sqrt(sum(t*t for t in q)))(rot_angles(RR[j]@prevR.T))
        u=RR[j].T@N[j]; lock=ang(u,Pu) if Pu is not None else float('nan')
        rows.append(dict(cut=x,steps=int(rec[j]+1),L=float(Lc[j]),d=float(D[j]),ratio=float(D[j]/Lc[j]),c=float(D[j]-Pn*Lc[j]),
                         s2=float(S2[j]),turn=turn,angles=ta,dF=dF,lock=lock,u=u.tolist(),totturn=float(math.degrees(TOT[j]))))
        print(' %-8.0e %9d %8.4f %9.4f %8.5f %8.4f %9.5f %10.3f %11.4f %9.3f'%(x,rec[j]+1,Lc[j],D[j],D[j]/Lc[j],D[j]-Pn*Lc[j],S2[j],turn,dF,lock))
        prevR=RR[j]
    return rows

def verdict(rows,Pn,tol=0.01):
    byc={r_['cut']:r_ for r_ in rows}
    cs=[byc[x]['c'] for x in (1e6,1e7) if x in byc]
    c=float(np.mean(cs)); last=rows[-1]
    pred=Pn+c/last['L']; rel=abs(last['ratio']-pred)/pred if pred!=0 else abs(last['ratio']-pred)
    if len(rows)>=3:
        a,b=rows[-3],rows[-1]; slope=(b['d']-a['d'])/(b['L']-a['L'])
    else: slope=float('nan')
    print(' fit c (mean of 1e6,1e7) = %.4f ; predicted d/L at largest cut = %.5f ; measured %.5f ; rel diff %.3f%% -> %s ; free slope over last two decades = %.4f'
          %(c,pred,last['ratio'],100*rel,'PASS' if rel<=tol else 'KILL',slope))
    return c,pred,rel,slope
