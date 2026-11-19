# SCRIPT: ST3D-CHECK-01 — the step runs, checked against Steve McCormick's own archive before anything is drawn.
# Jeromie Beasley. 18 Nov 2026. AI-assisted.
# (a) Same runs as his. Where his bisection logs (res_eosc_1.0_<T0>.json, res_eos_pf_<T0>.json) contain the exact amplitude we ran,
#     our outcome and end eps must be his: same status, |eps - his| <= 0.005 (he logs eps to 2 decimals).
#     Why it proves it: his log line is the output of the same function with the same arguments; a recorder that changed anything would move eps.
#     Kill line: any status different, or any eps off by more than 0.005.
# (b) The recorder is a copy, not a change: in each full-model run his own snapshot at eps = 2 equals our recorded frame (printed by ST3D-RUN-V1 as CHECKSNAP).
#     Kill line: any difference above 0.
# (c) Every outcome sits on the side of his threshold that it must: BH if delta_m > dc + w/2, dispersed if delta_m < dc - w/2 (dc, w from the same archive
#     file for that model and T0). Kill line: any outcome on the wrong side. Runs inside the bracket would be reported, not judged.
# (d) The step itself, from his archive alone: his physical curve (res_phys_*.json) against Table VII of the paper. Kill line: any value off by more than 0.00001.
import json, glob, re, numpy as np, sys
SIM = sys.argv[1]; fails = 0
def say(ok, s):
    global fails; print(('HOLDS  ' if ok else 'KILLED ') + s); fails += (not ok)
runs = sorted(glob.glob('run_*.npz')); worst = 0; nlog = 0; bad = []
for f in runs:
    d = np.load(f); row = str(d['row']); T0 = float(d['T0']); dm = float(d['delta_m'])
    arch = json.load(open(SIM + ('/res_eosc_1.0_%s.json' if row == 'nu' else '/res_eos_pf_%s.json') % repr(T0)))
    for (x, st, ep) in arch['log']:
        if abs(x - dm) < 1e-9:
            nlog += 1; dd = abs(float(d['eps_end']) - ep); worst = max(worst, dd)
            if st != str(d['status']) or dd > 0.005: bad.append((f, st, ep, str(d['status']), float(d['eps_end'])))
            print('    %-22s his %-9s eps %.2f   ours %-9s eps %.4f' % (f, st, ep, d['status'], d['eps_end']))
say(nlog >= 5 and not bad, '(a) %d runs with a twin in his logs: same outcome, largest eps difference %.4f %s' % (nlog, worst, bad))
cs = [float(m) for m in re.findall(r'largest difference ([0-9.e+-]+)', open('logA.txt').read() + open('logB.txt').read() + open('logC.txt').read())]
say(len(cs) == 7 and max(cs) == 0.0, '(b) recorder against his snapshot at eps = 2 in %d full-model runs: largest difference %g' % (len(cs), max(cs)))
side = []
for f in runs:
    d = np.load(f); row = str(d['row']); T0 = float(d['T0']); dm = float(d['delta_m'])
    a = json.load(open(SIM + ('/res_eosc_1.0_%s.json' if row == 'nu' else '/res_eos_pf_%s.json') % repr(T0)))
    need = 'BH' if dm > a['dc'] + a['w']/2 else ('dispersed' if dm < a['dc'] - a['w']/2 else 'inside')
    ok = need == 'inside' or need == str(d['status']); side.append(ok)
    print('    %-22s T_H %7.4f MeV  his dc %.5f +- %.5f  delta_m %.3f  must be %-9s is %s' % (f, a['TH'], a['dc'], a['w']/2, dm, need, d['status']))
say(all(side), '(c) every outcome on the side of his threshold it must be (%d runs)' % len(side))
T7 = {4.00: 0.50012, 2.00: 0.50788, 1.00: 0.51941, 0.70: 0.52350, 0.51: 0.52494, 0.31: 0.52306}
ph = [json.load(open(p)) for p in glob.glob(SIM + '/res_phys_*.json')]; dev = 0
for TH, v in T7.items():
    p = min(ph, key=lambda q: abs(q['TH'] - TH)); dev = max(dev, abs(round(p['dc'], 5) - v))
say(dev <= 1e-5, '(d) his physical curve against Table VII: largest difference %.1e over %d rows' % (dev, len(T7)))
print(fails and '%d KILLED' % fails or 'all hold')
