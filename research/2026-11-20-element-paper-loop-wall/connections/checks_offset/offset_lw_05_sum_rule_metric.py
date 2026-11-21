# SCRIPT: OFFSET-LW-05
# The element paper's junction sum rule and second moment, evaluated on the offset paper's Rice-Mele projector.
#
# WHY THIS CHECK PROVES WHAT IT CLAIMS
#   S4a (site sum rule, element README item 15): for an idempotent P, (P^2)_ii = P_ii gives
#       sum_{j != i} |P_ij|^2 = P_ii - P_ii^2 (per site, one orbital per site here).
#   S4b (region form): for a region A, Tr(C_A - C_A^2) = sum_{i in A, j not in A} |P_ij|^2: the number variance
#       of A is a cut-crossing sum.  Tr(C_A - C_A^2) = sum_i nu_i (1 - nu_i) is the even partner of the offset's
#       odd log-odds; per level nu(1 - nu) = (1 - Gamma_i^2)/4, so the loop wall Gamma^2 = 1/2 is a level holding
#       exactly half its maximum variance.
#   E13 (second moment = projector metric): with cell-centre positions (the element paper's partition, and the
#       orbital-position-free Bloch gauge of v31 Eq. 16), Parseval gives
#       (1/2) sum_R R^2 ||P(R)||_F^2 = (1/2) int dk/2pi Tr(dP/dk dP/dk) = int dk/2pi g^P_kk(k),
#       with g^P the intrinsic projector metric of v31 Eq. 20, g^P_kk = (1/4) |d dhat/dk|^2.
#   The run evaluates both sides independently (real-space Fourier sums from quadrature versus a k-space
#   integral of the analytic dhat derivative).  Positive control: the half-filled one-band chain must give the
#   element paper's nearest share 8/pi^2.
import numpy as np

t1, t2, v = 0.6, 1.0, 0.4
Nk = 1 << 14
k = 2 * np.pi * (np.arange(Nk) + 0.5) / Nk - np.pi


def dvec(k):
    # H(k) = [[v, -(t1 + t2 e^{-ik})], [-(t1 + t2 e^{ik}), -v]] = dx sx + dy sy + dz sz
    dx = -(t1 + t2 * np.cos(k))
    dy = -t2 * np.sin(k)
    dz = v * np.ones_like(k)
    return np.array([dx, dy, dz])


d = dvec(k)
E = np.linalg.norm(d, axis=0)
dh = d / E
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
Pk = 0.5 * (np.eye(2)[None] - (dh[0][:, None, None] * sx + dh[1][:, None, None] * sy + dh[2][:, None, None] * sz))
Rmax = 60
Rs = np.arange(-Rmax, Rmax + 1)
PR = np.array([np.mean(Pk * np.exp(1j * k * R)[:, None, None], axis=0) for R in Rs])  # P(R) cell blocks


def site_block(i, j):
    ci, ai = divmod(i, 2)
    cj, aj = divmod(j, 2)
    R = cj - ci
    if abs(R) > Rmax:
        return 0.0
    return PR[R + Rmax][ai, aj]


print('S4a site sum rule (sublattice A and B sites of cell 0)')
for i in [0, 1]:
    off = sum(abs(site_block(i, j)) ** 2 for j in range(-2 * Rmax, 2 * Rmax + 2) if j != i)
    pii = site_block(i, i).real
    print('  site %d: sum_j |P_ij|^2 = %.15f ; P_ii - P_ii^2 = %.15f ; diff %.1e' % (i, off, pii - pii ** 2, off - (pii - pii ** 2)))

print('S4b region sum rule, A = sites 0..16')
A = list(range(17))
C = np.array([[site_block(i, j) for j in A] for i in A])
lhs = np.trace(C - C @ C).real
rhs = sum(abs(site_block(i, j)) ** 2 for i in A for j in range(-2 * Rmax, 2 * Rmax + 2) if j not in A)
nu = np.linalg.eigvalsh(C)
G = 1 - 2 * nu
print('  Tr(C_A - C_A^2) = %.15f ; cut-crossing sum = %.15f ; sum (1-Gamma^2)/4 = %.15f' % (lhs, rhs, np.sum((1 - G ** 2) / 4)))

print('E13 second moment (cell centres) against the integrated projector metric')
lhs = 0.5 * sum((R ** 2) * np.sum(np.abs(PR[R + Rmax]) ** 2) for R in Rs)
# analytic derivative of dhat
dd = np.array([t2 * np.sin(k), -t2 * np.cos(k), np.zeros_like(k)])
ddh = dd / E - d * (np.sum(d * dd, axis=0)) / E ** 3
gkk = 0.25 * np.sum(ddh ** 2, axis=0)
rhs = np.mean(gkk)
print('  (1/2) sum_R R^2 ||P(R)||^2 = %.15f ; int dk/2pi g^P_kk = %.15f ; diff %.1e' % (lhs, rhs, lhs - rhs))

print('Control: half-filled one-band chain, nearest-shell share of the off-site budget')
Nk2 = 1 << 16
kk = 2 * np.pi * (np.arange(Nk2) + 0.5) / Nk2 - np.pi
occ = (np.cos(kk) > 0).astype(float)   # E = -2 cos k, half filling
P = [np.mean(occ * np.cos(kk * R)) for R in range(0, 400)]
budget = P[0] - P[0] ** 2
nearest = 2 * P[1] ** 2
print('  nearest share = %.12f ; 8/pi^2 = %.12f' % (nearest / budget, 8 / np.pi ** 2))
