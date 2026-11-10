# SCRIPT: SPLIT-SIGNS-01
# Q1: at a nullity-2 double root of the Alexander polynomial on the unit circle, what decides whether the two levels
# cross with EQUAL sign (signature jumps by 4) or OPPOSITE sign (silent)?
import collections, pickle, sys, numpy as np, sympy as sp
from fractions import Fraction as F
from sympy import QQ
from sympy.polys.matrices import DomainMatrix
from database_knotinfo import link_list
print('''WHY THIS CHECK DECIDES IT
 The label equal/opposite is read from KnotInfo's signature function (jump -+4 or 0 at a nullity-2 double root).
 Each candidate separator is computed from a DIFFERENT column (Alexander polynomials, symmetry, Seifert matrix,
 V + V^T) and cross-tabulated against the label on the full list of 199. A separator is a candidate whose every
 value holds one label only.
 Part A (definition check): the label is recomputed from the Seifert matrix: eigenvalues of H(w)=(1-w)V+(1-w*)V^T
 just before and just after the root. Must agree 199/199 or the list itself is wrong.
 Part B: the simple candidates. Part C: an arithmetic candidate written before the run:
   for the factor f = t^2-t+1 (193 of 199) the two levels form a rank-2 Hermitian form over Q(zeta6); equal sign iff its
   discriminant d > 0. Hilbert reciprocity for the pair (d, -3) says sign(d) = chi3(unit part of d) * prod over primes
   p = 2 mod 3 of (-1)^(v_p(d)).  PREDICTION: |d| is fixed by the cofactor g = Delta/f^2 at zeta6 (so the prime part
   comes from the Alexander polynomial), and the mod-3 part is the linking form of the DOUBLE BRANCHED COVER on its
   3-part (from V + V^T alone). So: label = chi3(3-part linking discriminant) * prod_{p=2 mod 3} (-1)^(v_p(g(zeta6))).
KILL CONDITIONS (written before the run)
 A: any disagreement between the Seifert-matrix label and the KnotInfo label.
 B: a candidate is a separator only if no value of it holds both labels; otherwise it is reported as NOT a separator.
 C: within the clean stratum (3 does not divide g(zeta6)) any knot on the wrong side kills the prediction as a rule.
''')
KI={r['name']:r for r in link_list()[1:]}
t=sp.symbols('t'); rows=[]; other=collections.Counter()
for k in link_list()[1:]:
    sf=k['signature_function']
    if not sf or sf=='[0]': continue
    try: ent=eval(sf)
    except Exception: continue
    if not isinstance(ent,list) or not ent or not isinstance(ent[0],list): continue
    P=sp.Poly(sp.sympify(k['alexander_polynomial'].replace('^','**')),t)
    fac=sp.factor_list(P)[1]
    for e in ent:
        w=complex(sp.exp(sp.pi*sp.I*e[0]).evalf()); hit=[(f,m) for f,m in fac if abs(complex(f.as_expr().subs(t,w).evalf()))<1e-8]
        mult=sum(m for f,m in hit)
        if e[2]==2 and mult>2: other[(mult,e[1][2]-e[1][0])]+=1
        if mult!=2 or e[2]!=2: continue
        l,a,r=e[1]
        rows.append(dict(name=k['name'],th=e[0],l=l,at=a,r=r,f=hit[0][0],P=P,ent=ent,cls='equal' if r!=l else 'opp'))
N=len(rows); print('nullity-2 double roots:',N,dict(collections.Counter(r['cls'] for r in rows)))
print('(nullity-2 roots of multiplicity 3-5, outside this list: (multiplicity, jump) ->',dict(other),')')
def table(title,key,maxrows=40):
    c=collections.defaultdict(lambda:[0,0])
    for r in rows: c[str(key(r))][0 if r['cls']=='equal' else 1]+=1
    mixed=sum(min(a,b) for a,b in c.values()); pure=all(min(a,b)==0 for a,b in c.values())
    print('\n--',title); print('   %-44s equal   opp'%'value')
    for v in sorted(c)[:maxrows]: print('   %-44s %5d %5d'%(v[:44],c[v][0],c[v][1]))
    if len(c)>maxrows: print('   ... %d values in all'%len(c))
    print('   VERDICT:', 'SEPARATES (no mixed value)' if pure and len(c)>1 else ('constant, cannot separate' if len(c)==1 else 'NOT a separator: %d of %d on the minority side of their value'%(mixed,N)))
    return c
# ---------- Part A
print('\n===== PART A: label recomputed from the Seifert matrix')
agree=0; bad=[]
for r in rows:
    V=np.array(eval(KI[r['name']]['seifert_matrix']),float); r['V']=V
    def sig(th):
        w=np.exp(1j*np.pi*th); ev=np.linalg.eigvalsh((1-w)*V+(1-np.conj(w))*V.T); return int((ev>1e-9).sum()-(ev<-1e-9).sum())
    eps=1e-3; s0,s1=sig(r['th']-eps),sig(r['th']+eps); jump=abs(s1-s0)
    w=np.exp(1j*np.pi*r['th']); ev=np.linalg.eigvalsh((1-w)*V+(1-np.conj(w))*V.T); nul=int((abs(ev)<1e-6).sum())
    r['nulV']=nul
    ok=(nul==2) and ((jump==4)==(r['cls']=='equal')) and jump in (0,4)
    agree+=ok
    if not ok: bad.append((r['name'],nul,s0,s1,r['l'],r['r']))
print('agree %d of %d; disagreements: %s'%(agree,N,bad[:10]))
# ---------- Part B
print('\n===== PART B: simple candidates')
def a2mult(r):
    s=(KI[r['name']].get('second_alexander_polynomial') or '').strip()
    if not s: return 'not listed'
    A2=sp.Poly(sp.sympify(s.replace('^','**')),t); m=0
    while sp.rem(A2,sp.Poly(r['f'].as_expr(),t)).is_zero: A2=sp.quo(A2,sp.Poly(r['f'].as_expr(),t)); m+=1
    return 'multiplicity %d'%m
table('root of the second Alexander polynomial, with multiplicity',a2mult)
def order(r):
    for n in range(1,61):
        if sp.rem(sp.Poly(t**n-1,t),sp.Poly(r['f'].as_expr(),t)).is_zero: return 'root of unity, order %d'%n
    return 'not a root of unity: f = %s'%r['f'].as_expr()
table('root of unity and its order',order)
table('factor f',lambda r:r['f'].as_expr())
table('signature just before the root, mod 4',lambda r:r['l']%4)
table('signature just before the root',lambda r:r['l'])
table('signature AT the root minus signature before (definitional: +-2 iff equal)',lambda r:r['at']-r['l'])
table('knot signature (at -1)',lambda r:int(KI[r['name']]['signature']))
table('cofactor g = Delta / f^2 is trivial (Delta = f^2)',lambda r:sp.quo(r['P'],sp.Poly(r['f'].as_expr()**2,t)).degree()==0)
def cof(r):
    g=sp.quo(r['P'],sp.Poly(r['f'].as_expr()**2,t)); n=0
    for h,m in sp.factor_list(g)[1]:
        for z in sp.Poly(h,t).nroots(n=30):
            if abs(abs(complex(z))-1)<1e-12: n+=m
    return n
table('number of unit-circle roots of the cofactor g',cof)
table('alternating',lambda r:KI[r['name']]['alternating'])
table('symmetry type (amphichiral kinds)',lambda r:KI[r['name']]['symmetry_type'])
table('algebraic concordance order',lambda r:KI[r['name']]['algebraic_concordance_order'] or 'not listed')
table('smooth four-genus',lambda r:KI[r['name']]['smooth_four_genus'])
table('fibered',lambda r:KI[r['name']]['fibered'])
table('crossing number',lambda r:KI[r['name']]['crossing_number'])
table('number of walls of the knot',lambda r:len(r['ent']))
table('signature function identically zero away from this root',lambda r:all(e[1][0]==0 and e[1][2]==0 for e in r['ent']))
print('\nconnected sums: every knot in KnotInfo is prime, so "connected sum K#K against K#mirror K" has no instance here.')
# ---------- Part C
print('\n===== PART C: arithmetic candidate for f = t^2 - t + 1 (193 of 199)')
z=sp.Rational(1,2)+sp.sqrt(-3)/2; Kf=QQ.algebraic_field(sp.sqrt(-3))
def v3adic(A):
    # diagonalise the symmetric integer matrix over the 3-adic integers; return list of (valuation, unit mod 3)
    n=len(A); M=[[F(int(x)) for x in row] for row in A]; out=[]
    def val(x):
        if x==0: return 10**6
        v=0; a,b=x.numerator,x.denominator
        while a%3==0: a//=3; v+=1
        while b%3==0: b//=3; v-=1
        return v
    idx=list(range(n))
    while idx:
        best=min(val(M[i][j]) for i in idx for j in idx)
        d=[i for i in idx if val(M[i][i])==best]
        if not d:
            i,j=[(i,j) for i in idx for j in idx if i!=j and val(M[i][j])==best][0]
            for k in idx: M[i][k]+=M[j][k]
            for k in idx: M[k][i]+=M[k][j]
            d=[i]; assert val(M[i][i])==best
        p=d[0]; piv=M[p][p]
        for i in idx:
            if i==p: continue
            c=M[i][p]/piv
            for k in idx: M[i][k]-=c*M[p][k]
            for k in idx: M[k][i]-=c*M[k][p]
        u=piv/F(3)**best; out.append((best,(u.numerator*pow(u.denominator,-1,3))%3)); idx.remove(p)
    return out
chi=lambda u:1 if u%3==1 else -1
res=[]
for r in rows:
    if sp.expand(r['f'].as_expr()-(t**2-t+1))!=0: continue
    Vs=sp.Matrix(eval(KI[r['name']]['seifert_matrix'])); n=Vs.shape[0]
    M=Vs.T-z*Vs
    dm=DomainMatrix([[Kf.from_sympy(sp.nsimplify(x)) for x in M.row(i)] for i in range(n)],(n,n),Kf)
    ns=dm.nullspace().to_Matrix(); assert ns.shape[0]==2
    S=Vs+Vs.T
    G=sp.Matrix(2,2,lambda i,j: sp.expand((ns.row(i).conjugate()*S*ns.row(j).T)[0]))
    d=sp.Rational(sp.nsimplify(sp.expand(G.det())))
    P=r['P']
    if P.eval(1)<0: P=-P
    g=sp.quo(P,sp.Poly((t**2-t+1)**2,t)); gz=sp.nsimplify(sp.expand(g.as_expr().subs(t,z)*z**(-(g.degree()//2)))); assert gz.is_integer
    gz=int(gz)
    odd=[p for p,e in sp.factorint(abs(gz)).items() if p%3==2 and e%2==1]; v3g=sp.factorint(abs(gz)).get(3,0)
    J=v3adic((Vs+Vs.T).tolist()); tors=sorted((e,u) for e,u in J if e>=1)
    chi3=1
    for e,u in tors: chi3*=chi(u)
    r.update(d=d,gz=gz,odd=odd,v3g=v3g,tors=tors,chi3=chi3,pred=chi3*(-1)**len(odd))
    res.append(r)
print('exact discriminant d of the Seifert form V+V^T on the zeta6 eigenspace (basis-dependent up to norms; sign is invariant):')
c=collections.Counter((r['cls'],'d>0' if r['d']>0 else 'd<0') for r in res); print('  ',dict(c),' (equal iff d>0 is the definition, re-checked exactly)')
# is |d| = norm-class of g(zeta)?  compare squarefree parts at primes 2 mod 3
def oddinert(x):
    x=sp.Rational(x); f=collections.Counter()
    for p,e in sp.factorint(abs(x.p)).items(): f[p]+=e
    for p,e in sp.factorint(abs(x.q)).items(): f[p]-=e
    return sorted(p for p,e in f.items() if p%3==2 and e%2)
same=sum(oddinert(r['d'])==sorted(r['odd']) for r in res)
print('primes p = 2 mod 3 at odd power in d agree with those in g(zeta6): %d of %d'%(same,len(res)))
print('\ncontingency: stratum v_3(g(zeta6)), 3-part of the double-cover linking form [(exponent, unit mod 3)], number of odd inert primes of g(zeta6), label')
c=collections.defaultdict(lambda:[0,0])
for r in res: c[(r['v3g'],str(r['tors']),len(r['odd'])%2)][0 if r['cls']=='equal' else 1]+=1
for k in sorted(c): print('   v3(g)=%d  3-part %-28s odd inert primes mod 2 = %d   equal %3d  opp %3d'%(k[0],k[1],k[2],c[k][0],c[k][1]))
print('\nPREDICTION label = chi3(product of 3-part units) * (-1)^(number of odd inert primes), by stratum:')
tot_ok=tot=0
for v in sorted(set(r['v3g'] for r in res)):
    sub=[r for r in res if r['v3g']==v]; c=collections.Counter((r['pred'],r['cls']) for r in sub)
    a=c[(1,'equal')]+c[(-1,'opp')]; b=c[(1,'opp')]+c[(-1,'equal')]
    print('   v3(g)=%d: n=%3d   pred=+1: equal %3d opp %3d | pred=-1: equal %3d opp %3d   -> one fixed sign convention fits %d of %d'%(v,len(sub),c[(1,'equal')],c[(1,'opp')],c[(-1,'equal')],c[(-1,'opp')],max(a,b),len(sub)))
    if v==0: print('      exceptions in the clean stratum:',[(r['name'],r['cls'],r['gz'],r['tors']) for r in sub if (r['pred']==1)!=( (r['cls']=='equal') if a>=b else (r['cls']=='opp'))][:20])
pickle.dump([{k:v for k,v in r.items() if k not in('V','P','f','ent')} for r in res],open('/home/claude/work/agent_signs/split_signs_01.pkl','wb'))
