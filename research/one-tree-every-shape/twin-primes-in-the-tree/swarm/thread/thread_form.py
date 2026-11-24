# SCRIPT: TWIN-THREAD-FORM-01
# Question: which "thread form" (sieve by the small primes up to P) produces the
# gap-weighted end-digit tilt of the real twin chain?
# Model (Granville-type): integers coprime to W = product of primes <= P are prime
# with probability q = (W/phi(W))/ln N, independently. Twin slots (n, n+2 both coprime
# to W) are disjoint, so twins = independent Bernoulli(q^2) on the slots.
# Measure: dev_j = (gap-weighted share of end digit j) - (count share of j), times mean gap G.
# Real reference: twin starts in (1e8, 1e9].
# KILL (written before the run): the thread-form explanation fails if NO W in the list
# reproduces all three signs of the real dev*G AND each magnitude within 10%.
import numpy as np, math, sys
def stats(a):
    g=np.diff(a); c=a[1:]%10
    out=[]
    for d in (1,7,9):
        m=(c==d); out.append(g[m].sum()/g.sum()-m.mean())
    return np.array(out), g.mean()
real=np.load(sys.argv[1]); real=real[(real>1e8)&(real<=1e9)]
dr,Gr=stats(real.astype(np.int64))
print('real 1e8-1e9  twins',len(real),' mean gap %.1f'%Gr,' dev*G (1,7,9) =',np.round(dr*Gr,3))
N=10**8.5; rng=np.random.default_rng(7)
for P in (5,7,11,13,17,19):
    ps=[p for p in (2,3,5,7,11,13,17,19) if p<=P]; W=math.prod(ps)
    n=np.arange(W); cop=np.ones(W,bool)
    for p in ps: cop&=(n%p!=0)
    slots=np.nonzero(cop & np.roll(cop,-2))[0]
    q=(W/np.prod([p-1 for p in ps]))/math.log(N); pr=q*q
    target=3_000_000; per=len(slots)*pr; reps=int(target/per)+1
    found=[]; base=0; chunk=max(1,int(4e7//len(slots)))
    while reps>0:
        k=min(chunk,reps); pos=(base+np.arange(k)[:,None]*W+slots[None,:]).ravel()
        found.append(pos[rng.random(pos.size)<pr]); base+=k*W; reps-=k
    a=np.concatenate(found)+W*1000  # shift so end digits are unaffected by small values
    d,G=stats(a)
    print('P<=%2d W=%8d slots/period %6d  twins %d  mean gap %.1f  dev*G (1,7,9) ='%(P,W,len(slots),len(a),G),np.round(d*G,3))
