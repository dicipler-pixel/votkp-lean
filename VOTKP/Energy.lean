/-
VOTKP energy ledger (Jeromie Beasley, 11 October 2026).
Exact finite-ladder identities, conditional on a supplied threshold function.
These theorems do not assert atomic spectra, transition rates or a binding force.
Developed with AI assistance.
-/
import Mathlib

namespace VOTKP.Energy

/-- Removal energy accumulated through the first q thresholds. -/
noncomputable def removed (I : ℕ → ℝ) (q : ℕ) : ℝ :=
  ∑ j ∈ Finset.range q, I j

/-- Complete neutral-to-bare electronic binding ledger. -/
noncomputable def total (I : ℕ → ℝ) (Z : ℕ) : ℝ := removed I Z

/-- Binding left after q removals. Physical interpretation uses q ≤ Z. -/
noncomputable def binding (I : ℕ → ℝ) (Z q : ℕ) : ℝ :=
  total I Z - removed I q

/-- Ground energy relative to the bare nucleus and free electrons. -/
noncomputable def ground (I : ℕ → ℝ) (Z q : ℕ) : ℝ := -binding I Z q

theorem removed_zero (I : ℕ → ℝ) : removed I 0 = 0 := by
  simp [removed]

theorem removed_succ (I : ℕ → ℝ) (q : ℕ) :
    removed I (q + 1) = removed I q + I q := by
  simp [removed, Finset.sum_range_succ]

theorem binding_neutral (I : ℕ → ℝ) (Z : ℕ) :
    binding I Z 0 = total I Z := by
  simp [binding, removed_zero]

theorem binding_bare (I : ℕ → ℝ) (Z : ℕ) : binding I Z Z = 0 := by
  simp [binding, total]

theorem ground_bare (I : ℕ → ℝ) (Z : ℕ) : ground I Z Z = 0 := by
  simp [ground, binding_bare]

theorem ledger_decomposition (I : ℕ → ℝ) (Z q : ℕ) :
    removed I q + binding I Z q = total I Z := by
  unfold binding
  ring

theorem binding_succ (I : ℕ → ℝ) (Z q : ℕ) :
    binding I Z q = I q + binding I Z (q + 1) := by
  simp only [binding, removed_succ]
  ring

theorem ground_step (I : ℕ → ℝ) (Z q : ℕ) :
    ground I Z (q + 1) - ground I Z q = I q := by
  simp only [ground, binding, removed_succ]
  ring

theorem ground_reference (I : ℕ → ℝ) (Z q : ℕ) :
    ground I Z q = removed I q - total I Z := by
  unfold ground binding
  ring

/-- Any finite sequence of state-energy differences telescopes. -/
theorem energy_telescope (E : ℕ → ℝ) (n : ℕ) :
    (∑ j ∈ Finset.range n, (E (j + 1) - E j)) = E n - E 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    ring

theorem removed_monotone (I : ℕ → ℝ) (hI : ∀ j, 0 ≤ I j) :
    Monotone (removed I) := by
  apply monotone_nat_of_le_succ
  intro q
  rw [removed_succ]
  linarith [hI q]

theorem binding_nonnegative (I : ℕ → ℝ) (hI : ∀ j, 0 ≤ I j)
    (Z q : ℕ) (hq : q ≤ Z) : 0 ≤ binding I Z q := by
  unfold binding total
  exact sub_nonneg.mpr (removed_monotone I hI hq)

/-- Changing the origin of energy leaves every state-energy gap unchanged. -/
theorem energy_origin_invariance (a b c : ℝ) :
    (b + c) - (a + c) = b - a := by ring

/-- The full peel record reconstructs a next threshold from its anchor. -/
theorem peel_anchor_reconstruction (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    a * (1 + (b - a) / (b + a)) / (1 - (b - a) / (b + a)) = b := by
  have hab : b + a ≠ 0 := by linarith
  have hden : 1 - (b - a) / (b + a) ≠ 0 := by
    intro h
    have heq : (b - a) / (b + a) = 1 := by linarith
    have hba : b - a = b + a := (div_eq_one_iff_eq hab).mp heq
    linarith
  field_simp [ha.ne', hab, hden]
  <;> ring

/-- A common positive rescaling preserves the peel but rescales binding. -/
theorem binding_scale (I : ℕ → ℝ) (l : ℝ) (Z q : ℕ) :
    binding (fun j => l * I j) Z q = l * binding I Z q := by
  simp only [binding, total, removed, ← Finset.mul_sum]
  ring

noncomputable def toyA (j : ℕ) : ℝ := if j = 0 then 1 else if j = 1 then 2 else 6
noncomputable def toyB (j : ℕ) : ℝ := if j = 0 then 1 else if j = 1 then 3 else 6

/-- The same first threshold does not determine complete binding. -/
theorem first_threshold_not_total :
    toyA 0 = toyB 0 ∧ total toyA 3 = 9 ∧ total toyB 3 = 10 := by
  norm_num [toyA, toyB, total, removed, Finset.sum_range_succ]

/-- A gap without a coupling weight does not determine a weighted readout. -/
theorem same_gap_different_weights :
    (1 : ℝ) / 2 ≠ 3 / 2 := by norm_num

/-- Peel coordinate of one positive step, `Γ_j = (I_{j+1} − I_j)/(I_{j+1} + I_j)`. -/
noncomputable def gammaStep (I : ℕ → ℝ) (j : ℕ) : ℝ :=
  (I (j + 1) - I j) / (I (j + 1) + I j)

/-- **§20.3.2.** Each later threshold is the anchor times the product of peel factors. -/
theorem anchored_product (I : ℕ → ℝ) (q : ℕ) (hI : ∀ j ≤ q, 0 < I j) :
    I q = I 0 * ∏ j ∈ Finset.range q, (1 + gammaStep I j) / (1 - gammaStep I j) := by
  induction q with
  | zero => simp
  | succ q ih =>
    have hIq : ∀ j ≤ q, 0 < I j := fun j hj => hI j (Nat.le_succ_of_le hj)
    have hstep := peel_anchor_reconstruction (I q) (I (q + 1))
      (hI q (Nat.le_succ q)) (hI (q + 1) (Nat.le_refl _))
    rw [Finset.prod_range_succ, ← mul_assoc, ← ih hIq]
    simpa [gammaStep, mul_div_assoc'] using hstep.symm

/-- **§20.3.2.** For `Z ≥ 1` and `I_0, …, I_{Z-1} > 0`,
`B_el = ∑_{q<Z} I_q = I_0 [1 + ∑_{q=1}^{Z-1} ∏_{j<q} (1+Γ_j)/(1−Γ_j)]`. -/
theorem binding_from_gammas (I : ℕ → ℝ) (Z : ℕ) (hZ : 0 < Z) (hI : ∀ j < Z, 0 < I j) :
    ∑ q ∈ Finset.range Z, I q =
      I 0 * (1 + ∑ q ∈ Finset.Ico 1 Z,
        ∏ j ∈ Finset.range q, (1 + gammaStep I j) / (1 - gammaStep I j)) := by
  have hterm : ∀ q ∈ Finset.range Z,
      I q = I 0 * ∏ j ∈ Finset.range q, (1 + gammaStep I j) / (1 - gammaStep I j) := by
    intro q hq
    exact anchored_product I q fun j hj => hI j (lt_of_le_of_lt hj (Finset.mem_range.mp hq))
  rw [Finset.sum_congr rfl hterm, ← Finset.mul_sum]
  have hsplit : Finset.range Z = insert 0 (Finset.Ico 1 Z) := by
    ext q
    simp only [Finset.mem_range, Finset.mem_insert, Finset.mem_Ico]
    omega
  have h0 : 0 ∉ Finset.Ico 1 Z := by simp
  rw [hsplit, Finset.sum_insert h0, Finset.prod_range_zero]

end VOTKP.Energy
