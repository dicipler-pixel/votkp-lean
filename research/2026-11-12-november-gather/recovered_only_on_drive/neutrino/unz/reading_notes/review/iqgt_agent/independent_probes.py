"""Review-only probes; original IQGT artifacts are not modified."""
import numpy as np

def norm(a):
    return np.linalg.norm(a, 2)

print('1. Gradient normalization under g(V,W)=Tr(VW)/2')
P = np.diag([1., 0.])
O = np.array([[0., 1.], [1., 0.]])
F = (O@P-P@O)@P-P@(O@P-P@O)
V = O
df = np.trace(O@V).real
gFV = .5*np.trace(F@V).real
print(f'df[V]={df}, g(F,V)={gFV}, g(2F,V)={2*gFV}')
assert np.isclose(2*gFV, df) and not np.isclose(gFV, df)

print('\n2. Gauge-closed lower-band Berry loop')
sx = np.array([[0,1],[1,0]])
sy = np.array([[0,-1j],[1j,0]])
sz = np.diag([1.,-1.])
theta = np.pi/3
phases = np.linspace(0, 2*np.pi, 4001)
vectors=[]
for phi in phases:
    H = np.sin(theta)*np.cos(phi)*sx + np.sin(theta)*np.sin(phi)*sy + np.cos(theta)*sz
    vectors.append(np.linalg.eigh(H)[1][:,0])
chain = np.prod([np.vdot(vectors[j],vectors[j+1]) for j in range(len(vectors)-1)])
closure = np.vdot(vectors[-1],vectors[0])
raw, closed = -np.angle(chain), -np.angle(chain*closure)
expected = np.pi*(1-np.cos(theta))
print(f'open chain={raw:.12g}, closure={closure}, closed={closed:.12g}, curvature integral={expected:.12g}')
assert abs(closed-expected)<1e-6

print('\n3. Interleaved-spectrum operator-norm counterexample to Eq. 10.5')
A = np.diag([0.,2.,1.,3.])
C = np.array([[1.,1.],[1.,-1.]])/np.sqrt(2)
E = 1e-4*np.block([[np.zeros((2,2)),C],[C.T,np.zeros((2,2))]])
P = np.diag([1.,1.,0.,0.])
values, U = np.linalg.eigh(A+E)
Pnew = U[:,[0,2]]@U[:,[0,2]].T
Qnew = np.eye(4)-Pnew
delta = min(abs(a-b) for a in [0.,2.] for b in values[[1,3]])
lhs = norm(Qnew@P)
rhs = norm(Qnew@E@P)/delta
print(f'delta={delta:.12g}, lhs={lhs:.12g}, rhs={rhs:.12g}, ratio={lhs/rhs:.12g}')
assert lhs > 1.2*rhs

print('\n4. Derived neutrino kept-population bound (random pointwise checks)')
rng=np.random.default_rng(492)
worst=0.
for _ in range(2000):
    n=8
    raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    H=(raw+raw.conj().T)/2
    rates=np.r_[0., rng.uniform(0,10,n-1)]
    v=rng.normal(size=n)+1j*rng.normal(size=n)
    v*=rng.uniform(.01,1)/np.linalg.norm(v)
    Dv=-rates*v
    vdot=-1j*H@v+Dv
    pop=abs(v[0])**2
    popdot=2*np.real(v[0].conjugate()*vdot[0])
    EB=np.sum(abs(H[0,1:])**2)
    total=np.vdot(v,v).real
    sharp=4*EB*pop*(total-pop)
    simple=4*EB*pop*(1-pop)
    assert popdot**2 <= sharp+1e-11
    assert sharp <= simple+1e-11
    assert 2*np.vdot(v,Dv).real <= 1e-12
    worst=max(worst,popdot**2/simple)
print(f'2,000 contractive-flow states passed; maximal fraction of simple bound={worst:.8f}')
print('These are numerical probes plus explicit counterexamples, not a proof-system run.')
