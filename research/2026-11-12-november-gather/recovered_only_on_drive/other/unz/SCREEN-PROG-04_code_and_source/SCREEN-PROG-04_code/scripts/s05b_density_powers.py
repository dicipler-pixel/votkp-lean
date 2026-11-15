# SCRIPT: s05b_density_powers
# Section 5.3: the cross-host plateau comparison under each density convention, and the two normalizations of
# the same observation. Inputs as stated in the paper (from the Szczecin tables).
import numpy as np
EG = 986e3; kT = 8.617333e-5*1080
fPd, fZr = np.exp(-0.150/kT), np.exp(-0.413/kT)
G = lambda U: np.sqrt(EG/U)*np.exp(-np.sqrt(EG/U))
r_f, r_G = fPd/fZr, G(400)/G(340); P = r_f*r_G; q = 37.0
print('f_Pd/f_Zr %.3f  G(400)/G(340) %.3f  product %.1f' % (r_f, r_G, P))
print('effective f n_D K: %.2f   updated f n_D^2 K (equal eta, W): %.3f   older f^2 n_D^2 K: %.2f' % (P/q, P/q**2, r_f**2*r_G/q**2))
absr = 0.0069/0.00026; normr = 14.6e6/3.9e5
print('absolute plateau ratio %.2f ; fitted normalization ratio %.2f ; normalized plateau ratio %.1f' % (absr, normr, absr*normr))
print('equal-W updated prediction with q = %.2f: %.3f ; W_Pd/W_Zr needed to match %.2f: %.1f' % (normr, P/normr**2, absr, absr/(P/normr**2)))
