# SCRIPT: COLOUR-PAPER-FIGURES-01
# Two figures for the paper, from computed data: (1) the colour of matter: Re sigma = d^2/8 and the isospectral pair;
# (2) Rule 30: dispersion and held-out colour gain by rows against by distinct states.
import json, os, math, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
INK, INK2, MUTED, GRID = '#0b0b0b', '#52514e', '#8a8984', '#e4e3df'
BLUE, ORANGE, AQUA, VIOLET = '#2a78d6', '#eb6834', '#1baf7a', '#6250d6'
plt.rcParams.update({'font.family': 'DejaVu Serif', 'font.size': 10, 'axes.edgecolor': MUTED, 'axes.labelcolor': INK2,
                     'xtick.color': INK2, 'ytick.color': INK2, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.grid': True, 'grid.color': GRID, 'grid.linewidth': 0.6, 'lines.linewidth': 2, 'savefig.dpi': 300, 'savefig.bbox': 'tight'})
# (1) colour of matter: conductivity from current elements (recomputed here, same model as COLOR-PROJECTOR-CHECK-01)
SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.array([[1, 0], [0, -1]], complex)
def model(kx, ky, d, M=1.0):
    a = d * math.sqrt(max(0.0, 1 - d * d))
    h = [a * ky * ky / M, d * kx * ky / M, (kx * kx + (1 - 2 * d * d) * ky * ky) / (2 * M)]
    hx = [0.0, d * ky / M, kx / M]
    H = h[0] * SX + h[1] * SY + h[2] * SZ; Vx = hx[0] * SX + hx[1] * SY + hx[2] * SZ
    return H, Vx
def sigma(d, M=1.0, w=1.0, nang=256):
    k = math.sqrt(M * w); tot = 0.0   # omega = k^2/M
    for th in np.linspace(0, 2 * np.pi, nang, endpoint=False):
        H, Vx = model(k * math.cos(th), k * math.sin(th), d, M)
        e, U = np.linalg.eigh(H); vcv = U[:, 1].conj() @ Vx @ U[:, 0]
        tot += abs(vcv) ** 2
    angular = 2 * np.pi * tot / nang        # as in COLOR-PROJECTOR-CHECK-01: gap omega = k^2/M, delta integral gives M/2
    return math.pi / w * M / 2 * angular / (2 * np.pi) ** 2
ds = np.linspace(0, 1, 41); sig = np.array([sigma(d) for d in ds])
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.1))
axs[0].plot(ds, ds ** 2 / 8, color=MUTED, lw=1.2, ls='--', label='$d^2/8$'); axs[0].plot(ds, sig, 'o', ms=3.5, color=BLUE, label='from current elements')
axs[0].set_xlabel('texture $d$ (eigenvectors; the spectrum is fixed)'); axs[0].set_ylabel(r'$\mathrm{Re}\,\sigma_{xx}\ /\ (e^2/\hbar)$'); axs[0].legend(frameon=False, fontsize=8)
axs[0].set_title('Absorption follows the texture, not the levels', fontsize=9.5, color=INK)
kx, ky = 0.8, 0.6; vals = []
for d in ds:
    H, Vx = model(kx, ky, d); e, U = np.linalg.eigh(H); vals.append(abs(U[:, 1].conj() @ Vx @ U[:, 0]) ** 2)
axs[1].plot(ds, vals, color=ORANGE, label='$|v_{cv}|^2$ at $k=(0.8,0.6)$')
axs[1].plot(ds, [0.5] * len(ds), color=MUTED, lw=1.2, ls='--', label='energy $\\pm k^2/2M$ (constant)')
axs[1].set_xlabel('texture $d$'); axs[1].legend(frameon=False, fontsize=8); axs[1].set_title('Same two levels, different transition strength', fontsize=9.5, color=INK)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'figM1_matter.png')); plt.close(fig); print('wrote figM1_matter.png')
# (2) Rule 30 by rows against by distinct states
j = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r30_distinct_states.json')))
bands = ['EARLY', 'MIDDLE', 'FINAL']; x = np.arange(3); wdt = 0.36
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.1))
axs[0].bar(x - wdt / 2, [j[b]['dispersion_rows'] for b in bands], wdt, color=ORANGE, label='counted by rows')
axs[0].bar(x + wdt / 2, [j[b]['dispersion_states'] for b in bands], wdt, color=BLUE, label='counted by distinct states')
axs[0].axhline(1, color=MUTED, lw=1, ls='--'); axs[0].set_xticks(x); axs[0].set_xticklabels(['early\n($N\\geq512$)', 'middle', 'final\n($N\\leq16$)'])
axs[0].set_ylabel('scatter of the split, in fair-coin units'); axs[0].legend(frameon=False, fontsize=8); axs[0].set_title('The families were merges', fontsize=9.5, color=INK)
gr = [(j[b]['soft_gain_rows_phase'] + j[b]['soft_gain_rows_width']) / 2 for b in bands]
gs = [(j[b]['soft_gain_states_phase'] + j[b]['soft_gain_states_width']) / 2 for b in bands]
axs[1].bar(x - wdt / 2, gr, wdt, color=ORANGE, label='by rows'); axs[1].bar(x + wdt / 2, gs, wdt, color=BLUE, label='by distinct states')
lo = [j[b]['control_gain_5_95_phase'][0] for b in bands]; hi = [j[b]['control_gain_5_95_phase'][1] for b in bands]
axs[1].fill_between([-0.6, 2.6], [min(lo)] * 2, [max(hi)] * 2, color=GRID, alpha=0.8, label='fair coins, 5–95%', zorder=0)
axs[1].axhline(0, color=MUTED, lw=1); axs[1].set_xticks(x); axs[1].set_xticklabels(['early', 'middle', 'final']); axs[1].set_ylabel('held-out gain of the colour model (nats)')
axs[1].legend(frameon=False, fontsize=8); axs[1].set_title('Colour steered duplicate rows', fontsize=9.5, color=INK)
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'figR1_rule30.png')); plt.close(fig); print('wrote figR1_rule30.png')
