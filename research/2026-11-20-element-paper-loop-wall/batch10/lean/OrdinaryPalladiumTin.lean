-- Archive at bcedbd9. k=1 is the first ordinary rung.
import OrdinaryGaZr
namespace VOTKP.ElementBatch10
open VOTKP.ElementBatches7And8

def Palladium : List Rat :=
  [8.336839, 19.43, 32.93, 46.0, 61.0, 84.1,
   101.0, 120.0, 141.0, 159.9, 238.57, 260.0,
   286.0, 311.0, 342.0, 369.1, 427.0, 457.5,
   810.0, 869.0, 933.0, 1000.0, 1065.0, 1145.0,
   1218.0, 1290.0, 1366.0, 1438.0, 1644.0, 1706.2,
   1781.3, 1869.0, 1962.0, 2016.0, 2181.0, 2248.87,
   5284.0, 5475.0, 5683.0, 5880.0, 6242.0, 6469.0,
   6759.0, 6943.097, 28776.032, 29622.678]

theorem ordinaryPalladium : Palladium.length = 46 ∧ checkLadder Palladium [] = true := by
  decide +kernel

def Silver : List Rat :=
  [7.576234, 21.4844, 34.8, 49.0, 65.0, 82.0,
   106.0, 125.0, 145.1, 167.0, 188.0, 271.46,
   294.0, 321.0, 347.0, 381.0, 408.43, 469.0,
   500.87, 885.0, 946.0, 1013.0, 1082.0, 1149.0,
   1231.0, 1308.0, 1382.0, 1460.0, 1535.0, 1747.0,
   1810.5, 1888.0, 1979.0, 2077.0, 2131.0, 2302.0,
   2371.99, 5558.0, 5753.0, 5966.0, 6170.0, 6551.0,
   6785.0, 7082.0, 7271.298, 30097.314, 30965.78]

theorem ordinarySilver : Silver.length = 47 ∧ checkLadder Silver [] = true := by
  decide +kernel

def Cadmium : List Rat :=
  [8.99382, 16.908313, 37.468, 51.0, 67.9, 87.0,
   105.0, 130.1, 150.0, 173.0, 195.0, 218.0,
   305.0, 329.0, 358.0, 385.0, 421.0, 452.6,
   513.0, 546.19, 963.0, 1026.0, 1095.0, 1167.0,
   1237.0, 1320.0, 1401.0, 1477.0, 1558.0, 1635.0,
   1852.0, 1917.9, 1998.0, 2091.0, 2195.0, 2250.0,
   2427.0, 2498.62, 5839.0, 6039.0, 6257.0, 6460.0,
   6869.0, 7109.0, 7414.0, 7607.95, 31451.07, 32341.587]

theorem ordinaryCadmium : Cadmium.length = 48 ∧ checkLadder Cadmium [] = true := by
  decide +kernel

def Indium : List Rat :=
  [5.7863558, 18.87041, 28.04415, 55.45, 69.3, 90.0,
   109.0, 130.1, 156.0, 178.0, 201.0, 226.0,
   249.0, 341.0, 368.0, 396.0, 425.0, 462.0,
   497.1, 560.0, 593.38, 1043.0, 1109.0, 1181.0,
   1255.0, 1328.0, 1413.0, 1496.0, 1575.0, 1659.0,
   1738.0, 1961.0, 2028.5, 2111.0, 2207.0, 2317.0,
   2373.0, 2555.0, 2628.77, 6126.0, 6331.0, 6554.0,
   6770.0, 7196.0, 7442.0, 7754.0, 7953.14, 32837.593,
   33750.404]

theorem ordinaryIndium : Indium.length = 49 ∧ checkLadder Indium [] = true := by
  decide +kernel

def Tin : List Rat :=
  [7.343918, 14.63307, 30.506, 40.74, 77.03, 94.0,
   112.9, 135.0, 156.0, 184.0, 208.0, 232.0,
   258.0, 282.0, 379.0, 407.0, 437.0, 466.0,
   506.0, 537.0, 608.0, 642.35, 1127.0, 1195.0,
   1269.0, 1347.0, 1421.0, 1508.0, 1596.0, 1676.0,
   1763.0, 1844.0, 2074.0, 2142.1, 2227.0, 2326.0,
   2443.0, 2499.0, 2687.0, 2762.49, 6421.0, 6631.0,
   6859.0, 7080.0, 7531.0, 7790.0, 8103.0, 8306.95,
   34257.148, 35192.501]

theorem ordinaryTin : Tin.length = 50 ∧ checkLadder Tin [] = true := by
  decide +kernel

def palladiumEA : Rat := 0.56214

/-- Crossing numbers 0,1,2,3,4 in element order. Only palladium uses the affinity. -/
theorem filled4dWallCalls :
    checkWall palladiumEA Palladium[0]! true = true ∧
    checkWall Silver[0]! Silver[1]! false = true ∧
    checkWall Cadmium[1]! Cadmium[2]! false = true ∧
    checkWall Indium[2]! Indium[3]! false = true ∧
    checkWall Tin[3]! Tin[4]! false = true := by
  decide +kernel

/-- The five exact ratios strictly decrease; the first divides by an affinity. -/
theorem filled4dRatiosDecrease :
    (Palladium[0]! / palladiumEA) > (Silver[1]! / Silver[0]!) ∧
    (Silver[1]! / Silver[0]!) > (Cadmium[2]! / Cadmium[1]!) ∧
    (Cadmium[2]! / Cadmium[1]!) > (Indium[3]! / Indium[2]!) ∧
    (Indium[3]! / Indium[2]!) > (Tin[4]! / Tin[3]!) := by
  decide +kernel

/-- Removing the anion boundary from palladium removes its only outside crossing. -/
theorem wrongPalladiumFirstOrdinaryOutside : checkLadder Palladium [1] = false := by
  decide +kernel

#print axioms ordinaryPalladium
#print axioms ordinarySilver
#print axioms ordinaryCadmium
#print axioms ordinaryIndium
#print axioms ordinaryTin
#print axioms filled4dWallCalls
#print axioms filled4dRatiosDecrease
#print axioms wrongPalladiumFirstOrdinaryOutside

end VOTKP.ElementBatch10
