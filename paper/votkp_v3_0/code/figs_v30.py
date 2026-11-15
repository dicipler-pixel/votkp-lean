# SCRIPT: FIGS-V30-01
# Figures 35 and 36 of VOTKP v3.0, drawn from the threshold archive (no fitted quantity).
import gzip, json, math, sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
RY = 13.605693122994; W = 3 + 2*math.sqrt(2)
d = {r['Z']: r for r in json.load(gzip.open(sys.argv[1]))['records']}
ie = lambda Z: {t['q']: (t['IE_eV'], t.get('unc_eV') or 0) for t in d[Z]['thresholds'] if t.get('IE_eV')}
NIGHT, PANEL, GOLD, GOLD2, INK, MESH, ROSE = '#03050c', '#070b1a', '#e2bd6c', '#f0d495', '#e6dfcd', '#7fa6e8', '#e98a8a'
plt.rcParams.update({'font.family': 'DejaVu Serif', 'font.size': 12, 'text.color': INK, 'axes.labelcolor': INK, 'xtick.color': INK,
                     'ytick.color': INK, 'axes.edgecolor': '#56627f', 'figure.facecolor': NIGHT, 'axes.facecolor': PANEL, 'savefig.facecolor': NIGHT})
CORES = [(2, 2, 'He core'), (10, 3, 'Ne core'), (18, 4, 'Ar core'), (36, 5, 'Kr core'), (54, 6, 'Xe core'), (86, 7, 'Rn core')]
# ---- Figure 35: each core line crosses the half line once
fig, ax = plt.subplots(figsize=(10.5, 5.6))
cols = [GOLD, MESH, '#9d86f0', '#7fd6b8', ROSE, '#d9d9d9']
for (core, n, lab), c in zip(CORES, cols):
    xs, ys = [], []
    for v in range(1, 9):
        Z = core + v; e = ie(Z); q = v - 1
        if q in e and q+1 in e: xs.append(v); ys.append(e[q+1][0]/e[q][0])
    ax.plot(xs, ys, '-o', color=c, lw=1.8, ms=5.5, label=lab)
    ax.axhline((n/(n-1))**2, color=c, lw=0.8, ls=':', alpha=0.75)
    ax.text(8.12, (n/(n-1))**2, r'$(%d/%d)^2$' % (n, n-1), color=c, fontsize=9.5, va='center')
ax.axhline(W, color='#ff5a6e', lw=1.6, ls='--'); ax.text(4.55, W*1.045, r'half line  $\Gamma^2=\frac{1}{2}$,  $z=3+2\sqrt{2}$', color='#ff9aa6', fontsize=12)
ax.set_yscale('log'); ax.set_yticks([1.5, 2, 3, 4, 5.83, 8, 10, 14]); ax.set_yticklabels(['1.5', '2', '3', '4', '5.83', '8', '10', '14']); ax.minorticks_off()
ax.set_xlim(0.55, 8.9); ax.set_ylim(1.3, 16)
ax.set_xlabel('electrons outside the closed core (1 = alkali-like ion)'); ax.set_ylabel(r'core-opening step ratio  $z = IE_{\rm core}/IE_{\rm valence}$')
for v, s in zip(range(1, 5), ['Li', r'Be$^{+}$', r'B$^{2+}$', r'C$^{3+}$']):
    e = ie(2+v); ax.annotate(s, (v, e[v][0]/e[v-1][0]), textcoords='offset points', xytext=(7, 5), color=GOLD2, fontsize=10)
e = ie(7); ax.annotate(r'N$^{4+}$', (5, e[5][0]/e[4][0]), textcoords='offset points', xytext=(6, -14), color=GOLD2, fontsize=10)
for Z, s in [(11, 'Na'), (19, 'K'), (37, 'Rb'), (55, 'Cs'), (87, 'Fr')]:
    e = ie(Z); ax.annotate(s, (1, e[1][0]/e[0][0]), textcoords='offset points', xytext=({'Na':9,'K':9,'Rb':-26,'Cs':-25,'Fr':-23}[s], {'Na':2,'K':3,'Rb':5,'Cs':-1,'Fr':-9}[s]), color=INK, fontsize=10)
leg = ax.legend(frameon=False, ncol=3, loc='lower left', fontsize=10.5)
fig.tight_layout(); fig.savefig('fig35_core_lines.png', dpi=170); plt.close(fig)
# ---- Figure 36: fixed alkali charge ratio against the rising wall ratio
fig, ax = plt.subplots(figsize=(10.5, 5.2))
ns = [x/100 for x in range(190, 761)]
ax.plot(ns, [(1+math.sqrt(2))*(n-1)/n for n in ns], color='#ff5a6e', lw=2, ls='--', label=r'wall ratio  $(1+\sqrt{2})\,(n-1)/n$')
ax.axhline(1+math.sqrt(2), color='#ff5a6e', lw=0.8, ls=':'); ax.text(2.0, 1+math.sqrt(2)-0.07, r'$1+\sqrt{2}$', color='#ff9aa6', fontsize=11)
pts = []
for Z, n, s in [(3, 2, 'Li'), (11, 3, 'Na'), (19, 4, 'K'), (37, 5, 'Rb'), (55, 6, 'Cs'), (87, 7, 'Fr')]:
    e = ie(Z); Zv = n*math.sqrt(e[0][0]/RY); Zc = (n-1)*math.sqrt(e[1][0]/RY); r = Zc/Zv
    lo = (n-1)*math.sqrt((e[1][0]-e[1][1])/RY)/Zv; hi = (n-1)*math.sqrt((e[1][0]+e[1][1])/RY)/Zv
    pts.append((s, n, r))
    ax.errorbar([n], [r], yerr=[[r-lo], [hi-r]], fmt='o', color=GOLD if s != 'Fr' else INK, ms=9, capsize=5, lw=1.4,
                mfc=GOLD if s != 'Fr' else 'none', mec=GOLD if s != 'Fr' else INK)
    ax.annotate('%s  %.3f' % (s, r), (n, r), textcoords='offset points', xytext=(9, 9 if s != 'Cs' else 11), color=GOLD2, fontsize=11)
band = [p[2] for p in pts if p[0] in ('Na', 'K', 'Rb', 'Cs')]
ax.axhspan(min(band), max(band), color=GOLD, alpha=0.16, lw=0); ax.text(3.0, min(band)-0.075, 'band of Na, K, Rb, Cs: 2.022 to 2.045', color=GOLD2, fontsize=11)
ax.set_xlim(1.85, 7.6); ax.set_ylim(1.15, 2.5); ax.set_xticks([2, 3, 4, 5, 6, 7])
ax.set_xlabel(r'principal quantum number $n$ of the outer electron'); ax.set_ylabel(r'charge ratio  $Z_c/Z_v$')
ax.legend(frameon=False, loc='lower right', fontsize=11)
fig.tight_layout(); fig.savefig('fig36_charge_ratio.png', dpi=170); plt.close(fig)
print('ok', pts)
