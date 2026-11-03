# Gaussian information-bound implementation checks

Written before execution on 3 November 2026, after the analytic B13 proof was
independently reviewed. Test 64 seeded complex 12-mode covariance matrices,
split 5/7, with spectra in [delta,1-delta] at delta=0.05,0.15,0.25,0.45.
Verify `4 Tr X <= I_G <= Tr X/[delta(1-delta)]` with tolerance `2e-12` and the
derived census bound at epsilon0.1. Check the sharp lower coefficient using
the 2-mode family C=0.5 I+r sigma_x at r=0.01,0.001,0.0001.
Record a pure-state family with p=0.01,0.0001,0.000001 illustrating the absence
of a uniform upper constant. All information is in natural-log units.

Seed 2026110313. These are finite implementation checks, not substitutes for
the universal analytic proof and not laboratory data.
