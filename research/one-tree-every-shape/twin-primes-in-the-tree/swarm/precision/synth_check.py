# SCRIPT: TWIN-WALK-SYNTH-01
# Straw man for the 'turn if the tilt dies' readout: is it a near-invariant of the walk, and does the turn really go to it
# when (and only when) the arm tilt dies? Same real gaps r_n (twin starts to 1e8), arms redrawn at random with chosen weights.
# Kill (before run): (a) in the DECAYING-tilt chain, |final turn - readout at the start of the window| > 0.05 deg -> the readout
# does not predict the limit; (b) in the CONSTANT-tilt chain, the readout drifts > 0.05 deg over the window -> not an invariant;
# (d) [added after (a) fired because the 0.06*(8/L)^4 tilt was still alive at 1e8: angle(u,m) = 0.97 deg]
#     FAST-decaying tilt 0.06*(8/L)^10 (dead by 1e7): kill if |turn at 1e8 - readout at 1e6| > 0.05 deg.
# (e) [added after (d) also fired: at 1e8 the heading has not finished relaxing, angle(u,m) = 0.44 deg] each chain is then
#     continued by an exactly balanced tail (palindromic x,y,z,z,y,x blocks, r = 1e-4, 12 units of path; [revised before
#     rerun: the first tail, plain x,y,z cycles over 40 units, was invalid - second-order commutator drift and d ~ 32 overflows
#     double precision in the polar split]) so the tilt is zero and the heading
#     relaxes fully: kill if |turn after the tail - readout at 1e8| > 0.01 deg for any chain.
# (c) in the constant-tilt chain the final turn lands within 0.05 deg of the readout -> readout is not specific to tilt death.
import numpy as np, math
N=10**8
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5].astype(float); del s,P
r=np.log(T[1:]/T[:-1]); Lc=np.log(T[1:]/11)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
m=np.ones(3)/math.sqrt(3)
def read(M):
    M=M/np.sqrt(np.linalg.det(M)); A=M@M.conj().T; tr=A.trace().real; d=math.acosh(tr/2)
    adj=np.array([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]]); U=(adj+np.eye(2))/math.sqrt(tr+2)@M
    c=abs((U[0,0]+U[1,1]).real/2); th=math.degrees(2*math.acos(min(1,c)))
    sd=math.sinh(d); n=np.array([A[0,1].real/sd,-A[0,1].imag/sd,(A[0,0]-A[1,1]).real/(2*sd)])
    R=np.array([[(sig[i]@U@sig[j]@U.conj().T).trace().real/2 for j in range(3)] for i in range(3)])
    u=R.T@n; k=np.cross(m,u); sk=np.linalg.norm(k); al=math.acos(max(-1,min(1,m@u))); k=k/sk
    K=np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]]); Q=np.eye(3)+math.sin(al)*K+(1-math.cos(al))*K@K
    Rp=R@Q; return th, math.degrees(math.acos(max(-1,min(1,(Rp.trace()-1)/2)))), math.degrees(al)
def run(beta_of_L,seed):
    rng=np.random.default_rng(seed); u=rng.random(len(r)); M=np.eye(2,dtype=complex); out=[]
    b=np.array([beta_of_L(L) for L in Lc[::1000]]); bb=np.repeat(b,1000,axis=0)[:len(r)]
    p=1/3+bb; cum=np.cumsum(p,axis=1); arms=(u[:,None]>cum).sum(1)
    marks=[1e5,1e6,1e7,1e8*0.999]; mi=0
    for n_ in range(len(r)):
        h=r[n_]/2; ch,sh=math.cosh(h),math.sinh(h); a=arms[n_]
        B=np.array([[ch,sh],[sh,ch]],complex) if a==0 else (np.array([[ch,-1j*sh],[1j*sh,ch]]) if a==1 else np.diag([math.exp(h),math.exp(-h)]).astype(complex))
        M=M@B
        if mi<len(marks) and T[n_+1]>=marks[mi]: out.append((marks[mi],*read(M))); mi+=1
    h=0.5e-4; ch,sh=math.cosh(h),math.sinh(h)
    Bs=[np.array([[ch,sh],[sh,ch]],complex),np.array([[ch,-1j*sh],[1j*sh,ch]]),np.diag([math.exp(h),math.exp(-h)]).astype(complex)]
    C3=Bs[0]@Bs[1]@Bs[2]@Bs[2]@Bs[1]@Bs[0]; C=np.eye(2,dtype=complex)
    for _ in range(20000): C=C@C3
    out.append(('tail',*read(M@C)))
    return out
dirn=np.array([1,-1,0])/math.sqrt(2)
for name,f in [('DECAYING tilt 0.06*(8/L)^4',lambda L: 0.06*(8/L)**4*dirn),('CONSTANT tilt 0.02',lambda L: 0.02*dirn),('NO tilt',lambda L:0*dirn),('FAST-DECAYING tilt 0.06*(8/L)^10',lambda L: 0.06*(8/L)**10*dirn)]:
    out=run(f,7); print(name)
    for X,th,pr,al in out[:-1]: print('   X=%.0e  turn %.4f  readout %.4f  angle(u,m) %.4f deg'%(X,th,pr,al))
    print('   after balanced tail: turn %.4f  readout %.4f  angle(u,m) %.5f deg ; turn - readout@1e8 = %+.4f'%(out[-1][1],out[-1][2],out[-1][3],out[-1][1]-out[-2][2]))
    print('   final turn - readout@1e6 = %+.4f ;  readout drift 1e6->1e8 = %+.4f'%(out[-2][1]-out[1][2],out[-2][2]-out[1][2]))
