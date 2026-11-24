# SCRIPT: BUILDING-CONE-01
# Claim under test: the 2^(mu^2) matrices over the two-element field, with squared distance = rank of the difference,
# sit isometrically inside a nonpositively curved space: the Euclidean cone over the spherical building of the
# general linear group of size 2*mu over the two-element field (matrix a -> its graph, a mu-dimensional subspace).
# Why this run can refute it: (i) if the graph subspaces did not meet in dimension mu - rank(a-b) the angle formula would be wrong;
# (ii) every metric that sits in a nonpositively curved space must pass the weighted four-point inequalities of Sturm and Gromov
#      for every four points and every pair of weights; one violation would prove no such space exists.
# Kill lines, written before the run:
#  K1: dim(graph a meet graph b) differs from mu - rank(a-b) for any pair (mu = 2 all pairs, mu = 3 sampled)
#  K2: apartment angle: cos(theta_k) differs from 1 - 2k/mu, or cone distance^2 differs from rank (cone radius^2 = mu/4)
#  K3: any four of the 16 points (mu = 2) violate any weighted four-point inequality on a 21 x 21 grid of weights
#  K4: same for mu = 3 on 300000 random quadruples of the 512 points
import itertools, random, math
import numpy as np
def rank_bits(rows,ncols):
    rows=list(rows); r=0
    for bit in reversed(range(ncols)):
        p=next((k for k in range(r,len(rows)) if rows[k]>>bit&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for k in range(len(rows)):
            if k!=r and rows[k]>>bit&1: rows[k]^=rows[r]
        r+=1
    return r
def mat_rows(v,mu): return [(v>>(i*mu))&((1<<mu)-1) for i in range(mu)]
def rk(v,mu): return rank_bits(mat_rows(v,mu),mu)
def graph_basis(v,mu):   # rows (e_i | a^T e_i ...) : subspace {(x, a x)}; basis vectors as 2mu-bit ints
    rows=mat_rows(v,mu); out=[]
    for j in range(mu):  # x = e_j ; a x = column j of a
        col=sum(((rows[i]>>j)&1)<<i for i in range(mu))
        out.append((1<<(mu+j))|col)
    return out
def meet_dim(a,b,mu): return 2*mu-rank_bits(graph_basis(a,mu)+graph_basis(b,mu),2*mu)
# K1
bad=0
for a in range(16):
    for b in range(16):
        if meet_dim(a,b,2)!=2-rk(a^b,2): bad+=1
random.seed(5)
for _ in range(20000):
    a,b=random.getrandbits(9),random.getrandbits(9)
    if meet_dim(a,b,3)!=3-rk(a^b,3): bad+=1
print('K1 pairs where the graphs do not meet in dimension mu - rank:',bad)
# K2
w=0
for mu in (2,3,4,5):
    for k in range(mu+1):
        S=set(range(mu)); T=set(range(k,mu+k))   # |S meet T| = mu-k inside 2mu coordinates
        vS=np.array([1.0 if i in S else 0.0 for i in range(2*mu)])-0.5; vT=np.array([1.0 if i in T else 0.0 for i in range(2*mu)])-0.5
        c=vS@vT/(np.linalg.norm(vS)*np.linalg.norm(vT)); R2=mu/4
        d2=2*R2*(1-c); w=max(w,abs(c-(1-2*k/mu)),abs(d2-k))
print('K2 worst error in cos(theta_k) = 1 - 2k/mu and cone distance^2 = k :',w)
# K3 / K4 weighted four-point inequality: for all t,s in [0,1]
# 0 <= (1-t)(1-s) d(x,y)^2 + t(1-s) d(y,z)^2 + t s d(z,w)^2 + (1-t) s d(w,x)^2 - t(1-t) d(x,z)^2 - s(1-s) d(y,w)^2
ts=np.linspace(0,1,21); T,S=np.meshgrid(ts,ts)
def worst(mu,quads):
    m=1e9
    for x,y,z,wq in quads:
        A=rk(x^y,mu);B=rk(y^z,mu);C=rk(z^wq,mu);D=rk(wq^x,mu);E=rk(x^z,mu);F=rk(y^wq,mu)
        val=(1-T)*(1-S)*A+T*(1-S)*B+T*S*C+(1-T)*S*D-T*(1-T)*E-S*(1-S)*F
        m=min(m,val.min())
    return m
m2=worst(2,itertools.product(range(16),repeat=4))
print('K3 size 2: smallest value of the weighted four-point form over all 65536 ordered quadruples x 441 weights:',round(float(m2),12),'(must be >= 0)')
m3=worst(3,((random.getrandbits(9),random.getrandbits(9),random.getrandbits(9),random.getrandbits(9)) for _ in range(300000)))
print('K4 size 3: smallest value over 300000 random quadruples x 441 weights:',round(float(m3),12),'(must be >= 0)')
# the ratio this metric gives
for mu in (2,3):
    n=1<<(mu*mu); s={r:[0,0] for r in range(mu+1)}
    for d in range(1,n):
        r=rk(d,mu); s[r][0]+=r; s[r][1]+=1
    print('size',mu,': ratio of mean squared distance, full rank over rank 1 =',(s[mu][0]/s[mu][1])/(s[1][0]/s[1][1]))
