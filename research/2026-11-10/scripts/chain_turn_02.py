# SCRIPT: CHAIN-TURN-02
# The opposite of CHAIN-TURN-01: read the SIGNED turn instead of the unsigned angle.
# For each 12-step window, U = exp(-i (w . sigma)/2); record the component of the rotation vector w along (1,1,1)/sqrt3,
# the axis about which the cyclic order i -> j -> k turns.
# Why this decides it: a hand in the step table (i->j->k preferred) can only reach a signed record (BallJoins J7).
#  (a) against chains with NO memory (same arm frequencies, independent steps): if the real value is outside that band,
#      the hand of the table reaches the frame.
#  (b) against one-step surrogates: if the real value is outside THAT band, there is order beyond one step.
# Kill for (a): real inside the no-memory band. Kill for (b): real inside the one-step band.
import numpy as np, math
rng=np.random.default_rng(11)
N=400000
s=np.ones(N+3,bool); s[:2]=False
for i in range(2,int((N+2)**.5)+1):
    if s[i]: s[i*i::i]=False
tw=[a for a in range(11,N) if s[a] and s[a+2]]
ax=np.array([{1:0,7:1,9:2}[a%10] for a in tw])
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def gens(z):
    k=1/(2*math.sqrt(z)); return [(z+1)*k*np.eye(2)+(z-1)*k*g for g in sig]
def signed(seq,G):
    n=len(seq)//12; tot=0.0
    for w in range(n):
        M=np.eye(2,dtype=complex)
        for a in seq[12*w:12*w+12]: M=M@G[a]
        P=M@M.conj().T; H=(P+np.eye(2))/math.sqrt(np.trace(P).real+2)
        U=np.array([[H[1,1],-H[0,1]],[-H[1,0],H[0,0]]])@M
        c=np.trace(U).real/2; v=np.array([(-(U@g).trace().imag)/2 for g in sig])   # U = c - i v.sigma
        if c<0: c,v=-c,-v
        nv=np.linalg.norm(v); ang=2*math.atan2(nv,c)
        if nv>1e-14: tot+=ang*(v/nv).sum()/math.sqrt(3)
    return tot/n
C=np.zeros((3,3))
for a,b in zip(ax[:-1],ax[1:]): C[a,b]+=1
Pm=C/C.sum(1,keepdims=True); cum=Pm.cumsum(1); f=np.bincount(ax,minlength=3)/len(ax)
def one_step():
    out=np.empty(len(ax),int); out[0]=ax[0]; u=rng.random(len(ax))
    for i in range(1,len(ax)): out[i]=min(2,int(np.searchsorted(cum[out[i-1]],u[i])))
    return out
for z in (5,7):
    G=gens(z); r=signed(ax,G); rr=signed(ax[::-1],G)
    A=[signed(rng.choice(3,len(ax),p=f),G) for _ in range(120)]; B=[signed(one_step(),G) for _ in range(120)]
    a0,a1=np.percentile(A,[2.5,97.5]); b0,b1=np.percentile(B,[2.5,97.5])
    print('ratio',z,'signed turn about (1,1,1): forward %+.4f  reversed %+.4f'%(r,rr))
    print('   (a) no-memory band %+.4f..%+.4f ->'%(a0,a1),'OUTSIDE' if not a0<=r<=a1 else 'INSIDE')
    print('   (b) one-step band  %+.4f..%+.4f ->'%(b0,b1),'OUTSIDE' if not b0<=r<=b1 else 'INSIDE')
