# SCRIPT: PAIR-FAMILIES-SIEVE-01
# Segmented numpy sieve to N; saves pair starts p with p and p+g both prime (g = 2, 4, 6), p + g <= N.
import numpy as np, os, sys, time
OUT = os.path.dirname(os.path.abspath(__file__))
N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**9
t0 = time.time()
R = int(N ** .5) + 2
s = np.ones(R + 1, bool); s[:2] = False
for i in range(2, int(R ** .5) + 1):
    if s[i]: s[i * i::i] = False
base = np.nonzero(s)[0]
seg = 2 * 10**7; G = (2, 4, 6); out = {g: [] for g in G}
for lo in range(0, N + 1, seg):
    hi = min(lo + seg + 6, N + 1)          # 6 extra cells so pairs straddling the cut are seen once
    m = np.ones(hi - lo, bool)
    if lo == 0: m[:2] = False
    for p in base:
        if p * p >= hi: break
        st = max(p * p, ((lo + p - 1) // p) * p)
        m[st - lo::p] = False
    own = min(seg, hi - lo)                 # starts owned by this segment: lo <= p < lo + seg
    for g in G:
        if hi - lo <= g: continue
        k = min(own, hi - lo - g)
        idx = np.nonzero(m[:k] & m[g:g + k])[0] + lo
        out[g].append(idx)
for g in G:
    a = np.concatenate(out[g]).astype(np.int64)
    np.save(os.path.join(OUT, 'pairs_g%d_%d.npy' % (g, N)), a)
    print('g=%d  pairs with p+g <= %d: %d   first: %s' % (g, N, len(a), a[:12].tolist()))
print('sieve seconds %.1f' % (time.time() - t0))
