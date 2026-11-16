# SCRIPT: NEVER-TURN-04 -- precision check of the family-B break 43/5 at 80 digits: print the band points found.
import mpmath as mp
exec(open('/home/claude/work/never_turn_02.py').read().split('rows=[]')[0].replace('MAXC=int(sys.argv[1])','MAXC=0'))
mp.mp.dps=80
for p,q in ((43,5),(33,5)):
    hits=[]
    for x in XS:
        s=mp.e**x; E=riley_coeffs(p,q,s); roots=mp.polyroots(E[::-1],maxsteps=400,extraprec=400)
        for v in roots:
            if abs(mp.im(v))>mp.mpf(10)**(-40)*max(1,abs(v)): continue
            v=mp.re(v); t=s*s+1/(s*s)-v; k=v*(t-2)
            if v>0 and t>2 and k<4: hits.append((float(x),float(v),float(t),float(k)))
    print(p,q,'band points (x, v, tr(ab), k):',hits[:4],' count',len(hits))
