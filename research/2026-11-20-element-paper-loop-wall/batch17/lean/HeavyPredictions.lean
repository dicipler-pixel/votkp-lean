-- Generated from the pinned archive and the batch 16–17 affinity evidence tables.
import HeavyChambers

namespace ElementPaper.HeavyChambers
open VOTKP.NearestPair
open ElementPaper.Batch12 (endpointLo endpointHi admitsInside admitsOutside)
set_option maxRecDepth 8192
set_option maxHeartbeats 10000000

/-- Beginning at lithium: each pair is (last 2s IE, u, first 1s IE, u), in eV. -/
def kOpenings : List Face :=
  [⟨5.391714996, 0.000000022, 75.640097, 0.0000012⟩,
   ⟨18.21115, 0.00004, 153.896205, 0.000004⟩,
   ⟨37.93059, 0.00007, 259.374379, 0.000009⟩,
   ⟨64.49352, 0.00019, 392.09056, 0.00004⟩,
   ⟨97.8901, 0.0004, 552.06741, 0.00008⟩,
   ⟨138.1189, 0.0021, 739.32697, 0.00015⟩,
   ⟨185.1868, 0.0006, 953.8983, 0.0003⟩,
   ⟨239.097, 0.0019, 1195.8082, 0.0004⟩,
   ⟨299.856, 0.007, 1465.0992, 0.0007⟩,
   ⟨367.489, 0.007, 1761.8049, 0.001⟩,
   ⟨442.005, 0.007, 2085.97693, 0.00016⟩,
   ⟨523.415, 0.007, 2437.65805, 0.00017⟩,
   ⟨611.741, 0.007, 2816.90868, 0.00019⟩,
   ⟨706.994, 0.007, 3223.78057, 0.0002⟩,
   ⟨809.198, 0.007, 3658.34366, 0.00022⟩,
   ⟨918.375, 0.007, 4120.66559, 0.00022⟩,
   ⟨1034.542, 0.007, 4610.80714, 0.00025⟩,
   ⟨1157.726, 0.007, 5128.8576, 0.0003⟩,
   ⟨1287.957, 0.007, 5674.9036, 0.0004⟩,
   ⟨1425.257, 0.007, 6249.0226, 0.0007⟩,
   ⟨1569.656, 0.007, 6851.3112, 0.0008⟩,
   ⟨1721.183, 0.007, 7481.8624, 0.0012⟩,
   ⟨1879.873, 0.007, 8140.7864, 0.0014⟩,
   ⟨2045.759, 0.007, 8828.1864, 0.0012⟩,
   ⟨2218.876, 0.007, 9544.1817, 0.001⟩,
   ⟨2399.259, 0.007, 10288.8848, 0.001⟩,
   ⟨2586.954, 0.007, 11062.4309, 0.0011⟩,
   ⟨2781.996, 0.007, 11864.9401, 0.0014⟩,
   ⟨2984.426, 0.007, 12696.5581, 0.0016⟩,
   ⟨3194.293, 0.007, 13557.4218, 0.0019⟩,
   ⟨3411.643, 0.007, 14447.6799, 0.0025⟩,
   ⟨3636.526, 0.007, 15367.493, 0.003⟩,
   ⟨3868.986, 0.007, 16317.014, 0.004⟩,
   ⟨4109.083, 0.009, 17296.424, 0.004⟩,
   ⟨4356.865, 0.01, 18305.886, 0.004⟩,
   ⟨4612.397, 0.011, 19345.59, 0.005⟩,
   ⟨4875.731, 0.012, 20415.719, 0.006⟩,
   ⟨5146.935, 0.014, 21516.471, 0.006⟩,
   ⟨5426.066, 0.015, 22648.046, 0.007⟩,
   ⟨5713.194, 0.016, 23810.653, 0.009⟩,
   ⟨6008.391, 0.017, 25004.531, 0.01⟩,
   ⟨6311.721, 0.019, 26229.888, 0.011⟩,
   ⟨6623.262, 0.02, 27486.979, 0.012⟩,
   ⟨6943.097, 0.022, 28776.032, 0.014⟩,
   ⟨7271.298, 0.024, 30097.314, 0.015⟩,
   ⟨7607.95, 0.03, 31451.07, 0.017⟩,
   ⟨7953.14, 0.03, 32837.593, 0.019⟩,
   ⟨8306.95, 0.04, 34257.148, 0.022⟩,
   ⟨8669.48, 0.04, 35710.03, 0.025⟩,
   ⟨9040.83, 0.04, 37196.52, 0.03⟩,
   ⟨9421.1, 0.04, 38717.0, 0.03⟩,
   ⟨9810.37, 0.04, 40271.73, 0.03⟩,
   ⟨10208.78, 0.05, 41861.08, 0.04⟩,
   ⟨10616.42, 0.05, 43485.37, 0.04⟩,
   ⟨11033.4, 0.05, 45145.0, 0.04⟩,
   ⟨11459.85, 0.06, 46840.31, 0.05⟩,
   ⟨11895.89, 0.06, 48571.71, 0.05⟩,
   ⟨12341.66, 0.07, 50339.59, 0.06⟩,
   ⟨12797.26, 0.07, 52144.29, 0.06⟩,
   ⟨13262.85, 0.09, 53986.12, 0.07⟩,
   ⟨13738.58, 0.09, 55865.93, 0.08⟩,
   ⟨14224.57, 0.1, 57783.91, 0.08⟩,
   ⟨14721.02, 0.1, 59741.12, 0.09⟩,
   ⟨15228.06, 0.11, 61736.62, 0.1⟩,
   ⟨15745.77, 0.11, 63772.42, 0.11⟩,
   ⟨16274.56, 0.12, 65848.24, 0.12⟩,
   ⟨16814.34, 0.14, 67965.25, 0.12⟩,
   ⟨17365.44, 0.15, 70123.04, 0.14⟩,
   ⟨17928.05, 0.16, 72322.87, 0.15⟩,
   ⟨18502.32, 0.17, 74565.91, 0.16⟩,
   ⟨19088.51, 0.19, 76852.0, 0.17⟩,
   ⟨19686.74, 0.2, 79181.94, 0.19⟩,
   ⟨20297.4, 0.21, 81556.58, 0.2⟩,
   ⟨20920.6, 0.22, 83976.18, 0.22⟩,
   ⟨21556.6, 0.24, 86442.44, 0.25⟩,
   ⟨22205.7, 0.3, 88955.1, 0.3⟩,
   ⟨22868.1, 0.3, 91515.8, 0.3⟩,
   ⟨23544.1, 0.3, 94124.7, 0.3⟩,
   ⟨24234.1, 0.4, 96783.2, 0.3⟩,
   ⟨24938.2, 0.4, 99491.8, 0.3⟩,
   ⟨25656.9, 0.4, 102251.8, 0.4⟩,
   ⟨26390.4, 0.4, 105064.3, 0.4⟩,
   ⟨27139.0, 0.4, 107930.0, 0.4⟩]

def goldK := kOpenings[76]'(by decide +kernel)
def mercuryK := kOpenings[77]'(by decide +kernel)

theorem fullFirstCrossing : kOpenings.length = 83 ∧
    (kOpenings.take 77).all aboveFour = true ∧ (kOpenings.drop 77).all belowFour = true ∧
    (kOpenings.zip kOpenings.tail).all (fun (a,b) => decide (endpointHi b < endpointLo a)) = true := by
  decide +kernel

theorem goldMercuryK : aboveFour goldK = true ∧ belowFour mercuryK = true ∧
    admitsInside goldK = true ∧ admitsInside mercuryK = true := by decide +kernel

def frozenModels : List (Rat × Rat) :=
  [(4.034052521,4.034266373), (4.030024809,4.030448440), (4.025997098,4.026623803), (4.021969386,4.022789889), (4.017941674,4.018944175), (4.013913962,4.015084181), (4.009886250,4.011207460), (4.005858539,4.007311593), (4.001830827,4.003394181), (3.997803115,3.999452836), (3.993775403,3.995485177), (3.989747691,3.991488820), (3.985719980,3.987461375), (3.981692268,3.983400432), (3.977664556,3.979303563)]
def scored := (kOpenings.drop 68).zip frozenModels

theorem linearAlwaysNearer : scored.length = 15 ∧
    scored.all (fun (f,m) => nearerTest f m) = true := by decide +kernel

theorem forecastBoxCoverage :
    (scored.zipIdx.filterMap (fun ((f,m),i) => if whollyIn f m.1 then some (i+71) else none)) = [71,80] ∧
    scored.all (fun (f,m) => whollyIn f m.1 || whollyOut f m.1) = true ∧
    scored.all (fun (f,m) => whollyOut f m.2) = true := by decide +kernel

def OsmiumEA : Face := ⟨1.077661, 0.000024, 8.43823, 0.0002⟩
def IridiumEA : Face := ⟨1.564057, 0.000011, 8.96702, 0.00022⟩
def PlatinumEA : Face := ⟨2.12510, 0.00005, 8.95883, 0.0001⟩
def GoldEA : Face := ⟨2.30861, 0.00003, 9.225554, 0.000004⟩
def ThalliumEA : Face := ⟨0.320053, 0.000019, 6.1082873, 0.0000012⟩
def LeadEA : Face := ⟨0.356721, 0.000002, 7.4166799, 0.0000006⟩
def BismuthEA : Face := ⟨0.942362, 0.000013, 7.285516, 0.000006⟩
def AstatineEA : Face := ⟨2.41578, 0.00007, 9.31751, 0.00008⟩

/-- Polonium has no final ground-state primary point in the evidence selection. -/
def primary : List Forecast := [⟨76,OsmiumEA,true⟩, ⟨77,IridiumEA,false⟩, ⟨78,PlatinumEA,false⟩, ⟨79,GoldEA,false⟩, ⟨82,LeadEA,true⟩, ⟨83,BismuthEA,true⟩, ⟨85,AstatineEA,false⟩]

theorem primarySeven : primary.map Forecast.z = [76,77,78,79,82,83,85] ∧
    primary.all predictionSupported = true ∧ primary.all leavesWindow = true ∧
    primary.all (fun r => chemistry r.face) = true := by decide +kernel

theorem thalliumComparison : admitsOutside ThalliumEA = true := by decide +kernel

/-- Both gold readings are inside the loop wall, on opposite sides of the bare reference four. -/
theorem goldOppositeAtFour : belowFour GoldEA = true ∧ aboveFour goldK = true ∧
    admitsInside GoldEA = true ∧ admitsInside goldK = true := by decide +kernel

def inverseCmToEV : Rat := 6621486190496429/53405887800000000000

/-- The second argument is an assumed half-width in cm⁻¹, not an inferred systematic uncertainty. -/
def polonium (wave halfWidth : Rat) : Face :=
  ⟨wave * inverseCmToEV, halfWidth * inverseCmToEV, 8.41807, 0.000004⟩

theorem poloniumStatisticalOnly :
    admitsInside (polonium 11905.631 0.009) = true ∧
    predictionSupported ⟨84,polonium 11905.631 0.009,true⟩ = false := by decide +kernel

theorem poloniumIfInDisplayedRange :
    let f := polonium 11875 75
    (f.a-f.ua = 11800*inverseCmToEV ∧ f.a+f.ua = 11950*inverseCmToEV) ∧
    admitsInside f = true ∧ leavesWindow ⟨84,f,false⟩ = true ∧
    predictionSupported ⟨84,f,true⟩ = false := by decide +kernel

/-- Even the archived IE uncertainty is allowed when bracketing the forward wall at fixed wavenumber. -/
theorem poloniumCriticalBracket :
    admitsOutside (polonium 11649.160 0) = true ∧
    admitsInside (polonium 11649.172 0) = true ∧
    (11905.631:Rat)-11649.172 = 256.459 := by decide +kernel

theorem controlsFalse : belowFour goldK = false ∧ aboveFour mercuryK = false ∧
    84 ∉ primary.map Forecast.z ∧
    predictionSupported ⟨84,polonium 11875 75,true⟩ = false := by decide +kernel

#print axioms strictlyAbove
#print axioms strictlyBelow
#print axioms descending
#print axioms sameCutForEveryInput
#print axioms fullFirstCrossing
#print axioms goldMercuryK
#print axioms nearerOnLeft
#print axioms nearerAcrossFullBox
#print axioms linearAlwaysNearer
#print axioms forecastBoxCoverage
#print axioms primarySeven
#print axioms thalliumComparison
#print axioms goldOppositeAtFour
#print axioms poloniumStatisticalOnly
#print axioms poloniumIfInDisplayedRange
#print axioms poloniumCriticalBracket
#print axioms controlsFalse

end ElementPaper.HeavyChambers
