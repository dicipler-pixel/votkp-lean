# SCRIPT: LIGHT-MATTER-01
# Fresh check of the numbers in "Light writes into matter". KILL: any value off the printed one in its last digit.
import numpy as np
h, c = 6.62607015e-34, 2.99792458e8
lam = 532e-9; nf, ns = 1.38, 1.52
r01 = (1 - nf) / (1 + nf); r12 = (nf - ns) / (nf + ns)
for d in [0.0, 100e-9]:
    delta = 2 * np.pi * nf * d / lam
    r = (r01 + r12 * np.exp(2j * delta)) / (1 + r01 * r12 * np.exp(2j * delta))
    print('film %3.0f nm: reflectance %.5f' % (d * 1e9, abs(r)**2))
E = h * c / lam; print('photon energy at 532 nm: %.4e J, frequency %.4e Hz' % (E, c / lam))
for P in [1e-12, 1e-15]: print('power %.0e W: %.4e photons/s' % (P, P / E))
