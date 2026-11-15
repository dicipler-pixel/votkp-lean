# SCRIPT: SCREEN04-S03-SIGNATURES
# DD heat-to-neutron conversion (mean 3.65 MeV per reaction, half the reactions give a neutron) and the 23.85 MeV pair channel.
eV = 1.602176634e-19
for P in [0.1, 1, 10]:
    r = P/(3.65e6*eV); n = r/2; print('%5.1f W: %.2e reactions/s, %.2e neutrons/s, deficit vs 4e4/s = 10^%.1f' % (P, r, n, __import__('math').log10(n/4e4)))
for P in [0.1, 1, 10]:
    print('%5.1f W through 23.85 MeV: %.2e pair creations/s' % (P, P/(23.85e6*eV)))
