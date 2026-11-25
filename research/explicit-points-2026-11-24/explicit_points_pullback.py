# SCRIPT: EXPLICIT-POINTS-02
# The paper's Definition A.4 says pull-backs of prices are prices: a spectral point on a
# smaller set W of parties gives a price on the 16 matrices along ANY map g: matrices -> W.
# So class (B) is wider than one leg per matrix: matrices may share a leg end, and a leg of
# length 0 is the centre.  d(u,v) = 0 if g(u) = g(v), else theta_g(u) + theta_g(v).
# This is every star: any grouping of the 16 matrices, any leg lengths >= 0.
# (Cuts need no rerun: a pulled-back cut is again a cut, and all cuts were checked: 3/2.)
#
# KILL LINE (written before the run): if any star with free leg lengths gives a ratio
# above 5/3, the claim "explicit points stop at 5/3" failed this way.
# CONTROL (must pass before the search counts): the known star (zero matrix and the six
# rank-2 matrices at the centre, rank-1 matrices on three legs by column space) must
# return exactly 5/3, and the climb must be able to find it from random starts.
from itertools import product
import numpy as np
mats=[tuple(b) for b in product((0,1),repeat=4)]
def rank(m):
    a,b,c,d=m
    if not any(m): return 0
    return 2 if (a*d-b*c)%2 else 1
X=np.array([[rank(tuple(p^q for p,q in zip(x,y))) for y in mats] for x in mats])
A={1:(X==1).astype(float),2:(X==2).astype(float)}; tot={1:16*9.0,2:16*6.0}
def forms(lab,L):
    P=np.zeros((16,L)); P[np.arange(16),lab]=1; Q={}
    for r in (1,2):
        N=P.T@A[r]@P; np.fill_diagonal(N,0)
        Q[r]=(2*N+np.diag(2*N.sum(1)))/tot[r]        # theta^T Q theta = sum over ordered pairs of (theta_g+theta_h)^2 / count = D(r)^2
    return Q
def best_theta(lab,L,rng,starts=4,its=300):
    Q=forms(lab,L); top=0;arg=np.ones(L)
    inits=[np.ones(L)]+[rng.random(L) for s in range(starts)]+[np.eye(L)[g]+1e-3 for g in range(L)]
    for t in inits:
        t=t.copy()
        for it in range(its):
            d=t@Q[1]@t
            if d<1e-12: break
            n=t@Q[2]@t
            t=np.maximum(t+0.2*(2*(Q[2]@t)/d-2*n*(Q[1]@t)/d**2),0)
            if t.max()==0: break
            t/=t.max()
        d=t@Q[1]@t
        if d>1e-12 and (t@Q[2]@t)/d>top: top=(t@Q[2]@t)/d;arg=t.copy()
    return top,arg
rng=np.random.default_rng(7)
# ---- control 1: the known star, unit legs, exact value
def col(m):
    a,b,c,d=m; return (a|b,c|d)                       # column space of a rank-1 matrix: its nonzero column
legs={(1,0):1,(0,1):2,(1,1):3}
known=np.array([legs[col(m)] if rank(m)==1 else 0 for m in mats])
Q=forms(known,4); t=np.array([0,1,1,1.0])
print('CONTROL 1: known star with unit legs gives',(t@Q[2]@t)/(t@Q[1]@t),' (5/3 =',5/3,')')
v,th=best_theta(known,4,rng)
print('CONTROL 1b: same grouping, leg lengths set free: best ratio',round(v,8),' lengths',np.round(th/th.max(),4))
# ---- greedy climb: from a labeling, try every single-matrix move, take the best, repeat
def climb(lab,L):
    cur,th=best_theta(lab,L,rng)
    while True:
        bestv,bestl=cur,None
        for i in range(16):
            for g in range(L):
                if g==lab[i]: continue
                new=lab.copy(); new[i]=g
                v,_=best_theta(new,L,rng,starts=1,its=120)
                if v>bestv+1e-9: bestv,bestl=v,new
        if bestl is None: return cur,lab
        lab,cur=bestl,bestv
overall=0
for L,nstart in ((4,40),(5,25),(6,15),(8,8)):
    vals=[]
    for s in range(nstart):
        v,lab=climb(rng.integers(0,L,16),L); vals.append(round(v,6))
    hits=sum(1 for v in vals if abs(v-5/3)<1e-5)
    print('up to',L,'groups:',nstart,'random starts; largest ratio',max(vals),'; starts ending at 5/3:',hits,'; distinct end values',sorted(set(vals),reverse=True)[:5])
    overall=max(overall,max(vals))
print('largest ratio found over all stars with free leg lengths:',overall,'  tree value 5/3 =',round(5/3,6))
print('KILL LINE fired' if overall>5/3+1e-5 else 'KILL LINE did not fire: no star found above 5/3')
