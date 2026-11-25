# SCRIPT: TWIN-HONEYCOMB-534-02  Markov surrogate for the honeycomb drift signal (see HONEYCOMB_PREREG.md)
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
M=np.zeros((3,3)); np.add.at(M,(s[:-1],s[1:]),1); T=M/M.sum(1,keepdims=True)
print('transition matrix (row = from x,y,z):'); print(np.round(T,4))
real=drift(s); rng=np.random.default_rng(5); out=[]
for j in range(60):
    q=np.empty(len(s),int); q[0]=s[0]; u=rng.random(len(s)); C=np.cumsum(T,1)
    for i in range(1,len(s)): q[i]=np.searchsorted(C[q[i-1]],u[i])
    out.append(drift(q))
out=np.array(out); z=(real-out.mean())/out.std()
print('drift per step: real %.6f; Markov surrogates %.6f +- %.6f; z = %.2f'%(real,out.mean(),out.std(),z))
print('KILL: honeycomb signal is fully the pair bias' if abs(z)<2 else 'PASS: longer-range order shows on the honeycomb')
