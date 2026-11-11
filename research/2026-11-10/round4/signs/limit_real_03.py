# SCRIPT: LIMIT-REAL-03
# Q2 part 5: are the exact limit values of LIMIT-M2-01 reached by REAL branches?  The paper's own method (KNOT-COMM-ASYM):
# real roots v of the Riley relation at s = e^x, x = 12, 200 digits; k = v (tr(ab) - 2).
print('''WHY: LIMIT-M2-01 gives every candidate limit exactly but cannot tell whether the branch is real. Here the real
branches are found numerically at x = 12 (200 digits) and their k compared with the predicted 4 sin^2(pi j/2r)/m^2.
At x = 12 the limit is approached to about e^-24 ~ 4e-11, so agreement to 8 digits is the test.
KILL: a two-term knot (p = 2rm +- 1) where a predicted value with m >= 2 has no real branch within 1e-8, or a real
branch with 1e-6 < k < 4 that is not a predicted/exact limit value.''')
import mpmath as mp, pickle
from math import gcd
exec(open('/home/claude/work/never_turn_02.py').read().split('rows=[]')[0].replace('MAXC=int(sys.argv[1])','MAXC=0'))
mp.mp.dps=200
rows={(p,q):F for p,q,F in pickle.load(open('/home/claude/work/agent_signs/limit_m2_01.pkl','rb'))}
def exact_vals(p,q):
    out=[]
    for nm in 'AB':
        for idn,e in rows[(p,q)][nm]:
            if not isinstance(idn[0],str):
                d,m,js=idn; out+= [(nm,d,m,j,4*mp.sin(mp.pi*j/d)**2/m**2) for j in js]
    return out
tests=[(17,3),(23,3),(29,5),(27,7),(41,7),(23,17),(35,29),(39,29),(13,5),(25,9),(31,13),(21,13),(47,3),(59,29)]
for p,q in tests:
    s=mp.e**mp.mpf(12); E=riley_coeffs(p,q,s); roots=mp.polyroots(E[::-1],maxsteps=3000,extraprec=1600)
    ks=[]
    for v in roots:
        if abs(mp.im(v))>mp.mpf(10)**-80*max(1,abs(v)): continue
        v=mp.re(v); t=s*s+1/(s*s)-v; ks.append(v*(t-2))
    band=sorted(k for k in ks if mp.mpf(10)**-6<k<4); ex=exact_vals(p,q)
    rep=[]
    for nm,d,m,j,val in ex:
        hit=[k for k in band if abs(k-val)<mp.mpf(10)**-8]; rep.append('%s:4sin^2(%d pi/%d)/%d^2=%s %s'%(nm,j,d,m,mp.nstr(val,8),'REAL x%d'%len(hit) if hit else 'no real branch'))
    stray=[mp.nstr(k,10) for k in band if not any(abs(k-val)<mp.mpf(10)**-8 for *_,val in ex)]
    print('%d/%d cf %s  real roots %d, with k in (1e-6,4): %d'%(p,q,cf(p,q),len(ks),len(band)))
    for r in rep: print('     ',r)
    print('      real branches in the band not at an exact limit value:',stray,flush=True)
