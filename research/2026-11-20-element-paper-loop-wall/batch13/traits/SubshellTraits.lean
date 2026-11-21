/- Aligned subshell counts. Each pair gives the occupation before and after the peel. -/
import Std

namespace VOTKP.SubshellTraits

abbrev Counts := List (Nat × Nat)

def before (v : Counts) : Nat := (v.map Prod.fst).sum
def after (v : Counts) : Nat := (v.map Prod.snd).sum
def kept (v : Counts) : Nat := (v.map (fun (x,y) => min x y)).sum
def gained (v : Counts) : Nat := (v.map (fun (x,y) => y-x)).sum
def lost (v : Counts) : Nat := (v.map (fun (x,y) => x-y)).sum
def distance (v : Counts) : Nat := (v.map (fun (x,y) => (x-y)+(y-x))).sum

theorem after_decomposes (v : Counts) : after v = kept v + gained v := by
  induction v with
  | nil => rfl
  | cons p tail ih =>
    rcases p with ⟨a,b⟩
    simp [after, kept, gained] at ih ⊢
    omega

theorem before_decomposes (v : Counts) : before v = kept v + lost v := by
  induction v with
  | nil => rfl
  | cons p tail ih =>
    rcases p with ⟨a,b⟩
    simp [before, kept, lost] at ih ⊢
    omega

theorem distance_decomposes (v : Counts) : distance v = lost v + gained v := by
  induction v with
  | nil => rfl
  | cons p tail ih =>
    rcases p with ⟨a,b⟩
    simp [distance, lost, gained] at ih ⊢
    omega

theorem peel_identity (v : Counts) (net : before v = after v + 1) :
    lost v = gained v + 1 ∧
    distance v = 2 * gained v + 1 ∧
    (distance v - 1) / 2 = gained v ∧
    after v - kept v = gained v := by
  have a := after_decomposes v
  have b := before_decomposes v
  have d := distance_decomposes v
  omega

theorem pure_removal (v : Counts) (net : before v = after v + 1) :
    gained v = 0 ↔ distance v = 1 := by
  have h := (peel_identity v net).2.1
  omega

#print axioms after_decomposes
#print axioms before_decomposes
#print axioms distance_decomposes
#print axioms peel_identity
#print axioms pure_removal
end VOTKP.SubshellTraits
