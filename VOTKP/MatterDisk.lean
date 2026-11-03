/-
Matter, Then On Down (Jeromie Beasley, draft v3, 3 November 2026).
The algebraic core of the paper, machine-checked.

* The bridge: for an occupation `0 < ν < 1` with odds `z = (1 − ν)/ν`, `(z − 1)/(z + 1) = 1 − 2ν`.
* The census is the gauge without its sign: `ν(1 − ν) = (1 − (1 − 2ν)²)/4`.
* Peel steps add like velocities: with `g z = (z − 1)/(z + 1)`,
  `g z₁ + g z₂ = g (z₁ z₂) · (1 + g z₁ · g z₂)` for `z₁, z₂ > 0`.
* Defect split: the top-left block of `C²` is `A² + B E`, so `A − A² = (A − (C²)₁₁) + B E`.
* Idempotence survives opening: if `C² = C` then `B E = A − A²`, with no Hermiticity assumed.
* The exit line: for `p > 0`, `1 + u²/p = 2 ↔ p = u²`.
* The nucleus: for `S > s > 0` and `z = S/(−s)`, `Γ = (S + s)/(S − s)`, so `Γ − 1 = 2s/(S − s)`;
  the Cayley pole `z = −1` is `S_first + S_next = 0`.
* The ideal gas: two Saha ratios give `n₀ n₂ / n₁² = S₁/S₀` with the electron density cancelled.
* The last peel step at first order: `z = (Z²/2)/(Z²/2 − 5Z/8)` gives `Γ = 5/(8Z − 5)`.
-/
import Mathlib

namespace VOTKP.MatterDisk

/-- The Smith coordinate of a ratio. -/
noncomputable def g (z : ℝ) : ℝ := (z - 1) / (z + 1)

/-- **The bridge.** `Γ = 1 − 2ν` for the odds `z = (1 − ν)/ν`. -/
theorem bridge (ν : ℝ) (h0 : 0 < ν) (h1 : ν < 1) : g ((1 - ν) / ν) = 1 - 2 * ν := by
  have hν : ν ≠ 0 := h0.ne'
  unfold g
  rw [div_sub_one hν, div_add_one hν, div_div_div_cancel_right₀ hν]
  have h2 : (1 - ν + ν) = 1 := by ring
  rw [h2, div_one]
  ring

/-- **The census is the gauge without its sign.** -/
theorem census_square (ν : ℝ) : ν * (1 - ν) = (1 - (1 - 2 * ν) ^ 2) / 4 := by ring

/-- The census of a level and of its complement agree. -/
theorem census_complement (ν : ℝ) : ν * (1 - ν) = (1 - ν) * (1 - (1 - ν)) := by ring

/-- **Peel steps add like velocities**, written without dividing by `1 + g₁ g₂`. -/
theorem rapidities_add (z₁ z₂ : ℝ) (h₁ : 0 < z₁) (h₂ : 0 < z₂) :
    g z₁ + g z₂ = g (z₁ * z₂) * (1 + g z₁ * g z₂) := by
  have a : z₁ + 1 ≠ 0 := by linarith
  have b : z₂ + 1 ≠ 0 := by linarith
  have c : z₁ * z₂ + 1 ≠ 0 := by nlinarith
  unfold g
  field_simp
  ring

/-- **Defect split.** The top-left block of `C²` is `A² + BE`. -/
theorem topleft_sq {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    (A : Matrix m m ℂ) (B : Matrix m n ℂ) (E : Matrix n m ℂ) (D : Matrix n n ℂ) :
    (Matrix.fromBlocks A B E D * Matrix.fromBlocks A B E D).toBlocks₁₁ = A * A + B * E := by
  rw [Matrix.fromBlocks_multiply, Matrix.toBlocks_fromBlocks₁₁]

/-- **Idempotence survives opening.** If `C² = C` then `BE = A − A²`; no Hermiticity is used,
so this holds for the biorthogonal projector of a non-Hermitian band. -/
theorem idempotent_cross {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    (A : Matrix m m ℂ) (B : Matrix m n ℂ) (E : Matrix n m ℂ) (D : Matrix n n ℂ)
    (hC : Matrix.fromBlocks A B E D * Matrix.fromBlocks A B E D = Matrix.fromBlocks A B E D) :
    B * E = A - A * A := by
  have h := congrArg Matrix.toBlocks₁₁ hC
  rw [topleft_sq, Matrix.toBlocks_fromBlocks₁₁] at h
  rw [← h]
  abel

/-- **The exit line.** With `⟨K⟩ = 1 + u²/p` and `p = E(0)E(π) > 0`, `⟨K⟩ = 2 ↔ p = u²`. -/
theorem exit_line (u p : ℝ) (hp : 0 < p) : 1 + u ^ 2 / p = 2 ↔ p = u ^ 2 := by
  have hp' : p ≠ 0 := hp.ne'
  constructor
  · intro h
    have : u ^ 2 / p = 1 := by linarith
    rw [div_eq_one_iff_eq hp'] at this
    exact this.symm
  · intro h
    rw [h, div_self (by rw [← h]; exact hp')]
    norm_num

/-- **The nucleus outside the rim.** For a negative first separation energy `−s` and a positive
next one `S > s`, `Γ = (S + s)/(S − s)`. -/
theorem outside_rim (S s : ℝ) (hs : 0 < s) (hS : s < S) :
    g (S / (-s)) = (S + s) / (S - s) := by
  have h1 : (-s) ≠ 0 := by linarith
  have h2 : S - s ≠ 0 := by linarith
  have h3 : S / (-s) + 1 ≠ 0 := by
    rw [div_add_one h1]
    exact div_ne_zero (by linarith) h1
  unfold g
  rw [div_sub_one h1, div_add_one h1, div_div_div_cancel_right₀ h1]
  rw [div_eq_div_iff (by linarith) h2]
  ring

/-- **The rim distance, exactly.** `Γ − 1 = 2s/(S − s)`. -/
theorem rim_distance (S s : ℝ) (hs : 0 < s) (hS : s < S) :
    g (S / (-s)) - 1 = 2 * s / (S - s) := by
  have h2 : S - s ≠ 0 := by linarith
  rw [outside_rim S s hs hS, div_sub_one h2]
  ring_nf

/-- **The Cayley pole.** For `S₁ ≠ 0`, the ratio `S₂/S₁` is `−1` exactly when `S₁ + S₂ = 0`. -/
theorem cayley_pole (S₁ S₂ : ℝ) (h : S₁ ≠ 0) : S₂ / S₁ = -1 ↔ S₁ + S₂ = 0 := by
  rw [div_eq_iff h]
  constructor <;> intro hh <;> linarith

/-- **The ideal gas.** Two Saha ratios share the electron density, which cancels. -/
theorem saha_ratio (n₀ n₁ n₂ x S₀ S₁ : ℝ) (h₀ : n₀ ≠ 0) (h₁ : n₁ ≠ 0) (hx : x ≠ 0)
    (hS : S₀ ≠ 0) (e₀ : n₁ / n₀ = S₀ / x) (e₁ : n₂ / n₁ = S₁ / x) :
    n₀ * n₂ / n₁ ^ 2 = S₁ / S₀ := by
  have a : n₁ = S₀ / x * n₀ := by rw [← e₀]; field_simp
  have b : n₂ = S₁ / x * n₁ := by rw [← e₁]; field_simp
  rw [b, a]
  field_simp
  ring

/-- **The last peel step at first order.** With `I_H = Z²/2` and `I_He = Z²/2 − 5Z/8`
(Hartree), the ratio `z = I_H / I_He` has `Γ = 5/(8Z − 5)`. -/
theorem last_step (Z : ℝ) (hZ : 2 ≤ Z) :
    g ((Z ^ 2 / 2) / (Z ^ 2 / 2 - 5 * Z / 8)) = 5 / (8 * Z - 5) := by
  have h1 : Z ^ 2 / 2 - 5 * Z / 8 ≠ 0 := by nlinarith
  have h2 : 8 * Z - 5 ≠ 0 := by linarith
  have h3 : (Z ^ 2 / 2) / (Z ^ 2 / 2 - 5 * Z / 8) + 1 ≠ 0 := by
    have : 0 < (Z ^ 2 / 2) / (Z ^ 2 / 2 - 5 * Z / 8) := by
      apply div_pos <;> nlinarith
    linarith
  unfold g
  rw [div_eq_div_iff h3 h2]
  field_simp
  ring

end VOTKP.MatterDisk
