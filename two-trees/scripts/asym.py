# SCRIPT: KNOT-COMM-ASYM — limits of k = v(tr ab - 2) on every real branch as x -> infinity (x = 6, 9, 12; 200 digits)
import warnings; warnings.filterwarnings('ignore')
import mpmath as mp, sympy as sp, json
from census_lib import riley_poly, S_, V_
d = json.load(open('band_out.json')); out = {}
mp.mp.dps = 200
for name, e in d.items():
    R = sp.Poly(riley_poly(e['p'], e['q']), V_); cs = [sp.lambdify(S_, c, 'mpmath') for c in R.all_coeffs()]
    rows = {}
    for x in [6, 9, 12]:
        s = mp.e ** mp.mpf(x); rts = mp.polyroots([c(s) for c in cs], maxsteps=2000, extraprec=1500)
        ks = []
        for r in rts:
            if abs(mp.im(r)) < mp.mpf(10) ** -80:
                v = mp.re(r); t = s*s + 1/(s*s) - v; ks.append((float(t), mp.nstr(v*(t-2), 8)))
        rows[x] = sorted(ks, key=lambda z: -z[0])
    out[name] = {str(k): [list(z) for z in v] for k, v in rows.items()}
    small = [(t, k) for t, k in rows[12] if abs(float(k)) < 10]
    print('%-7s x=12 branches with |k|<10 (t, k):' % name, small, flush=True)
json.dump(out, open('asym_out.json', 'w'), indent=1)
