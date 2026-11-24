# SCRIPT: OPPOSITE-FIXED-STEP-SPREAD-01
# e-fix follow-up: is twin-arm d/L (0.7636) different from iid arms (0.7715)? 8 iid seeds give the spread; the
# twin arm sequence's repeat fraction (same arm twice in a row) against 1/3 says why (a repeat is a straight step, full gain ln5).
# Also an arm-shuffled twin sequence (same counts, order destroyed). Kill for "order matters": twin value inside the iid spread.
import numpy as np, math
from owalk import *
P=primes_upto(10**8); tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]; arm=np.searchsorted([1,7,9],T[1:]%10)
ns=arm.size; rf=np.full(ns,math.log(5)); L=ns*math.log(5)
def dl(a): D,_,_,_=walk(rf,a,np.eye(3),np.array([ns-1])); return D[0]/L
print('twin arms d/L %.5f   repeat fraction %.4f'%(dl(arm),(arm[1:]==arm[:-1]).mean()))
v=[dl(np.random.default_rng(s).integers(0,3,ns)) for s in range(8)]
print('iid arms d/L: mean %.5f  min %.5f max %.5f'%(np.mean(v),min(v),max(v)))
sh=[dl(np.random.default_rng(50+s).permutation(arm)) for s in range(4)]
print('shuffled twin arms d/L:',np.round(sh,5))
# alternating-free control: Markov arms with repeat prob = twin repeat fraction
rep=(arm[1:]==arm[:-1]).mean(); rng=np.random.default_rng(77); m=np.empty(ns,dtype=np.int64); m[0]=0
u=rng.random(ns); o=rng.integers(1,3,ns)
for i in range(1,ns): m[i]=m[i-1] if u[i]<rep else (m[i-1]+o[i])%3
print('Markov arms with the twin repeat fraction: d/L %.5f'%dl(m))
