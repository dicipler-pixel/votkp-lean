-- Batch 9 from archive at 182da01: central energies in eV.
import OrdinaryGaZr
namespace VOTKP.ElementBatch9
open VOTKP.ElementBatches7And8

def energiesNb : List Rat :=
  [6.75885, 14.32, 25.04, 37.611, 50.5728, 102.069,
   119.1, 136.0, 159.2, 180.0, 200.28, 246.1,
   268.59, 482.5, 530.0, 581.0, 636.0, 688.0,
   758.0, 816.0, 877.0, 940.0, 1000.0, 1176.0,
   1230.6, 1293.7, 1368.0, 1439.0, 1488.0, 1625.9,
   1684.97, 4020.1, 4187.0, 4369.0, 4540.0, 4815.0,
   5011.0, 5265.0, 5426.066, 22648.046, 23388.85]

theorem ordinary_Nb :
    energiesNb.length = 41 ∧ checkLadder energiesNb [] = true := by
  decide +kernel

def energiesMo : List Rat :=
  [7.09243, 16.16, 27.13, 40.33, 54.417, 68.82704,
   125.638, 143.6, 164.12, 186.3, 209.3, 230.28,
   279.1, 302.6, 544.0, 591.0, 646.0, 702.0,
   758.0, 829.0, 890.0, 953.0, 1019.0, 1082.0,
   1263.0, 1319.6, 1385.1, 1462.0, 1537.0, 1587.0,
   1730.1, 1790.93, 4259.0, 4430.0, 4618.0, 4800.0,
   5084.0, 5287.0, 5548.0, 5713.194, 23810.653, 24572.213]

theorem ordinary_Mo :
    energiesMo.length = 42 ∧ checkLadder energiesMo [] = true := by
  decide +kernel

def energiesTc : List Rat :=
  [7.11938, 15.26, 29.55, 41.0, 57.0, 72.0,
   88.0, 150.0, 169.0, 189.9, 214.0, 239.0,
   262.08, 311.0, 338.55, 604.0, 655.0, 713.0,
   773.0, 829.0, 904.0, 968.0, 1032.0, 1102.0,
   1166.0, 1354.0, 1411.6, 1479.5, 1559.0, 1638.0,
   1689.0, 1838.0, 1900.28, 4505.0, 4681.0, 4874.0,
   5060.0, 5361.0, 5570.0, 5838.0, 6008.391, 25004.531,
   25787.047]

theorem ordinary_Tc :
    energiesTc.length = 43 ∧ checkLadder energiesTc [] = true := by
  decide +kernel

def energiesRu : List Rat :=
  [7.3605, 16.76, 28.47, 45.0, 59.0, 76.0,
   93.0, 110.0, 178.41, 198.0, 219.9, 245.0,
   271.0, 295.9, 348.0, 376.25, 670.0, 723.0,
   784.0, 845.0, 905.0, 981.0, 1048.0, 1115.0,
   1187.0, 1253.0, 1447.0, 1506.7, 1577.0, 1659.0,
   1743.0, 1794.0, 1949.0, 2013.04, 4758.0, 4939.0,
   5136.0, 5330.0, 5647.0, 5861.0, 6137.0, 6311.721,
   26229.888, 27033.564]

theorem ordinary_Ru :
    energiesRu.length = 44 ∧ checkLadder energiesRu [] = true := by
  decide +kernel

def energiesRh : List Rat :=
  [7.4589, 18.08, 31.06, 42.0, 63.0, 80.0,
   97.0, 115.1, 135.0, 207.51, 228.0, 252.1,
   277.0, 306.0, 331.58, 389.3, 415.97, 739.0,
   794.0, 857.0, 921.0, 984.0, 1061.0, 1131.0,
   1202.0, 1274.0, 1344.0, 1544.0, 1604.9, 1677.6,
   1763.0, 1851.0, 1903.0, 2063.0, 2129.22, 5018.0,
   5203.0, 5406.0, 5600.0, 5940.0, 6161.0, 6444.0,
   6623.262, 27486.979, 28312.031]

theorem ordinary_Rh :
    energiesRh.length = 45 ∧ checkLadder energiesRh [] = true := by
  decide +kernel

/-- A neutral or positively ionized Nb–Rh atom has fewer than the 46 electrons
required for a [Kr] 4d¹⁰ core. This bound uses the specified core occupancy. -/
theorem below_kr_4d10_count (Z k : Nat) (h : Z ≤ 45) : Z - k < 36 + 10 := by
  omega

/-- Negative controls for assigning outside noble-core openings to Nb and Rh. -/
theorem nb_false_outside_kr_core : checkLadder energiesNb [5] = false := by
  decide +kernel

theorem rh_false_outside_he_core : checkLadder energiesRh [43] = false := by
  decide +kernel

#print axioms ordinary_Nb
#print axioms ordinary_Mo
#print axioms ordinary_Tc
#print axioms ordinary_Ru
#print axioms ordinary_Rh
#print axioms below_kr_4d10_count
#print axioms nb_false_outside_kr_core
#print axioms rh_false_outside_he_core

end VOTKP.ElementBatch9
