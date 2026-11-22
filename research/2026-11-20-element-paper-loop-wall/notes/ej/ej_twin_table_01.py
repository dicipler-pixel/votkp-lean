# SCRIPT: EJ-TWIN-TABLE-01
# Decode of Elizabeth's "In Progress" page: column = span from the lower prime of one twin pair to the
# upper prime of the next twin pair; "a:b" = last digits of those two primes; tally = primes in the segment.
from sympy import primerange
P=list(primerange(2,2*10**6)); S=set(P)
T=[(p,p+2) for p in P if p+2 in S]
allowed={}
for (a,b),(c,d) in zip(T,T[1:]):
    if a<11: continue
    allowed.setdefault((d-a)%30,set()).add(f'{a%10}:{d%10}')
for r in sorted(allowed): print('span mod 30 =',r,' digit pairs seen below 2e6:',sorted(allowed[r]))
# theory: lower twins (>5) lie in 11,17,29 mod 30; span h = (L'+2)-L, so L' = L+h-2 must be a twin class
for h in [8,14,20,26,32]:
    pairs=sorted(f'{L%10}:{(L+h)%10}' for L in (11,17,29) if (L+h-2)%30 in (11,17,29))
    print('span',h,'(and',h+30,') predicted pairs:',pairs)
