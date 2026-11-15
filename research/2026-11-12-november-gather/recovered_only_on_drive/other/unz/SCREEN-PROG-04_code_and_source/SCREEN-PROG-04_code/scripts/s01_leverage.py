# SCRIPT: SCREEN04-S01-LEVERAGE
# Screening leverage: rate ratio exp(sqrt(EG/100) - sqrt(EG/U)) at the zero-energy end, and the prefactor (EG/U)^(1/2).
import numpy as np
EG = 986e3   # eV, Gamow energy for d+d: 2 mu c^2 (pi alpha)^2
mu = 1875.613e6/2; alpha = 1/137.035999
print('EG from constants: %.1f keV' % (2*mu*(np.pi*alpha)**2/1e3))
print(' U (eV)  sqrt(EG/U)  log10 rate ratio vs 100 eV')
for U in [100, 200, 340, 400]:
    print('  %4d     %6.2f       %5.1f' % (U, np.sqrt(EG/U), (np.sqrt(EG/100)-np.sqrt(EG/U))/np.log(10)))
print('prefactor (EG/U)^(1/2) ratio 100 -> 400 eV: %.2f' % np.sqrt(400/100))
