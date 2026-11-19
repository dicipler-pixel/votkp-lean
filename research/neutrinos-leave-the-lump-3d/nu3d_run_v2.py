# SCRIPT: NU3D-RUN-V2 — Steve McCormick's Figure 1 runs, with every shell recorded for the 3D model.
# Jeromie Beasley. 18 Nov 2026. AI-assisted.
# Runs his own run_nu.run (PBH_neutrino_simulation, commit eb7c4de, 11 Nov 2026) exactly as his dyn_runs.py and dyn_runs2.py do:
#   fluid: delta_m = 0.51, fnu = 0, K = 2;  nu: delta_m = 0.51, fnu = 0.409, K = 32;  nu535: delta_m = 0.535, fnu = 0.409, K = 32;
#   N = 400, eps0 = 0.1, eps_max = 9, hist_every = 10, disperse_rule = False.
# His diag (dyn_runs_diag.diag) is called unchanged and its rows are kept, so the run can be checked against his archived figure data.
# Alongside it, a frame is recorded whenever eps has advanced by 0.025 since the last (and the first and last diag calls), saving the shells: R, U, M (edges), e, lapse A = ((1 - fnu) rho_b / e)^(1/4) (his state()),
# compaction C = 2(M - Mb)/R, 2M/R, and the neutrino intensity I(mu) per shell.
import sys, os, json, time, numpy as np
SIM = sys.argv[1]; TAG = sys.argv[2]
sys.path.insert(0, SIM); os.chdir(SIM)
from run_nu import run
from ms_nu import rho_b
from dyn_runs_diag import diag as his_diag
CFG = { 'fluid':(0.51, dict(fnu=0.0, K=2)), 'nu':(0.51, dict(fnu=0.409, K=32)), 'nu535':(0.535, dict(fnu=0.409, K=32)) }
dm, kw = CFG[TAG]; fnu = kw['fnu']; snaps = []; ncall = [0]
def rec(t, epsn, r, R, U, e, I, M, mue, C):
    out = his_diag(t, epsn, r, R, U, e, I, M, mue, C)
    if not snaps or epsn - snaps[-1]['eps'] >= 0.025:
        eb = (1.0 - fnu)*rho_b(t); A = (eb/e)**0.25
        snaps.append(dict(t=float(t), eps=float(epsn), R=R.astype(np.float32), U=U.astype(np.float32), M=M.astype(np.float32), e=e.astype(np.float32),
                          A=A.astype(np.float32), C=C.astype(np.float32), rhob=float(rho_b(t)), I=(I.astype(np.float32) if fnu > 0 else None)))
    ncall[0] += 1
    return out
t1 = time.time()
o = run(dm, N=400, eps0=0.1, eps_max=9.0, hist_every=10, diag=rec, disperse_rule=False, **kw)
print(TAG, o['status'], round(o['eps'], 3), 'steps', o['steps'], 'snaps', len(snaps), 'time %.0fs' % (time.time() - t1), flush=True)
OUT = sys.argv[3]
np.save(os.path.join(OUT, 'diag_' + TAG + '.npy'), np.array(o['hist2']))
S = lambda k: np.stack([x[k] for x in snaps])
np.savez_compressed(os.path.join(OUT, 'shells_' + TAG + '.npz'), tag=TAG, delta_m=dm, fnu=fnu, status=o['status'], eps_end=float(o['eps']), r=o['r'], mue=o['mue'],
  t=np.array([x['t'] for x in snaps]), eps=np.array([x['eps'] for x in snaps]), rhob=np.array([x['rhob'] for x in snaps]),
  R=S('R'), U=S('U'), M=S('M'), e=S('e'), A=S('A'), C=S('C'), I=(S('I') if fnu > 0 else np.zeros(1)))
