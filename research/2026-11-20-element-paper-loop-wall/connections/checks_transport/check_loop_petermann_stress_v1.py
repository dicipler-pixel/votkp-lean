# SCRIPT: WTK-LOOPWALL-PETERMANN-STRESS-01
"""
Connection: WTK Proposition 7 (rank-one stress S = 1 - |u*v|^2, idempotent norm
kappa = 1/|v*u|, S = 1 - kappa^-2) applied to the loop holonomy of the element paper.

Why this check proves what it claims:
 - The loop holonomy W = A B A^-1 B^-1 (perpendicular half-steps h_a, h_b, built as in
   WTK-LOOPWALL-LOOP-SELECTION-01) is a real 2x2 matrix of determinant 1. Inside the
   wall it has two complex eigenvalues; each spectral idempotent is the rank-one
   Pi = r l^T/(l^T r). WTK Prop 7 says its operator norm is kappa = ||l|| ||r||/|l^T r|
   (unit u = r/||r||, v = conj(l)/||l||) and its stress is S = 1 - kappa^-2.
 - If sympy proves kappa^2 = 1/(1 - Gamma_a^2 - Gamma_b^2) identically (Gamma = tanh h),
   then S = Gamma_a^2 + Gamma_b^2: the loop's WTK stress IS the element paper's closing
   sum, and the wall S = 1 is where kappa diverges (the idempotent stops existing: WTK
   says "at zero overlap this idempotent is undefined"). Equal faces give S = 2 Gamma^2,
   kappa^2 = 1/(1 - 2 Gamma^2), the VOTKP v3.2 Petermann factor.
 - Frame check (WTK Theorem 4 / assumption A1): kappa is a property of W AND the inner
   product. Conjugating W by an orthogonal rotation must leave kappa unchanged; by a
   non-orthogonal boost it must change it. If both happen, the identity is a statement
   in the frame centred at the loop's corner, as WTK requires such statements to be.
 - Face check: the per-face rank-one idempotent u v^T/(v^T u) with u = (cosh(h/2), sinh(h/2)),
   v = (cosh(h/2), -sinh(h/2)) must have S = tanh^2 h = Gamma^2 and kappa = cosh h; and
   WTK's tensor law 1 - S(a x b) = (1 - S_a)(1 - S_b) must hold for two faces.
"""
import sympy as sp, numpy as np, math, gzip, json
ARCH = '/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
IE = {r['symbol']: [t['IE_eV'] for t in sorted(r['thresholds'], key=lambda t: t['q'])] for r in json.load(gzip.open(ARCH))['records']}

ga, gb = sp.symbols('g_a g_b', positive=True)          # g = Gamma = tanh h
# write cosh, sinh, e^h through Gamma: e^{2h} = (1+g)/(1-g)
def parts(g):
    e2 = (1+g)/(1-g); e = sp.sqrt(e2)
    c = (e + 1/e)/2; s = (e - 1/e)/2
    return e, c, s
ea, ca, sa = parts(ga); eb, cb, sb = parts(gb)
A = sp.Matrix([[ea, 0], [0, 1/ea]]); B = sp.Matrix([[cb, sb], [sb, cb]])
W = sp.simplify(A*B*A.inv()*B.inv())
t = sp.simplify(W.trace())
print('tr W in Gammas:', sp.factor(t))
# For a real 2x2 W = [[p,q],[r,s]] with complex eigenvalues lam, conj(lam):
# right eigvec (q, lam - p), left eigvec (r, lam - p) (rows of W^T), so
# kappa^2 = (|q|^2+|lam-p|^2)(|r|^2+|lam-p|^2)/|q r + (lam-p)^2|^2 .
p, q, r, s = W[0,0], W[0,1], W[1,0], W[1,1]
lam = sp.symbols('lam')
# |lam - p|^2 with lam = t/2 + i*sqrt(1 - t^2/4):  (t/2 - p)^2 + 1 - t^2/4
m2 = sp.simplify((t/2 - p)**2 + 1 - t**2/4)
# q r + (lam-p)^2 : lam^2 - 2 p lam + p^2 + q r, use lam^2 = t lam - 1
# = (t - 2p) lam - 1 + p^2 + q r ; real part and imaginary part:
re = sp.simplify((t - 2*p)*t/2 - 1 + p**2 + q*r); im2 = sp.simplify((t - 2*p)**2*(1 - t**2/4))
kappa2 = sp.simplify((q**2 + m2)*(r**2 + m2)/(re**2 + im2))
print('kappa^2 * (1 - Ga^2 - Gb^2) simplifies to:', sp.simplify(sp.factor(kappa2*(1 - ga**2 - gb**2))))

def loop(za, zb):
    a, b = 0.5*math.log(za), 0.5*math.log(zb)
    A = np.array([[math.exp(a), 0], [0, math.exp(-a)]])
    B = np.array([[math.cosh(b), math.sinh(b)], [math.sinh(b), math.cosh(b)]])
    return A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
def kappa2_num(W):
    w, R = np.linalg.eig(W); w2, L = np.linalg.eig(W.T)
    r = R[:, 0]; l = L[:, np.argmin(abs(w2 - w[0]))]
    return (np.linalg.norm(l)**2*np.linalg.norm(r)**2)/abs(l @ r)**2
print('\nnumeric, inside the wall (archive ratios):')
for name, za, zb in [('nitrogen K opening both faces', 552.06741/97.8901, 552.06741/97.8901),
                     ('potassium with calcium (Ar-core)', IE['K'][1]/IE['K'][0], IE['Ca'][2]/IE['Ca'][1]),
                     ('rubidium with strontium (Kr-core)', IE['Rb'][1]/IE['Rb'][0], IE['Sr'][2]/IE['Sr'][1]),
                     ('z = 3 both faces', 3.0, 3.0), ('z = 5 both faces', 5.0, 5.0)]:
    g1 = ((za-1)/(za+1))**2; g2 = ((zb-1)/(zb+1))**2
    if g1 + g2 >= 1: print('  ', name, 'outside, skipped'); continue
    print(f'   {name:30s} kappa^2 = {kappa2_num(loop(za,zb)):.9f}   1/(1-G1^2-G2^2) = {1/(1-g1-g2):.9f}')

W = loop(552.06741/97.8901, 552.06741/97.8901)
th = 0.7; Rm = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
Bm = np.array([[math.cosh(0.3), math.sinh(0.3)], [math.sinh(0.3), math.cosh(0.3)]])
print('\nframe check (WTK A1, Theorem 4):')
print('   original frame        kappa^2 =', f'{kappa2_num(W):.9f}')
print('   rotated frame R W R^T kappa^2 =', f'{kappa2_num(Rm @ W @ Rm.T):.9f}  (orthogonal change: unchanged)')
print('   boosted frame S W S^-1 kappa^2 =', f'{kappa2_num(Bm @ W @ np.linalg.inv(Bm)):.9f}  (non-orthogonal change: different)')

print('\nface idempotent and WTK tensor law:')
def face(z):
    h = 0.5*math.log(z); u = np.array([math.cosh(h/2), math.sinh(h/2)]); v = np.array([math.cosh(h/2), -math.sinh(h/2)])
    return u/np.linalg.norm(u), v/np.linalg.norm(v), h
for z in [392.09056/64.49352, 552.06741/97.8901]:
    u, v, h = face(z); S = 1 - (u @ v)**2; G = (z-1)/(z+1)
    print(f'   z = {z:.6f}: S = {S:.12f}, Gamma^2 = {G*G:.12f}, kappa = {1/abs(u@v):.12f}, cosh h = {math.cosh(h):.12f}')
(u1, v1, _), (u2, v2, _) = face(392.09056/64.49352), face(552.06741/97.8901)
U = np.kron(u1, u2); V = np.kron(v1, v2)
S12 = 1 - (U @ V)**2; S1 = 1 - (u1 @ v1)**2; S2 = 1 - (u2 @ v2)**2
print(f'   1 - S(a x b) = {1-S12:.12f}   (1-S_a)(1-S_b) = {(1-S1)*(1-S2):.12f}')
print(f'   but the loop needs S_a + S_b < 1: S_a + S_b = {S1+S2:.6f}; tensor stress S(a x b) = {S12:.6f}')
print('\ngeometric reading of the frame: kappa^2 = cosh^2 d(corner i, fixed point of W) in the upper half-plane')
print('  (the inner product of WTK A1 picks the point i; a different instrument picks a different point)')
for za, zb in [(3.0, 3.0), (5.0, 5.0), (552.06741/97.8901, 552.06741/97.8901), (IE['K'][1]/IE['K'][0], IE['Ca'][2]/IE['Ca'][1])]:
    Wm = loop(za, zb); p_, q_, r_, s_ = Wm.ravel()
    w = [x for x in np.roots([r_, s_ - p_, -q_]) if x.imag > 0][0]
    cd = 1 + abs(w - 1j)**2/(2*w.imag)
    print(f'  z = ({za:.6f}, {zb:.6f}): cosh^2 d = {cd*cd:.9f}, kappa^2 = {kappa2_num(Wm):.9f}')
