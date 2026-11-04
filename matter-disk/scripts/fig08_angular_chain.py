# SCRIPT: MATTER-DISK-FIG08  the angular gas chain L = -i k M - kappa (I - P0), k = 1.
# Left (ANG1): reference impedance Z_b(s) = 1/g0(s) - s, g0 = arctan(k/s)/k, tends to 2k/pi as s -> 0+.
# Middle (ANG2): isolated real pole s* = k cot(k/kappa) - kappa, right of the cut at s = -kappa, born at kappa = 2k/pi.
# Right (ANG3): |(L^q)_{2,l}| is zero below q = l - 2: a planted moment reaches stress no sooner than order l - 2.
import numpy as np, math, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
k = 1.0
fig, (a, b, c) = plt.subplots(1, 3, figsize=(14.5, 4.4))
s = np.logspace(-4, 1.2, 400); Z = 1 / (np.arctan(k / s) / k) - s
a.semilogx(s, Z, color='#1b6f8a', lw=2); a.axhline(2 * k / np.pi, color='#c0392b', ls='--', lw=1)
a.text(2e-4, 2 / np.pi - 0.05, '$2k/\\pi=0.6366$', color='#c0392b', fontsize=10)
a.set_xlabel('$s$'); a.set_ylabel('$Z_b(s)$'); a.set_title('ANG1: free-streaming impedance', fontsize=11)
kap = np.linspace(2 / np.pi + 1e-4, 3, 400); ps = k / np.tan(k / kap) - kap
b.plot(kap, ps, color='#7b5ea7', lw=2, label='pole $s^*=k\\cot(k/\\kappa)-\\kappa$')
b.plot(kap, -kap, color='0.4', ls=':', lw=1.5, label='branch point $s=-\\kappa$')
b.axvline(2 / np.pi, color='#c0392b', ls='--', lw=1); b.text(2 / np.pi + 0.04, -2.6, '$\\kappa=2k/\\pi$', color='#c0392b')
b.set_xlabel('$\\kappa$'); b.set_ylabel('$s$'); b.set_title('ANG2: the pole leaves the cut at $\\kappa=2k/\\pi$', fontsize=11); b.legend(fontsize=8.5)
n = 20; cc = np.array([(l + 1) / math.sqrt((2 * l + 1) * (2 * l + 3)) for l in range(n - 1)])
M = np.diag(cc, 1) + np.diag(cc, -1); L = -1j * k * M
img = np.zeros((9, 7))
for qi, q in enumerate(range(9)):
    Lq = np.linalg.matrix_power(L, q)
    for li, l in enumerate(range(3, 10)):
        img[qi, li] = abs(Lq[2, l])
c.imshow(np.log10(img + 1e-18), origin='lower', cmap='magma', vmin=-6, vmax=0, aspect='auto', extent=[2.5, 9.5, -0.5, 8.5])
c.plot(range(3, 10), [l - 2 for l in range(3, 10)], 'w--', lw=1.2)
c.set_xlabel('planted moment $l$'); c.set_ylabel('order $q$ of $L^q$'); c.set_title('ANG3: $|(L^q)_{2,l}|$, zero below $q=l-2$', fontsize=11)
plt.tight_layout(); plt.savefig('../figures/fig08_angular_chain.png', dpi=170)
print('Z_b(1e-4)', 1 / (math.atan(k / 1e-4) / k) - 1e-4, '2k/pi', 2 * k / math.pi)
