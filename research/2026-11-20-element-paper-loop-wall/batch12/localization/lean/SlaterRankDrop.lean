import Mathlib.LinearAlgebra.Determinant
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition

/-!
An occupied overlap sends a source Bloch fibre into the target fibre specified
by a commensurate twist. A strict dimension drop on one such fibre forces zero
determinant of the full finite-dimensional occupied-overlap operator.
-/

namespace VOTKP.Junction

variable {K A B V : Type*} [Field K] [AddCommGroup A] [Module K A]
  [AddCommGroup B] [Module K B] [AddCommGroup V] [Module K V] [Module.Finite K B]

/-- The restriction of M to one embedded occupied fibre factors through a
smaller target fibre. This precludes injectivity of the global map. -/
theorem occupiedOverlap_not_injective_of_rank_drop
    (M : V →ₗ[K] V) (src : A →ₗ[K] V) (dst : B →ₗ[K] V) (block : A →ₗ[K] B)
    (hsrc : Function.Injective src) (fiber : M.comp src = dst.comp block)
    (drop : Module.finrank K B < Module.finrank K A) : ¬ Function.Injective M := by
  intro hM
  apply (not_le_of_gt drop)
  apply LinearMap.finrank_le_finrank_of_injective (f := block)
  intro a b hab
  apply hsrc
  apply hM
  have h : M.comp src a = M.comp src b := by
    rw [fiber]
    exact congrArg dst hab
  exact h

/-- This is the determinant of the overlap on the entire occupied space V. -/
theorem occupiedOverlap_det_zero_of_rank_drop [Module.Finite K V]
    (M : V →ₗ[K] V) (src : A →ₗ[K] V) (dst : B →ₗ[K] V) (block : A →ₗ[K] B)
    (hsrc : Function.Injective src) (fiber : M.comp src = dst.comp block)
    (drop : Module.finrank K B < Module.finrank K A) : M.det = 0 := by
  apply LinearMap.det_eq_zero_iff_ker_ne_bot.mpr
  intro hker
  exact occupiedOverlap_not_injective_of_rank_drop M src dst block hsrc fiber drop
    (LinearMap.ker_eq_bot.mp hker)

#print axioms occupiedOverlap_not_injective_of_rank_drop
#print axioms occupiedOverlap_det_zero_of_rank_drop

end VOTKP.Junction
