# SCRIPT: TWIN-WALL-BITE-01
# Is the wall where the thread bites? Scramble the end-digit arms inside one window of steps
# (a permutation, so the counts are unchanged) and measure the spread ("runout") of the final frame
# turn and of the offset c = d - L/sqrt3 at 1e8, over 200 scrambles per window.
# Windows have the same number of steps:
#   A = from 11 up to the wall crossing (twin start 227),
#   B = the same number of steps right after it,
#   C = the same number of steps starting near 1e5.
# Prediction (written before the run): runout A >> runout C ("polishing after the wall").
# KILL (written before the run): the wall is not special if the turn runout of C is at least
# half that of A.
import numpy as np, math
tw=np.load('../swarm/shapes/twins_1000000000.npy').astype(np.int64); tw=tw[(tw>=11)&(tw<=10**8)]
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
arm={1:0,7:1,9:2}
r=np.log(tw[1:]/tw[:-1]); s=np.array([arm[int(x)%10] for x in tw[1:]]); Ls=math.log(tw[-1]/11)
def B(rr,ss): return math.cosh(rr/2)*np.eye(2)+math.sinh(rr/2)*sg[ss]
def prod_range(a,b,arms):
    M=np.eye(2,dtype=complex)
    for i in range(a,b): M=M@B(r[i],arms[i-a])
    return M
def readout(L):
    M=L@L.conj().T; d=math.acosh(np.trace(M).real/2)
    w,V=np.linalg.eigh(M); H=V@np.diag(np.sqrt(w))@V.conj().T; U=np.linalg.solve(H,L)
    ang=2*math.degrees(math.acos(min(1,abs(np.trace(U).real)/2)))
    return ang, d-Ls/math.sqrt(3)
nA=int(np.searchsorted(tw[1:],227,side='right'))
iC=int(np.searchsorted(tw[1:],100000))
wins={'A before wall':(0,nA),'B just after':(nA,2*nA),'C near 1e5':(iC,iC+nA)}
N=len(r)
true=readout(prod_range(0,N,s))
print('steps per window',nA,' true turn %.4f deg, c %.5f'%true)
rng=np.random.default_rng(3)
res={}
for name,(a,b) in wins.items():
    P=prod_range(0,a,s[:a]); Q=prod_range(b,N,s[b:N])
    out=[]
    for _ in range(200):
        arms=rng.permutation(s[a:b]); out.append(readout(P@prod_range(a,b,arms)@Q))
    out=np.array(out); res[name]=out
    print('%-14s twin starts %d..%d  turn runout (sd) %.4f deg  range %.3f..%.3f   c runout %.5f'%(name,tw[a],tw[b],out[:,0].std(),out[:,0].min(),out[:,0].max(),out[:,1].std()))
ra=res['A before wall'][:,0].std(); rc=res['C near 1e5'][:,0].std()
print('ratio C/A turn runout %.4f ->'%(rc/ra),'KILL' if rc>=0.5*ra else 'PASS (polishing after the wall)')
