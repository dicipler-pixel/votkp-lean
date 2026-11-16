# SCRIPT: NEVER-TURN-05 -- precision recheck of the golden family D (89/34 at 120 digits, 233/89 at 200 digits) and of 21/8.
import mpmath as mp, sys
exec(open('/home/claude/work/never_turn_02.py').read().split('rows=[]')[0].replace('MAXC=int(sys.argv[1])','MAXC=0'))
for p,q,dps in ((21,13,80),(89,34,120),(233,89,200)):
    mp.mp.dps=dps; hits=[]
    for x in [mp.mpf(i)/10 for i in (2,4,6,8,10,12,15,20,30)]:
        s=mp.e**x; E=riley_coeffs(p,q,s)
        try: roots=mp.polyroots(E[::-1],maxsteps=600,extraprec=2*dps)
        except Exception as e: print('  polyroots failed at x',float(x)); continue
        for v in roots:
            if abs(mp.im(v))>mp.mpf(10)**(-dps//2)*max(1,abs(v)): continue
            v=mp.re(v); t=s*s+1/(s*s)-v; k=v*(t-2)
            if v>0 and t>2 and k<4: hits.append((float(x),float(v),float(k)))
    print(p,q,'digits',dps,'band points',len(hits),hits[:3]); sys.stdout.flush()
