# SCRIPT: EJ-TWIN-TALLIES-02
# Tallies of Elizabeth's twin-segment table for every segment below 10 million:
# primes in (upper twin of one pair, lower twin of the next], the seats (numbers coprime to 30 there), mean fill.
from sympy import primerange
import bisect
from math import gcd
P=list(primerange(2,10**7)); S=set(P)
T=[(p,p+2) for p in P if p+2 in S and p>5]
stats={}
for (a,b),(c,d) in zip(T,T[1:]):
    n=bisect.bisect_right(P,c)-bisect.bisect_right(P,b)
    seats=sum(1 for m in range(b+1,c+1) if gcd(m,30)==1)
    st=stats.setdefault(d-a,[0,0,seats,{}]); st[0]+=1; st[1]+=n; st[3][n]=st[3].get(n,0)+1
for s in [8,14,20,26,32,38,44,50,56,62]:
    c,t,seats,h=stats[s]
    print(s,'segments',c,'seats',seats,'mean tally',round(t/c,3),'fill',round(t/c/seats,3),'counts',dict(sorted(h.items())))
