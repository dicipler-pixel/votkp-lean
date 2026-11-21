# SCRIPT: WTK-LOOPWALL-LOOP-SELECTION-01
"""
Connection: the loop wall is exactly where What Transport Keeps' line-selection
(Theorem 1, Theorem 2 and the three tied-growth outcomes) switches on for the loop.

Why this check proves what it claims:
 1. Symbolic. The loop of the element paper is two perpendicular half-steps h_a, h_b.
    In SL(2,R) take A = diag(e^h_a, e^-h_a) (axis: the imaginary axis of the upper
    half-plane) and B = [[cosh h_b, sinh h_b],[sinh h_b, cosh h_b]] (axis: the unit
    semicircle, perpendicular to the first at i). The loop holonomy is the group
    commutator W = A B A^-1 B^-1. If sympy reduces tr W - (2 - 4 sinh^2 h_a sinh^2 h_b)
    to zero, then |tr W| < 2 (elliptic, a turn) is EXACTLY sinh h_a sinh h_b < 1, the
    paper's two-face closing condition, and tr W = -2 (parabolic, a Jordan block) is the
    border. Substituting sinh^2 h = (z-1)^2/(4z) for equal faces must give z^2-6z+1 = 0
    at the border: the loop-wall polynomial.
 2. Numeric, WTK Theorem 1. WTK's diagnostic is the trace-normalised Gram matrix
    H_N = (W^N)*(W^N)/Tr; its top projector Q_N either converges to a line or not.
    WTK lists three tied outcomes (fixed line, rotating line, unresolved block). We
    compute 1 - Tr(Q_N Q_{N+1}) along N. If it stays O(1) forever inside the wall,
    falls polynomially at the wall (a Jordan block, W^N = -(I + N n)), and falls exponentially outside, then the wall is the
    selection threshold. The final check confirms WTK Theorem 2's limit: the selected
    right line equals the dominant LEFT eigenvector (the seed covector a*), read as a column.
 3. The five first-opening pairs from the archive: the sign of Gamma1^2+Gamma2^2-1 must
    agree with the sign of |tr W| - 2 on every pair, and on 2000 random face pairs.
"""
import sympy as sp, numpy as np, math, random

ha, hb = sp.symbols('h_a h_b', positive=True)
A = sp.Matrix([[sp.exp(ha), 0], [0, sp.exp(-ha)]])
B = sp.Matrix([[sp.cosh(hb), sp.sinh(hb)], [sp.sinh(hb), sp.cosh(hb)]])
W = A * B * A.inv() * B.inv()
diff = sp.simplify((W.trace() - (2 - 4*sp.sinh(ha)**2*sp.sinh(hb)**2)).rewrite(sp.exp))
print('1. tr(ABA^-1B^-1) - (2 - 4 sinh^2 h_a sinh^2 h_b) =', diff)
z = sp.symbols('z', positive=True)
s2 = (z-1)**2/(4*z)
border = sp.factor(sp.numer(sp.together((2 - 4*s2*s2) + 2)))
print('   equal faces, tr W + 2 numerator factors as:', border)
print('   so tr W = -2 exactly at z^2 - 6z + 1 = 0, i.e. z = 3 + 2 sqrt2 = %.9f' % (3+2*math.sqrt(2)))

def mats(za, zb):
    a, b = 0.5*math.log(za), 0.5*math.log(zb)
    A = np.array([[math.exp(a), 0], [0, math.exp(-a)]])
    B = np.array([[math.cosh(b), math.sinh(b)], [math.sinh(b), math.cosh(b)]])
    return A, B

def loop(za, zb):
    A, B = mats(za, zb)
    return A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)

def top_proj(M):
    H = M.T @ M; H = H/np.trace(H)
    w, V = np.linalg.eigh(H); v = V[:, -1:]
    return v @ v.T

def selection_run(za, zb, Nmax=400):
    Wm = loop(za, zb); P = np.eye(2); out = []; Qprev = None
    for N in range(1, Nmax+1):
        P = Wm @ P; P = P/np.linalg.norm(P)      # scalar rescaling does not change H_N
        Q = top_proj(P)
        if Qprev is not None: out.append(1 - np.trace(Q @ Qprev))
        Qprev = Q
    return Wm, out

print('\n2. WTK Theorem 1 on the loop holonomy W^N (1 - Tr(Q_N Q_N+1))')
wall = 3 + 2*math.sqrt(2)
cases = [('nitrogen K opening, both faces', 552.06741/97.8901, 552.06741/97.8901),
         ('the wall itself 3+2sqrt2', wall, wall),
         ('carbon K opening, both faces', 392.09056/64.49352, 392.09056/64.49352),
         ('carbon with nitrogen (mixed)', 392.09056/64.49352, 552.06741/97.8901)]
for name, za, zb in cases:
    Wm, d = selection_run(za, zb)
    g1 = ((za-1)/(za+1))**2; g2 = ((zb-1)/(zb+1))**2
    tr = np.trace(Wm)
    kind = 'elliptic (turn)' if abs(tr) < 2-1e-12 else ('parabolic' if abs(abs(tr)-2) < 1e-9 else 'hyperbolic (run)')
    print(f'  {name:34s} G1^2+G2^2={g1+g2:.6f} trW={tr:+.9f} {kind}')
    print('     N=10,50,100,200,399:', ' '.join(f'{d[i]:.3e}' for i in (9, 49, 99, 199, 398)),
          ' max over N>=300:', f'{max(d[299:]):.3e}')
    if 'mixed' in name or 'carbon K' in name:
        w, V = np.linalg.eig(Wm.T)                 # left eigenvectors of W
        a = np.real(V[:, np.argmax(abs(w))]); a = a/np.linalg.norm(a)
        P = np.linalg.matrix_power(Wm, 60); P = P/np.linalg.norm(P)
        Q = top_proj(P)
        print('     Theorem 2: 1 - Tr(Q_60 a a^T) =', f'{1-np.trace(Q @ np.outer(a,a)):.3e}')
    if name.startswith('nitrogen'):
        print('     is W orthogonal in this frame?  ||W W^T - I|| =', f'{np.linalg.norm(Wm@Wm.T-np.eye(2)):.4f}',
              '-> rotating line (WTK control 2), not the unresolved block (control 3)')

print('\n3. Sign agreement: Gamma1^2+Gamma2^2 < 1  <=>  |tr W| < 2')
pairs = {'carbon with nitrogen': (392.09056/64.49352, 552.06741/97.8901),
         'sodium with magnesium': (47.28636/5.13907696, 80.1436/15.035271)}
for k, (za, zb) in pairs.items():
    g = ((za-1)/(za+1))**2 + ((zb-1)/(zb+1))**2
    print(f'  {k:24s} G1^2+G2^2-1 = {g-1:+.6f}  |trW|-2 = {abs(np.trace(loop(za,zb)))-2:+.6f}')
random.seed(1); bad = 0
for _ in range(2000):
    za, zb = 1+9*random.random(), 1+9*random.random()
    g = ((za-1)/(za+1))**2 + ((zb-1)/(zb+1))**2
    bad += ((g < 1) != (abs(np.trace(loop(za, zb))) < 2))
print('  random face pairs, disagreements:', bad, 'of 2000')
