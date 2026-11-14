# SCRIPT: CHK-09-CHART-FORMULA (R7 O17: chart closed form y=2X^2+Z^2-X^2 Z-2 with X=s+1/s, Z=s^2+1/s^2-v vs numeric tr[a,b] and 2-v(A-v))
import numpy as np, math
rng=np.random.default_rng(1); mx1=mx2=0
for _ in range(1000):
    x=rng.uniform(0.05,3); v=rng.uniform(-3,6); s=math.exp(x)
    a=np.array([[s,1],[0,1/s]]); b=np.array([[s,0],[-v,1/s]])
    K=a@b@np.linalg.inv(a)@np.linalg.inv(b); tr=K[0,0]+K[1,1]
    X=s+1/s; Z=s*s+1/s/s-v; y=2*X*X+Z*Z-X*X*Z-2
    A=(s-1/s)**2; t3=2-v*(A-v)
    mx1=max(mx1,abs(tr-y)/(1+abs(tr))); mx2=max(mx2,abs(tr-t3)/(1+abs(tr)))
print("max rel diff numeric trace vs chart closed form:",mx1,"  vs 2 - v((s-1/s)^2 - v):",mx2)
# trefoil: v from R3=s^4 - s^2 v - s^2 + 1 = 0 -> tr[a,b] = 2 + ... check k=-v
for x in (0.05,0.5,2):
    s=math.exp(x); v=(s**4-s**2+1)/s**2; A=(s-1/s)**2; print("trefoil x",x,"v",v,"v-(A+1)",v-(A+1),"k=v(A-v)",v*(A-v))
