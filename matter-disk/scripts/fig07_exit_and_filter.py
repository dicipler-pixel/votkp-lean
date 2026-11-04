# SCRIPT: MATTER-DISK-FIG07  the exit line and the instrument that reads it.
# Left: band-averaged Petermann factor <K> = 1 + u^2/(E(0)E(pi)) along v at u = 0.5, w = 1, with the
#   continued endpoint phase theta = 2 arctan(u/sqrt(E(0)E(pi))) on the right axis; <K> = 2 exactly where
#   theta = pi/2. Measured census exit 0.468 (s05a) marked.
# Right: the exit returned by the endpoint filter (rerun of the formal edition's audit, g_incoming_exit_filter).
import numpy as np, ast, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
u, w = 0.5, 1.0
v = np.linspace(0.0, 0.499, 600)
p = np.sqrt((v + w) ** 2 - u ** 2) * np.sqrt((v - w) ** 2 - u ** 2)
K = 1 + u * u / p; th = 2 * np.arctan(u / np.sqrt(p))
vex = np.sqrt(w * w + u * u - np.sqrt(4 * w * w * u * u + u ** 4 * 0 + 0) * 0) if False else None
# solve E(0)E(pi) = u^2 exactly: ((v+w)^2-u^2)((v-w)^2-u^2) = u^4
from scipy.optimize import brentq
f = lambda x: ((x + w) ** 2 - u ** 2) * ((x - w) ** 2 - u ** 2) - u ** 4
vex = brentq(f, 0.3, 0.4999)
fig, (a, b) = plt.subplots(1, 2, figsize=(13, 4.9))
a.plot(v, K, color='#c0392b', lw=2, label='$\\langle K\\rangle=1+u^2/E(0)E(\\pi)$')
a.axhline(2, color='0.5', ls='--', lw=1); a.axvline(vex, color='k', lw=1)
a.text(vex - 0.005, 3.3, f'$\\langle K\\rangle=2$ at $v={vex:.4f}$', ha='right', fontsize=9.5)
a.set_ylim(1, 4); a.set_xlabel('$v$  ($w=1$, $u=0.5$)'); a.set_ylabel('$\\langle K\\rangle$', color='#c0392b')
a2 = a.twinx(); a2.plot(v, th / np.pi, color='#1f5f6b', lw=2, ls='-.', label='$\\theta/\\pi$, $\\theta=2\\arctan(u/\\sqrt{E(0)E(\\pi)})$')
a2.axhline(0.5, color='#1f5f6b', lw=0.6, ls=':'); a2.set_ylabel('$\\theta/\\pi$', color='#1f5f6b'); a2.set_ylim(0, 1)
a.set_title('$\\langle K\\rangle=\\sec^2(\\theta/2)$: the exit line is a quarter turn', fontsize=11.5)
h1, l1 = a.get_legend_handles_labels(); h2, l2 = a2.get_legend_handles_labels(); a.legend(h1 + h2, l1 + l2, fontsize=8.5, loc='upper left')
rows = [ast.literal_eval(x) for x in open('../outputs/g_incoming_exit_filter.txt') if x.startswith('{')]
for m, c, lab in [(0.4, '#7b5ea7', 'massive $m=0.4$'), (0.0, '#c08a2e', 'massless $m=0$')]:
    rr = [r for r in rows if r['m'] == m]
    b.plot([r['cut'] for r in rr], [r['exit_gamma'] for r in rr], 'o-', color=c, lw=2, label=lab)
    for r in rr: b.annotate(f"{r['mean_Petermann']:.3f}", (r['cut'], r['exit_gamma']), (r['cut'] * 0.75, r['exit_gamma'] + 0.012), fontsize=7.5, color=c)
b.set_xscale('log'); b.set_ylim(0.1, 0.51); b.invert_xaxis(); b.set_xlabel('endpoint filter $\\delta$ (levels with $|\\nu|$ or $|1-\\nu|<\\delta$ dropped)')
b.set_ylabel('returned exit $\\gamma$'); b.set_title('The filter is part of the instrument (labels: $\\langle K\\rangle$ at exit)', fontsize=11.5)
b.legend(fontsize=9)
plt.tight_layout(); plt.savefig('../figures/fig07_exit_and_filter.png', dpi=170)
print('v at <K>=2', vex)
