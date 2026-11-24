# SCRIPT: TWIN-SHAPES-LIB-01
# Shared tools for the shape readings of the twin chain (Jeromie Beasley, 24 Nov 2026, AI-assisted).
#  twin_starts(N): twin starts p (p, p+2 both prime) with 11 <= p, p+2 <= N  (segmented sieve, cached to .npy)
#  run_chain(T, arm, E, marks): the ball chain (kept as a 2x2 spinor product, well conditioned at large d) L_n = B(e_{s1}, r1) ... B(e_{sn}, rn), r_n = ln(a_{n+1}/a_n),
#     arm index of a_{n+1} picks the unit arm vector E[arm]. Body-frame (right) multiplication, as in conv_probe.py.
#     At each mark a' (first twin start >= mark) it records the polar split L = Boost(d n) R and three running sums
#     that split d - |P| L exactly:
#        d - |P| L = start term (first step, r1(1-|P|)) + sum[dd - r u.e]  (curvature gain)  +  sum r u.(e - P)  (arm noise)  +  sum r (u.P - |P|)  (heading lag)
#     where u = body heading (R^T n) before the step and P = mean of the arm vectors.
import numpy as np, math, os
from numba import njit
HERE = os.path.dirname(os.path.abspath(__file__))

def twin_starts(N=10**9):
    f = os.path.join(HERE, 'twins_%d.npy' % N)
    if os.path.exists(f): return np.load(f)
    R = int(N ** .5) + 2
    s = np.ones(R + 1, bool); s[:2] = False
    for i in range(2, int(R ** .5) + 1):
        if s[i]: s[i * i::i] = False
    base = np.nonzero(s)[0]
    seg = 10 ** 7; out = []; last = -10
    for lo in range(0, N + 1, seg):
        hi = min(lo + seg, N + 1)
        m = np.ones(hi - lo, bool)
        if lo == 0: m[:2] = False
        for p in base:
            if p * p >= hi: break
            st = max(p * p, ((lo + p - 1) // p) * p)
            m[st - lo::p] = False
        pr = np.nonzero(m)[0] + lo
        if len(pr) == 0: continue
        allp = np.concatenate([[last], pr])
        g = allp[1:] - allp[:-1]
        out.append(allp[:-1][g == 2])
        last = pr[-1]
    T = np.concatenate(out).astype(np.int64)
    T = T[T >= 11]
    np.save(f, T); return T

@njit(cache=True)
def boost4(e, r):
    B = np.eye(4); c = math.cosh(r); s = math.sinh(r)
    B[0, 0] = c
    for i in range(3):
        B[0, i + 1] = s * e[i]; B[i + 1, 0] = s * e[i]
        for j in range(3):
            B[i + 1, j + 1] += (c - 1) * e[i] * e[j]
    return B

@njit(cache=True)
def polar(L):
    g = L[0, 0]
    d = math.acosh(max(g, 1.0))
    sh = math.sqrt(max(g * g - 1, 1e-300))
    n = L[1:, 0] / sh
    Binv = boost4(-n, d)
    M = Binv @ L
    return d, n, M[1:, 1:].copy()

@njit(cache=True)
def sl2(e, r):
    # spinor boost cosh(r/2) + sinh(r/2) e.sigma  (acts X -> M X M^dagger on X = t + x.sigma)
    c = math.cosh(r / 2); s = math.sinh(r / 2)
    B = np.zeros((2, 2), np.complex128)
    B[0, 0] = c + s * e[2]; B[1, 1] = c - s * e[2]
    B[0, 1] = s * (e[0] - 1j * e[1]); B[1, 0] = s * (e[0] + 1j * e[1])
    return B

@njit(cache=True)
def coeffs(M):
    # M = m0 + m.sigma
    m0 = (M[0, 0] + M[1, 1]) / 2; m3 = (M[0, 0] - M[1, 1]) / 2
    m1 = (M[0, 1] + M[1, 0]) / 2; m2 = (M[1, 0] - M[0, 1]) / (2j)
    return m0, m1, m2, m3

@njit(cache=True)
def split2(M):
    # polar split M = H U. Position: M M^dag = cosh d + sinh d n.sigma ; body heading: M^dag M = cosh d + sinh d u.sigma
    # frame: U proportional to Re(m0) + i Im(m).sigma  (because M + (M^dag)^-1 = 2 Re m0 + 2i Im m.sigma, det M = 1)
    H2 = M @ M.conj().T; K2 = M.conj().T @ M
    ch = (H2[0, 0].real + H2[1, 1].real) / 2
    d = math.acosh(max(ch, 1.0)); sh = math.sinh(d)
    n = np.zeros(3); u = np.zeros(3)
    if sh > 1e-300:
        n[0] = H2[1, 0].real / sh; n[1] = H2[1, 0].imag / sh; n[2] = (H2[0, 0].real - H2[1, 1].real) / 2 / sh
        u[0] = K2[1, 0].real / sh; u[1] = K2[1, 0].imag / sh; u[2] = (K2[0, 0].real - K2[1, 1].real) / 2 / sh
    m0, m1, m2, m3 = coeffs(M)
    q = np.array([m0.real, m1.imag, m2.imag, m3.imag])
    q = q / math.sqrt(q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2)
    return d, n, u, q

@njit(cache=True)
def qrot(q):
    # rotation matrix of the spinor U = q0 + i (q1,q2,q3).sigma : X -> U X U^dag on vectors
    a = q[0]; b = -q[1]; c = -q[2]; e = -q[3]
    R = np.empty((3, 3))
    R[0, 0] = 1 - 2 * (c * c + e * e); R[0, 1] = 2 * (b * c - a * e); R[0, 2] = 2 * (b * e + a * c)
    R[1, 0] = 2 * (b * c + a * e); R[1, 1] = 1 - 2 * (b * b + e * e); R[1, 2] = 2 * (c * e - a * b)
    R[2, 0] = 2 * (b * e - a * c); R[2, 1] = 2 * (c * e + a * b); R[2, 2] = 1 - 2 * (b * b + c * c)
    return R

@njit(cache=True)
def qangle(q0, q1):
    # angle of the relative rotation U1 U0^-1, computed from quaternions (well conditioned for tiny angles)
    w = q1[0] * q0[0] + q1[1] * q0[1] + q1[2] * q0[2] + q1[3] * q0[3]
    x = q1[1] * q0[0] - q1[0] * q0[1]; y = q1[2] * q0[0] - q1[0] * q0[2]; z = q1[3] * q0[0] - q1[0] * q0[3]
    x -= q1[2] * q0[3] - q1[3] * q0[2]; y -= q1[3] * q0[1] - q1[1] * q0[3]; z -= q1[1] * q0[2] - q1[2] * q0[1]
    return 2 * math.atan2(math.sqrt(x * x + y * y + z * z), abs(w))

@njit(cache=True)
def run_chain(T, arm, E, marks, omega_from):
    # E: (k,3) unit arm vectors; arm[i] = arm index of twin start T[i]
    k = E.shape[0]
    P = np.zeros(3)
    for a in range(k): P += E[a] / k
    Pn = math.sqrt(P[0] ** 2 + P[1] ** 2 + P[2] ** 2)
    M = np.eye(2).astype(np.complex128)
    nm = len(marks)
    rec = np.zeros((nm, 30))
    mi = 0; path = 0.0; curv = 0.0; noise = 0.0; lag = 0.0; s2 = 0.0; start = 0.0
    om_sum = 0.0; om_cnt = 0.0; om_pred = 0.0
    d0, n0, u, q0 = split2(M)
    for i in range(len(T) - 1):
        r = math.log(T[i + 1] / T[i]); e = E[arm[i + 1]]
        first = d0 < 1e-12        # at the origin the heading is undefined: the first step is booked as its own 'start' term
        if first:
            u = e.copy()
        ue = u[0] * e[0] + u[1] * e[1] + u[2] * e[2]
        uP = u[0] * P[0] + u[1] * P[1] + u[2] * P[2]
        M = M @ sl2(e, r)
        if i % 4096 == 0:
            m0, m1, m2, m3 = coeffs(M); det = m0 * m0 - m1 * m1 - m2 * m2 - m3 * m3
            M = M / np.sqrt(det)
        d1, n1, u1, q1 = split2(M)
        if first:
            start += (d1 - d0) - Pn * r
        else:
            curv += (d1 - d0) - r * ue
            noise += r * (ue - uP)
            lag += r * (uP - Pn)
        path += r; s2 += r * r
        if omega_from > 0 and T[i + 1] >= omega_from:
            om_sum += qangle(q0, q1) / r; om_cnt += 1
            om_pred += math.tanh(d0 / 2) * math.sqrt(max(0.0, 1 - ue * ue))
        d0 = d1; u = u1; q0 = q1
        while mi < nm and T[i + 1] >= marks[mi]:
            R = qrot(q1)
            rec[mi, 0] = T[i + 1]; rec[mi, 1] = path; rec[mi, 2] = d1
            rec[mi, 3:6] = n1; rec[mi, 6:15] = R.ravel()
            rec[mi, 15] = curv; rec[mi, 16] = noise; rec[mi, 17] = lag; rec[mi, 18] = s2
            rec[mi, 19] = om_sum / max(om_cnt, 1.0); rec[mi, 20] = om_pred / max(om_cnt, 1.0)
            rec[mi, 21] = Pn; rec[mi, 22] = start
            rec[mi, 23:27] = q1; rec[mi, 27:30] = u1
            mi += 1
    return rec

def rot_angle_axis(R):
    ax = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]])
    nax = np.linalg.norm(ax); ang = math.atan2(nax / 2, (np.trace(R) - 1) / 2)
    if ang > 3.0:   # near a half turn the antisymmetric part is small: take the axis from R + I
        S = R + np.eye(3); k = np.argmax(np.linalg.norm(S, axis=0)); ax = S[:, k]; nax = np.linalg.norm(ax)
    return ang, (ax / nax if nax > 1e-15 else ax)

def arms_digit(T):
    return np.searchsorted(np.array([1, 7, 9]), T % 10).astype(np.int64)
