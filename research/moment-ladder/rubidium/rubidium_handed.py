# SCRIPT: RUBIDIUM-HANDED-02  (01 had the hartree-to-terahertz constant off by 1000 and did not finish)
# Rubidium-87 ground state (5S, J = 1/2, m_J = +1/2, the F = m = 2 stretched state) with its two strong lines.
# Both halves of the field-space response from the same dipole matrix elements, compared with
# the measured tune-out for circular light: 785.1522(3) nm (Phys. Rev. A 105, L030802, 2022).
# KILL LINE (written before the run): with the background constant fixed on the plain tune-out 790.03235 nm,
# the predicted handed tune-out must be within 0.01 nm of 785.1522 nm; otherwise it failed this way.
import numpy as np
from sympy.physics.wigner import wigner_3j
from sympy import Rational as R_
from scipy.optimize import brentq
HART_NM = 45.563352529          # hartree energy <-> vacuum wavelength in nm
THZ = 1.0/6579.683920502        # hartree per terahertz (one hartree is 6579.68392 terahertz)
f_D1, f_D2 = 377.107463380, 384.230484468      # line centres, THz (Steck, rubidium 87 line data)
hf = 2.563005979e-3             # F = 2 ground level sits this many THz above the centroid
E1, E2 = (f_D1 - hf)*THZ, (f_D2 - hf)*THZ
d1 = 4.234; ratio = 1.99217; d2 = np.sqrt(ratio)*d1      # reduced elements (atomic units); ratio of squares, from the paper
C = 0.9931                      # effective circular fraction of the experiment (Stokes parameter times field alignment)
# states: ground |1/2, +1/2>; excited J' = 1/2 (2 states, gap E1) and J' = 3/2 (4 states, gap E2)
def sph(Jp, mp, q, red):        # <J' m'| d_q |1/2 1/2>
    return float((-1)**(Jp - mp) * wigner_3j(Jp, 1, R_(1, 2), -mp, q, R_(1, 2))) * red
ex = [(R_(1, 2), m, E1, d1) for m in (R_(-1, 2), R_(1, 2))] + [(R_(3, 2), m, E2, d2) for m in (R_(-3, 2), R_(-1, 2), R_(1, 2), R_(3, 2))]
gap = np.array([e[2] for e in ex])
dq = {q: np.array([sph(Jp, mp, q, red) for (Jp, mp, E, red) in ex]) for q in (-1, 0, 1)}
Dx = (dq[-1] - dq[1])/np.sqrt(2); Dy = 1j*(dq[-1] + dq[1])/np.sqrt(2); Dz = dq[0] + 0j     # <m|D_x|0>, <m|D_y|0>, <m|D_z|0>
def alpha(e, w, bg=0.0):        # light shift is -(1/4)|field|^2 * alpha
    a = e[0]*Dx + e[1]*Dy + e[2]*Dz; b = np.conj(e[0])*Dx + np.conj(e[1])*Dy + np.conj(e[2])*Dz
    return float(np.sum(abs(a)**2/(gap - w) + abs(b)**2/(gap + w))) + bg
lin = np.array([1, 0, 0], complex); sm = np.array([1, -1j, 0])/np.sqrt(2); sp = np.array([1, 1j, 0])/np.sqrt(2)
plain = lambda w, bg=0.0: 0.5*(alpha(sm, w) + alpha(sp, w)) + bg
handed = lambda w: 0.5*(alpha(sm, w) - alpha(sp, w))
w_of = lambda lam: HART_NM/lam; lam_of = lambda w: HART_NM/w
print('check: plain part equals linear light:', plain(w_of(790.0)), alpha(lin, w_of(790.0)))
# the tensor on rung -3 (two-line model): Q_ij = sum <0|D_i|m><m|D_j|0>/gap^2 = g - (i/2) Omega
Q = lambda A, B: np.sum(np.conj(A)*B/gap**2)
gxx, Om = np.real(Q(Dx, Dx)), -2*np.imag(Q(Dx, Dy))
print('metric g_xx = %.4f   curvature Omega_xy = %.4f   (atomic units)   steady polarizability = %.3f' % (gxx, Om, plain(0.0)))
print('curvature / metric = %.5f' % (Om/gxx))
# plain tune-out, two lines only, then the background that puts it on the measured value
t0 = brentq(lambda lam: plain(w_of(lam)), 781.0, 794.5)
bg = -plain(w_of(790.03235))
print('plain tune-out, two lines only: %.4f nm   (measured 790.03235)   background needed: %.3f atomic units' % (t0, bg))
total = lambda lam, bg, C: plain(w_of(lam), bg) + C*handed(w_of(lam))
for label, b in (('two lines only', 0.0), ('with calibrated background', bg)):
    lam = brentq(lambda L: total(L, b, C), 781.0, 794.5)
    print('handed tune-out, %s: %.4f nm   measured 785.1522(3)   miss %+.4f nm' % (label, lam, lam - 785.1522))
lamc = brentq(lambda L: total(L, bg, C), 781.0, 794.5); w = w_of(lamc)
print('at that wavelength: plain part %.1f, handed part %.1f (atomic units); paper quotes 12347.7 and 24716.8/2 = %.1f for its vector term' % (plain(w, bg), handed(w), 24716.8/2))
print('sign test: opposite handedness gives a zero at', end=' ')
try: print('%.4f nm' % brentq(lambda L: total(L, bg, -C), 781.0, 794.5))
except ValueError: print('no wavelength between the lines (the two parts add instead of cancelling)')
print('handed part at tune-out / (frequency * curvature) = %.1f  -> near the lines the higher odd rungs dominate' % (handed(w)/(w*Om)))
for ww in (1e-4, 1e-3, 5e-3):
    print('  low frequency %.0e: handed/(frequency*curvature) = %.6f' % (ww, handed(ww)/(ww*Om)))
print('sensitivity: 1e-4 change in circular fraction moves the handed tune-out by %.5f nm' % (brentq(lambda L: total(L, bg, C+1e-4), 781.0, 794.5) - lamc))
