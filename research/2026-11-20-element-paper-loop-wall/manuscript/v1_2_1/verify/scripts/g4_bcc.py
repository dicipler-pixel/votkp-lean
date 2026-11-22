# SCRIPT: G4_BCC_HALF_FILLED
import numpy as np
N=96
k=(np.arange(N)+0.5)/N*2*np.pi-np.pi  # offset grid avoids exact zeros
kx,ky,kz=np.meshgrid(k,k,k,indexing='ij')
eps=-8*np.cos(kx)*np.cos(ky)*np.cos(kz)
occ=eps<0
print('filling',occ.mean())
# P(R)=<exp(ik.R)> over occupied / (N^3)
def P(R):
    return (np.exp(1j*(kx*R[0]+ky*R[1]+kz*R[2]))*occ).sum()/occ.size
p=P((1,1,1)).real; print('P nn',p,'per-spin; X per neighbour (two-spin)=',2*p*p, 'per-spin',p*p)
print('1/48',1/48)
