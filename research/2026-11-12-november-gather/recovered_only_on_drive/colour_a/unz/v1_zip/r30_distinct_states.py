# SCRIPT: R30_COLOUR_DISTINCT_STATES
# Rule 30 left half driven by the 0101 centre, widths 12..40, both phases, post-wall steps (as in R30_COLOUR_BRANCHING).
# Question: when rows that have merged into the same whole configuration are counted ONCE, does the population's
# colour (its previous pass share E+) still steer the next split, and do the "families" survive?
# KILL (written before the run):
#   K1 if the per-step dispersion z^2 (scatter of pass counts in fair-coin units) falls from the row-level 5.7-12.9
#      to within [0.8, 1.2] when counted by distinct states in every band, the family signal was duplication.
#   K2 if the soft-colour held-out gain on distinct states is <= 0 in the early and middle bands (by phase and by
#      width), colour does not steer the bulk branching; the earlier row-level gain was carried by duplicate rows.
# Opposite run: the same statistics counted by rows (must reproduce R30_COLOUR_BRANCHING_OPPOSITE: 5.68, 8.97, 12.91).
import numpy as np, json
from math import lgamma, log
def run_states(n, phase, H=200):
    c = (lambda t: t % 2 == 1) if phase == 'A' else (lambda t: t % 2 == 0)
    frees = [d for d in range(1, n + 1) if not c(d - 1)]
    K = len(frees); N = 1 << K; idx = np.arange(N)
    Z = np.zeros(N, bool); O = ~Z
    alive = O.copy(); diag = {}; steps = []
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
            if d > n:
                before = alive.copy()
                alive &= ~fix
                # configuration of each alive-before row at this step (all current cells), packed to bytes
                M = np.packbits(np.array([r[before] for r in row], dtype=np.uint8), axis=0)
                keys = [M[:, i].tobytes() for i in range(M.shape[1])]
                passed_rows = alive[before]
                groups = {}
                for kk, p in zip(keys, passed_rows):
                    g = groups.setdefault(kk, [0, None]); g[0] += 1; g[1] = bool(p)
                Nrow = int(before.sum()); krow = int(passed_rows.sum())
                Nst = len(groups); kst = sum(1 for g in groups.values() if g[1])
                steps.append((Nrow, krow, Nst, kst))
        diag[d] = row
        if d > 3: del diag[d - 3]
        if not alive.any(): break
    return steps
def ll(k, N, p):
    p = min(max(p, 1e-6), 1 - 1e-6)
    return lgamma(N + 1) - lgamma(k + 1) - lgamma(N - k + 1) + k * log(p) + (N - k) * log(1 - p)
rows = []
for ph in 'AB':
    for n in range(12, 41, 2):
        S = run_states(n, ph)
        for j in range(1, len(S)):
            Nr, kr, Ns, ks = S[j]; Nrp, krp, Nsp, ksp = S[j - 1]
            if Nr == 0 or Nrp == 0 or Ns == 0 or Nsp == 0: continue
            rows.append(dict(ph=ph, n=n, N=Nr, k=kr, prevE=krp / Nrp, Ns=Ns, ks=ks, prevEs=ksp / Nsp))
bands = [('FINAL', lambda x: x['N'] <= 16), ('MIDDLE', lambda x: 16 < x['N'] < 512), ('EARLY', lambda x: x['N'] >= 512)]
grid = np.linspace(-1, 1, 81)
def soft_gain(r, key_N, key_k, key_prev, split):
    tot = 0; lams = []
    for fit_sel in split:
        rf = [x for x in r if fit_sel(x)]; rt = [x for x in r if not fit_sel(x)]
        if not rf or not rt: continue
        best = max(grid, key=lambda L: sum(ll(x[key_k], x[key_N], .5 + L * (x[key_prev] - .5)) for x in rf))
        lams.append(round(float(best), 3))
        tot += sum(ll(x[key_k], x[key_N], .5 + best * (x[key_prev] - .5)) - ll(x[key_k], x[key_N], .5) for x in rt)
    return tot, lams
out = {}
for name, sel in bands:
    r = [x for x in rows if sel(x)]
    zr = np.array([(x['k'] - x['N'] / 2) / np.sqrt(x['N'] / 4) for x in r])
    zs = np.array([(x['ks'] - x['Ns'] / 2) / np.sqrt(x['Ns'] / 4) for x in r])
    byphase = [lambda x: x['ph'] == 'A', lambda x: x['ph'] == 'B']
    bywidth = [lambda x: x['n'] <= 26, lambda x: x['n'] > 26]
    gr_ph, _ = soft_gain(r, 'N', 'k', 'prevE', byphase); gr_w, _ = soft_gain(r, 'N', 'k', 'prevE', bywidth)
    gs_ph, lam_ph = soft_gain(r, 'Ns', 'ks', 'prevEs', byphase); gs_w, lam_w = soft_gain(r, 'Ns', 'ks', 'prevEs', bywidth)
    rps = float(np.mean([x['N'] / x['Ns'] for x in r]))
    out[name] = dict(steps=len(r), dispersion_rows=round(float(np.mean(zr ** 2)), 2), dispersion_states=round(float(np.mean(zs ** 2)), 2),
                     rows_per_state=round(rps, 1), soft_gain_rows_phase=round(gr_ph, 1), soft_gain_rows_width=round(gr_w, 1),
                     soft_gain_states_phase=round(gs_ph, 1), soft_gain_states_width=round(gs_w, 1), lam_states=lam_ph + lam_w)
    print(f"{name}: steps={len(r)} dispersion by rows={out[name]['dispersion_rows']} by distinct states={out[name]['dispersion_states']} "
          f"rows per state={out[name]['rows_per_state']} soft-colour held-out gain by rows (phase/width)={gr_ph:.1f}/{gr_w:.1f} "
          f"by distinct states={gs_ph:.1f}/{gs_w:.1f} lam(states)={lam_ph + lam_w}")
k1 = all(0.8 <= out[b]['dispersion_states'] <= 1.2 for b in out)
k2 = all(out[b]['soft_gain_states_phase'] <= 0 or out[b]['soft_gain_states_width'] <= 0 for b in ('EARLY', 'MIDDLE'))
print('K1 (families were duplication):', 'FIRED' if k1 else 'did not fire')
print('K2 (colour does not steer the bulk once rows are counted once):', 'FIRED' if k2 else 'did not fire')
# Control (added after K2 was read): fair-coin culls on the same distinct-state populations, 200 replicates,
# scored by the same held-out soft-colour fit, to show the size of gain that chance alone produces.
rng = np.random.default_rng(30)
ctrl = {b: [] for b, _ in bands}
for rep in range(200):
    fake = []
    prev = {}
    for x in rows:
        key = (x['ph'], x['n'])
        pe = prev.get(key, 0.5)
        ks = int(rng.binomial(x['Ns'], 0.5))
        fake.append(dict(ph=x['ph'], n=x['n'], Ns=x['Ns'], ks=ks, prevEs=pe, N=x['N']))
        prev[key] = ks / x['Ns'] if x['Ns'] else 0.5
    for name, sel in bands:
        r = [x for x in fake if sel(x)]
        g1, _ = soft_gain(r, 'Ns', 'ks', 'prevEs', [lambda x: x['ph'] == 'A', lambda x: x['ph'] == 'B'])
        g2, _ = soft_gain(r, 'Ns', 'ks', 'prevEs', [lambda x: x['n'] <= 26, lambda x: x['n'] > 26])
        ctrl[name].append((g1, g2))
for name in ctrl:
    a = np.array(ctrl[name])
    print(f"CONTROL fair coins on distinct states, {name}: held-out soft gain 5-95% by phase [{np.percentile(a[:,0],5):.1f}, {np.percentile(a[:,0],95):.1f}], "
          f"by width [{np.percentile(a[:,1],5):.1f}, {np.percentile(a[:,1],95):.1f}]")
    out[name]['control_gain_5_95_phase'] = [round(float(np.percentile(a[:,0],5)),1), round(float(np.percentile(a[:,0],95)),1)]
    out[name]['control_gain_5_95_width'] = [round(float(np.percentile(a[:,1],5)),1), round(float(np.percentile(a[:,1],95)),1)]
json.dump(out, open('r30_distinct_states.json', 'w'), indent=1)
