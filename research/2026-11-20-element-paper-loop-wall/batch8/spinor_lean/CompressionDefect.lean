import Std

namespace VOTKP.SpinorPeel

open Lean.Grind

variable {R : Type} [Ring R]

private theorem leftDiff (a b c : R) : (a-b)*c = a*c-b*c := by
  simp only [Ring.sub_eq_add_neg, Semiring.right_distrib, Ring.neg_mul]

private theorem rightDiff (a b c : R) : a*(b-c) = a*b-a*c := by
  simp only [Ring.sub_eq_add_neg, Semiring.left_distrib, Ring.mul_neg]

private theorem contract {e : R} (he : e*e = e) (b : R) : e*(e*b) = e*b := by
  rw [← Semiring.mul_assoc, he]

/-- Compressing A² differs from squaring the compression by the discarded middle block.
Multiplication need not commute. Only the retained projection is idempotent. -/
theorem compression_of_square (e A : R) (he : e*e = e) :
    e * A^2 * e - (e*A*e)^2 = e*A*(1-e)*A*e := by
  simp only [Semiring.pow_two, leftDiff, rightDiff, Semiring.mul_one,
    Semiring.mul_assoc, contract he]

/-- Specializing the observable to a projection gives the on-site projector deficit. -/
theorem projector_compression (e P : R) (he : e*e = e) (hP : P*P = P) :
    e*P*e - (e*P*e)^2 = e*P*(1-e)*P*e := by
  simpa only [Semiring.pow_two, hP] using compression_of_square e P he

/-- The dagger laws used here hold for Hilbert adjoints and conjugate transposes. -/
structure Adjoint (R : Type) [Ring R] where
  apply : R → R
  involutive : ∀ x, apply (apply x) = x
  reverseProduct : ∀ x y, apply (x*y) = apply y * apply x
  subtract : ∀ x y, apply (x-y) = apply x - apply y
  one : apply 1 = 1

private theorem complement_idempotent (e : R) (he : e*e = e) :
    (1-e)*(1-e) = (1-e) := by
  rw [leftDiff, Semiring.one_mul, rightDiff, Semiring.mul_one, he]
  grind

/-- For self-adjoint retention and observable, the defect is L†L for the leakage
L = (1−e)Ae. This is an algebraic factorization in the ambient ring. -/
theorem squared_leakage (adj : Adjoint R) (e A : R)
    (he : e*e = e) (ese : adj.apply e = e) (ase : adj.apply A = A) :
    e*A^2*e - (e*A*e)^2 =
      adj.apply ((1-e)*A*e) * ((1-e)*A*e) := by
  rw [compression_of_square e A he]
  simp only [adj.reverseProduct, adj.subtract, adj.one, ese, ase,
    Semiring.mul_assoc, contract (complement_idempotent e he)]

/-- With an occupied projector P, the same squared leakage is C−C², C=ePe. -/
theorem projector_squared_leakage (adj : Adjoint R) (e P : R)
    (he : e*e = e) (hP : P*P = P) (ese : adj.apply e = e) (pse : adj.apply P = P) :
    e*P*e - (e*P*e)^2 =
      adj.apply ((1-e)*P*e) * ((1-e)*P*e) := by
  simpa only [Semiring.pow_two, hP] using squared_leakage adj e P he ese pse

/-- On the one-dimensional rational space take the identity retention e=1 and
P=2. There is zero leakage, but the proposed projected deficit is −2. -/
theorem nonidempotent_observable_control :
    let e : Rat := 1
    let P : Rat := 2
    e*e=e ∧ P*P ≠ P ∧ e*P*e - (e*P*e)^2 = -2 ∧
    e*P*(1-e)*P*e = 0 ∧ e*P*e - (e*P*e)^2 ≠ e*P*(1-e)*P*e := by
  decide +kernel

/-- An additive cyclic signed trace, e.g. Im Tr for complex matrices. The
scalar codomain has no nonzero element equal to its own negative. -/
structure SignedTrace {S : Type} [Ring S] (adj : Adjoint R) where
  apply : R → S
  additive : ∀ x y, apply (x+y) = apply x + apply y
  cyclic : ∀ x y, apply (x*y) = apply (y*x)
  oddAdjoint : ∀ x, apply (adj.apply x) = - apply x
  noTwoTorsion : ∀ s : S, s = -s → s = 0

private theorem signedPairZero {S : Type} [Ring S] {adj : Adjoint R}
    (tr : SignedTrace (S := S) adj) (x y : R)
    (hx : adj.apply x = x) (hy : adj.apply y = y) : tr.apply (x*y) = 0 := by
  apply tr.noTwoTorsion
  calc
    tr.apply (x*y) = tr.apply (y*x) := tr.cyclic x y
    _ = tr.apply (adj.apply (x*y)) := by rw [adj.reverseProduct, hx, hy]
    _ = -tr.apply (x*y) := tr.oddAdjoint _

/-- With exactly three sites resolving the identity, the signed distinct-site
projector triangle vanishes. The algebra only needs the three summands to
sum to 1 and the first two to be self-adjoint; orthogonal site projections
satisfy these hypotheses. -/
theorem signed_triangle_three_sites {S : Type} [Ring S] (adj : Adjoint R)
    (tr : SignedTrace (S := S) adj) (P e f g : R) (sumSites : e+f+g=1)
    (hP : P*P=P) (sP : adj.apply P=P) (se : adj.apply e=e) (sf : adj.apply f=f) :
    tr.apply (e*P*f*P*g*P) = 0 := by
  have htotal : tr.apply (e*P*f*P*(e+f+g)*P) = 0 := by
    rw [sumSites, Semiring.mul_one, Semiring.mul_assoc (e*P*f), hP]
    rw [Semiring.mul_assoc e P f, Semiring.mul_assoc e _ P]
    apply signedPairZero tr e _ se
    simp only [adj.reverseProduct, sP, sf, Semiring.mul_assoc]
  have hfirst : tr.apply (e*P*f*P*e*P) = 0 := by
    apply signedPairZero tr _ P _ sP
    simp only [adj.reverseProduct, se, sf, sP, Semiring.mul_assoc]
  have hsecond : tr.apply (e*P*f*P*f*P) = 0 := by
    simp only [Semiring.mul_assoc]
    apply signedPairZero tr e _ se
    simp only [adj.reverseProduct, sf, sP, Semiring.mul_assoc]
  have hzero (x : S) : 0+x=x := (Semiring.add_comm 0 x).trans (Semiring.add_zero x)
  simpa only [Semiring.left_distrib, Semiring.right_distrib, tr.additive,
    hfirst, hsecond, Semiring.add_zero, hzero] using htotal

#print axioms compression_of_square
#print axioms projector_compression
#print axioms squared_leakage
#print axioms projector_squared_leakage
#print axioms nonidempotent_observable_control
#print axioms signed_triangle_three_sites

end VOTKP.SpinorPeel
