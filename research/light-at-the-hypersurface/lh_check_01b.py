# SCRIPT: LH-CHECK-01b
# Re-run of the two lines killed in lh_check_01.out, same kill lines (K6 > 1e-12, K18 > 1e-8). Causes found in the CHECK:
#  K6: the Python transfer matrix used the time convention e^{+iωt}; the page and Lean film_is_oplus use x = r12 e^{2iφ}.
#      With opposite conventions r comes out as the complex conjugate. Fix: same convention (layer phase −φ); both forms are reported.
#  K18: the grid search was confined to arc lengths −0.3 to 1.2 on two lines of the planes, and the feet run far out as g → 1.
#      Fix: minimise over the whole of both planes (two parameters each) with scipy, from several starts.
# Opposite runs under the same lines: a wrong reflection (Γ ⊖ x) is killed by K6; a wrong distance arccosh(g²) is killed by K18.
import numpy as np, math
from scipy.optimize import minimize
rng = np.random.default_rng(20261116); eta = np.diag([1.,-1,-1,-1]); mk = lambda p,q: float(p@eta@q)
def TM(Ys, ph, sgn):
    Mt = np.eye(2, dtype=complex)
    for k in range(1, len(Ys)-1):
        c, s = np.cos(sgn*ph[k]), np.sin(sgn*ph[k]); Mt = Mt @ np.array([[c, 1j*s/Ys[k]],[1j*Ys[k]*s, c]])
    A = Mt @ np.array([1, Ys[-1]]); t = 2/(A[0] + A[1]/Ys[0]); return t*A[0] - 1, t
def rec(Ys, ph, wrong=False):
    g = [(Ys[k]-Ys[k+1])/(Ys[k]+Ys[k+1]) for k in range(len(Ys)-1)]; rho = g[-1]
    for k in range(len(g)-2, -1, -1):
        x = rho*np.exp(2j*ph[k+1]); rho = (g[k] - x)/(1 - g[k]*x) if wrong else (g[k] + x)/(1 + g[k]*x)
    return rho
e = e_conj = e_flux = e_wrong = 0
for _ in range(2000):
    D = rng.integers(2,7); Ys = np.exp(rng.uniform(-1.5,1.5,D+1)); ph = rng.uniform(0,6,D+1)
    r, t = TM(Ys, ph, -1); rc, _ = TM(Ys, ph, +1); rr = rec(Ys, ph)
    e = max(e, abs(rr - r)); e_conj = max(e_conj, abs(rr - np.conj(rc))); e_flux = max(e_flux, abs(abs(r)**2 + (Ys[-1]/Ys[0])*abs(t)**2 - 1)); e_wrong = max(e_wrong, abs(rec(Ys, ph, True) - r))
out = []
def line(k, v, tol, note, ok=None): ok = (v <= tol) if ok is None else ok; out.append(('HOLDS ' if ok else 'KILLED') + f'  {k:<4} {v:>10.2e}  tol {tol:<8}  {note}')
line('K6', max(e, e_flux), 1e-12, 'recursion by ⊕ = transfer matrix in the same phase convention; flux in = flux out')
line('K6', e_conj, 1e-12, 'with the opposite convention the transfer matrix gives exactly the complex conjugate')
line('K6', e_wrong, 1e-12, 'opposite: Γ ⊖ x must be killed', ok=e_wrong > 1e-12)
def plane_pt(N, a, b):
    # a point on the plane <Y,N> = 0: start from the foot nearest O and move along two orthonormal tangent directions
    n = N[1:]/np.linalg.norm(N[1:]); h = math.asinh(N[0]); F = np.r_[math.cosh(h), math.sinh(h)*n]
    e1 = np.cross(n, [0,0,1.]) if abs(n[2]) < 0.9 else np.cross(n, [1.,0,0]); e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
    v = a*np.r_[0, e1] + b*np.r_[0, e2]; s = math.hypot(a, b)
    if s < 1e-15: return F
    u = v/s; u = u + mk(u, F)*F  # already tangent at F
    return math.cosh(s)*F + math.sinh(s)*u
ed = ew = 0
for _ in range(60):
    ha, hb = rng.uniform(0.05, 2, 2); g = math.sinh(ha)*math.sinh(hb)
    if g <= 1.02: continue
    Na = np.array([math.sinh(ha), math.cosh(ha), 0, 0]); Nb = np.array([math.sinh(hb), 0, math.cosh(hb), 0])
    f = lambda q: math.acosh(max(1.0, mk(plane_pt(Na, q[0], q[1]), plane_pt(Nb, q[2], q[3]))))
    best = min((minimize(f, rng.normal(size=4)*0.8, method='Nelder-Mead', options={'xatol':1e-13, 'fatol':1e-15, 'maxiter':40000, 'maxfev':40000}).fun for _ in range(6)))
    ed = max(ed, abs(best - math.acosh(g))); ew = max(ew, abs(best - math.acosh(g*g)))
line('K18', ed, 1e-8, 'minimum distance between separated planes = arccosh g (Nelder–Mead over both planes, 6 starts)')
line('K18', ew, 1e-8, 'opposite: arccosh(g²) must be killed', ok=ew > 1e-8)
print('\n'.join(out))
