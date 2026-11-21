import Mathlib.LinearAlgebra.Determinant
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
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

/-- At least the dimension lost on this fibre lies in the global overlap kernel. -/
theorem occupiedOverlap_kernel_at_least_rank_loss [Module.Finite K A] [Module.Finite K V]
    (M : V →ₗ[K] V) (src : A →ₗ[K] V) (dst : B →ₗ[K] V) (block : A →ₗ[K] B)
    (hsrc : Function.Injective src) (fiber : M.comp src = dst.comp block) :
    Module.finrank K A - Module.finrank K B ≤ Module.finrank K (LinearMap.ker M) := by
  let lift : LinearMap.ker block →ₗ[K] LinearMap.ker M :=
    (src.comp (LinearMap.ker block).subtype).codRestrict (LinearMap.ker M) (by
      intro a
      change M (src (a : A)) = 0
      have e := congrArg (fun f : A →ₗ[K] V => f (a : A)) fiber
      simpa [LinearMap.comp_apply, show block (a : A) = 0 from a.property] using e)
  have hlift : Function.Injective lift := by
    intro a b hab
    apply Subtype.ext
    apply hsrc
    exact congrArg Subtype.val hab
  have hker := LinearMap.finrank_le_finrank_of_injective (f := lift) hlift
  have hsum := block.finrank_range_add_finrank_ker
  have hrange := Submodule.finrank_le (LinearMap.range block)
  omega

#print axioms occupiedOverlap_kernel_at_least_rank_loss
#print axioms occupiedOverlap_not_injective_of_rank_drop
#print axioms occupiedOverlap_det_zero_of_rank_drop

end VOTKP.Junction
