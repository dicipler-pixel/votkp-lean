# SCRIPT: LEDGER  kinetic-model ledger L(eps) for a given collision history (same kept-sector model as paper/code/main/memory_curve.py)
# Model: Legendre moments a_l(k, tau) of one comoving Fourier mode k (units 1/r_m), tau = eps = conformal time in units of r_m.
#   da/dtau = -i k M a - K(tau) (1-P0) a,   K(tau) = (kappa/H)(tau)/tau,   a_l(tau0) = delta_l0,  tau0 = eps0 = 0.1
# Kept population S(tau) = sum_k w_k |a_0|^2, w_k ~ k^2 exp(-k^2/2) (Gauss-Legendre on [0.25, 9], 36 nodes, as memory_curve.py).
# Collisions never touch a_0, so dS/dtau = -sum_k w_k 2 k M01 Re(i conj(a0) a1): the ONLY pen is the density-flux link.
# Ledger: L(tau) = -dS/dtau ; the ledger written in a window [e1,e2] is S(e1)-S(e2).
import os
os.environ['OMP_NUM_THREADS'] = '1'
import numpy as np, scipy.sparse as sp
from scipy.integrate import solve_ivp
from scipy.special import roots_legendre
import sys
sys.path.insert(0, __import__('os').environ.get('MCCORMICK_SIM', 'PBH_neutrino_simulation/simulation')); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_burst import make_kH
kn, kw = roots_legendre(36); kmin, kmax = 0.25, 9.0
ks = 0.5*(kmax-kmin)*(kn+1)+kmin; wk = 0.5*(kmax-kmin)*kw
wE = wk*ks**2*np.exp(-ks**2/2); wE /= wE.sum()
LM = 60; NL = LM+1
d = np.array([l/np.sqrt(4.0*l*l-1) for l in range(1, LM+1)])
Mm = sp.diags([d, d], [-1, 1], format='csr')
Q = sp.diags(np.r_[0.0, np.ones(LM)], format='csr')
TAU0 = 0.1; CAP = 5e5
def breakpoints(h):
    b = []
    for a, c, v in h.get('windows', []): b += [a, c]
    return sorted(set(x for x in b if x > TAU0))
def S_curve(h, tg, rtol=1e-8, atol=1e-11):
    """S(tau) on grid tg (sorted, >= TAU0). Integrates piecewise between window edges."""
    kH = make_kH(h)
    Kf = lambda t: min(kH(t), CAP)/t
    edges = [TAU0] + [x for x in breakpoints(h) if x < tg[-1]] + [tg[-1]]
    S = np.zeros(len(tg))
    for k, w in zip(ks, wE):
        y = np.zeros(NL, complex); y[0] = 1.0
        A0 = -1j*k*Mm
        out = np.zeros(len(tg), complex)
        for a, b in zip(edges[:-1], edges[1:]):
            mid = 0.5*(a+b)
            # constant-in-window part handled exactly by the rate function; evaluate K strictly inside the piece
            def Kp(t, a=a, b=b): return Kf(min(max(t, a*(1+1e-12)), b*(1-1e-12)))
            fun = lambda t, v: (A0 - Kp(t)*Q) @ v
            jac = lambda t, v: (A0 - Kp(t)*Q).tocsc()
            te = [x for x in tg if a <= x <= b]
            s = solve_ivp(fun, (a, b), y, method='BDF', jac=jac, t_eval=te if te else None, rtol=rtol, atol=atol)
            assert s.success, s.message
            for x, col in zip(s.t, s.y.T):
                out[np.searchsorted(tg, x)] = col[0]
            y = s.y[:, -1]
        S += w*np.abs(out)**2
    return S
GRID = np.unique(np.r_[np.geomspace(TAU0, 14.0, 400), TAU0])
