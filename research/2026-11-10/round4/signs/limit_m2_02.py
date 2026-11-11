# SCRIPT: LIMIT-M2-02  (same checks as LIMIT-M2-01, default range p <= 101, own result file)
# Q2: the limit values of k = 2 - tr[a,b] on the real slice of a two-bridge knot (Two Trees census 8.8), the division
# by m^2, and the lead d = 2q.
import sys, time, collections, sympy as sp, mpmath as mp
from math import gcd
from sympy.polys.rings import ring
from sympy import ZZ
PMAX=int(sys.argv[1]) if len(sys.argv)>1 else 101
print('''WHY THIS CHECK DECIDES IT
 1. EXACT LIMITS. k = v (t - 2), t = tr(ab) = s^2 + s^-2 - v. k stays finite as s -> infinity only if v ~ kappa/s^2
    (type A) or t - 2 ~ kappa/s^2 (type B). Substituting each into the exact Riley polynomial (integer arithmetic,
    no digits) and taking the leading coefficient in s gives a polynomial P_A(kappa), P_B(kappa) whose roots are ALL
    candidate limits. Each irreducible factor is then matched to 4 sin^2(pi j/d)/m^2 at 60 digits (d <= 240, m <= 12,
    smallest m first). A root of P is a limit of a REAL branch only if the branch is real; part 5 checks samples at
    200 digits against the paper's own method.
 2. THE m^2. Two exact identities are proved with sympy: (i) v and t-2 are the two roots of X^2 + dM X + k = 0
    (dM = 2 - s^2 - s^-2; this is the coordinator's k = -v(v + dM)); (ii) for c = ab or ab^-1,
    tr[a,c^m] - 2 = S_(m-1)(tr c)^2 (tr[a,c] - 2), S the Chebyshev polynomial with S_(m-1)(2) = m.
    Since tr[a,c] = tr[a,b] and tr c -> 2 in both limit types, the limit of 2 - tr[a,c^m] is m^2 kappa.
    PREDICTION (written before the census run, read off p <= 41): for a presentation p/q (q odd) and r = q (type B) or
    r = p - q (type A), if p = 2 r m +- 1 then the nonzero limits are EXACTLY 4 sin^2(pi j/(2r))/m^2, 0 < j < r, j = r mod 2.
 3. d = 2q, d = q, d = p, d = 2p are each counted against every nonzero limit factor of every presentation.
KILL CONDITIONS
 identities: sympy remainder not zero.   two-term prediction: one presentation with p = 2rm +- 1 whose exact nonzero
 limit set differs from the predicted set.   d-candidates: a candidate is a rule only if it holds for every nonzero limit.
 OPPOSITE of the two-term prediction (same kill): types swapped (r = q for type A, r = p - q for type B).
''')
# ---------- identities
s_,v_=sp.symbols('s v')
a=sp.Matrix([[s_,1],[0,1/s_]]); b=sp.Matrix([[s_,0],[-v_,1/s_]])
k=sp.simplify(2-(a*b*a.inv()*b.inv()).trace()); t=sp.simplify((a*b).trace()); dM=2-s_**2-s_**-2
print('IDENTITY (i):  v + (t-2) + dM =',sp.simplify(v_+(t-2)+dM),';  v (t-2) - k =',sp.simplify(v_*(t-2)-k),';  tr(ab^-1) - 2 - v =',sp.simplify((a*b.inv()).trace()-2-v_))
a1,a2,a3,c1,c2,c3=sp.symbols('a1 a2 a3 c1 c2 c3')
A=sp.Matrix([[a1,a2],[a3,(1+a2*a3)/a1]]); C=sp.Matrix([[c1,c2],[c3,(1+c2*c3)/c1]])
def S(n,x):
    p0,p1=sp.Integer(1),x
    if n==0: return p0
    for _ in range(n-1): p0,p1=p1,sp.expand(x*p1-p0)
    return p1
ok=True
for m in range(1,7):
    Cm=C**m; lhs=(A*Cm*A.inv()*Cm.inv()).trace()-2; rhs=S(m-1,C.trace())**2*((A*C*A.inv()*C.inv()).trace()-2)
    z=sp.simplify(sp.together(lhs-rhs)); ok&=(z==0); print('IDENTITY (ii) m=%d: tr[a,c^m]-2 - S_(m-1)(tr c)^2 (tr[a,c]-2) = %s ; S_(m-1)(2) = %s'%(m,z,S(m-1,sp.Integer(2))))
print('identities','HOLD (generic SL2 matrices, m = 1..6)' if ok else 'KILLED')
# ---------- exact limits
R,s,v=ring('s,v',ZZ); K,y,kk=ring('y,k',ZZ); ks=sp.Symbol('k')
def cf(p,q):
    o=[]
    while q: o.append(p//q); p,q=q,p%q
    return o
def eps(p,q): return [(-1)**((i*q)//p) for i in range(1,p)]
def mm(X,Y): return [[X[i][0]*Y[0][j]+X[i][1]*Y[1][j] for j in range(2)] for i in range(2)]
def riley(p,q):
    A=[[s**2,s],[R(0),R(1)]]; Ai=[[R(1),-s],[R(0),s**2]]; B=[[s**2,R(0)],[-v*s,R(1)]]; Bi=[[R(1),R(0)],[v*s,s**2]]
    W=[[R(1),R(0)],[R(0),R(1)]]
    for i,x in enumerate(eps(p,q)): W=mm(W,((B if x>0 else Bi) if i%2==0 else (A if x>0 else Ai)))
    return mm(A,W)[0][1]-mm(W,B)[0][1]
def limits(E):
    terms=list(E.terms()); mA=max(i-2*j for (i,j),c in terms); PA=K(0)
    for (i,j),c in terms:
        if i-2*j==mA: PA+=c*kk**j
    jmax=max(j for (i,j),c in terms); w=1-2*y+(1-kk)*y**2; pw={0:K(1)}
    for j in range(1,jmax+1): pw[j]=pw[j-1]*w
    top=max(i+2*j for (i,j),c in terms); tot=K(0)
    for (i,j),c in terms: tot+=c*y**((top-i-2*j)//2)*pw[j]
    lo=min(m[0] for m in tot.monoms()); PB=K(0)
    for (a_,b_),c in tot.terms():
        if a_==lo: PB+=c*kk**b_
    return PA,PB
mp.mp.dps=60
def ident(h):
    P=sp.Poly(h,ks)
    if P.degree()==1 and P.eval(0)==0: return ('zero',)
    rts=[mp.mpc(r) for r in P.nroots(n=55,maxsteps=400)]
    if any(abs(mp.im(r))>mp.mpf(10)**-40 for r in rts): return ('complex',P.degree())
    rts=[mp.re(r) for r in rts]
    if any(r<=0 for r in rts): return ('real, not all positive',P.degree())
    for m in range(1,13):
        if any(m*m*r>4 for r in rts): continue
        th=[mp.asin(m*mp.sqrt(r)/2)/mp.pi for r in rts]
        for d in range(2,241):
            if abs(float(th[0])*d-round(float(th[0])*d))>1e-9: continue
            if all(abs(x*d-mp.nint(x*d))<mp.mpf(10)**-40 for x in th): return (d,m,tuple(sorted(int(mp.nint(x*d)) for x in th)))
    return ('positive, no clock value',P.degree())
def predicted(r,m):   # set of (d_reduced, m, j_reduced)
    out=set()
    for j in range(1,r):
        if (j-r)%2: continue
        g=gcd(j,2*r); d,jj=2*r//g,j//g
        jj=min(jj,d-jj); out.add((d,m,jj))
    return out
def asset(fl):
    out=set(); extra=[]
    for idn,e in fl:
        if idn[0]=='zero': continue
        if isinstance(idn[0],str): extra.append(idn); continue
        d,m,js=idn
        for j in js:
            g=gcd(j,d); dd,jj=d//g,j//g; jj=min(jj,dd-jj); out.add((dd,m,jj))
        if e>1: extra.append(('multiplicity',e,idn))
    return out,extra
t0=time.time(); rows=[]; cnt=collections.Counter(); kills=[]; anti=collections.Counter(); kinds=collections.Counter(); dc=collections.Counter(); nfac=0
mhist=collections.Counter(); outside=[]
for p in range(3,PMAX+1,2):
    for q in range(1,p,2):
        if gcd(p,q)!=1: continue
        PA,PB=limits(riley(p,q)); F={}
        for nm,P in (('A',PA),('B',PB)):
            F[nm]=[(ident(h),e) for h,e in sp.factor_list(P.as_expr())[1]]
            for idn,e in F[nm]:
                kinds[idn[0] if isinstance(idn[0],str) else 'clock value']+=1
                if not isinstance(idn[0],str):
                    d,m,js=idn; nfac+=1; mhist[m]+=1
                    qi=pow(q,-1,p); reps={q,p-q,qi,p-qi}
                    # a factor's roots are 4 sin^2(pi j/d)/m^2 with the factor's own primitive d; candidates must equal it or be a multiple with all j allowed
                    for name,cands in (('d = 2q (given q)',{2*q}),('d = 2q (any of the 4 forms of q)',{2*x for x in reps}),('d = q (any form)',reps),('d = p',{p}),('d = 2p',{2*p}),
                                       ('d divides 2q (given q)',None),('d divides 2(p-q)',None),('d divides 2q or 2(p-q)',None)):
                        if cands is not None: hit=d in cands
                        elif name.startswith('d divides 2q (g'): hit=(2*q)%d==0
                        elif name.startswith('d divides 2(p'): hit=(2*(p-q))%d==0
                        else: hit=(2*q)%d==0 or (2*(p-q))%d==0
                        dc[(name,hit)]+=1
        rows.append((p,q,F))
        for nm,r in (('B',q),('A',p-q)):
            for sgn in (1,-1):
                if (p-sgn)%(2*r)==0 and (p-sgn)//(2*r)>=1:
                    m=(p-sgn)//(2*r); got,extra=asset(F[nm]); pred=predicted(r,m)
                    okk=(got==pred and not extra); cnt[(nm,m if m<4 else '>=4',okk)]+=1
                    if not okk: kills.append((p,q,nm,r,m,sorted(pred-got)[:3],sorted(got-pred)[:3],extra[:2]))
                    other='A' if nm=='B' else 'B'; g2,e2=asset(F[other]); anti[(g2==pred and not e2)]+=1
        # presentations with a nonzero limit not covered by the two-term rule
        cov={('B',q):any((p-sg)%(2*q)==0 for sg in (1,-1)),('A',p-q):any((p-sg)%(2*(p-q))==0 for sg in (1,-1))}
        for nm,r in (('B',q),('A',p-q)):
            g,e=asset(F[nm])
            if (g or e) and not cov[(nm,r)]: outside.append((p,q,nm,sorted(g)[:6],e[:2]))
print('\npresentations p/q, q odd, p <= %d: %d   (%.0f s)'%(PMAX,len(rows),time.time()-t0))
print('kinds of irreducible factor of the limit polynomials:',dict(kinds))
print('m of the clock-value factors:',dict(sorted(mhist.items())))
print('\nTWO-TERM PREDICTION p = 2 r m +- 1 (type, m, exact match): count')
for key in sorted(cnt,key=str): print('  ',key,cnt[key])
print('   mismatches:',len(kills),kills[:8])
print('OPPOSITE (types swapped) exact matches:',dict(anti))
print('\nd-CANDIDATES over all %d clock-value factors (candidate, holds): count'%nfac)
for key in sorted(dc,key=str): print('   %-40s %-5s %d'%(key[0],key[1],dc[key]))
print('\npresentation/type pairs with nonzero limits NOT covered by the two-term rule: %d ; first 25:'%len(outside))
for o in outside[:25]: print('   %d/%d cf %s type %s  (d, m, j): %s  %s'%(o[0],o[1],cf(o[0],o[1]),o[2],o[3],o[4]))
print('\nFULL TABLE p <= 31 (factor: (d, m, [j...]) ^ multiplicity)')
for p,q,F in rows:
    if p>31: break
    print('  %d/%d cf %s | A: %s | B: %s'%(p,q,str(cf(p,q)).replace(' ',''),' '.join('%s^%d'%(str(i).replace(' ',''),e) for i,e in F['A']) or '-',' '.join('%s^%d'%(str(i).replace(' ',''),e) for i,e in F['B']) or '-'))
import pickle; pickle.dump(rows,open('/home/claude/work/agent_signs/limit_m2_02.pkl','wb'))
