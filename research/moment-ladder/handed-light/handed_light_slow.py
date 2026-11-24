# SCRIPT: HANDED-LIGHT-03  same test at half the frequency.
# Reason: in HANDED-LIGHT-02 one ratio missed the 2 percent line (1.0233). If the miss is the next rung (order frequency squared),
# halving the frequency must cut it about four-fold. KILL LINE: if the miss does not shrink, the claim failed this way.
import numpy as np, importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location('h', 'handed_light.py'); h = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(h)
h.rng = np.random.default_rng(11); Dx, Dy = h.herm(False), h.herm(False)
Om = -2*np.imag(sum(Dx[0, m]*Dy[m, 0]/h.gaps[m]**2 for m in range(1, h.n)))
for w, T in ((0.04, 900.0), (0.02, 1700.0), (0.01, 3300.0)):
    cx, cy = h.run(Dx, Dy, +1, w=w, T=T)
    print('frequency %.2f : ratios %.4f  %.4f   diagonal leak %.4f %.4f' % (w, cx[3]/Om, cy[2]/Om, cx[2]/abs(Om), cy[3]/abs(Om)))
