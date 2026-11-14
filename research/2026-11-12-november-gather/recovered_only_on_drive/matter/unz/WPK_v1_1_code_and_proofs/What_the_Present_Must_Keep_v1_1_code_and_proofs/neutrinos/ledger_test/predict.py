# SCRIPT: PREDICT  K2: G(history) = int W L_hist / int W L_inst, W(eps) from burst probes (interpolated linearly in log eps), L from ledger_hist.json
# Probe at eps_b covers [eps_b, 1.25 eps_b]; W is placed at the window's log-midpoint 1.118 eps_b. Below the first probe W is held flat;
# above the last measured probe W falls linearly in log eps to 0 at the eps_b=6 window midpoint (where the burst had no effect on the outcome).
import json, sys, numpy as np
src = sys.argv[1] if len(sys.argv) > 1 else 'fast'
LH = json.load(open('ledger_hist.json')); g = np.array(LH['grid'])
LB = json.load(open('ledger_burst.json'))
if src == 'fast':
    FR = json.load(open('fast_readout.json'))
    def dd(t):
        ro = FR[t]['readout']; v = [x for k, x in ro.items() if isinstance(x, float) and abs(float(k)-5.0) < 1e-9]
        return v[0] if v else [x for x in ro.values() if isinstance(x, float)][-1]
    base_dc = None
    probes = [(eb, dd('burst_%g' % eb)) for eb in (0.25, 0.5, 1, 1.5, 2, 3, 4)]
else:
    F = {json.loads(l)['tag']: json.loads(l) for l in open('full_results.jsonl')}
    b = F['F_base']['dc']
    probes = [(eb, F['F_burst_%g' % eb]['dc'] - b) for eb in (0.25, 0.5, 1, 1.5, 2, 3, 4) if 'F_burst_%g' % eb in F]
pe = [eb*np.sqrt(1.25) for eb, _ in probes] + [6*np.sqrt(1.25)]
pw = [d/LB['%g' % eb]['Lb'] for eb, d in probes] + [0.0]
print('probes (eps_b, L_b, Ddc, W):'); [print('  %.2f  %.5f  %.6f  %.5f' % (eb, LB['%g' % eb]['Lb'], d, d/LB['%g' % eb]['Lb'])) for eb, d in probes]
def W(e): return np.interp(np.log(e), np.log(pe), pw, left=pw[0], right=0.0)
em = np.sqrt(g[1:]*g[:-1])
def reading(key):
    S = np.array(LH[key]); return float(np.sum(W(em)*(S[:-1]-S[1:])))
Ri = reading('inst')
meas = {'n3_0.25': .959, 'n3_0.5': .867, 'n3_1': .683, 'n3_2': .431, 'n3_4': .190, 'n3_8': .063, 'n6_1': .648, 'n6_2': .317, 'n6_3': .154}
DI = 0.52832-0.49773
print('int W L_inst = %.5f  (measured instant shift %.5f)' % (Ri, DI))
print('%-8s %8s %8s %8s %10s %10s' % ('hist', 'G_meas', 'G_pred', 'diff', 'Ddc_pred', 'Ddc_meas'))
res = {}; worst = 0
for k, m in meas.items():
    r = reading(k); gp = r/Ri; worst = max(worst, abs(gp-m)); res[k] = dict(G_meas=m, G_pred=gp, Ddc_pred=r, Ddc_meas=m*DI)
    print('%-8s %8.3f %8.3f %+8.3f %10.5f %10.5f' % (k, m, gp, gp-m, r, m*DI))
print('worst |G_pred - G_meas| = %.3f  -> K2 %s (threshold 0.05)' % (worst, 'PASS' if worst <= 0.05 else 'FAIL'))
json.dump(dict(src=src, probes=probes, W_eps=pe, W_val=pw, inst_reading=Ri, res=res, worst=worst), open('predict_%s.json' % src, 'w'), indent=1)
