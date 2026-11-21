import Std

namespace VOTKP.FixedFace
open Lean.Grind Std

variable {K : Type} [Field K] [LE K] [LT K] [LawfulOrderLT K] [IsLinearOrder K]
  [OrderedRing K]

/-- t is the square-root clock, not the energy ratio z=t². -/
def partner (t : K) : K := (t+1)/(t-1)

private theorem clearPartner {t : K} (ht : 1 < t) :
    partner t * (t-1) = t+1 :=
  Field.div_mul_cancel (by grind)

/-- In the shifted clock coordinate the partner is reciprocal with numerator 2. -/
theorem reciprocal {t : K} (ht : 1 < t) : (t-1)*(partner t-1)=2 := by
  have h := clearPartner ht
  grind

theorem mapsForward {t : K} (ht : 1 < t) : 1 < partner t := by
  have h := reciprocal ht
  have h₁ : 0 < t-1 := by grind
  have hp : 0 < (t-1)*(partner t-1) := by rw [h]; grind
  have := OrderedRing.mul_pos_iff.mp hp
  grind

theorem partnerIff {t u : K} (ht : 1 < t) :
    u = partner t ↔ (t-1)*(u-1)=2 := by
  have h := reciprocal ht
  constructor
  · rintro rfl; exact h
  · intro h'
    have hn : t-1 ≠ 0 := by grind
    grind

theorem involution {t : K} (ht : 1 < t) : partner (partner t) = t := by
  apply Eq.symm
  apply (partnerIff (mapsForward ht)).mpr
  have h := reciprocal ht
  grind

theorem fixedIff {t : K} (ht : 1 < t) : partner t = t ↔ t^2 - 2*t-1=0 := by
  rw [eq_comm, partnerIff ht]
  grind

/-- Exact finite-change sensitivity, valid for both orders and for t=u. -/
theorem sensitivity {t u : K} (ht : 1 < t) (hu : 1 < u) :
    (partner t - partner u) * ((t-1)*(u-1)) = 2*(u-t) := by
  have h := clearPartner ht
  have h' := clearPartner hu
  grind

theorem strictlyReverses {t u : K} (ht : 1 < t) (htu : t < u) : partner u < partner t := by
  have hu : 1 < u := by grind
  have h := sensitivity ht hu
  have hd := OrderedRing.mul_pos (a := t-1) (b := u-1) (by grind) (by grind)
  have hr := OrderedRing.mul_pos (a := (2:K)) (b := u-t) (by grind) (by grind)
  have hprod : 0 < (partner t - partner u) * ((t-1)*(u-1)) := by rw [h]; exact hr
  have := OrderedRing.mul_pos_iff.mp hprod
  grind

/-- The previously used squared mixed-face score, for input ratios t² and u². -/
def mixedScore (t u : K) : K :=
  (t^2-1)^2*(u^2-1)^2-16*t^2*u^2

/-- Two positive factors carry the displaced partner clock into the old score. -/
private theorem positiveFactors {t u : K} (ht : 1<t) (hu : 1<u) :
    0 < (t*u+t+u-1) * ((t^2-1)*(u^2-1)+4*t*u) := by
  have htu := OrderedRing.mul_pos (a:=t) (b:=u) (by grind) (by grind)
  have ht2 := OrderedRing.mul_pos (a:=t-1) (b:=t+1) (by grind) (by grind)
  have hu2 := OrderedRing.mul_pos (a:=u-1) (b:=u+1) (by grind) (by grind)
  have h₂ := OrderedRing.mul_pos (a:=t^2-1) (b:=u^2-1) (by grind) (by grind)
  apply OrderedRing.mul_pos <;> grind

private theorem positiveFactorization {t u : K} (ht : 1<t) :
    mixedScore t u = (u-partner t) *
      ((t-1) * ((t*u+t+u-1)*((t^2-1)*(u^2-1)+4*t*u))) := by
  have h := clearPartner ht
  unfold mixedScore
  grind

/-- This characterizes all three strict/ideal outcomes in the same order
as displacement of the observed partner u from the critical partner. -/
theorem mixedScoreSigns {t u : K} (ht : 1<t) (hu : 1<u) :
    (mixedScore t u < 0 ↔ u < partner t) ∧
    (mixedScore t u = 0 ↔ u = partner t) ∧
    (0 < mixedScore t u ↔ partner t < u) := by
  rw [positiveFactorization ht]
  have hp := OrderedRing.mul_pos (a:=t-1) (by grind) (positiveFactors ht hu)
  have := OrderedRing.mul_pos_iff (a:=u-partner t)
    (b:=((t-1) * ((t*u+t+u-1)*((t^2-1)*(u^2-1)+4*t*u))))
  have := OrderedRing.mul_pos_iff (a:=partner t-u)
    (b:=((t-1) * ((t*u+t+u-1)*((t^2-1)*(u^2-1)+4*t*u))))
  grind

/-- A positive square root of two determines the forward equal-face clock and
its original energy-ratio coordinate. This assumes only the stated root, so
fields lacking such a root acquire no spurious existence claim. -/
theorem positiveRootFixedClock {s : K} (hs : 0<s) (hr : s^2=2) :
    partner (1+s)=1+s ∧ (1+s)^2=3+2*s := by
  constructor
  · apply (fixedIff (t:=1+s) (by grind)).mpr
    grind
  · grind

/-- A rectangular uncertainty interval needs two corner tests because the
partner clock decreases. These implications use strict inequalities throughout. -/
theorem boxMargins {t0 t t1 u0 u u1 : K} (ht0 : 1<t0) (htl : t0≤t)
    (hth : t≤t1) (hu0 : 1<u0) (hul : u0≤u) (huh : u≤u1) :
    (partner t0 < u0 → 0 < mixedScore t u) ∧
    (u1 < partner t1 → mixedScore t u < 0) := by
  have ht : 1<t := by grind
  have hu : 1<u := by grind
  have hl : partner t ≤ partner t0 := by
    by_cases he : t=t0
    · grind
    · have := strictlyReverses ht0 (show t0<t by grind); grind
  have hh : partner t1 ≤ partner t := by
    by_cases he : t=t1
    · grind
    · have := strictlyReverses ht (show t<t1 by grind); grind
  have h := mixedScoreSigns ht hu
  grind

/-- Exact countercontrol to treating the partner map as increasing. -/
theorem order_control : (2 : Rat)<3 ∧ partner (2:Rat)=3 ∧ partner (3:Rat)=2 ∧
    ¬ (partner (2:Rat)<partner (3:Rat)) := by decide +kernel

/-- The finite sensitivity has no constant slope: t=2 to 3 has slope −1;
t=3 to 4 has slope −1/3. -/
theorem nonlinear_control : partner (3:Rat)-partner 2 = -1 ∧
    partner (4:Rat)-partner 3 = -1/3 := by decide +kernel

#print axioms reciprocal
#print axioms mapsForward
#print axioms partnerIff
#print axioms involution
#print axioms fixedIff
#print axioms sensitivity
#print axioms strictlyReverses
#print axioms mixedScoreSigns
#print axioms positiveRootFixedClock
#print axioms boxMargins
#print axioms order_control
#print axioms nonlinear_control

end VOTKP.FixedFace
