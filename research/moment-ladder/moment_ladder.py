# SCRIPT: MOMENT-LADDER-01
# Pinpoints every rung of the oscillator-strength moment ladder S(k) = sum_m f_m * gap_m^k,
# with f_m = 2 * gap_m * |<0|D|m>|^2 (atomic units, one field direction).
# KILL LINES (written before the run):
#  K1 hydrogen: the field-space metric Q = sum |D|^2/gap^2 must equal 43/8 (half of published S(-3) = 43/4)
#     to 1e-6; otherwise "the tensor is the minus-third rung" failed this way.
#  K2 hydrogen: S(-4) must equal 319/12 to 1e-5, S(-2) must equal 9/2, S(-1) must equal 2; otherwise the code is wrong.
#  K3 three-level example: polarizability must vanish at photon energy squared 4/3 while Q = 2.
import numpy as np, sympy as sp
from scipy.sparse import diags
from scipy.sparse.linalg import splu

print('=== hydrogen ground state, uniform field along one axis')
R, n = 80.0, 400000
r = np.linspace(R/n, R, n); h = r[1]-r[0]
u0 = 2*r*np.exp(-r)                                   # ground state, radial
# (H - E0) on the angular-momentum-one channel: -1/2 d2/dr2 + 1/r^2 - 1/r + 1/2
main = 1.0/h**2 + 1.0/r**2 - 1.0/r + 0.5; off = -0.5/h**2*np.ones(n-1)
lu = splu(diags([off, main, off], [-1, 0, 1], format='csc'))
G = [r*u0]                                            # G0 = D|0> (radial part); angular factor 1/3
for k in range(3): G.append(lu.solve(G[-1]))
ip = lambda a, b: float(np.sum(a*b)*h)/3.0
S = {-1: 2*ip(G[0], G[0]), -2: 2*ip(G[0], G[1]), -3: 2*ip(G[1], G[1]), -4: 2*ip(G[1], G[2]), -5: 2*ip(G[2], G[2]), -6: 2*ip(G[2], G[3])}
Q = ip(G[1], G[1])
rr = sp.symbols('r', positive=True); psi2 = sp.exp(-2*rr)/sp.pi
p2 = 1                                                # <p^2> = 1 for the ground state
S[0] = 1; S[1] = sp.Rational(2, 3)*p2; S[2] = sp.Rational(4, 3)   # f-sum; (2/3)<p^2>; (4 pi/3) * density at nucleus
exact = {2: '4/3', 1: '2/3', 0: '1', -1: '2', -2: '9/2', -3: '43/4', -4: '319/12'}
for k in range(2, -7, -1): print('S(%2d) = %-12s' % (k, ('%.6f' % float(S[k]))), ' published/closed form:', exact.get(k, ''))
print('field-space metric Q = %.7f   43/8 = %.7f' % (Q, 43/8))
print('static polarizability = S(-2) = %.6f ; next terms of polarizability in photon energy: S(-4) = %.5f, S(-6) = %.4f' % (S[-2], S[-4], S[-6]))

print('=== your three-level example: gaps 1 and 2, |D01|^2 = 1, |D02|^2 = 4')
gap = np.array([1.0, 2.0]); d2 = np.array([1.0, 4.0]); f = 2*gap*d2
for k in range(2, -7, -1): print('S(%2d) = %.6f' % (k, np.sum(f*gap**k)))
Q3 = np.sum(d2/gap**2); print('field-space metric Q = S(-3)/2 =', Q3)
alpha = lambda y: np.sum(f/(gap**2 - y))
print('polarizability at photon energy squared 0, 1/2, 4/3, 3:', [round(alpha(y), 6) for y in (0, 0.5, 4/3, 3)])
y = sp.symbols('y'); a = sum(sp.Rational(int(ff))/(sp.Rational(int(g))**2 - y) for ff, g in zip(f, gap))
print('closed form:', sp.factor(sp.together(a)), '  zero at y =', sp.solve(sp.numer(sp.together(a)), y))
print('series of polarizability in y:', sp.series(a, y, 0, 4))
print('mean-gap ladder: S(-1)/S(-2) = %.4f, S(-2)/S(-3) = %.4f, S(-3)/S(-4) = %.4f (each is a weighted mean gap; they fall toward the smallest gap, 1)' % tuple(np.sum(f*gap**k)/np.sum(f*gap**(k-1)) for k in (-1, -2, -3)))
