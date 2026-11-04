# SCRIPT: MATTER-DISK-FIG04  the disk as a reflection chart.
# Left: one Smith disk carrying the boundary readings that Beyond the Event Horizon (ed. 10) places on it:
#   centre = matched load (S_b = 0), rim = total reflection, fermion record Gamma = tanh(omega/2T),
#   gap-step reflection Gamma = tanh(ln(D2/D1)/2). Different normalised impedances on one chart, not one object.
# Right: the single curve Gamma = tanh(eps/2) with four readings of eps marked at real values.
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig, (a, b) = plt.subplots(1, 2, figsize=(13.2, 6.2), gridspec_kw={'width_ratios': [1, 1.15]})
t = np.linspace(0, 2 * np.pi, 400)
a.fill(np.cos(t), np.sin(t), color='#f3efe6', zorder=0)
a.plot(np.cos(t), np.sin(t), color='0.15', lw=2.2)
for r in (0.33, 0.66): a.plot(r * np.cos(t), r * np.sin(t), color='0.86', lw=0.7)
a.axhline(0, color='0.7', lw=0.8)
a.scatter([0], [0], s=150, marker='o', facecolor='white', edgecolor='k', lw=2, zorder=8)
a.annotate('centre: matched load\n$Z_b=I$, $S_b=0$ returns nothing\n(horizon surface resistance = $Z_0$)', (0, 0), (-0.05, -0.62), fontsize=9,
           arrowprops=dict(arrowstyle='-', color='0.3', lw=0.8))
x = np.array([0.25, 0.5, 1, 2, 4, 8]); G = np.tanh(x / 2)
a.scatter(G, 0 * G, s=60, color='#c0392b', zorder=7, label='fermion record of a Hawking pair: $\\Gamma=\\tanh(\\hbar\\omega/2k_BT_H)$')
for xi, gi, dx in zip(x[[0, 2, 3, 5]], G[[0, 2, 3, 5]], [-0.02, -0.01, -0.02, 0.03]):
    a.annotate(f'{xi:g}', (gi, 0), (gi + dx, 0.07), fontsize=8, color='#c0392b')
a.text(0.42, 0.16, '$\\hbar\\omega/k_BT_H$', fontsize=9, color='#c0392b')
r = np.array([1 / 8, 1 / 4, 1 / 2, 3 / 4]); Gs = np.tanh(0.5 * np.log(r))
a.scatter(Gs, 0 * Gs, s=60, marker='^', color='#1f5f6b', zorder=7, label='step in spectral gap: $\\Gamma=\\tanh(\\frac{1}{2}\\ln\\Delta_2/\\Delta_1)$')
for ri, gi in zip(r, Gs):
    a.annotate(f'{ri:g}', (gi, 0), (gi - 0.03, -0.11), fontsize=8, color='#1f5f6b')
a.text(-0.75, -0.24, '$\\Delta_2/\\Delta_1$', fontsize=9, color='#1f5f6b')
th = np.linspace(0.62 * np.pi, 0.95 * np.pi, 60)
a.plot(np.cos(th), np.sin(th), color='#7b5ea7', lw=5, alpha=0.75, solid_capstyle='round')
a.annotate('rim $|\\Gamma|=1$: total reflection\n(past a geodesic turning point;\npolar stratum = perfect mirror)', (np.cos(0.8 * np.pi), np.sin(0.8 * np.pi)), (-1.28, 1.05), fontsize=9,
           color='#5a3f85', arrowprops=dict(arrowstyle='-', color='#7b5ea7', lw=0.8))
a.text(0.0, -1.16, 'inside: passive, $\\|S_b\\|\\leq 1$', ha='center', fontsize=9, color='0.3')
a.set_xlim(-1.35, 1.35); a.set_ylim(-1.75, 1.45); a.set_aspect('equal'); a.axis('off')
a.legend(fontsize=8, loc='lower center', bbox_to_anchor=(0.5, 0.0), framealpha=0.95)
a.set_title('One disk, three boundary readings', fontsize=12)
e = np.linspace(-6, 6, 400)
b.plot(e, np.tanh(e / 2), color='0.15', lw=2)
b.axhline(1, color='0.7', ls='--', lw=0.8); b.axhline(-1, color='0.7', ls='--', lw=0.8); b.axhline(0, color='0.85', lw=0.8); b.axvline(0, color='0.85', lw=0.8)
pts = [(np.log((1 - 0.2) / 0.2), 'occupation odds: $\\varepsilon=\\ln((1-\\nu)/\\nu)$, $\\nu=0.2$', '#1b6f8a'),
       (np.log(54.4177655282 / 24.587389011), 'helium thresholds: $\\varepsilon=\\ln I_1/I_0$', '#c08a2e'),
       (np.log(2.0), 'gap step: $\\varepsilon=\\ln\\Delta_2/\\Delta_1$, ratio 2', '#1f5f6b'),
       (1.0, 'Hawking fermion record: $\\varepsilon=\\hbar\\omega/k_BT_H=1$', '#c0392b')]
pts = sorted(pts, key=lambda q: -q[0] if False else -np.tanh(q[0] / 2))
for i, (ei, lab, c) in enumerate(pts):
    gi = np.tanh(ei / 2)
    b.scatter([ei], [gi], s=70, color=c, zorder=6, edgecolor='k', lw=0.6)
    b.annotate(f'{lab}\n$\\Gamma={gi:.4f}$', (ei, gi), (1.9, 0.12 - 0.3 * i), fontsize=8.5, color=c, va='center',
               arrowprops=dict(arrowstyle='-', color=c, lw=0.7, relpos=(0, 0.5)))
b.set_xlabel('rapidity $\\varepsilon=\\ln z$'); b.set_ylabel('$\\Gamma$')
b.set_title('$\\Gamma=\\frac{z-1}{z+1}=\\tanh\\frac{\\varepsilon}{2}$: one function, every boundary ratio', fontsize=12)
b.set_xlim(-6, 6); b.set_ylim(-1.25, 1.25)
plt.tight_layout(); plt.savefig('../figures/fig04_reflection_chart.png', dpi=170)
print('Hawking points', dict(zip(x.tolist(), np.round(G, 6).tolist())))
print('gap points', dict(zip(r.tolist(), np.round(Gs, 6).tolist())))
print('readings', [(round(p[0], 6), round(float(np.tanh(p[0] / 2)), 6)) for p in pts])
