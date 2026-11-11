# SCRIPT: CHAIN-TURN-01
# Rerun of the test printed in the Two Trees, One Scale mixer ("What the merge shows").
# Claim under test: the twin-prime chain, walked through the tree of peel boosts (end digit 1,7,9 -> axis i,j,k),
# puts order into the frame turning beyond what one step remembers of the step before.
# Why this decides it: the frame turn of a window is fixed by the ORDER of its 12 axes. A surrogate chain drawn
# from the real chain's own step-to-step table has the same one-step memory and no more. If the real mean turn
# lies inside the surrogate band, nothing beyond one step is being seen by the turn.
# Kill (for the claim): real mean turn inside the central 95% band of the surrogates, at ratio 5 and at ratio 7,
# forward and reversed.
import numpy as np, math
rng=np.random.default_rng(7)
N=400000
s=np.ones(N+3,bool); s[:2]=False
for i in range(2,int((N+2)**.5)+1):
    if s[i]: s[i*i::i]=False
tw=[a for a in range(11,N) if s[a] and s[a+2]]
ax=np.array([{1:0,7:1,9:2}[a%10] for a in tw])
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def gens(z):
    k=1/(2*math.sqrt(z)); return [ (z+1)*k*np.eye(2)+(z-1)*k*g for g in sig]
def mean_turn(seq,G):
    n=len(seq)//12; tot=0.0
    for w in range(n):
        M=np.eye(2,dtype=complex)
        for a in seq[12*w:12*w+12]: M=M@G[a]
        P=M@M.conj().T; H=(P+np.eye(2))/math.sqrt(np.trace(P).real+2)   # exact square root of P for det 1
        Hi=np.array([[H[1,1],-H[0,1]],[-H[1,0],H[0,0]]]); U=Hi@M
        tot+=2*math.acos(min(1.0,abs(np.trace(U).real)/2))
    return tot/n
C=np.zeros((3,3)); 
for a,b in zip(ax[:-1],ax[1:]): C[a,b]+=1
Pm=C/C.sum(1,keepdims=True)
def surrogate():
    out=np.empty(len(ax),int); out[0]=ax[0]; u=rng.random(len(ax)); cum=Pm.cumsum(1)
    for i in range(1,len(ax)): out[i]=min(2,int(np.searchsorted(cum[out[i-1]],u[i])))
    return out
print('twin pairs',len(tw),' step-to-step table rows:',np.round(Pm,4).tolist())
for z in (5,7):
    G=gens(z); S=[mean_turn(surrogate(),G) for _ in range(120)]
    lo,hi=np.percentile(S,[2.5,97.5])
    for name,seq in (('forward',ax),('reversed',ax[::-1])):
        r=mean_turn(seq,G)
        print('ratio',z,name,'real %.4f  band %.4f-%.4f '%(r,lo,hi),'INSIDE' if lo<=r<=hi else 'OUTSIDE')
