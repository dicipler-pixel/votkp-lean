# SCRIPT: TORUS-CHECK-02
# Is 15n_41185 the torus knot T(4,5)? Without Sage, compare fingerprints with T(4,5) built from its braid (s1 s2 s3)^5:
# (1) hyperbolicity: torus-knot complements are not hyperbolic (no positive-volume solution);
# (2) homology of the first several cyclic covers (a strong knot fingerprint), H1 of the 2..7-fold cyclic branched-type covers
#     via M.covers(n, cover_type='cyclic').
import snappy, warnings
warnings.filterwarnings('ignore')
A=snappy.Manifold('K15n41185')
B=snappy.Link(braid_closure=[1,2,3]*5).exterior()
C=snappy.Manifold('10_124'); D=snappy.Link(braid_closure=[1,2]*5).exterior()
for nm,M in [('15n_41185',A),('T(4,5) braid',B),('10_124',C),('T(3,5) braid',D)]:
    hc=[]
    for n in range(2,7):
        try: hc.append(str([X.homology() for X in M.covers(n,cover_type='cyclic')]))
        except Exception as e: hc.append('err')
    print('%-13s solution: %-40s vol %.4f'%(nm,M.solution_type(),float(M.volume())))
    print('    cyclic cover homology n=2..6:',hc)
