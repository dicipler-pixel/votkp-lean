# SCRIPT: TWIN-HONEYCOMB-534-03  block Markov surrogate (transition matrix per 50,000-step block)
import numpy as np, math
phi=(1+5**.5)/2; l=math.acosh(phi)
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
mats=[math.cosh(l/2)*np.eye(2)+math.sinh(l/2)*sg[k] for k in range(3)]
TW=np.load('../shapes/twins_1000000000.npy').astype(np.int64); TW=TW[TW>=11]
arm={1:0,7:1,9:2}; s=np.array([arm[int(x)%10] for x in TW[1:]])[:10**6]
def drift(seq):
    v=np.eye(2,dtype=complex); logs=0.0
    for k in seq:
        v=v@mats[k]; m=np.abs(v).max(); v/=m; logs+=math.log(m)
    return 2*(logs+math.log(np.linalg.svd(v,compute_uv=False)[0]))/len(seq)
B=50000; Ts=[]
for b0 in range(0,len(s),B):
    seg=s[max(b0-1,0):b0+B]; M=np.zeros((3,3)); np.add.at(M,(seg[:-1],seg[1:]),1); Ts.append(np.cumsum(M/M.sum(1,keepdims=True),1))
print('repeat rate by block:',[round(float(np.mean(s[b0+1:b0+B]==s[b0:b0+B-1])),4) for b0 in range(0,len(s),B)])
real=drift(s); rng=np.random.default_rng(9); out=[]
for j in range(60):
    q=np.empty(len(s),int); q[0]=s[0]; u=rng.random(len(s))
    for i in range(1,len(s)): q[i]=np.searchsorted(Ts[i//B][q[i-1]],u[i])
    out.append(drift(q))
out=np.array(out); z=(real-out.mean())/out.std()
print('drift per step: real %.6f; block-Markov surrogates %.6f +- %.6f; z = %.2f'%(real,out.mean(),out.std(),z))
print('KILL: the residual was the drifting pair bias' if abs(z)<2 else 'PASS: longer-range order shows on the honeycomb')
