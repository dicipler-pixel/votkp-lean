/-
Prime Colour Transport, corpus bridges §5.3 / proof obligation OP01:
the predictive quotient for several permitted linear continuation actions.

This extends VOTKP.Observer's single-action result. A word is chronological:
the head acts first. No commutativity of actions is assumed. The action type
may be arbitrary; a finite alphabet is a special case. Finite-dimensionality
is used only for the finite stabilization bound.

These are theorems about a declared linear state, actions and record. They do
not supply that dictionary for a physical palette or a prime construction.
Developed with AI assistance for Jeromie Beasley's research programme.
-/
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Push

namespace VOTKP.MultiObserver

open Module

variable {K V Y W D : Type*} [Field K]
  [AddCommGroup V] [Module K V]
  [AddCommGroup Y] [Module K Y]
  [AddCommGroup W] [Module K W]

/-- Ordered action of a chronological word: its head acts first. -/
def wordMap (L : D → V →ₗ[K] V) : List D → V →ₗ[K] V
  | [] => LinearMap.id
  | d :: w => (wordMap L w).comp (L d)

/-- Unseen differences after inspecting all words of length at most `k`. -/
def unseenChain (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) : ℕ → Submodule K V
  | 0 => LinearMap.ker R
  | k + 1 => unseenChain L R k ⊓ ⨅ d, (unseenChain L R k).comap (L d)

/-- Differences that no permitted future word can distinguish. -/
def unseen (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) : Submodule K V :=
  ⨅ w : List D, LinearMap.ker (R.comp (wordMap L w))

lemma mem_unseen {L : D → V →ₗ[K] V} {R : V →ₗ[K] Y} {v : V} :
    v ∈ unseen L R ↔ ∀ w : List D, R (wordMap L w v) = 0 := by
  simp [unseen]

lemma chain_step_le (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (k : ℕ) :
    unseenChain L R (k + 1) ≤ unseenChain L R k := inf_le_left

lemma chain_le_ker (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (k : ℕ) :
    unseenChain L R k ≤ LinearMap.ker R := by
  induction k with
  | zero => exact le_rfl
  | succ k ih => exact le_trans (chain_step_le L R k) ih

/-- The recursive chain checks exactly the words up to its stated horizon. -/
theorem mem_chain_iff (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (k : ℕ) (v : V) :
    v ∈ unseenChain L R k ↔
      ∀ w : List D, w.length ≤ k → R (wordMap L w v) = 0 := by
  induction k generalizing v with
  | zero =>
    simp only [unseenChain, LinearMap.mem_ker]
    constructor
    · intro h w hw
      have : w = [] := List.length_eq_zero_iff.mp (by omega)
      subst w
      simpa [wordMap] using h
    · intro h
      simpa [wordMap] using h [] (by simp)
  | succ k ih =>
    simp only [unseenChain, Submodule.mem_inf, Submodule.mem_iInf,
      Submodule.mem_comap, ih]
    constructor
    · rintro ⟨h, hd⟩ w hw
      cases w with
      | nil => exact h [] (by simp)
      | cons d w =>
        simpa [wordMap] using hd d w (by simpa using hw)
    · intro h
      constructor
      · intro w hw
        exact h w (by omega)
      · intro d w hw
        simpa [wordMap] using h (d :: w) (by simpa using hw)

lemma unseen_le_chain (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (k : ℕ) :
    unseen L R ≤ unseenChain L R k := by
  intro v hv
  rw [mem_chain_iff]
  exact fun w _ => mem_unseen.mp hv w

/-- One equal pair of adjacent subspaces gives invariance under every action. -/
theorem stabilized_invariant (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (k : ℕ)
    (h : unseenChain L R (k + 1) = unseenChain L R k) (d : D)
    {v : V} (hv : v ∈ unseenChain L R k) : L d v ∈ unseenChain L R k := by
  have hs : v ∈ unseenChain L R (k + 1) := h.symm ▸ hv
  have hall : v ∈ ⨅ d, (unseenChain L R k).comap (L d) := hs.2
  exact (Submodule.mem_iInf _).mp hall d

/-- Stabilization certifies every future word, regardless of its length. -/
theorem stabilized_eq_unseen (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (k : ℕ)
    (h : unseenChain L R (k + 1) = unseenChain L R k) :
    unseenChain L R k = unseen L R := by
  apply le_antisymm
  · intro v hv
    rw [mem_unseen]
    intro w
    have keep : ∀ (w : List D) (v : V), v ∈ unseenChain L R k →
        wordMap L w v ∈ unseenChain L R k := by
      intro w
      induction w with
      | nil => intro v hv; simpa [wordMap] using hv
      | cons d w ih =>
        intro v hv
        exact ih (L d v) (stabilized_invariant L R k h d hv)
    exact LinearMap.mem_ker.mp (chain_le_ker L R k (keep w v hv))
  · exact unseen_le_chain L R k

/-- Equality of all future records is precisely equality modulo `unseen`. -/
theorem same_future_iff (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (v w : V) :
    (∀ u : List D, R (wordMap L u v) = R (wordMap L u w)) ↔
      v - w ∈ unseen L R := by
  simp only [mem_unseen, map_sub, sub_eq_zero]

/-- The all-word unseen space is invariant under every permitted action. -/
theorem unseen_invariant (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) (d : D)
    {v : V} (hv : v ∈ unseen L R) : L d v ∈ unseen L R := by
  rw [mem_unseen] at hv ⊢
  intro w
  simpa [wordMap] using hv (d :: w)

/-- Any summary that preserves the record and intertwines every action can
forget only all-word unseen directions. This is the quotient's minimality. -/
theorem summary_kernel (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y)
    (F : V →ₗ[K] W) (A : D → W →ₗ[K] W) (Q : W →ₗ[K] Y)
    (hFL : ∀ d, F.comp (L d) = (A d).comp F) (hR : R = Q.comp F) :
    LinearMap.ker F ≤ unseen L R := by
  intro v hv
  rw [LinearMap.mem_ker] at hv
  rw [mem_unseen]
  have intertwine : ∀ (w : List D) (v : V),
      F (wordMap L w v) = wordMap A w (F v) := by
    intro w
    induction w with
    | nil => intro v; rfl
    | cons d w ih =>
      intro v
      simp only [wordMap, LinearMap.comp_apply]
      have hh : F (L d v) = A d (F v) := LinearMap.congr_fun (hFL d) v
      rw [ih, hh]
  intro w
  rw [hR, LinearMap.comp_apply, intertwine, hv, map_zero, map_zero]

/-- The minimal quotient actually carries all induced actions and the record. -/
theorem quotient_is_summary (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) :
    ∃ (A : D → (V ⧸ unseen L R) →ₗ[K] (V ⧸ unseen L R))
      (Q : (V ⧸ unseen L R) →ₗ[K] Y),
      (∀ d, (unseen L R).mkQ.comp (L d) = (A d).comp (unseen L R).mkQ) ∧
      R = Q.comp (unseen L R).mkQ ∧
      LinearMap.ker (unseen L R).mkQ = unseen L R := by
  refine ⟨(fun d => (unseen L R).mapQ (unseen L R) (L d)
    (fun v hv => unseen_invariant L R d hv)),
    (unseen L R).liftQ R (fun v hv => LinearMap.mem_ker.mpr ?_), ?_, ?_,
    Submodule.ker_mkQ _⟩
  · simpa [wordMap] using mem_unseen.mp hv []
  · intro d
    exact (Submodule.mapQ_mkQ _ _ _).symm
  · exact (Submodule.liftQ_mkQ _ _ _).symm

/-- In finite dimension, an equal adjacent pair occurs by `dim (ker R)`.
Unlike a one-action Cayley–Hamilton argument this permits noncommuting actions. -/
theorem exists_stabilization [FiniteDimensional K V]
    (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) :
    ∃ k ≤ finrank K (LinearMap.ker R),
      unseenChain L R (k + 1) = unseenChain L R k := by
  by_contra hn
  push Not at hn
  have drop : ∀ k ≤ finrank K (LinearMap.ker R),
      finrank K (unseenChain L R (k + 1)) < finrank K (unseenChain L R k) := by
    intro k hk
    apply Submodule.finrank_lt_finrank_of_lt
    exact lt_of_le_of_ne (chain_step_le L R k) (hn k hk)
  have bound : ∀ k ≤ finrank K (LinearMap.ker R) + 1,
      finrank K (unseenChain L R k) + k ≤ finrank K (LinearMap.ker R) := by
    intro k
    induction k with
    | zero => intro _; simp only [unseenChain, Nat.add_zero]; exact le_rfl
    | succ k ih =>
      intro hk
      have hi := ih (by omega)
      have hd := drop k (by omega)
      omega
  have := bound (finrank K (LinearMap.ker R) + 1) le_rfl
  omega

/-- The stated finite horizon already equals the all-word predictive kernel. -/
theorem finite_horizon [FiniteDimensional K V]
    (L : D → V →ₗ[K] V) (R : V →ₗ[K] Y) :
    unseenChain L R (finrank K (LinearMap.ker R)) = unseen L R := by
  obtain ⟨k, hk, hs⟩ := exists_stabilization L R
  have mono : Antitone (unseenChain L R) :=
    antitone_nat_of_succ_le (chain_step_le L R)
  apply le_antisymm
  · rw [← stabilized_eq_unseen L R k hs]
    exact mono hk
  · exact unseen_le_chain L R _

/-- Exact three-coordinate control: the visible record is the first coordinate. -/
def controlRecord : (ℚ × ℚ × ℚ) →ₗ[ℚ] ℚ := LinearMap.fst ℚ ℚ (ℚ × ℚ)

/-- Transfer the middle coordinate into the visible one. -/
def controlA : (ℚ × ℚ × ℚ) →ₗ[ℚ] (ℚ × ℚ × ℚ) where
  toFun v := (v.2.1, 0, 0)
  map_add' := by intro v w; simp
  map_smul' := by intro a v; simp

/-- Transfer the last coordinate into the middle one. -/
def controlB : (ℚ × ℚ × ℚ) →ₗ[ℚ] (ℚ × ℚ × ℚ) where
  toFun v := (0, v.2.2, 0)
  map_add' := by intro v w; simp
  map_smul' := by intro a v; simp

def controlState : ℚ × ℚ × ℚ := (0, 0, 1)

def controlActions (d : Bool) : (ℚ × ℚ × ℚ) →ₗ[ℚ] (ℚ × ℚ × ℚ) :=
  if d then controlA else controlB

/-- Each action separately hides the state at every time, while the mixed word
`[B,A]` returns a visible value of one. Checking actions separately is insufficient. -/
theorem separate_actions_miss_mixed_word :
    (∀ k : ℕ, controlRecord ((controlA ^ k) controlState) = 0) ∧
    (∀ k : ℕ, controlRecord ((controlB ^ k) controlState) = 0) ∧
    controlRecord (wordMap controlActions [false, true] controlState) = 1 := by
  refine ⟨?_, ?_, ?_⟩
  · intro k
    cases k with
    | zero => norm_num [controlRecord, controlState]
    | succ k =>
      rw [pow_succ, Module.End.mul_apply]
      have hz : controlA controlState = 0 := by rfl
      rw [hz, map_zero, map_zero]
  · intro k
    cases k with
    | zero => norm_num [controlRecord, controlState]
    | succ k =>
      cases k with
      | zero => norm_num [controlRecord, controlState, controlB]
      | succ k =>
        rw [pow_succ, Module.End.mul_apply, pow_succ, Module.End.mul_apply]
        have hz : controlB (controlB controlState) = 0 := by rfl
        rw [hz, map_zero, map_zero]
  · norm_num [wordMap, controlActions, controlRecord, controlState, controlA, controlB]

end VOTKP.MultiObserver
