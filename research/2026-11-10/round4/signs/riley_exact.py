# SCRIPT: RILEY-EXACT-LIB
# Shared library. The Riley relation of the two-bridge knot p/q (q odd) as an EXACT integer polynomial E(s, v)
# (a = [[s,1],[0,1/s]], b = [[s,0],[-v,1/s]], scaled by powers of s), so no coefficient is ever trimmed by size.
# Why it exists: /home/claude/work/never_turn_02.py builds the coefficients in floating point and then drops leading
# coefficients smaller than 1e-25 of the largest. At large s (or large p) TRUE leading coefficients are that small
# (ratio ~ s^(-2 deg)), so branches with v ~ s^2 are lost. This library evaluates exact integer coefficients instead.
import mpmath as mp
from math import gcd
from sympy.polys.rings import ring
from sympy import ZZ
R,s_,v_=ring('s,v',ZZ)
def cf(p,q):
    o=[]
    while q: o.append(p//q); p,q=q,p%q
    return o
def eps(p,q): return [(-1)**((i*q)//p) for i in range(1,p)]
def _mm(X,Y): return [[X[i][0]*Y[0][j]+X[i][1]*Y[1][j] for j in range(2)] for i in range(2)]
def riley(p,q):
    A=[[s_**2,s_],[R(0),R(1)]]; Ai=[[R(1),-s_],[R(0),s_**2]]; B=[[s_**2,R(0)],[-v_*s_,R(1)]]; Bi=[[R(1),R(0)],[v_*s_,s_**2]]
    W=[[R(1),R(0)],[R(0),R(1)]]
    for i,x in enumerate(eps(p,q)): W=_mm(W,((B if x>0 else Bi) if i%2==0 else (A if x>0 else Ai)))
    E=_mm(A,W)[0][1]-_mm(W,B)[0][1]
    by={}
    for (i,j),c in E.terms(): by.setdefault(j,[]).append((i,int(c)))
    return by            # {power of v: [(power of s, integer coefficient), ...]}
def vcoeffs(by,s):
    n=max(by); lo=min(i for j in by for i,_ in by[j]); out=[]
    for j in range(n,-1,-1):
        out.append(mp.fsum(c*s**(i-lo) for i,c in by.get(j,[])) if j in by else mp.mpf(0))
    return out           # highest power of v first
def branches(by,x,dps):
    """all roots v at s = e^x; returns list of (v, t, k, is_real) with k = v (t - 2), t = tr(ab)."""
    mp.mp.dps=dps; s=mp.e**mp.mpf(x); co=vcoeffs(by,s)
    try: roots=mp.polyroots(co,maxsteps=400+20*len(co),extraprec=4*dps+10*len(co))
    except mp.libmp.libhyper.NoConvergence: roots=mp.polyroots(co,maxsteps=4000+100*len(co),extraprec=10*dps+40*len(co))
    out=[]
    for v in roots:
        real=abs(mp.im(v))<=mp.mpf(10)**(-dps//2)*max(1,abs(v))
        vr=mp.re(v); t=s*s+1/(s*s)-vr; out.append((v,t,vr*(t-2),real))
    return out
def band(by,x,dps):
    return [(v,t,k) for v,t,k,real in branches(by,x,dps) if real and mp.re(v)>0 and t>2 and 0<k<4]
def knots(pmax,pmin=3):
    """two-bridge knots up to mirror and up to q <-> q^-1; representative = smallest odd of {q, p-q, q^-1, p-q^-1}."""
    seen={}
    for p in range(pmin,pmax+1,2):
        for q in range(1,p):
            if gcd(p,q)!=1: continue
            qi=pow(q,-1,p); c=[q,p-q,qi,p-qi]; key=(p,min(c))
            if key not in seen: seen[key]=min(x for x in c if x%2==1)
    return sorted((p,q) for (p,_),q in seen.items())
