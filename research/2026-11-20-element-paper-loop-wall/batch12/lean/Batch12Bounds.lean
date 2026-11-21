import MarginBounds
import AntimonyCesium

namespace ElementPaper.Batch12

open VOTKP.NearestPair

/-- Archive central value and stated absolute uncertainty, both in eV. -/
abbrev Reading := Rat × Rat

def face (a b : Reading) : Face := ⟨a.1, a.2, b.1, b.2⟩

def faces (xs : List Reading) : List Face :=
  (xs.zip xs.tail).map (fun (a,b) => face a b)

def endpointLo (f : Face) : Rat := (f.b-f.ub)/(f.a+f.ua)
def endpointHi (f : Face) : Rat := (f.b+f.ub)/(f.a-f.ua)

private theorem ratioMono {a b c d : Rat} (hc : 0<c) (hb : 0<b)
    (hca : c≤a) (hbd : b≤d) : b/a ≤ d/c := by
  have ha : 0<a := by grind
  have X := Rat.mul_le_mul_of_nonneg_right hca (show 0≤b by grind)
  have Y := Rat.mul_le_mul_of_nonneg_right hbd (show 0≤a by grind)
  by_cases h : b/a ≤ d/c
  · exact h
  have hp := (Rat.lt_div_iff ha).mp (show d/c < b/a by grind)
  have hz := Rat.mul_lt_mul_of_pos_right hp hc
  have eq : (d/c*a)*c = d*a := by
    calc
      (d/c*a)*c = (d/c*c)*a := by grind
      _ = d*a := by rw [Rat.div_mul_cancel (by grind)]
  rw [eq] at hz
  grind

/-- Ratios of all positive rational realizations lie in the rectangle's corner interval. -/
theorem ratioBounds {f : Face} (ok : valid f = true) {a b : Rat} (h : Admits f a b) :
    endpointLo f ≤ b/a ∧ b/a ≤ endpointHi f := by
  simp only [valid, decide_eq_true_eq] at ok
  obtain ⟨ha,hA,hb,hB⟩ := h
  constructor
  · exact ratioMono (by grind) ok.2.1 hA hb
  · exact ratioMono ok.1 (by grind) ha hB

def admitsInside (f : Face) : Bool := valid f && decide (pHi f < (1:Rat)/2)
def admitsOutside (f : Face) : Bool := valid f && decide ((1:Rat)/2 < pLo f)

theorem interiorForEveryRealization {f : Face} (ok : admitsInside f = true)
    {a b : Rat} (h : Admits f a b) : power a b < (1:Rat)/2 := by
  simp [admitsInside] at ok
  have hbound := (powerBounds ok.1 h).2
  grind

theorem exteriorForEveryRealization {f : Face} (ok : admitsOutside f = true)
    {a b : Rat} (h : Admits f a b) : (1:Rat)/2 < power a b := by
  simp [admitsOutside] at ok
  have hbound := (powerBounds ok.1 h).1
  grind

/-- The entire reference-power interval lies above every other interval. -/
def ranked (fs : List Face) (reference : Face) : Bool :=
  valid reference && fs.all (fun f => valid f && decide (pHi f < pLo reference))

theorem strictRankForEveryRealization {fs : List Face} {reference f : Face}
    (ok : ranked fs reference = true) (hf : f ∈ fs)
    {a b c d : Rat} (h : Admits f a b) (k : Admits reference c d) :
    power a b < power c d := by
  simp only [ranked, Bool.and_eq_true] at ok
  have row := List.all_eq_true.mp ok.2 f hf
  simp only [Bool.and_eq_true, decide_eq_true_eq] at row
  have lo := (powerBounds row.1 h).2
  have hi := (powerBounds ok.1 k).1
  grind

/-- Pearson finite-difference hardness and Mulliken electronegativity at the anion rung. -/
def eta (ea ie : Rat) : Rat := (ie-ea)/2
def chi (ea ie : Rat) : Rat := (ie+ea)/2
def omega (ea ie : Rat) : Rat := (chi ea ie)^2/(2*eta ea ie)

def chemistryOutside (f : Face) : Bool :=
  decide (0 < f.a ∧ f.a < f.b ∧ 0 < eta f.a f.b ∧
    g f.a f.b = eta f.a f.b / chi f.a f.b ∧
    omega f.a f.b / eta f.a f.b = 1/(2*power f.a f.b) ∧
    omega f.a f.b < eta f.a f.b)

def centralPairs (xs : List Reading) : List (Rat × Rat) :=
  let es := xs.map Prod.fst
  es.zip es.tail

def kFace (xs : List Reading) (z : Nat) : Face :=
  face (xs[z-3]!) (xs[z-2]!)

def nonKFaces (xs : List Reading) (z : Nat) : List Face :=
  ((faces xs).zipIdx.filter (fun p => p.2 != z-3)).map Prod.fst

def tiesForward (xs : List Reading) : List Nat :=
  (faces xs).zipIdx.filterMap (fun (f,i) => if endpointLo f ≤ 1 then some (i+1) else none)

end ElementPaper.Batch12
