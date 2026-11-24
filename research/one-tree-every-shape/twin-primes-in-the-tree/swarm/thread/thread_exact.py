# SCRIPT: TWIN-THREAD-EXACT-01
# The screw model computed exactly (no random runs).
# Thread cut by primes <= P: slots = n with n, n+2 both coprime to W = prod(p <= P).
# Each slot is a twin start with probability p_slot = (W/phi(W) / ln N)^2, independently.
# The gap ending at slot s is pos(s) - pos(s-k) with probability p_slot (1-p_slot)^(k-1).
# So the gap-weighted share of each end digit is exact: share_j = sum over j-slots of E[gap|s] / sum over all slots.
# Count shares are exactly 1/3 each (the Chinese remainder theorem gives equal slot counts per class).
# Real reference: dev_j x G per decade, from the twin starts cached to 1e9, with 8-block standard errors.
# KILL (written before the run): the screw explains the tilt only if, for the deepest cut,
# digits 1 and 7 both lie within 2 standard errors of the real value in EVERY decade 1e5..1e9.
import numpy as np, math, sys
def real_dev(b):
    g=np.diff(b); c=b[1:]%10
    return np.array([g[c==d].sum()/g.sum()-(c==d).mean() for d in (1,7,9)])*g.mean()
a=np.load(sys.argv[1]).astype(np.int64)
decs=((1e5,1e6),(1e6,1e7),(1e7,1e8),(1e8,1e9))
R={}
for lo,hi in decs:
    b=a[(a>lo)&(a<=hi)]; m=real_dev(b)
    bl=np.array([real_dev(x) for x in np.array_split(b,8)]); se=bl.std(0,ddof=1)/np.sqrt(8)
    R[(lo,hi)]=(m,se)
    print('REAL %.0e-%.0e dev*G (1,7,9) %s  se %s'%(lo,hi,np.round(m,3),np.round(se,3)))
def model(P,N):
    ps=[p for p in (2,3,5,7,11,13,17,19) if p<=P]; W=math.prod(ps)
    n=np.arange(W); cop=np.ones(W,bool)
    for p in ps: cop&=(n%p!=0)
    s=np.nonzero(cop&np.roll(cop,-2))[0]; M=len(s)
    q=(W/np.prod([p-1 for p in ps]))/math.log(N); pr=q*q
    K=int(40/pr)+1
    Eg=np.zeros(M); w=pr
    for k in range(1,K+1):
        idx=np.arange(M)-k; per=np.floor_divide(idx,M); prev=s[idx%M]+per*W
        Eg+=(s-prev)*w; w*=(1-pr)
    G=Eg.mean(); cls=s%10
    return np.array([(Eg[cls==d].sum()/Eg.sum())-1/3 for d in (1,7,9)])*G, G, M
for P in (5,7,11,13,17,19):
    line=[]; ok=True
    for lo,hi in decs:
        N=math.sqrt(lo*hi); d,G,M=model(P,N); m,se=R[(lo,hi)]
        z=(m-d)/se; ok&= bool(abs(z[0])<2 and abs(z[1])<2)
        line.append('%s z%s'%(np.round(d,3),np.round(z[:2],1)))
    print('P<=%2d slots %6d | '%(P,M)+' | '.join(line)+('  ALL-DECADE MATCH' if ok else ''))
