# SCRIPT: RUBIDIUM-HANDED-CHECKS-01  two side checks on RUBIDIUM-HANDED-02
# (a) does the curvature vanish when the two lines are not split (equal gaps, strength ratio exactly 2)?
# (b) steady polarizability with the calibrated background, for comparison with the published value.
import numpy as np, importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location('r', 'rubidium_handed.py'); r = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(r)
print('steady polarizability, two lines + background: %.2f atomic units' % (r.plain(0.0) + r.bg))
def curv(E1, E2, ratio):
    red = {r.R_(1, 2): r.d1, r.R_(3, 2): np.sqrt(ratio)*r.d1}; gap = np.array([E1 if e[0] == r.R_(1, 2) else E2 for e in r.ex])
    dq = {q: np.array([r.sph(Jp, mp, q, red[Jp]) for (Jp, mp, E, _) in r.ex]) for q in (-1, 1)}
    Dx = (dq[-1] - dq[1])/np.sqrt(2); Dy = 1j*(dq[-1] + dq[1])/np.sqrt(2)
    return -2*np.imag(np.sum(np.conj(Dx)*Dy/gap**2)), np.real(np.sum(abs(Dx)**2/gap**2))
for lab, a in (('real rubidium', (r.E1, r.E2, r.ratio)), ('same gaps, real strength ratio', (r.E1, r.E1, r.ratio)), ('same gaps, strength ratio exactly 2', (r.E1, r.E1, 2.0)), ('real gaps, strength ratio exactly 2', (r.E1, r.E2, 2.0))):
    c, g = curv(*a); print('%-38s curvature %.4f   metric %.2f   curvature/metric %.5f' % (lab, c, g, c/g))
print('fractional line splitting (E2-E1)/E1 = %.5f' % ((r.E2 - r.E1)/r.E1))
