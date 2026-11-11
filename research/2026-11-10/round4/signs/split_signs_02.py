# SCRIPT: SPLIT-SIGNS-02
# Q1 follow-up. SPLIT-SIGNS-01 killed the arithmetic prediction as first written (127 of 137 in the clean stratum;
# all 10 misses have g(zeta6) = +-2). This run tests the repair, and its opposite.
import pickle, collections, sympy as sp
from database_knotinfo import link_list
print('''WHY THIS CHECK DECIDES IT
 Reciprocity needs the parity of v_p(d) at primes p = 2 mod 3, where d is the discriminant of the two levels.
 SPLIT-SIGNS-01 assumed v_p(d) = v_p(g(zeta6)), g = Delta/(t^2-t+1)^2. That holds when the factor of p sits INSIDE the
 two levels. REPAIR (made AFTER seeing the 10 misses, so it is a fit on those and a test only on the rest):
 count the generators of the Alexander module at the prime (2, t^2+t+1): corank of V^T - w V over the field F_4.
 corank 2 -> the 2 sits inside the two levels, use (-1)^(v_2(g)); corank 3 -> it sits in a third summand, use +1.
 RULE: equal sign  iff  chi3(product of the two units of the 3-part of the double cover linking form)
                        * (-1)^(number of odd primes p = 2 mod 3 at odd power in g(zeta6))
                        * (-1)^(v_2(g(zeta6)) if corank_F4 = 2 else 0)   = +1.
 Inputs: Alexander polynomial, V + V^T (double branched cover), V mod 2. The signature function is not used.
KILL: any knot of the clean stratum (3 not dividing g(zeta6)) on the wrong side.
OPPOSITE run under the same kill: the rule with the F_4 correction inverted (corank 3 -> use v_2, corank 2 -> +1).
SECOND SETUP: the same rule on the strata where 3 divides g(zeta6) (no claim made there before the run).
''')
KI={r['name']:r for r in link_list()[1:]}
res=pickle.load(open('/home/claude/work/agent_signs/split_signs_01.pkl','rb'))
def vp(x,p):
    x=abs(int(x)); v=0
    while x%p==0: x//=p; v+=1
    return v
def mul(a,b):
    a0,a1=a&1,a>>1; b0,b1=b&1,b>>1
    return ((a0*b0+a1*b1)%2)|(((a0*b1+a1*b0+a1*b1)%2)<<1)
inv={1:1,2:3,3:2}
def corank4(V):
    n=len(V); M=[[(int(V[j][i])%2)^mul(2,int(V[i][j])%2) for j in range(n)] for i in range(n)]; r=0
    for c in range(n):
        p=next((i for i in range(r,n) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; iv=inv[M[r][c]]; M[r]=[mul(iv,x) for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]:
                f=M[i][c]; M[i]=[x^mul(f,y) for x,y in zip(M[i],M[r])]
        r+=1
    return n-r
for r in res:
    r['c4']=corank4(eval(KI[r['name']]['seifert_matrix'])); r['v2g']=vp(r['gz'],2)
    oddp=len([p for p in r['odd'] if p!=2])
    r['rule']=r['chi3']*(-1)**(oddp+(r['v2g'] if r['c4']==2 else 0))
    r['anti']=r['chi3']*(-1)**(oddp+(r['v2g'] if r['c4']!=2 else 0))
print('F_4 corank against v_2(g(zeta6)):',dict(collections.Counter((r['v2g'],r['c4']) for r in res)))
for nm in ('rule','anti'):
    print('\n%s:'%('REPAIRED RULE' if nm=='rule' else 'OPPOSITE (F_4 correction inverted)'))
    for v in sorted(set(r['v3g'] for r in res)):
        sub=[r for r in res if r['v3g']==v]; c=collections.Counter((r[nm],r['cls']) for r in sub)
        ok=c[(1,'equal')]+c[(-1,'opp')]
        print('   v_3(g(zeta6)) = %d (n = %3d):  rule +1: equal %3d opp %3d | rule -1: equal %3d opp %3d   correct %d of %d'%(v,len(sub),c[(1,'equal')],c[(1,'opp')],c[(-1,'equal')],c[(-1,'opp')],ok,len(sub)))
clean=[r for r in res if r['v3g']==0]
print('\nclean stratum, the knots the repair was NOT fitted on (g(zeta6) odd, or v_2 even): ',
      sum((r['rule']==1)==(r['cls']=='equal') for r in clean if r['v2g']%2==0),'of',sum(1 for r in clean if r['v2g']%2==0))
print('clean stratum, the knots with v_2(g) odd (the repair was read off these): ',
      sum((r['rule']==1)==(r['cls']=='equal') for r in clean if r['v2g']%2==1),'of',sum(1 for r in clean if r['v2g']%2==1),
      ' split by corank:',dict(collections.Counter((r['c4'],r['cls'],r['chi3']) for r in clean if r['v2g']%2==1)))
print('\nfull list of 199: rule applies and is correct on %d; 3 divides g(zeta6) (rule not valid) %d; other factor f %d'%(
      sum((r['rule']==1)==(r['cls']=='equal') for r in clean),sum(1 for r in res if r['v3g']>0),199-len(res)))
