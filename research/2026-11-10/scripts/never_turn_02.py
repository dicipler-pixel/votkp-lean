# SCRIPT: NEVER-TURN-02
# Two Trees section 9: which two-bridge knots never turn?  Extend the 26-knot census to every two-bridge knot of up to
# MAXC crossings and look for what the never-turners share.
# Method (as KNOT-COMM-BAND, at 40 digits to avoid the cancellation the paper warns about): for x on a grid, s = e^x,
# real roots v of the Riley relation; the commutator turns iff v > 0, t = tr(ab) = s^2 + s^-2 - v > 2 and v (t - 2) < 4.
# Check on the method: it must reproduce the paper's 7 never / 19 turn on the 26 knots of census 8.8.
import sys, mpmath as mp
from math import gcd
mp.mp.dps=40
MAXC=int(sys.argv[1])
def cf(p,q):
    o=[]
    while q: o.append(p//q); p,q=q,p%q
    return o
def census(maxc):
    seen={}
    for p in range(3,400,2):
        for q in range(1,p):
            if gcd(p,q)!=1 or sum(cf(p,q))>maxc: continue
            qi=pow(q,-1,p); c=[q,p-q,qi,p-qi]; key=(p,min(c))
            if key not in seen: seen[key]=(min(x for x in c if x%2==1),sum(cf(p,q)))
    return sorted((p,v[0],v[1]) for (p,_),v in seen.items())
def eps(p,q): return [(-1)**((i*q)//p) for i in range(1,p)]
def pmul(A,B):
    r=[mp.mpf(0)]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        if a==0: continue
        for j,b in enumerate(B): r[i+j]+=a*b
    return r
def padd(A,B):
    n=max(len(A),len(B)); return [(A[i] if i<len(A) else 0)+(B[i] if i<len(B) else 0) for i in range(n)]
def mmul(X,Y): return [[padd(pmul(X[i][0],Y[0][j]),pmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def riley_coeffs(p,q,s):
    one=[mp.mpf(1)]; zero=[mp.mpf(0)]
    a=[[[s],one],[zero,[1/s]]]; ai=[[[1/s],[mp.mpf(-1)]],[zero,[s]]]
    b=[[[s],zero],[[mp.mpf(0),mp.mpf(-1)],[1/s]]]; bi=[[[1/s],zero],[[mp.mpf(0),mp.mpf(1)],[s]]]
    W=[[one,zero],[zero,one]]
    for i,x in enumerate(eps(p,q)): W=mmul(W,((b if x>0 else bi) if i%2==0 else (a if x>0 else ai)))
    L=mmul(a,W)[0][1]; R=mmul(W,b)[0][1]; E=padd(L,[-c for c in R])
    while len(E)>1 and abs(E[-1])<mp.mpf(10)**(-25)*max(abs(c) for c in E): E.pop()
    return E
XS=[mp.mpf(x)/100 for x in list(range(10,160,10))+[200,250,300,350,400]]
def turns(p,q):
    first=None
    for x in XS:
        s=mp.e**x; E=riley_coeffs(p,q,s)
        if len(E)<2: continue
        try: roots=mp.polyroots(E[::-1],maxsteps=200,extraprec=200)
        except Exception: continue
        for v in roots:
            if abs(mp.im(v))>mp.mpf(10)**(-20)*max(1,abs(v)): continue
            v=mp.re(v); t=s*s+1/(s*s)-v; k=v*(t-2)
            if v>0 and t>2 and k<4:
                return float(x)
    return None
rows=[]
for p,q,c in census(MAXC):
    f=turns(p,q); rows.append((p,q,c,f)); print('%d/%d  crossings %d  cf %s  %s'%(p,q,c,cf(p,q),'turns from x<=%.1f'%f if f else 'NEVER'),flush=True)
print('NEVER:',[(p,q,cf(p,q)) for p,q,c,f in rows if f is None])
