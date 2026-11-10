# SCRIPT: LIMIT-REAL-06  (LIMIT-REAL-05 reached its time cap before 41/7, 47/3, 59/29; same check on those three only)
# Q2 part 5, third setup. LIMIT-REAL-04 (exact coefficients, v-polynomial only) passed its control but still showed
# "no real branch" for simple roots of the type-B limit polynomial (41/7, 47/3, 59/29), which is impossible: a simple
# real root of the leading polynomial continues to a real branch. Cause: polyroots loses the v ~ s^2 cluster.
# Here type-A values are read from the v-polynomial and type-B values from the w-polynomial (w = tr(ab) - 2).
print('''WHY: every exact limit value (LIMIT-M2-01) is compared with the real branches at x = 12, 200 digits, exact
integer coefficients, in the variable where that branch is small (v for type A, w for type B).
PREDICTION (elementary): a limit value that is a SIMPLE root of its limit polynomial is always reached by a real
branch; a repeated root may or may not be.
KILL: a simple-root value with no real branch within 1e-8; or a real branch with 1e-6 < k < 4 away from every exact value.''')
import sys, pickle, time, mpmath as mp
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact_w import *
rows=pickle.load(open('/home/claude/work/agent_signs/limit_m2_01.pkl','rb'))
sel=[(p,q,F) for p,q,F in rows if (p,q) in {(41,7),(47,3),(59,29)}]
t0=time.time(); tally={}; kills=[]; strays=[]
def add(key): tally[key]=tally.get(key,0)+1
for p,q,F in sel:
    if time.time()-t0>400: print('time cap reached before %d/%d'%(p,q)); break
    by=riley(p,q); bw=to_w(by); mp.mp.dps=200; s=mp.e**mp.mpf(12); A=s*s+1/(s*s)-2; line=[]
    allex=[]; found={}
    for nm,b in (('A',by),('B',bw)):
        co=vcoeffs(b,s); roots=mp.polyroots(co,maxsteps=3000+100*len(co),extraprec=3000)
        ks=sorted(mp.re(r)*(A-mp.re(r)) for r in roots if abs(mp.im(r))<mp.mpf(10)**-100*max(1,abs(r)) and 0<mp.re(r)<A/2)
        found[nm]=[k for k in ks if mp.mpf(10)**-6<k<4]
        ex=[]
        for idn,e in F[nm]:
            if not isinstance(idn[0],str):
                d,m,js=idn; ex+=[(d,m,j,e,4*mp.sin(mp.pi*j/d)**2/m**2) for j in js]
        for d,m,j,e,val in ex:
            hit=sum(1 for k in found[nm] if abs(k-val)<mp.mpf(10)**-8)
            add((nm,'simple' if e==1 else 'repeated','real' if hit else 'not real'))
            if e==1 and not hit: kills.append((p,q,nm,d,m,j))
            line.append('%s (%d,%d,%d)^%d:%s'%(nm,d,m,j,e,'real x%d'%hit if hit else 'NOT real'))
        st=[mp.nstr(k,8) for k in found[nm] if not any(abs(k-val)<mp.mpf(10)**-8 for *_,val in ex)]
        if st: strays.append((p,q,nm,st))
    print('%d/%d cf %s : %s'%(p,q,str(cf(p,q)).replace(' ',''),'; '.join(line) or 'no nonzero limit value'),flush=True)
print('\nTALLY (type, root kind, branch): count')
for key in sorted(tally): print('  ',key,tally[key])
print('simple-root values with no real branch (kill list):',kills)
print('real band branches away from every exact value:',strays)
