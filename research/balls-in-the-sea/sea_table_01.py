# SCRIPT: SEA-TABLE-01
# Reads the sweep results and applies the marks fixed in WAYS_SEA_01.md. Jeromie Beasley. 17 Nov 2026. AI-assisted.
import json, sys, collections
R = [json.loads(l) for f in ('res_01_p0.jsonl', 'res_01_p1.jsonl') for l in open(f)]
key = lambda r: (r['world'], r['machine'], r['ends'], r['clocks'], r['push'])
G = collections.defaultdict(dict)
for r in R: G[key(r)][r['feed']] = r
def marks(k, g):
    world, mach, ends, clocks, push = k; m = {}; runs = [r for f, r in g.items() if f != 'none']
    if not runs: return None
    if ends == 'leak': m['M1'] = all(r['trace_max'] <= r['trace_start'] + 1e-8 for r in runs)
    else: m['M1'] = all(abs(r['trace_end'] - r['trace_start']) < 1e-8 and r['proj_dev'] < 1e-7 for r in runs)
    if 'none' in g: m['M2'] = g['none']['max_sea_change'] < 1e-8 and g['none']['ball_turn_max'] < 1e-8
    kk = g.get('kick')
    if kk:
        m['M3'] = kk['far_change_before_crossing'] < 1e-9; m['M4'] = kk['tie_at_start'] > 1e-6
        m['M5'] = kk['far_swing_last'] >= 0.5*kk['far_swing_mid'] and kk['far_swing_mid'] > 1e-9
        m['first_move'] = kk['first_move_time']; m['cross'] = kk['crossing_time']; m['tie'] = kk['tie_at_start']; m['swing'] = (kk['far_swing_mid'], kk['far_swing_last'])
    for nm, a, b in (('M6k', 'kicks_in', 'kicks_out'), ('M6s', 'squeeze_in', 'squeeze_out')):
        if a in g and b in g: m[nm] = g[a]['lifted_mean'] >= 2*g[b]['lifted_mean'] and g[a]['lifted_mean'] > 1e-9; m[nm + '_ratio'] = g[a]['lifted_mean']/g[b]['lifted_mean'] if abs(g[b]['lifted_mean']) > 1e-300 else float('inf'); m[nm + '_in'] = g[a]['lifted_mean']
    m['M7'] = [(f, r['locks']) for f, r in g.items() if r.get('locks')]; m['M8'] = [(f, r['gears']) for f, r in g.items() if r.get('gears')]
    m['works'] = m['M1'] and m.get('M2', True) and m.get('M3', True); return m
T = {k: marks(k, g) for k, g in G.items()}; T = {k: v for k, v in T.items() if v}
json.dump([dict(way=list(k), **{a: b for a, b in v.items()}) for k, v in T.items()], open('sea_table_01.json', 'w'), indent=0, default=float)
tf = lambda b: {True: 'Y', False: 'n', None: '-'}[b]
print('runs', len(R), 'errors', sum('error' in r for r in R), 'ways', len(T))
print('world machine ends clocks push | M1 M2 M3 M4 M5 M6k M6s works | first/cross tie kickratio sqratio locks gears')
for k in sorted(T):
    v = T[k]; print(' '.join(str(x) for x in k), '|', ' '.join(tf(v.get(x)) for x in ('M1', 'M2', 'M3', 'M4', 'M5', 'M6k', 'M6s', 'works')), '|', v.get('first_move'), '/', round(v.get('cross', 0), 2), '%.1e' % v.get('tie', 0), '%.2f' % v.get('M6k_ratio', float('nan')), '%.2f' % v.get('M6s_ratio', float('nan')), len(v['M7']), len(v['M8']))
