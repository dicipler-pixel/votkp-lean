/-
  NewProps.lean — Elemental Peeling v3.2, Propositions 22.1, 22.2, 22.3, 24.1, 25.1, 25.2.
  Jeromie Beasley. Lean 4.34.1, Mathlib v4.34.1 (narrow imports), no sorry, no axioms.
-/
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.Data.Matrix.Block
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.Analysis.Real.Sqrt
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.LinearCombination

set_option linter.unusedSectionVars false
set_option linter.unusedSimpArgs false
set_option linter.unnecessarySeqFocus false

namespace NewProps

open Matrix

/-! ## 22.1  A peel is a projector move -/

/-- Squared Frobenius norm of a complex matrix. -/
noncomputable def frob2 {m n : Type*} [Fintype m] [Fintype n] (M : Matrix m n ℂ) : ℝ :=
  ∑ i, ∑ j, Complex.normSq (M i j)

section peel
variable {p q : Type*} [Fintype p] [Fintype q] [DecidableEq p] [DecidableEq q]

theorem frob2_conjTranspose (B : Matrix p q ℂ) : frob2 Bᴴ = frob2 B := by
  unfold frob2
  rw [Finset.sum_comm]
  simp [Matrix.conjTranspose_apply]

theorem frob2_fromBlocks (A : Matrix p p ℂ) (B : Matrix p q ℂ) (C : Matrix q p ℂ)
    (D : Matrix q q ℂ) :
    frob2 (fromBlocks A B C D) = frob2 A + frob2 B + frob2 C + frob2 D := by
  unfold frob2
  simp only [Fintype.sum_sum_type, fromBlocks_apply₁₁, fromBlocks_apply₁₂,
    fromBlocks_apply₂₁, fromBlocks_apply₂₂, Finset.sum_add_distrib]
  ring

/-- The projector onto the retained block. -/
def Pr (p q : Type*) [Fintype p] [Fintype q] [DecidableEq p] [DecidableEq q] :
    Matrix (p ⊕ q) (p ⊕ q) ℂ := fromBlocks 1 0 0 0

theorem one_sub_Pr : (1 : Matrix (p ⊕ q) (p ⊕ q) ℂ) - Pr p q = fromBlocks 0 0 0 1 := by
  ext i j
  rcases i with i | i <;> rcases j with j | j <;>
    simp [Pr, Matrix.one_apply, Matrix.sub_apply]

/-- Proposition 22.1, first reading: the weight of `P H (1 - P)` is the weight of `B`. -/
theorem prop22_1_weight (A : Matrix p p ℂ) (B : Matrix p q ℂ) (D : Matrix q q ℂ) :
    frob2 (Pr p q * fromBlocks A B Bᴴ D * (1 - Pr p q)) = frob2 B := by
  have : Pr p q * fromBlocks A B Bᴴ D * (1 - Pr p q) = fromBlocks 0 B 0 0 := by
    rw [one_sub_Pr]
    unfold Pr
    simp [fromBlocks_multiply]
  rw [this, frob2_fromBlocks]
  simp [frob2]

/-- Proposition 22.1, second reading: half the squared weight of `[H, P]` is the weight of `B`. -/
theorem prop22_1_commutator (A : Matrix p p ℂ) (B : Matrix p q ℂ) (D : Matrix q q ℂ) :
    (1 / 2 : ℝ) * frob2 (fromBlocks A B Bᴴ D * Pr p q - Pr p q * fromBlocks A B Bᴴ D)
      = frob2 B := by
  have : fromBlocks A B Bᴴ D * Pr p q - Pr p q * fromBlocks A B Bᴴ D
      = fromBlocks 0 (-B) Bᴴ 0 := by
    unfold Pr
    simp [fromBlocks_multiply]
    ext i j
    rcases i with i | i <;> rcases j with j | j <;> simp [fromBlocks]
  rw [this, frob2_fromBlocks, frob2_conjTranspose]
  have hn : frob2 (-B) = frob2 B := by simp [frob2]
  have h0 : frob2 (0 : Matrix p p ℂ) = 0 := by simp [frob2]
  have h0' : frob2 (0 : Matrix q q ℂ) = 0 := by simp [frob2]
  rw [h0, h0', hn]
  ring

/-- Proposition 22.1, third reading at lag zero: `Re Tr K(0) = Re Tr (B B†)` is the weight of `B`. -/
theorem prop22_1_trace (B : Matrix p q ℂ) :
    (∑ i, (B * Bᴴ) i i).re = frob2 B := by
  unfold frob2
  simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Complex.re_sum, Complex.mul_conj,
    Complex.normSq_eq_conj_mul_self]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
  rw [Complex.normSq_apply]

end peel

/-! ## 22.2  The peel step is an edge of two books -/

/-- Peel coordinate `(z - 1)/(z + 1)`. -/
noncomputable def peel (z : ℝ) : ℝ := (z - 1) / (z + 1)

/-- Einstein addition. -/
noncomputable def oplus (u v : ℝ) : ℝ := (u + v) / (1 + u * v)

section edge
variable (di dj : ℝ)

/-- The two books of an edge. -/
def Em : ℝ := (di - dj) ^ 2
def Ep : ℝ := (di + dj) ^ 2

theorem budget : Em di dj + Ep di dj = 2 * (di ^ 2 + dj ^ 2) := by unfold Em Ep; ring

theorem difference : Ep di dj - Em di dj = 4 * di * dj := by unfold Em Ep; ring

variable {di dj}

/-- Proposition 22.2: the four edge coefficients are the peel coordinate of `z = di/dj`. -/
theorem prop22_2 (hi : 0 < di) (hj : 0 < dj) :
    (di - dj) / (di + dj) = peel (di / dj) ∧
    Em di dj / Ep di dj = (peel (di / dj)) ^ 2 ∧
    Em di dj / (Em di dj + Ep di dj) = (peel (di / dj)) ^ 2 / (1 + (peel (di / dj)) ^ 2) ∧
    (Ep di dj - Em di dj) / Ep di dj = 1 - (peel (di / dj)) ^ 2 := by
  have h1 : di + dj ≠ 0 := by positivity
  have h2 : dj ≠ 0 := hj.ne'
  have h3 : di / dj + 1 ≠ 0 := by positivity
  have h4 : (di - dj) ^ 2 + (di + dj) ^ 2 ≠ 0 := by positivity
  have hp : peel (di / dj) = (di - dj) / (di + dj) := by
    unfold peel; field_simp
  refine ⟨hp.symm, ?_, ?_, ?_⟩ <;> rw [hp] <;> unfold Em Ep <;> field_simp <;> ring

end edge

/-- The half line: at `z = 3 + 2 √2`, `Γ² = 1/2`, that is `E₊ = 2 E₋`. -/
theorem half_line : (peel (3 + 2 * Real.sqrt 2)) ^ 2 = 1 / 2 := by
  have h : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs : 0 ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  unfold peel
  have : (3 + 2 * Real.sqrt 2 + 1) ≠ 0 := by positivity
  field_simp
  nlinarith [h]

/-- Half line: `E₊ = 2 E₋` iff `Γ² = 1/2`, so the first book holds one third of the budget. -/
theorem half_line_share (hi : 0 < di) (hj : 0 < dj) :
    (peel (di / dj)) ^ 2 = 1 / 2 ↔ Ep di dj = 2 * Em di dj := by
  have h1 : di + dj ≠ 0 := by positivity
  have h2 : dj ≠ 0 := hj.ne'
  have hp : peel (di / dj) = (di - dj) / (di + dj) := by
    unfold peel; field_simp
  rw [hp, div_pow, div_eq_iff (by positivity)]
  unfold Em Ep
  constructor <;> intro h <;> nlinarith [h]

/-! ## 22.3  Gap powers compose the step -/

/-- `k` copies of `u` added by `oplus`, left-folded from `0`. -/
noncomputable def oplusPow (u : ℝ) : ℕ → ℝ
  | 0 => 0
  | k + 1 => oplus (oplusPow u k) u

/-- Proposition 22.3: `Γ(z^k) = Γ ⊕ ⋯ ⊕ Γ` (`k` times), for `z > 0`. -/
theorem prop22_3 {z : ℝ} (hz : 0 < z) (k : ℕ) :
    oplusPow (peel z) k = peel (z ^ k) := by
  induction k with
  | zero => simp [oplusPow, peel]
  | succ k ih =>
    have hk : 0 < z ^ k := pow_pos hz k
    have h1 : z + 1 ≠ 0 := by positivity
    have h2 : z ^ k + 1 ≠ 0 := by positivity
    have h3 : z ^ (k + 1) + 1 ≠ 0 := by positivity
    have he : (1 : ℝ) + (z ^ k - 1) / (z ^ k + 1) * ((z - 1) / (z + 1))
        = 2 * (z ^ (k + 1) + 1) / ((z ^ k + 1) * (z + 1)) := by
      field_simp; ring
    rw [oplusPow, ih]
    unfold oplus peel
    rw [he]
    field_simp
    ring

/-- A negative power reverses the sign. -/
theorem peel_inv {z : ℝ} (hz : 0 < z) : peel z⁻¹ = - peel z := by
  have h1 : z + 1 ≠ 0 := by positivity
  have h2 : z ≠ 0 := hz.ne'
  unfold peel
  field_simp
  ring

/-- Charge form: `(Zc² - Zv²)/(Zc² + Zv²) = r ⊕ r` with `r = (Zc - Zv)/(Zc + Zv)`. -/
theorem prop22_3_charge {Zc Zv : ℝ} (hc : 0 < Zc) (hv : 0 < Zv) :
    (Zc ^ 2 - Zv ^ 2) / (Zc ^ 2 + Zv ^ 2)
      = oplus ((Zc - Zv) / (Zc + Zv)) ((Zc - Zv) / (Zc + Zv)) := by
  have h1 : Zc + Zv ≠ 0 := by positivity
  have h2 : Zc ^ 2 + Zv ^ 2 ≠ 0 := by positivity
  have h3 : (1 : ℝ) + (Zc - Zv) / (Zc + Zv) * ((Zc - Zv) / (Zc + Zv)) ≠ 0 := by
    have : (1 : ℝ) + (Zc - Zv) / (Zc + Zv) * ((Zc - Zv) / (Zc + Zv))
        = 2 * (Zc ^ 2 + Zv ^ 2) / (Zc + Zv) ^ 2 := by field_simp; ring
    rw [this]; positivity
  unfold oplus
  field_simp
  ring

/-! ## 24.1  The touch is one Jordan block (finite-dimensional linear algebra) -/

section jordan
variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V] [FiniteDimensional K V]

/-- With `N = h - λ`: if `dim ker N = 1` and `dim ker N² = 2`, then `N` is nonzero on
`ker N²` (and `N² = 0` there by definition): one Jordan block. -/
theorem prop24_1_touch (N : V →ₗ[K] V)
    (h1 : Module.finrank K (LinearMap.ker N) = 1)
    (h2 : Module.finrank K (LinearMap.ker (N ^ 2)) = 2) :
    ∃ w ∈ LinearMap.ker (N ^ 2), N w ≠ 0 := by
  by_contra hcon
  push Not at hcon
  have hle : LinearMap.ker (N ^ 2) ≤ LinearMap.ker N := fun w hw => hcon w hw
  have := Submodule.finrank_mono hle
  omega

/-- Split case: if `dim ker N = 2 = dim ker N²` then `N` vanishes on `ker N²`. -/
theorem prop24_1_split (N : V →ₗ[K] V)
    (h1 : Module.finrank K (LinearMap.ker N) = 2)
    (h2 : Module.finrank K (LinearMap.ker (N ^ 2)) = 2) :
    ∀ w ∈ LinearMap.ker (N ^ 2), N w = 0 := by
  have hle : LinearMap.ker N ≤ LinearMap.ker (N ^ 2) := by
    intro w hw
    simp only [LinearMap.mem_ker] at hw ⊢
    simp [pow_two, hw]
  have heq := Submodule.eq_of_le_of_finrank_eq hle (by omega)
  intro w hw
  rw [← heq] at hw
  exact hw

end jordan

/-! ## 25.1  Anatomy of the loop -/

/-- Boost along the first axis, half-angle `(c, s)`. -/
def Bx (c s : ℂ) : Matrix (Fin 2) (Fin 2) ℂ := Matrix.of ![![c, s], ![s, c]]
def By (c s : ℂ) : Matrix (Fin 2) (Fin 2) ℂ := Matrix.of ![![c, -Complex.I * s], ![Complex.I * s, c]]
/-- The loop `B_x B_y B_x⁻¹ B_y⁻¹`, inverses written out (`c² - s² = 1`). -/
def loopW (c s : ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  Bx c s * By c s * Bx c (-s) * By c (-s)

theorem loopW_trace_raw (c s : ℂ) :
    loopW c s 0 0 + loopW c s 1 1 = 2 * c ^ 4 - 4 * c ^ 2 * s ^ 2 - 2 * s ^ 4 := by
  have hI := Complex.I_sq
  simp [loopW, Bx, By, Matrix.mul_apply, Fin.sum_univ_two]
  ring_nf
  rw [hI]
  ring

theorem loopW_trace (c s : ℂ) (h : c ^ 2 - s ^ 2 = 1) :
    loopW c s 0 0 + loopW c s 1 1 = 2 - 4 * s ^ 4 := by
  rw [loopW_trace_raw]
  have hc : c ^ 2 = 1 + s ^ 2 := by rw [← h]; ring
  have : c ^ 4 = (1 + s ^ 2) ^ 2 := by rw [← hc]; ring
  rw [this, hc]; ring

/-- (c) At the wall `s² = 1`, `c² = 2`: `tr W = -2`. -/
theorem loopW_wall_trace (c s : ℂ) (h : c ^ 2 - s ^ 2 = 1) (hs : s ^ 2 = 1) :
    loopW c s 0 0 + loopW c s 1 1 = -2 := by
  rw [loopW_trace c s h]
  have : s ^ 4 = 1 := by rw [show s ^ 4 = (s ^ 2) ^ 2 by ring, hs]; norm_num
  rw [this]; norm_num

/-- (c) At the wall, `(W + 1)² = 0`. -/
theorem loopW_wall_nilpotent (c s : ℂ) (h : c ^ 2 - s ^ 2 = 1) (hs : s ^ 2 = 1) :
    (loopW c s + 1) * (loopW c s + 1) = 0 := by
  have hI := Complex.I_sq
  have hs := hs
  have hc1 : c ^ 2 = 1 + s ^ 2 := by rw [← h]; ring
  have hc : c ^ 2 = 2 := by rw [hc1, hs]; norm_num
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [loopW, Bx, By, Matrix.mul_apply, Fin.sum_univ_two, Matrix.add_apply, Matrix.one_apply]
  · linear_combination (c^6 + 2 * c^4 * Complex.I^2 * s^2 + 4 * c^4 * Complex.I * s^2 - 2 * c^4 * s^2 + 2 * c^4 + c^2 * Complex.I^4 * s^4 + 4 * c^2 * Complex.I^3 * s^4 + 4 * c^2 * Complex.I^2 * s^4 + 4 * c^2 * Complex.I^2 * s^2 - 4 * c^2 * Complex.I * s^4 + 8 * c^2 * Complex.I * s^2 + c^2 * s^4 - 4 * c^2 * s^2 + 6 * c^2 + 6 * Complex.I^4 * s^6 + 2 * Complex.I^4 * s^4 + 4 * Complex.I^3 * s^6 + 8 * Complex.I^3 * s^4 - 6 * Complex.I^2 * s^6 + 8 * Complex.I^2 * s^4 + 10 * Complex.I^2 * s^2 - 8 * Complex.I * s^4 + 20 * Complex.I * s^2 + 2 * s^4 - 10 * s^2 + 12) * hc + (Complex.I^4 * s^6 + 13 * Complex.I^4 * s^4 + 17 * Complex.I^4 * s^2 + 17 * Complex.I^4 + 8 * Complex.I^3 * s^4 + 24 * Complex.I^3 * s^2 + 24 * Complex.I^3 - 12 * Complex.I^2 * s^4 + 6 * Complex.I^2 * s^2 + 26 * Complex.I^2 - 16 * Complex.I * s^2 + 24 * Complex.I + 4 * s^2 - 16) * hs + (17 * Complex.I^2 + 24 * Complex.I + 9) * hI
  · linear_combination (4 * c^3 * Complex.I^2 * s^3 - 4 * c^3 * Complex.I * s^3 + 4 * c * Complex.I^4 * s^5 - 4 * c * Complex.I^3 * s^5 - 4 * c * Complex.I^2 * s^5 + 8 * c * Complex.I^2 * s^3 + 4 * c * Complex.I * s^5 - 8 * c * Complex.I * s^3) * hc + (4 * c * Complex.I^4 * s^5 + 12 * c * Complex.I^4 * s^3 + 12 * c * Complex.I^4 * s - 4 * c * Complex.I^3 * s^5 - 12 * c * Complex.I^3 * s^3 - 12 * c * Complex.I^3 * s - 8 * c * Complex.I^2 * s^3 + 12 * c * Complex.I^2 * s + 8 * c * Complex.I * s^3 - 12 * c * Complex.I * s) * hs + (12 * c * Complex.I^2 * s - 12 * c * Complex.I * s) * hI
  · linear_combination (4 * c^3 * Complex.I^2 * s^3 + 4 * c^3 * Complex.I * s^3 + 4 * c * Complex.I^4 * s^5 + 4 * c * Complex.I^3 * s^5 - 4 * c * Complex.I^2 * s^5 + 8 * c * Complex.I^2 * s^3 - 4 * c * Complex.I * s^5 + 8 * c * Complex.I * s^3) * hc + (4 * c * Complex.I^4 * s^5 + 12 * c * Complex.I^4 * s^3 + 12 * c * Complex.I^4 * s + 4 * c * Complex.I^3 * s^5 + 12 * c * Complex.I^3 * s^3 + 12 * c * Complex.I^3 * s - 8 * c * Complex.I^2 * s^3 + 12 * c * Complex.I^2 * s - 8 * c * Complex.I * s^3 + 12 * c * Complex.I * s) * hs + (12 * c * Complex.I^2 * s + 12 * c * Complex.I * s) * hI
  · linear_combination (c^6 + 2 * c^4 * Complex.I^2 * s^2 - 4 * c^4 * Complex.I * s^2 - 2 * c^4 * s^2 + 2 * c^4 + c^2 * Complex.I^4 * s^4 - 4 * c^2 * Complex.I^3 * s^4 + 4 * c^2 * Complex.I^2 * s^4 + 4 * c^2 * Complex.I^2 * s^2 + 4 * c^2 * Complex.I * s^4 - 8 * c^2 * Complex.I * s^2 + c^2 * s^4 - 4 * c^2 * s^2 + 6 * c^2 + 6 * Complex.I^4 * s^6 + 2 * Complex.I^4 * s^4 - 4 * Complex.I^3 * s^6 - 8 * Complex.I^3 * s^4 - 6 * Complex.I^2 * s^6 + 8 * Complex.I^2 * s^4 + 10 * Complex.I^2 * s^2 + 8 * Complex.I * s^4 - 20 * Complex.I * s^2 + 2 * s^4 - 10 * s^2 + 12) * hc + (Complex.I^4 * s^6 + 13 * Complex.I^4 * s^4 + 17 * Complex.I^4 * s^2 + 17 * Complex.I^4 - 8 * Complex.I^3 * s^4 - 24 * Complex.I^3 * s^2 - 24 * Complex.I^3 - 12 * Complex.I^2 * s^4 + 6 * Complex.I^2 * s^2 + 26 * Complex.I^2 + 16 * Complex.I * s^2 - 24 * Complex.I + 4 * s^2 - 16) * hs + (17 * Complex.I^2 - 24 * Complex.I + 9) * hI

/-- (c) At the wall `W + 1 ≠ 0`: its top-left entry is `4 i`. -/
theorem loopW_wall_ne (c s : ℂ) (h : c ^ 2 - s ^ 2 = 1) (hs : s ^ 2 = 1) :
    loopW c s + 1 ≠ 0 := by
  have hI := Complex.I_sq
  have hc1 : c ^ 2 = 1 + s ^ 2 := by rw [← h]; ring
  have hc : c ^ 2 = 2 := by rw [hc1, hs]; norm_num
  have h00 : (loopW c s + 1) 0 0 = 4 * Complex.I := by
    simp [loopW, Bx, By, Matrix.mul_apply, Fin.sum_univ_two, Matrix.add_apply, Matrix.one_apply]
    linear_combination (c^2 + Complex.I^2 * s^2 + 2 * Complex.I * s^2 - s^2 + 2) * hc + (Complex.I^2 * s^2 + 3 * Complex.I^2 + 4 * Complex.I - 2) * hs + (3) * hI
  intro h0
  have := congrFun (congrFun h0 0) 0
  rw [h00] at this
  simp at this

/-! Closed forms in the step coordinate `Γ`. -/

/-- Obliqueness `K = 1/(1 - 2Γ²)` below the wall. -/
noncomputable def Kbelow (G : ℝ) : ℝ := 1 / (1 - 2 * G ^ 2)
/-- Beyond the wall `K = 2Γ²/(2Γ² - 1)`. -/
noncomputable def Kbeyond (G : ℝ) : ℝ := 2 * G ^ 2 / (2 * G ^ 2 - 1)

/-- (b): with `R = Γ²`, `T = 1 - R`, `K = 1/(T - R)`. -/
theorem K_eq_inv_T_sub_R (G : ℝ) : Kbelow G = 1 / ((1 - G ^ 2) - G ^ 2) := by
  unfold Kbelow; ring_nf

/-- (e): `K = 1/sin²(α/2)` with `cos²(α/2) = 2Γ²`: `sin² = 1 - 2Γ²`. -/
theorem K_eq_inv_sin_sq (G : ℝ) : Kbelow G = 1 / (1 - 2 * G ^ 2) := rfl

/-- Pairing across the wall: `Γ Γ' = 1/2` gives the same `K`. -/
theorem K_pair {G G' : ℝ} (hG : G ≠ 0) (hp : G * G' = 1 / 2) (hw : 1 - 2 * G ^ 2 ≠ 0) :
    Kbeyond G' = Kbelow G := by
  have hG' : G' = 1 / (2 * G) := by field_simp; linarith
  subst hG'
  unfold Kbeyond Kbelow
  have h2 : 2 * G ^ 2 - 1 ≠ 0 := by intro h; apply hw; linarith
  field_simp

/-- `R/T` equals `sinh²(r/2)` when `Γ = tanh(r/2)`; algebraically `Γ²/(1-Γ²)`, and
the trace of the loop is `2 - 4 (R/T)²`. At `Γ² = 1/2` it is `-2`. -/
theorem trace_at_wall : (2 : ℝ) - 4 * ((1 / 2) / (1 - 1 / 2)) ^ 2 = -2 := by norm_num


/-- Values at the three marked steps: `z = 3, 5, 7` give `Γ = 1/2, 2/3, 3/4`. -/
theorem peel_3 : peel 3 = 1 / 2 := by norm_num [peel]
theorem peel_5 : peel 5 = 2 / 3 := by norm_num [peel]
theorem peel_7 : peel 7 = 3 / 4 := by norm_num [peel]

/-- The steps of ratio 5 and 7 are paired across the wall: `Γ Γ' = 1/2`. -/
theorem pair_5_7 : peel 5 * peel 7 = 1 / 2 := by norm_num [peel]

/-- `K = 2` at `z = 3`, `K = 9` at `z = 5`, and `K = 9` at `z = 7` (beyond the wall). -/
theorem K_3 : Kbelow (peel 3) = 2 := by norm_num [Kbelow, peel]
theorem K_5 : Kbelow (peel 5) = 9 := by norm_num [Kbelow, peel]
theorem K_7 : Kbeyond (peel 7) = 9 := by norm_num [Kbeyond, peel]

/-- `z = 5`: `R = 4/9`, `T = 5/9`, `R/T = 4/5`, `tr W = 2 - 4 (R/T)² = -14/25`,
`cos(θ/2) = 1 - 2 (R/T)² = -7/25`, `(tr W)² = 196/625`. -/
theorem z5_trace :
    (peel 5) ^ 2 = 4 / 9 ∧ 1 - (peel 5) ^ 2 = 5 / 9 ∧
    (peel 5) ^ 2 / (1 - (peel 5) ^ 2) = 4 / 5 ∧
    2 - 4 * ((peel 5) ^ 2 / (1 - (peel 5) ^ 2)) ^ 2 = -14 / 25 ∧
    1 - 2 * ((peel 5) ^ 2 / (1 - (peel 5) ^ 2)) ^ 2 = -7 / 25 ∧
    (2 - 4 * ((peel 5) ^ 2 / (1 - (peel 5) ^ 2)) ^ 2) ^ 2 = 196 / 625 := by
  norm_num [peel]

/-- `z = 5`: `cos θ = 2 cos²(θ/2) - 1 = -527/625`. -/
theorem z5_cos_turn (θ : ℝ) (h : Real.cos (θ / 2) = -7 / 25) : Real.cos θ = -527 / 625 := by
  have : θ = 2 * (θ / 2) := by ring
  rw [this, Real.cos_two_mul, h]; norm_num

/-- `z = 7`: `R/T = 9/7`, `tr W = 2 - 4 (R/T)² = -226/49`, beyond the wall `|tr W| > 2`. -/
theorem z7_trace :
    (peel 7) ^ 2 = 9 / 16 ∧ 1 - (peel 7) ^ 2 = 7 / 16 ∧
    (peel 7) ^ 2 / (1 - (peel 7) ^ 2) = 9 / 7 ∧
    2 - 4 * ((peel 7) ^ 2 / (1 - (peel 7) ^ 2)) ^ 2 = -226 / 49 := by
  norm_num [peel]

/-- Centre of turn: `ρ² = (1 - s)/(1 + s)` with `s = √(1 - 2Γ²)`; at `z = 5`, `s = 1/3`,
`ρ² = 1/2` and `cosh η = 1/s = 3`. -/
theorem z5_centre :
    Real.sqrt (1 - 2 * (peel 5) ^ 2) = 1 / 3 ∧
    (1 - 1 / 3) / (1 + 1 / 3 : ℝ) = 1 / 2 ∧ 1 / (1 / 3 : ℝ) = 3 := by
  refine ⟨?_, by norm_num, by norm_num⟩
  have : 1 - 2 * (peel 5) ^ 2 = (1 / 3) ^ 2 := by norm_num [peel]
  rw [this, Real.sqrt_sq (by norm_num)]

/-- `z = 3`: `ρ = √2 - 1` (`ρ²= (1 - s)/(1 + s)` with `s = √2/2`). -/
theorem z3_centre : (1 - Real.sqrt 2 / 2) / (1 + Real.sqrt 2 / 2) = (Real.sqrt 2 - 1) ^ 2 := by
  have h : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs : 0 ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  have hd : (1 + Real.sqrt 2 / 2) ≠ 0 := by positivity
  rw [div_eq_iff hd]
  nlinarith [h, hs]

/-- `ρ² = 1/2` at `z = 5` and at no other ratio (for `0 < Γ`, `Γ² < 1/2`). -/
theorem rho_sq_half_iff {G : ℝ} (hG : 0 < G) (hw : G ^ 2 < 1 / 2) :
    (1 - Real.sqrt (1 - 2 * G ^ 2)) / (1 + Real.sqrt (1 - 2 * G ^ 2)) = 1 / 2 ↔ G = 2 / 3 := by
  have hpos : 0 < 1 - 2 * G ^ 2 := by linarith
  have hs : Real.sqrt (1 - 2 * G ^ 2) ^ 2 = 1 - 2 * G ^ 2 := Real.sq_sqrt hpos.le
  have hs0 : 0 ≤ Real.sqrt (1 - 2 * G ^ 2) := Real.sqrt_nonneg _
  have hd : (1 + Real.sqrt (1 - 2 * G ^ 2)) ≠ 0 := by positivity
  rw [div_eq_iff hd]
  constructor
  · intro h
    have h3 : Real.sqrt (1 - 2 * G ^ 2) = 1 / 3 := by linarith
    rw [h3] at hs
    nlinarith
  · intro h
    subst h
    have h3 : Real.sqrt (1 - 2 * (2 / 3 : ℝ) ^ 2) = 1 / 3 := by
      rw [show 1 - 2 * (2 / 3 : ℝ) ^ 2 = (1 / 3) ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
    rw [h3]; norm_num

/-! ## 25.2  The tree feeds the phase record (arithmetic of the formula) -/

/-- The read share after `n` passes: `c_n = ½ [1 + sin(nθ) sin φ]`. -/
noncomputable def share (θ φ : ℝ) (n : ℕ) : ℝ := (1 + Real.sin (n * θ) * Real.sin φ) / 2

/-- The share is a share: `0 ≤ c_n ≤ 1`. -/
theorem share_mem (θ φ : ℝ) (n : ℕ) : 0 ≤ share θ φ n ∧ share θ φ n ≤ 1 := by
  have h1 := Real.sin_le_one (n * θ)
  have h2 := Real.neg_one_le_sin (n * θ)
  have h3 := Real.sin_le_one φ
  have h4 := Real.neg_one_le_sin φ
  unfold share
  constructor <;> nlinarith [mul_self_nonneg (Real.sin (n * θ) + Real.sin φ),
    mul_self_nonneg (Real.sin (n * θ) - Real.sin φ)]

/-- On the fixed line (`sin φ = 0`) there is no signal at any pass: `c_n = 1/2`. -/
theorem share_fixed_line (θ : ℝ) (n : ℕ) : share θ 0 n = 1 / 2 := by
  simp [share]

/-- The peel coordinate of the read share is `Γ = 1 - 2 c_n = - sin(nθ) sin φ`. -/
theorem share_peel (θ φ : ℝ) (n : ℕ) : 1 - 2 * share θ φ n = - (Real.sin (n * θ) * Real.sin φ) := by
  unfold share; ring

/-- Third-axis direction: `sin²φ = 2Γ²`; at `z = 5` it is `8/9`. -/
theorem third_axis_z5 : 2 * (peel 5) ^ 2 = 8 / 9 := by norm_num [peel]

/-- Third-axis light first reaches the half line (`2Γ² = 1/2`) at `z = 3`. -/
theorem third_axis_half_line {z : ℝ} (hz : 0 < z) : 2 * (peel z) ^ 2 = 1 / 2 ∧ 0 < peel z ↔ z = 3 := by
  have h1 : z + 1 ≠ 0 := by positivity
  unfold peel
  constructor
  · rintro ⟨h, hp⟩
    have hz1 : 1 < z := by
      by_contra hc
      push Not at hc
      have : z - 1 ≤ 0 := by linarith
      have : (z - 1) / (z + 1) ≤ 0 := div_nonpos_of_nonpos_of_nonneg this (by positivity)
      linarith
    field_simp at h
    nlinarith
  · rintro rfl
    norm_num

end NewProps
