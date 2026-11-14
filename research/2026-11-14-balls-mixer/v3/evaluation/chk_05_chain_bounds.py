# SCRIPT: CHK-05-CHAIN-BOUNDS (does the page literal 1.2527 / 1.3838 come from another sieve bound?)
import numpy as np, math
def sieve(N):
    s=bytearray([1])*(N+1); s[0]=s[1]=0
    for i in range(2,int(N**0.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return s
def sl2(z, ax, sg):
    k=1/(2*math.sqrt(z)); p=(z+1)*k; q=sg*(z-1)*k
    if ax==0: return np.array([[p,q],[q,p]],complex)
    if ax==1: return np.array([[p,-1j*q],[1j*q,p]],complex)
    return np.array([[p+q,0],[0,p-q]],complex)
def turn(M):
    W,S_,Vh=np.linalg.svd(M); U=W@Vh; return 2*math.acos(min(1,abs((U[0,0]+U[1,1]).real)/2))
dig={1:0,7:1,9:2}
for N in (1000, 3125, 20000, 100000, 400000, 1000000, 2000000):
    S=sieve(N+2); TW=[a for a in range(11,N+1) if S[a] and S[a+2]]
    out=[]
    for z in (5,7):
        M=np.eye(2,dtype=complex); w=0; ends=[]
        for a in TW:
            if w%12==0: M=np.eye(2,dtype=complex)
            M=M@sl2(z,dig[a%10],1); w+=1
            if w%12==0: ends.append(turn(M))
        out.append(round(float(np.mean(ends)),4))
    print("N",N,"pairs",len(TW),"window-end mean turn z=5,7:",out)
