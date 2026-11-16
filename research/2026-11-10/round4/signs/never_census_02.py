# SCRIPT: NEVER-CENSUS-02
# Q3 census, repaired. NEVER-CENSUS-01 reported six knots as TURN "by roots only" at x = 3.5 or 4 (47/9, 49/9, 49/17,
# 53/5, 53/17, 55/21). Rechecked: for 47/9 the 80-digit root finder returned a spurious real root v ~ A (k ~ 4e-10)
# from the v ~ s^2 cluster; at 160 and 320 digits there is none. Same trap as the 40-digit false turn of 43/5.
# usage: never_census_02.py PMIN PMAX OUTFILE
import sys, time, json, mpmath as mp
from multiprocessing import Pool
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact_w import *
PMIN,PMAX,OUT=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]; DPS=80
HEAD='''DEFINITION (as NEVER-TURN-02): the pair turns at x iff some REAL root v of the Riley relation at s = e^x has v > 0,
 t = tr(ab) > 2 and k = v (t - 2) < 4.  NEVER = no such root on the grid x = 0.1..1.5 (step 0.1), 2, 2.5, 3, 3.5, 4.
WHY THIS CHECK DECIDES IT
 v and w = t - 2 are the two roots of X^2 + dM X + k = 0, so the band is {v < A/2} + {w < A/2} (A = v + w), k = r (A - r) < 4.
 Each half is read in the variable where its roots are SMALL (v-polynomial for v < A/2, w-polynomial for w < A/2),
 with exact integer coefficients; the large cluster of either polynomial is never used (that is where polyroots fails).
 Pass 1: sign change of the exact polynomial along the half band (no root finder): proves a real root -> TURN.
 Pass 2 (only if pass 1 is silent at every x): roots at 80 digits in both views. A root-only hit must be confirmed by a
 sign change of the polynomial across r (1 -+ 1e-6) evaluated at 160 digits, else it is listed as UNCONFIRMED.
 Torus knots p/1 are run only for p <= 21 (control); for all p the centre argument of Two Trees Thm 8.7 applies.
CONTROL / KILL: Two Trees census 8.8 must come out 19 turn / 7 never.'''
XS=[0.8,0.5,1.2,0.3,1.0,0.6,1.5,0.4,0.7,0.2,0.9,1.1,1.3,1.4,0.1,2.0,2.5,3.0,3.5,4.0]
def half(x):
    s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2
    return s,A,(A/2 if A*A<=16 else (A-mp.sqrt(A*A-16))/2)
def scan(b,x,n=240):
    mp.mp.dps=DPS; s,A,hi=half(x); co=vcoeffs(b,s)
    pts=sorted(set([hi*i/n for i in range(0,n+1)]+[hi*mp.mpf(10)**(-j/8) for j in range(1,160)])); prev=None; ch=0
    for r in pts:
        sg=mp.sign(mp.polyval(co,r))
        if sg==0: continue
        if prev is not None and sg!=prev: ch+=1
        prev=sg
    return ch
def roots_half(b,x):
    mp.mp.dps=DPS; s,A,hi=half(x); co=vcoeffs(b,s)
    try: roots=mp.polyroots(co,maxsteps=400+20*len(co),extraprec=4*DPS+10*len(co))
    except mp.libmp.libhyper.NoConvergence: roots=mp.polyroots(co,maxsteps=6000+200*len(co),extraprec=12*DPS+60*len(co))
    out=[]; near=[]
    for r in roots:
        rr=mp.re(r)
        if not (0<rr<hi): continue
        im=abs(mp.im(r))/abs(r)
        if im<=mp.mpf(10)**(-DPS//2): out.append(rr)
        elif im<mp.mpf(10)**-6: near.append(round(float(mp.log10(im)),1))
    conf=[]
    for rr in out:
        mp.mp.dps=160; s2,A2,hi2=half(x); co2=vcoeffs(b,s2)
        a_,b_=mp.polyval(co2,rr*(1-mp.mpf(10)**-6)),mp.polyval(co2,rr*(1+mp.mpf(10)**-6)); conf.append(mp.sign(a_)!=mp.sign(b_)); mp.mp.dps=DPS
    return [float(r*(A-r)) for r in out],conf,near
def work(pq):
    p,q=pq; t0=time.time(); by=riley(p,q); bw=to_w(by)
    for x in XS:
        if scan(by,x)+scan(bw,x)>0: return dict(p=p,q=q,verdict='TURN',how='sign change',x=x,sec=round(time.time()-t0,1))
    border=[]; unconf=[]
    for x in XS:
        for nm,b in (('v',by),('w',bw)):
            ks,conf,near=roots_half(b,x); border+=near
            if any(conf): return dict(p=p,q=q,verdict='TURN',how='roots, confirmed by sign change at 160 digits',x=x,k=ks[:3],sec=round(time.time()-t0,1))
            if ks: unconf.append((x,nm,ks[:2]))
    return dict(p=p,q=q,verdict='NEVER',how='no real band root on the grid',border=sorted(set(border))[:4],unconfirmed=unconf,sec=round(time.time()-t0,1))
if __name__=='__main__':
    print(HEAD,flush=True); ks=[(p,q) for p,q in knots(PMAX,PMIN) if q>1 or p<=21]; t0=time.time(); res=[]
    with Pool(2) as pool:
        for r in pool.imap(work,ks,chunksize=1):
            res.append(r); print('%d/%d cf %s  %s  (%s%s) %.1fs'%(r['p'],r['q'],str(cf(r['p'],r['q'])).replace(' ',''),r['verdict'],r['how'],', first found at x=%s'%r['x'] if 'x' in r else '',r['sec']),flush=True)
            json.dump(res,open(OUT,'w'))
    print('knots %d  TURN %d  NEVER %d  (%.0f s)'%(len(res),sum(r['verdict']=='TURN' for r in res),sum(r['verdict']=='NEVER' for r in res),time.time()-t0))
    print('NEVER:',[(r['p'],r['q'],cf(r['p'],r['q'])) for r in res if r['verdict']=='NEVER'])
    print('TURN found by roots only:',[(r['p'],r['q'],r['x'],r['k']) for r in res if r['how'].startswith('roots')])
    print('NEVER with unconfirmed root-finder hits (x, view, k):',[(r['p'],r['q'],r['unconfirmed']) for r in res if r['verdict']=='NEVER' and r['unconfirmed']])
    print('NEVER with a near-real complex pair in the half band (log10 relative |Im|):',[(r['p'],r['q'],r['border']) for r in res if r['verdict']=='NEVER' and r['border']])
