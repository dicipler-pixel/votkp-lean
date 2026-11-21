# Advance prediction: francium's radon-core opening (registered 21 November 2026)

Jeromie Beasley

**The test.** The first opening of each noble-gas core by an alkali atom is the step z = IE₂/IE₁. Every one measured so far lies outside the loop wall, and the sequence falls towards it:
lithium 14.0289, sodium 9.2013, potassium 7.2858, rubidium 6.5331, caesium 5.9471 (archive data/element_thresholds_20261011.json.gz).

**Francium is next.** Its first ionisation energy is measured, IE₁ = 4.072741 eV (NIST, ABDJ90). Its second ionisation energy has not been measured: NIST lists no Fr II energy levels.

**Prediction.** The wall Γ² = ½ (z = 3 + 2√2) puts francium's radon-core opening inside the wall exactly when

  IE₂(Fr) < 4.072741 × (3 + 2√2) = 23.738 eV.

If the measured IE₂ lies below 23.738 eV, francium is the first alkali whose core opening is inside the wall. If it lies above, the alkali column stays outside.

**What it can and cannot decide.** The archive already pins any cutoff that reproduces every classification from hydrogen to astatine to the window [5.80790, 5.86654), between silver's anion rung and silicon's (certified in lean/LoopWall.lean as window_silver_silicon). For francium that window is IE₂ ∈ [23.654, 23.893) eV. Only a value inside that 0.24 eV band separates the wall from the other cutoffs the data allow; any other value tests the column pattern, not the exact number.

Status: registered before any measurement of IE₂(Fr) was consulted beyond the statement that none exists in NIST's tables.
