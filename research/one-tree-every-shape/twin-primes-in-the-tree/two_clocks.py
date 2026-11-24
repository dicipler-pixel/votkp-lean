# SCRIPT: TWIN-TWO-CLOCKS-01
# Question: does a second clock (the phase: start residue mod 30, and the previous air) carry what the log clock misses?
# Kill written before the run: if the phase clock gives < 0.01 bits about the next air class, or shifts the mean
# next-gap ratio by < 5% between its classes, the second clock adds nothing and one clock is enough.
import numpy as np, math
N=10**8
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
C2=0.6601618158468696
g=(T[1:]-T[:-1]).astype(float); r=g/(np.log(T[:-1].astype(float))**2/(2*C2))
air=(g-2).astype(int)%30
def H(x):
    _,c=np.unique(x,return_counts=True); p=c/c.sum(); return -(p*np.log2(p)).sum()
def MI(x,y): return H(x)+H(y)-H(x*1000+y)
start=T[:-1]%30
prev=np.r_[-1,air[:-1]]
m=(T[:-1]>1e6)&(prev>=0)
print('H(next air class) = %.3f bits'%H(air[m]))
print('MI(start residue ; next air) = %.4f bits'%MI(start[m],air[m]))
print('MI(previous air ; next air)  = %.4f bits'%MI(prev[m],air[m]))
print('MI(both ; next air)          = %.4f bits'%MI(start[m]*100+prev[m],air[m]))
print('mean next-gap ratio (log clock = 1) by start residue:',{int(k):round(r[m][start[m]==k].mean(),3) for k in (11,17,29)})
print('mean next-gap ratio by previous air class:',{int(k):round(r[m][prev[m]==k].mean(),3) for k in (4,10,16,22,28)})
