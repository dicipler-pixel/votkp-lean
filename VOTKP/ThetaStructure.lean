/-
Conditional structural consequences for the theta invariant.

These are algebraic theorems about supplied functions and supplied laws.  This
file does not define knots, prove the connected-sum formula for the published
theta invariant, or prove its conjectural mirror/reversal laws.

Application to the research record:
* theta is Bar-Natan--van der Veen's two-variable invariant;
* weight K is Delta_K(T1) * Delta_K(T2) * Delta_K(T1*T2);
* sumLaw is their connected-sum formula (Fact 23);
* mirror antisymmetry and reversal invariance remain explicit hypotheses
  corresponding to Conjectures 21 and 22.

In a Laurent-polynomial application, nonvanishing of weight must be justified.
At a specialization where weight vanishes, the cancellation equivalence is not
available.  The record-factorization statements concern the mirror-composite
family only; they are not statements about all knots or unknotting number.
-/
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace VOTKP.ThetaStructure

variable {K R : Type*}

/-- The sum law and mirror-invariance of the weight expose the exact factor
that a mirror-composite cancellation test measures. -/
theorem mirror_sum_factor [CommRing R]
    (theta weight : K → R) (sum : K → K → K) (mirror : K → K)
    (sumLaw : ∀ a b, theta (sum a b) =
      theta a * weight b + weight a * theta b)
    (mirrorWeight : ∀ a, weight (mirror a) = weight a)
    (k : K) :
    theta (sum k (mirror k)) = weight k * (theta k + theta (mirror k)) := by
  rw [sumLaw, mirrorWeight]
  ring

/-- With a nonzero weight and no zero divisors, cancellation of the mirror
composite is equivalent to mirror antisymmetry at the original object.
Consequently, predicting cancellation from this formula is not independent
evidence for the mirror law. -/
theorem mirror_cancellation_iff_antisymmetry [CommRing R] [NoZeroDivisors R]
    (theta weight : K → R) (sum : K → K → K) (mirror : K → K)
    (sumLaw : ∀ a b, theta (sum a b) =
      theta a * weight b + weight a * theta b)
    (mirrorWeight : ∀ a, weight (mirror a) = weight a)
    (k : K) (weight_ne_zero : weight k ≠ 0) :
    theta (sum k (mirror k)) = 0 ↔ theta (mirror k) = -theta k := by
  rw [mirror_sum_factor theta weight sum mirror sumLaw mirrorWeight k]
  constructor
  · intro h
    have hz : theta k + theta (mirror k) = 0 :=
      (mul_eq_zero.mp h).resolve_left weight_ne_zero
    linear_combination hz
  · intro h
    rw [h]
    ring

/-- The universal cancellation claim has exactly the same strength as the
universal mirror law under the stated sum/weight hypotheses. -/
theorem all_mirror_cancellation_iff_antisymmetry
    [CommRing R] [NoZeroDivisors R]
    (theta weight : K → R) (sum : K → K → K) (mirror : K → K)
    (sumLaw : ∀ a b, theta (sum a b) =
      theta a * weight b + weight a * theta b)
    (mirrorWeight : ∀ a, weight (mirror a) = weight a)
    (weights_ne_zero : ∀ a, weight a ≠ 0) :
    (∀ k, theta (sum k (mirror k)) = 0) ↔
      (∀ k, theta (mirror k) = -theta k) := by
  constructor
  · intro h k
    exact (mirror_cancellation_iff_antisymmetry theta weight sum mirror
      sumLaw mirrorWeight k (weights_ne_zero k)).mp (h k)
  · intro h k
    exact (mirror_cancellation_iff_antisymmetry theta weight sum mirror
      sumLaw mirrorWeight k (weights_ne_zero k)).mpr (h k)

/-- Assuming the mirror law at k, the combined (Delta, theta) record of its
mirror composite is exactly (Delta(k)^2, 0).  No cancellation or nonzero
assumption is needed for this forward implication. -/
theorem mirror_composite_record {D : Type*} [Monoid D] [CommRing R]
    (delta : K → D) (theta weight : K → R) (sum : K → K → K) (mirror : K → K)
    (deltaSum : ∀ a b, delta (sum a b) = delta a * delta b)
    (deltaMirror : ∀ a, delta (mirror a) = delta a)
    (thetaSum : ∀ a b, theta (sum a b) =
      theta a * weight b + weight a * theta b)
    (mirrorWeight : ∀ a, weight (mirror a) = weight a)
    (k : K) (mirrorOddAt : theta (mirror k) = -theta k) :
    (delta (sum k (mirror k)), theta (sum k (mirror k))) =
      (delta k ^ 2, 0) := by
  apply Prod.ext
  · simp only [deltaSum, deltaMirror, pow_two]
  · rw [mirror_sum_factor theta weight sum mirror thetaSum mirrorWeight k,
      mirrorOddAt]
    ring

/-- On the mirror-composite family, the combined record factors through
Delta if the mirror law holds at both inputs.  This does not assert that
theta globally factors through Delta. -/
theorem mirror_composite_records_eq_of_delta_eq {D : Type*} [Monoid D] [CommRing R]
    (delta : K → D) (theta weight : K → R) (sum : K → K → K) (mirror : K → K)
    (deltaSum : ∀ a b, delta (sum a b) = delta a * delta b)
    (deltaMirror : ∀ a, delta (mirror a) = delta a)
    (thetaSum : ∀ a b, theta (sum a b) =
      theta a * weight b + weight a * theta b)
    (mirrorWeight : ∀ a, weight (mirror a) = weight a)
    (a b : K) (mirrorOddA : theta (mirror a) = -theta a)
    (mirrorOddB : theta (mirror b) = -theta b)
    (sameDelta : delta a = delta b) :
    (delta (sum a (mirror a)), theta (sum a (mirror a))) =
      (delta (sum b (mirror b)), theta (sum b (mirror b))) := by
  rw [mirror_composite_record delta theta weight sum mirror deltaSum
      deltaMirror thetaSum mirrorWeight a mirrorOddA,
    mirror_composite_record delta theta weight sum mirror deltaSum
      deltaMirror thetaSum mirrorWeight b mirrorOddB,
    sameDelta]

/-- The self-composite retains twice the weighted theta value. -/
theorem self_sum_theta [CommRing R]
    (theta weight : K → R) (sum : K → K → K)
    (sumLaw : ∀ a b, theta (sum a b) =
      theta a * weight b + weight a * theta b)
    (k : K) : theta (sum k k) = 2 * weight k * theta k := by
  rw [sumLaw]
  ring

/-- A nonzero theta value distinguishes the self-composite from the mirror
composite, conditionally on the mirror law.  In particular such a pair cannot
serve as an equal-(Delta,theta), different-target counterexample. -/
theorem self_sum_theta_ne_mirror_sum_theta
    [CommRing R] [NoZeroDivisors R]
    (theta weight : K → R) (sum : K → K → K) (mirror : K → K)
    (sumLaw : ∀ a b, theta (sum a b) =
      theta a * weight b + weight a * theta b)
    (mirrorWeight : ∀ a, weight (mirror a) = weight a)
    (two_ne_zero : (2 : R) ≠ 0)
    (k : K) (weight_ne_zero : weight k ≠ 0) (theta_ne_zero : theta k ≠ 0)
    (mirrorOddAt : theta (mirror k) = -theta k) :
    theta (sum k k) ≠ theta (sum k (mirror k)) := by
  rw [self_sum_theta theta weight sum sumLaw k,
    mirror_sum_factor theta weight sum mirror sumLaw mirrorWeight k,
    mirrorOddAt]
  simpa using mul_ne_zero (mul_ne_zero two_ne_zero weight_ne_zero) theta_ne_zero

/-- Direct inequalities against both mirror branches exclude either
symmetry, with no mirror or reversal law assumed.  The two witnesses may use
different evaluation points.  Applying this to knots still requires the
supplied equivalence relation and invariance law to model knot equivalence. -/
theorem direct_witnesses_exclude_unoriented_amphichirality
    {P : Type*} (equiv : K → K → Prop)
    (observe : K → P → R) (mirror reverse : K → K)
    (invariant : ∀ a b, equiv a b → ∀ p, observe a p = observe b p)
    (k : K) (p q : P)
    (mirrorWitness : observe k p ≠ observe (mirror k) p)
    (reverseMirrorWitness : observe k q ≠ observe (reverse (mirror k)) q) :
    ¬ (equiv k (mirror k) ∨ equiv k (reverse (mirror k))) := by
  intro h
  rcases h with hm | hrm
  · exact mirrorWitness (invariant k (mirror k) hm p)
  · exact reverseMirrorWitness (invariant k (reverse (mirror k)) hrm q)

/-- Deducing theta = 0 from either mirror branch uses both transformation
laws explicitly.  The branch `equiv k (mirror k)` needs only the mirror law;
the branch with a reversed mirror also uses reversal invariance.  The
condition 2 != 0 and absence of zero divisors make the final cancellation
valid. -/
theorem amphichiral_theta_zero_of_mirror_and_reversal_laws
    [CommRing R] [NoZeroDivisors R]
    (equiv : K → K → Prop) (theta : K → R) (mirror reverse : K → K)
    (invariant : ∀ a b, equiv a b → theta a = theta b)
    (mirrorOdd : ∀ a, theta (mirror a) = -theta a)
    (reverseEven : ∀ a, theta (reverse a) = theta a)
    (two_ne_zero : (2 : R) ≠ 0)
    (k : K) (amphichiral : equiv k (mirror k) ∨ equiv k (reverse (mirror k))) :
    theta k = 0 := by
  have hneg : theta k = -theta k := by
    rcases amphichiral with hm | hrm
    · exact (invariant k (mirror k) hm).trans (mirrorOdd k)
    · exact ((invariant k (reverse (mirror k)) hrm).trans
        (reverseEven (mirror k))).trans (mirrorOdd k)
  have htwice : (2 : R) * theta k = 0 := by
    linear_combination hneg
  exact (mul_eq_zero.mp htwice).resolve_left two_ne_zero

end VOTKP.ThetaStructure
