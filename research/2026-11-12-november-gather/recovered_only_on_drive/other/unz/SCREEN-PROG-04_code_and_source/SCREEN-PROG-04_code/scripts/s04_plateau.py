# SCRIPT: SCREEN04-S04-PLATEAU
# Could screening drift alone flatten the low-energy yield? U needed at each E for the penetration factor to equal its 1250 eV value at U = 340 eV.
import numpy as np
EG = 986e3; P = lambda E, U: np.exp(-np.sqrt(EG/(E+U)))
ref = P(1250, 340)
print(' Ecm (eV)  yield ratio at U=340   U for a flat yield (eV)')
for E in [1250, 1000, 800, 625, 500]:
    print('  %5d       %.2e              %5.0f' % (E, P(E,340)/ref, EG/np.log(ref)**2 - E))
