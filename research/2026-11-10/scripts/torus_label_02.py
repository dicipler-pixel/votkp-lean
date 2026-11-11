# SCRIPT: TORUS-LABEL-02
# Why this check proves the claim: an arc has two end steps k. A quantity labels arcs completely only if
# (a) the two ends of one arc give the same value and (b) different arcs give different values.
# So among the steps k (1..pq-1, not divisible by p or q) a complete arc label must take exactly
# (p-1)(q-1)/2 distinct values, each hit exactly twice. Count that for k^2 mod pq (the carried-over
# direction) and for k^2 mod 4pq (the normalisation in the Kirk-Klassen / Dubois-Kashaev formula).
# Kill condition (written before the run): a label fails if for any (p,q) its distinct-value count
# differs from the arc count or some value is not hit exactly twice.
from math import gcd
from collections import Counter
bad={1:[],4:[]}; n=0
for p in range(2,12):
    for q in range(p+1,16):
        if gcd(p,q)!=1: continue
        n+=1; ks=[k for k in range(1,p*q) if k%p and k%q]; arcs=(p-1)*(q-1)//2
        for m in (1,4):
            c=Counter((k*k)%(m*p*q) for k in ks)
            ok=(len(c)==arcs and set(c.values())=={2})
            if not ok: bad[m].append((p,q,arcs,len(c)))
print('torus knots tested:',n)
print('k^2 mod pq  fails on',len(bad[1]),'of',n,'; first (p,q,arcs,distinct):',bad[1][:8])
print('k^2 mod 4pq fails on',len(bad[4]),'of',n,'; first:',bad[4][:8])
