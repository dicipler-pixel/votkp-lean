/-
VOTKP §6.2: surviving matches.

`C : ℝⁿ → ℝ³` is the receiver. Full row rank is surjectivity of `C`, and it is the
hypothesis the paper uses for `(3) ⇒ (4)`. `P` is the orthogonal projector onto `ker C`.
The four conditions are equivalent, and the factor `T` is the map induced on the quotient
by `ker C`.
-/
import Mathlib

namespace VOTKP.Surviving

open LinearMap Submodule

variable {n : ℕ}

/-- **§6.2.** For a surjective receiver `C : ℝⁿ → ℝ³` and a later endomorphism `M`,
the following are equivalent:
(1) `Cx = Cy` implies `CMx = CMy`;
(2) `ker C ⊆ ker(CM)`;
(3) `CMP = 0`, with `P` the orthogonal projector onto `ker C`;
(4) `CM = TC` for some `T : ℝ³ → ℝ³`. -/
theorem surviving_matches
    (C : EuclideanSpace ℝ (Fin n) →ₗ[ℝ] EuclideanSpace ℝ (Fin 3))
    (M : EuclideanSpace ℝ (Fin n) →ₗ[ℝ] EuclideanSpace ℝ (Fin n))
    (hC : Function.Surjective C) :
    let P := (ker C).starProjection.toLinearMap
    ((∀ x y, C x = C y → C (M x) = C (M y)) ↔ ker C ≤ ker (C ∘ₗ M)) ∧
      (ker C ≤ ker (C ∘ₗ M) ↔ (C ∘ₗ M) ∘ₗ P = 0) ∧
      ((C ∘ₗ M) ∘ₗ P = 0 ↔
        ∃ T : EuclideanSpace ℝ (Fin 3) →ₗ[ℝ] EuclideanSpace ℝ (Fin 3), C ∘ₗ M = T ∘ₗ C) := by
  intro P
  have hmem : ∀ x, P x ∈ ker C := fun x => by
    simpa [P] using starProjection_apply_mem (ker C) x
  have hfix : ∀ v, v ∈ ker C → P v = v := fun v hv => by
    have h := (starProjection_eq_self_iff (K := ker C)).mpr hv
    simpa [P] using h
  refine ⟨?_, ?_, ?_⟩
  · constructor
    · intro h v hv
      have h0 : C v = 0 := mem_ker.mp hv
      have hstep : C (M v) = C (M 0) := h v 0 (by simp [h0])
      rw [mem_ker, LinearMap.comp_apply, hstep]
      simp
    · intro h x y hxy
      have hx : x - y ∈ ker C := by
        rw [mem_ker, map_sub, hxy, sub_self]
      have hm : C (M (x - y)) = 0 := by
        simpa [LinearMap.comp_apply] using mem_ker.mp (h hx)
      have hm' : C (M x) - C (M y) = 0 := by
        rw [← map_sub, ← map_sub]
        exact hm
      exact sub_eq_zero.mp hm'
  · constructor
    · intro hker
      apply LinearMap.ext
      intro x
      rw [LinearMap.comp_apply, LinearMap.comp_apply]
      exact mem_ker.mp (hker (hmem x))
    · intro h0 v hv
      have happ := LinearMap.congr_fun h0 v
      rw [LinearMap.comp_apply, LinearMap.comp_apply, hfix v hv] at happ
      exact mem_ker.mpr happ
  · constructor
    · intro h0
      have hker : ker C ≤ ker (C ∘ₗ M) := by
        intro v hv
        have happ := LinearMap.congr_fun h0 v
        rw [LinearMap.comp_apply, LinearMap.comp_apply, hfix v hv] at happ
        exact mem_ker.mpr happ
      let B := C ∘ₗ M
      let Q := (ker C).liftQ B fun x hx => mem_ker.mpr (hker hx)
      refine ⟨Q ∘ₗ (C.quotKerEquivOfSurjective hC).symm.toLinearMap, ?_⟩
      apply LinearMap.ext
      intro x
      simp [B, Q, LinearMap.comp_apply, quotKerEquivOfSurjective_symm_apply, liftQ_apply]
    · rintro ⟨T, hT⟩
      apply LinearMap.ext
      intro x
      show C (M (P x)) = 0
      have hCx : C (P x) = 0 := mem_ker.mp (hmem x)
      have hCM : C (M (P x)) = T (C (P x)) := by
        simpa [LinearMap.comp_apply] using congr_fun (congrArg DFunLike.coe hT) (P x)
      rw [hCM, hCx, map_zero]

end VOTKP.Surviving
