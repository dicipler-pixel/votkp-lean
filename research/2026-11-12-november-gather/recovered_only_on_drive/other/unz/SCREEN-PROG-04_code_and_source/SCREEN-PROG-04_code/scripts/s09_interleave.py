# SCRIPT: SCREEN04-S09-INTERLEAVE
# Correlated instrumental drift: residual in U of order r*tau / (d ln ratio / dU). Uninterleaved sequence of 6 h.
import numpy as np
EG = 986e3; U = 340; k = lambda E: 0.5*np.sqrt(EG)*(E+U)**-1.5; s = k(2000)-k(6000)
print(' drift rate   5 min swap   30 min swap   uninterleaved 6 h')
for r in [0.01, 0.03, 0.10]:
    print('  %4.0f%%/h      %5.1f eV     %5.1f eV       %5.0f eV' % (100*r, r*5/60/s, r*30/60/s, r*6/s))
