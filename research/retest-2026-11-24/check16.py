# SCRIPT: CHECK-16MATRIX-01
# Independent check of the 16-matrix retest. Own code, different construction from RETEST-ALL-01:
# matrices as integers 0..2^(mu^2)-1 (bit i*mu+j = entry (i,j)), rank by GF(2) elimination on row bitmasks.
# What each check proves:
#  A counts and the even quadrilateral cover (gives ratio <= 2 in every CAT(0) space at mu=2);
#  B flat maximum over ALL characters (enough, since translation-invariant flat ratios are maximised on a character);
#  C the 5/3 star, and an exhaustive search over all 4^9 placements of rank-1 matrices on a unit three-leg star;
#  D the hyperbolic star from the hyperbolic law of cosines;
#  E the rank-1 character's ratio 2 - 2^(1-mu) at mu = 5 (closed count) and a sampled check of other characters at mu = 5.
# KILL (written before the run): any printed value differing from the retest's
# (3/2, 7/4, 15/8; 5/3 with 12 maximisers; 1.662399 at leg 40; quad cover 6 and 4).
import itertools, math, random
from fractions import Fraction as F
def rank(m,mu):
    rows=[(m>>(i*mu))&((1<<mu)-1) for i in range(mu)]; r=0
    for c in range(mu):
        p=next((k for k in range(r,mu) if rows[k]>>c&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for k in range(mu):
            if k!=r and rows[k]>>c&1: rows[k]^=rows[r]
        r+=1
    return r
# A
mu=2; N=16; rk=[rank(m,2) for m in range(N)]
R1=[m for m in range(N) if rk[m]==1]; R2=[m for m in range(N) if rk[m]==2]
ways={d:sum(1 for a in R1 for b in R1 if a^b==d) for d in R2}
part={a:sum(1 for b in R1 if rk[a^b]==2) for a in R1}
print('A rank1',len(R1),'rank2',len(R2),'pairs',N*len(R1)//2,N*len(R2)//2,'ways',set(ways.values()),'partners',set(part.values()))
# B
def flatmax(mu):
    N=1<<(mu*mu); rk=[rank(m,mu) for m in range(N)]
    full=[m for m in range(N) if rk[m]==mu]; one=[m for m in range(N) if rk[m]==1]
    best=F(0); seen=set()
    for c in range(1,N):          # every nonzero character
        if mu==4 and rk[c] in seen: continue   # mu=4: one representative per rank (GL x GL invariance), cheap
        val=F(sum(bin(c&m).count('1')&1 for m in full),len(full))/F(sum(bin(c&m).count('1')&1 for m in one),len(one))
        best=max(best,val); seen.add(rk[c])
    return best
for mu in (2,3,4): print('B mu',mu,'flat max over characters',flatmax(mu))
# C
mu=2
def col(m):  # nonzero column of a rank-1 2x2 matrix, as an int 1..3
    c0=(m&1)|((m>>2)&1)<<1; c1=((m>>1)&1)|((m>>3)&1)<<1
    return c0 or c1
def ratio(place):   # place: dict rank1 matrix -> 0 (centre) or leg 1..3 (leg end at distance 1)
    pos=lambda m: place.get(m,0)
    def d(a,b):
        pa,pb=pos(a),pos(b)
        return 0 if pa==pb else (1 if 0 in (pa,pb) else 2)
    s1=s2=0;c1=c2=0
    for a,b in itertools.combinations(range(16),2):
        if rk[a^b]==1: s1+=d(a,b)**2;c1+=1
        else: s2+=d(a,b)**2;c2+=1
    return F(s2,c2)/F(s1,c1) if s1 else F(0)
print('C star by column space',ratio({m:col(m) for m in R1}))
best=F(0);cnt=0
for lab in itertools.product(range(4),repeat=9):
    r=ratio(dict(zip(R1,lab)))
    if r>best: best,cnt=r,1
    elif r==best: cnt+=1
print('C exhaustive over 4^9 placements: max',best,'reached by',cnt)
# D
def hyp(L):
    dd=math.acosh(math.cosh(L)**2-math.sinh(L)**2*math.cos(2*math.pi/3))
    place={m:col(m) for m in R1}; pos=lambda m: place.get(m,0)
    def d(a,b):
        pa,pb=pos(a),pos(b); return 0 if pa==pb else (L if 0 in (pa,pb) else dd)
    s1=s2=0;c1=c2=0
    for a,b in itertools.combinations(range(16),2):
        if rk[a^b]==1: s1+=d(a,b)**2;c1+=1
        else: s2+=d(a,b)**2;c2+=1
    return (s2/c2)/(s1/c1)
print('D hyperbolic star leg 0.01 %.6f leg 40 %.6f leg 200 %.6f'%(hyp(0.01),hyp(40),hyp(200)))
# E
mu=5; p1=F(2**(mu-1),2**mu-1)
print('E mu=5 rank-1 character exact ratio',p1/p1**2,' formula',2-F(1,2**(mu-1)))
random.seed(1); full=[]
while len(full)<200000:
    m=random.getrandbits(25)
    if rank(m,5)==5: full.append(m)
one=[]
for u in range(1,32):
    for v in range(1,32):
        m=0
        for i in range(5):
            if u>>i&1: m|=v<<(i*5)
        one.append(m)
for r in range(1,6):
    c=sum(1<<(i*5+i) for i in range(r))
    pf=sum(bin(c&m).count('1')&1 for m in full)/len(full); po=sum(bin(c&m).count('1')&1 for m in one)/len(one)
    print('E mu=5 character of rank',r,'ratio ~ %.4f'%(pf/po))
