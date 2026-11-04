# SCRIPT: s13_v4_bridges
# Checks every new statement that enters Matter, Then On Down v4.
# Each block states what it proves and its kill line, written before the run.
#
# K1 joint offset example: two projectors with equal census, equal offset and
#    equal generator coupling saturate tau'^2 = 4 g S while their offsets move
#    in opposite directions. KILL: saturation error > 1e-10 anywhere, or the
#    bound written with the cross weight Tr X in place of E_H is NOT violated
#    for omega >= 1 (then the two objects could be the same and the text is wrong).
# K2 metric signature of the opened SSH plane: det Q = -u^2 w^2 cos^2 k/(16 s^3).
#    Symbolic identity in sympy, plus 2000 random eigenvector evaluations.
#    KILL: sympy residual not identically 0, or scaled numeric error > 1e-9.
# K3 branch of the continued endpoint offset: tau_end = 2 artanh(i g) = 2 i arctan g,
#    Gamma_end = i g, Kbar = 1 + g^2 = sec^2(Im tau_end / 2). KILL: any error > 1e-12,
#    or |Gamma_end| != 1 at g = 1, or tau_end not finite at g = 1.
# K4 fermion record of a Hawking pair: tau = omega/T, Gamma = tanh(omega/2T) for every
#    pair phase (partial trace of the two-mode pure state). KILL: error > 1e-12.
# K5 a step in spectral gap reflects with the peel coordinate:
#    Gamma = (Y1-Y2)/(Y1+Y2), Y = sqrt(g_par), g_par ~ 1/Delta^2  =>  tanh(ln(D2/D1)/2).
#    Checked against a direct transfer-matrix solution of the 1D wave equation on a step.
#    KILL: error > 1e-10.
# K6 complement parity: nu -> 1-nu sends Gamma, tau to minus themselves and keeps nu(1-nu);
#    P -> I-P, V,W -> -V,-W conjugates Q = Tr(P V W): metric even, curvature odd.
#    KILL: error > 1e-12 on 200 random cases.
# K7 resolvent under adjoint: R_{H*}(z) = R_H(conj z)^*, and R_{H*}(z) != -R_H(z) in general.
#    KILL: first identity error > 1e-12, or the minus-sign law holds on the random control.
# K8 angular chain ANG1-ANG4 (L = -i k M - kappa (I - P0)):
#    ANG1 Z_b(0+) = 2k/pi; ANG2 isolated pole s* = k cot(k/kappa) - kappa for kappa > 2k/pi;
#    ANG3 first stress return at order l-2 with coefficient prod c / (l-2)!;
#    ANG4 E_- = k^2 kappa^2 / 3 for every N >= 2, Henrici departure at N = 200, 400.
#    KILL: any analytic identity off by > 1e-10, or E_- depends on N.
import json, math
import numpy as np
from scipy.linalg import expm, eigvals
from scipy.integrate import quad
import sympy as sp

out = {}
rng = np.random.default_rng(20261104)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)

# K1 -----------------------------------------------------------------------
sat = 0.0
viol = []
for om in [0.3, 1.0, 2.0]:
    H = om * sx
    for sgn in [1, -1]:
        P0 = (I2 + sgn * sy) / 2
        for t in np.linspace(0.0, 0.6, 31):
            U = expm(-1j * H * t)
            P = U @ P0 @ U.conj().T
            Pd = -1j * (H @ P - P @ H)
            nu = P[0, 0].real
            g = 0.5 * np.linalg.norm(Pd) ** 2
            S = 1 / (nu * (1 - nu))
            taud = -Pd[0, 0].real * S
            sat = max(sat, abs(taud ** 2 / (4 * g * S) - 1))
            EH = np.linalg.norm(P @ H @ (I2 - P)) ** 2
            TrX = nu * (1 - nu)
            if t == 0.0:
                viol.append([om, sgn, abs(taud), 2 * math.sqrt(EH * S), 2 * math.sqrt(TrX * S)])
assert sat < 1e-10
assert all(r[2] > r[4] + 1e-9 for r in viol if r[0] >= 1.0)
out['K1_joint_offset'] = {'max_saturation_error': sat, 'at_t0_[omega,sign,|taudot|,bound_EH,bound_TrX]': viol}

# K2 -----------------------------------------------------------------------
k, v, u, w = sp.symbols('k v u w', real=True)
d = sp.Matrix([v + w * sp.cos(k), w * sp.sin(k), sp.I * u])
s = (d.T * d)[0]
dk, dv = d.diff(k), d.diff(v)
def bil(a, b):
    return (a.T * b)[0]
def Qab(a, b):
    return (s * bil(a, b) - bil(d, a) * bil(d, b)) / (4 * s ** 2)
Qm = sp.Matrix([[Qab(dk, dk), Qab(dk, dv)], [Qab(dv, dk), Qab(dv, dv)]])
res = sp.simplify(sp.expand(Qm.det() * 16 * s ** 3 + u ** 2 * w ** 2 * sp.cos(k) ** 2))
assert res == 0
worst = 0.0
for _ in range(2000):
    vv, uu, kk, ww = rng.uniform(.05, 2), rng.uniform(.01, .8), rng.uniform(0, 2 * np.pi), rng.uniform(.3, 1.5)
    E2 = vv * vv + ww * ww + 2 * vv * ww * np.cos(kk) - uu * uu
    if abs(E2) < .03:
        continue
    h = np.array([[1j * uu, vv + ww * np.exp(-1j * kk)], [vv + ww * np.exp(1j * kk), -1j * uu]])
    ev, R = np.linalg.eig(h)
    L = np.linalg.inv(R).conj().T
    Dk = np.array([[0, -1j * ww * np.exp(-1j * kk)], [1j * ww * np.exp(1j * kk), 0]])
    Dv = np.array([[0, 1], [1, 0]], complex)
    def Q(V):
        return ((L[:, 1].conj() @ V @ R[:, 0]) * (L[:, 0].conj() @ V @ R[:, 1]) / (ev[1] - ev[0]) ** 2).real
    a, c = Q(Dk), Q(Dv)
    b = Q((Dk + Dv) / np.sqrt(2)) - (a + c) / 2
    det = a * c - b * b
    exp_ = -uu * uu * ww * ww * np.cos(kk) ** 2 / (16 * E2 ** 3)
    worst = max(worst, abs(det - exp_) / max(1, abs(exp_)))
assert worst < 1e-9
grid = [(kk, vv) for kk in np.linspace(0, 2 * np.pi, 401)[:-1] for vv in np.linspace(0, 2, 400)]
lor = sum(1 for kk, vv in grid if (vv * vv + 1 + 2 * vv * np.cos(kk) - .25) > 0 and abs(np.cos(kk)) > 1e-12)
out['K2_metric_signature'] = {'sympy_residual': str(res), 'random_cases_max_scaled_error': worst,
                              'Lorentzian_fraction_u0.5_w1_grid_k0..2pi_v0..2': lor / len(grid)}

# K3 -----------------------------------------------------------------------
e3 = 0.0
for g in np.linspace(0.05, 3, 60):
    te = 2 * np.arctanh(1j * g)
    e3 = max(e3, abs(te - 2j * math.atan(g)), abs(np.tanh(te / 2) - 1j * g),
             abs((1 + g * g) - 1 / math.cos(te.imag / 2) ** 2))
t1 = 2 * np.arctanh(1j * 1.0)
assert e3 < 1e-12 and np.isfinite(t1) and abs(abs(np.tanh(t1 / 2)) - 1) < 1e-15
out['K3_branch'] = {'max_error': e3, 'tau_end_at_gamma1': [t1.real, t1.imag], 'Gamma_end_at_gamma1': [0.0, 1.0]}

# K4 -----------------------------------------------------------------------
e4 = 0.0
for x in [0.1, 0.5, 1.0, 2.0, 5.0, 9.0]:
    r = math.atan(math.exp(-x / 2))
    for phi in np.linspace(0, 2 * np.pi, 7):
        psi = np.zeros(4, complex); psi[0] = math.cos(r); psi[3] = np.exp(1j * phi) * math.sin(r)
        rho = np.outer(psi, psi.conj()).reshape(2, 2, 2, 2)
        rout = np.einsum('ajbj->ab', rho)
        C = rout[1, 1].real
        tau = math.log((1 - C) / C)
        e4 = max(e4, abs(tau - x), abs((1 - 2 * C) - math.tanh(x / 2)))
assert e4 < 1e-12
out['K4_fermion_record'] = {'max_error': e4, 'frequencies_omega_over_T': [0.1, 0.5, 1, 2, 5, 9], 'phases': 7}

# K5 -----------------------------------------------------------------------
# 1D wave u'' + omega^2 g u = 0 with index sqrt(g); g = c / Delta^2. Step at y = 0.
e5 = 0.0
for _ in range(200):
    D1, D2 = rng.uniform(.2, 5, 2)
    om = rng.uniform(.5, 4)
    n1, n2 = 1 / D1, 1 / D2
    k1, k2 = om * n1, om * n2
    # incident e^{ik1 y} + r e^{-ik1 y} for y<0, t e^{ik2 y} for y>0; continuity of u and u'
    A = np.array([[1, -1], [-1j * k1, -1j * k2]])
    rhs = np.array([-1, -1j * k1])
    r_, t_ = np.linalg.solve(A, rhs)
    e5 = max(e5, abs(r_ - math.tanh(0.5 * math.log(D2 / D1))))
assert e5 < 1e-10
out['K5_gap_step_reflection'] = {'random_steps': 200, 'max_error': e5}

# K6 -----------------------------------------------------------------------
e6 = 0.0
for _ in range(200):
    nu = rng.uniform(.01, .99)
    G, Gc = 1 - 2 * nu, 1 - 2 * (1 - nu)
    ta, tc = math.log((1 - nu) / nu), math.log(nu / (1 - nu))
    e6 = max(e6, abs(G + Gc), abs(ta + tc), abs(nu * (1 - nu) - (1 - nu) * nu))
    n, rk = 5, 2
    Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Qm_, _ = np.linalg.qr(Z)
    P = Qm_[:, :rk] @ Qm_[:, :rk].conj().T
    def tangent():
        Hh = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); Hh = Hh + Hh.conj().T
        return 1j * (Hh @ P - P @ Hh)
    V, W = tangent(), tangent()
    Q1 = np.trace(P @ V @ W)
    Q2 = np.trace((np.eye(n) - P) @ (-V) @ (-W))
    e6 = max(e6, abs(Q2 - np.conj(Q1)), abs(np.trace(V @ W) - 2 * Q1.real))
assert e6 < 1e-12
out['K6_complement_parity'] = {'cases': 200, 'max_error': e6}

# K7 -----------------------------------------------------------------------
e7, minus_law = 0.0, 0.0
for _ in range(50):
    Hh = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    z = complex(rng.normal(), rng.normal())
    R1 = np.linalg.inv(z * np.eye(4) - Hh.conj().T)
    R2 = np.linalg.inv(np.conj(z) * np.eye(4) - Hh).conj().T
    e7 = max(e7, np.abs(R1 - R2).max())
    minus_law = max(minus_law, np.abs(R1 + np.linalg.inv(z * np.eye(4) - Hh)).max())
assert e7 < 1e-12 and minus_law > 1e-3
out['K7_resolvent_adjoint'] = {'max_error_adjoint_law': e7, 'min_violation_of_minus_law_max_over_cases': minus_law}

# K8 -----------------------------------------------------------------------
def cvec(n):
    return np.array([(l + 1) / math.sqrt((2 * l + 1) * (2 * l + 3)) for l in range(n - 1)])
ang = {}
kk = 1.0
eA1 = max(abs(quad(lambda mu: s_ / (s_ * s_ + kk * kk * mu * mu), -1, 1)[0] / 2 - math.atan(kk / s_) / kk) for s_ in [.01, .1, .5, 2])
ang['ANG1'] = {'angular_integral_error': eA1, 'Z_b_0plus': 2 * kk / math.pi,
               'Z_b_small_s': [[s_, 1 / (math.atan(kk / s_) / kk) - s_] for s_ in [1e-2, 1e-4, 1e-6]]}
poles = []
for kap in [.64, .7, .916, 1, 2]:
    p = kk / math.tan(kk / kap) - kap
    g0 = math.atan(kk / (p + kap)) / kk
    poles.append([kap, p, abs(1 - kap * g0)])
    assert p > -kap and abs(1 - kap * g0) < 1e-12
ang['ANG2'] = {'onset_kappa': 2 * kk / math.pi, 'poles_[kappa,s*,residual]': poles}
n = 16; c = cvec(n); M = np.diag(c, 1) + np.diag(c, -1); L = -1j * kk * M
ret = []
for l in [3, 4, 5, 8]:
    for q in range(l - 2):
        assert abs(np.linalg.matrix_power(L, q)[2, l]) < 1e-15
    exact = np.prod(c[2:l]) / math.factorial(l - 2)
    calc = abs(np.linalg.matrix_power(L, l - 2)[2, l]) / math.factorial(l - 2)
    assert abs(calc - exact) < 1e-14
    for q in range(l):
        assert abs(np.linalg.matrix_power(L, q)[0, l]) < 1e-15
    ret.append([l, l - 2, exact, abs(np.linalg.matrix_power(L, l)[0, l])])
ang['ANG3'] = {'[l, stress order, coefficient, density coefficient at order l]': ret}
rows = []
for n in [2, 5, 20, 100, 200, 400]:
    c = cvec(n); M = np.diag(c, 1) + np.diag(c, -1)
    for kap in [1.0, 0.5]:
        L = -1j * kk * M - kap * np.diag([0] + [1] * (n - 1)); A_ = L.conj().T
        Em = np.linalg.norm(L @ A_ - A_ @ L, 'fro') ** 2 / 8
        Ep = np.linalg.norm(L @ L - A_ @ A_, 'fro') ** 2 / 8
        dep = np.linalg.norm(L, 'fro') ** 2 - np.sum(abs(eigvals(L)) ** 2)
        assert abs(Em - kk * kk * kap * kap / 3) < 1e-10
        rows.append([n, kap, Em, Ep, float(dep)])
ang['ANG4'] = {'[N, kappa, E_minus, E_plus, departure^2]': rows}
out['K8_angular_chain'] = ang
out['status'] = 'PASS'
print(json.dumps(out, indent=1))
