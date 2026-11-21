# SCRIPT: OFFSET-LW-03
# The loop wall read on the Rice-Mele family of the offset paper.
#
# WHY THIS CHECK PROVES WHAT IT CLAIMS
#   E8 (algebra): k_e = Gamma(e^{1/xi_c}) (OFFSET-LW-02), so the loop wall Gamma^2 = 1/2 applied to the
#   correlation rail is k_e^2 = 1/2, i.e. Emax^2 = 2 Emin^2, i.e. t1^2 + t2^2 + v^2 = 6 t1 t2.  The same
#   quadratic, written as rho = (t1^2 + t2^2 + v^2)/(2 t1 t2) = 3, says the mid-gap cell transfer matrix has
#   trace magnitude 6 = z_w + 1/z_w, sec psi = 3, rails 3 +- 2 sqrt 2.  On the dimerized line (v = 0) it is
#   r^2 - 6 r + 1 = 0 with r = t1/t2: the element paper's wall polynomial z^2 - 6 z + 1 with z = t2/t1.
#   At elliptic parameter m = k_e^2 = 1/2 the periods K(m) and K(1 - m) are equal, so v31's spacing
#   Delta* = 4 pi K(m)/K(1 - m) equals 4 pi exactly (Eq. 92), and the Ising parameter eta_I = 2 pi (Eq. 94).
#   The run checks each equality at sample points of the wall locus, builds the transfer matrix explicitly,
#   and then MEASURES the entanglement ladder spacing from finite even blocks (v31 Appendix C covariance) at
#   a dimerized wall point (where the spacing is a proved endpoint result) and at an interior wall point
#   (where v31 grades Eq. 92 as R/V, so this is a new out-of-sample test of that formula).
#   Positive control: the same instrument at (0.6, 1, 0.4) must return v31's measured 8.138524807.
#   Kill condition, written before the run: if the measured interior spacing differs from 4 pi by more than
#   1e-6 relative while the reference control passes at that level, Eq. 92 fails at the wall point.
from mpmath import mp, mpf, sqrt, log, atanh, ellipk, pi, matrix, eigsy, nstr

mp.dps = 160


def covariance(a, b, v, length):
    A = a * a + b * b + v * v
    p = a * b
    s = (A + sqrt(A * A - 4 * p * p)) / 2
    r = p / s
    memo = {}

    def g(j):
        j = abs(j)
        if j not in memo:
            memo[j] = ((-r) ** j / sqrt(s) * mp.rf(mpf('0.5'), j) / mp.factorial(j)
                       * mp.hyp2f1(mpf('0.5'), j + mpf('0.5'), j + 1, r * r))
        return memo[j]

    C = matrix(length)
    for i in range(length):
        for j in range(length):
            d = i // 2 - j // 2
            if i % 2 == j % 2:
                C[i, j] = ((1 if i == j else 0) + (-v if i % 2 == 0 else v) * g(d)) / 2
            elif i % 2 == 0:
                C[i, j] = (a * g(d) + b * g(d - 1)) / 2
            else:
                C[i, j] = (a * g(d) + b * g(d + 1)) / 2
    return C


def spacing(a, b, v, L):
    C = covariance(a, b, v, L)
    nus = eigsy(C, eigvals_only=True)
    eps = sorted([log((1 - nus[i]) / nus[i]) for i in range(L)])
    mid = L // 2
    # towers interleave: eps[k+2] - eps[k] is one rung of one tower; read the central ones
    vals = [eps[k + 2] - eps[k] for k in range(mid - 3, mid + 1)]
    return vals, eps


def delta_star(a, b, v):
    Emin = sqrt((a - b) ** 2 + v ** 2)
    Emax = sqrt((a + b) ** 2 + v ** 2)
    m = (Emin / Emax) ** 2
    return 4 * pi * ellipk(m) / ellipk(1 - m), m


def transfer_trace_E0(a, b, v):
    # cell transfer matrix of H psi = E psi at E = 0 for hoppings -t1 (intra), -t2 (inter), onsite +v, -v
    # A-site eq: -t2 psiB(n-1) + v psiA(n) - t1 psiB(n) = E psiA(n)
    # B-site eq: -t1 psiA(n) - v psiB(n) - t2 psiA(n+1) = E psiB(n)
    E = 0
    # state (psiA(n), psiB(n-1)) -> (psiA(n+1), psiB(n))
    # psiB(n) = ((v - E) psiA(n) - t2 psiB(n-1)) / t1
    # psiA(n+1) = (-t1 psiA(n) - (v + E) psiB(n)) / t2
    m11 = (v - E) / a
    m12 = -b / a
    T = matrix([[(-a - (v + E) * m11) / b, -(v + E) * m12 / b], [m11, m12]])
    return T[0, 0] + T[1, 1], T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0]


wall = 3 + 2 * sqrt(2)
print('Wall locus t1^2 + t2^2 + v^2 = 6 t1 t2 (t2 = 1): algebraic readings')
pts = []
for v in [mpf(0), mpf('0.2'), mpf('0.5'), mpf('1.0'), mpf('2.0')]:
    t1 = (6 - sqrt(36 - 4 * (1 + v * v))) / 2
    pts.append((t1, mpf(1), v))
for (a, b, v) in pts:
    Emin = sqrt((a - b) ** 2 + v ** 2)
    Emax = sqrt((a + b) ** 2 + v ** 2)
    ke = Emin / Emax
    xi_c = 1 / (2 * atanh(ke))
    D, m = delta_star(a, b, v)
    tr, dt = transfer_trace_E0(a, b, v)
    rho = (a * a + b * b + v * v) / (2 * a * b)
    hI = (1 - ke) / (1 + ke)
    etaI = pi * ellipk(1 - hI ** 2) / ellipk(hI ** 2)
    print('  t1=%s v=%s: k_e^2-1/2=%s |trM(0)|-6=%s detM=%s rho-3=%s Delta*-4pi=%s 2eta_I-4pi=%s xi_c*ln(3+2sqrt2)-1=%s'
          % (nstr(a, 10), nstr(v, 3), nstr(ke ** 2 - mpf(1) / 2, 3), nstr(abs(tr) - 6, 3), nstr(dt, 6),
             nstr(rho - 3, 3), nstr(D - 4 * pi, 3), nstr(2 * etaI - 4 * pi, 3), nstr(xi_c * log(wall) - 1, 3)))
print('  dimerized wall point t1/t2 = 3 - 2 sqrt2 =', nstr(3 - 2 * sqrt(2), 15), '; t2/t1 =', nstr(1 / (3 - 2 * sqrt(2)), 15))
print()

print('Measured ladder spacing from finite even blocks (central rungs)')
ref = (mpf('0.6'), mpf('1'), mpf('0.4'))
for name, (a, b, v), L in [('reference control (0.6,1,0.4)', ref, 40),
                           ('reference control (0.6,1,0.4)', ref, 48),
                           ('dimerized wall point', pts[0], 20),
                           ('dimerized wall point', pts[0], 28),
                           ('interior wall point v=0.5', pts[2], 20),
                           ('interior wall point v=0.5', pts[2], 28),
                           ('interior wall point v=1.0', pts[3], 28)]:
    vals, eps = spacing(a, b, v, L)
    D, m = delta_star(a, b, v)
    print('  %-30s L=%2d  central rungs %s  Eq.92 %s  max rel dev %s'
          % (name, L, [nstr(x, 12) for x in vals], nstr(D, 12), nstr(max(abs(x / D - 1) for x in vals), 3)))
print('  4 pi =', nstr(4 * pi, 15))
