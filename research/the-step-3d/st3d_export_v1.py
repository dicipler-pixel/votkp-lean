# SCRIPT: ST3D-EXPORT-V1 — frames for the 3D step page from the fourteen runs of ST3D-RUN-V1 (checked by ST3D-CHECK-01), plus his threshold curves.
# Jeromie Beasley. 18 Nov 2026. AI-assisted.
# Per run, 14 plasma shells (Lagrangian edges nearest the targets, in units of r_m) and every recorded frame:
#   Ra    = R / a, with a = R / r at the outer edge (r = 9 r_m, where the universe is unperturbed),
#   C     = his compaction 2(M - Mb)/R at the shell, Mb = (4 pi / 3) rho_b R^3, rho_b = 3 H_b^2 / 8 pi, H_b = U/R at the outer edge,
#   twoMR = 2M/R, fall = 1 where U < 0,
#   A     = his lapse Ac of the cell inside the shell (A = 1 at the outer cell); clock tau_i = running sum of A_i over frames (frames equal steps in eps),
#   kH    = his local collision rate kap over H_b in that cell (full model only): above 1 the neutrinos there are held, below 1 they stream,
#   I     = his neutrino intensity in 32 bins of mu, over its mean (full model only).
# Per frame of the run: eps, Tb (MeV, background temperature his loop passes to rhs), kbH (his kb/H_b), Cmax over r < 4 r_m (his rule).
# Curves: his archived thresholds against T_H, perfect fluid (res_eos_pf) and physical (res_phys), with M_H from his MHof (massfn/mass_function.py).
import json, glob, sys, numpy as np
SIM = sys.argv[1]
TB = np.load(SIM + '/thermo_tables.npz'); o = np.argsort(TB['T']); Tt = TB['T'][o]; rt = (TB['rpl'] + TB['rnu'])[o]
G, c, Msun, MeV4 = 6.674e-11, 2.998e8, 1.989e30, 2.3201e8
MHof = lambda TH: c**3/(2*G*np.sqrt(8*np.pi*G*np.interp(TH, Tt, rt)*MeV4/3))/Msun
TARGET = [0.12, 0.2, 0.3, 0.42, 0.55, 0.7, 0.85, 1.0, 1.2, 1.45, 1.75, 2.1, 2.6, 3.2]
rnd = lambda x, n=4: [float(round(float(v), n)) for v in x]
out = dict(runs={}, curves={})
for f in sorted(glob.glob('run_*_0.515.npz')):
    d = np.load(f); row = str(d['row']); r = d['r']; nu = row == 'nu'
    idx = sorted(set(int(np.argmin(abs(r - x))) for x in TARGET)); cells = [i - 1 for i in idx]; inner = r[1:] < 4.0
    tau = np.zeros(len(idx)); fr = []
    for k in range(len(d['eps'])):
        R = d['R'][k].astype(float); U = d['U'][k].astype(float); M = d['M'][k].astype(float)
        a = R[-1]/r[-1]; Hb = U[-1]/R[-1]; rhob = 3*Hb*Hb/(8*np.pi)
        C = 2*(M[1:] - (4*np.pi/3)*rhob*R[1:]**3)/R[1:]
        A = d['A'][k][cells].astype(float); tau = tau + A
        row_ = dict(eps=round(float(d['eps'][k]), 4), Cmax=round(float(C[inner].max()), 5), Ra=rnd(R[idx]/a), C=rnd(C[np.array(idx) - 1]),
                    twoMR=rnd(2*M[idx]/R[idx]), fall=[int(U[i] < 0) for i in idx], A=rnd(A), tau=rnd(tau, 3))
        if nu:
            row_['Tb'] = round(float(d['Tb'][k]), 5); row_['kbH'] = float('%.3g' % float(d['kbH'][k]))
            row_['kH'] = [float('%.3g' % float(v)) for v in d['kapH'][k][cells]]
            I = d['I'][k][cells].astype(float); m = I.mean(axis=1)
            if np.all(m > 0): row_['I'] = [rnd(v/mm, 3) for v, mm in zip(I, m)]
            else: row_['one'] = 1          # his tight phase: plasma and neutrinos still one fluid, no transport yet (I = 0 by his construction)
        fr.append(row_)
    TH = float(d['TH']); key = '%s_%g' % (row, float(d['T0']))
    out['runs'][key] = dict(row=row, T0=float(d['T0']), TH=TH, MH=float(MHof(TH)), delta_m=float(d['delta_m']), status=str(d['status']),
                            eps_end=float(d['eps_end']), r=rnd(r[idx]), frames=fr)
    print(key, d['status'], 'T_H %.4f' % TH, 'M_H %.3g' % MHof(TH), 'frames', len(fr))
for name, pat in [('pf', '/res_eos_pf_*.json'), ('phys', '/res_phys_*.json')]:
    rows = sorted([json.load(open(p)) for p in glob.glob(SIM + pat)], key=lambda q: -q['TH'])
    out['curves'][name] = [dict(TH=round(q['TH'], 5), MH=float('%.4g' % MHof(q['TH'])), dc=round(q['dc'], 5), w=round(q['w']/2, 5), src=q.get('source', 'pf')) for q in rows]
json.dump(out, open('st3d_frames_v1.json', 'w'), separators=(',', ':'))
import os; print('bytes', os.path.getsize('st3d_frames_v1.json'))
