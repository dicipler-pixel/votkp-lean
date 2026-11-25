# SCRIPT: WELL-READING-01
# Question (Session A, entry A3 NEXT): does putting the gap back in, read from the prime 2, lift the
# 16 matrices of Mat_2(F_2) past the flat ceiling 3/2 toward the tree value 5/3 or the cone value 2?
#
# PLACEMENT (the release's own, Appendix D.1 and Step 7): the parties are the matrices of Mat_mu(F_2);
# D(r)^2 = mean of |a, a+W|^2 over all a and all W of rank r; the limiting price has |a,a'|^2 = rk(a-a').
# THE WELL READING (Dirac Time: K(0) = B B^+ has no gap, the well B D^-1 B^+ has the gap once, the metric
# has it squared). For a pair (a, b) the cross block B is the difference of the integer lifts (entries 0,1),
# X = a - b over Z. Its hidden spectrum is its 2-adic Smith form: X = U diag(2^v1, 2^v2, ...) V with U, V
# invertible over Z_2. Mod 2 only the v_i = 0 entries survive, which is the rank the release sees; the
# entries with v_i >= 1 are the hidden levels. Each level is read over its own gap 2^v_i:
#   gap power 0 (K(0)):  n0 = number of nonzero levels        (rank over Q_2)
#   gap power 1 (well):  n1 = sum 2^(-v_i)
#   gap power 2 (metric): n2 = sum 4^(-v_i)
# Every reading equals rk(a-b) mod 2 when no hidden level is present.
#
# KILL LINE 1 (written in entry A3 before this run): the well reading is flat on the 16 matrices
#   (test: the double-centred Gram matrix -1/2 J d^2 J is positive semidefinite = Euclidean).
# KILL LINE 2 (written now, before the run): if a reading is not flat, it breaks the quadrilateral
#   inequality of the release's Lemma C.4(b), |xv|^2+|yu|^2 <= |xu|^2+|yv|^2+2|xy||uv|, on some
#   quadruple. A reading that breaks it is not a price, and its ratio says nothing about the price question.
# WHY THIS DECIDES IT: every price is pulled back from a CAT(0) space (Proposition C.3), where Lemma C.4(b)
#   holds for all quadruples. A Euclidean reading is capped at 3/2 at size 2 (Session A, RANK-FLATNESS-01).
#   So a reading can only matter if it is non-flat AND passes C.4(b).
import itertools, math
from fractions import Fraction as F
import numpy as np

def v2(n):
    n=abs(n)
    if n==0: return None
    v=0
    while n%2==0: n//=2; v+=1
    return v

def minors_gcd(X,k):
    m=len(X); g=0
    for R in itertools.combinations(range(m),k):
        for C in itertools.combinations(range(m),k):
            M=np.array([[X[i][j] for j in C] for i in R],dtype=object)
            d=int(round(np.linalg.det(np.array(M,dtype=float))))
            g=math.gcd(g,d)
    return g

def snf_vals(X):
    m=len(X); prev=1; out=[]
    for k in range(1,m+1):
        g=minors_gcd(X,k)
        if g==0: break
        out.append(v2(g)-v2(prev)); prev=g
    return out  # valuations of the nonzero elementary divisors

def rk2(X):
    return sum(1 for v in snf_vals([[x%2 for x in r] for r in X]) if v==0) if True else 0

def run(mu, lift):
    n=mu*mu
    mats=[tuple(b) for b in itertools.product((0,1),repeat=n)]
    def M(m): return [[lift(m[i*mu+j]) for j in range(mu)] for i in range(mu)]
    def rkF2(m):
        A=np.array(m,int).reshape(mu,mu)%2; A=A.copy(); r=0
        for c in range(mu):
            p=[i for i in range(r,mu) if A[i,c]]
            if not p: continue
            A[[r,p[0]]]=A[[p[0],r]]
            for i in range(mu):
                if i!=r and A[i,c]: A[i]^=A[r]
            r+=1
        return r
    idx={m:i for i,m in enumerate(mats)}
    N=len(mats); vals={}
    cache={}
    for a in mats:
        for b in mats:
            X=[[M(a)[i][j]-M(b)[i][j] for j in range(mu)] for i in range(mu)]
            key=tuple(map(tuple,X))
            if key not in cache: cache[key]=snf_vals(X)
            vals[(a,b)]=cache[key]
    readings={'K(0) gap^0':lambda vs:F(len(vs)),
              'well gap^1':lambda vs:sum(F(1,2**v) for v in vs),
              'metric gap^2':lambda vs:sum(F(1,4**v) for v in vs)}
    rank={a:{} for a in mats}
    for a in mats:
        for b in mats: rank[a][b]=rkF2(tuple(x^y for x,y in zip(a,b)))
    for name,f in readings.items():
        d2=np.zeros((N,N)); d2F={}
        for a in mats:
            for b in mats:
                q=f(vals[(a,b)]); d2F[(a,b)]=q; d2[idx[a],idx[b]]=float(q)
        assert np.allclose(d2,d2.T)
        D={}
        for r in range(1,mu+1):
            pr=[d2F[(a,b)] for a in mats for b in mats if rank[a][b]==r]
            D[r]=sum(pr)/len(pr)
        J=np.eye(N)-np.ones((N,N))/N; G=-0.5*J@d2@J; emin=np.linalg.eigvalsh(G).min()
        flat=emin>-1e-9
        # control: the release's own limiting price rk(a-a') must give D(r)^2 = r
        d=np.sqrt(d2); viol=0; worst=0.0
        if not flat:
            pts=range(N)
            if N<=16:
                quads=itertools.product(pts,repeat=4)
            else:
                rng=np.random.default_rng(1); quads=(tuple(rng.integers(0,N,4)) for _ in range(400000))
            for x,y,v,u in quads:
                lhs=d2[x,v]+d2[y,u]; rhs=d2[x,u]+d2[y,v]+2*d[x,y]*d[u,v]
                if lhs>rhs+1e-9:
                    viol+=1; worst=max(worst,lhs-rhs)
        rat=' '.join(f'D({r})^2/D(1)^2={D[r]/D[1]} ({float(D[r]/D[1]):.6f})' for r in range(2,mu+1))
        print(f'  {name:13s} D(1)^2={D[1]} ({float(D[1]):.4f})  {rat}')
        print(f'      Gram min eigenvalue {emin:.4e} -> KILL LINE 1 '+('FIRED: flat' if flat else 'did not fire: not flat'))
        if not flat:
            print(f'      quadrilateral C.4(b): {viol} violations, worst excess {worst:.4f} -> KILL LINE 2 '+('FIRED: not a price' if viol else 'did not fire'))
    # control
    pr={r:[rank[a][b] for a in mats for b in mats if rank[a][b]==r] for r in range(1,mu+1)}
    print('  CONTROL release price rk(a-a'+"'"+'):', ' '.join(f'D({r})^2={sum(pr[r])/len(pr[r])}' for r in pr))

for mu in (2,3):
    for lname,lift in (('lift 0,1',lambda x:x),('lift +1,-1',lambda x:1-2*x)):
        print(f'=== mu={mu}, {lname}')
        run(mu,lift)
print('reference at mu=2: flat ceiling 3/2, tree star 5/3, building cone 2; at mu=3 flat ceiling 7/4, cone 3')
