# SCRIPT: RILEY-EXACT-W-LIB
# Second view of the exact Riley relation: the variable w = tr(ab) - 2 = s^2 + s^-2 - 2 - v instead of v.
# Why it exists: v and w are the two roots of X^2 + dM X + k = 0 (k = v w). Branches with tr(ab) -> 2 have v ~ s^2 in a
# tight cluster; mpmath.polyroots on the v-polynomial returns them inaccurately even at 200 digits and they are then
# counted as complex (found on 47/3, 41/7, 59/29 at x = 12). In the w-polynomial the same branches are small and
# well separated. A band test must look at BOTH polynomials.
import sys
sys.path.insert(0,'/home/claude/work/agent_signs')
import riley_exact as RE
from riley_exact import *
def to_w(by):
    R,s,w=RE.R,RE.s_,RE.v_
    jmax=max(by); A=s**4-2*s**2+1-w*s**2; pw={0:R(1)}
    for j in range(1,jmax+1): pw[j]=pw[j-1]*A
    tot=R(0)
    for j,lst in by.items():
        mono=R(0)
        for i,c in lst: mono+=c*s**(i+2*(jmax-j))
        tot+=mono*pw[j]
    out={}
    for (i,j),c in tot.terms(): out.setdefault(j,[]).append((i,int(c)))
    return out
def band2(by,bw,x,dps):
    """band points from both views: list of (view, small root, k). In either view the root r gives k = r (A - r)."""
    mp.mp.dps=dps; s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2; out=[]
    for nm,b in (('v',by),('w',bw)):
        co=vcoeffs(b,s)
        try: roots=mp.polyroots(co,maxsteps=400+20*len(co),extraprec=4*dps+10*len(co))
        except mp.libmp.libhyper.NoConvergence: roots=mp.polyroots(co,maxsteps=6000+200*len(co),extraprec=12*dps+60*len(co))
        for r in roots:
            if abs(mp.im(r))>mp.mpf(10)**(-dps//2)*max(1,abs(r)): continue
            r=mp.re(r); k=r*(A-r)
            if 0<r<A and 0<k<4: out.append((nm,r,k))
    return out
def sign_scan(b,x,dps,n=400):
    """root-finder-free evidence: sign changes of the polynomial along the band region 0 < r < A, k = r(A-r) < 4.
    Scans r in (0, min(A/2, r1)) where r1 is the smaller root of r(A-r) = 4 (the half r < A/2 of the band in this view;
    the other half is the same set seen in the other view). Returns number of sign changes."""
    mp.mp.dps=dps; s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2
    hi=A/2 if A*A<=16 else (A-mp.sqrt(A*A-16))/2
    co=vcoeffs(b,s); prev=None; ch=0
    for i in range(1,n):
        r=hi*i/n; val=mp.polyval(co,r); sg=mp.sign(val)
        if prev is not None and sg!=0 and sg!=prev: ch+=1
        if sg!=0: prev=sg
    return ch
