# SCRIPT: RETEST-ALL-01
# Second, independent derivation of the day's claims. Exact arithmetic (fractions / sympy) wherever possible.
# Kill lines, written before the run:
#  R1: the quadrilateral count does not cover rank-2 pairs and rank-1 pairs evenly (then the bound 2 is not proved this way)
#  R2: exact flat maximum is not 3/2 (size 2) or 7/4 (size 3) or 15/8 (size 4)
#  R3: the star's exact ratio is not 5/3
#  R4: hyperbolic star: ratio at leg 40 is not 1.6624 to four places, or end-to-end is not 2*leg - ln(4/3) to 1e-9
#  R5: any of the three loop identities fails symbolically
#  R6: with the published Cheshire states the cat is not wholly in one arm and the grin wholly in the other
import itertools, math
from fractions import Fraction as F
import numpy as np, sympy as sp

def mats(mu):
    return [tuple(tuple((v>>(i*mu+j))&1 for j in range(mu)) for i in range(mu)) for v in range(2**(mu*mu))]
def rank(M):
    rows=[int(''.join(map(str,r)),2) for r in M]; r=0
    for bit in reversed(range(len(M))):
        piv=None
        for k in range(r,len(rows)):
            if rows[k]>>bit&1: piv=k;break
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        for k in range(len(rows)):
            if k!=r and rows[k]>>bit&1: rows[k]^=rows[r]
        r+=1
    return r
def add(A,B): return tuple(tuple(a^b for a,b in zip(ra,rb)) for ra,rb in zip(A,B))

# ---------- R1: counts and the quadrilateral bound at size 2
M2=mats(2); rk={M:rank(M) for M in M2}
n1=sum(1 for M in M2 if rk[M]==1); n2=sum(1 for M in M2 if rk[M]==2)
print('size 2: rank-1 matrices',n1,' rank-2 matrices',n2,' rank-1 pairs',16*n1//2,' rank-2 pairs',16*n2//2)
dec={M:0 for M in M2 if rk[M]==2}; part={E:0 for E in M2 if rk[E]==1}
for E1 in M2:
    for E2 in M2:
        if rk[E1]==1 and rk[E2]==1 and rk[add(E1,E2)]==2:
            dec[add(E1,E2)]+=1; part[E1]+=1
print('R1 ways to write each rank-2 matrix as rank-1 + rank-1:',sorted(set(dec.values())),'  partners per rank-1 matrix:',sorted(set(part.values())))
print('   even cover => (sum of 2 squared diagonals) <= (sum of 4 squared sides) averages to ratio <= 2 in any space with the quadrilateral inequality;')
print('   plain triangle inequality gives only d^2 <= 2a^2+2b^2, ratio <= 4 (reached by the word metric: rank-1 step = 1, rank-2 step = 2).')

# ---------- R2: exact flat maximum by characters
def flat_max(mu):
    Ms=mats(mu); byrank={}
    for M in Ms: byrank.setdefault(rank(M),[]).append(M)
    best=F(0)
    reps={}
    for C in Ms:
        r=rank(C)
        if r and r not in reps: reps[r]=C
    for r,C in reps.items():
        def frac(k):
            L=byrank[k]; odd=sum(1 for M in L if sum(C[i][j]&M[i][j] for i in range(mu) for j in range(mu))&1)
            return F(odd,len(L))
        val=frac(mu)/frac(1); best=max(best,val)
        print('   size',mu,'character of rank',r,': ratio',val)
    return best
for mu,want in ((2,F(3,2)),(3,F(7,4)),(4,F(15,8))):
    b=flat_max(mu); print('R2 size',mu,'flat maximum',b,' expected',want,' formula 2-2^(1-mu) =',2-F(1,2**(mu-1)),' MATCH' if b==want else ' MISMATCH')

# ---------- R3: the star, exact, with three ways of grouping the rank-1 matrices
def colspace(M):
    cols=[(M[0][j],M[1][j]) for j in range(2)]; return next(c for c in cols if c!=(0,0))
def rowspace(M):
    return next(r for r in M if r!=(0,0))
def kernel(M):
    for v in ((1,0),(0,1),(1,1)):
        if all((M[i][0]&v[0])^(M[i][1]&v[1])==0 for i in range(2)): return v
def star_ratio(group,leg=(1,1,1)):
    labels=sorted({group(M) for M in M2 if rk[M]==1}); L=dict(zip(labels,leg))
    def d(A,B):
        a=None if rk[A]!=1 else group(A); b=None if rk[B]!=1 else group(B)
        if a==b: return F(0)
        return F((L[a] if a else 0)+(L[b] if b else 0))
    s1=s2=F(0);c1=c2=0
    for A,B in itertools.combinations(M2,2):
        r=rk[add(A,B)]
        if r==1: s1+=d(A,B)**2;c1+=1
        else: s2+=d(A,B)**2;c2+=1
    return (s2/c2)/(s1/c1)
for nm,g in (('column space',colspace),('row space',rowspace),('kernel',kernel)):
    print('R3 star grouped by',nm,': ratio',star_ratio(g))
print('   unequal legs (1,2,3), column space:',star_ratio(colspace,(1,2,3)),' (1,1,2):',star_ratio(colspace,(1,1,2)))

# ---------- R4: the star in the hyperbolic plane, legs at 120 degrees
def hyp_ratio(Lg):
    cc=math.cosh(Lg)**2+0.5*math.sinh(Lg)**2; dd=math.acosh(cc) if Lg<300 else None
    def d(A,B):
        a=None if rk[A]!=1 else colspace(A); b=None if rk[B]!=1 else colspace(B)
        if a==b: return 0.0
        if a is None or b is None: return Lg
        return dd
    s1=s2=0.0;c1=c2=0
    for A,B in itertools.combinations(M2,2):
        r=rk[add(A,B)]
        if r==1: s1+=d(A,B)**2;c1+=1
        else: s2+=d(A,B)**2;c2+=1
    return (s2/c2)/(s1/c1),dd
for Lg in (0.01,1,2,5,10,20,40):
    r,dd=hyp_ratio(Lg); print('R4 leg %5.2f  ratio %.6f   end-to-end minus (2*leg - ln(4/3)) = %.3e'%(Lg,r,dd-(2*Lg-math.log(4/3))))

# ---------- R5: loop identities, symbolic
Phi,u=sp.symbols('Phi u',real=True)
z=sp.exp(sp.I*Phi); Aw=sp.Rational(1,2)/((1+sp.exp(-sp.I*Phi))/2)   # <f|P1|i>/<f|i>
print('R5a weak value - (1+Gamma)/2 simplifies to:',sp.simplify(Aw-(1+(z-1)/(z+1))/2),';  Gamma - i tan(Phi/2):',sp.simplify(sp.expand_trig(sp.simplify(((z-1)/(z+1)-sp.I*sp.tan(Phi/2)).rewrite(sp.cos)))))
lam=sp.symbols('lam')
for N in (3,4,5,6,7):
    def ringL(sign,flux):
        L=sp.zeros(N,N)
        for k in range(N):
            j=(k+1)%N; ph=sp.exp(sp.I*sp.Rational(flux)*sp.pi/N) if flux else 1
            L[k,k]+=2; L[k,j]+=sign*ph; L[j,k]+=sign*sp.conjugate(ph)
        return sp.expand(sp.simplify(L.charpoly(lam).as_expr()))
    sg=ringL(+1,0); hf=ringL(-1,1); zf=ringL(-1,0)
    print('R5b N=%d signless==half-flux: %s   signless==zero-flux: %s'%(N,sp.simplify(sg-hf)==0,sp.simplify(sg-zf)==0))
for N in (3,4,5):
    B=sp.zeros(2*N,2*N); ph=sp.exp(sp.I*Phi/N)
    for k in range(N):
        B[(k+1)%N,k]=ph; B[N+k,N+(k+1)%N]=sp.conjugate(ph)
    print('R5c N=%d det(I-uB)-(1-2cos(Phi)u^N+u^2N) =',sp.simplify(sp.expand((sp.eye(2*N)-u*B).det())-(1-2*sp.cos(Phi)*u**N+u**(2*N))) if True else None)

# ---------- R6: the published Cheshire states (Aharonov, Popescu, Rohrlich, Skrzypczyk 2013)
H=np.array([1,0],complex); V=np.array([0,1],complex); Lk=np.array([1,0],complex); Rk=np.array([0,1],complex)
pre=np.kron((1j*Lk+Rk)/np.sqrt(2),H)
post=(np.kron(Lk,H)+np.kron(Rk,V))/np.sqrt(2)     # their post-selected state up to arm phases
plus=(H+1j*V)/np.sqrt(2); minus=(H-1j*V)/np.sqrt(2)
sig=np.outer(plus,plus.conj())-np.outer(minus,minus.conj())
PL=np.outer(Lk,Lk.conj()); PR=np.outer(Rk,Rk.conj()); I2=np.eye(2)
ov=np.vdot(post,pre)
for nm,A in (('cat in L',np.kron(PL,I2)),('cat in R',np.kron(PR,I2)),('grin in L',np.kron(PL,sig)),('grin in R',np.kron(PR,sig))):
    print('R6',nm,': weak value',np.round(np.vdot(post,A@pre)/ov,12))
print('   success probability of the post-selection:',round(abs(ov)**2,6))
