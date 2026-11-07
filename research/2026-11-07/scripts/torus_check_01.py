# SCRIPT: TORUS-CHECK-01
# Is Micheletti's 15-crossing privileged knot 15n_41185 the torus knot T(4,5)? Two independent checks:
# (1) its Alexander polynomial must equal T(4,5)'s, (t^20-1)(t-1)/((t^4-1)(t^5-1)); (2) its complement must be
# non-hyperbolic (volume 0 / not a hyperbolic solution), as torus-knot complements are Seifert fibred.
import snappy, warnings, sympy as sp
warnings.filterwarnings('ignore')
t=sp.Symbol('t')
for name,(p,q) in [('K15n41185',(4,5)),('K10n21',(3,5))]:
    try:
        M=snappy.Manifold(name)
    except Exception as e:
        print(name,'not found:',e); continue
    A=sp.Poly(sp.sympify(str(M.alexander_polynomial()).replace('a','t')),t)
    T=sp.Poly(sp.cancel((t**(p*q)-1)*(t-1)/((t**p-1)*(t**q-1))),t)
    print(name,'Alexander:',A.as_expr(),'| T(%d,%d):'%(p,q),T.as_expr(),'| equal:',sp.expand(A.as_expr()-T.as_expr())==0 or sp.expand(A.as_expr()+T.as_expr())==0)
    print('   solution type:',M.solution_type(),' volume:',float(M.volume()))
print('10_124 in snappy as Rolfsen:',snappy.Manifold('10_124').solution_type(), float(snappy.Manifold('10_124').volume()))
