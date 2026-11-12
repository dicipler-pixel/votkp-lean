# SCRIPT: SCREEN04-S02-THERMAL
# Thermal mobilisation N/N0 = exp(-EA/kT) for ZrD2, EA = 413 meV.
import numpy as np
k = 8.617333e-5; EA = 0.413
print(' T (K)  kT (meV)   N/N0        (N/N0)^2')
for T in [300, 980, 1080, 2540]:
    r = np.exp(-EA/(k*T)); print('  %4d   %5.1f    %.2e    %.2e' % (T, 1e3*k*T, r, r*r))
g = np.exp(-EA/(k*1080))/np.exp(-EA/(k*300))
print('gain 300 -> 1080 K: through N %.2e, through N^2 %.2e' % (g, g*g))
