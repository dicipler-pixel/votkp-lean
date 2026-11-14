# SCRIPT: CHK-07-RILEY-CENSUS (independent recomputation of band entry for the 26 two-bridge knots from the R7 rwords)
import sys, math, time
from mpmath import mp, mpf, polyroots, exp, mpc
mp.dps=60
WORDS={'T(2,3)':'ba','T(2,5)':'baba','4_1':'bABa','T(2,7)':'bababa','5_2':'baBAba','6_1':'bABabABa','6_2':'babABABaba','7_2':'baBAbaBAba',
'7_3':'babaBABAbaba','6_3':'baBABabABAba','8_1':'bABabABabABa','7_4':'bAbaBaBAbAbaBa','8_2':'bababABABABababa','7_5':'babABAbabaBABaba','8_3':'bAbABaBabAbABaBa',
'8_4':'babABABababABABaba','7_6':'baBABabaBAbababABAba'.replace('babababABAba','bababABAba') if False else 'baBABabaBAbabABAba','7_7':'bABaBAbaBabAbaBAbABa','8_7':'babaBABABababABABAbaba','8_6':'babABAbabABABabaBABaba',
'8_9':'babABABabaBABAbabABABaba','8_8':'baBABabaBABabABAbabABAba','8_11':'bABaBAbABabAbaBabABaBAbABa','8_13':'baBABabABAbabABabaBABabABAba','8_12':'bABabAbaBAbABabABaBAbaBabABa','8_14':'baBAbabABabABAbaBABabABabaBAba'}
# polynomials in v: lists of mpf, index = power
def padd(a,b):
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def pmul(a,b):
    r=[mpf(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return r
def mmul(A,B):
    return [[padd(pmul(A[i][0],B[0][j]),pmul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def mats(s):
    c=lambda v:[mpf(v)]
    a=[[c(s),c(1)],[c(0),c(1/s)]]; ai=[[c(1/s),c(-1)],[c(0),c(s)]]
    b=[[c(s),c(0)],[[mpf(0),mpf(-1)],c(1/s)]]; bi=[[c(1/s),c(0)],[[mpf(0),mpf(1)],c(s)]]
    return {'a':a,'A':ai,'b':b,'B':bi}
def riley_poly(word,s):
    M=mats(s); W=None
    for ch in word:
        W=M[ch] if W is None else mmul(W,M[ch])
    # relation: a W - W b = 0 ; entry [0][1]
    aW=mmul(M['a'],W); Wb=mmul(W,M['b'])
    d=padd(aW[0][1],[-x for x in Wb[0][1]])
    while len(d)>1 and abs(d[-1])<mpf(10)**(-(mp.dps-10))*max(abs(y) for y in d): d.pop()
    return d
def real_roots(poly):
    if len(poly)<2: return []
    rts=polyroots(poly[::-1],maxsteps=400,extraprec=200)
    out=[]
    for r in rts:
        if abs(r.imag)<mpf(10)**(-20)*(1+abs(r.real)): out.append(r.real)
    return out
def kvals(s,v):
    A=(s-1/s)**2; return v*(A-v)   # 2 - tr[a,b]
def scan(name,xs):
    hits=[]
    for xx in xs:
        s=exp(mpf(xx)); poly=riley_poly(WORDS[name],s)
        for v in real_roots(poly):
            k=kvals(s,v)
            if 0<k<4: hits.append((xx,float(v),float(k)))
    return hits
if __name__=='__main__':
    names=sys.argv[1:] or list(WORDS)
    xs=[round(0.02+0.005*i,3) for i in range(0,200)]  # 0.02..1.015
    for nm in names:
        t0=time.time(); h=scan(nm,xs)
        print(nm,"first entry:",(h[0] if h else "none up to x=1.015"),"n_hits",len(h),"time",round(time.time()-t0,1),flush=True)
