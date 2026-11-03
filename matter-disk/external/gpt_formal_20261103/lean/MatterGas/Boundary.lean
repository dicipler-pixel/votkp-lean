/- Finite matrix core. Standard matrix algebra, specialized to the proposed boundary diagnostic.
   No empirical interpretation is encoded in these theorems. -/
import Mathlib.Analysis.Matrix.Order
import Mathlib.Data.Matrix.Block
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Module
import Mathlib.Tactic.NormNum

set_option linter.unusedSectionVars false

namespace MatterGas
open Matrix
open scoped MatrixOrder Matrix.Norms.L2Operator ComplexOrder

variable {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]

/-- Principal A block of a finite matrix on A⊕B. -/
abbrev localBlock (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) : Matrix m m ℂ := C.toBlocks₁₁
/-- Off-diagonal cross block. -/
abbrev crossBlock (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) : Matrix m n ℂ := C.toBlocks₁₂
/-- Cross-boundary one-body matrix, independent of Gaussian/physical interpretation. -/
def boundary (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) : Matrix m m ℂ := crossBlock C * (crossBlock C)ᴴ
/-- Global failure of idempotency, restricted to A. -/
def thermalDefect (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) : Matrix m m ℂ := (C-C*C).toBlocks₁₁

/-- Exact block identity for a Hermitian finite matrix. -/
theorem block_defect_identity (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) (hC : C.IsHermitian) :
    localBlock C - localBlock C * localBlock C = thermalDefect C + boundary C := by
  ext i j
  simp only [localBlock, thermalDefect, boundary, crossBlock, Matrix.toBlocks₁₁,
    Matrix.toBlocks₁₂, Matrix.of_apply, Matrix.sub_apply, Matrix.add_apply,
    Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_sum_type]
  have hh (k : n) : star (C (Sum.inl j) (Sum.inr k)) = C (Sum.inr k) (Sum.inl j) := by
    exact congrFun (congrFun hC.eq (Sum.inr k)) (Sum.inl j)
  simp only [hh]
  ring

/-- The cross-boundary matrix is always positive semidefinite. -/
theorem boundary_posSemidef (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) :
    (boundary C).PosSemidef := Matrix.posSemidef_self_mul_conjTranspose _

/-- A positive Hermitian contraction has a positive idempotency defect. -/
theorem contraction_defect_posSemidef (C : Matrix (m ⊕ n) (m ⊕ n) ℂ)
    (h0 : 0 ≤ C) (h1 : C ≤ 1) : (C-C*C).PosSemidef := by
  have hc : Commute C (1-C) := by
    show C*(1-C) = (1-C)*C
    noncomm_ring
  have hp := Commute.mul_nonneg h0 (sub_nonneg.mpr h1) hc
  simpa only [mul_sub, mul_one] using hp.posSemidef

/-- Restricting the positive defect preserves positivity. -/
theorem thermalDefect_posSemidef (C : Matrix (m ⊕ n) (m ⊕ n) ℂ)
    (h0 : 0 ≤ C) (h1 : C ≤ 1) : (thermalDefect C).PosSemidef := by
  exact (contraction_defect_posSemidef C h0 h1).submatrix Sum.inl

/-- The boundary matrix is bounded by the local covariance polynomial. -/
theorem boundary_le_local_defect (C : Matrix (m ⊕ n) (m ⊕ n) ℂ)
    (h0 : 0 ≤ C) (h1 : C ≤ 1) :
    boundary C ≤ localBlock C - localBlock C * localBlock C := by
  rw [block_defect_identity C h0.posSemidef.isHermitian]
  exact le_add_of_nonneg_left (thermalDefect_posSemidef C h0 h1).nonneg

/-- Idempotency kills the thermal term exactly. -/
theorem thermalDefect_projector (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) (hp : C*C=C) :
    thermalDefect C = 0 := by
  ext i j
  simp [thermalDefect, hp, Matrix.toBlocks₁₁]

/-- Pure-projector reduction of the boundary construction. -/
theorem boundary_projector (C : Matrix (m ⊕ n) (m ⊕ n) ℂ)
    (hC : C.IsHermitian) (hp : C*C=C) :
    boundary C = localBlock C - localBlock C * localBlock C := by
  simpa [thermalDefect_projector C hp] using (block_defect_identity C hC).symm

/-- Disconnected blocks have no cross-boundary signal. -/
theorem boundary_disconnected (A : Matrix m m ℂ) (D : Matrix n n ℂ) :
    boundary (Matrix.fromBlocks A 0 0 D) = 0 := by
  simp [boundary, crossBlock]

/-- Vanishing cross-boundary trace is equivalent to a vanishing cross block. -/
theorem boundary_trace_zero_iff (C : Matrix (m ⊕ n) (m ⊕ n) ℂ) :
    (boundary C).trace = 0 ↔ crossBlock C = 0 := by
  exact Matrix.trace_mul_conjTranspose_self_eq_zero_iff

/-- The local covariance polynomial is bounded by one quarter of the identity.
This holds for every Hermitian A, independently of a contraction hypothesis. -/
theorem local_defect_le_quarter (A : Matrix m m ℂ) (hA : A.IsHermitian) :
    A-A*A ≤ (1/4:ℝ) • (1 : Matrix m m ℂ) := by
  let S : Matrix m m ℂ := (1/2:ℝ) • (1 : Matrix m m ℂ) - A
  have hS : Sᴴ = S := by simp [S, hA.eq]
  have hpos := Matrix.posSemidef_conjTranspose_mul_self S
  rw [hS] at hpos
  rw [Matrix.le_iff]
  convert hpos using 1
  dsimp [S]
  simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm,
    one_mul, mul_one]
  module

/-- Full finite-matrix boundary bound for every Hermitian contraction. -/
theorem boundary_bounds (C : Matrix (m ⊕ n) (m ⊕ n) ℂ)
    (h0 : 0 ≤ C) (h1 : C ≤ 1) :
    0 ≤ boundary C ∧ boundary C ≤ (1/4:ℝ) • (1 : Matrix m m ℂ) := by
  refine ⟨(boundary_posSemidef C).nonneg, ?_⟩
  exact (boundary_le_local_defect C h0 h1).trans
    (local_defect_le_quarter (localBlock C) (h0.posSemidef.isHermitian.submatrix Sum.inl))

/-- Exact coordinate change in the square-and-offset disk construction. -/
theorem square_offset_identity (nu : ℂ) :
    1-4*(nu*(1-nu)) = (1-2*nu)^2 := by ring

/-- Any finite square matrix embeds as the A block of an idempotent.
The embedding need not be Hermitian; positivity must not be inferred from idempotency alone. -/
theorem arbitrary_block_idempotent (A : Matrix m m ℂ) :
    let C := Matrix.fromBlocks A (1 : Matrix m m ℂ) (A-A*A) (1-A)
    C*C=C := by
  dsimp
  rw [Matrix.fromBlocks_multiply]
  congr 1 <;> noncomm_ring

end MatterGas
