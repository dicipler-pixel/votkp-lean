# SCRIPT: KNOT-COMM-8_8 — k = v(t-2) on 8_8's real branches with t near 2, x = 3..12 (200 digits); scaled by s^6
import warnings; warnings.filterwarnings('ignore')
import mpmath as mp, sympy as sp
from census_lib import riley_poly, S_, V_
mp.mp.dps = 200
R = sp.Poly(riley_poly(25, 9), V_); cs = [sp.lambdify(S_, c, 'mpmath') for c in R.all_coeffs()]
for i in range(0, 37):
    x = 3 + 0.25 * i; s = mp.e ** mp.mpf(x)
    rts = mp.polyroots([c(s) for c in cs], maxsteps=3000, extraprec=2000)
    row = []
    for r in rts:
        if abs(mp.im(r)) < mp.mpf(10) ** -90:
            v = mp.re(r); t = s*s + 1/(s*s) - v
            if abs(t - 2) < 0.1: k = v*(t-2); row.append('t-2=%s k=%s k*s^6=%s' % (mp.nstr(t-2, 5), mp.nstr(k, 6), mp.nstr(k*s**6, 6)))
    print('x=%.2f' % x, ' | '.join(row), flush=True)
