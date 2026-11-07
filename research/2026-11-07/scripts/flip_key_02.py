# SCRIPT: FLIP-KEY-02
# Exploratory. Separatrix lune of the intermediate axis: planes L3 = +/- k L1, k = sqrt(I3(I2-I1)/(I1(I3-I2))).
# Predicted lune angle alpha = 2 arctan k (area 2 alpha). Balanced case: 1/I2 midway between 1/I1 and 1/I3 gives k = 1,
# planes at 45 deg to each outer axis. Check by integrating one period close to the separatrix for several bodies.
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar
def run(I,eps=1e-4):
    I=np.array(I,float)
    f=lambda t,L: np.cross(L,L/I)
    L0=np.array([eps,I[1],0.7*eps]); Lm=np.linalg.norm(L0)
    s=solve_ivp(f,[0,400],L0,rtol=1e-12,atol=1e-14,dense_output=True,max_step=0.02)
    ts=np.linspace(0.5,400,800001); d=np.linalg.norm(s.sol(ts).T-L0,axis=1)
    i=np.where((d[1:-1]<d[:-2])&(d[1:-1]<d[2:])&(d[1:-1]<5e-3))[0][0]+1
    T=minimize_scalar(lambda t: np.linalg.norm(s.sol(t)-L0),bracket=(ts[i]-0.05,ts[i],ts[i]+0.05)).x
    n=(s.sol(np.linspace(0,T,200001))/Lm).T
    th=np.arccos(np.clip(n[:,2],-1,1)); ph=np.unwrap(np.arctan2(n[:,1],n[:,0]))
    sa=abs(np.sum((1-np.cos(0.5*(th[1:]+th[:-1])))*np.diff(ph)))
    k=np.sqrt(I[2]*(I[1]-I[0])/(I[0]*(I[2]-I[1])))
    return sa, 4*np.arctan(k), np.degrees(np.arctan(k))
for I in [(1,2,3),(1,1.5,3),(1,1.2,3),(1,2.5,3),(2,3,6),(1,4/3,2)]:
    sa,pred,deg=run(I)
    mid=abs(1/I[1]-0.5*(1/I[0]+1/I[2]))<1e-12
    print(f'I={I}: enclosed solid angle {sa:.6f}  predicted lune 4*arctan(k) {pred:.6f}  plane angle from axis 1: {deg:.4f} deg  {"<- 1/I2 midway" if mid else ""}')
