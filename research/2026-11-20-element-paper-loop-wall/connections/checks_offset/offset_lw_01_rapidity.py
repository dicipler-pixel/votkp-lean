# SCRIPT: OFFSET-LW-01
# Offset paper (v31) against the Loop Wall element paper: the offset as a peel reflection.
#
# WHY THIS CHECK PROVES WHAT IT CLAIMS
#   Claim E1: the offset paper's finite asymmetry a = (P_empty - P_full)/(P_empty + P_full) is exactly the
#   element paper's peel reflection Gamma(z) = (z - 1)/(z + 1) of the ratio z = P_empty/P_full, and
#   tau = log z = 2 artanh a.  This is algebra; the run checks that the paper's own objects (built here from
#   the analytic infinite-chain covariance of v31 Appendix C) obey it with the sign conventions as printed,
#   and that z equals the Schur ratio s0/s1 of v31 Theorem 8 (the even interior cancels).
#   Claim E2: every entanglement level is a peel step: z_i = (1 - nu_i)/nu_i, eps_i = ln z_i,
#   2 nu_i - 1 = -Gamma(z_i) = -tanh(eps_i/2) (v31 Eq. 12).  The loop wall Gamma^2 = 1/2 on one level is
#   |eps| = ln(3 + 2 sqrt 2), equivalently nu(1 - nu) >= 1/8 inside.  The run counts levels on each side.
#   Claim E3: reversing (v -> -v, or a one-site translation) sends z -> 1/z, Gamma -> -Gamma, Gamma^2 kept.
#   Claim E4: the protected even block has z = 1, Gamma = 0 (the matched junction).
#   Claim E7: tan(chi/2) = gamma with sec chi = (1 + gamma^2)/(1 - gamma^2) = cosh tau (the Two Trees
#   boost entry), and 2 sec chi = z + 1/z.
#   A failure of any identity beyond working precision would mean a misread convention, not new physics.
from mpmath import mp, mpf, sqrt, log, atanh, tanh, cosh, atan, sec, matrix, eye, eigsy, det, fsum, inverse, nstr

mp.dps = 110


def covariance(a, b, v, length, start=0):
    """v31 Appendix C covariance (analytic Fourier coefficients of 1/E), sites start .. start+length-1."""
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

    n = length + start
    C = matrix(n)
    for i in range(n):
        for j in range(n):
            d = i // 2 - j // 2
            if i % 2 == j % 2:
                C[i, j] = ((1 if i == j else 0) + (-v if i % 2 == 0 else v) * g(d)) / 2
            elif i % 2 == 0:
                C[i, j] = (a * g(d) + b * g(d - 1)) / 2
            else:
                C[i, j] = (a * g(d) + b * g(d + 1)) / 2
    return C[start:n, start:n]


def gam(z):
    return (z - 1) / (z + 1)


def probs(C):
    L = C.rows
    return det(eye(L) - C), det(C)


wall = 3 + 2 * sqrt(2)
lw = log(wall)
a_, b_, v_ = mpf('0.6'), mpf('1'), mpf('0.4')
e = sqrt((a_ - b_) ** 2 + v_ ** 2)
M = sqrt((a_ + b_) ** 2 + v_ ** 2)
gamma = v_ / sqrt(e * M)
print('reference (t1, t2, v) = (0.6, 1, 0.4); gamma = v/sqrt(Emin Emax) =', nstr(gamma, 30))
print('tau_inf = 2 artanh gamma =', nstr(2 * atanh(gamma), 30))
print()

print('E1  finite blocks: z = P_empty/P_full, Gamma(z), tanh(tau/2), and the Schur ratio s0/s1')
for L in [5, 9, 13, 17]:
    C = covariance(a_, b_, v_, L)
    Pe, Pf = probs(C)
    z = Pe / Pf
    tau = log(Pe) - log(Pf)
    a_fin = (Pe - Pf) / (Pe + Pf)
    # Schur: even block B = first L-1 sites, added site x = last site
    B = C[0:L - 1, 0:L - 1]
    c = C[0:L - 1, L - 1]
    cxx = C[L - 1, L - 1]
    s1 = cxx - (c.T * inverse(B) * c)[0]
    s0 = 1 - cxx - (c.T * inverse(eye(L - 1) - B) * c)[0]
    print('  L=%2d  tau=%s  |a - Gamma(z)|=%s  |a - tanh(tau/2)|=%s  |z - s0/s1|/z=%s  |a|-gamma=%s'
          % (L, nstr(tau, 22), nstr(abs(a_fin - gam(z)), 3), nstr(abs(a_fin - tanh(tau / 2)), 3),
             nstr(abs(z - s0 / s1) / z, 3), nstr(abs(a_fin) - gamma, 6)))
print()

print('E3  reversal: v -> -v and one-site translation (L = 17)')
C = covariance(a_, b_, v_, 17)
Pe, Pf = probs(C)
z = Pe / Pf
Cm = covariance(a_, b_, -v_, 17)
Pem, Pfm = probs(Cm)
Ct = covariance(a_, b_, v_, 17, start=1)
Pet, Pft = probs(Ct)
print('  z(v)*z(-v) - 1 =', nstr(z * (Pem / Pfm) - 1, 3), '  Gamma(v)+Gamma(-v) =', nstr(gam(z) + gam(Pem / Pfm), 3))
print('  z(start 0)*z(start 1) - 1 =', nstr(z * (Pet / Pft) - 1, 3), '  Gamma^2 equal:',
      nstr(gam(z) ** 2 - gam(Pet / Pft) ** 2, 3))
print()

print('E4  protected even block (L = 16): z - 1, Gamma')
C16 = covariance(a_, b_, v_, 16)
Pe16, Pf16 = probs(C16)
print('  z - 1 =', nstr(Pe16 / Pf16 - 1, 3), '  Gamma =', nstr(gam(Pe16 / Pf16), 3))
print()

print('E2  each level a peel step (L = 17); the loop wall on single levels')
nus = eigsy(C, eigvals_only=True)
nus = sorted([nus[i] for i in range(17)])
worst = mpf(0)
inside = []
S_in = mpf(0)
S_all = mpf(0)
for nu in nus:
    eps = log((1 - nu) / nu)
    zi = (1 - nu) / nu
    worst = max(worst, abs((2 * nu - 1) + gam(zi)), abs((2 * nu - 1) + tanh(eps / 2)))
    s = -(nu * log(nu) + (1 - nu) * log(1 - nu))
    S_all += s
    in_wall = abs(eps) < lw
    # equivalent statements of inside: Gamma^2 < 1/2  <->  nu(1-nu) > 1/8
    assert in_wall == (gam(zi) ** 2 < mpf(1) / 2) == (nu * (1 - nu) > mpf(1) / 8)
    if in_wall:
        inside.append(eps)
        S_in += s
print('  max |2nu-1 + Gamma(z_i)| and |2nu-1 + tanh(eps/2)| over 17 levels:', nstr(worst, 3))
print('  wall on one level: |eps| = ln(3+2sqrt2) =', nstr(lw, 20), '; nu window = (2-sqrt2)/4 =', nstr((2 - sqrt(2)) / 4, 15))
print('  levels inside the wall:', [nstr(x, 10) for x in inside], 'of 17')
print('  entanglement entropy carried by inside levels: %s of %s (fraction %s)'
      % (nstr(S_in, 12), nstr(S_all, 12), nstr(S_in / S_all, 8)))
print('  eps range:', nstr(log((1 - nus[0]) / nus[0]), 8), 'to', nstr(log((1 - nus[-1]) / nus[-1]), 8))
print()

print('E7  offset angle and the Two Trees boost')
tau_inf = 2 * atanh(gamma)
chi = 2 * atan(gamma)
print('  sec chi - (1+g^2)/(1-g^2) =', nstr(sec(chi) - (1 + gamma ** 2) / (1 - gamma ** 2), 3),
      '  sec chi - cosh tau =', nstr(sec(chi) - cosh(tau_inf), 3))
zo = (1 + gamma) / (1 - gamma)
print('  2 sec chi - (z + 1/z) =', nstr(2 * sec(chi) - (zo + 1 / zo), 3), '  chi (deg) =', nstr(chi * 180 / mp.pi, 12))
print('  at the wall gamma^2 = 1/2: sec chi =', nstr((1 + mpf(1) / 2) / (1 - mpf(1) / 2), 5),
      ' so trace 2 sec chi = 6 = z_w + 1/z_w:', nstr(wall + 1 / wall, 20))
print()

print('E12 chemistry form of the boundary pair (L = 17): m = s0 (vacancy), p = s1 (occupation)')
B = C[0:16, 0:16]
c = C[0:16, 16]
cxx = C[16, 16]
s1 = cxx - (c.T * inverse(B) * c)[0]
s0 = 1 - cxx - (c.T * inverse(eye(16) - B) * c)[0]
eta_like = (s0 - s1) / 2
chi_like = (s0 + s1) / 2
print('  s0 =', nstr(s0, 15), ' s1 =', nstr(s1, 15))
print('  "hardness"/"electronegativity" = (s0-s1)/(s0+s1) =', nstr(eta_like / chi_like, 20),
      ' = tanh(tau/2) =', nstr(tanh((log(Pe) - log(Pf)) / 2), 20))
print('  "omega/eta" = 1/(2 a^2) =', nstr(1 / (2 * (eta_like / chi_like) ** 2), 12), '(wall at 1)')
print()

print('NEAR-COINCIDENCE (reported, not a connection): reference gamma against sqrt2 - 1 = tan(pi/8)')
print('  gamma - (sqrt2-1) =', nstr(gamma - (sqrt(2) - 1), 8),
      '   tau_inf - ln(1+sqrt2) =', nstr(tau_inf - log(1 + sqrt(2)), 8))
print('  e^tau_inf =', nstr(zo, 15), ' against 1+sqrt2 =', nstr(1 + sqrt(2), 15), '= sqrt(3+2sqrt2), the face apex of the wall')
