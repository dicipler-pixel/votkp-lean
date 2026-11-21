# SCRIPT: OFFSET-LW-04
# Two faces and the offset's own position against the loop wall.
#
# WHY THIS CHECK PROVES WHAT IT CLAIMS
#   E10 (algebra): put gamma = |v|/Q and delta = |t1 - t2|/Q with Q = sqrt(Emin Emax).  Then
#   gamma^2 + delta^2 = (v^2 + (t1 - t2)^2)/(Emin Emax) = Emin^2/(Emin Emax) = k_e.  The element paper's
#   two-face closing test Gamma_1^2 + Gamma_2^2 < 1 is therefore k_e < 1, which holds exactly when
#   t1 t2 > 0 (the offset paper's connected regime); contact Gamma_1^2 + Gamma_2^2 = 1 is t1 t2 = 0, the
#   decoupled chain where finite blocks reach occupations 0 and 1 and the offset's strict domain fails.
#   On the isospectral circle (v31 Eq. 46) gamma = sin(theta) sqrt(k_e), delta = |cos(theta)| sqrt(k_e).
#   E11: the offset itself is "outside the wall" when gamma^2 > 1/2, tau_inf > ln(3 + 2 sqrt 2).  Since
#   gamma^2 <= k_e on its circle, this needs k_e > 1/2.  At equal hopping t, k_e = |v|/sqrt(4t^2 + v^2) and
#   gamma^2 = k_e, so gamma^2 = 1/2 exactly at v = 2t/sqrt(3).  The run builds finite odd blocks there and
#   shows tau_L -> ln(3 + 2 sqrt 2) (a Rice-Mele substrate whose offset sits ON the wall), and at a point
#   beyond it.  Kill condition before the run: if |tau_L| at L = 21 differs from 2 artanh gamma by more than
#   1e-6 at either point, the v31 endpoint (Theorem E7) is misapplied here.
from mpmath import mp, mpf, sqrt, log, atanh, matrix, eye, det, nstr, sin, cos, pi

mp.dps = 120


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


def tau(a, b, v, L):
    C = covariance(a, b, v, L)
    return log(det(eye(L) - C)) - log(det(C))


print('E10 gamma^2 + delta^2 = k_e')
for (a, b, v) in [('0.6', '1', '0.4'), ('0.3', '1', '0.4'), ('1', '1', '1.5'), ('0.01', '1', '0.4'), ('0.000001', '1', '0.4')]:
    a, b, v = mpf(a), mpf(b), mpf(v)
    Emin = sqrt((a - b) ** 2 + v ** 2)
    Emax = sqrt((a + b) ** 2 + v ** 2)
    Q = sqrt(Emin * Emax)
    g2 = (v / Q) ** 2
    d2 = ((a - b) / Q) ** 2
    print('  (%s,%s,%s): gamma^2=%s delta^2=%s sum-k_e=%s  1-sum=%s'
          % (nstr(a, 6), nstr(b, 3), nstr(v, 3), nstr(g2, 10), nstr(d2, 10), nstr(g2 + d2 - Emin / Emax, 3), nstr(1 - g2 - d2, 6)))
print('  on the circle: gamma = sin(theta) sqrt(k_e), delta = |cos(theta)| sqrt(k_e)')
e0, p0 = mpf('0.8'), mpf('0.6')
for th in [pi / 7, pi / 3, 2 * pi / 5]:
    d, v = e0 * cos(th), e0 * sin(th)
    a = (sqrt(d * d + 4 * p0) + d) / 2
    b = (sqrt(d * d + 4 * p0) - d) / 2
    Emin = sqrt((a - b) ** 2 + v ** 2)
    Emax = sqrt((a + b) ** 2 + v ** 2)
    ke = Emin / Emax
    Q = sqrt(Emin * Emax)
    print('    theta=%s: gamma - sin(theta)sqrt(k_e) = %s ; delta - |cos|sqrt(k_e) = %s'
          % (nstr(th, 6), nstr(v / Q - sin(th) * sqrt(ke), 3), nstr(abs(a - b) / Q - abs(cos(th)) * sqrt(ke), 3)))
print()

print('E11 an offset on the wall and one beyond it (equal hopping t = 1)')
lw = log(3 + 2 * sqrt(2))
for label, v in [('on the wall, v = 2/sqrt3', 2 / sqrt(3)), ('beyond, v = 1.5', mpf('1.5')), ('reference-like, v = 0.4', mpf('0.4'))]:
    a = b = mpf(1)
    Emin = sqrt(v ** 2)
    Emax = sqrt(4 + v ** 2)
    gamma = v / sqrt(Emin * Emax)
    tinf = 2 * atanh(gamma)
    row = []
    for L in [5, 9, 13, 17, 21]:
        row.append(abs(tau(a, b, v, L)))
    print('  %-26s gamma^2=%s tau_inf=%s  tau_inf-ln(3+2sqrt2)=%s' % (label, nstr(gamma ** 2, 12), nstr(tinf, 15), nstr(tinf - lw, 6)))
    print('     |tau_L| at L=5..21:', [nstr(x, 15) for x in row], ' last - tau_inf =', nstr(row[-1] - tinf, 3))
