# SCRIPT: NONRIEMANN-WHERE-01
# Where does "non-Riemannian" belong in Jeromie's corpus? Every claim re-checked a new way.
import numpy as np, mpmath as mp
rng = np.random.default_rng(20261122)
out = []
def rep(tag, msg): out.append(f"[{tag}] {msg}"); print(out[-1])

# ---------- C1. Hermitian intrinsic g is Riemannian (positive definite) ----------
# Why it proves it: a metric is Riemannian iff g(V,V)>0 for every nonzero tangent V.
# New way: build tangent vectors as i[A,P] from random Hermitian A (not from blocks), then compare
# g(V,V)=1/2 Tr(V^2) against ||X||^2 and against the smallest eigenvalue of the full Gram on a random 6-vector basis.
worst = np.inf; minEig = np.inf
for trial in range(300):
    n = rng.integers(3, 9); k = rng.integers(1, n)
    U = np.linalg.qr(rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n)))[0]
    P = U[:, :k] @ U[:, :k].conj().T
    Vs = []
    for _ in range(6):
        A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n)); A = A + A.conj().T
        Vs.append(1j*(A@P - P@A))
    G = np.array([[0.5*np.trace(a@b).real for b in Vs] for a in Vs])
    X = P @ Vs[0] @ (np.eye(n)-P)
    worst = min(worst, (0.5*np.trace(Vs[0]@Vs[0]).real) / np.linalg.norm(X)**2)
    dimT = 2*k*(n-k)
    ev = np.linalg.eigvalsh(G)
    if dimT >= 6: minEig = min(minEig, ev.min())
rep("C1", f"g(V,V)/||X||^2 min over 300 = {worst:.12f} (Riemannian needs >0; theory 1); "
          f"smallest Gram eigenvalue when 6 <= dim = {minEig:.3e} (>0 => positive definite)")

# ---------- C1b. Its Riemannian curvature is ordinary and finite ----------
# Why: on CP^1 with g = 1/4 round metric the sphere has radius 1/2, Gaussian curvature 4.
# New way: compute curvature numerically from the metric in (theta,phi) by the Brioschi-type formula.
def gauss_K(th, h=1e-4):
    E = lambda t: 0.25; G = lambda t: 0.25*np.sin(t)**2
    # K = -1/(2 sqrt(EG)) d/dtheta( G_theta / sqrt(EG) ) for metric E dth^2 + G dphi^2
    f = lambda t: (G(t+h)-G(t-h))/(2*h)/np.sqrt(E(t)*G(t))
    return -1/(2*np.sqrt(E(th)*G(th)))*(f(th+h)-f(th-h))/(2*h)
rep("C1b", f"Gaussian curvature of the intrinsic metric on CP^1 at theta=0.7,1.2,2.0: "
           f"{gauss_K(0.7):.6f}, {gauss_K(1.2):.6f}, {gauss_K(2.0):.6f} (Riemannian, = 4)")
# Berry curvature is a different object: Omega_thph = 1/2 sin th, a 2-form; K is a scalar 4.
rep("C1c", "Berry 2-form Omega = (1/2) sin(th) dth^dph = 2 x area form of g; it is the Kaehler form, not the Riemann tensor of g")

# ---------- C2. The trace-log ledger is the non-Riemannian object ----------
# Why: a Riemannian distance is additive along a geodesic, d(a,c)=d(a,b)+d(b,c).
# Atlas B15 claims sqrt(S) is locally d_R/(2 sqrt 2) but not additive. New way: scalar intensities,
# exact closed form S = log cosh(1/2 ln(I/J)) = -1/2 ln(1-Gamma^2), Gamma=(I-J)/(I+J) = tanh(1/2 ln(I/J)).
mp.mp.dps = 40
def S_ld(I, J): return mp.log((I+J)/2) - mp.log(I)/2 - mp.log(J)/2
for I, J in [(3, 1), (mp.mpf(3)+2*mp.sqrt(2), 1), (17, 2)]:
    G = (I-J)/(I+J)
    rep("C2a", f"I/J={mp.nstr(I/J,10)}: logdet S={mp.nstr(S_ld(I,J),20)}, logcosh={mp.nstr(mp.log(mp.cosh(mp.log(I/J)/2)),20)}, "
               f"-1/2 ln(1-Gamma^2)={mp.nstr(-mp.log(1-G**2)/2,20)}, Gamma={mp.nstr(G,12)}")
zw = 3+2*mp.sqrt(2)
rep("C2b", f"at the peel wall z=3+2sqrt2: Gamma^2={mp.nstr(((zw-1)/(zw+1))**2,20)}, ledger S={mp.nstr(S_ld(zw,1),20)} = 1/2 ln 2 = {mp.nstr(mp.log(2)/2,20)}")
# local constant and non-additivity along the geodesic ln I in [0, L] cut into N equal steps
for L in [1, 2, 4, 6, 8]:
    N = 4000
    acc = sum(mp.sqrt(S_ld(mp.e**(L*(i+1)/N), mp.e**(L*i/N))) for i in range(N))
    direct = mp.sqrt(S_ld(mp.e**L, 1))
    rep("C2c", f"ln contrast {L}: accumulated/direct sqrt(S) = {mp.nstr(acc/direct,6)}  (Riemannian d_R gives exactly 1)")
rep("C2d", f"local ratio sqrt(S)/d_R at d_R=1e-6: {mp.nstr(mp.sqrt(S_ld(mp.e**mp.mpf('1e-6'),1))/mp.mpf('1e-6'),12)} vs 1/(2sqrt2)={mp.nstr(1/(2*mp.sqrt(2)),12)}")

# ---------- C2e. matrix version (reproduce Atlas B15 numbers a different way) ----------
# Affine-invariant geodesic A(t)=A^1/2 (A^-1/2 B A^-1/2)^t A^1/2 between rigidity operators with contrast kappa.
def ld(M): return np.linalg.slogdet(M)[1]
def Sm(A, B): return ld((A+B)/2) - ld(A)/2 - ld(B)/2
def powh(M, t):
    w, V = np.linalg.eigh(M); return (V*w**t) @ V.T
for lk in [1, 2, 4, 6, 8]:
    d = 4
    Q = np.linalg.qr(rng.normal(size=(d,d)))[0]
    A = np.eye(d); B = Q @ np.diag(np.exp(np.linspace(0, lk, d))) @ Q.T
    N = 3000
    pts = [powh(B, t) for t in np.linspace(0, 1, N+1)]
    acc = sum(np.sqrt(Sm(pts[i], pts[i+1])) for i in range(N))
    dR = np.sqrt(np.sum(np.linspace(0, lk, d)**2))
    rep("C2e", f"4x4, eigen-contrast up to e^{lk}: accumulated/direct = {acc/np.sqrt(Sm(A,B)):.4f}; Riemannian (affine-invariant) control "
               f"{sum(np.sqrt(np.sum(np.log(np.linalg.eigvalsh(np.linalg.solve(pts[i], pts[i+1])))**2)) for i in range(0,N,1))/dR:.6f}")

# ---------- C3. Non-Hermitian: the biorthogonal metric goes indefinite ----------
# Why: Riemannian requires det g > 0 in 2D; a negative determinant means one timelike and one spacelike direction.
# New way: biorthogonal projector by contour-free eigen decomposition, finite differences in (Re z, Im z) directions.
def biproj(H, which=0):
    w, R = np.linalg.eig(H); Linv = np.linalg.inv(R)
    i = np.argsort(w.real)[which]
    return np.outer(R[:, i], Linv[i, :])
for z in [0.7+0.3j, -0.4+0.9j, 1.3-0.2j]:
    h = 1e-5
    H = lambda zz: np.array([[0, 1], [zz, 0]], dtype=complex)
    P0 = biproj(H(z))
    dirs = [1, 1j]
    dP = [(biproj(H(z+h*d)) - biproj(H(z-h*d)))/(2*h) for d in dirs]
    Q = np.array([[np.trace(P0 @ dP[a] @ dP[b]) for b in range(2)] for a in range(2)])
    pred = (1/(16*z**2))*np.array([[-1, -1j], [-1j, 1]])
    g = (Q + Q.T)/2; Om = (Q - Q.T)
    rep("C3", f"z={z}: |Q - (1/16z^2)[[-1,-i],[-i,1]]| = {np.abs(Q-pred).max():.1e}; antisym part {np.abs(Om).max():.1e}; "
              f"det(Re g) = {np.linalg.det(g.real):.4e}, -|1/16z^2|^2 = {-abs(1/(16*z**2))**2:.4e}")
# Hermitian control: z real positive -> H Hermitian only if z=1; use Hermitian family d.sigma instead
sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.diag([1,-1])
def Hd(dx, dy, dz): return dx*sx+dy*sy+dz*sz
h = 1e-5; d0 = (2.0, 0.0, 0.4)
P0 = biproj(Hd(*d0))
dP = [(biproj(Hd(d0[0]+h, d0[1], d0[2])) - biproj(Hd(d0[0]-h, d0[1], d0[2])))/(2*h),
      (biproj(Hd(d0[0], d0[1]+h, d0[2])) - biproj(Hd(d0[0], d0[1]-h, d0[2])))/(2*h)]
Q = np.array([[np.trace(P0 @ dP[a] @ dP[b]) for b in range(2)] for a in range(2)])
rep("C3ctl", f"Hermitian point d=(2,0,0.4): det Re Q_sym = {np.linalg.det(((Q+Q.T)/2).real):.4e} (>0, Riemannian)")
# cone-paper point d=(2,0,0.4+0.6i): signature of Re Q_sym
d1 = (2.0, 0.0, 0.4+0.6j)
P0 = biproj(Hd(*d1))
dP = [(biproj(Hd(d1[0]+h, d1[1], d1[2])) - biproj(Hd(d1[0]-h, d1[1], d1[2])))/(2*h),
      (biproj(Hd(d1[0], d1[1]+h, d1[2])) - biproj(Hd(d1[0], d1[1]-h, d1[2])))/(2*h)]
Q = np.array([[np.trace(P0 @ dP[a] @ dP[b]) for b in range(2)] for a in range(2)])
ev = np.linalg.eigvalsh(((Q+Q.T)/2).real)
th = np.linspace(0, np.pi, 200001); q = np.array([np.cos(th), np.sin(th)])
form = np.einsum('ik,ij,jk->k', q, ((Q+Q.T)/2).real, q)
zer = th[np.where(np.diff(np.sign(form)))[0]]*180/np.pi
rep("C3cone", f"cone point d=(2,0,0.4+0.6i): eigenvalues of Re g = {ev[0]:.4e}, {ev[1]:.4e} (one negative => Lorentzian); "
              f"null directions at {', '.join(f'{x:.3f}' for x in zer)} deg (cone paper metric quadrature: 7.963/172.037)")

# ---------- C4. The peel step is a Lorentz boost; the wall is a null rotation ----------
# Why: B = exp(r/2 a.sigma) is Hermitian with det 1, so X -> B X B^dagger preserves det X = t^2-x^2-y^2-z^2,
# the Minkowski form (signature +,-,-,-), which is not Riemannian. Its 4x4 image Lambda satisfies Lambda^T eta Lambda = eta.
# At the wall W = Bi Bj Bi^-1 Bj^-1 has trace -2 and W+1 nilpotent: -W is parabolic, i.e. a NULL rotation fixing a lightlike vector.
pauli = [np.eye(2), sx, sy, sz]; eta = np.diag([1, -1, -1, -1])
def lorentz(M):
    return np.array([[0.5*np.trace(pauli[a] @ M @ pauli[b] @ M.conj().T).real for b in range(4)] for a in range(4)])
def expm2(r, a):  # exp(r/2 a.sigma) for unit a
    A = a[0]*sx + a[1]*sy + a[2]*sz
    return np.cosh(r/2)*np.eye(2) + np.sinh(r/2)*A
for G2 in [0.3, 0.5, 0.7]:
    Gm = np.sqrt(G2); z = (1+Gm)/(1-Gm); r = np.log(z)
    Bi = expm2(r, (1, 0, 0)); Bj = expm2(r, (0, 1, 0))
    W = Bi @ Bj @ np.linalg.inv(Bi) @ np.linalg.inv(Bj)
    L = lorentz(W)
    lor = np.abs(L.T @ eta @ L - eta).max()
    RT = G2/(1-G2)
    msg = f"Gamma^2={G2}: tr W={np.trace(W).real:+.12f} (formula 2-4(R/T)^2 = {2-4*RT**2:+.12f}); Lambda^T eta Lambda - eta = {lor:.1e}"
    if abs(G2-0.5) < 1e-12:
        N1 = W + np.eye(2)
        Lm = L - np.eye(4)
        Vt = np.linalg.svd(Lm)[2]; K2 = Vt[-2:].T  # 2-dim kernel of Lambda-1
        Mq = K2.T @ eta @ K2; wq, vq = np.linalg.eigh(Mq)
        # pick combination with eta-norm 0 inside the kernel (Mq is singular-indefinite: one zero eigenvalue)
        fixed = K2 @ vq[:, np.argmin(np.abs(wq))]; fixed = fixed/np.abs(fixed).max()
        ker_dim = int(np.sum(np.linalg.svd(Lm)[1] < 1e-6))
        msg += (f"; (W+1)^2 = {np.abs(N1@N1).max():.1e}, W+1 = {np.abs(N1).max():.3f} != 0; "
                f"(Lambda-1)^3 = {np.abs(np.linalg.matrix_power(Lm,3)).max():.1e}; fixed vector {np.round(fixed,6)} "
                f"has Minkowski norm {fixed@eta@fixed:.1e} (lightlike); kernel dim of Lambda-1 = {ker_dim}")
    else:
        w = np.linalg.eigvals(L)
        msg += f"; Lorentz eigenvalues {np.round(w,6)}"
    rep("C4", msg)

# ---------- C5. Pullback (fold) degenerates while the intrinsic g stays 1 ----------
# Why: Riemannian needs nondegenerate; a pullback with det g -> 0 at open gap is a degenerate (Carrollian-type) metric
# that is no longer Riemannian there, while the tensor upstairs never degenerates.
def Pfold(x, y):
    th, ph = y + 1.1, x**2/2
    n = np.array([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)])
    return 0.5*(np.eye(2) - (n[0]*sx + n[1]*sy + n[2]*sz))
for x in [0.6, 0.2, 0.05, 0.0]:
    h = 1e-6
    Vx = (Pfold(x+h, 0) - Pfold(x-h, 0))/(2*h); Vy = (Pfold(x, h) - Pfold(x, -h))/(2*h)
    g = np.array([[0.5*np.trace(a@b).real for b in (Vx, Vy)] for a in (Vx, Vy)])
    rep("C5", f"fold x={x}: det(pullback g) = {np.linalg.det(g):.4e}; intrinsic g on unit X = 1 by C1")
open('/home/claude/nr/nonriemann_checks_output.txt', 'w').write("\n".join(out))
