/-
Colour records, surviving matches, and retained mixture amount.

Sources:
* Jeromie Beasley, VOTKP v2.9, §6.2 and Appendix A.13 (surviving matches).
* Prime Colour Transport, research edition 1 November 2026, independent review §6,
  obligation CO04 (absolute mixture amounts and reduced records).

The linear closure equivalence reuses `VOTKP.Observer.closes_iff`. The finite-spectrum
witness below adds the admissibility step: a lost kernel direction can be realized by
two reflectances in [0,1], not just by an unrestricted signed vector.

The mixture results concern declared additive channels, normalized by their total.
They do not identify a perceptual colour metric, certify optical datasets, or assert a
paint law. The newer affine Z/9 palette and decimal Z/10 quarter-turn are distinct
constructions; neither is silently substituted for the channel model here.
Developed with AI assistance.
-/
import VOTKP.Observer

namespace VOTKP.Colour

open Module

section LinearRecords

variable {K V Y : Type*} [Field K]
  [AddCommGroup V] [Module K V]
  [AddCommGroup Y] [Module K Y]

/-- Every pair matched by the first receiver stays matched after the declared operation. -/
def PreservesMatches (C : V →ₗ[K] Y) (M : V →ₗ[K] V) : Prop :=
  ∀ x y, C x = C y → C (M x) = C (M y)

/-- Surviving matches are exactly invariance of the receiver's invisible directions. -/
theorem preservesMatches_iff_kernel (C : V →ₗ[K] Y) (M : V →ₗ[K] V) :
    PreservesMatches C M ↔ ∀ v, C v = 0 → C (M v) = 0 := by
  constructor
  · intro h v hv
    simpa using h v 0 (by simpa using hv)
  · intro h x y hxy
    have hv : C (x - y) = 0 := by rw [map_sub, hxy, sub_self]
    have := h (x - y) hv
    simpa only [map_sub, sub_eq_zero] using this

/-- A later colour record is determined by the current record exactly when it factors
through that record. This applies the existing finite-observer closure theorem. -/
theorem preservesMatches_iff_factors [FiniteDimensional K V]
    (C : V →ₗ[K] Y) (M : V →ₗ[K] V) :
    PreservesMatches C M ↔ ∃ T : Y →ₗ[K] Y, C ∘ₗ M = T ∘ₗ C := by
  rw [preservesMatches_iff_kernel]
  exact (Observer.closes_iff M C).symm

/-- The `CMP = 0` test only needs a map with range exactly `ker C`; orthogonality is
unnecessary. An orthogonal projector onto `ker C` is one permitted choice. -/
theorem preservesMatches_iff_projected_zero (C : V →ₗ[K] Y) (M P : V →ₗ[K] V)
    (hP : LinearMap.range P = LinearMap.ker C) :
    PreservesMatches C M ↔ (C ∘ₗ M) ∘ₗ P = 0 := by
  rw [preservesMatches_iff_kernel]
  constructor
  · intro h
    ext v
    apply h
    apply LinearMap.mem_ker.mp
    rw [← hP]
    exact LinearMap.mem_range_self P v
  · intro h v hv
    have hvP : v ∈ LinearMap.range P := by
      rw [hP]
      exact LinearMap.mem_ker.mpr hv
    obtain ⟨u, rfl⟩ := hvP
    simpa only [LinearMap.comp_apply, LinearMap.zero_apply] using LinearMap.congr_fun h u

/-- A spectrally neutral scalar filter preserves every match. -/
theorem neutral_preservesMatches (C : V →ₗ[K] Y) (c : K) :
    PreservesMatches C (c • LinearMap.id) := by
  rw [preservesMatches_iff_kernel]
  intro v hv
  simp [hv]

end LinearRecords

section BoundedSpectra

variable {ι Y : Type*} [Fintype ι]
  [AddCommGroup Y] [Module ℝ Y]

/-- A finite reflectance spectrum is bounded at every sampled wavelength. -/
def InUnitCube (x : ι → ℝ) : Prop := ∀ i, 0 ≤ x i ∧ x i ≤ 1

/-- Any invisible direction that becomes visible after `M` has a bounded metamer
witness. The construction uses a flat one-half baseline and a sufficiently small
nonzero multiple of the direction. It certifies no particular material or dataset. -/
theorem bounded_metamer_of_hidden (C : (ι → ℝ) →ₗ[ℝ] Y)
    (M : (ι → ℝ) →ₗ[ℝ] (ι → ℝ)) (v : ι → ℝ)
    (hv : C v = 0) (hMv : C (M v) ≠ 0) :
    ∃ x y : ι → ℝ, InUnitCube x ∧ InUnitCube y ∧ C x = C y ∧ C (M x) ≠ C (M y) := by
  classical
  let B : ℝ := 1 + ∑ i, |v i|
  have hB : 0 < B := by
    have hs : 0 ≤ ∑ i, |v i| := Finset.sum_nonneg (fun i _ => abs_nonneg (v i))
    dsimp [B]
    linarith
  let t : ℝ := 1 / (2 * B)
  have ht : 0 < t := by dsimp [t]; positivity
  have htB : t * B = 1 / 2 := by
    dsimp [t]
    field_simp [hB.ne']
  have hbound (i : ι) : -(1 / 2 : ℝ) ≤ t * v i ∧ t * v i ≤ 1 / 2 := by
    have hi : |v i| ≤ ∑ j, |v j| :=
      Finset.single_le_sum (fun j _ => abs_nonneg (v j)) (Finset.mem_univ i)
    have hu : v i ≤ B := by
      have := le_abs_self (v i)
      dsimp [B]
      linarith
    have hl : -B ≤ v i := by
      have := neg_abs_le (v i)
      dsimp [B]
      linarith
    have htu := mul_le_mul_of_nonneg_left hu ht.le
    have htl := mul_le_mul_of_nonneg_left hl ht.le
    constructor <;> nlinarith
  let y : ι → ℝ := fun _ => 1 / 2
  let x : ι → ℝ := fun i => 1 / 2 + t * v i
  have hxy : x - y = t • v := by
    ext i
    simp [x, y]
  refine ⟨x, y, ?_, ?_, ?_, ?_⟩
  · intro i
    have := hbound i
    dsimp [x]
    constructor <;> linarith
  · intro i
    norm_num [y]
  · apply sub_eq_zero.mp
    rw [← map_sub, hxy, map_smul, hv, smul_zero]
  · intro heq
    have hzero : C (M (x - y)) = 0 := by rw [map_sub, map_sub, heq, sub_self]
    rw [hxy, map_smul, map_smul] at hzero
    exact (smul_ne_zero ht.ne' hMv) hzero

/-- Restricting tests to valid bounded spectra loses none of the universal
factorization criterion: every failure has a witness inside the reflectance cube. -/
theorem bounded_matches_iff_factors (C : (ι → ℝ) →ₗ[ℝ] Y)
    (M : (ι → ℝ) →ₗ[ℝ] (ι → ℝ)) :
    (∀ x y, InUnitCube x → InUnitCube y → C x = C y → C (M x) = C (M y)) ↔
      ∃ T : Y →ₗ[ℝ] Y, C ∘ₗ M = T ∘ₗ C := by
  rw [← preservesMatches_iff_factors, preservesMatches_iff_kernel]
  constructor
  · intro h v hv
    by_contra hMv
    obtain ⟨x, y, hx, hy, hxy, hMxy⟩ := bounded_metamer_of_hidden C M v hv hMv
    exact hMxy (h x y hx hy hxy)
  · intro h x y _ _ hxy
    exact (preservesMatches_iff_kernel C M).mpr h x y hxy

end BoundedSpectra

section MixtureAmount

variable {ι : Type*} [Fintype ι]

/-- Total amount in the declared additive channel model. -/
noncomputable def amount (x : ι → ℝ) : ℝ := ∑ i, x i

/-- The normalized channel record forgets overall amount. -/
noncomputable def normalized (x : ι → ℝ) : ι → ℝ := fun i => x i / amount x

/-- The amount ledger is additive. -/
theorem amount_add (x u : ι → ℝ) : amount (x + u) = amount x + amount u := by
  simp [amount, Finset.sum_add_distrib]

/-- Retaining amount repairs normalization: it reconstructs the complete channel state. -/
theorem amount_normalized_reconstruct (x : ι → ℝ) (hx : amount x ≠ 0) :
    amount x • normalized x = x := by
  ext i
  simp only [Pi.smul_apply, smul_eq_mul, normalized]
  field_simp [hx]

/-- Equality of normalized record and nonzero total amount forces equality of the
original mixtures; this is a genuine retained-state statement, not just one example. -/
theorem normalized_amount_injective (x y : ι → ℝ)
    (hx : amount x ≠ 0) (hy : amount y ≠ 0)
    (hrecord : normalized x = normalized y) (hamount : amount x = amount y) : x = y := by
  calc
    x = amount x • normalized x := (amount_normalized_reconstruct x hx).symm
    _ = amount y • normalized y := by rw [hamount, hrecord]
    _ = y := amount_normalized_reconstruct y hy

/-- A retained normalized record plus amount predicts every declared absolute addition.
The added vector is in absolute units, not an input mixing fraction. This algebraic
identity uses totalized division; its normalized-mixture interpretation requires
nonnegative channels and positive output amount. -/
theorem normalized_add_from_record (x u : ι → ℝ) (hx : amount x ≠ 0) :
    normalized (x + u) =
      fun i => (amount x * normalized x i + u i) / (amount x + amount u) := by
  ext i
  have hrec := congrFun (amount_normalized_reconstruct x hx) i
  simp only [Pi.smul_apply, smul_eq_mul] at hrec
  simp only [normalized, Pi.add_apply, amount_add]
  rw [show amount x * (x i / amount x) = x i from hrec]

/-- The source's exact CO04 example: two positive mixtures match under normalization
but separate after addition of the same fixed absolute amount. -/
theorem normalized_absolute_addition_witness :
    normalized (![1, 1] : Fin 2 → ℝ) = normalized (![2, 2] : Fin 2 → ℝ) ∧
    normalized ((![1, 1] : Fin 2 → ℝ) + ![1, 0]) ≠
      normalized ((![2, 2] : Fin 2 → ℝ) + ![1, 0]) := by
  constructor
  · ext i
    fin_cases i <;> norm_num [normalized, amount, Fin.sum_univ_two]
  · intro h
    have := congrFun h 0
    norm_num [normalized, amount, Fin.sum_univ_two] at this

/-- No function of normalized colour alone predicts this permitted absolute addition,
even when inputs are restricted to nonnegative mixtures with positive total amount. -/
theorem no_normalized_only_absolute_update :
    ¬ ∃ F : (Fin 2 → ℝ) → (Fin 2 → ℝ),
      ∀ x : Fin 2 → ℝ, (∀ i, 0 ≤ x i) → 0 < amount x →
        F (normalized x) = normalized (x + ![1, 0]) := by
  rintro ⟨F, hF⟩
  have hx := hF (![1, 1]) (by intro i; fin_cases i <;> norm_num)
    (by norm_num [amount, Fin.sum_univ_two])
  have hy := hF (![2, 2]) (by intro i; fin_cases i <;> norm_num)
    (by norm_num [amount, Fin.sum_univ_two])
  obtain ⟨hmatch, hsplit⟩ := normalized_absolute_addition_witness
  exact hsplit (hx.symm.trans ((congrArg F hmatch).trans hy))

end MixtureAmount

end VOTKP.Colour
