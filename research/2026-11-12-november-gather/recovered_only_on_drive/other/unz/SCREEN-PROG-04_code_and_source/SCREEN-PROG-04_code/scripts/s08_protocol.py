# SCRIPT: SCREEN04-S08-PROTOCOL
# Sensitivities, the error budget, the performance ladder and discrimination for the two-energy interleaved ratio.
import numpy as np
EG = 986e3; U = 340
k = lambda E: 0.5*np.sqrt(EG)*(E+U)**-1.5
print('d lnR/dU at 3 keV: %.3e /eV' % k(3000))
print('d ln[Y(2)/Y(6)]/dU: %.3e /eV ; noise penalty factor vs single energy: %.2f' % (k(2000)-k(6000), np.sqrt(2)*k(3000)/(k(2000)-k(6000))))
print('10%% change in N0 equals %.0f eV at 3 keV' % (np.log(1.1)/k(3000)))
terms = {'counting E1': 0.020, 'counting E2': 0.005, 'gain drift': 0.004, 'dead time': 0.002, 'beam spot': 0.006, 'background': 0.005, 'stopping power': 0.010}
tot = np.sqrt(sum(v*v for v in terms.values())); s = k(2000)-k(6000)
print('budget quadrature total %.4f -> sigma(U) per step %.2f eV, over six steps %.2f eV' % (tot, tot/s, tot/s/np.sqrt(6)))
print('ladder (step-to-step precision p, both energies at p): ' + ', '.join('%g%% -> %.1f eV' % (100*p, np.sqrt(2)*p/s) for p in [0.01, 0.02, 0.03, 0.05, 0.10]))
sg = tot/s
print('discrimination at the budget: 100 -> 340 span %.1f sigma; 300 -> 400 drift %.1f sigma; at 10%% precision the span is %.1f sigma' % (240/sg, 100/sg, 240/(np.sqrt(2)*0.10/s)))
print('six-step rise of 300 eV, slope fitted over 6 steps: sd of rise %.1f eV -> %.0f sigma against a flat (dose-independent) prediction' % (5*sg/np.sqrt(17.5), 300/(5*sg/np.sqrt(17.5))))
