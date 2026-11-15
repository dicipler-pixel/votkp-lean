# SCRIPT: SCHRODINGER-QGT-01
# Claim under test: Schrödinger's 1920 colour line element
#     ds^2 = (1/h) * sum_i a_i dx_i^2 / x_i ,   h = sum_i a_i x_i      (Roberti & Peruzzi 2023, eq. 7)
# splits EXACTLY into a brightness part and a chromatic part, and the chromatic part is
# 4 x the quantum (Fubini-Study) metric of the real "colour amplitude" state psi_i = sqrt(a_i x_i / h):
#     ds^2 = (d ln h)^2 + 4 * g_FS(psi),   g_FS = <dpsi|dpsi> - <psi|dpsi>^2 .
# WHY THIS CHECK PROVES IT: (A) is a symbolic identity in arbitrary positive x_i and arbitrary dx_i —
# if the difference simplifies to 0 the split holds everywhere, for any a_i. (B) checks a consequence
# stated independently in the history literature (Roberti & Peruzzi): geodesics from a white point to the
# three fundamental colours are straight lines in the chromaticity diagram, others curved. On a sphere
# that follows because great circles through a vertex keep the other two amplitudes in fixed ratio.
# KILL CONDITION: (A) residual not identically 0, or (B) straight-line deviation for vertex geodesics
# not at round-off while a generic geodesic bends by > 1e-3.
import sympy as sp, numpy as np, json

x = sp.symbols('x1:4', positive=True); dx = sp.symbols('dx1:4', real=True); a = sp.symbols('a1:4', positive=True)
h = sum(ai * xi for ai, xi in zip(a, x)); dh = sum(ai * dxi for ai, dxi in zip(a, dx))
ds2 = sum(ai * dxi**2 / xi for ai, xi, dxi in zip(a, x, dx)) / h
p = [ai * xi / h for ai, xi in zip(a, x)]
dp = [sum(sp.diff(pi, xj) * dxj for xj, dxj in zip(x, dx)) for pi in p]
psi = [sp.sqrt(pi) for pi in p]
dpsi = [sum(sp.diff(si, xj) * dxj for xj, dxj in zip(x, dx)) for si in psi]
gFS = sum(d**2 for d in dpsi) - sum(s * d for s, d in zip(psi, dpsi))**2
resA = sp.simplify(ds2 - ((dh / h)**2 + 4 * gFS))
resFisher = sp.simplify(ds2 - ((dh / h)**2 + sum(d**2 / pi for d, pi in zip(dp, p))))
print('A: ds2 - [(dln h)^2 + 4 gFS] =', resA)
print('A2: ds2 - [(dln h)^2 + Fisher-Rao] =', resFisher)

# (B) geodesics on the positive octant of the unit sphere psi (great circles), mapped to chromaticity p = psi^2
def great_circle(u, v, n=400):
    u = u / np.linalg.norm(u); v = v - (v @ u) * u; v /= np.linalg.norm(v)
    return u, v
def path(p0, p1, n=401):
    s0, s1 = np.sqrt(p0), np.sqrt(p1)
    th = np.arccos(np.clip(s0 @ s1, -1, 1)); t = np.linspace(0, 1, n)
    S = (np.sin((1 - t)[:, None] * th) * s0 + np.sin(t[:, None] * th) * s1) / np.sin(th)
    return S**2  # chromaticity coordinates (sum to 1)
def max_dev_from_chord(P):
    A, B = P[0], P[-1]; d = B - A; d /= np.linalg.norm(d)
    R = P - A; perp = R - np.outer(R @ d, d)
    return float(np.max(np.linalg.norm(perp, axis=1)))
white = np.array([1, 1, 1]) / 3.0
out = {}
for i, name in enumerate(['fundamental 1', 'fundamental 2', 'fundamental 3']):
    e = np.zeros(3); e[i] = 1.0
    out['white->' + name] = max_dev_from_chord(path(white, e))
out['white->(0.6,0.35,0.05)'] = max_dev_from_chord(path(white, np.array([0.6, 0.35, 0.05])))
out['white->(0.1,0.45,0.45)'] = max_dev_from_chord(path(white, np.array([0.1, 0.45, 0.45])))
print('B: max deviation from straight chord in chromaticity triangle:', json.dumps(out, indent=1))
# Curvature of the chromatic part: sphere of radius 2 (since 4 g_FS = (2)^2 * round metric) -> Gaussian curvature 1/4
print('chromatic sheet = sphere radius 2, Gaussian curvature 1/4; brightness direction flat (product metric R x S^2)')
ok = (resA == 0) and (resFisher == 0) and all(out['white->fundamental %d' % k] < 1e-12 for k in (1, 2, 3)) \
     and out['white->(0.6,0.35,0.05)'] > 1e-3
print('VERDICT:', 'PASS' if ok else 'FAIL')
