# SCRIPT: COLOUR-PEEL-03
# Third setup: the paper's sampler AND its luminous weights (Exner: a = 43.33, 32.76, 1), same seed as the paper (1920) is not
# reproducible here because the paper's generator had been advanced by earlier draws, so the count is compared in size, not digit.
# With weights the chromatic share is p_i = a_i x_i / h, so "white" in share space is x proportional to 1/a.
# Question: (1) is the paper's stretch count a property of the weights (unit weights gave 0 of 20,000 in COLOUR-PEEL-02)?
#           (2) do the stretches sit on passes that carry the pair toward share-white, as two channels force?
# KILL: (1) dies if unit weights and Exner weights give comparable counts; (2) dies if the stretch rate among toward-white
#       passes is not higher than among away passes.  Opposite: stretch count among away passes is printed.
import numpy as np
def hil(x,y): r=np.log(x/y); return r.max(-1)-r.min(-1)
def run(a,label,seed):
    rng=np.random.default_rng(seed); N=20000
    M=rng.uniform(0,1,(N,3,3))+1e-3; x=rng.uniform(.01,1,(N,3)); y=rng.uniform(.01,1,(N,3))
    def sch(x,y):
        p=a*x; p=p/p.sum(-1,keepdims=True); q=a*y; q=q/q.sum(-1,keepdims=True)
        return 4*np.arcsin(np.clip(np.linalg.norm(np.sqrt(p)-np.sqrt(q),axis=-1)/2,0,1))
    Mx=np.einsum('nij,nj->ni',M,x); My=np.einsum('nij,nj->ni',M,y); w=1/a
    st=sch(Mx,My)>sch(x,y)*(1+1e-12)
    tw=(hil(Mx,w)+hil(My,w))<(hil(x,w)+hil(y,w))
    print('%-22s stretched %4d of %d | toward share-white: %5d passes, %4d stretched (%.2f%%) | away: %5d passes, %4d stretched (%.2f%%)'%(
        label,int(st.sum()),N,int(tw.sum()),int((st&tw).sum()),100*(st&tw).sum()/max(tw.sum(),1),int((~tw).sum()),int((st&~tw).sum()),100*(st&~tw).sum()/max((~tw).sum(),1)))
for seed in (1,2,3):
    run(np.array([43.33,32.76,1.0]),'Exner weights, seed %d'%seed,seed)
    run(np.ones(3),'unit weights,  seed %d'%seed,seed)
run(np.array([1.0,32.76,43.33]),'Exner reversed, seed 1',1)
run(np.array([10.0,10.0,1.0]),'weights 10,10,1 seed 1',1)
