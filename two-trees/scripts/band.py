# SCRIPT: KNOT-COMM-BAND
# Where does a two-bridge knot's real Riley curve meet the band where the meridian commutator is a rotation?
# Identity (checked on 5,243 samples and proved in Lean): tr[a,b] = 2 - v((s - 1/s)^2 - v).
# So [a,b] is elliptic  <=>  |tr| < 2  <=>  0 < v(Z - 2) < 4 with Z - 2 = (s - 1/s)^2 - v = tr(ab) - 2,
# i.e. v > 0, tr(ab) > 2 and v (tr(ab) - 2) < 4.
import warnings; warnings.filterwarnings('ignore')
import json, math, numpy as np, sympy as sp
from census_lib import riley_poly, alexander, eps, S_, V_, T
KN = [(n, k['p'], k['q']) for n, k in [(k['name'], k) for k in json.load(open('../../../atlas_sm/knot3d/data_v2.json'))['knots']]]
xs = np.concatenate([np.linspace(1e-4, 0.05, 60), np.arange(0.05, 6.0, 0.005)])
out = {}
for name, p, q in KN:
    R = sp.Poly(riley_poly(p, q), V_)
    cf = [sp.lambdify(S_, c, 'numpy') for c in R.all_coeffs()]
    ent, pts = [], 0
    vmin_pos = None
    for x in xs:
        s = math.exp(x); co = [complex(f(s)) if callable(f) else complex(f) for f in cf]
        co = [c.real for c in co]
        for v in np.roots(co):
            if abs(v.imag) > 1e-9 * max(1, abs(v)): continue
            v = v.real; pts += 1
            A = (s - 1 / s) ** 2; tr = 2 - v * (A - v)
            if abs(tr) < 2: ent.append((round(x, 4), round(v, 5), round(tr, 5)))
    D = sp.Poly(alexander(p, q), T); r = [complex(z) for z in sp.Poly(D).nroots(n=30)]
    off = sum(1 for z in r if abs(abs(z) - 1) > 1e-8)
    det = abs(int(D.eval(-1)))
    sig = sum(eps(p, q))   # sum of the eps signs (two-bridge: signature is a known function of these; recorded raw)
    out[name] = dict(p=p, q=q, real_points=pts, enters=len(ent) > 0, first=ent[0] if ent else None, last=ent[-1] if ent else None,
                     det=det, alex_offcircle_roots=off, eps_sum=sig, alexander=str(D.as_expr()))
    print('%-7s p/q=%d/%d  enters=%-5s  first=%-28s det=%-3d off-circle Alexander roots=%d  sum eps=%+d' % (
        name, p, q, len(ent) > 0, str(ent[0]) if ent else '-', det, off, sig), flush=True)
json.dump(out, open('band_out.json', 'w'), indent=1)
