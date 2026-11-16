# SCRIPT: NEVER-RULE-03
# Q3: candidate rules for "never turns", scored against the census NEVER-CENSUS-02 (all two-bridge knots p/q, p <= PMAX,
# up to mirror and q <-> 1/q; torus knots p/1 set aside: they never turn by the centre argument of Two Trees Thm 8.7).
import sys, json, glob, pickle, collections, time
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact import cf, eps
from fractions import Fraction as Fr
import sympy as sp
print('''WHY THIS CHECK DECIDES IT
 Each rule is computed from p/q alone (continued fraction, Alexander polynomial, exact limit polynomials of LIMIT-M2-02)
 and compared with the census verdict, which was computed from the Riley relation. A rule is "the rule" only with zero
 misses in both directions on the whole table.
RULES WRITTEN BEFORE THIS RUN (read off p <= 55, so p > 55 and the targeted run NEVER-RULE-04 are the test):
 T1 (one-way): the Alexander polynomial has a real positive root  ->  TURN.  Reason: at s^2 = root the real slice passes
    through a reducible representation (v = 0, k = 0) and v changes sign there, so the band is entered at x = (1/2) ln(root).
 T2 (one-way): a limit polynomial P_A or P_B has a nonzero root of odd multiplicity  ->  TURN (a real branch stays in
    the band as x -> infinity).
 R3 (two-way, non-torus): NEVER  iff  p/q = a +- 1/(b + 1/c) with a odd >= 3, b and c even >= 2, and a > c.
    In ordinary continued fractions: [a, b, c] and [a-1, 1, b-1, c].
 Opposite of R3's last clause, same kill: a < c (in place of a > c) predicts never.
KILL: R3 is killed as "the rule" by one knot on the wrong side; each miss is listed.''')
res={}
for f in sorted(glob.glob('/home/claude/work/agent_signs/never_census_02_p*.json')):
    for r in json.load(open(f)): res[(r['p'],r['q'])]=r
PMAX=max(p for p,q in res); T=[k for k in sorted(res) if k[1]>1]
never={k for k in T if res[k]['verdict']=='NEVER'}
print('\ncensus: p <= %d, non-torus knots %d: TURN %d, NEVER %d'%(PMAX,len(T),len(T)-len(never),len(never)))
print('NEVER list:',[('%d/%d'%k,cf(*k)) for k in sorted(never)])
lim={(p,q):F for p,q,F in pickle.load(open('/home/claude/work/agent_signs/limit_m2_02.pkl','rb'))}
x=sp.Symbol('x')
def alex(p,q):
    e=eps(p,q); ex=[0]
    for z in e: ex.append(ex[-1]+z)
    lo=min(ex); c=collections.Counter()
    for k in range(p): c[ex[k]-lo]+=(-1)**k
    n=max(c); return [c.get(i,0) for i in range(n,-1,-1)]
def rootclasses(p,q):
    co=alex(p,q); g=(len(co)-1)//2; C=[sp.Integer(2),x]
    for k in range(2,g+1): C.append(sp.expand(x*C[-1]-C[-2]))
    hh=co[g]
    for k in range(1,g+1): hh+=co[g-k]*C[k]
    h=sp.Poly(sp.expand(hh),x)
    return g,2*int(h.count_roots(-2,2)),2*int(h.count_roots(2,None)-(1 if h.eval(2)==0 else 0)),2*int(h.count_roots(None,-2))
def key(p,q):
    q%=p; qi=pow(q,-1,p); c=[q,p-q,qi,p-qi]; return (p,min(z for z in c if z%2==1))
def fam3(cond):
    S={}
    for a in range(1,PMAX):
        for b in range(1,PMAX):
            if a*b>PMAX+2: break
            for c in range(1,PMAX):
                if a*(b*c+1)-c>PMAX: break
                if not cond(a,b,c): continue
                for sg in (1,-1):
                    z=Fr(a)+sg/(Fr(b)+Fr(1,c)); p,q=z.numerator,z.denominator
                    if p%2==0 or p>PMAX or q>=p or q==1: continue
                    S[key(p,q)]=(a,'+' if sg>0 else '-',b,c)
    return S
F={}
for k in T:
    p,q=k; g,circ,pos,neg=rootclasses(p,q); c=cf(p,q); L=lim[k]
    odd=sum(1 for nm in 'AB' for idn,e in L[nm] if not isinstance(idn[0],str) and e%2==1)
    F[k]=dict(g=g,circ=circ,pos=pos,neg=neg,sig=sum(eps(p,q)),cf=c,odd=odd,q2=(q*q)%p)
def oneway(name,pred):
    S=[k for k in T if pred(k)]; bad=[k for k in S if k in never]
    print('\n%s: applies to %d knots; TURN %d, NEVER %d %s ; leaves %d knots undecided (%d NEVER, %d TURN)'%(name,len(S),len(S)-len(bad),len(bad),bad[:5],len(T)-len(S),len(never-set(S)),len(T)-len(S)-len(never-set(S))))
    return set(S)
s1=oneway('T1 real positive Alexander root -> TURN',lambda k:F[k]['pos']>0)
s2=oneway('T2 odd-multiplicity nonzero limit -> TURN',lambda k:F[k]['odd']>0)
rest=[k for k in T if k not in s1 and k not in s2]
print('T1 or T2: decide %d of %d knots; undecided %d of which NEVER %d, TURN %d: %s'%(len(T)-len(rest),len(T),len(rest),len(never&set(rest)),len(set(rest)-never),[('%d/%d'%k,F[k]['cf']) for k in rest if k not in never][:30]))
def twoway(name,S):
    S={k:v for k,v in S.items() if k in set(T)}; tp=never&set(S); fp=sorted(set(S)-never); fn=sorted(never-set(S))
    print('\n%s\n    predicts never for %d knots: correct %d, wrong (they turn) %d %s\n    never-turners it misses: %d %s\n    score on all %d knots: %d right, %d wrong'%(name,len(S),len(tp),len(fp),[('%d/%d'%k,S[k]) for k in fp][:8],len(fn),[('%d/%d'%k,cf(*k)) for k in fn][:10],len(T),len(T)-len(fp)-len(fn),len(fp)+len(fn)))
    return S
ev=lambda a,b,c:a%2==1 and a>=3 and b%2==0 and c%2==0
R3=twoway('R3: a odd >= 3, b, c even, a > c',fam3(lambda a,b,c:ev(a,b,c) and a>c))
twoway('R3 opposite: a odd >= 3, b, c even, a < c',fam3(lambda a,b,c:ev(a,b,c) and a<c))
twoway('R3 without the last clause: a odd >= 3, b, c even',fam3(lambda a,b,c:ev(a,b,c)))
twoway('earlier family [a,2,2], a odd',fam3(lambda a,b,c:a%2==1 and a>=3 and b==2 and c==2)|{} if False else {k:v for k,v in fam3(lambda a,b,c:a%2==1 and a>=3 and b==2 and c==2).items() if v[1]=='+'})
twoway('earlier family [a,1,1,2], a even  (= a+1 - 1/(2+1/2))',{k:v for k,v in fam3(lambda a,b,c:a%2==1 and a>=3 and b==2 and c==2).items() if v[1]=='-'})
twoway('earlier family [a,m,2], m even',{k:v for k,v in fam3(lambda a,b,c:a%2==1 and a>=3 and b%2==0 and c==2).items() if v[1]=='+'})
print('R3 by sign and by p range:',dict(collections.Counter((v[1],'p<=55' if k[0]<=55 else 'p>55',k in never) for k,v in R3.items())))
def table(name,fn):
    c=collections.defaultdict(lambda:[0,0])
    for k in T: c[str(fn(k))][0 if k in never else 1]+=1
    mixed=sum(min(a,b) for a,b in c.values())
    print('\n-- %s   (value: NEVER / TURN)'%name); print('   '+' | '.join('%s: %d / %d'%(v,c[v][0],c[v][1]) for v in sorted(c)[:14]))
    print('   best it can do as a rule: %d of %d knots wrong'%(mixed,len(T)))
table('p mod 4',lambda k:k[0]%4); table('p mod 8',lambda k:k[0]%8); table('p prime',lambda k:sp.isprime(k[0]))
table('q^2 = +1 / -1 / other mod p',lambda k:{1:'+1',k[0]-1:'-1'}.get(F[k]['q2'],'other'))
table('continued fraction is a palindrome',lambda k:F[k]['cf']==F[k]['cf'][::-1])
table('last entry of the continued fraction even',lambda k:F[k]['cf'][-1]%2==0)
table('parity pattern of the continued fraction (o/e)',lambda k:''.join('eo'[z%2] for z in F[k]['cf']))
table('length of the continued fraction',lambda k:len(F[k]['cf']))
table('signature = 0',lambda k:F[k]['sig']==0); table('|signature| = 2 genus',lambda k:abs(F[k]['sig'])==2*F[k]['g'])
table('number of Alexander roots on the unit circle = degree (all on the circle)',lambda k:F[k]['circ']==2*F[k]['g'])
table('number of Alexander roots on the unit circle',lambda k:F[k]['circ'])
table('Alexander polynomial has a real positive root',lambda k:F[k]['pos']>0)
table('Alexander polynomial has a real negative root',lambda k:F[k]['neg']>0)
table('genus',lambda k:F[k]['g'])
print('\n"The Riley polynomial has no real root in the turning range" is the DEFINITION of never used by the census (with the\nrange 0 < v < A, v(A - v) < 4 and the grid of x); it cannot be scored against the census as a separate rule.')
