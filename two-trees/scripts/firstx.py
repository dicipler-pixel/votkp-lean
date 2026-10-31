# SCRIPT: KNOT-COMM-FIRSTX — 80-digit check of the float scan's first band entry x1 for every knot:
# at x1 some real branch has 0<k<4 (k = v(tr ab - 2), elliptic iff 0<k<4), at x1-0.005 none does.
# Never-enter knots: max k over all real branches at 120 sample x in (0,6] must be <= 0.
# Kill condition: an entering knot with no band point at x1, or a never-enter knot with max k > 0 that survives 80 digits.
import warnings; warnings.filterwarnings('ignore')
import mpmath as mp, sympy as sp, json
from census_lib import riley_poly, S_, V_
mp.mp.dps = 80
d = json.load(open('band_out.json')); res = {}
NEVER = {'T(2,3)', 'T(2,5)', 'T(2,7)', '6_3', '7_5', '8_7', '8_8'}
def ks(cs, x):
    s = mp.e ** mp.mpf(x); rts = mp.polyroots([c(s) for c in cs], maxsteps=1500, extraprec=800)
    return [mp.re(r) * (s*s + 1/(s*s) - mp.re(r) - 2) for r in rts if abs(mp.im(r)) < mp.mpf(10) ** -40]
for name, e in d.items():
    R = sp.Poly(riley_poly(e['p'], e['q']), V_); cs = [sp.lambdify(S_, c, 'mpmath') for c in R.all_coeffs()]
    if name in NEVER:
        mx = max([max([float(k) for k in ks(cs, 0.05 * i)] or [-9e9]) for i in range(1, 121)])
        res[name] = dict(enters=False, max_k=mx); print(name, 'never: max k over 120 samples =', mx, flush=True)
    else:
        x1 = e['first'][0]
        a = [float(k) for k in ks(cs, x1) if 0 < k < 4]; b = [float(k) for k in ks(cs, round(x1 - 0.005, 3)) if 0 < k < 4]
        res[name] = dict(enters=True, x1=x1, in_band_at_x1=a, in_band_before=b); print(name, 'x1', x1, 'k at x1', a, 'before', b, flush=True)
json.dump(res, open('firstx_out.json', 'w'), indent=1)
