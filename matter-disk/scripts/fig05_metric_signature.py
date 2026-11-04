# SCRIPT: MATTER-DISK-FIG05  the opened plane's metric signature, drawn from the exact determinant
# det Q = -u^2 w^2 cos^2 k / (16 s^3), s = E^2 = v^2 + w^2 + 2 v w cos k - u^2  (u = 0.5, w = 1).
# Orange: s > 0, det < 0, Lorentzian. Blue: s < 0, negative definite. Dashed: cos k = 0, degenerate.
# Black: s = 0, where the formula is singular (exceptional points). Stars: critical points k = pi, v = w -+ u.
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
u, w = 0.5, 1.0
K, V = np.meshgrid(np.linspace(0, 2 * np.pi, 800), np.linspace(0, 2, 600))
s = V ** 2 + w ** 2 + 2 * V * w * np.cos(K) - u ** 2
sign = np.where(s > 0, 1, 0)
fig, ax = plt.subplots(figsize=(8.6, 5.6))
ax.pcolormesh(K, V, sign, cmap=ListedColormap(['#4fa3c7', '#e07b39']), shading='auto')
ax.contour(K, V, s, levels=[0], colors='k', linewidths=1.6)
for kk in (np.pi / 2, 3 * np.pi / 2): ax.axvline(kk, color='k', ls='--', lw=1)
ax.scatter([np.pi, np.pi], [w - u, w + u], marker='*', s=260, color='k', zorder=5)
ax.text(0.15, 1.85, 'Lorentzian: $s>0$, $\\det Q<0$', fontsize=10, color='white', weight='bold')
ax.text(np.pi - 0.42, 1.0, 'negative\ndefinite\n$s<0$', fontsize=9, color='white', weight='bold', ha='center')
ax.text(np.pi / 2 + 0.05, 0.08, '$\\cos k=0$: degenerate', fontsize=8.5, color='k', rotation=90, va='bottom')
ax.set_xlabel('momentum $k$'); ax.set_ylabel('hopping $v$  ($w=1$, $u=0.5$)')
ax.set_title('$\\det Q=-\\frac{u^2w^2\\cos^2k}{16\\,s^3}$,   $s=E(k)^2$', fontsize=13)
plt.tight_layout(); plt.savefig('../figures/fig05_metric_signature.png', dpi=170)
cells = np.mean((s > 0) & (np.abs(np.cos(K)) > 1e-9))
print('Lorentzian fraction of this grid', round(float(cells), 4))
