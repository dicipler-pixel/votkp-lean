# SCRIPT: COLOUR-PEEL-01
# Join under test (hole 2): the two rulers of Colour Selects the Leader (Section 6: Hilbert's projective metric, which every
# strictly positive map contracts, and Schrodinger's chromatic metric, which 955 of 20,000 recorded passes stretched) are,
# for two channels, the two coordinates of one peel step:
#     ratio z = x1/x2,  share balance s1 - s2 = (z-1)/(z+1) = G (the Smith point),
#     Hilbert distance = |ln z - ln z'| = peel distance tau (VOTKP 8.1),
#     Schrodinger distance = |phi - phi'| with cos(phi) = G = tanh(tau/2), so d(phi) = (1/2) sech(tau/2) d(tau).
# Prediction that follows (and that the paper does not state): a pass stretches Schrodinger's metric on a close pair
# exactly when  c * cosh(tau/2)/cosh(tau'/2) > 1  (c = local Hilbert contraction, tau' = image position), which forces
# |tau'| < |tau|: a stretch can only happen while the pair is carried TOWARD the white point (equal shares).
# Why this decides it: the identities are checked on random pairs to round-off; the prediction is checked by counting
# stretches on random positive maps and comparing each with the formula and with the direction of motion.
# KILL: (1) any identity off by more than 1e-9; (2) any two-channel stretch with |tau'| >= |tau|;
#       (3) the formula misclassifies any pass.  Opposite: count stretches among passes carried AWAY from white (must be 0).
# Three channels (the paper's own setting) is run as exploration, with "toward white" = Hilbert distance to (1,1,1) falls.
import numpy as np
rng=np.random.default_rng(7)
def hil(x,y): r=np.log(x/y); return r.max(-1)-r.min(-1)
def sch(x,y):
    p=x/x.sum(-1,keepdims=True); q=y/y.sum(-1,keepdims=True)
    return 2*np.arccos(np.clip(np.sqrt(p*q).sum(-1),-1,1))
n=20000
x=rng.uniform(.05,5,(n,2)); y=rng.uniform(.05,5,(n,2))
z=x[:,0]/x[:,1]; w=y[:,0]/y[:,1]
G=(z-1)/(z+1); bal=(x[:,0]-x[:,1])/x.sum(1)
print('identities, 2 channels, %d random pairs:'%n)
print('  balance - Smith point            max err %.2e'%np.abs(bal-G).max())
print('  Hilbert - |ln z - ln w|          max err %.2e'%np.abs(hil(x,y)-np.abs(np.log(z/w))).max())
print('  Schrodinger - |phi - phi\'|       max err %.2e'%np.abs(sch(x,y)-np.abs(np.arccos(G)-np.arccos((w-1)/(w+1)))).max())
print('  cos(phi) - tanh(tau/2)           max err %.2e'%np.abs(np.cos(np.arccos(G))-np.tanh(np.log(z)/2)).max())
# stretch test, close pairs
M=rng.uniform(.01,3,(n,2,2)); x=rng.uniform(.05,5,(n,2)); y=x*np.exp(1e-4*rng.standard_normal((n,2)))
Mx=np.einsum('nij,nj->ni',M,x); My=np.einsum('nij,nj->ni',M,y)
st=sch(Mx,My)>sch(x,y); c=hil(Mx,My)/hil(x,y)
tau=np.log(x[:,0]/x[:,1]); taup=np.log(Mx[:,0]/Mx[:,1])
pred=c*np.cosh(tau/2)/np.cosh(taup/2)>1
print('2 channels, %d passes on close pairs: Hilbert stretched %d; Schrodinger stretched %d (%.1f%%)'%(n,int((c>1+1e-9).sum()),int(st.sum()),100*st.mean()))
print('  formula agrees on %d of %d passes'%(int((pred==st).sum()),n))
print('  stretches with the pair carried toward white: %d   away from white: %d'%(int((st&(np.abs(taup)<np.abs(tau))).sum()),int((st&(np.abs(taup)>=np.abs(tau))).sum())))
# three channels, the paper's setting
M=rng.uniform(.01,3,(n,3,3)); x=rng.uniform(.05,5,(n,3)); y=rng.uniform(.05,5,(n,3))
Mx=np.einsum('nij,nj->ni',M,x); My=np.einsum('nij,nj->ni',M,y)
st=sch(Mx,My)>sch(x,y); one=np.ones(3)
tw=(hil(Mx,one)+hil(My,one))<(hil(x,one)+hil(y,one))
print('3 channels, %d passes, generic pairs: Hilbert stretched %d; Schrodinger stretched %d (paper recorded 955 of 20,000)'%(n,int((hil(Mx,My)>hil(x,y)+1e-12).sum()),int(st.sum())))
print('  of the stretches: pair carried toward white %d, away %d;   base rate toward white over all passes %.3f'%(int((st&tw).sum()),int((st&~tw).sum()),tw.mean()))
