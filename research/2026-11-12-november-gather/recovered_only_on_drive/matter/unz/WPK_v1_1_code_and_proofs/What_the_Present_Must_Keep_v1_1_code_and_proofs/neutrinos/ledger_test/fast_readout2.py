# SCRIPT: FAST-READOUT2  (FAST-READOUT generalised: baseline prefix, probe prefix and output file as arguments)
# burst -> equivalent initial-amplitude shift by matching the compaction history C_max(eps) to the baseline family
# For a burst run at delta0, at each readout epoch eps_r after the burst, find delta_equiv with C_base(delta_equiv; eps_r) = C_burst(eps_r)
# (linear interpolation across the baseline family, which must be monotone in delta at eps_r). Delta delta_c = delta0 - delta_equiv.
# The readout is trusted only if delta_equiv is flat in eps_r (the burst has then projected onto the growing mode only).
import json, sys, numpy as np
BP, PP, OUT = sys.argv[1], sys.argv[2], sys.argv[3]; fn = sys.argv[4:]
R = {}
for f in fn:
    for l in open(f):
        r = json.loads(l); R[r['tag']] = r
B = sorted([r for t, r in R.items() if t.startswith(BP) and r.get('N') == 400], key=lambda r: r['d'])
def Cat(r, e):
    E = np.array(r['hist_eps']); C = np.array(r['hist_C'])
    return np.interp(e, E, C) if e <= E[-1] else np.nan
EPSR = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.3]
def readout(r, eend):
    row = {}
    for er in EPSR:
        if er < eend + 0.25: continue
        cb = np.array([Cat(b, er) for b in B]); db = np.array([b['d'] for b in B]); ok = np.isfinite(cb)
        cb, db = cb[ok], db[ok]; c = Cat(r, er)
        if len(cb) < 3 or not np.isfinite(c) or np.any(np.diff(cb) <= 0): row[er] = None; continue
        if c < cb[0] or c > cb[-1]: row[er] = 'out'; continue
        row[er] = float(r['d'] - np.interp(c, cb, db))
    return row
out = {}
print('baselines:', [(b['d'], b['status'], round(b['eps'], 2)) for b in B])
for er in EPSR: print('  eps_r %.1f  C_base:' % er, ' '.join('%.5f' % Cat(b, er) for b in B))
for t, r in sorted(R.items()):
    if not t.startswith(PP): continue
    w = r['hspec']['windows']; eend = max(x[1] for x in w)
    row = readout(r, eend); out[t] = dict(status=r['status'], eps_end=r['eps'], readout=row)
    print(t, r['status'], 'eps_end=%.2f' % r['eps'], ' '.join('%.1f:%s' % (k, ('%.5f' % v) if isinstance(v, float) else v) for k, v in row.items()))
json.dump(out, open(OUT, 'w'), indent=1)
