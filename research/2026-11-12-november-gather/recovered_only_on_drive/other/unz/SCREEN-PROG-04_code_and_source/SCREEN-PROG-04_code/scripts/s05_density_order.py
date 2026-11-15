# SCRIPT: SCREEN04-S05-DENSITY-ORDER
# Cross-host comparison of the thermal-spike rate, linear vs quadratic in deuteron density, at the averaged track temperature 1080 K.
# Inputs as published: EA (meV) Zr 413, Ti 680, Pd 150; Ue (eV) Zr 340, Ti 25 (370 postulated), Pd 400; Pd/Zr deuteron density 1/37.
import numpy as np
EG = 986e3; kT = 8.617333e-5*1080
mob = lambda EA: np.exp(-EA/1000/kT)
scr = lambda U: np.sqrt(EG/U)*np.exp(-np.sqrt(EG/U))      # (EG/U)^(1/2) exp(-sqrt(EG/U))
m = mob(150)/mob(413); s = scr(400)/scr(340)
print('Pd/Zr mobile-fraction ratio %.2f, screening ratio with prefactor %.1f, product %.0f (relative plateau 1000)' % (m, s, m*s))
print('linear in N:    absolute Pd/Zr plateau %.1f (observed 26.5)' % (m*s/37))
print('quadratic in N: absolute Pd/Zr plateau %.1f (observed 26.5)' % (m*m*s/37**2))
t = mob(680)/mob(413)
print('Ti/Zr with measured 25 eV: %.1e ; with postulated 370 eV: %.2f (observed 0.6)' % (t*scr(25)/scr(340), t*scr(370)/scr(340)))
