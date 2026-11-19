# SCRIPT: NU3D-EXPORT-V1 — frames for the 3D page from Steve McCormick's three Figure 1 runs (NU3D-RUN-V2 output, checked by NU3D-CHECK-01).
# Jeromie Beasley. 18 Nov 2026. AI-assisted.
# For 14 plasma shells (Lagrangian edges r nearest the targets below, in units of r_m) and every recorded frame:
#   Ra   = R / a, the areal radius over the background scale factor a = sqrt(t/t0) (radiation; R = a r for the unperturbed universe),
#   C    = 2(M - Mb)/R at the shell (his compaction function), twoMR = 2M/R, fall = 1 where U < 0,
#   A    = lapse of the cell just inside the shell, his A = ((1 - fnu) rho_b / e)^(1/4); the shell's clock runs at A against the background,
#   dp   = e / ((1 - fnu) rho_b) - 1, the plasma density contrast of that cell,
#   I    = the neutrino intensity of that cell in his 32 bins of mu, divided by its mean (1 = isotropic); dn = its energy density over background - 1.
# The clock of each shell: tau_i = sum of A_i over frames, so its hand turns at A_i against the background (frames are equally spaced in eps,
# and dt/deps = eps/(2 t0) is the same for every shell, so the ratio of rates is exactly A).
# The curves for the strip chart are his own diag rows (dyn_runs_diag.diag): eps, C_max, plasma and neutrino central contrasts.
import json, numpy as np
TARGET = [0.12, 0.2, 0.3, 0.42, 0.55, 0.7, 0.85, 1.0, 1.2, 1.45, 1.75, 2.1, 2.6, 3.2]
out = {}
for tag in ['fluid', 'nu', 'nu535']:
    d = np.load('shells_%s.npz' % tag); r = d['r']; t = d['t']; a = np.sqrt(t/t[0]); fnu = float(d['fnu'])
    idx = sorted(set(int(np.argmin(abs(r - x))) for x in TARGET))
    R = d['R']; U = d['U']; M = d['M']; A = d['A']; C = d['C']; e = d['e']; rhob = d['rhob']
    rnd = lambda x, n=4: [float(round(float(v), n)) for v in x]
    fr = []
    tau = np.zeros(len(idx))
    for k in range(len(t)):
        cells = [i - 1 for i in idx]
        Ak = A[k][cells]; tau = tau + Ak
        row = dict(eps=round(float(d['eps'][k]), 4), Ra=rnd(R[k][idx]/a[k]), C=rnd(C[k][cells]), twoMR=rnd(2*M[k][idx]/R[k][idx]), fall=[int(U[k][i] < 0) for i in idx],
                   A=rnd(Ak), tau=rnd(tau, 3), dp=rnd(e[k][cells]/((1 - fnu)*rhob[k]) - 1, 3))
        if fnu > 0:
            I = d['I'][k][cells]; mean = I.mean(axis=1, keepdims=True); dmu = 2.0/I.shape[1]
            row['I'] = [rnd(v/m, 3) for v, m in zip(I, mean[:, 0])]
            row['dn'] = rnd(2*np.pi*I.sum(axis=1)*dmu/(fnu*rhob[k]) - 1, 3)
        fr.append(row)
    dg = np.load('diag_%s.npy' % tag); step = max(1, len(dg)//600)
    out[tag] = dict(delta_m=float(d['delta_m']), fnu=fnu, status=str(d['status']), eps_end=float(d['eps_end']), r=rnd(r[idx]),
                    nmu=(int(d['I'].shape[2]) if fnu > 0 else 0), frames=fr, curve=[rnd(row, 5) for row in dg[::step]] + [rnd(dg[-1], 5)])
json.dump(out, open('nu3d_frames_v1.json', 'w'), separators=(',', ':'))
for k, v in out.items(): print(k, v['status'], 'shells', len(v['r']), 'frames', len(v['frames']), 'curve', len(v['curve']), 'r', v['r'])
import os; print('bytes', os.path.getsize('nu3d_frames_v1.json'))
