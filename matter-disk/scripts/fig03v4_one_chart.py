# SCRIPT: MATTER-DISK-FIG03V4  one Smith disk, every scale, every point at its true signed value.
# Real ratios sit ON the real axis (Im Gamma = 0); labels are moved off the axis with leader lines only.
# Nuclear ratios use VOTKP 15.4's order z = S_next / S_first: bound nuclei give z < 1, so Gamma < 0.
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
ns = {}; exec(open('s02_ladder.py').read().split('op=lambda')[0], ns)
ssh = {}; exec(open('nhssh_lib_and_s03a_occupations.py').read().split('w=1.0')[0], ssh)
G = lambda z: (z - 1) / (z + 1)
fig, ax = plt.subplots(figsize=(8.8, 8.8))
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), color='0.2', lw=1.5)
for r in (0.25, 0.5, 0.75): ax.plot(r * np.cos(t), r * np.sin(t), color='0.9', lw=0.7)
ax.axhline(0, color='0.75', lw=0.8); ax.axvline(0, color='0.88', lw=0.7)
# matter: Ising census ladder (c = 1/2), both signs of the level energy
xi, em = ns['ladder'](1.02, 8192); lev = em[::2][:5]
Gl = np.concatenate([np.tanh(lev / 2), -np.tanh(lev / 2)])
ax.scatter(Gl, 0 * Gl, s=52, color='#1b6f8a', zorder=6, label='matter: Ising census levels (c = 1/2), $\\Gamma=\\tanh(\\varepsilon/2)$, both signs')
# atom: sodium thresholds, NIST ASD (eV), composite peel from the first removal
IE = np.array([5.139076, 47.28636, 71.6200, 98.936, 138.39, 172.18, 208.50, 264.18, 299.856, 1465.091, 1648.659])
walk = np.tanh(0.5 * np.log(IE / IE[0]))
ax.scatter(walk, 0 * walk, s=30, marker='o', facecolor='white', edgecolor='#c08a2e', lw=1.6, zorder=7, label='atom: sodium peel walk $\\tanh(\\frac{1}{2}\\ln I_k/I_1)$ (NIST)')
ax.scatter([0.377575], [0], marker='D', s=80, color='#c08a2e', edgecolor='k', zorder=8, label='atom: helium $\\Gamma_0=0.377575$')
# nucleus, z = S_next / S_first (keV, NUBASE2020 via VOTKP 15.4)
nuc = {'$^7$Li': (7251.1, 5664.4), '$^4$He': (20577.6, 5493.5), '$^5$He': (-734.8, 20577.6), '$^5$Li': (-1966.1, 19813.9), '$^8$Be': (-91.8, 7366.6)}
lab_y = {'$^7$Li': -0.16, '$^4$He': -0.16, '$^5$He': -0.42, '$^5$Li': -0.16, '$^8$Be': -0.30}
lab_x = {'$^7$Li': -0.06, '$^4$He': -0.06, '$^5$He': -0.02, '$^5$Li': -0.06, '$^8$Be': -0.20}
for k, (s1, s2) in nuc.items():
    g = G(s2 / s1)
    inside = abs(g) < 1
    ax.scatter([g], [0], marker='s', s=70, color='#7b5ea7' if inside else 'white', edgecolor='#7b5ea7', lw=2, zorder=9)
    ax.annotate(f'{k}  {g:+.3f}', (g, 0), (g + lab_x[k], lab_y[k]), fontsize=9, color='#5a3f85',
                arrowprops=dict(arrowstyle='-', color='#7b5ea7', lw=0.7))
ax.scatter([], [], marker='s', color='#7b5ea7', label='nucleus: bound inside ($\\Gamma<0$), unbound outside ($\\Gamma>1$)')
# opened matter, u = 0.5, before and past the exit
for v, c, lab in [(0.30, '#2a9d55', 'opened matter, gapped: complex $\\Gamma$ inside'), (0.49, '#d1495b', 'opened matter past the exit: $\\Gamma$ leaves the disk')]:
    nu = np.linalg.eigvals(ssh['corr'](v, 1.0, 0.5, 2000, 40)); nu = nu[(abs(nu) > 1e-9) & (abs(1 - nu) > 1e-9)]
    g = 1 - 2 * nu; g = g[abs(g) < 1.6]
    ax.scatter(g.real, g.imag, s=14, color=c, alpha=0.85, zorder=5, label=lab)
ax.text(0, 1.06, 'rim $|\\Gamma|=1$: rapidity turned a quarter ($|{\\rm Im}\\,W|=\\pi/2$)', ha='center', fontsize=9.5, color='0.3')
ax.text(0.02, 0.04, 'centre: $z=1$', fontsize=8.5, color='0.35')
ax.set_xlim(-1.3, 1.34); ax.set_ylim(-1.34, 1.3); ax.set_aspect('equal')
ax.set_xlabel('Re $\\Gamma$'); ax.set_ylabel('Im $\\Gamma$')
ax.set_title('Matter, then on down: one chart, signed values', fontsize=13)
ax.legend(fontsize=7.6, loc='lower left', framealpha=0.95)
plt.tight_layout(); plt.savefig('../figures/fig03v4_one_chart.png', dpi=170)
print('sodium walk end', walk[-1]); print({k: round(G(b / a), 6) for k, (a, b) in nuc.items()})
