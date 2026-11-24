# SCRIPT: WHAT-BENDS-TURN-01
# Readout: the ball's TURN along the twin chain (eye 1 tree: every edge a boost of rapidity ln z along the arm of the
# twin start's end digit 1,7,9 -> x,y,z). Each consecutive pair of steps composes to boost x Thomas rotation; we compose
# those rotations along the chain and also count total turning.
# Kill, written before the run: if the real chain's readout lies inside the 2.5-97.5% spread of 200 arm-shuffled chains
# (same digit counts, order destroyed), the turn does not read the end-digit order either; option 4 stays failed.
import numpy as np, math
rng=np.random.default_rng(1)
N=5*10**7
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
arm=np.searchsorted([1,7,9],T%10)   # 0,1,2
print('twin starts',len(T),' arm counts',np.bincount(arm))
def boost(u,r):
    B=np.eye(4); c,sh=math.cosh(r),math.sinh(r); B[0,0]=c; B[0,u+1]=B[u+1,0]=sh; B[u+1,u+1]=c; return B
def thomas(u,v,r):
    M=boost(u,r)@boost(v,r)
    # polar split M = Bst R ; R = rotation part from M^T eta M ... use: R = Bst^{-1} M with Bst built from M e0
    g=M[:,0]; gam=g[0]; n=g[1:]/math.sqrt(gam*gam-1) if gam>1 else np.zeros(3)
    rap=math.acosh(gam); Bst=np.eye(4); Bst[0,0]=gam; Bst[0,1:]=Bst[1:,0]=math.sinh(rap)*n
    Bst[1:,1:]=np.eye(3)+(gam-1)*np.outer(n,n)
    R=np.linalg.inv(Bst)@M; return R[1:,1:]
def readout(seq,z):
    r=math.log(z); RT={(a,b):thomas(a,b,r) for a in range(3) for b in range(3)}
    Rtot=np.eye(3); turn=0.0
    for a,b in zip(seq[:-1],seq[1:]):
        Rp=RT[(a,b)]; Rtot=Rtot@Rp
        turn+=math.acos(max(-1,min(1,(np.trace(Rp)-1)/2)))
    net=math.acos(max(-1,min(1,(np.trace(Rtot)-1)/2)))
    return turn,net
for z in (3,5,7):
    seq=arm[:20000]
    t0,n0=readout(seq,z)
    TT=[];NN=[]
    for _ in range(200):
        sh=rng.permutation(seq); t,n=readout(sh,z); TT.append(t); NN.append(n)
    lo,hi=np.percentile(TT,[2.5,97.5]); nlo,nhi=np.percentile(NN,[2.5,97.5])
    print(f'z={z}: per-turn angle i->j = {math.degrees(readout([0,1],z)[0]):.2f} deg')
    print(f'   total turning real {math.degrees(t0):.0f} deg; shuffled 95% [{math.degrees(lo):.0f}, {math.degrees(hi):.0f}]',' -> OUTSIDE (survives)' if not lo<=t0<=hi else ' -> inside (KILL)')
    print(f'   net frame turn real {math.degrees(n0):.1f} deg; shuffled 95% [{math.degrees(nlo):.1f}, {math.degrees(nhi):.1f}]',' -> OUTSIDE' if not nlo<=n0<=nhi else ' -> inside')
