# SCRIPT: GRAV_RETEST_01
# Fresh, independent re-test of "The Ledger Outlives the Metric" edition 6 (Zenodo 22959910 v4).
# Each check is written from the statement in the paper, not from the shipped scripts.
import numpy as np, sympy as sp, mpmath as mp, json
from scipy.linalg import expm, null_space
from scipy.integrate import quad
from scipy.optimize import brentq
rng = np.random.default_rng(20261101)
OUT = []
def rep(tag, ok, detail):
    OUT.append(dict(tag=tag, result='PASS' if ok else 'FAIL', detail=detail))
    print('%-5s %s  %s' % (tag, 'PASS' if ok else 'FAIL', detail), flush=True)
def crand(*s): return rng.normal(size=s) + 1j*rng.normal(size=s)

# ---------- G1 Theorem 2 example ----------
P0 = np.diag([1., 0.]); D = np.array([[0., 1.], [-1., 0.]]); A = np.array([[0., -1.], [-1., 0.]])
h = 1e-6
Pt = lambda t: expm(t*A) @ P0 @ expm(-t*A)
Dfd = (Pt(h) - Pt(-h))/(2*h)
rep('G1', np.allclose(P0@D + D@P0, D) and abs(np.trace(D@D)/2 + 1) < 1e-12 and np.abs(Dfd - D).max() < 1e-8,
    'P0D+DP0=D, Tr(D^2)/2=%.3f, |dP/dt - D|=%.1e' % (np.trace(D@D).real/2, np.abs(Dfd-D).max()))

# ---------- G2 Theorem 6: tangent space found as the null space of D -> PD+DP-D (not from the proof's block form) ----------
def tangent_basis(P):
    n = P.shape[0]; cols = []
    for idx in range(2*n*n):
        E = np.zeros(2*n*n); E[idx] = 1
        Dm = (E[:n*n] + 1j*E[n*n:]).reshape(n, n)
        L = P@Dm + Dm@P - Dm
        cols.append(np.r_[L.real.ravel(), L.imag.ravel()])
    N = null_space(np.array(cols).T)
    return [(v[:n*n] + 1j*v[n*n:]).reshape(n, n) for v in N.T]
def inertia(Gm, tol=1e-9):
    w = np.linalg.eigvalsh((Gm + Gm.T)/2); s = tol*max(1, np.abs(w).max())
    return int((w > s).sum()), int((w < -s).sum()), int((np.abs(w) <= s).sum())
ok = True; rows = []
for n, k in [(2, 1), (3, 1), (4, 2), (5, 2), (6, 3)]:
    S = crand(n, n); P = S @ np.diag([1.]*k + [0.]*(n-k)) @ np.linalg.inv(S)
    Bs = tangent_basis(P)
    Gm = np.array([[0.5*np.trace(a@b).real for b in Bs] for a in Bs])
    ip = inertia(Gm); exp_ = (2*k*(n-k), 2*k*(n-k), 0)
    rows.append('(n=%d,k=%d) dim %d inertia %s' % (n, k, len(Bs), ip)); ok &= (len(Bs) == 4*k*(n-k) and ip == exp_)
    # opposite: orthogonal projector, Hermitian tangents only
    U = np.linalg.qr(crand(n, n))[0]; Po = U[:, :k] @ U[:, :k].conj().T
    Bh = [b for b in tangent_basis(Po)]
    # Hermitian part of the tangent space: D = D^dagger subspace
    M = np.array([np.r_[(b - b.conj().T).real.ravel(), (b - b.conj().T).imag.ravel()] for b in Bh]).T
    Ncoef = null_space(M); Bher = [sum(c*b for c, b in zip(col, Bh)) for col in Ncoef.T]
    Gh = np.array([[0.5*np.trace(a@b).real for b in Bher] for a in Bher])
    iph = inertia(Gh); ok &= (iph[1] == 0 and iph[2] == 0 and iph[0] == 2*k*(n-k))
    rows.append('  opposite (orthogonal P, Hermitian D) dim %d inertia %s' % (len(Bher), iph))
rep('G2', ok, '; '.join(rows))

# ---------- G3/G4 Theorem 8 and Corollary 9 (mpmath, 40 digits) ----------
mp.mp.dps = 40
def mpc(Mx): return mp.matrix([[mp.mpc(complex(x)) for x in r] for r in Mx])
def mtr(Mx): return sum(Mx[i, i] for i in range(Mx.rows))
n, k = 4, 2
S0, S1, S2 = mpc(crand(n, n)), mpc(crand(n, n)), mpc(crand(n, n))
E = mp.diag([1]*k + [0]*(n-k))
def Pc(t):
    S = S0 + t*S1 + t*t*S2; return S*E*mp.inverse(S)
Pz = Pc(0); Dz = (Pc(mp.mpf('1e-15')) - Pc(mp.mpf('-1e-15')))/mp.mpf('2e-15')
pred = -mp.re(mtr(Dz*Dz))/2
worst = 0
for t in [mp.mpf('1e-6'), mp.mpf('-1e-6')]:
    val = (mp.re(mtr(Pz*Pc(t))) - k)/t**2
    worst = max(worst, abs(val/pred - 1))
rep('G3', worst < 1e-4, 'Re Tr(P0 P(t))-k over t^2 vs -ReTr(D^2)/2 = %s; rel err %.1e' % (mp.nstr(pred, 8), float(worst)))
# G4: negative direction (Theorem 2 example) -> overlap above cap for small t of both signs; opposite: orthogonal curve stays <= k
ov = [np.trace(P0 @ Pt(t)).real for t in (1e-3, -1e-3, 1e-2, -1e-2)]
Uh = 1j*np.array([[0., 1.], [1., 0.]])   # anti-Hermitian generator -> unitary conjugation -> orthogonal projectors
ovo = [np.trace(P0 @ expm(t*Uh) @ P0 @ expm(-t*Uh)).real for t in (1e-3, -1e-3, 1e-2, -1e-2)]
rep('G4', all(x > 1 for x in ov) and all(x <= 1 + 1e-15 for x in ovo),
    'negative direction overlaps-1: %s ; opposite (unitary) overlaps-1: %s' % (['%.3e' % (x-1) for x in ov], ['%.3e' % (x-1) for x in ovo]))

# ---------- G5 Theorem 10 and Corollary 11 ----------
n = 5
Bm = crand(n, n); Bm = Bm + Bm.T
Am = crand(n, n); Am = Am + Am.T; H = np.linalg.solve(Bm, Am)
Cs = [crand(n, n) for _ in range(2)]; Cs = [c + c.T for c in Cs]; Vs = [np.linalg.solve(Bm, c) for c in Cs]
lam, R = np.linalg.eig(H)
R = np.array([R[:, j]/np.sqrt(R[:, j] @ Bm @ R[:, j]) for j in range(n)]).T
L = Bm @ R
sym = max(abs(L[:, m] @ V @ R[:, q] - L[:, q] @ V @ R[:, m]) for V in Vs for m in range(n) for q in range(n))
m_, q_ = 0, 1
u = np.array([(L[:, m_] @ V @ R[:, q_])/(lam[m_] - lam[q_]) for V in Vs])
g = np.array([[(u[a]*u[b]).real for b in range(2)] for a in range(2)])
d_conj = -(np.imag(u[0]*np.conj(u[1])))**2; d_noconj = -(np.imag(u[0]*u[1]))**2
uz = (1+1j)*np.array([1., 2.]); gz = np.array([[(uz[a]*uz[b]).real for b in range(2)] for a in range(2)])
rep('G5', sym < 1e-9 and abs(np.linalg.det(g) - d_conj) < 1e-9*max(1, abs(d_conj)) and np.abs(gz).max() < 1e-15,
    'reciprocity asym %.1e; det g=%.6e, -(Im u1*conj u2)^2=%.6e, -(Im u1 u2)^2=%.6e; phase-aligned form max %.1e'
    % (sym, np.linalg.det(g), d_conj, d_noconj, np.abs(gz).max()))

# ---------- G6 Theorem 16, Corollaries 16A, 16B (exact) ----------
x, y, hh = sp.symbols('x y h', real=True)
z = x + sp.I*y; w = x + sp.I*y**2
Pch = sp.Matrix([[1, w], [z, z*w]])/(1 + z*w)
idem = sp.simplify(Pch*Pch - Pch); trP = sp.simplify(Pch.trace())
Dx, Dy = Pch.diff(x), Pch.diff(y)
def gij(a, b): return sp.simplify(sp.re(sp.expand(sp.simplify((a*b).trace()/2))))
G0 = {k_: sp.simplify(v.subs(x, 0)) for k_, v in {'xx': (Dx*Dx).trace()/2, 'xy': (Dx*Dy).trace()/2, 'yy': (Dy*Dy).trace()/2}.items()}
G0 = {k_: sp.simplify(sp.re(sp.expand(v))) for k_, v in G0.items()}
gxx_ok = sp.simplify(G0['xx'] - 1/(1-y**3)**2) == 0
gyy_ok = sp.simplify(G0['yy'] + 2*y/(1-y**3)**2) == 0
gxy_ok = sp.simplify(G0['xy']) == 0
detg = sp.simplify(G0['xx']*G0['yy'] - G0['xy']**2)
om = sp.simplify(sp.re(sp.expand(sp.simplify((-sp.I*(Pch*(Dx*Dy - Dy*Dx)).trace()).subs(x, 0)))))
om_ok = sp.simplify(om - (1-2*y)/(1-y**3)**2) == 0
detQ = sp.simplify(detg - om**2/4); detQ_ok = sp.simplify(detQ + (1+2*y)**2/(4*(1-y**3)**4)) == 0
Hm = (2 + y/10)*Pch + (5 + y/5)*(sp.eye(2) - Pch)
ev = [sp.simplify(e) for e in Hm.subs(x, 0).eigenvals()]
dPy0 = sp.simplify(Dy.subs({x: 0, y: 0}))
P1 = Pch.subs(x, 0); P2 = Pch.subs({x: 0}).subs(y, y+hh)
excess = sp.simplify(sp.re(sp.expand(sp.simplify((P1*P2).trace()))) - 1)
ex_ok = sp.simplify(excess - hh**2*(2*y+hh)/((1-y**3)*(1-(y+hh)**3))) == 0
special = sp.nsimplify(excess.subs({y: sp.Rational(-1, 10), hh: sp.Rational(1, 4)}))
# contour quadrature, independent of the closed forms
def Pnum(yv): zz = 1j*yv; ww = 1j*yv**2; return np.array([[1, ww], [zz, zz*ww]])/(1+zz*ww)
qerr = 0
for yv in (-0.2, -0.1, 0.0, 0.1, 0.2):
    Pn = Pnum(yv); Hn = (2+yv/10)*Pn + (5+yv/5)*(np.eye(2)-Pn)
    th = 2*np.pi*np.arange(256)/256; zc = 2 + 0.4*np.exp(1j*th); dz = 0.4j*np.exp(1j*th)*(2*np.pi/256)
    Rtr = np.array([np.trace(np.linalg.inv(zc_*np.eye(2) - Hn)) for zc_ in zc])
    Nn = (Rtr*dz).sum()/(2j*np.pi); Zn = (np.log(zc)*Rtr*dz).sum()/(2j*np.pi)
    qerr = max(qerr, abs(Nn-1), abs(Zn - np.log(2+yv/10)))
okG6 = (idem == sp.zeros(2) and trP == 1 and gxx_ok and gyy_ok and gxy_ok and om_ok and detQ_ok and ex_ok
        and special == sp.Rational(25000, 7980973) and dPy0 == sp.Matrix([[0, 0], [sp.I, 0]]) and (dPy0*dPy0) == sp.zeros(2) and qerr < 1e-10)
rep('G6', okG6, 'P^2=P %s, TrP=%s, g_xx/g_yy/g_xy %s/%s/%s, det g=%s, omega %s, detQhat %s, eig(H|x=0)=%s, dP_y(0,0)=%s, overlap formula %s, special=%s, contour err %.1e'
    % (idem == sp.zeros(2), trP, gxx_ok, gyy_ok, gxy_ok, detg, om_ok, detQ_ok, ev, dPy0.tolist(), ex_ok, special, qerr))

# ---------- G7 Proposition 15 ----------
lam0 = np.array([2, 3, 20, -20, 35, -35.]); p = np.array([1, 1, 0, 0, 0, 0.])
def herm(n): M = crand(n, n); return (M + M.conj().T)/2
Bh = [herm(6) for _ in range(2)]; Sa = [herm(6)*1j for _ in range(2)]
def DV(V): Dm = np.zeros((6, 6), complex); [Dm.__setitem__((m, q), (p[m]-p[q])/(lam0[m]-lam0[q])*V[m, q]) for m in range(6) for q in range(6) if m != q]; return Dm
def riesz_fd(V, hs=1e-6):
    def Pr(t):
        w, U = np.linalg.eig(np.diag(lam0) + t*V); sel = np.argsort(np.abs(w - 2.5))[:2]
        Ui = np.linalg.inv(U); return U[:, sel] @ Ui[sel, :]
    return (Pr(hs) - Pr(-hs))/(2*hs)
fd_err = max(np.abs(riesz_fd(V) - DV(V)).max() for V in Bh + Sa)
Ai = [DV(b) for b in Bh]; Ci = [DV(s) for s in Sa]
GH = np.array([[np.trace(a@b).real/2 for b in Ai] for a in Ai]); GA = np.array([[-np.trace(a@b).real/2 for b in Ci] for a in Ci])
cross = max(abs(np.trace(a@c).real) for a in Ai for c in Ci)
gk_err = 0
for kap in (0.1, 0.6, 1.3):
    Dk = [a + kap*c for a, c in zip(Ai, Ci)]
    gk = np.array([[np.trace(a@b).real/2 for b in Dk] for a in Dk]); gk_err = max(gk_err, np.abs(gk - (GH - kap**2*GA)).max())
rep('G7', fd_err < 1e-6 and cross < 1e-12 and gk_err < 1e-12 and min(np.linalg.eigvalsh(GH)) >= -1e-14 and min(np.linalg.eigvalsh(GA)) >= -1e-14,
    'entry formula vs finite-difference Riesz %.1e; cross terms %.1e; g(kappa)-(GH-kappa^2 GA) %.1e; eig GH %s, GA %s'
    % (fd_err, cross, gk_err, np.round(np.linalg.eigvalsh(GH), 6), np.round(np.linalg.eigvalsh(GA), 6)))

# ---------- G8 Proposition 14 ----------
m = 4; lamJ = 0.7+0.2j; J = lamJ*np.eye(m) + np.diag(np.ones(m-1), 1)
trJ = abs(np.trace(expm(J)) - m*np.exp(lamJ))
t = 0.01; Jt = np.array([[2, 1], [t, 2.]])
th = 2*np.pi*np.arange(512)/512; zc = 2 + 1.0*np.exp(1j*th); dz = 1j*np.exp(1j*th)*(2*np.pi/512)
Zt = sum(np.log(zz)*np.trace(np.linalg.inv(zz*np.eye(2) - Jt))*d for zz, d in zip(zc, dz))/(2j*np.pi)
mu_, eps_ = 0.3, 0.02; sep = np.ptp(np.linalg.eigvals(np.array([[0, mu_], [eps_, 0]])).real)
rep('G8', trJ < 1e-12 and abs(Zt - np.log(4-t)) < 1e-12 and abs(sep - 2*np.sqrt(mu_*eps_)) < 1e-12,
    '|Tr e^J - m e^lam| %.1e; J_t contour trace-log err %.1e; separation %.6f vs 2sqrt(mu eps) %.6f' % (trJ, abs(Zt-np.log(4-t)), sep, 2*np.sqrt(mu_*eps_)))

# ---------- G9 Proposition 20 ----------
ok = True; rr = []
for d in range(3, 13):
    om_ = np.exp(2j*np.pi/d); Uc = np.diag(om_**np.arange(d)); Vs_ = np.roll(np.eye(d), 1, axis=0)
    if not np.allclose(Uc@Vs_, om_*Vs_@Uc):
        Uc, Vs_ = Vs_, Uc   # use whichever order satisfies UV = e^{2pi i/d} VU
    Rr = Uc@Vs_@Uc.conj().T@Vs_.conj().T
    wv = np.angle(np.linalg.eigvals(Rr)).sum()/(2*np.pi); dl = np.linalg.norm(Rr - np.eye(d))**2/d
    ok &= np.allclose(Rr, om_*np.eye(d)) and abs(wv-1) < 1e-12 and abs(dl - 4*np.sin(np.pi/d)**2) < 1e-12
    rr.append('%d:%.4f' % (d, dl))
rep('G9', ok, 'R = e^{2pi i/d} I, w=1, delta = 4 sin^2(pi/d): ' + ' '.join(rr))

# ---------- G10 Proposition 22 ----------
yy = sp.symbols('y')
p1 = (20+yy)/(70+3*yy); p2 = (50+2*yy)/(70+3*yy)
Drel = p1*sp.log(p1/p1.subs(yy, 0)) + p2*sp.log(p2/p2.subs(yy, 0))
ser = sp.series(Drel, yy, 0, 3).removeO()
fisher = sp.simplify(sp.diff(p1, yy).subs(yy, 0)**2*(1/p1.subs(yy, 0) + 1/p2.subs(yy, 0)))
Zinc = sp.series(sp.log(2+yy/10) - sp.log(2), yy, 0, 2).removeO()
rep('G10', sp.simplify(ser - yy**2/98000) == 0 and fisher == sp.Rational(1, 49000) and sp.simplify(Zinc - yy/20) == 0 and sp.diff(p1, yy).subs(yy, 0) == sp.Rational(1, 490),
    'D series %s, Fisher %s, p1\'(0) %s, Z increment %s' % (ser, fisher, sp.diff(p1, yy).subs(yy, 0), Zinc))

# ---------- G11 Proposition 23 ----------
b, Rs, lP, Gn = sp.symbols('beta R l_P G', positive=True)
expr = -sp.log(1-b*Rs) - 4*sp.log(1-b*Rs/4) - 6*sp.log(1-b*Rs/6)
s2 = sp.expand(sp.series(expr, b, 0, 3).removeO())
coef = sp.simplify((3*b*Rs).subs(b, lP**2/(48*sp.pi))/lP**4).subs(lP, sp.sqrt(Gn))
rep('G11', sp.simplify(s2 - (3*b*Rs + sp.Rational(17, 24)*b**2*Rs**2)) == 0 and sp.simplify(coef - Rs/(16*sp.pi*Gn)) == 0,
    'series %s ; leading l_P^-4 * 3 beta R = %s' % (s2, coef))

# ---------- G12 Proposition 24 and the Section 14 table ----------
def fp(tv, pp):
    return (pp+1)*tv**(pp+1)*quad(lambda uu: uu**(pp+1)/np.expm1(uu) if uu > 0 else (0.0 if pp > 0 else 1.0), 0, 1/tv, limit=400)[0]
lim_ok = True; lim_rows = []
for pp in (0, 1, 2):
    small = fp(1e-3, pp)/((pp+1)*float(sp.gamma(pp+2)*sp.zeta(pp+2))*1e-3**(pp+1)); large = fp(1e4, pp)
    lim_ok &= abs(small-1) < 1e-6 and abs(large-1) < 1e-3; lim_rows.append('p=%d small-ratio %.8f large %.6f' % (pp, small, large))
aD = np.pi**2/6   # a0 = 1
def accel(aN): return brentq(lambda a: a*fp(a/aD, 0) - aN, 1e-12, aN + aD)
rar = lambda aN: aN/(1-np.exp(-np.sqrt(aN)))
table = {1e-4: (0.010000, 0.010050, -0.00217), 1e-2: (0.100000, 0.105083, -0.02153), 0.1: (0.319738, 0.368859, -0.06207),
         1: (1.356625, 1.581977, -0.06674), 10: (10.40401, 10.44200, -0.00158), 100: (100.4105, 100.0045, +0.00176)}
tab_ok = True; trows = []
for aN, (aa, ar, dx) in table.items():
    a_ = accel(aN); dex = np.log10(a_/rar(aN))
    ok_ = abs(a_/aa-1) < 2e-6 and abs(rar(aN)/ar-1) < 2e-6 and abs(dex-dx) < 1e-5
    tab_ok &= ok_; trows.append('%g: %.6f %.6f %+.5f %s' % (aN, a_, rar(aN), dex, '' if ok_ else '<-MISS'))
grid = np.logspace(-4, 4, 801); dexs = np.array([np.log10(accel(v)/rar(v)) for v in grid]); i = np.argmax(np.abs(dexs))
a0 = 1.2e-10; hbar, c, kB = 1.054571817e-34, 2.99792458e8, 1.380649e-23
aDs = np.pi**2*a0/6; TD = hbar*aDs/(2*np.pi*c*kB)
sweep_ok = abs(abs(dexs[i]) - 0.07954) < 5e-6 and abs(grid[i] - 0.372) < 0.005
rep('G12', lim_ok and tab_ok and sweep_ok and abs(aDs/4 - 4.93e-11) < 5e-14 and abs(TD - 8.00e-31) < 5e-33,
    '%s | table: %s | sweep max |dex| %.5f at aN/a0=%.4f | offset aD/4 %.3e | T_D %.3e K' % ('; '.join(lim_rows), '; '.join(trows), abs(dexs[i]), grid[i], aDs/4, TD))

# ---------- G13 Proposition 25 ----------
def fm(tv, mm): j = np.arange(1, mm+1); uu = (j-0.5)/(mm*tv); return np.mean(uu/np.expm1(uu))
r1, r2, r3 = fm(0.01, 10)/fp(0.01, 0), fm(0.01, 100)/fp(0.01, 0), fm(0.001, 100)/fp(0.001, 0)
rep('G13', abs(r1-0.20623) < 5e-6 and abs(r2-0.98734) < 5e-6 and abs(r3-0.20623) < 5e-6, 'f10/finf(0.01)=%.5f f100/finf(0.01)=%.5f f100/finf(0.001)=%.5f' % (r1, r2, r3))

# ---------- G14 Theorem 26 (with a Jordan-block cluster), opposite on K=K^dagger>0 ----------
def contour_Z(K, c0, rad, M=600):
    th = 2*np.pi*np.arange(M)/M; zc = c0 + rad*np.exp(1j*th); dz = 1j*rad*np.exp(1j*th)*(2*np.pi/M)
    n = K.shape[0]; Zs = 0; Pm = np.zeros((n, n), complex)
    for zz, d in zip(zc, dz):
        Rz = np.linalg.inv(zz*np.eye(n) - K); Zs += np.log(zz)*np.trace(Rz)*d; Pm += Rz*d
    return Zs/(2j*np.pi), Pm/(2j*np.pi)
worst = 0
for trial in range(4):
    n = 5
    if trial < 2:
        J = np.diag([3.0, 3.0, 7.0, 9.0, 11.0]).astype(complex); J[0, 1] = 1.0   # Jordan block at 3
    else:
        J = np.diag([3.0+0.3j, 3.4-0.2j, 7.0, 9.0+1j, 11.0])
    Sm = crand(n, n); K = Sm @ J @ np.linalg.inv(Sm); Bsrc = crand(n, n)
    _, Pc_ = contour_Z(K, 3.2, 1.5); pred = np.trace(Pc_ @ np.linalg.inv(K) @ Bsrc)
    hs = 1e-5; fd = (contour_Z(K + hs*Bsrc, 3.2, 1.5)[0] - contour_Z(K - hs*Bsrc, 3.2, 1.5)[0])/(2*hs)
    worst = max(worst, abs(fd - pred)/abs(pred))
Uq = np.linalg.qr(crand(6, 6))[0]; Kp = Uq @ np.diag([1.0, 1.5, 2.0, 6.0, 7.0, 8.0]) @ Uq.conj().T
_, Pp = contour_Z(Kp, 1.5, 0.9); Ap = Pp @ np.linalg.inv(Kp)
qmin = min((bb.conj() @ Ap @ bb).real for bb in (crand(6) for _ in range(2000)))
rep('G14', worst < 1e-7 and qmin >= -1e-12, 'finite-difference vs Tr(P K^-1 B), worst rel err %.1e (2 Jordan, 2 generic); opposite K=K^dag>0: min q over 2000 sources %.3e' % (worst, qmin))

# ---------- G15 Corollaries 27-28 and Counterexample 29 ----------
def q_meas(bb, hs=1e-5):   # measured as a finite-difference derivative of Z_C, independent of the formula
    Bb = np.outer(bb, bb.conj()); return ((contour_Z(Kp + hs*Bb, 1.5, 0.9)[0] - contour_Z(Kp - hs*Bb, 1.5, 0.9)[0])/(2*hs)).real
Erec = np.zeros((6, 6), complex); e = np.eye(6)
qd = [q_meas(e[i]) for i in range(6)]
for i in range(6):
    Erec[i, i] = qd[i]
    for j in range(i+1, 6):
        re_ = (q_meas(e[i]+e[j]) - qd[i] - qd[j])/2; im_ = -(q_meas(e[i]+1j*e[j]) - qd[i] - qd[j])/2
        Erec[i, j] = re_ + 1j*im_; Erec[j, i] = np.conj(Erec[i, j])
tom = np.abs(Erec - Ap).max()
wv, Uv = np.linalg.eigh(Erec); supp = Uv[:, wv > 1e-6] @ Uv[:, wv > 1e-6].conj().T
null_ok = all(abs((v.conj() @ Ap @ v)) < 1e-10 for v in null_space(Pp).T)
Kc = np.array([[2., 9.], [0., 5.]]); _, Pcx = contour_Z(Kc, 2.0, 1.0); bc = np.array([1., 1.])
val = bc @ Pcx @ np.linalg.inv(Kc) @ bc
lam_t = lambda tt: min(np.linalg.eigvals(Kc + tt*np.outer(bc, bc)), key=lambda v: abs(v-2))
dlam = (lam_t(1e-6) - lam_t(-1e-6))/2e-6
rep('G15', tom < 1e-7 and np.abs(supp - Pp).max() < 1e-7 and null_ok and abs(val + 1) < 1e-10 and abs(dlam + 2) < 1e-6 and np.allclose(Pcx, [[1, -3], [0, 0]]),
    'tomography from measured derivatives err %.1e; support vs P_C %.1e; nullspace silent %s; oblique b^dag P K^-1 b = %.6f, eigen-derivative %.6f, P_C=%s'
    % (tom, np.abs(supp - Pp).max(), null_ok, val.real, dlam.real, np.round(Pcx.real, 6).tolist()))

# ---------- G16 Proposition 30 ----------
al = 2.7; K = Sm @ np.diag([3.0+0.3j, 3.4-0.2j, 7.0, 9.0+1j, 11.0]) @ np.linalg.inv(Sm)
Z1, P1n = contour_Z(K, 3.2, 1.5); Z2, P2n = contour_Z(al*K, al*3.2, al*1.5)
Bsrc = crand(5, 5)
d1 = np.trace(P1n @ np.linalg.inv(K) @ Bsrc); d2 = np.trace(P2n @ np.linalg.inv(al*K) @ Bsrc)
rep('G16', np.abs(P1n - P2n).max() < 1e-10 and abs(Z2 - Z1 - 2*np.log(al)) < 1e-10 and abs(d2*al - d1) < 1e-10,
    'P unchanged %.1e; Z shift - k log alpha %.1e; derivative x alpha - original %.1e' % (np.abs(P1n-P2n).max(), abs(Z2-Z1-2*np.log(al)), abs(d2*al-d1)))

# ---------- G17 Section 17 lapse curvature ----------
tt, xx = sp.symbols('t x'); Nf = sp.Function('N')(xx); coords = [tt, xx]
gm = sp.diag(-Nf**2, 1); gi = gm.inv()
Gam = [[[sum(gi[a, d]*(sp.diff(gm[d, b], coords[c]) + sp.diff(gm[d, c], coords[b]) - sp.diff(gm[b, c], coords[d])) for d in range(2))/2 for c in range(2)] for b in range(2)] for a in range(2)]
def Ric(b, c): return sp.simplify(sum(sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c]) + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(2)) for a in range(2)))
Rsc = sp.simplify(sum(gi[b, c]*Ric(b, c) for b in range(2) for c in range(2)))
rep('G17', sp.simplify(Rsc + 2*sp.diff(Nf, xx, 2)/Nf) == 0, 'Ricci scalar = %s (convention R^a_{bcd} = d_c Gamma^a_{bd} - ...)' % Rsc)

# ---------- G18 Theorem 3 and Proposition 4 ----------
bad = 0
for _ in range(20000):
    a_, b_, c_, o_ = rng.normal(size=4)
    psd = np.linalg.eigvalsh(np.array([[a_, b_+1j*o_/2], [b_-1j*o_/2, c_]])).min() >= -1e-12
    crit = a_ >= 0 and c_ >= 0 and 4*(a_*c_ - b_**2) >= o_**2 - 1e-12
    bad += psd != crit
ce = np.diag([0., -1.])
Hh = herm(5); wv, Uv = np.linalg.eigh(Hh); Vp = herm(5); Vm = Uv.conj().T @ Vp @ Uv
rt = min((Vm[m, q]*Vm[q, m]).real/(wv[m]-wv[q])**2 for m in range(5) for q in range(5) if m != q)
rti = max(abs((Vm[m, q]*Vm[q, m]).imag) for m in range(5) for q in range(5) if m != q)
rep('G18', bad == 0 and np.linalg.det(ce) == 0 and np.linalg.eigvalsh(ce).min() < 0 and rt >= 0 and rti < 1e-12,
    'criterion vs eigenvalues mismatches %d/20000; diag(0,-1) det 0, min eig -1; Hermitian round trip min %.3e, max imag %.1e' % (bad, rt, rti))

json.dump(OUT, open('grav_retest_01.json', 'w'), indent=1)
print('\nSUMMARY'); [print('%-5s %s' % (o['tag'], o['result'])) for o in OUT]
