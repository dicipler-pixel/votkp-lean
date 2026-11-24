# SCRIPT: GAPS186-AXIOM-CHECK-01
# Independent check (our own code, not OpenAI's) of the two finite-field inputs of the 186 proof,
# exhaustively over all c (and all A, B) for every prime p up to a cutoff.
# Axiom 1: |Kl3(c;p)| <= 3, Kl3 = (1/p) * sum over x1 x2 x3 = c of e_p(x1+x2+x3).
# Axiom 2: |sum over t != 0,-1 of K2(A/t) K2(B/(t+1))| <= 8 p sqrt(p), K2(c) = sum over u != 0 of e_p(u + c/u),
#          for ALL nonzero A, B, including A = B.
# Why this check means something: a single prime where the measured maximum passes 3 (or 8 p^1.5)
# makes that axiom false as stated. Passing for small p does not prove it for all p, which rests on
# Deligne (Katz Thm 4.1.1) and Fouvry-Kowalski-Michel Prop. 2.
# KILL (written before the run): an axiom is refuted if any tested prime gives a ratio above its bound.
# We also record the largest ratio, to see how close the stated constants are to the truth.
import numpy as np, sys
def primes(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=False
    return [int(x) for x in np.nonzero(s)[0]]
P=int(sys.argv[1]) if len(sys.argv)>1 else 200
w1=w2=0; at1=at2=None
for p in primes(P):
    e=np.exp(2j*np.pi*np.arange(p)/p)
    inv=np.array([pow(int(u),p-2,p) if u else 0 for u in range(p)])
    # K2(c) for all c
    u=np.arange(1,p)
    K2=np.array([e[(u+c*inv[u])%p].sum() for c in range(p)])
    # Kl3(c) = (1/p) sum_{x1,x2 != 0} e(x1+x2+c/(x1 x2))  (x3 determined)
    x=np.arange(1,p); X1,X2=np.meshgrid(x,x,indexing='ij'); s12=(X1+X2)%p; ip=inv[(X1*X2)%p]
    m1=0
    for c in range(1,p):
        v=abs(e[(s12+c*ip)%p].sum())/p; m1=max(m1,v)
    if m1>w1: w1,at1=m1,p
    # Axiom 2: S(A,B) = sum_{t != 0,-1} K2(A/t) K2(B/(t+1)), all A, B
    t=np.array([tt for tt in range(1,p) if tt!=p-1],int)
    if len(t)==0: continue
    it=inv[t]; it1=inv[(t+1)%p]
    Acol=K2[(np.arange(1,p)[:,None]*it[None,:])%p]   # rows A
    Bcol=K2[(np.arange(1,p)[:,None]*it1[None,:])%p]  # rows B
    S=Acol@Bcol.T
    m2=np.abs(S).max()/(p**1.5)
    if m2>w2: w2,at2=m2,p
print('primes up to',P)
print('Axiom 1: max |Kl3| = %.6f at p=%s   (bound 3)  %s'%(w1,at1,'PASS' if w1<=3 else 'KILL'))
print('Axiom 2: max |S|/(p sqrt p) = %.6f at p=%s   (bound 8)  %s'%(w2,at2,'PASS' if w2<=8 else 'KILL'))
