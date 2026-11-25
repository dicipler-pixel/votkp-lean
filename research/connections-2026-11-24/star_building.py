# SCRIPT: CONNECT-STAR-BUILDING-01
# Leads L1, L5, L6. Exact counts with fractions.
# KILL LINES (written before the run):
#  K1 the three-leg star, described as "leg = hyperplane through the graph of the zero matrix", must reproduce ratio 5/3
#     exactly and the 7 + 3x3 split; otherwise that geometric description is wrong.
#  K2 if left multiplication by the 6 invertible matrices does NOT permute the legs as Sym(3) on 3 objects (or right
#     multiplication moves legs), the "star = cone over the projective line, image map" statement is refuted.
#  K3 flat maximum must equal 1/P(first coordinate of a nonzero vector is 1) = (2^mu-1)/2^(mu-1) through the count
#     P(a11=1 | full rank)/P(a11=1 | rank 1) at mu = 2, 3; otherwise the half-flux-count reading is refuted.
#  K4 L1: if the minimising two-element-field cochain at k = 5 (constant 5/3) has no count in common with the star's
#     5/3 (numerator/denominator structure), 5/3 in both lists is graded a coincidence.
import itertools, numpy as np
from fractions import Fraction as F
def rank2(M):
    M=[list(r) for r in M]; n=len(M); r=0
    for c in range(n):
        p=next((i for i in range(r,n) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(n):
            if i!=r and M[i][c]: M[i]=[a^b for a,b in zip(M[i],M[r])]
        r+=1
    return r
def mats(mu): return [tuple(tuple(v[i*mu:(i+1)*mu]) for i in range(mu)) for v in itertools.product((0,1),repeat=mu*mu)]
def sub(a,b): return tuple(tuple(x^y for x,y in zip(r,s)) for r,s in zip(a,b))
def mul(a,b):
    n=len(a); return tuple(tuple(sum(a[i][k]&b[k][j] for k in range(n))%2 for j in range(n)) for i in range(n))
M2=mats(2); Z=((0,0),(0,0))
# --- L6: graphs as two-dimensional subspaces of the four-dimensional space
def graph(a): return frozenset((x0,x1,(a[0][0]&x0)^(a[0][1]&x1),(a[1][0]&x0)^(a[1][1]&x1)) for x0 in (0,1) for x1 in (0,1))
vecs=[v for v in itertools.product((0,1),repeat=4) if any(v)]
add=lambda u,v: tuple(a^b for a,b in zip(u,v))
lines=set()
for u,v in itertools.combinations(vecs,2): lines.add(frozenset([(0,0,0,0),u,v,add(u,v)]))
W=frozenset((0,0,a,b) for a in (0,1) for b in (0,1))
meet=lambda A,B: len(A&B)
print('L6 two-dimensional subspaces in all:',len(lines),'; equal to W:',sum(l==W for l in lines),'; meeting W in a point:',sum(meet(l,W)==2 for l in lines),'; missing W (the 16 graphs):',sum(meet(l,W)==1 for l in lines))
G={a:graph(a) for a in M2}; V0=G[Z]
print('L6 graphs meeting the zero graph V0 in: itself',sum(meet(G[a],V0)==4 for a in M2),', a point',sum(meet(G[a],V0)==2 for a in M2),'(rank 1), nothing',sum(meet(G[a],V0)==1 for a in M2),'(invertible)')
def span(A,B): return frozenset(add(u,v) for u in A for v in B)
legs={}
for a in M2:
    if rank2(a)==1: legs.setdefault(span(G[a],V0),[]).append(a)
print('L6 hyperplanes through V0 that hold rank-1 graphs:',len(legs),'; graphs on each:',[len(v) for v in legs.values()],'; each hyperplane meets W in',[len(h&W)-1 for h in legs],'nonzero point(s)')
lab={a:0 for a in M2}
for i,(h,v) in enumerate(legs.items(),1):
    for a in v: lab[a]=i
# dual star: legs by the point of V0 the graph passes through
legsd={}
for a in M2:
    if rank2(a)==1: legsd.setdefault(G[a]&V0,[]).append(a)
labd={a:0 for a in M2}
for i,(h,v) in enumerate(legsd.items(),1):
    for a in v: labd[a]=i
def ratio(d2):
    s1=[d2(a,b) for a in M2 for b in M2 if rank2(sub(a,b))==1]; s2=[d2(a,b) for a in M2 for b in M2 if rank2(sub(a,b))==2]
    return F(sum(s2),len(s2))/F(sum(s1),len(s1)), (sum(s2),len(s2),sum(s1),len(s1))
def tree(lab): return lambda a,b: 0 if lab[a]==lab[b] else (1 if 0 in (lab[a],lab[b]) else 4)
r,c=ratio(tree(lab)); print('K1 star by hyperplanes through V0: ratio',r,' counts (sum, pairs) rank 2:',c[:2],' rank 1:',c[2:], 'HELD' if r==F(5,3) else 'FIRED')
r,c=ratio(tree(labd)); print('   dual star by points on V0: ratio',r)
# product of the two stars (cone over the link of V0 in the building = K_{3,3}): d^2 = s*[hyperplane differs]*... 
for s,t in ((1,0),(1,1),(2,1),(1,2)):
    def d2(a,b,s=s,t=t): return F(s)*tree(lab)(a,b)+F(t)*tree(labd)(a,b)
    print('   product of the two stars, weights',s,t,': ratio',ratio(d2)[0])
# classify pair types in the star for the exact 5/3
from collections import Counter
for k in (1,2):
    cnt=Counter()
    for a in M2:
        for b in M2:
            if rank2(sub(a,b))==k: cnt[tree(lab)(a,b)]+=1
    print('   steps of rank',k,': ordered pairs by squared tree distance',dict(sorted(cnt.items())))
# --- K2 equivariance
inv=[a for a in M2 if rank2(a)==2]
perms_left=set(); right_moves=0
for g in inv:
    perms_left.add(tuple(sorted((lab[a],lab[mul(g,a)]) for a in M2 if lab[a]) ) and tuple(lab[mul(g,legs_v[0])] for legs_v in legs.values()))
    for a in M2:
        if lab[a] and lab[mul(a,g)]!=lab[a]: right_moves+=1
        if lab[a] and len({lab[mul(g,b)] for b in M2 if lab[b]==lab[a]})!=1: print('left action splits a leg')
print('K2 left multiplication: distinct leg permutations',len(perms_left),'(Sym(3) has 6); right multiplication moves a leg in',right_moves,'cases;','HELD' if len(perms_left)==6 and right_moves==0 else 'FIRED')
# --- K3 flat maximum as a count of half-flux edges
for mu in (2,3):
    Ms=mats(mu); rk=[rank2(a) for a in Ms]
    p_full=F(sum(a[0][0] for a,r in zip(Ms,rk) if r==mu),sum(r==mu for r in rk)); p_one=F(sum(a[0][0] for a,r in zip(Ms,rk) if r==1),sum(r==1 for r in rk))
    print('K3 mu =',mu,': P(a11 = 1 | full rank) =',p_full,'; P(a11 = 1 | rank 1) =',p_one,'; quotient',p_full/p_one,'; 2 - 2^(1-mu) =',F(2**mu-1,2**(mu-1)),'; 1/P(first coordinate 1) =',1/F(2**(mu-1),2**mu-1), 'HELD' if p_full/p_one==F(2**mu-1,2**(mu-1)) else 'FIRED')
# --- K4 the two-element-field degree-one constant with its minimisers
def h1(k):
    V=range(k); E=list(itertools.combinations(V,2)); T=list(itertools.combinations(V,3)); idx={e:i for i,e in enumerate(E)}
    cob=np.array(sorted({tuple(g[u]^g[v] for u,v in E) for bits in itertools.product((0,1),repeat=k-1) for g in [(0,)+bits]}))
    best=None; arg=[]
    Tm=np.zeros((len(T),len(E)),dtype=np.int64)
    for i,(u,v,w) in enumerate(T): Tm[i,idx[(u,v)]]=Tm[i,idx[(v,w)]]=Tm[i,idx[(u,w)]]=1
    for f in itertools.product((0,1),repeat=len(E)):
        fa=np.array(f); N=int(((Tm@fa)%2).sum())
        if N==0: continue
        D=int((cob^fa).sum(1).min()); r=F(N,D)
        if best is None or r<best: best=r; arg=[(N,D,sum(f))]
        elif r==best and (N,D,sum(f)) not in arg: arg.append((N,D,sum(f)))
    return best,arg,len(E),len(T)
for k in (4,5,6):
    b,arg,nE,nT=h1(k)
    # normalised form: (N/triangles)/(D/edges)
    print('K4 k =',k,': raw minimum of (unbalanced triangles)/(edge distance to coboundaries) =',b,'; normalised by counts (edges',nE,', triangles',nT,') =',b*F(nE,nT),'; minimisers (N, D, edges used):',sorted(arg)[:6])
