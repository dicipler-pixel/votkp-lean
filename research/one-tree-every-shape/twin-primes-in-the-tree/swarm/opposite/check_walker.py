# SCRIPT: OPPOSITE-WALKER-CHECK-01
# Kill line: stable polar walker must match brute matrix products to 1e-8 in d, n, R (3D twins, 4D primes, 5D tetra-free, random signs, fixed ln5 steps)
import numpy as np, math
from owalk import *
P=primes_upto(10**6)
tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
r=np.log(T[1:]/T[:-1]); arm=np.searchsorted([1,7,9],T[1:]%10)
print('twin 3D', check_walker(r,arm,np.eye(3),3000))
Q=P[P>5]; r2=np.log(Q[1:]/Q[:-1]); arm2=np.searchsorted([1,3,7,9],Q[1:]%10)
print('primes 4D', check_walker(r2,arm2,np.eye(4),3000))
tet=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/math.sqrt(3)
print('primes tetra', check_walker(r2,arm2,tet,3000))
rng=np.random.default_rng(0)
print('signed 5D', check_walker(r[:3000]*rng.choice([-1,1],3000),rng.integers(0,5,3000),np.eye(5),3000))
print('fixed ln5 (only 12 steps, matrices overflow later)', check_walker(np.full(12,math.log(5)),arm,np.eye(3),12))
