# SCRIPT: OFFSET-LW-02
# The offset paper's moduli are peel reflections of ratios of the Rice-Mele chain.
#
# WHY THIS CHECK PROVES WHAT IT CLAIMS
#   E5: the signed dimerization u = (t1 - t2)/(t1 + t2) of v31 Sec 7.5 is Gamma(t1/t2), and the intercept
#       variable u0 = (1 - r)/(1 + r), r = t1/t2, of v31 Eq. 113 is Gamma(t2/t1) = -u.
#   E6: the combined modulus k_e = Emin/Emax obeys xi_c = 1/(2 artanh k_e) (v31 Eq. 19), so k_e = Gamma(e^{1/xi_c});
#       the inner branch point h = (1 - k_e)/(1 + k_e) of v31 Sec 7.4 equals Gamma(Emax/Emin), the reflection of
#       the band-edge ratio, and equals e^{-1/xi_c}.  The run does NOT assume these: it takes h as the root of
#       the symbol quadratic t1 t2 w^2 + (t1^2 + t2^2 + v^2) w + t1 t2 = 0 (v27 Eq. 40-41), compares it to
#       Gamma(Emax/Emin), and compares Gamma(Emax/Emin) with the "Matched h" column printed in v31 Sec 7.4.
#       Agreement with the printed column to its nine digits is a check against the paper, not against myself.
#   Also: Gamma composed with itself is z -> -1/z (the Cayley map has order four); the Landen step
#       h = (1 - k)/(1 + k) is -Gamma(k).
from mpmath import mp, mpf, sqrt, log, atanh, exp, nstr, polyroots

mp.dps = 50


def gam(z):
    return (z - 1) / (z + 1)


printed = {  # v31 Sec 7.4 table: (t1, t2, v) -> matched h
    ('0.6', '1', '0.4'): '0.489206414',
    ('0.5', '1', '0.3'): '0.448035875',
    ('0.7', '0.9', '0.2'): '0.701531611',
    ('0.8', '0.8', '0.5657'): '0.499991412',
    ('0.3', '1', '0.4'): '0.255690650',
}
print('E6  inner branch point h: symbol-quadratic root against Gamma(Emax/Emin) against the printed column')
for key, hp in printed.items():
    t1, t2, v = map(mpf, key)
    Emin = sqrt((t1 - t2) ** 2 + v ** 2)
    Emax = sqrt((t1 + t2) ** 2 + v ** 2)
    roots = polyroots([t1 * t2, t1 ** 2 + t2 ** 2 + v ** 2, t1 * t2])
    w_in = [w for w in roots if abs(w) < 1][0]
    h_root = -w_in.real
    h_gam = gam(Emax / Emin)
    ke = Emin / Emax
    xi_c = 1 / (2 * atanh(ke))
    print('  %-18s root %s  Gamma(Emax/Emin) %s  printed %s  |k_e - Gamma(e^(1/xi_c))| %s  |h - e^(-1/xi_c)| %s'
          % (str(key), nstr(h_root, 12), nstr(h_gam, 12), hp, nstr(abs(ke - gam(exp(1 / xi_c))), 3),
             nstr(abs(h_gam - exp(-1 / xi_c)), 3)))
print()
print('E5  dimerization modulus and the intercept variable')
for t1, t2 in [(mpf('0.3'), 1), (mpf('0.6'), 1), (mpf('0.8'), 1)]:
    u = (t1 - t2) / (t1 + t2)
    r = t1 / t2
    u0 = (1 - r) / (1 + r)
    print('  t1/t2 = %s: u - Gamma(t1/t2) = %s ; u0 - Gamma(t2/t1) = %s ; u0 + u = %s'
          % (nstr(r, 3), nstr(u - gam(t1 / t2), 3), nstr(u0 - gam(t2 / t1), 3), nstr(u0 + u, 3)))
print()
print('Cayley order four and Landen as a reflection')
for z in [mpf(2), mpf('5.828427'), mpf('0.3')]:
    print('  z = %s: Gamma(Gamma(z)) + 1/z = %s ; (1 - z)/(1 + z) + Gamma(z) = %s'
          % (nstr(z, 8), nstr(gam(gam(z)) + 1 / z, 3), nstr((1 - z) / (1 + z) + gam(z), 3)))
