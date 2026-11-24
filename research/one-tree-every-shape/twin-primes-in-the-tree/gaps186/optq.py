# SCRIPT: GAPS-OPT-QUOTIENT-01
# Best cap quotient rho* c^T B c / c^T A c over the 77-function trial space: a generalized eigenvalue
# problem. A is scaled to unit diagonal and solved through eigh; the answer is checked by plugging the
# optimal c back into both forms.
import numpy as np, sys
from capgram import C_THEIRS
rs=2624989/10**7
k=int(sys.argv[1]); A,B=np.load(f'gram_k{k}_N98304.npy')
d=1/np.sqrt(np.diag(A)); As=A*d[:,None]*d[None,:]; Bs=B*d[:,None]*d[None,:]
w,V=np.linalg.eigh(As); print('cond(A scaled) %.2e'%(w.max()/w.min()))
keep=w>w.max()*1e-14; W=V[:,keep]/np.sqrt(w[keep])
M=W.T@Bs@W; m,U=np.linalg.eigh(M); c=d*(W@U[:,-1])
q=rs*(c@B@c)/(c@A@c)
print('k',k,'best cap quotient %.8f'%q, ' (their trial at k=40: %.8f)'%(rs*(C_THEIRS@np.load('gram_k40_N98304.npy')[1]@C_THEIRS)/(C_THEIRS@np.load('gram_k40_N98304.npy')[0]@C_THEIRS)))
np.save(f'copt_k{k}.npy',c)
