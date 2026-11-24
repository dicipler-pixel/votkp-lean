# SCRIPT: HANDED-LIGHT-02  (01 used one frequency on both axes: field and rate were collinear, fit meaningless)
# Does a rotating field read the curvature half of the field-space tensor?
# Tensor: Q_ij = sum_m <0|D_i|m><m|D_j|0> / gap_m^2 = g_ij - (i/2) Omega_ij   (so Omega_xy = -2 Im Q_xy).
# Claim under test: for a slowly changing classical field E(t), the induced dipole is
#     d_i = alpha_ij E_j + c * Omega_ij * dE_j/dt + (higher),   |c| = 1,
# and the real (metric) half does NOT appear at first order in the rate.
# KILL LINES (written before the run):
#  H1 fitted coefficient of dE_y/dt in d_x must equal +/- Omega_xy within 2 percent, and the coefficient of
#     dE_x/dt in d_y must be its negative; otherwise the claim failed this way.
#  H2 coefficients of dE_x/dt in d_x and dE_y/dt in d_y must be below 2 percent of |Omega_xy| (metric half hidden).
#  H3 reversing the handedness must leave the fitted coefficients unchanged (they are properties of the electron),
#     so the sideways dipole itself flips sign.
#  H4 control with real dipole elements: Omega = 0 and the fitted rate coefficients must vanish.
import numpy as np
from scipy.integrate import solve_ivp
rng = np.random.default_rng(11)
n = 4; gaps = np.array([0.0, 1.0, 1.7, 2.6]); H0 = np.diag(gaps)
def herm(real):
    A = rng.normal(size=(n, n)) + (0 if real else 1j) * rng.normal(size=(n, n)); return (A + A.conj().T) / 2
def run(Dx, Dy, hand, w=0.04, eps=2e-3, T=900.0):
    ramp = lambda t: np.sin(np.pi * min(t, 300.0) / 600.0) ** 2
    E = lambda t: eps * ramp(t) * np.array([np.cos(w * t), hand * np.sin(1.37 * w * t + 0.4)])   # two frequencies, so field and rate are independent
    rhs = lambda t, y: -1j * ((H0 - E(t)[0] * Dx - E(t)[1] * Dy) @ y)
    y0 = np.zeros(n, complex); y0[0] = 1
    ts = np.linspace(400, T, 1500)
    sol = solve_ivp(rhs, [0, T], y0, t_eval=ts, rtol=1e-11, atol=1e-13, method='DOP853')
    d = np.array([[np.real(np.vdot(sol.y[:, k], D @ sol.y[:, k])) for D in (Dx, Dy)] for k in range(len(ts))])
    d0 = np.array([np.real(Dx[0, 0]), np.real(Dy[0, 0])]); d = d - d0
    Ev = np.array([E(t) for t in ts]); h = 1e-3; Ed = np.array([(E(t + h) - E(t - h)) / (2 * h) for t in ts])
    X = np.hstack([Ev, Ed]); cx = np.linalg.lstsq(X, d[:, 0], rcond=None)[0]; cy = np.linalg.lstsq(X, d[:, 1], rcond=None)[0]
    return cx, cy
for real in (False, True):
    Dx, Dy = herm(real), herm(real)
    Q = lambda A, B: sum(A[0, m] * B[m, 0] / gaps[m] ** 2 for m in range(1, n))
    Om = -2 * np.imag(Q(Dx, Dy)); gxx, gyy, gxy = np.real(Q(Dx, Dx)), np.real(Q(Dy, Dy)), np.real(Q(Dx, Dy))
    axx = sum(2 * abs(Dx[0, m]) ** 2 / gaps[m] for m in range(1, n))
    print('=== dipole elements', 'REAL (control)' if real else 'COMPLEX')
    print('curvature Omega_xy = %.6f   metric g_xx, g_yy, g_xy = %.4f, %.4f, %.4f   steady polarizability xx = %.4f' % (Om, gxx, gyy, gxy, axx))
    for hand in (+1, -1):
        cx, cy = run(Dx, Dy, hand)
        print(' handedness %+d : d_x on [E_x, E_y, dE_x/dt, dE_y/dt] = %s' % (hand, np.round(cx, 5)))
        print('                 d_y on [E_x, E_y, dE_x/dt, dE_y/dt] = %s' % np.round(cy, 5))
        if not real: print('                 ratio (rate coefficient)/Omega: d_x,dE_y %.4f   d_y,dE_x %.4f   diagonal leak %.4f, %.4f' % (cx[3] / Om, cy[2] / Om, cx[2] / abs(Om), cy[3] / abs(Om)))
