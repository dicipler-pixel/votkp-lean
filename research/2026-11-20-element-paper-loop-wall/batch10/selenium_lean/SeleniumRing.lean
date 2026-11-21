import Std

namespace VOTKP.SeleniumRing

/-- Fractional crystallographic coordinates and their errors are stored as
integer multiples of 1/100000. The determinant consequently scales by 10¹⁰. -/
abbrev scale : Int := 100000
structure Interval where
  lo : Int
  hi : Int
  deriving DecidableEq, Repr, Inhabited
structure Site where
  x : Interval
  y : Interval
  z : Interval
  deriving DecidableEq, Repr, Inhabited

def band (a error : Int) : Interval := ⟨a-error,a+error⟩

-- BEGIN CIF VALUES
def sites : List Site :=
  [⟨band 6355 10, band 68641 11, band 91290 7⟩,
   ⟨band 25586 11, band 77285 11, band 102241 8⟩,
   ⟨band 25827 11, band 60084 11, band 116858 7⟩,
   ⟨band 44886 10, band 41857 11, band 114620 7⟩,
   ⟨band 34045 11, band 17089 11, band 109083 7⟩,
   ⟨band 35943 10, band 16250 11, band 90960 7⟩,
   ⟨band 13558 10, band 24704 12, band 84010 7⟩,
   ⟨band 16495 11, band 52018 13, band 78818 7⟩]
-- END CIF VALUES

def sub (a b : Interval) : Interval := ⟨a.lo-b.hi, a.hi-b.lo⟩
def mul (a b : Interval) : Interval :=
  let u := a.lo*b.lo
  let v := a.lo*b.hi
  let w := a.hi*b.lo
  let x := a.hi*b.hi
  ⟨min (min u v) (min w x), max (max u v) (max w x)⟩

def orientation (a b c : Site) : Interval :=
  sub (mul (sub b.y a.y) (sub c.z a.z)) (mul (sub b.z a.z) (sub c.y a.y))

/-- Scaled perturbation coordinates may be any rational points in the boxes. -/
def Mem (x : Rat) (a : Interval) : Prop := (a.lo : Rat)≤x ∧ x≤(a.hi : Rat)

theorem subSound {a b : Interval} {x y : Rat} (hx : Mem x a) (hy : Mem y b) :
    Mem (x-y) (sub a b) := by
  unfold Mem sub at *
  simp only [Rat.intCast_sub]
  grind

private theorem linearSound (m x l u L U : Rat) (hl : l≤x) (hu : x≤u)
    (h₁ : L≤m*l ∧ m*l≤U) (h₂ : L≤m*u ∧ m*u≤U) :
    L≤m*x ∧ m*x≤U := by
  by_cases hm : 0≤m
  · have a := Rat.mul_le_mul_of_nonneg_left hl hm
    have b := Rat.mul_le_mul_of_nonneg_left hu hm
    grind
  · have a := Rat.mul_le_mul_of_nonneg_left hl (show 0≤ -m by grind)
    have b := Rat.mul_le_mul_of_nonneg_left hu (show 0≤ -m by grind)
    grind

theorem mulSound {a b : Interval} {x y : Rat} (hx : Mem x a) (hy : Mem y b) :
    Mem (x*y) (mul a b) := by
  have corners (i j : Int) (hi : i=a.lo ∨ i=a.hi) (hj : j=b.lo ∨ j=b.hi) :
      Mem ((i:Rat)*(j:Rat)) (mul a b) := by
    unfold Mem mul
    rw [← Rat.intCast_mul]
    simp only [Rat.intCast_le_intCast]
    rcases hi with rfl|rfl <;> rcases hj with rfl|rfl <;> omega
  have ends (j : Int) (hj : j=b.lo ∨ j=b.hi) : Mem (x*(j:Rat)) (mul a b) := by
    rw [Rat.mul_comm x]
    apply linearSound _ _ _ _ _ _ hx.1 hx.2
    · simpa only [Mem, Rat.mul_comm (j:Rat)] using corners a.lo j (.inl rfl) hj
    · simpa only [Mem, Rat.mul_comm (j:Rat)] using corners a.hi j (.inr rfl) hj
  exact linearSound _ _ _ _ _ _ hy.1 hy.2 (ends b.lo (.inl rfl)) (ends b.hi (.inr rfl))

theorem orientationSound {a b c : Site} {ay az byy bz cy cz : Rat}
    (h₁ : Mem ay a.y) (h₂ : Mem az a.z) (h₃ : Mem byy b.y) (h₄ : Mem bz b.z)
    (h₅ : Mem cy c.y) (h₆ : Mem cz c.z) :
    Mem ((byy-ay)*(cz-az)-(bz-az)*(cy-ay)) (orientation a b c) :=
  subSound (mulSound (subSound h₃ h₁) (subSound h₆ h₂))
    (mulSound (subSound h₄ h₂) (subSound h₅ h₁))

/-- Every oriented projected edge against each of its six nonincident vertices. -/
def determinants (vertices : List Site) : List Interval := Id.run do
  let mut result := []
  for i in [:vertices.length] do
    let k := (i+1)%vertices.length
    for j in [:vertices.length] do
      if j≠i && j≠k then
        result := orientation vertices[i]! vertices[k]! vertices[j]! :: result
  return result

theorem allPublishedEdgesStrict :
    (determinants sites).length = 48 ∧
    (determinants sites).all (fun d => decide (44414721 ≤ d.lo)) = true ∧
    (determinants sites).any (fun d => decide (44414721 = d.lo)) = true := by
  decide +kernel

theorem indexedLower : ∀ i j : Fin 8, j ≠ i → j.val ≠ (i.val+1)%8 →
    44414721 ≤ (orientation sites[i.val]! sites[(i.val+1)%8]! sites[j.val]!).lo := by
  decide +kernel

/-- The determinant remains strictly positive under every admitted rational coordinate
perturbation for every indexed published edge and every nonincident vertex. -/
theorem projectedStrict (i j : Fin 8) (hij : j ≠ i) (hkj : j.val ≠ (i.val+1)%8)
    {ay az byy bz cy cz : Rat}
    (h₁ : Mem ay sites[i.val]!.y) (h₂ : Mem az sites[i.val]!.z)
    (h₃ : Mem byy sites[(i.val+1)%8]!.y) (h₄ : Mem bz sites[(i.val+1)%8]!.z)
    (h₅ : Mem cy sites[j.val]!.y) (h₆ : Mem cz sites[j.val]!.z) :
    0 < (byy-ay)*(cz-az)-(bz-az)*(cy-ay) := by
  have hL := indexedLower i j hij hkj
  have hR := (orientationSound h₁ h₂ h₃ h₄ h₅ h₆).1
  have hp := Rat.intCast_lt_intCast.mpr (show 0 < (orientation sites[i.val]! sites[(i.val+1)%8]! sites[j.val]!).lo by omega)
  grind

def badOrder : List Site := [0,1,5,3,4,2,6,7].map fun k => sites[k]!

theorem permutedBondsFail :
    (determinants badOrder).any (fun d => decide (d.hi < 0)) = true := by decide +kernel

def unionBox (a b : Interval) : Interval := ⟨min a.lo b.lo,max a.hi b.hi⟩
def bounding (v : List Site) : Site :=
  v.tail.foldl (fun a b => ⟨unionBox a.x b.x, unionBox a.y b.y, unionBox a.z b.z⟩) v.head!

def preserve (a : Interval) (d : Int) : Interval := ⟨a.lo+d,a.hi+d⟩
def reflect (a : Interval) (d : Int) : Interval := ⟨d-a.hi,d-a.lo⟩

inductive Op where | identity | screw | inversion | glide
  deriving DecidableEq, Repr

/-- The four CIF symmetry operations in its published setting. -/
def image (op : Op) (a : Site) : Site :=
  match op with
  | .identity => a
  | .screw => ⟨reflect a.x 0,preserve a.y 50000,reflect a.z 50000⟩
  | .inversion => ⟨reflect a.x 0,reflect a.y 0,reflect a.z 0⟩
  | .glide => ⟨preserve a.x 0,reflect a.y (-50000),preserve a.z (-50000)⟩

/-- Constraints on lattice translations in scaled fractional-coordinate units.
Two closed coordinate boxes overlap only if every axis interval overlaps. -/
def shiftWindow (op : Op) : Site :=
  let a := bounding sites
  let b := bounding (sites.map (image op))
  ⟨sub a.x b.x,sub a.y b.y,sub a.z b.z⟩

def permits (axis : Interval) (n : Int) : Prop :=
  axis.lo ≤ n*scale ∧ n*scale ≤ axis.hi

def compatible (op : Op) (nx ny nz : Int) : Prop :=
  let w := shiftWindow op
  permits w.x nx ∧ permits w.y ny ∧ permits w.z nz

/-- An interval and a translated interval overlap precisely when their
endpoint difference interval contains the displacement. -/
theorem axisCriterion (a b : Interval) (n : Int) :
    a.lo ≤ b.hi+n*scale ∧ b.lo+n*scale ≤ a.hi ↔ permits (sub a b) n := by
  unfold permits sub
  simp only
  omega

def encloses (a b : Site) : Bool :=
  decide (a.x.lo≤b.x.lo ∧ b.x.hi≤a.x.hi ∧ a.y.lo≤b.y.lo ∧ b.y.hi≤a.y.hi ∧ a.z.lo≤b.z.lo ∧ b.z.hi≤a.z.hi)

theorem allBoxesContainTheirSites (op : Op) :
    let v := sites.map (image op)
    v.all (encloses (bounding v)) = true := by
  cases op <;> decide +kernel

-- BEGIN COMPUTED WINDOWS
private theorem w_identity : shiftWindow .identity = ⟨⟨-38551,38551⟩,⟨-61057,61057⟩,⟨-38054,38054⟩⟩ := by decide +kernel
private theorem w_screw : shiftWindow .screw = ⟨⟨12690,89792⟩,⟨-111057,11057⟩,⟨107622,183730⟩⟩ := by decide +kernel
private theorem w_inversion : shiftWindow .inversion = ⟨⟨12690,89792⟩,⟨32478,154592⟩,⟨157622,233730⟩⟩ := by decide +kernel
private theorem w_glide : shiftWindow .glide = ⟨⟨-38551,38551⟩,⟨82478,204592⟩,⟨11946,88054⟩⟩ := by decide +kernel

/-- Overlap with any symmetry-translated image forces the identity copy. -/
theorem onlyIdentityCopy (op : Op) (nx ny nz : Int) (h : compatible op nx ny nz) :
    op = .identity ∧ nx=0 ∧ ny=0 ∧ nz=0 := by
  cases op <;> simp only [compatible, w_identity, w_screw, w_inversion, w_glide, permits, scale] at h <;>
    first | exact ⟨rfl, by omega, by omega, by omega⟩ | omega

-- END COMPUTED WINDOWS

#print axioms subSound
#print axioms mulSound
#print axioms orientationSound
#print axioms allPublishedEdgesStrict
#print axioms indexedLower
#print axioms projectedStrict
#print axioms permutedBondsFail
#print axioms axisCriterion
#print axioms allBoxesContainTheirSites
#print axioms onlyIdentityCopy

end VOTKP.SeleniumRing
