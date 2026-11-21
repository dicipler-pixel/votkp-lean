"""Finite-dimensional cross-check; synthetic orbitals, no elemental calculation."""
import numpy as np

rng=np.random.default_rng(37)
N,M=8,4
k=2*np.pi*(np.arange(N)+.217)/N
positions=np.arange(N)
occupations=[3,3,2,2,1,1,2,2]
states=[]
for n in occupations:
    trial=rng.normal(size=(M,M))+1j*rng.normal(size=(M,M))
    frame=np.linalg.qr(trial)[0]
    states.append(frame[:,:n])

def run(states, weights):
    phase=np.exp(1j*positions[:,None]*k)
    allstates=np.concatenate([np.kron(phase[:,j,None],u)/np.sqrt(N) for j,u in enumerate(states)],axis=1)
    vals=np.concatenate(weights)
    rho=(allstates*vals)@allstates.T.conj()
    real=2*np.array([np.linalg.norm(rho[:M,R*M:(R+1)*M])**2 for R in positions])
    spec=np.zeros(N,dtype=complex)
    for j,u in enumerate(states):
        for l,v in enumerate(states):
            g=u.T.conj()@v
            pair=np.sum(weights[j][:,None]*weights[l][None,:]*np.abs(g)**2)
            spec+=2/N**2*np.exp(1j*(k[j]-k[l])*positions)*pair
    assert np.max(np.abs(real-spec))<1e-12
    charge=2*sum(np.sum(w) for w in weights)/N
    b=charge-real[0]
    return real,charge,b

weights=[np.ones(s.shape[1]) for s in states]
x,tr,b=run(states,weights)
assert abs(sum(x)-tr)<1e-12
assert abs(sum(x[1:])-b)<1e-12
print(f'Pure projector: cell trace {tr:.9f}, X0 {x[0]:.9f}, off-cell budget {b:.9f}. Both independent constructions agree.')
rotated=[]
for u in states:
    n=u.shape[1];w=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
    rotated.append(u@w)
xrot,_,_=run(rotated,weights)
assert np.max(np.abs(xrot-x))<1e-12
print('Independent occupied-band unitary gauge rotations preserve all R.')
frac=[w*.73 for w in weights]
xf,tf,bf=run(states,frac)
res=tf-sum(xf)
expected=2*sum(np.sum(w-w*w) for w in frac)/N
assert abs(res-expected)<1e-12 and expected>1e-2
print(f'Fractional-occupation control: missing weight {res:.9f} matches Tr(rho-rho²) per cell.')
identity=[np.eye(M) for j in k]
allx,allt,allb=run(identity,[np.ones(M) for j in k])
assert abs(allb)<1e-12 and np.max(np.abs(allx[1:]))<1e-12
print('Complete occupied one-site basis has B=0, so X/B is undefined.')
