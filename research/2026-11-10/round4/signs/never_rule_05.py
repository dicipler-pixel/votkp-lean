# SCRIPT: NEVER-RULE-05
# Q3: the lead R4 (R3 extended to longer even blocks), scored against the whole census p <= 75.
import sys, json, glob, itertools
from fractions import Fraction as Fr
sys.path.insert(0,'/home/claude/work/agent_signs')
from riley_exact import cf
print('''R4 (written after NEVER-RULE-03 showed R3 misses exactly 55/21, 71/21, 75/29; so those three are FITTED, not tested):
 non-torus NEVER iff  p/q = a +- 1/E,  a odd >= 3,  E = [e1, ..., e_2n] a continued fraction with EVEN entries, EVEN length,
 the entries pairing up by sign (e1 e2 > 0, e3 e4 > 0, ...; the sign may change only between pairs), e1 > 0,
 and for n = 1 the size clause a > e2.  No size clause is known for n >= 2 (none could be tested below p = 101).
WHY THIS CHECK DECIDES IT: R4 is enumerated for all p <= 75 and compared knot by knot with NEVER-CENSUS-02.
 What is a real test here: R4 must not predict never for any of the 250 turners (false positives), in particular the
 unpaired sign patterns must all turn.   KILL: one false positive, or one never-turner outside R4.
OPPOSITE (same kill): sign patterns that are NOT paired (a sign change inside a pair) predicted never.''')
res={}
for f in sorted(glob.glob('/home/claude/work/agent_signs/never_census_02_p*.json')):
    for r in json.load(open(f)): res[(r['p'],r['q'])]=r['verdict']
T={k for k in res if k[1]>1}; never={k for k in T if res[k]=='NEVER'}; PM=max(p for p,q in T)
def key(p,q):
    q%=p; qi=pow(q,-1,p); c=[q,p-q,qi,p-qi]; return (p,min(z for z in c if z%2==1))
def val(E):
    x=Fr(E[-1])
    for e in reversed(E[:-1]): x=Fr(e)+1/x
    return x
def enum(n,paired,pmax):
    out={}
    mags=[m for m in itertools.product(range(2,40,2),repeat=2*n) if 3*abs(val(list(m)).numerator)-abs(val(list(m)).denominator)<=3*pmax] if n==1 else [m for m in itertools.product((2,4,6,8),repeat=2*n)]
    for m in mags:
        for sg in itertools.product((1,-1),repeat=2*n-1):
            s=(1,)+sg
            ispaired=all(s[2*i]==s[2*i+1] for i in range(n))
            if ispaired!=paired: continue
            E=[a*b for a,b in zip(m,s)]
            try: x=val(E)
            except ZeroDivisionError: continue
            if x<=1: continue
            for a in range(3,pmax,2):
                if n==1 and paired and not a>E[1]: continue
                for pm in (1,-1):
                    z=Fr(a)+pm/x; p,q=z.numerator,z.denominator
                    if p%2==0 or p>pmax or q<=1 or q>=p: continue
                    out.setdefault(key(p,q),(a,'+' if pm>0 else '-',E))
    return out
def score(name,S):
    S={k:v for k,v in S.items() if k in T}; fp=sorted(set(S)-never)
    print('%-34s predicts never for %3d knots (p <= %d): never %3d, turn %3d  %s'%(name,len(S),PM,len(set(S)&never),len(fp),[('%d/%d'%k,S[k]) for k in fp][:4]))
    return S
A=score('R4, n = 1 (= R3)',enum(1,True,PM)); B=score('R4, n = 2',enum(2,True,PM)); C=score('R4, n = 3',enum(3,True,PM))
allp=set(A)|set(B)|set(C)
print('R4 all n: never-turners covered %d of %d; missed %s; false positives %d'%(len(allp&never),len(never),sorted(never-allp),len(allp-never)))
print('  n = 2 instances:',[('%d/%d'%k,B[k]) for k in sorted(B)])
print('\nOPPOSITE: unpaired sign patterns')
score('unpaired, n = 1 (b, c opposite sign)',enum(1,False,PM)); score('unpaired, n = 2',enum(2,False,PM))
print('\nR4 on the golden family [2,1^n,2] (membership only; verdicts from NEVER-GOLDEN-03 and the census):')
for n_,p,q in ((2,13,5),(3,21,8),(5,55,21),(6,89,34),(8,233,89)):
    # 3 - r/q' form: p/q = 3 - 1/E ; even continued fraction of E by nearest-even steps
    x=1/(3-Fr(p,q)); E=[]
    while True:
        e=2*round(x/2) if x.denominator!=1 else int(x)
        if x.denominator==1: E.append(int(x)); break
        fl=int(x//1); e=fl if fl%2==0 else fl+1; E.append(e); x=1/(x-e)
        if len(E)>40: break
    paired=len(E)%2==0 and all(E[2*i]*E[2*i+1]>0 for i in range(len(E)//2)) and all(e%2==0 for e in E)
    print('  n=%d  %d/%d = 3 - 1/%s   even entries %s, length %d, paired %s  -> R4 says %s'%(n_,p,q,E,all(e%2==0 for e in E),len(E),paired,'NEVER' if paired else 'TURN'))
B101=enum(2,True,101)
print('\nR4 n = 2 predictions for 77 <= p <= 101 (untested except by NEVER-RULE-04, capped):',[('%d/%d'%k,B101[k]) for k in sorted(B101) if k[0]>PM])
