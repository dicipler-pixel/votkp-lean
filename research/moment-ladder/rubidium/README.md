# Rubidium: both halves of the tensor against a measured tune-out

Jeromie Beasley. 24 November 2026. A computation calibrated against other people's published measurements.

Model: rubidium-87 ground state (the F = m = 2 stretched state) and its two strong lines, from published line
frequencies and dipole elements. Plain (even) and handed (odd) parts of the response from the same matrix elements.

- Plain tune-out, two lines only: 790.0280 nm (measured 790.03235 nm).
- One background constant set on that measurement: 10.940 atomic units (measured ionic core: 9.116).
  Steady polarizability then comes out 319.06 atomic units.
- Handed tune-out for the experiment's light (circular fraction 0.9931): predicted 785.1535 nm,
  measured 785.1522(3) nm, miss +0.0013 nm on a move of 4.88 nm. Kill line was 0.01 nm. Passed.
  The experiment's own full calculation gives 785.1538(9) nm.
- Opposite handedness: no zero between the lines.
- Tensor on rung -3, two-line model: metric 2655.03, curvature -73.68 atomic units, ratio -0.0278.
  With the two lines unsplit and strength ratio exactly 2 the curvature is 0.0000.
- Low frequency: handed part = frequency times curvature (ratio -1.000006 at 1e-4 hartree).
  At the tune-out the handed part is 2881 times that: near the lines the higher odd rungs carry it.

RUBIDIUM-HANDED-01 had a unit constant off by 1000 and did not finish; it is not a result.
Source of the measurement: Phys. Rev. A 105, L030802 (2022).
