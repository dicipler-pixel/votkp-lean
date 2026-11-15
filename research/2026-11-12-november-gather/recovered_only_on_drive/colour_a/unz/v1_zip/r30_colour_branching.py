# SCRIPT: R30_COLOUR_BRANCHING
# Does the population's colour (its two-book balance at the previous step) guide the next branching?
# Left half of Rule 30 driven by the 0101 center, every valid row at widths 12..40, both phases.
# At step j past the wall: N_j rows alive, k_j of them pass (the pass book E+ = k_j/N_j, the fail book E- = 1 - E+).
# COIN model: each step is a fair split, p = 1/2.
# COLOUR model: the split follows the previous step's books, p = E+_(j-1) (clipped to [0.05, 0.95]).
# Score = log-likelihood of the observed k_j under Binomial(N_j, p); higher is better.
# KILL (written before the run): if on FINAL steps (N_j <= 16) the colour model does not beat the coin model,
# colour does not guide the final branching. OPPOSITE RUN: the same on EARLY steps (N_j >= 512).
import numpy as np, json
from math import lgamma, log
def run(n, phase, H=200):
    c = (lambda t: t % 2 == 1) if phase == 'A' else (lambda t: t % 2 == 0)
    frees = [d for d in range(1, n + 1) if not c(d - 1)]
    K = len(frees); N = 1 << K; idx = np.arange(N)
    Z = np.zeros(N, bool); O = ~Z
    alive = O.copy(); passed = np.zeros(N, np.int32); diag = {}
    for d in range(1, H + 1):
        base = ((idx >> frees.index(d)) & 1).astype(bool) if d in frees else Z
        row = [base]
        for s in range(1, d):
            j = d - s
            e = (O if c(s - 1) else Z) if j == 1 else diag[d - 2][s - 1]
            row.append(row[s - 1] ^ (diag[d - 1][s - 1] | e))
        if c(d - 1):
            fix = (O if not c(d) else Z) ^ row[d - 1]
            row = [r ^ fix for r in row]
            if d > n: alive &= ~fix
            passed += alive
        diag[d] = row
        if d > 3: del diag[d - 3]
        if not alive.any(): break
    r0 = sum(1 for t in range(n) if c(t))
    post = passed - r0
    S = [int((post >= j).sum()) for j in range(0, int(post.max()) + 2)]
    return S
def ll(k, Nn, p):
    return lgamma(Nn + 1) - lgamma(k + 1) - lgamma(Nn - k + 1) + k * log(p) + (Nn - k) * log(1 - p)
rows = []
for ph in 'AB':
    for n in range(12, 41, 2):
        S = run(n, ph)
        for j in range(1, len(S) - 1):
            Nj, kj = S[j], S[j + 1]; Np, kp = S[j - 1], S[j]
            if Nj == 0 or Np == 0: continue
            prev = min(max(kp / Np, 0.05), 0.95)
            rows.append(dict(ph=ph, n=n, j=j, N=Nj, k=kj, prevE=kp / Np, E=kj / Nj,
                             ll_coin=ll(kj, Nj, 0.5), ll_colour=ll(kj, Nj, prev)))
def summary(sel, label):
    r = [x for x in rows if sel(x)]
    lc = sum(x['ll_coin'] for x in r); lk = sum(x['ll_colour'] for x in r)
    a = np.array([x['prevE'] - 0.5 for x in r]); b = np.array([x['E'] - 0.5 for x in r])
    corr = float(np.corrcoef(a, b)[0, 1]) if len(r) > 2 and a.std() > 0 and b.std() > 0 else float('nan')
    return dict(label=label, steps=len(r), loglik_coin=round(lc, 2), loglik_colour=round(lk, 2),
                colour_minus_coin=round(lk - lc, 2), corr_prev_vs_next=round(corr, 3),
                mean_pass=round(float(np.mean([x['E'] for x in r])), 4))
res = [summary(lambda x: x['N'] <= 16, 'FINAL steps (N <= 16)'),
       summary(lambda x: 16 < x['N'] < 512, 'MIDDLE steps (16 < N < 512)'),
       summary(lambda x: x['N'] >= 512, 'EARLY steps (N >= 512)')]
for x in res: print(json.dumps(x))
# control: the same scoring on simulated fair-coin culls with the same starting populations
rng = np.random.default_rng(11); ctrl = []
for x0 in [x for x in rows if x['j'] == 1]:
    Nn = x0['N']; prevE = 0.5; seq = []
    while Nn > 0:
        k = rng.binomial(Nn, 0.5); seq.append((Nn, k, prevE)); prevE = k / Nn; Nn = k
    for Nn, k, pe in seq[1:]:
        ctrl.append((Nn, k, ll(k, Nn, 0.5), ll(k, Nn, min(max(pe, 0.05), 0.95))))
for lo, hi, lab in [(0, 16, 'FINAL'), (17, 511, 'MIDDLE'), (512, 10**9, 'EARLY')]:
    c = [x for x in ctrl if lo <= x[0] <= hi]
    print('CONTROL (fair coins)', lab, 'steps', len(c), 'colour_minus_coin', round(sum(x[3] - x[2] for x in c), 2))
json.dump(dict(results=res, rows=rows), open('colour_branching.json', 'w'))
