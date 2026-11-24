# SCRIPT: SQUARED-MAP-MASS-BREAK-01
# Your August prediction: break the mass symmetry and a cone with holonomy -1 appears
# for the squared-distance operator (which has NO cone at equal masses).
# KILL LINE (before the run): if for unequal masses the gap of the squared-distance operator has no zero
# near the equilateral shape, or every zero found has holonomy +1, the prediction failed this way.
import numpy as np, importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location('g', 'gaps_totals_check.py')
g = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(g)
from scipy.optimize import minimize

def conf(p):  # triangle with two vertices fixed, third free: a chart on shapes
    return np.array([[0.0, 0.0], [1.0, 0.0], [p[0], p[1]]])

def gap(p, m, squared=True):
    w = np.linalg.eigvalsh(g.gram(g.normalise(conf(p), m), m, squared)); return w[-1] - w[-2]

def holonomy(p0, m, r, squared=True):
    prev = None; first = None
    for phi in np.linspace(0, 2 * np.pi, 361):
        p = (p0[0] + r * np.cos(phi), p0[1] + r * np.sin(phi))
        w, V = np.linalg.eigh(g.gram(g.normalise(conf(p), m), m, squared)); u = V[:, -1]
        if prev is not None and np.dot(u, prev) < 0: u = -u
        if first is None: first = u
        prev = u
    return float(np.dot(first, prev))

eq = np.array([0.5, np.sqrt(3) / 2])
for mm in ((1, 1, 1), (1, 1, 1.3), (1, 1, 2), (1, 2, 3)):
    m = np.array(mm, float); found = []
    rng = np.random.default_rng(1)
    for _ in range(40):
        s = eq + rng.normal(scale=0.35, size=2)
        res = minimize(gap, s, args=(m,), method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-13, maxiter=4000))
        if res.fun < 1e-5 and res.x[1] > 0.05 and not any(np.linalg.norm(res.x - f) < 1e-3 for f in found):
            found.append(res.x)
    print('masses', mm, ' zeros of the squared-map gap (upper half):', len(found))
    for f in found:
        print('   at third vertex', np.round(f, 5), ' gap', '%.1e' % gap(f, m), ' distance from equilateral chart point', round(float(np.linalg.norm(f - eq)), 5),
              ' holonomy r=0.01:', round(holonomy(f, m, 0.01), 4), ' big loop r=0.6 about equilateral:', round(holonomy(eq, m, 0.6), 4))
