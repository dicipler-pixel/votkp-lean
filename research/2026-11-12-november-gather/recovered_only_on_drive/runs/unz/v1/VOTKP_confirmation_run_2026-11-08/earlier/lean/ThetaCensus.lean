/-
  Theta census: a machine-checked test package.

  WHAT THIS FILE DOES
  -------------------
  It formalises and proves, in Lean 4 + Mathlib, the *arithmetic and combinatorial
  facts* that the published census asserts. Nothing here formalises the invariant
  theta itself, and nothing here is a statement about knot theory that Lean can
  check: the knot-theoretic input is the census data, which is a computation
  recorded in results/share/data/census_through_13.csv.

  The point of the package is to make the numbers in the paper un-fudgeable and to
  state the one genuine theorem the construction needs (the parity lemma, §4), so
  that the surrounding prose can be checked against something executable.

  WHAT IS *NOT* HERE
  ------------------
  * No definition of theta, of the Alexander polynomial, or of amphichirality.
  * No proof that theta detects chirality (that is an open mathematical question,
    stated as such in the paper).
  * No formalisation of the degree bound of §5.2 of the paper.
-/
import Mathlib

set_option maxRecDepth 100000

namespace ThetaCensus

/-! ## 1. The census table, per family -/

/-- One row per knot family: number of prime knots, of those how many KnotInfo
classifies as amphichiral, and on how many theta was certified to vanish. -/
structure Family where
  name : String
  knots : Nat
  amphichiral : Nat
  thetaZero : Nat
deriving DecidableEq, Repr

/-- The fourteen families, exactly as counted by the census run. -/
def families : List Family :=
[
⟨"3", 1, 0, 0⟩,
  ⟨"4", 1, 1, 1⟩,
  ⟨"5", 2, 0, 0⟩,
  ⟨"6", 3, 1, 1⟩,
  ⟨"7", 7, 0, 0⟩,
  ⟨"8", 21, 5, 5⟩,
  ⟨"9", 49, 0, 0⟩,
  ⟨"10", 165, 13, 13⟩,
  ⟨"11a", 367, 0, 0⟩,
  ⟨"11n", 185, 0, 0⟩,
  ⟨"12a", 1288, 54, 54⟩,
  ⟨"12n", 888, 4, 4⟩,
  ⟨"13a", 4878, 0, 0⟩,
  ⟨"13n", 5110, 0, 0⟩,
]

/-- The total number of prime knots through thirteen crossings. -/
theorem total_knots : (families.map Family.knots).sum = 12965 := by decide

/-- The total number of amphichiral entries, from KnotInfo's classification. -/
theorem total_amphichiral : (families.map Family.amphichiral).sum = 78 := by decide

/-- The total number of entries on which theta was certified to vanish. -/
theorem total_thetaZero : (families.map Family.thetaZero).sum = 78 := by decide

/-- **The census proposition, in the only form Lean can check it here:** for every
family, the number of knots with theta = 0 equals the number KnotInfo classifies as
amphichiral. -/
theorem every_family_agrees :
    ∀ f ∈ families, f.thetaZero = f.amphichiral := by decide

/-- Consequently the two totals agree, which is the finite statement of the paper. -/
theorem totals_agree :
    (families.map Family.thetaZero).sum = (families.map Family.amphichiral).sum := by
  decide

/-- There is no amphichiral prime knot with 11 crossings, and none with 13. -/
theorem none_at_11_and_13 :
    (families.filter (fun f => f.name = "11a" ∨ f.name = "11n" ∨
                               f.name = "13a" ∨ f.name = "13n")).all
      (fun f => f.amphichiral = 0) = true := by decide

/-! ## 2. The 78, and their certificates -/

/-- The 78 knots on which theta vanishes: the same list that KnotInfo classifies as
amphichiral. -/
def the78 : List String :=
  [ "4_1",
    "6_3",
    "8_3",
    "8_9",
    "8_12",
    "8_17",
    "8_18",
    "10_17",
    "10_33",
    "10_37",
    "10_43",
    "10_45",
    "10_79",
    "10_81",
    "10_88",
    "10_99",
    "10_109",
    "10_115",
    "10_118",
    "10_123",
    "12a_4",
    "12a_58",
    "12a_125",
    "12a_268",
    "12a_273",
    "12a_341",
    "12n_356",
    "12a_427",
    "12a_435",
    "12a_458",
    "12a_462",
    "12n_462",
    "12a_465",
    "12a_471",
    "12a_477",
    "12a_499",
    "12a_506",
    "12a_510",
    "12a_627",
    "12n_706",
    "12a_819",
    "12a_821",
    "12a_868",
    "12n_873",
    "12a_887",
    "12a_890",
    "12a_906",
    "12a_960",
    "12a_990",
    "12a_1008",
    "12a_1019",
    "12a_1039",
    "12a_1102",
    "12a_1105",
    "12a_1123",
    "12a_1124",
    "12a_1127",
    "12a_1152",
    "12a_1167",
    "12a_1188",
    "12a_1202",
    "12a_1209",
    "12a_1211",
    "12a_1218",
    "12a_1225",
    "12a_1229",
    "12a_1249",
    "12a_1251",
    "12a_1254",
    "12a_1260",
    "12a_1267",
    "12a_1269",
    "12a_1273",
    "12a_1275",
    "12a_1280",
    "12a_1281",
    "12a_1287",
    "12a_1288" ]

theorem the78_count : the78.length = 78 := by decide

/-- No knot is counted twice. -/
theorem the78_distinct : the78.Nodup := by decide

/-- Grid-cell counts of the 78 zero certificates of §5.4, in the same order. -/
def certificateCells : List Nat :=
  [ 156, 272, 600, 420, 420, 420, 420, 600, 812, 812, 600, 600, 600, 812, 600, 600, 600, 812, 600, 600, 812, 812, 1056, 1056, 1056, 812, 812, 812, 1056, 812, 812, 812, 812, 1056, 812, 812, 812, 1056, 812, 812, 812, 1056, 1332, 812, 1056, 1056, 1056, 1056, 1056, 1056, 812, 812, 812, 812, 1332, 1332, 1056, 812, 1056, 1056, 1640, 812, 812, 812, 812, 812, 812, 1056, 812, 812, 1056, 1056, 812, 1056, 1056, 1056, 1332, 812 ]

theorem certificateCells_count : certificateCells.length = 78 := by decide

/-- The 66,728 cell evaluations reported in the paper. -/
theorem certificateCells_sum : certificateCells.sum = 66728 := by decide

/-- The largest single certificate is 1,640 cells; the smallest is 156, for the
figure-eight. -/
theorem largest_certificate : certificateCells.max? = some 1640 := by decide

theorem smallest_certificate : certificateCells.min? = some 156 := by decide

/-! ## 3. Diagram sizes -/

/-- The census used braid words up to 73 letters on up to 12 strands, so the largest
matrix in the computation is 147 by 147. -/
theorem largest_matrix : 2 * 73 + 1 = (147 : Nat) := by decide

/-- The five knots with a 73-letter braid. -/
def longestBraids : List String :=
  ["13a_3143", "13a_4573", "13a_4843", "13a_4856", "13a_4873"]

theorem longestBraids_count : longestBraids.length = 5 := by decide

/-! ## 4. The parity lemma

The construction of §2 of the paper takes theta on the closure of a braid word. Its
one mathematical input is that the normalisation exponent is an integer, which needs
`L ≡ m - 1 (mod 2)` when the closure of an `L`-letter word on `m` strands is a knot.
That follows from two facts: a product of `L` transpositions has sign `(-1)^L`, and an
`m`-cycle on an `m`-element type has sign `(-1)^(m+1)`.

Both are proved here. -/

/-- The sign of an `m`-cycle on an `m`-element type is `-(-1)^m`. -/
theorem sign_of_full_cycle {m : Nat} (σ : Equiv.Perm (Fin m))
    (hcycle : σ.IsCycle) (hcard : σ.support.card = m) :
    Equiv.Perm.sign σ = -(-1 : ℤˣ) ^ m := by
  rw [hcycle.sign, hcard]

/-- `-x = x * (-1)` in `ℤˣ`, so `-(-1)^m = (-1)^(m+1)`. -/
theorem neg_pow_neg_one (m : Nat) :
    -((-1 : ℤˣ) ^ m) = (-1 : ℤˣ) ^ (m + 1) := by
  rw [pow_succ, mul_comm]
  exact (neg_one_mul ((-1 : ℤˣ) ^ m)).symm

/-- **The parity lemma.** If a permutation of `Fin m` is an `m`-cycle and also has the
sign of an `L`-fold product of transpositions, then `L ≡ m - 1 (mod 2)`. This is the
step that makes the normalisation exponent of the invariant an integer. `m ≥ 1` is
automatic for a braid closure that is a knot: a braid has at least one strand. -/
theorem parity_of_closure {m L : Nat} (hm1 : 1 ≤ m) (σ : Equiv.Perm (Fin m))
    (hcycle : σ.IsCycle) (hcard : σ.support.card = m)
    (hL : Equiv.Perm.sign σ = (-1 : ℤˣ) ^ L) :
    L % 2 = (m - 1) % 2 := by
  rw [sign_of_full_cycle σ hcycle hcard] at hL
  have hv : -((-1 : ℤ) ^ m) = (-1 : ℤ) ^ L := by
    have := congrArg Units.val hL
    simpa using this
  rcases Nat.even_or_odd L with hL' | hL'
  · rw [hL'.neg_one_pow] at hv
    have hm : Odd m := by
      rcases Nat.even_or_odd m with hm' | hm'
      · rw [hm'.neg_one_pow] at hv; norm_num at hv
      · exact hm'
    have hm2 : m % 2 = 1 := Nat.odd_iff.mp hm
    have hL2 : L % 2 = 0 := Nat.even_iff.mp hL'
    omega
  · rw [hL'.neg_one_pow] at hv
    have hm : Even m := by
      rcases Nat.even_or_odd m with hm' | hm'
      · exact hm'
      · rw [hm'.neg_one_pow] at hv; norm_num at hv
    have hm2 : m % 2 = 0 := Nat.even_iff.mp hm
    have hL2 : L % 2 = 1 := Nat.odd_iff.mp hL'
    omega

end ThetaCensus
