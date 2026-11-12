/-
Berry curvature of the lower Pauli projector, checked exactly.

The two-level example of the IQGT manuscript (Appendix B) and of the note
"From Geometric Flux to Magnetic Charge": for a unit direction n the lower
eigenprojector of H = n·σ is P(n) = (1/2)(I - n·σ).  The Berry curvature in the
convention Ω_ab = i Tr(P [∂_a P, ∂_b P]) is Ω = (1/2) sin θ dθ∧dφ on the sphere.

What is proved here, with no analytic input beyond the derivatives of sin and cos:

* `pauli_comm`      : [a·σ, b·σ] = 2i (a×b)·σ for every pair of real vectors.
* `curvature_formula`: for every real n, a, b (unit norm not needed),
                       i Tr( P(n) · [D(a), D(b)] ) = (1/2) n·(a×b),  D(a) = -(1/2) a·σ.
* `proj_affine`     : P(n + h a) - P(n) = h · D(a) exactly; the projector is affine
                       in n, so D(a) is its derivative along a with no remainder.
* `hasDerivAt_nvec_*`: the six component derivatives of n(θ,φ).
* `triple_product`  : n·(∂_θ n × ∂_φ n) = sin θ.
* `berry_curvature` : i Tr( P(n) [D(∂_θ n), D(∂_φ n)] ) = sin θ / 2 = omega θ,
                       the coefficient that the monopole_stance archive took as input.

Not proved here: the line bundle, its Chern class, any spatial pullback, any
electromagnetic identification.  Those remain written mathematics, as the note says.
-/
import Mathlib

open Matrix Complex

namespace MonopoleStance

noncomputable section

/-- A real 3-vector. -/
abbrev Vec3 := ℝ × ℝ × ℝ

/-- a·σ = a₁σ₁ + a₂σ₂ + a₃σ₃ as an explicit 2×2 complex matrix. -/
def pauli (a : Vec3) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(a.2.2 : ℂ), (a.1 : ℂ) - I * (a.2.1 : ℂ);
     (a.1 : ℂ) + I * (a.2.1 : ℂ), -(a.2.2 : ℂ)]

/-- The lower eigenprojector P(n) = (1/2)(I - n·σ), written out entrywise. -/
def proj (n : Vec3) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(((1 - n.2.2) / 2 : ℝ) : ℂ), -((n.1 : ℂ) - I * (n.2.1 : ℂ)) / 2;
     -((n.1 : ℂ) + I * (n.2.1 : ℂ)) / 2, (((1 + n.2.2) / 2 : ℝ) : ℂ)]

/-- The derivative of P along a direction a in n-space: D(a) = -(1/2) a·σ. -/
def dproj (a : Vec3) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![-(a.2.2 : ℂ) / 2, -((a.1 : ℂ) - I * (a.2.1 : ℂ)) / 2;
     -((a.1 : ℂ) + I * (a.2.1 : ℂ)) / 2, (a.2.2 : ℂ) / 2]

def cross (a b : Vec3) : Vec3 :=
  (a.2.1 * b.2.2 - a.2.2 * b.2.1, a.2.2 * b.1 - a.1 * b.2.2, a.1 * b.2.1 - a.2.1 * b.1)

def dot (a b : Vec3) : ℝ := a.1 * b.1 + a.2.1 * b.2.1 + a.2.2 * b.2.2

/-- [a·σ, b·σ] = 2i (a×b)·σ. -/
theorem pauli_comm (a b : Vec3) :
    pauli a * pauli b - pauli b * pauli a = (2 * I) • pauli (cross a b) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pauli, cross, Matrix.mul_apply, Fin.sum_univ_two] <;>
    apply Complex.ext <;> simp <;> ring

/-- The projector is affine in n: P(n + h a) - P(n) = h D(a), with no remainder. -/
theorem proj_affine (n a : Vec3) (h : ℝ) :
    proj (n.1 + h * a.1, n.2.1 + h * a.2.1, n.2.2 + h * a.2.2) - proj n = (h : ℂ) • dproj a := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [proj, dproj] <;>
    apply Complex.ext <;> simp <;> ring

/-- The curvature identity, for arbitrary real vectors:
    i Tr( P(n) [D(a), D(b)] ) = (1/2) n·(a×b). -/
theorem curvature_formula (n a b : Vec3) :
    I * trace (proj n * (dproj a * dproj b - dproj b * dproj a)) =
      ((dot n (cross a b) / 2 : ℝ) : ℂ) := by
  simp [proj, dproj, dot, cross, Matrix.trace, Matrix.mul_apply, Fin.sum_univ_two]
  apply Complex.ext <;> simp <;> ring

/-- The unit direction n(θ,φ) = (sin θ cos φ, sin θ sin φ, cos θ). -/
def nvec (θ φ : ℝ) : Vec3 :=
  (Real.sin θ * Real.cos φ, Real.sin θ * Real.sin φ, Real.cos θ)

/-- ∂_θ n. -/
def dθn (θ φ : ℝ) : Vec3 :=
  (Real.cos θ * Real.cos φ, Real.cos θ * Real.sin φ, -Real.sin θ)

/-- ∂_φ n. -/
def dφn (θ φ : ℝ) : Vec3 :=
  (Real.sin θ * -Real.sin φ, Real.sin θ * Real.cos φ, 0)

theorem hasDerivAt_nvec_θ1 (θ φ : ℝ) :
    HasDerivAt (fun t => (nvec t φ).1) (dθn θ φ).1 θ := by
  simpa [nvec, dθn] using (Real.hasDerivAt_sin θ).mul_const (Real.cos φ)

theorem hasDerivAt_nvec_θ2 (θ φ : ℝ) :
    HasDerivAt (fun t => (nvec t φ).2.1) (dθn θ φ).2.1 θ := by
  simpa [nvec, dθn] using (Real.hasDerivAt_sin θ).mul_const (Real.sin φ)

theorem hasDerivAt_nvec_θ3 (θ φ : ℝ) :
    HasDerivAt (fun t => (nvec t φ).2.2) (dθn θ φ).2.2 θ := by
  simpa [nvec, dθn] using Real.hasDerivAt_cos θ

theorem hasDerivAt_nvec_φ1 (θ φ : ℝ) :
    HasDerivAt (fun t => (nvec θ t).1) (dφn θ φ).1 φ := by
  simpa [nvec, dφn] using (Real.hasDerivAt_cos φ).const_mul (Real.sin θ)

theorem hasDerivAt_nvec_φ2 (θ φ : ℝ) :
    HasDerivAt (fun t => (nvec θ t).2.1) (dφn θ φ).2.1 φ := by
  simpa [nvec, dφn] using (Real.hasDerivAt_sin φ).const_mul (Real.sin θ)

theorem hasDerivAt_nvec_φ3 (θ φ : ℝ) :
    HasDerivAt (fun t => (nvec θ t).2.2) (dφn θ φ).2.2 φ := by
  simpa [nvec, dφn] using hasDerivAt_const φ (Real.cos θ)

/-- n·(∂_θ n × ∂_φ n) = sin θ. -/
theorem triple_product (θ φ : ℝ) :
    dot (nvec θ φ) (cross (dθn θ φ) (dφn θ φ)) = Real.sin θ := by
  have h1 := Real.sin_sq_add_cos_sq θ
  have h2 := Real.sin_sq_add_cos_sq φ
  simp only [dot, cross, nvec, dθn, dφn]
  linear_combination (Real.sin θ * (Real.cos φ ^ 2 + Real.sin φ ^ 2)) * h1 + Real.sin θ * h2

/-- The curvature coefficient the monopole_stance archive took as its input. -/
def omega (θ : ℝ) : ℝ := Real.sin θ / 2

/-- Berry curvature of the lower Pauli eigenline:
    i Tr( P(n) [D(∂_θ n), D(∂_φ n)] ) = sin θ / 2. -/
theorem berry_curvature (θ φ : ℝ) :
    I * trace (proj (nvec θ φ) *
      (dproj (dθn θ φ) * dproj (dφn θ φ) - dproj (dφn θ φ) * dproj (dθn θ φ))) =
      ((omega θ : ℝ) : ℂ) := by
  rw [curvature_formula, triple_product]
  simp [omega]

/-- The curvature does not depend on φ, and vanishes only at the poles. -/
theorem berry_curvature_eq_zero_iff (θ : ℝ) : omega θ = 0 ↔ Real.sin θ = 0 := by
  unfold omega; constructor <;> intro h <;> linarith

/-- The complementary projector P₊ = I - P carries the opposite curvature:
    i Tr( P₊(n) [D(a), D(b)] ) = -(1/2) n·(a×b), since the derivatives of P₊ are
    minus those of P and the trace of a commutator vanishes. -/
theorem complement_curvature (n a b : Vec3) :
    I * trace ((1 - proj n) * (dproj a * dproj b - dproj b * dproj a)) =
      -((dot n (cross a b) / 2 : ℝ) : ℂ) := by
  simp [proj, dproj, dot, cross, Matrix.trace, Matrix.mul_apply, Fin.sum_univ_two,
    Matrix.one_apply]
  apply Complex.ext <;> simp <;> ring

end

end MonopoleStance
