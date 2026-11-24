# SCRIPT: TWIN-THREAD-NOISE-01
# Noise bars for TWIN-THREAD-FORM-01: repeat the W=30 and W=210 and W=30030 models with
# 4 seeds each, and bootstrap the real data in 8 blocks. Rule (written before the run):
# a model "matches" if each real dev*G lies within 2 combined standard errors of the model mean.
import numpy as np, math, sys
def stats(a):
    g=np.diff(a); c=a[1:]%10
    return np.array([g[c==d].sum()/g.sum()-(c==d).mean() for d in (1,7,9)]), g.mean()
real=np.load(sys.argv[1]); real=real[(real>1e8)&(real<=1e9)].astype(np.int64)
blocks=np.array_split(real,8); rb=np.array([stats(b)[0]*stats(b)[1] for b in blocks])
rm=stats(real); rm=rm[0]*rm[1]; rse=rb.std(0,ddof=1)/np.sqrt(8)
print('real dev*G',np.round(rm,3),' se',np.round(rse,3))
N=10**8.5
for P in (5,7,13):
    ps=[p for p in (2,3,5,7,11,13) if p<=P]; W=math.prod(ps)
    n=np.arange(W); cop=np.ones(W,bool)
    for p in ps: cop&=(n%p!=0)
    slots=np.nonzero(cop&np.roll(cop,-2))[0]
    pr=((W/np.prod([p-1 for p in ps]))/math.log(N))**2
    vals=[]
    for seed in range(4):
        rng=np.random.default_rng(100+seed); reps=int(3e6/(len(slots)*pr))+1
        out=[];base=0;ch=max(1,int(4e7//len(slots)))
        while reps>0:
            k=min(ch,reps);pos=(base+np.arange(k)[:,None]*W+slots[None,:]).ravel()
            out.append(pos[rng.random(pos.size)<pr]);base+=k*W;reps-=k
        d,G=stats(np.concatenate(out)+W*1000); vals.append(d*G)
    vals=np.array(vals); m=vals.mean(0); se=vals.std(0,ddof=1)/2
    z=(rm-m)/np.sqrt(se**2+rse**2)
    print('W=%6d model dev*G'%W,np.round(m,3),' se',np.round(se,3),' z',np.round(z,2),' MATCH' if np.all(abs(z)<2) else ' NO')
