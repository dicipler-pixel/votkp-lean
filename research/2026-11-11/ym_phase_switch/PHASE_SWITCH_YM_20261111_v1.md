# The phase switch on Yang–Mills: what it shows, computed

Jeromie Beasley · 11 November 2026 · working record (scripts in this folder)

H = Σ_e C₂(e) + λ Σ_p (3 − Re tr U_p), with α = 1, on the room's graphs. Every number below comes from a script in this folder. Grades: "computed" means a float or grid check whose kill line was written first; "standard" means textbook physics.

## 1. Electric cutoffs lose the vacuum at weak coupling (computed: ONE-PLAQUETTE-PHASE-01)

One plaquette, character basis, with the same operator as the repo's `su3_character_certificate`. Converged to ≤ 3e-11 in the cutoff.

| λ | gap | gap / 2√λ | vacuum weight above C₂ = 8 | above C₂ = 40/3 | ⟨C₂⟩ / E₀ |
|---:|---:|---:|---:|---:|---:|
| 4 | 3.281 | 0.820 | 0.014 | 0.0001 | 0.387 |
| 16 | 7.336 | 0.917 | 0.312 | 0.051 | 0.450 |
| 64 | 15.357 | 0.960 | 0.797 | 0.483 | 0.477 |
| 256 | 31.366 | 0.980 | 0.971 | 0.884 | 0.489 |

What the table shows:
- The gap goes to the oscillator value 2√λ from below.
- The electric share of the vacuum climbs to ½ from below, the same below-half share as the classical swing.
- The vacuum leaves any fixed electric cutoff. This is why the window wall closes: a retained space chosen by electric energy cannot hold the weak-coupling vacuum.

## 2. The phase floor (computed: LARGE-FIELD-FLOOR-02)

Outside the small-field ball (some eigenphase |θ| ≥ δ):

3 − Re χ(U) ≥ m(δ) = (1 − cos δ) + 2(1 − cos δ/2) ≈ ¾ δ² for small δ.

- The minimum is attained at (δ, −δ/2, −δ/2).
- It held to rounding on a 2001² grid for δ from 0.05π to π.
- At δ = π, m = 4: this is the B128 winding floor, the far end of the same formula.
- With δ = k λ^(−1/4), the large-field cost λ m(δ) ≈ ¾ k² √λ grows at the same rate as the vacuum energy, with a free constant k. This is the small-field / large-field split, and the IMS localization formula is its operator form.

## 3. In the small field, the gap belongs to the box (computed: SMALL-FIELD-GAP-03)

Near U = 1 each colour decouples into oscillators: ω = √(λμ), with μ a nonzero eigenvalue of BᵀB (B the plaquette–link curl). A colour singlet needs two quanta, so the small-field gap is 2√(λ μ_min).
- Normalization check: one plaquette gives μ = 4, which matches the repo operator.

| graph | μ_min | small-field gap / √λ |
|---|---:|---:|
| two squares | 3 | 3.464 |
| strip | 2.586 | 3.216 |
| corner | 2 | 2.828 |
| cube | 4 | 4.000 |
| double cube | 3 | 3.464 |

- **Open 1×n strips:** μ_min falls to 2 as n grows (2.008 at n = 34). A one-wide strip keeps a floor at every length.
- **Periodic L×L tori:** μ_min = 4 sin²(π/L) exactly (3, 2, 1, 0.586, 0.268, 0.152 for L = 3 to 16), so the small-field gap closes like 1/L. These are the massless gluons of perturbation theory (standard).

## What this says about the programme
- **Prediction for the room (untested against their certificates):** at large λ the true gap on each fixed graph approaches 2√(λ μ_min) with the μ_min above. This is the finite-box Gaussian gap, not the mass gap.
- **The five graphs are thin.** The one-wide strip has a floor 2√(2λ) at every length, which a two- or three-dimensional bulk does not. A method that looks uniform on strips can be seeing the thinness.
- **The mass gap at weak coupling is non-Gaussian.** It is a large-field / confinement effect that only shows once the box is larger than the correlation length, and with asymptotic freedom the box must grow like e^{c/g²} in lattice units (standard). Any certificate route must reach that regime, through a renormalization step, before its gap can be the mass gap. On the atlas this is B160: one scale has to come from outside the projector geometry.
- **Strong coupling:** a volume-uniform gap is already proved (Osterwalder–Seiler for the Euclidean lattice; Yarotsky, Commun. Math. Phys. 2005, for relatively bounded perturbations of classical lattice systems). The room's proved floors (no dangling links, at least 4/3 per nontrivial link) are its hypotheses. A Lean statement of it would be new as a formalization, not as mathematics.
