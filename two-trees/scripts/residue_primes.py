# SCRIPT: RESIDUE_PRIMES
# Step 3(a): for every prime p<=200 and z in {2,4,8}, scale Q_u=2zB_u (integer) and reduce mod p.  Report rank of Q_u mod p and,
# for p | z^2+1, z^2-1, the shape of the time/axis block.  KILL CONDITION for the idea "a residue argument like the odd-divisor one works":
# it needs, for some p, a rank-one (or otherwise ping-pong-able) reduction of the scaled generators.  If every Q_u mod p has rank 4
# (p odd) or if the reduction is monomial/scalar, the residue idea is dead for that p.  det(Q_u)=16 z^4.
from mkgens import boost
import sympy as sp
primes=[p for p in sp.primerange(2,200)]
for z in (2,4,8):
    print("=== z =",z," det(Q_u) =",16*z**4)
    rows=[]
    for p in primes:
        ranks=set()
        for a in (1,2,3):
            Q=sp.Matrix(boost(z,a,1))
            ranks.add(Q.rank(iszerofunc=lambda x: x%p==0) if False else sp.Matrix(Q).applyfunc(lambda x:x%p).rank(iszerofunc=lambda x:x%p==0))
        # proper rank mod p via GF(p) elimination
        def rank_mod(Mx,p):
            A=[[int(Mx[i,j])%p for j in range(4)] for i in range(4)]; r=0
            for c in range(4):
                piv=None
                for i in range(r,4):
                    if A[i][c]%p: piv=i;break
                if piv is None: continue
                A[r],A[piv]=A[piv],A[r]; iv=pow(A[r][c],-1,p)
                A[r]=[x*iv%p for x in A[r]]
                for i in range(4):
                    if i!=r and A[i][c]%p:
                        f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
                r+=1
            return r
        rk=rank_mod(sp.Matrix(boost(z,1,1)),p)
        tag=""
        if (z*z+1)%p==0: tag="p | z^2+1: block [[0,-2],[-2,0]] mod p (monomial, finite image)"
        if (z*z-1)%p==0: tag="p | z^2-1: block 2*I mod p (scalar-like on the block)"
        rows.append((p,rk,tag))
    print(" ranks of Q_u mod p, p<=199:",{p:rk for p,rk,t in rows if rk!=4})
    print(" primes with extra structure:",[(p,t) for p,rk,t in rows if t])
    print(" => rank-one reductions for odd p: none (all odd p have rank 4); only p=2 degenerates (det Q has only the prime 2).")
