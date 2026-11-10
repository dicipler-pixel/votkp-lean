# SCRIPT: COLOUR-PEEL-02
# Second setup for COLOUR-PEEL-01, using the paper's own sampler (COLOUR-LEADER-01: M = uniform(0,1)+1e-3, colours uniform(0.01,1)),
# because the first setup found no three-channel stretches at all.
# Question: are the paper's stretching passes (955 of 20,000) the ones that carry the pair toward the white point, as the
# two-channel identity d(phi) = (1/2) sech(tau/2) d(tau) forces for two channels?
# "Toward white" = the summed Hilbert distance of the pair to equal shares falls in the pass.
# KILL: if stretches are no more common among toward-white passes than among away passes (ratio of rates <= 1), the two-channel
#       mechanism does not carry to three channels.  Opposite: count stretches among away passes.
import numpy as np
rng=np.random.default_rng(3)
def hil(x,y): r=np.log(x/y); return r.max(-1)-r.min(-1)
def sch(x,y):
    p=x/x.sum(-1,keepdims=True); q=y/y.sum(-1,keepdims=True)
    return 4*np.arcsin(np.clip(np.linalg.norm(np.sqrt(p)-np.sqrt(q),axis=-1)/2,0,1))
for ch in (2,3):
    N=20000; M=rng.uniform(0,1,(N,ch,ch))+1e-3; x=rng.uniform(.01,1,(N,ch)); y=rng.uniform(.01,1,(N,ch))
    Mx=np.einsum('nij,nj->ni',M,x); My=np.einsum('nij,nj->ni',M,y); one=np.ones(ch)
    st=sch(Mx,My)>sch(x,y)*(1+1e-12); hs=hil(Mx,My)>hil(x,y)*(1+1e-12)
    tw=(hil(Mx,one)+hil(My,one))<(hil(x,one)+hil(y,one))
    print('%d channels: Schrodinger stretched in %d of %d; Hilbert in %d'%(ch,int(st.sum()),N,int(hs.sum())))
    print('   toward white: %d passes, %d stretched (%.2f%%)   away: %d passes, %d stretched (%.2f%%)'%(int(tw.sum()),int((st&tw).sum()),100*(st&tw).sum()/max(tw.sum(),1),int((~tw).sum()),int((st&~tw).sum()),100*(st&~tw).sum()/max((~tw).sum(),1)))
