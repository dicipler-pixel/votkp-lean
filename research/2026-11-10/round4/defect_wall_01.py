# SCRIPT: DEFECT-WALL-01
# Joins under test (holes 2 and 3; all exact algebra, then numerics as a guard):
#  A. Two Trees meridians a=[[s,1],[0,1/s]], b=[[s,0],[-v,1/s]]: commutator number k = 2 - tr[a,b].
#     Claim: k = -v (v + dM), where dM = 2 - (s^2 + s^-2) is the UPG defect |lambda-1|^2 of the squared meridian eigenvalue.
#  B. For a real climb step z = s^2 = e^tau:  dM = -4 sinh^2(tau/2) = -4 G^2/(1-G^2),  G = (z-1)/(z+1).
#     For a turn step s = e^{i theta/2}:      dM = +4 sin^2(theta/2)  (the clock defect, and 4x the crossed-port fraction of the
#     Colour paper eq. (6) at retardance theta).
#  C. Claim: the half line G^2 = 1/2 (z = 3+2 sqrt2) is exactly |dM| = 4, and on the real slice (v real) the commutator can
#     reach the top of the turning band, k = 4, if and only if |dM| >= 4.  With the meridian on the unit circle, k <= dM^2/4 < 4.
#  D. A strictly positive 2x2 map (the Colour paper's Theorem 2 with two channels) can never be elliptic or parabolic.
# Why this decides it: A, B, C are polynomial identities; sympy simplify must return 0 exactly. D is a discriminant sign.
# KILL: any identity leaves a nonzero remainder; or a random real (s,v) gives k > dM^2/4; or a positive matrix has
#       discriminant <= 0.  Opposite test: look for a positive matrix that turns by random search (must find none).
import sympy as sp, numpy as np
s,v,z,tau,th=sp.symbols('s v z tau theta',positive=True)
a=sp.Matrix([[s,1],[0,1/s]]); b=sp.Matrix([[s,0],[-v,1/s]])
com=a*b*a.inv()*b.inv(); k=sp.simplify(2-com.trace())
dM=2-(s**2+s**-2)
print('A  k =',sp.factor(k),'   remainder k + v(v+dM) =',sp.simplify(k+v*(v+dM)))
G=(z-1)/(z+1); dMz=2-(z+1/z)
print('B  dM + 4G^2/(1-G^2) =',sp.simplify(dMz+4*G**2/(1-G**2)),
      '   dM + 4 sinh^2(tau/2) =',sp.simplify((2-(sp.exp(tau)+sp.exp(-tau))+4*sp.sinh(tau/2)**2).rewrite(sp.exp)))
print('   turn: dM - 4 sin^2(theta/2) =',sp.simplify(2-2*sp.cos(th)-4*sp.sin(th/2)**2))
print('C  solve |dM| = 4 for z:',sp.solve(sp.Eq(-dMz,4),z),'  G^2 there:',[sp.nsimplify(sp.simplify(G.subs(z,r)**2)) for r in sp.solve(sp.Eq(-dMz,4),z)])
d=sp.symbols('d',real=True); vv=sp.symbols('vv',real=True)
kq=-vv*(vv+d); print('   max over real v of k = ',sp.simplify(kq.subs(vv,-d/2)),' at v = -dM/2;  k=4 has real v iff disc =',sp.factor(sp.discriminant(vv**2+d*vv+4,vv)),'>= 0')
rng=np.random.default_rng(1); bad=0; n=200000
S=np.exp(rng.uniform(-2,2,n)); V=rng.uniform(-30,30,n); D=2-(S**2+S**-2); K=-V*(V+D); bad=int(np.sum(K>D**2/4+1e-9))
print('   numeric guard: k > dM^2/4 in',bad,'of',n,'random real (s,v)')
th_=rng.uniform(0,2*np.pi,n); D2=4*np.sin(th_/2)**2; K2=-V*(V+D2); print('   unit-circle meridian: max k found =',round(float(K2.max()),6),' (cap 4 only at theta=pi); k>=4 count:',int(np.sum(K2>=4)))
M=rng.uniform(1e-6,10,(n,4)); disc=(M[:,0]-M[:,3])**2+4*M[:,1]*M[:,2]
print('D  positive 2x2 maps with discriminant <= 0 (would turn or sit on the wall):',int(np.sum(disc<=0)),'of',n,'   [exact: (a-d)^2+4bc > 0]')
print('   crossed-port fraction at the trefoil walls (alpha=1/12,5/12; omega=M^2): ',[float(np.sin(2*np.pi*x)**2) for x in (1/12,5/12)],' = defect/4 with defect 1 (clock d=6)')
