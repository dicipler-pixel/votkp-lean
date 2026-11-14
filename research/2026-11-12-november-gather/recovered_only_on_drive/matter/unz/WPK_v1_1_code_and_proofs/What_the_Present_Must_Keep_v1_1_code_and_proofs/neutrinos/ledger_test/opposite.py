# SCRIPT: OPPOSITE  K2 opposite setup: listening curve measured from the other end (coupling bursts on the instant-decoupling base).
# A coupling burst (kappa/H ramped 0 -> 1e4 over the first 5%, then 1e4, in [eps_b, 1.25 eps_b]; the abrupt switch to the cap crashes the code) is not a localized ledger entry, so W is recovered by solving the linear system
#   Ddc_j = int W(eps) [L_cb_j(eps) - L_inst(eps)] d eps,   W piecewise linear in log eps on nodes at the probe midpoints 1.118 eps_b,
#   held flat below the first node and above the last. Then G is predicted with the SAME formula as K2: G = int W L_hist / int W L_inst.
import json, sys, numpy as np
from scipy.optimize import nnls
LH = json.load(open('ledger_hist.json')); g = np.array(LH['grid']); LC = json.load(open('ledger_rburst.json'))
FR = json.load(open(sys.argv[1]))           # fast readout of the cburst runs (Ddc = d0 - delta_equiv, negative = threshold lowered)
EPR = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
ebs = (0.25, 0.5, 1, 1.5, 2, 3, 4, 6)
em = np.sqrt(g[1:]*g[:-1]); nodes = np.log(np.array(ebs)*np.sqrt(1.25))
def hat(n):
    v = np.zeros(len(nodes)); v[n] = 1.0
    return np.interp(np.log(em), nodes, v)
def dS(S): S = np.array(S); return S[:-1]-S[1:]
Li = dS(LH['inst'])
rows, rhs, used = [], [], []
for eb in ebs:
    t = 'rburst_%g' % eb
    if t not in FR: continue
    ro = FR[t]['readout']; vals = {float(k): v for k, v in ro.items() if isinstance(v, float)}
    if not vals: print(t, 'no readout', ro); continue
    k = min(vals, key=lambda x: abs(x-EPR)); d = vals[k]
    dL = dS(LC['rb_%g' % eb]) - Li
    rows.append([np.sum(hat(n)*dL) for n in range(len(nodes))]); rhs.append(d); used.append((eb, k, d, float(dL.sum())))
A = np.array(rows); b = np.array(rhs)
print('probe  eps_r  Ddc_fast   total ledger change (S_inst(14)-S_cb(14) sign: +=less ledger)')
for u in used: print('  %.2f  %.1f  %+.6f  %+.5f' % (u[0], u[1], u[2], -u[3]))
print('cond(A) = %.2e' % np.linalg.cond(A))
meas = {'n3_0.25': .959, 'n3_0.5': .867, 'n3_1': .683, 'n3_2': .431, 'n3_4': .190, 'n3_8': .063, 'n6_1': .648, 'n6_2': .317, 'n6_3': .154}
out = {}
for name, w in [('lstsq', np.linalg.lstsq(A, b, rcond=None)[0]), ('nnls', nnls(A, b)[0])]:
    Wg = sum(w[n]*hat(n) for n in range(len(nodes)))
    Ri = float(np.sum(Wg*Li)); print('\n%s W nodes:' % name, ' '.join('%.4f' % x for x in w), ' residual %.2e' % np.linalg.norm(A@w-b))
    print('  int W L_inst = %.5f (measured instant shift 0.03059)' % Ri)
    worst = 0; res = {}
    for k, m in meas.items():
        r = float(np.sum(Wg*dS(LH[k]))); gp = r/Ri if Ri != 0 else np.nan; worst = max(worst, abs(gp-m)); res[k] = (m, gp)
        print('  %-8s G_meas %.3f G_pred %.3f diff %+.3f' % (k, m, gp, gp-m))
    print('  worst %.3f -> %s' % (worst, 'PASS' if worst <= 0.05 else 'FAIL'))
    out[name] = dict(W=w.tolist(), inst_reading=Ri, res=res, worst=worst)
json.dump(dict(used=used, out=out), open('opposite.json', 'w'), indent=1)
