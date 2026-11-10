# SCRIPT: NEVER-CENSUS-01
# Q3: which two-bridge knots never turn.  Census by exact coefficients, two views, with a root-finder-free first pass.
# usage: never_census_01.py PMIN PMAX OUTFILE [DPS]
import sys, time, json, mpmath as mp
from multiprocessing import Pool
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact_w import *
PMIN,PMAX,OUT=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]; DPS=int(sys.argv[4]) if len(sys.argv)>4 else 80
HEAD='''DEFINITION (as NEVER-TURN-02): on the real slice s = e^x the pair turns at x iff some REAL root v of the Riley
 relation has v > 0, t = tr(ab) > 2 and k = v (t - 2) < 4.  "Never" = no such root at any x of the grid
 x = 0.1, 0.2, ..., 1.5, 2, 2.5, 3, 3.5, 4 (the grid of NEVER-TURN-02).
WHY THIS CHECK DECIDES IT (and what was changed from NEVER-TURN-02):
 (1) coefficients are exact integers evaluated at s (no trimming of small leading coefficients: that trimming drops
     true branches with v ~ s^2 at large s or large p);
 (2) TURN is first looked for WITHOUT a root finder: a sign change of the exact polynomial along the band region
     (uniform and logarithmic sample points, in v and in w = t - 2) proves a real root there;
 (3) only if no sign change is found at any x are the roots computed (mpmath.polyroots, %d digits): in v for x <= 1.5,
     in v and in w for x >= 2 (each view loses the other's cluster at large s).
KILL / CONTROL: the 26 knots of Two Trees census 8.8 must come out 19 turn / 7 never, and the eleven never-turners of
 NEVER-TURN-02 must be reproduced; a verdict NEVER rests on (3) and is re-run at double digits in NEVER-CENSUS-02.'''%DPS
XS=[0.8,0.5,1.2,0.3,1.0,0.6,1.5,0.4,0.7,0.2,0.9,1.1,1.3,1.4,0.1,2.0,2.5,3.0,3.5,4.0]
def scan(b,x,n=240):
    mp.mp.dps=DPS; s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2
    hi=A/2 if A*A<=16 else (A-mp.sqrt(A*A-16))/2
    co=vcoeffs(b,s); pts=[hi*i/n for i in range(0,n)]+[hi*mp.mpf(10)**(-j/8) for j in range(1,160)]
    pts=sorted(set(pts)); prev=None; ch=0
    for r in pts:
        sg=mp.sign(mp.polyval(co,r))
        if sg==0: continue
        if prev is not None and sg!=prev: ch+=1
        prev=sg
    return ch
def roots_band(b,x):
    mp.mp.dps=DPS; s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2; co=vcoeffs(b,s)
    try: roots=mp.polyroots(co,maxsteps=400+20*len(co),extraprec=4*DPS+10*len(co))
    except mp.libmp.libhyper.NoConvergence: roots=mp.polyroots(co,maxsteps=6000+200*len(co),extraprec=12*DPS+60*len(co))
    out=[]; near=[]
    for r in roots:
        im=abs(mp.im(r))/max(1,abs(r)); rr=mp.re(r); k=rr*(A-rr)
        if im<=mp.mpf(10)**(-DPS//2):
            if 0<rr<A and 0<k<4: out.append(float(k))
        elif im<mp.mpf(10)**-8 and 0<rr<A and 0<k<4: near.append(float(mp.log10(im)))
    return out,near
def work(pq):
    p,q=pq; t0=time.time(); by=riley(p,q); bw=to_w(by)
    for x in XS:
        if scan(by,x)+scan(bw,x)>0: return dict(p=p,q=q,verdict='TURN',how='sign change',x=x,sec=round(time.time()-t0,1))
    border=[]
    for x in XS:
        h,near=roots_band(by,x); border+=near
        if not h and x>=2: h2,near2=roots_band(bw,x); h+=h2; border+=near2
        if h: return dict(p=p,q=q,verdict='TURN',how='roots only (even cluster)',x=x,k=h[:3],sec=round(time.time()-t0,1))
    return dict(p=p,q=q,verdict='NEVER',how='no real band root on the grid',border=border[:5],sec=round(time.time()-t0,1))
if __name__=='__main__':
    print(HEAD,flush=True); ks=knots(PMAX,PMIN); t0=time.time(); res=[]
    with Pool(2) as pool:
        for r in pool.imap(work,ks,chunksize=1):
            res.append(r); print('%d/%d cf %s  %s  (%s%s) %.1fs'%(r['p'],r['q'],str(cf(r['p'],r['q'])).replace(' ',''),r['verdict'],r['how'],', first found at x=%s'%r['x'] if 'x' in r else '',r['sec']),flush=True)
    json.dump(res,open(OUT,'w'))
    print('knots %d  TURN %d  NEVER %d  (%.0f s)'%(len(res),sum(r['verdict']=='TURN' for r in res),sum(r['verdict']=='NEVER' for r in res),time.time()-t0))
    print('NEVER:',[(r['p'],r['q'],cf(r['p'],r['q'])) for r in res if r['verdict']=='NEVER'])
    print('TURN found by roots only:',[(r['p'],r['q'],r['x']) for r in res if r['how'].startswith('roots')])
    print('NEVER with a near-real complex root in the band (borderline, log10 |Im|):',[(r['p'],r['q'],r['border']) for r in res if r['verdict']=='NEVER' and r['border']])
