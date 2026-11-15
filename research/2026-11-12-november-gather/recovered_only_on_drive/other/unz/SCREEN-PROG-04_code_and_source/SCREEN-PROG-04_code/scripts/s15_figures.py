# SCRIPT: s15_figures
# The six figures of SCREEN-PROG-04, computed from screen04_model. SVG with all text as paths; the PDF is converted
# from that SVG, so it contains vector paths and no fonts at all.
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, minimize
from screen04_model import *
from s13_third_energy_forecast import Z
plt.rcParams.update({'text.usetex': False, 'font.family': 'serif', 'font.serif': ['DejaVu Serif'], 'mathtext.fontset': 'cm', 'font.size': 9, 'axes.labelsize': 9,
    'legend.fontsize': 7.5, 'xtick.labelsize': 8, 'ytick.labelsize': 8, 'svg.fonttype': 'path',
    'axes.spines.top': False, 'axes.spines.right': False, 'lines.linewidth': 1.4})
INK, BLUE, GOLD, RED, GREEN, GREY, VIOLET = '#1d2430', '#2a6fdb', '#c98a00', '#c2410c', '#1b8a5a', '#8a96a8', '#6d4fc2'
OUT = '../figs/'
import cairosvg
def save(fig, name):
    fig.savefig(OUT+name+'.svg', bbox_inches='tight'); fig.savefig(OUT+name+'.png', dpi=200, bbox_inches='tight'); plt.close(fig)
    cairosvg.svg2pdf(url=OUT+name+'.svg', write_to=OUT+name+'.pdf')

# F1 leverage: thermal limit (left, powers of ten) against beam energies (right, plain factor)
U = np.linspace(100, 500, 200); fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 2.7))
a1.plot(U, (lnR(0, U) - lnR(0, 100))/np.log(10), color=INK); a1.set_xlabel(r'$U_e$ (eV)'); a1.set_ylabel(r'$\log_{10}\,[R(0,U_e)/R(0,100\,\mathrm{eV})]$')
a1.set_title(r'thermal limit, $E \to 0$', fontsize=8); a1.set_xlim(100, 500)
for E, c, lab in [(1000, VIOLET, r'$E = 1$ keV'), (2000, RED, r'$E = 2$ keV'), (3000, GOLD, r'$E = 3$ keV'), (6000, BLUE, r'$E = 6$ keV')]:
    a2.plot(U, np.exp(lnR(E, U) - lnR(E, 100)), color=c, label=lab)
a2.set_yscale('log'); a2.set_xlabel(r'$U_e$ (eV)'); a2.set_ylabel(r'$R(E,U_e)/R(E,100\,\mathrm{eV})$'); a2.set_title('beam energies (centre of mass)', fontsize=8)
a2.legend(frameon=False, loc='upper left'); a2.set_xlim(100, 500); fig.tight_layout(); save(fig, 'f1_leverage')

# F2 acquisition order and normalisation
L = lambda f: 200 + 300*f
fits = [('high$\\to$low, bins, free', fit_const(campaign(L)), GOLD), ('high$\\to$low, points, free', fit_const(campaign(L, point=True)), RED),
        ('high$\\to$low, bins, fixed', fit_const(campaign(L), fixed=True), GREEN), ('low$\\to$high, bins, free', fit_const(campaign(L, SCAN[::-1]), SCAN[::-1]), BLUE)]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 2.7), gridspec_kw={'width_ratios': [1.3, 1]})
f = np.linspace(0, 1, 300); a1.plot(f, L(f), color=INK)
cm = plt.get_cmap('coolwarm')
for i, E in enumerate(SCAN): a1.axvspan(i/8, (i+1)/8, color=cm(1 - i/7), alpha=0.18, lw=0); a1.text((i+.5)/8, 205, '%g' % (E/1000), ha='center', fontsize=6.5)
a1.set_xlabel(r'accumulated fluence $\Phi$ (energy in keV, high$\to$low)'); a1.set_ylabel(r'$U_e^{\mathrm{inst}}$ (eV)'); a1.set_ylim(180, 520)
for y, t in [(200, 'start'), (350, 'mean'), (500, 'endpoint')]: a2.axhline(y, color=GREY, lw=0.8, ls='--'); a2.text(-0.45, y+6, t, fontsize=6.5, color=GREY, ha='left')
for k, (lab, v, c) in enumerate(fits): a2.plot(k, v, 'o', color=c, ms=6); a2.text(k, v+14, '%.0f' % v, ha='center', fontsize=7)
a2.set_xticks(range(4)); a2.set_xticklabels([x[0] for x in fits], rotation=35, ha='right', fontsize=6.5); a2.set_ylabel(r'constant-model fit $\widehat U$ (eV)'); a2.set_ylim(150, 600); a2.set_xlim(-0.5, 3.7)
fig.tight_layout(); save(fig, 'f2_order')

# F3 conditioning: single descending sweep vs down-up at fixed total fluence (uniform 2%)
def chi_grid(Es, sig):
    d = campaign(L, Es, nodes=200); u0 = np.linspace(80, 320, 90); du = np.linspace(150, 450, 90); G = np.zeros((90, 90))
    for i, a in enumerate(u0):
        for j, b in enumerate(du):
            r = (d - campaign(lambda f: a + b*f, Es, nodes=60))/sig; G[j, i] = np.sum((r - r.mean())**2)
    return u0, du, G - G.min()
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.8), sharey=True)
for ax, Es, sig, t in [(axs[0], SCAN, 0.02, 'one high$\\to$low sweep (8 exposures)'), (axs[1], np.concatenate([SCAN, SCAN[::-1]]), 0.02*np.sqrt(2), 'down and back up (16, same total fluence)')]:
    u0, du, G = chi_grid(Es, sig); ax.contourf(u0, du, G, levels=[0, 1, 4, 9, 25], colors=['#1b8a5a', '#5fb98a', '#a9d8bd', '#e3f1e8'])
    ax.contour(u0, du, G, levels=[1, 4, 9], colors=INK, linewidths=0.5); ax.plot(200, 300, 'k+', ms=8); ax.set_title(t, fontsize=8); ax.set_xlabel(r"start $U_0'$ (eV)")
axs[0].set_ylabel(r"drift $\Delta U'$ (eV)"); fig.tight_layout(); save(fig, 'f3_conditioning')

# F4 protocol: six interleaved dose steps
fig, ax = plt.subplots(figsize=(5.2, 2.8)); steps = (np.arange(6)+0.5)/6; SIG = 0.02462/3.403e-3
ax.plot(f, 300 + 100*f, color=BLUE, label=r'evolving target, $300\to400$ eV')
ax.axhline(350, color=GREY, ls='--', lw=1, label=r'state that does not evolve')
nz = np.array([0.6, -1.1, 0.3, 0.9, -0.5, -0.2]); ax.errorbar(steps, 300 + 100*steps + nz*SIG, yerr=SIG, fmt='o', color=GOLD, ms=4, capsize=2, label=r'interleaved ratio, $\sigma = 7.2$ eV per step')
drift = 0.03*6*steps/3.403e-3; ax.plot(steps, 300 + 100*steps + drift, 'x', color=RED, ms=5, label=r'same drift, energies not interleaved (3%/h)')
ax.set_xlabel(r'accumulated fluence (six steps)'); ax.set_ylabel(r'$U_e$ read from the ratio (eV)'); ax.legend(frameon=False, fontsize=6.8, loc='upper left'); ax.set_ylim(280, 470)
save(fig, 'f4_protocol')

# F5 third-energy forecast against spread
s = np.linspace(20, 250, 47); fig, ax = plt.subplots(figsize=(5.2, 2.8))
for mode, c, lab in [('indep', GOLD, 'stopping residual independent per step'), ('shared_smooth', GREEN, 'one smooth stopping error, shared'), ('shared_unrelated', RED, 'stopping shared, unrelated between ratios')]:
    ax.plot(s, [Z(x, mode=mode) for x in s], color=c, label=lab)
ax.axhline(3, color=GREY, lw=0.8, ls=':'); ax.axvline(150, color=GREY, lw=0.8, ls=':')
ax.set_xlabel(r'screening spread $s$ across the target (eV), $\mu = 340$ eV'); ax.set_ylabel(r'expected separation from $s=0$, $\sqrt{q_A}$')
ax.set_yscale('log'); ax.legend(frameon=False, loc='upper left'); save(fig, 'f5_third_energy')

# F6 spread and additive plateau give the same three numbers
mu_h = 340.; E = np.linspace(1500, 6000, 200); Es3 = np.array([2000, 3500, 6000])
P = 0.10*np.exp(lnR(2000, mu_h))
lnHP = lambda e: np.log(np.exp(lnR(e, mu_h)) + P)
def ratios(fn): return np.array([fn(2000)-fn(6000), fn(3500)-fn(6000)])
target = ratios(lnHP)
res = minimize(lambda p: np.sum((ratios(lambda e: lnYmix(e, p[0], p[1])) - target)**2), [340, 140], method='Nelder-Mead', options={'xatol':1e-6, 'fatol':1e-16, 'maxiter':4000})
mu_s, s_s = res.x
fig, ax = plt.subplots(figsize=(5.2, 2.8))
base = lambda e: lnR(e, mu_h)
c_sp = np.array([lnYmix(e, mu_s, s_s) for e in E]); c_hp = lnHP(E); c_b = base(E)
off_sp = c_sp[-1] - c_b[-1]; off_hp = c_hp[-1] - c_b[-1]
ax.plot(E/1000, 100*(c_hp - c_b - off_hp), color=RED, label=r'one $U_e = 340$ eV plus a 10% additive plateau')
ax.plot(E/1000, 100*(c_sp - c_b - off_sp), color=BLUE, ls='--', label=r'spread: $\mu = %.0f$, $s = %.0f$ eV, no plateau' % (mu_s, s_s))
for e in Es3: ax.axvline(e/1000, color=GREY, lw=0.8, ls=':')
ax.set_xlabel(r'centre-of-mass energy (keV); dotted: 2, 3.5, 6 keV'); ax.set_ylabel(r'$\ln Y$ relative to one $U_e$, scaled at 6 keV (%)')
ax.legend(frameon=False, loc='upper right'); ax.set_xlim(1.5, 6.05); save(fig, 'f6_plateau')
print('plateau mimic: mu %.1f s %.1f residual %.2e' % (mu_s, s_s, res.fun))
