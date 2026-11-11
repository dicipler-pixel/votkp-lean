# SCRIPT: NEVER-RULE-04
# Q3: R3 tested on knots it was NOT read from: 77 <= p <= 101, plus the lead R4 for the three never-turners R3 misses.
import sys, time, json, mpmath as mp
from fractions import Fraction as Fr
from multiprocessing import Pool
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact_w import *
print('''R3: non-torus NEVER iff p/q = a +- 1/(b + 1/c), a odd >= 3, b, c even >= 2, a > c.
R4 (lead, read off 55/21, 71/21, 75/29 after NEVER-RULE-03): p/q = a +- 1/E with E an even continued fraction of length 4
   whose entries pair up by sign, E = [2,2,-2,-2] = 21/8 or [2,2,2,2] = 29/12.  Predictions: 97/21 = 5 - 8/21 and
   99/29 = 3 + 12/29 never.
WHY THIS CHECK DECIDES IT
 (i) every knot R3 predicts NEVER in 77 <= p <= 101: a sign change of the exact Riley polynomial in the half band at any
     grid x (80 digits, re-evaluated at 160) PROVES a turn and kills R3.  Silence is not proof of never.
 (ii) every near miss (a odd >= 3, b, c even, a < c or a = c) in the same range is predicted TURN: a sign change proves it;
     silence there counts against R3 (listed).
 (iii) CAP: the root finder (needed to call NEVER) is run only on 4 knots and only at x = 0.5, 0.8, 1.2, 2.0 in both views
     (degree 38-50 polynomials at 80 digits; the full 20-point grid would take about 20 minutes per knot).
KILL: any sign change in (i); any silent knot in (ii) is reported as a possible miss; any confirmed real band root in (iii).''')
XS=[0.8,0.5,1.2,0.3,1.0,0.6,1.5,0.4,0.7,0.2,0.9,1.1,1.3,1.4,0.1,2.0,2.5,3.0,3.5,4.0]
def half(x):
    s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2
    return s,A,(A/2 if A*A<=16 else (A-mp.sqrt(A*A-16))/2)
def scan(b,x,dps,n=300):
    mp.mp.dps=dps; s,A,hi=half(x); co=vcoeffs(b,s)
    pts=sorted(set([hi*i/n for i in range(0,n+1)]+[hi*mp.mpf(10)**(-j/8) for j in range(1,160)])); prev=None; ch=0
    for r in pts:
        sg=mp.sign(mp.polyval(co,r))
        if sg==0: continue
        if prev is not None and sg!=prev: ch+=1
        prev=sg
    return ch
def key(p,q):
    q%=p; qi=pow(q,-1,p); c=[q,p-q,qi,p-qi]; return (p,min(z for z in c if z%2==1))
def scan_knot(k):
    p,q=k; by=riley(p,q); bw=to_w(by)
    for x in XS:
        for b in (by,bw):
            if scan(b,x,80) and scan(b,x,160): return (k,x)
    return (k,None)
def roots_knot(k):
    p,q=k; by=riley(p,q); bw=to_w(by); hits=[]; near=[]
    for x in (0.8,0.5,1.2,2.0):
        for nm,b in (('v',by),('w',bw)):
            mp.mp.dps=80; s,A,hi=half(x); co=vcoeffs(b,s)
            try: roots=mp.polyroots(co,maxsteps=400+20*len(co),extraprec=320+10*len(co))
            except mp.libmp.libhyper.NoConvergence: roots=mp.polyroots(co,maxsteps=8000+200*len(co),extraprec=1200+60*len(co))
            for r in roots:
                rr=mp.re(r)
                if not (0<rr<hi): continue
                im=abs(mp.im(r))/abs(r)
                if im<=mp.mpf(10)**-40:
                    mp.mp.dps=160; s2,A2,hi2=half(x); co2=vcoeffs(b,s2)
                    conf=mp.sign(mp.polyval(co2,rr*(1-mp.mpf(10)**-6)))!=mp.sign(mp.polyval(co2,rr*(1+mp.mpf(10)**-6))); mp.mp.dps=80
                    hits.append((x,nm,float(rr*(A-rr)),bool(conf)))
                elif im<mp.mpf(10)**-6: near.append(round(float(mp.log10(im)),1))
    return (k,hits,sorted(set(near))[:4])
if __name__=='__main__':
    t0=time.time(); pred={}; nearm={}
    for a in range(3,40,2):
        for b in range(2,60,2):
            for c in range(2,60,2):
                for sg in (1,-1):
                    z=Fr(a)+sg/(Fr(b)+Fr(1,c)); p,q=z.numerator,z.denominator
                    if p%2==0 or not (77<=p<=101) or q==1: continue
                    (pred if a>c else nearm)[key(p,q)]=(a,'+' if sg>0 else '-',b,c)
    print('\nR3 predicts NEVER for %d knots with 77 <= p <= 101; near misses (a <= c) predicted TURN: %d'%(len(pred),len(nearm)))
    with Pool(2) as pool:
        r1=pool.map(scan_knot,sorted(pred)); r2=pool.map(scan_knot,sorted(nearm)); r3=pool.map(scan_knot,[key(97,21),key(99,29)])
    print('(i) predicted NEVER: sign change found (R3 killed there) in %d of %d: %s'%(sum(x is not None for k,x in r1),len(r1),[(k,pred[k],x) for k,x in r1 if x is not None]))
    print('    silent (consistent with never):',[('%d/%d'%k,pred[k]) for k,x in r1 if x is None])
    print('(ii) near misses predicted TURN: turn proved in %d of %d; silent: %s'%(sum(x is not None for k,x in r2),len(r2),[('%d/%d'%k,nearm[k]) for k,x in r2 if x is None]))
    print('     proved turns:',[('%d/%d'%k,nearm[k],'x=%s'%x) for k,x in r2 if x is not None])
    print('R4 lead: 97/21 and 99/29 sign scan:',[('%d/%d'%k,'TURN proved at x=%s'%x if x is not None else 'silent') for k,x in r3])
    print('   [%.0f s so far]'%(time.time()-t0),flush=True)
    sil=[k for k,x in r1 if x is None]
    sample=[k for k in ([k for k in sil if pred[k][1]=='+'][:1]+[k for k in sil if pred[k][1]=='-'][:1])]+[k for k,x in r3 if x is None]
    print('(iii) root finder on the capped sample',['%d/%d'%k for k in sample],flush=True)
    with Pool(2) as pool:
        for k,hits,near in pool.imap(roots_knot,sample):
            print('    %d/%d cf %s: real band roots at x = 0.5, 0.8, 1.2, 2.0: %s ; near-real complex pairs (log10 rel. Im): %s  -> %s'%(k[0],k[1],cf(*k),hits,near,'TURN' if any(h[3] for h in hits) else ('no confirmed real band root at the 4 sampled x' if not hits else 'unconfirmed root-finder hits only')),flush=True)
    print('[%.0f s]'%(time.time()-t0))
