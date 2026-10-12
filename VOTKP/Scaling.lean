/-
VOTKP §15.3, Theorem 15.4: scale blindness (Jeromie Beasley).

Take a Coulomb Hamiltonian `H = Σ p²/2m + V` on a configuration space `E`, and multiply every mass
by `λ > 0`. Writing the coordinate scale `r = r'/λ`, the kinetic term scales by `λ²/λ = λ` and
the Coulomb term, homogeneous of degree `−1`, by `λ`, so `H_λ` is unitarily equivalent to `λH`:
every energy scales by `λ` and every ratio `IE_{k+1}/IE_k` is unchanged (`Smith.scale_blind`).

The kinetic operator is written with one mass per coordinate direction `b k` (three directions per
particle), `(Tψ)(x) = −Σₖ (ℏ²/2mₖ) ∂²_{bₖ}ψ(x)`. The theorem `scale_blindness` is the pointwise
intertwining: if `Hψ = Eψ`, then `φ(x) = ψ(λx)` satisfies `H_λ φ = λE φ`. Any potential with
`V(λx) = λ⁻¹V(x)` qualifies; `coulomb_homogeneous` shows every pair-Coulomb sum does.
Developed with AI assistance.
-/
import Mathlib

namespace VOTKP.Scaling

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {ι : Type*} [Fintype ι]

/-- `(T_m ψ)(x) = −Σₖ (ℏ²/2mₖ) ∂²_{bₖ} ψ(x)`. -/
noncomputable def kinetic (hbar : ℝ) (m : ι → ℝ) (b : ι → E) (ψ : E → ℂ) (x : E) : ℂ :=
  -∑ k, (hbar ^ 2 / (2 * m k)) • iteratedFDeriv ℝ 2 ψ x (fun _ => b k)

/-- `(Hψ)(x) = (T_m ψ)(x) + V(x) ψ(x)`. -/
noncomputable def hamiltonian (hbar : ℝ) (m : ι → ℝ) (b : ι → E) (V : E → ℝ) (ψ : E → ℂ)
    (x : E) : ℂ :=
  kinetic hbar m b ψ x + (V x : ℂ) * ψ x

/-- A sum of pair Coulomb terms `V(x) = Σₚ Qₚ/‖Lₚ x‖`, `Lₚ` the relative coordinate of pair `p`
and `Qₚ = qᵢqⱼ/(4πε₀)`. -/
noncomputable def coulomb {P : Type*} [Fintype P] (Q : P → ℝ) (L : P → E →L[ℝ] E) (x : E) : ℝ :=
  ∑ p, Q p / ‖L p x‖

/-- Second derivatives scale by `λ²` under the dilation `x ↦ λx`. -/
lemma iteratedFDeriv_two_dilate (ψ : E → ℂ) (hψ : ContDiff ℝ 2 ψ) (l : ℝ) (x v : E) :
    iteratedFDeriv ℝ 2 (fun y => ψ (l • y)) x (fun _ => v)
      = (l ^ 2) • iteratedFDeriv ℝ 2 ψ (l • x) (fun _ => v) := by
  have hcomp : (fun y => ψ (l • y)) = ψ ∘ (l • ContinuousLinearMap.id ℝ E) := by
    funext y
    simp
  rw [hcomp, ContinuousLinearMap.iteratedFDeriv_comp_right (i := 2) _ hψ x (by norm_num),
    ContinuousMultilinearMap.compContinuousLinearMap_apply]
  have hv : (fun i : Fin 2 => (l • ContinuousLinearMap.id ℝ E) ((fun _ => v) i))
      = fun i => (fun _ : Fin 2 => l) i • (fun _ : Fin 2 => v) i := by
    funext i
    simp
  rw [hv, ContinuousMultilinearMap.map_smul_univ]
  simp

/-- **Theorem 15.4, the potential.** A pair-Coulomb sum is homogeneous of degree `−1`. -/
theorem coulomb_homogeneous {P : Type*} [Fintype P] (Q : P → ℝ) (L : P → E →L[ℝ] E)
    (l : ℝ) (hl : 0 < l) (x : E) : coulomb Q L (l • x) = l⁻¹ * coulomb Q L x := by
  unfold coulomb
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [map_smul, norm_smul, Real.norm_eq_abs, abs_of_pos hl]
  ring

lemma mass_coefficient (hbar l mk : ℝ) (hl : 0 < l) :
    hbar ^ 2 / (2 * (l * mk)) * l ^ 2 = l * (hbar ^ 2 / (2 * mk)) := by
  by_cases hm : mk = 0
  · simp [hm]
  · have hl0 : l ≠ 0 := hl.ne'
    field_simp
    try ring

/-- **Theorem 15.4, the kinetic term.** With every mass multiplied by `λ`, the kinetic operator on
`ψ(λ·)` is `λ` times the original kinetic operator at `λx`. -/
theorem kinetic_scaling (hbar : ℝ) (m : ι → ℝ) (b : ι → E) (ψ : E → ℂ) (hψ : ContDiff ℝ 2 ψ)
    (l : ℝ) (hl : 0 < l) (x : E) :
    kinetic hbar (fun k => l * m k) b (fun y => ψ (l • y)) x
      = (l : ℂ) * kinetic hbar m b ψ (l • x) := by
  unfold kinetic
  rw [mul_neg, Finset.mul_sum]
  congr 1
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [iteratedFDeriv_two_dilate ψ hψ l x (b k), smul_smul, mass_coefficient hbar l (m k) hl,
    Complex.real_smul, Complex.real_smul]
  push_cast
  ring

/-- **Theorem 15.4, scale blindness.** If `Hψ = Eψ` with a potential homogeneous of degree `−1`,
then `φ(x) = ψ(λx)` satisfies `H_λ φ = λE φ`, where `H_λ` has every mass multiplied by `λ`. -/
theorem scale_blindness (hbar : ℝ) (m : ι → ℝ) (b : ι → E) (V : E → ℝ) (l : ℝ) (hl : 0 < l)
    (hV : ∀ x, V (l • x) = l⁻¹ * V x) (ψ : E → ℂ) (hψ : ContDiff ℝ 2 ψ) (En : ℂ)
    (heig : ∀ y, hamiltonian hbar m b V ψ y = En * ψ y) (x : E) :
    hamiltonian hbar (fun k => l * m k) b V (fun y => ψ (l • y)) x = (l * En) * ψ (l • x) := by
  have hl0 : l ≠ 0 := hl.ne'
  have hVx : V x = l * V (l • x) := by
    rw [hV x]
    field_simp
  have h := heig (l • x)
  unfold hamiltonian at h ⊢
  rw [kinetic_scaling hbar m b ψ hψ l hl x, hVx]
  push_cast
  linear_combination (l : ℂ) * h

end VOTKP.Scaling
