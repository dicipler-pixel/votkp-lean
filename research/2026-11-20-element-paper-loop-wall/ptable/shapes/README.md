# Elements on different shapes (PT-SHAPES-01, -02) - Jeromie Beasley, 23 Nov 2026, AI-assisted

Every element so far was read on one circle (the Smith disk). Here the same books (first 8 ionization steps
z_k = IE_{k+1}/IE_k from ptable_v2_data.json) are read on: circle/ball (now), diamond (per-step peel), cube's own
reading, simplex (ladder shape only), and a no-shape control (raw energies). Score: share of elements whose nearest
element sits in the same column (chance about 0.05).

- Any peel shape reads the table: about 0.60-0.67 vs 0.09 for raw energies. No shape beats the circle beyond its bootstrap spread.
- Simplex (ladder shape only) is highest (0.667) but not clearly above the circle.
- Old short-form (8-group) reading: raw gains, but after correcting for chance the gain is small: cube and simplex about +0.04
  from genuine A/B pairs (Al-Ac, Si-Zr), the circle about none. Merged triads (Rh-Pd, Ir-Pt) inflate the raw number.
Shapes and tests come from research/poincare-diamond on claude/moving-matrix-of-balls.
