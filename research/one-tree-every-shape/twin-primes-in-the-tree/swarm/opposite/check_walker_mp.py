# SCRIPT: OPPOSITE-WALKER-CHECK-MP-01
# Large-step check at 60 digits (mpmath): 40 steps of r = ln5 (d reaches ~37) along twin end-digit arms. Kill: any |diff| > 1e-9.
import numpy as np, math, mpmath as mp
from owalk import *
mp.mp.dps=60
P=primes_upto(10**6); tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]; arm=np.searchsorted([1,7,9],T[1:]%10)
def bm(i,r):
    B=mp.eye(4); c,s=mp.cosh(r),mp.sinh(r); B[0,0]=c; B[0,i+1]=B[i+1,0]=s; B[i+1,i+1]=c; return B
n_=40; r=mp.log(5); L=mp.eye(4)
for i in range(n_): L=L*bm(int(arm[i]),r)
g=L[0,0]; d=mp.acosh(g); n=[L[j,0]/mp.sinh(d) for j in (1,2,3)]
Bn=mp.eye(4); Bn[0,0]=g
for a in range(3):
    Bn[0,a+1]=Bn[a+1,0]=mp.sinh(d)*n[a]
    for b in range(3): Bn[a+1,b+1]=(1 if a==b else 0)+(g-1)*n[a]*n[b]
R=(Bn**-1)*L
D,N,RR,_=walk(np.full(n_,math.log(5)),arm[:n_],np.eye(3),np.array([n_-1]))
print('d mp %.12f walker %.12f'%(float(d),D[0]))
print('max |n diff|',max(abs(float(n[a])-N[0][a]) for a in range(3)),' max |R diff|',max(abs(float(R[a+1,b+1])-RR[0][a,b]) for a in range(3) for b in range(3)))
