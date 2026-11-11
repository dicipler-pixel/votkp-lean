# Snell, the Smith chart and the two trees, read on the Yang–Mills gap

Jeromie Beasley · 11 November 2026 · working record

Read in full for this note:
- Two Trees in One Ball v4, the exposition §1–9 (Appendix A Lean source and Appendix B outputs were not read line by line).
- The One Tree, One Ball mixer: both scenes' text and the app code.
- Atlas cards B30, B39, B175, B189.
- Script: SNELL-SMITH-TREES-04.

## 1. What Snell leaves in between is the gap (exact, standard)
- Past the critical angle, Snell asks for sin² > 1. The normal momentum turns imaginary and the wave decays into the layer, e^{−|p⊥|w} (B39).
- A gapped theory does the same at every energy below the gap: k² = E² − m² < 0, so the field decays as e^{−√(m² − E²) x}.
- The mass gap is the width of that evanescent band, between the vacuum and the first excitation. In the transfer direction, correlations fall by the ratio z = t₀/t₁ = e^{ma} per slice (TransferGap.lean).

## 2. The Smith chart reads the transfer trace (exact)
- One transfer step with trace tr = 2 cosh κ has Smith coordinate Γ = tanh(κ/2). So

  Γ² = (|tr| − 2) / (|tr| + 2).

- Γ² > 0 (inside the disk): the step is evanescent, a boost. This is total internal reflection.
- Γ² ≤ 0: the step propagates, a rotation.
- The gap question becomes: is Γ² of the transfer step bounded away from 0?
- Checked on the strip (SNELL-SMITH-TREES-04): μ = 0 gives Γ² = 1/3, μ = 1 gives 1/5, μ = 1.5 gives 1/9. The band [2, 6] is propagating.
- The Schottky line of Two Trees (Γ² = 1/2) is |tr| = 6, i.e. κ = 2 ln(1 + √2).

## 3. In the small field
- **The 1×n strip:** the transfer trace is 4 − μ, so the band is [2, 6]. Below μ = 2 there is an evanescent region, which is why a strip keeps a floor at every length.
- **The 2D torus:** the band reaches μ = 0, so nothing is left in between. Perturbatively the bulk has no evanescent band, and confinement has to open one.

## 4. The knot's tree is the gauge constraint (structural, with an exact piece)
- Garrett's tree never closes: a free group, where no word returns (Two Trees Thm 5.1).
- A knot's tree closes: a relation, a loop of boosts summing to zero.
- Gauss's law does the same to lattice states: every gauge-invariant electric support is closed (no dangling link; the room's SmallSupportsAreCycles).
- The exact piece: at strong coupling the lowest excitation is the cheapest closed word. Its energy is (4/3) × girth = 16/3 on all five graphs (checked), because every nontrivial support contains a cycle and each nontrivial link costs at least 4/3.
- Two Trees §7, "a knot is what a tree of boosts looks like when its steps are tied back on themselves", reads here as: a glueball is the shortest relator.

## 5. The plaquette is a commutator of perpendicular steps (exact identity, reading for SU(3))
- In Two Trees, two perpendicular boosts compose to a boost followed by a turn, with tan(θ/2) = Γ² (Thm 4.7).
- So a square of boosts has holonomy 1 − cos θ = 2Γ⁴/(1 + Γ⁴). That is fourth order in the step.
- The lattice plaquette is the same kind of object: a commutator of perpendicular link transports. The magnetic term measures its turn.
- Whether this boost-plaquette picture says anything about SU(3) links (which are rotations, not boosts) is untested.

## 6. Where the continuum limit sits in the ball
- The continuum limit sends ma → 0, so Γ → 0: deep below the Schottky line. That is the regime Two Trees §5.3 proves "free but not discrete, distances not kept in proportion".
- Turned words do not accumulate distance there: the commutator word stays within 3.5255 for every n.
- Reading, not result: at weak coupling, decay along turned paths need not add up. That is the same warning as the small-field 1/L closing.
