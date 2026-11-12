# SCRIPT: FIGS-V31-01
# Figures 37 and 38 of VOTKP v3.1. Closed forms only (checked in feed_loop_01/02/03.py); nothing fitted.
import math, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
NIGHT, PANEL, GOLD, GOLD2, INK, MESH, ROSE = '#03050c', '#070b1a', '#e2bd6c', '#f0d495', '#e6dfcd', '#7fa6e8', '#e98a8a'
plt.rcParams.update({'font.family': 'DejaVu Serif', 'font.size': 12, 'text.color': INK, 'axes.labelcolor': INK, 'xtick.color': INK,
                     'ytick.color': INK, 'axes.edgecolor': '#56627f', 'figure.facecolor': NIGHT, 'axes.facecolor': PANEL, 'savefig.facecolor': NIGHT})
G2 = lambda z: ((z-1)/(z+1))**2
# ---- Figure 37: the loop of two perpendicular steps
R = np.linspace(0, 0.4999, 600); s = np.sqrt(1-2*R); rho = np.sqrt((1-s)/(1+s))
fig, (a, b) = plt.subplots(1, 2, figsize=(12.2, 5.0))
a.plot(R, rho, color=GOLD, lw=2.2); a.axhline(1/math.sqrt(2), color='#ff5a6e', lw=1.4, ls='--')
a.text(0.012, 0.735, r'half-line sphere, radius $1/\sqrt{2}$', color='#ff9aa6', fontsize=11)
for z, lab, dx, dy in [(3, r'$z=3$:  $\rho=\sqrt{2}-1$', 0.012, -0.075), (5, r'$z=5$:  $\rho^2=\frac{1}{2}$', -0.155, 0.045)]:
    r_ = G2(z); s_ = math.sqrt(1-2*r_); p = math.sqrt((1-s_)/(1+s_)); a.plot([r_], [p], 'o', color=GOLD2, ms=8); a.text(r_+dx, p+dy, lab, color=GOLD2, fontsize=11)
a.axvline(0.5, color=MESH, lw=1.1, ls=':'); a.text(0.488, 0.06, r'wall  $\Gamma^2=\frac{1}{2}$', color=MESH, fontsize=10.5, rotation=90, va='bottom', ha='right')
a.set_xlim(0, 0.52); a.set_ylim(0, 1.02); a.set_xlabel(r'$\Gamma^2$ of one step'); a.set_ylabel(r'radius $\rho$ of the centre of turn'); a.set_title('where the loop turns', color=INK, fontsize=12.5)
Rb = np.linspace(0, 0.56, 300)
b.plot(Rb, 2*Rb, color=MESH, lw=2.2, label=r'push on the layer  $P=2\Gamma^2$'); b.plot(R, 1-2*R, color=ROSE, lw=2.2, label=r'$1/K=T-R=1-2\Gamma^2$')
b.axvline(0.5, color=MESH, lw=1.1, ls=':'); b.axhline(1, color='#56627f', lw=0.8)
for z, lab in [(3, r'$z=3$:  $K=2$'), (5, r'$z=5$:  $K=9$')]:
    r_ = G2(z); b.plot([r_], [1-2*r_], 'o', color=GOLD2, ms=8); b.text(r_+0.012, 1-2*r_+0.035, lab, color=GOLD2, fontsize=11)
b.set_xlim(0, 0.56); b.set_ylim(0, 1.22); b.set_xlabel(r'$\Gamma^2$ of one step'); b.legend(loc='upper left', bbox_to_anchor=(0.30, 1.0), frameon=False, fontsize=10.5); b.set_title('obliqueness and push', color=INK, fontsize=12.5)
fig.tight_layout(); fig.savefig('fig37_loop.png', dpi=150); plt.close(fig)
# ---- Figure 38: the loop-fed signal on the peel disk at z = 5
th = 2*math.acos(1-2*(G2(5)/(1-G2(5)))**2); t = np.linspace(0, 6, 1200)
fig, ax = plt.subplots(figsize=(10.5, 4.9))
for s2, lab, c in [(1.0, r'arm $i$ or $j$:  $\sin^2\varphi=1$', GOLD), (8/9, r'arm $k$:  $\sin^2\varphi=2\Gamma^2=\frac{8}{9}$', MESH), (0.30108, r'diagonal $(1,1,1)$:  $\sin^2\varphi=0.301$', ROSE)]:
    ax.plot(t, -math.sqrt(s2)*np.sin(t*th), color=c, lw=1.9, label=lab)
for y in (1/math.sqrt(2), -1/math.sqrt(2)): ax.axhline(y, color='#ff5a6e', lw=1.3, ls='--')
ax.text(6.06, 1/math.sqrt(2), r'$\Gamma^2=\frac{1}{2}$', color='#ff9aa6', fontsize=11, va='center')
for n in range(7): ax.axvline(n, color='#2a3350', lw=0.7)
ax.set_xlim(0, 6.55); ax.set_ylim(-1.12, 1.5); ax.set_xlabel('passes of the loop'); ax.set_ylabel(r'$\Gamma=1-2c$ of the read share')
ax.legend(loc='upper left', ncol=3, frameon=False, fontsize=10); fig.tight_layout(); fig.savefig('fig38_signal.png', dpi=150); plt.close(fig)
print('theta/2pi', th/(2*math.pi))
