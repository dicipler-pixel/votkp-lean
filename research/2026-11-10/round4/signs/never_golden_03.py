# SCRIPT: NEVER-GOLDEN-03
# Q3: the golden family [2, 1^n, 2] (13/5, 21/13, 55/21, 89/34, 233/89), and the unfinished 233/89 run.
# NEVER-TURN-05 (120 and 200 digits) gave 89/34 NEVER and 233/89 three band points; both used never_turn_02.riley_coeffs,
# which trims true leading coefficients (degree 44 and 116: the trimmed part is far below 1e-25 already at x = 0.8).
import sys, time, mpmath as mp
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact_w import *
print('''WHY: exact integer coefficients; a sign change of the exact polynomial along the half band, evaluated at 200 and again
at 400 digits, proves a real root in the band (TURN) without any root finder.  The band point of NEVER-TURN-05 for
233/89 (x = 0.8, v = 1.1301089, k = 2.288) is tested directly: sign of the polynomial at v (1 -+ 1e-4).
GUESS UNDER TEST (the one that "failed" earlier): n = 2, 5, 8 never; n = 0, 3, 6 turn.
KILL: a sign change for n = 5 or 8 (they would turn), or no sign change at any x for n = 3 or 6 (weak: silence is
not proof of never; a silent knot is passed to the root finder where the degree allows, and is otherwise "not decided").''')
XS=[0.8,0.5,1.2,0.3,1.0,0.6,1.5,0.4,0.7,0.2,0.9,1.1,1.3,1.4,0.1,2.0,2.5,3.0,3.5,4.0]
def scan(b,x,dps,n=600):
    mp.mp.dps=dps; s=mp.e**mp.mpf(x); A=s*s+1/(s*s)-2; hi=A/2 if A*A<=16 else (A-mp.sqrt(A*A-16))/2; co=vcoeffs(b,s)
    pts=sorted(set([hi*i/n for i in range(0,n+1)]+[hi*mp.mpf(10)**(-j/8) for j in range(1,200)])); prev=None; ch=[]
    for r in pts:
        sg=mp.sign(mp.polyval(co,r))
        if sg==0: continue
        if prev is not None and sg!=prev[0]: ch.append((float(prev[1]),float(r),float(r*(A-r))))
        prev=(sg,r)
    return ch
t0=time.time()
for n_,p,q in ((2,13,5),(3,21,13),(5,55,21),(6,89,34),(8,233,89)):
    q0=q if q%2 else p-q
    by=riley(p,q0); bw=to_w(by); found=None; t1=time.time()
    for x in XS:
        for nm,b in (('v',by),('w',bw)):
            c200=scan(b,x,200)
            if c200:
                c400=scan(b,x,400); found=(x,nm,len(c200),len(c400),c200[0]); break
        if found: break
        if time.time()-t0>330: break
    print('n=%d  %d/%d (as %d/%d), degree %d: %s   [%.0f s]'%(n_,p,q,p,q0,max(by),('TURN: sign change at x=%s in %s (200 digits: %d changes, 400 digits: %d), first bracket r in (%.6g, %.6g), k ~ %.4g'%(found[0],found[1],found[2],found[3],found[4][0],found[4][1],found[4][2])) if found else 'no sign change on the grid points reached (%d digits)'%200,time.time()-t1),flush=True)
# direct test of the NEVER-TURN-05 band point of 233/89
by=riley(233,89)
for dps in (200,400):
    mp.mp.dps=dps; s=mp.e**mp.mpf('0.8'); co=vcoeffs(by,s); v=mp.mpf('1.1301089220261178')
    print('233/89, x=0.8, sign of the exact Riley polynomial at v(1-1e-4), v(1+1e-4), %d digits: %s %s'%(dps,mp.sign(mp.polyval(co,v*(1-mp.mpf(10)**-4))),mp.sign(mp.polyval(co,v*(1+mp.mpf(10)**-4)))))
