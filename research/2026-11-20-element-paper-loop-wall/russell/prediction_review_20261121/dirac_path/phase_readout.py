"""Verify the coherent two-route probe and its phase-randomized control."""
from math import pi, sin
import numpy as np
from scipy.linalg import expm

def normdist(rho):
    return sum(abs(np.linalg.eigvalsh(rho)))/2

def history(phi,visibility):
    # common path/record subspace in the basis |01>, |10>
    a = visibility*np.exp(1j*phi)
    state=np.zeros((4,4),complex)
    state[1:3,1:3]=np.array([[1,a.conjugate()],[a,1]])/2
    return state

X=np.array([[0,1],[1,0]])
H=np.zeros((4,4))
H[1:3,1:3]=X
U=expm(-1j*pi/4*H)
Z=np.diag([1,1,-1,-1])

def responses(rho):
    out=[]
    for q in (1,1j):
        # The local phase acts on the second alternative.
        ph=np.diag([1,1,q,q])
        u=U@ph
        out.append(float(np.trace(Z@u@rho@u.conj().T).real))
    return np.array(out)

def marginals(r):
    a=r.reshape((2,2,2,2))
    return np.trace(a,axis1=0,axis2=2), np.trace(a,axis1=1,axis2=3)

def test():
    maximum=0
    n=0
    for v in (0,0.20,0.75,1):
        for a in np.linspace(-pi, pi,17):
            for b in np.linspace(-pi, pi,17):
                ra,rb=history(a,v),history(b,v)
                assert all(np.allclose(x,y) for x,y in zip(marginals(ra),marginals(rb)))
                measured=np.linalg.norm(responses(ra)-responses(rb))/2
                direct=normdist(ra-rb)
                theory=v*abs(sin((a-b)/2))
                maximum=max(maximum,abs(measured-direct),abs(theory-direct))
                assert max(abs(measured-direct),abs(theory-direct)) < 1e-12
                n+=1
    print('phase-pair/visibility combinations:',n,'maximum error',f'{maximum:.3g}')
    for v,a,b in [(1,.74,2.22),(0,.74,2.22),(1,.74,pi-.74)]:
        da=responses(history(a,v))-responses(history(b,v))
        print('visibility, phases',v,round(a,6),round(b,6),'differences in Z probes',*(round(x,6) for x in da),'trace distance',round(np.linalg.norm(da)/2,6))
if __name__=='__main__':test()
