# SCRIPT: OFFSET-LW-07
# The offset paper's endpoint proof and remainder conjecture written as peel reflections.
#
# WHY THIS CHECK PROVES WHAT IT CLAIMS
#   E1b: v31 Theorem E2 (Eq. 68) defines a_hat_n = (R_n - 1)/(R_n + 1): literally Gamma(R_n) of the Hankel
#   ratio R_n.  Its limit (Eq. 76) is R_inf = (sqrt M + sqrt e)/(sqrt M - sqrt e), so Gamma(R_inf) = sqrt(e/M)
#   = sqrt(k_e); and at equal hopping gamma^2 = k_e = Gamma(e^{1/xi_c}): the square of the offset's reflection
#   is the reflection of the correlation rail.  Checked at sample points.
#   E14: Conjecture E6's candidate step ratio rho = ((sqrt(M+e) - sqrt(2e))/(sqrt(M+e) + sqrt(2e)))^2 equals
#   Gamma(w)^2 with w = sqrt((M+e)/(2e)): a returned power in the element paper's sense.  The run recomputes
#   the four printed rho values of v31 Sec 5.10 from Gamma(w)^2 and compares to the printed digits.
#   Aside (algebra only, meaning untested): rho = 1/2 exactly when w = 3 + 2 sqrt 2, i.e. when
#   (Emax + Emin)/(2 Emin) = (3 + 2 sqrt 2)^2 = 17 + 12 sqrt 2.
from mpmath import mp, mpf, sqrt, atanh, nstr

mp.dps = 40


def gam(z):
    return (z - 1) / (z + 1)


printed = {('0.3', '1', '0.4'): '0.005430335405', ('0.6', '1', '0.4'): '0.02768429499',
           ('1', '1', '0.1'): '0.2793728502', ('1', '1', '0.02'): '0.5674378981'}
print('E14 remainder step ratio rho = Gamma(w)^2, w = sqrt((M+e)/(2e))')
for key, rp in printed.items():
    a, b, v = map(mpf, key)
    e = sqrt((a - b) ** 2 + v ** 2)
    M = sqrt((a + b) ** 2 + v ** 2)
    rho = ((sqrt(M + e) - sqrt(2 * e)) / (sqrt(M + e) + sqrt(2 * e))) ** 2
    w = sqrt((M + e) / (2 * e))
    print('  %-16s rho=%s  Gamma(w)^2=%s  printed %s' % (str(key), nstr(rho, 12), nstr(gam(w) ** 2, 12), rp))
print()
print('E1b Hankel limit and equal-hopping square law')
for key in [('1', '1', '0.4'), ('1', '1', '1.5'), ('0.5', '0.5', '0.4')]:
    a, b, v = map(mpf, key)
    e = sqrt((a - b) ** 2 + v ** 2)
    M = sqrt((a + b) ** 2 + v ** 2)
    Rinf = (sqrt(M) + sqrt(e)) / (sqrt(M) - sqrt(e))
    ke = e / M
    xi_c = 1 / (2 * atanh(ke))
    gamma = v / sqrt(e * M)
    print('  %-16s Gamma(R_inf) - sqrt(k_e) = %s ; gamma^2 - Gamma(e^(1/xi_c)) = %s'
          % (str(key), nstr(gam(Rinf) - sqrt(ke), 3), nstr(gamma ** 2 - gam(mp.e ** (1 / xi_c)), 3)))
print()
wall = 3 + 2 * sqrt(2)
print('Aside: rho = 1/2 at (Emax+Emin)/(2 Emin) =', nstr(wall ** 2, 20), ' = 17 + 12 sqrt2 =', nstr(17 + 12 * sqrt(2), 20))
x = wall ** 2
ke = 1 / (2 * x - 1)
print('  i.e. k_e = Emin/Emax =', nstr(ke, 15), '; check Gamma(w)^2 with M = 1/k_e, e = 1:',
      nstr(gam(sqrt((1 / ke + 1) / 2)) ** 2, 15))
