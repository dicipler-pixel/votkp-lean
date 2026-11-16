# SCRIPT: CHAIN-WHOLE-03
# Next in turn from the equation-file entry: the chain stepped by its TRUE ratios a'/a (the "whole" eye of One Tree, One Ball).
# Each twin pair steps from a to a' by the boost of peel ratio a'/a along the arm of the end digit of a' (1,7,9 -> i,j,k).
# Product M = H U.  Question: does the frame turn U of the whole chain settle to a fixed rotation as the chain grows?
# Why it can: a turn between two steps of rapidity r1, r2 is of size r1 r2 / 2, and r ~ gap/a, so the turns are summable
# if the sum of (gap/a)^2 converges.  Kill: the angle or the axis keeps drifting between 10^5 and 10^7.
# Also printed: distance from the centre against path length ln(a/11), and the same for a no-memory shuffle of the arms.
import numpy as np, math
N=20_000_000
s=np.ones(N+3,bool); s[:2]=False
for i in range(2,int((N+2)**.5)+1):
    if s[i]: s[i*i::i]=False
idx=np.nonzero(s[:-2]&s[2:])[0]; tw=idx[idx>=11]
print('twin pairs to',N,':',len(tw))
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
AX={1:0,7:1,9:2}
def walk(arms,marks):
    M=np.eye(2,dtype=complex); out=[]; mi=0
    for j in range(len(tw)-1):
        z=tw[j+1]/tw[j]; k=1/(2*math.sqrt(z)); M=M@((z+1)*k*np.eye(2)+(z-1)*k*sig[arms[j]])
        if tw[j+1]>=marks[mi]:
            P=M@M.conj().T; tr=np.trace(P).real; H=(P+np.eye(2))/math.sqrt(tr+2)
            U=np.array([[H[1,1],-H[0,1]],[-H[1,0],H[0,0]]])@M
            c=np.trace(U).real/2; v=np.array([(-(U@g).trace().imag)/2 for g in sig])
            if c<0: c,v=-c,-v
            ang=2*math.atan2(np.linalg.norm(v),c); d=math.acosh(max(1.0,tr/2)); L=math.log(tw[j+1]/11)
            out.append((int(tw[j+1]),math.degrees(ang),v/np.linalg.norm(v),d,L)); mi+=1
            if mi==len(marks): break
    return out
marks=[10**3,10**4,10**5,10**6,10**7,N-1000]
arms=np.array([AX[int(a)%10] for a in tw[1:]])
print('REAL CHAIN')
for a,ang,ax,d,L in walk(arms,marks): print('  to %9d  turn %.5f deg  axis (%+.4f %+.4f %+.4f)  distance %.4f  path %.4f  ratio %.4f'%(a,ang,ax[0],ax[1],ax[2],d,L,d/L))
rng=np.random.default_rng(3)
print('SAME RATIOS, ARMS SHUFFLED (three draws) at the last mark')
for t in range(3):
    a,ang,ax,d,L=walk(rng.permutation(arms),marks)[-1]; print('  turn %.5f deg  axis (%+.4f %+.4f %+.4f)  distance %.4f  ratio %.4f'%(ang,ax[0],ax[1],ax[2],d,d/L))
