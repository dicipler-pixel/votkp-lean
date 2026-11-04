# SCRIPT: MATTER-DISK-FIG06  equal present records, different futures.
# Left: R3 / M1. Weights w0 = (1,1,1,1)/4 and w1 = (3,7,1,5)/16 on levels (-3,-1,1,3) share moments 0,1,2;
#   retained survival |sum w e^{-i lambda t}|^2 differs; the reflected weights (5,1,7,3)/16 give the same
#   intensity as w1 at every t (intensity-only readout erases the distinction).
# Right: K2 / K4. Equal density, flow and stress; free streaming separates density as -16 a eta rho sin^3(k v0 t)
#   at sin(kx) = 1; a pre-release velocity reset multiplies the contrast by exp(-nu s).
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
lam = np.array([-3, -1, 1, 3.])
W = {'uniform $(1,1,1,1)/4$': np.ones(4) / 4, '$(3,7,1,5)/16$': np.array([3, 7, 1, 5]) / 16, 'reflected $(5,1,7,3)/16$': np.array([5, 1, 7, 3]) / 16}
t = np.linspace(0, np.pi, 600)
fig, (a, b) = plt.subplots(1, 2, figsize=(13, 4.9))
sty = ['-', '-', ':']; col = ['#1b6f8a', '#c0392b', '0.1']
for (k, wv), s_, c in zip(W.items(), sty, col):
    amp = (wv[None, :] * np.exp(-1j * lam[None, :] * t[:, None])).sum(1)
    a.plot(t, abs(amp) ** 2, s_, color=c, lw=2 if s_ == '-' else 2.4, label=k)
    print(k, 'moments', [float((wv * lam ** m).sum()) for m in range(4)])
a.axvline(np.pi / 4, color='0.6', lw=0.8); a.text(np.pi / 4 + 0.03, 0.9, '$t=\\pi/4$: $0$ vs $1/32$', fontsize=9)
a.set_xlabel('$t$'); a.set_ylabel('retained survival $|a(t)|^2$')
a.set_title('Same spectrum, same $A$, same $BB^\\dagger=5$: different survival', fontsize=11.5)
a.legend(fontsize=9)
aa, eta, rho = 1 / 24, 0.5, 1.0
for ns_, ls in [(0, '-'), (0.5, '--'), (1.5, ':')]:
    dn = -16 * aa * eta * rho * np.exp(-ns_) * np.sin(t) ** 3
    b.plot(t, dn, ls, color='#7b5ea7', lw=2, label=f'reset before release, $\\nu s={ns_:g}$')
b.axhline(0, color='0.7', lw=0.8)
b.scatter([np.pi / 2], [-1 / 3], color='k', zorder=5); b.annotate('$\\Delta n=-1/3$', (np.pi / 2, -1 / 3), (np.pi / 2 + 0.45, -0.335), fontsize=10)
b.set_xlabel('$k v_0 t$'); b.set_ylabel('$\\Delta n$ at $\\sin kx=1$')
b.set_title('Same density, flow and stress: density splits as $\\sin^3$', fontsize=11.5)
b.legend(fontsize=9, loc='lower left')
plt.tight_layout(); plt.savefig('../figures/fig06_records_and_futures.png', dpi=170)
for k, wv in W.items():
    amp = (wv * np.exp(-1j * lam * np.pi / 4)).sum(); print(k, 'survival at pi/4', round(abs(amp) ** 2, 12))
