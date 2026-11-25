# SCRIPT: EXPLICIT-POINTS-01
# Question: what ratio D(2)^2 / D(1)^2 does each EXPLICIT spectral point give on the
# 16 matrices Mat_2(F_2)?  (D(r)^2 = mean squared distance over all pairs a, a+W with rank W = r.)
#
# KILL LINE (written before the run): if any explicit point gives a ratio above 5/3,
# the claim "explicit points stop at the tree value 5/3" failed this way.
#
# The explicit points and the metric each one puts on the parties:
#  (A) rank of a flattening across a split S | rest.  A wire of dimension q between u and v
#      flattens to the q x q identity when S separates u from v (rank q) and to a single
#      vector when it does not (rank 1).  So d(u,v) = 1 if S separates u,v, else 0: a cut.
#  (B) quantum functional with weights theta on the single-party splits (proved universal
#      over the complex numbers, Christandl-Vrana-Zuiddam Corollary 3.31).  On a wire only the
#      two splits {u} and {v} separate its ends, so d(u,v) = theta_u + theta_v: a star with
#      one leg per party, leg lengths theta >= 0.
#  (B') Strassen support functionals: same weights on single-party splits, same metric on wires.
from fractions import Fraction as F
from itertools import product
import numpy as np

mats=[tuple(b) for b in product((0,1),repeat=4)]            # (a,b,c,d) = [[a,b],[c,d]]
idx={m:i for i,m in enumerate(mats)}
def rank(m):
    a,b,c,d=m
    if not any(m): return 0
    return 2 if (a*d-b*c)%2 else 1
def add(x,y): return tuple(p^q for p,q in zip(x,y))
R={1:[m for m in mats if rank(m)==1], 2:[m for m in mats if rank(m)==2]}
print('rank-1 matrices:',len(R[1]),' rank-2 matrices:',len(R[2]))
pairs={r:[(idx[a],idx[add(a,W)]) for a in mats for W in R[r]] for r in (1,2)}   # ordered pairs

# ---------- (A) every cut, exact
best=F(0); hist={}; arg=[]
for S in range(1,2**15):                                     # matrix 15 fixed outside S: each split once
    inS=[(S>>i)&1 for i in range(16)]
    s1=sum(1 for i,j in pairs[1] if inS[i]!=inS[j]); s2=sum(1 for i,j in pairs[2] if inS[i]!=inS[j])
    r=F(s2,len(pairs[2]))/F(s1,len(pairs[1]))
    hist[r]=hist.get(r,0)+1
    if r>best: best=r; arg=[S]
    elif r==best: arg.append(S)
print('(A) cuts: splits checked',2**15-1,' largest ratio',best,'=',float(best),' attained by',len(arg),'splits')
print('    five largest ratios and how many splits give each:',[(str(k),hist[k]) for k in sorted(hist,reverse=True)[:5]])
S=arg[0]; side=[mats[i] for i in range(16) if (S>>i)&1]
print('    one best split, the side of size',len(side),':',side)
print('    sizes of the smaller side among best splits:',sorted(set(min(bin(s).count('1'),16-bin(s).count('1')) for s in arg)))

# ---------- (B) one leg per party: d = theta_u + theta_v
def quad(r):
    Q=np.zeros((16,16))
    for i,j in pairs[r]:
        Q[i,i]+=1;Q[j,j]+=1;Q[i,j]+=1;Q[j,i]+=1
    return Q/len(pairs[r])
Q1,Q2=quad(1),quad(2)
# upper bound with the sign condition dropped: largest generalized eigenvalue of (Q2,Q1)
w=np.linalg.eigvals(np.linalg.solve(Q1,Q2)).real
print('(B) star with one leg per party')
print('    bound with theta allowed any sign (generalized eigenvalues):',sorted(set(np.round(w,10)),reverse=True))
# exact search over all 0/1 leg patterns
bestB=F(0)
for T in range(1,2**16):
    t=[(T>>i)&1 for i in range(16)]
    n1=sum((t[i]+t[j])**2 for i,j in pairs[1]); n2=sum((t[i]+t[j])**2 for i,j in pairs[2])
    r=F(n2,len(pairs[2]))/F(n1,len(pairs[1]))
    if r>bestB: bestB=r; argB=T
print('    largest ratio over all 65535 patterns of legs of length 0 or 1:',bestB,'=',float(bestB),
      ' legs switched on:',[mats[i] for i in range(16) if (argB>>i)&1])
# numeric ascent over theta >= 0
rng=np.random.default_rng(1); top=0
for trial in range(400):
    t=rng.random(16)**3
    for it in range(3000):
        n,d=t@Q2@t,t@Q1@t
        g=2*(Q2@t)/d-2*n*(Q1@t)/d**2
        t=np.maximum(t+0.05*g,0); t/=t.sum()
    top=max(top,(t@Q2@t)/(t@Q1@t))
print('    largest ratio from 400 random starts, theta >= 0 free:',round(top,10))
print('TREE VALUE 5/3 =',5/3)
print('KILL LINE fired' if max(float(best),float(bestB),top)>5/3+1e-9 else 'KILL LINE did not fire: no explicit point is above 5/3')
