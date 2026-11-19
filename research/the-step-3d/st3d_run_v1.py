# SCRIPT: ST3D-RUN-V1 — Steve McCormick's full model (e± plasma + neutrinos that decouple), one lump at seven horizon masses, every shell recorded.
# Jeromie Beasley. 18 Nov 2026. AI-assisted.
# Runs his own code (PBH_neutrino_simulation, commit eb7c4de, 11 Nov 2026) exactly as his bisections call it:
#   'nu' row: run_eosc.run(delta_m, T0, Tdec=1.0)            (bisect_eosc.py; all other settings his defaults: N = 300, K = 32, eps_max = 15, disperse rule on)
#   'pf' row: run_eos.run(delta_m, kind='pf', T0=T0, K=2)     (bisect_eos.py pf: one perfect fluid with the e± equation of state, neutrinos never leave)
# Nothing in his loop is changed. His rhs is wrapped from outside: the wrapper calls his rhs and returns its result untouched,
# and on each call that starts a step (call 0, 3, 6, ...: each step calls rhs once at the state, then twice for the Runge-Kutta stages)
# it keeps the state when eps has reached the next multiple of 0.025 past eps0 = 0.1: R, U, M, e, the lapse Ac (his state(), A = 1 at the outer cell),
# the local collision rate kap (nu row), the neutrino intensity I(mu), and the background temperature Tb and kb/Hb that his loop passes in.
# Usage: python3 st3d_run_v1.py <his simulation dir> <row: pf|nu> <T0> <delta_m> <out dir> [check]
import sys, os, time, numpy as np
SIM, ROW, T0, DM, OUT = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
CHECK = len(sys.argv) > 6
sys.path.insert(0, SIM); os.chdir(SIM)
import run_eos, run_eosc
from ms_fluid import make_grid
mod = run_eosc if ROW == 'nu' else run_eos
his_rhs = mod.rhs
N = 300 if ROW == 'nu' else 400
r = make_grid(N, 9.0, 3.0)
frames = []; ncall = [0]; nxt = [0]
target = lambda k: round(0.1 + 0.025*k, 6)
def wrap(*a):
    out = his_rhs(*a)
    if ncall[0] % 3 == 0:
        R, U, e, I = a[1], a[2], a[4], a[5]
        epsn = r[-1]/U[-1]
        if epsn >= target(nxt[0]):
            while epsn >= target(nxt[0]): nxt[0] += 1
            M, Ac = out[0], out[1]
            kb, Tb = (a[11], a[12]) if ROW == 'nu' else (0.0, np.nan)
            kap = out[5] if ROW == 'nu' else np.zeros(len(e))
            Hb = U[-1]/R[-1]
            frames.append(dict(eps=float(epsn), R=R.copy(), U=U.copy(), M=M.copy(), e=e.copy(), A=Ac.copy(), kapH=kap/Hb, I=I.copy(), Tb=float(Tb), kbH=float(kb/Hb)))
    ncall[0] += 1
    return out
mod.rhs = wrap
t1 = time.time()
if ROW == 'nu':
    o = run_eosc.run(DM, T0, Tdec=1.0, snap_eps=((2.0,) if CHECK else ()))
else:
    o = run_eos.run(DM, kind='pf', T0=T0, K=2)
tag = '%s_%g_%g' % (ROW, T0, DM)
print(tag, o['status'], 'eps %.4f' % o['eps'], 'TH', o['TH'], 'steps', o['steps'], 'frames', len(frames), 'calls', ncall[0], 'time %.0fs' % (time.time() - t1), flush=True)
S = lambda k: np.stack([f[k] for f in frames]).astype(np.float32)
np.savez_compressed(os.path.join(OUT, 'run_%s.npz' % tag), row=ROW, T0=T0, delta_m=DM, status=o['status'], eps_end=float(o['eps']), TH=float(o['TH'] or np.nan),
    peakC=float(o['peakC']), r=r, eps=np.array([f['eps'] for f in frames]), Tb=np.array([f['Tb'] for f in frames]), kbH=np.array([f['kbH'] for f in frames]),
    R=S('R'), U=S('U'), M=S('M'), e=S('e'), A=S('A'), kapH=S('kapH'), I=S('I'), hist=o['hist'])
if CHECK and ROW == 'nu':
    sn = o['snaps'][2.0]; k = int(np.argmin([abs(f['eps'] - sn['eps']) for f in frames])); f = frames[k]
    d = max(float(np.max(np.abs(f[q] - sn[q]))) for q in ['R', 'U', 'e', 'I', 'M'])
    print('CHECKSNAP his snapshot at eps %.6f vs recorded frame at eps %.6f: largest difference %.3e' % (sn['eps'], f['eps'], d), flush=True)
