-- Generated from c35b18b archive bytes and batch8_ladder.py affinity data.
import IntervalWall
namespace VOTKP.Element8Intervals

def inputsKr : List Input :=
  [.unbound, .energy 13.9996055 (some 0.000002), .energy 24.35984 (some 0.00012), .energy 35.838 (some 0.02),
   .energy 50.85 (some 0.11), .energy 64.69 (some 0.2), .energy 78.49 (some 0.2), .energy 109.13 (some 0.05),
   .energy 125.802 (some 0.003), .energy 233.0 (some 0.7), .energy 268.0 (some 3.0), .energy 308.0 (some 3.0),
   .energy 350.0 (some 3.0), .energy 391.0 (some 4.0), .energy 446.0 (some 3.0), .energy 492.0 (some 5.0),
   .energy 540.0 (some 3.0), .energy 591.0 (some 3.0), .energy 640.0 (some 3.0), .energy 785.316 (some 0.012),
   .energy 831.6 (some 0.9), .energy 882.8 (some 1.3), .energy 945.0 (some 3.0), .energy 999.0 (some 2.4),
   .energy 1042.0 (some 5.0), .energy 1155.0 (some 1.6), .energy 1205.23 (some 0.04), .energy 2928.9 (some 1.7),
   .energy 3072.0 (some 5.0), .energy 3228.0 (some 7.0), .energy 3380.0 (some 30.0), .energy 3584.0 (some 4.0),
   .energy 3752.0 (some 2.5), .energy 3971.0 (some 4.0), .energy 4109.083 (some 0.009), .energy 17296.424 (some 0.004),
   .energy 17936.2405 (some 0.0016)]

theorem intervals_Kr : statuses inputsKr =
    [.noBoundAnion] ++ List.replicate 35 .inside := by
  decide +kernel

def inputsRb : List Input :=
  [.energy 0.485916 (some 0.000021), .energy 4.1771281 (some 0.0000012), .energy 27.28954 (some 0.00006), .energy 39.247 (some 0.003),
   .energy 52.2 (some 0.25), .energy 68.44 (some 0.15), .energy 82.9 (some 2.0), .energy 98.67 (some 0.04),
   .energy 132.79 (some 0.25), .energy 150.628 (some 0.025), .energy 277.12 (some 0.12), .energy 313.1 (some 2.4),
   .energy 356.0 (some 2.5), .energy 400.0 (some 3.0), .energy 443.0 (some 3.0), .energy 502.0 (some 3.0),
   .energy 550.0 (some 3.0), .energy 601.0 (some 3.0), .energy 654.0 (some 3.0), .energy 706.0 (some 2.2),
   .energy 857.0 (some 3.0), .energy 905.3 (some 1.0), .energy 958.9 (some 1.4), .energy 1024.0 (some 4.0),
   .energy 1080.0 (some 3.0), .energy 1125.0 (some 5.0), .energy 1242.5 (some 1.7), .energy 1294.57 (some 0.04),
   .energy 3133.3 (some 1.8), .energy 3281.0 (some 6.0), .energy 3443.0 (some 8.0), .energy 3600.0 (some 30.0),
   .energy 3815.0 (some 4.0), .energy 3988.0 (some 3.0), .energy 4214.0 (some 4.0), .energy 4356.865 (some 0.01),
   .energy 18305.886 (some 0.004), .energy 18965.5484 (some 0.002)]

theorem intervals_Rb : statuses inputsRb =
    [.outside, .outside] ++ List.replicate 35 .inside := by
  decide +kernel

def inputsSr : List Input :=
  [.energy 0.05206 (some 0.00006), .energy 5.69486745 (some 0.00000012), .energy 11.0302765 (some 0.0000025), .energy 42.88353 (some 0.00019),
   .energy 56.28 (some 0.003), .energy 70.7 (some 0.6), .energy 88.0 (some 2.0), .energy 104.0 (some 2.0),
   .energy 121.21 (some 0.06), .energy 158.33 (some 0.25), .energy 177.3 (some 0.06), .energy 324.07 (some 0.15),
   .energy 362.0 (some 2.5), .energy 408.0 (some 3.0), .energy 454.0 (some 3.0), .energy 499.0 (some 3.0),
   .energy 562.0 (some 3.0), .energy 612.0 (some 3.0), .energy 665.0 (some 3.0), .energy 722.0 (some 3.0),
   .energy 774.0 (some 4.0), .energy 932.0 (some 3.0), .energy 982.1 (some 1.1), .energy 1038.0 (some 1.5),
   .energy 1105.0 (some 4.0), .energy 1165.0 (some 3.0), .energy 1211.0 (some 6.0), .energy 1333.4 (some 1.9),
   .energy 1387.19 (some 0.05), .energy 3344.7 (some 1.9), .energy 3497.0 (some 6.0), .energy 3664.0 (some 8.0),
   .energy 3830.0 (some 30.0), .energy 4053.0 (some 4.0), .energy 4232.0 (some 3.0), .energy 4465.0 (some 4.0),
   .energy 4612.397 (some 0.011), .energy 19345.59 (some 0.005), .energy 20025.2673 (some 0.0024)]

theorem intervals_Sr : statuses inputsSr =
    [.outside] ++ List.replicate 37 .inside := by
  decide +kernel

def inputsY : List Input :=
  [.energy 0.31129 (some 0.00022), .energy 6.21726 (some 0.0001), .energy 12.2236 (some 0.0006), .energy 20.52441 (some 0.00012),
   .energy 60.6072 (some 0.0025), .energy 75.35 (some 0.04), .energy 91.39 (some 0.025), .energy 110.02 (some 0.15),
   .energy 128.12 (some 0.12), .energy 145.64 (some 0.04), .energy 185.7 (some 0.4), .energy 205.814 (some 0.025),
   .energy 374.04 (some 0.25), .energy 414.0 (some 3.0), .energy 463.0 (some 3.0), .energy 512.0 (some 3.0),
   .energy 559.0 (some 3.0), .energy 624.0 (some 3.0), .energy 677.0 (some 3.0), .energy 733.0 (some 3.0),
   .energy 790.0 (some 4.0), .energy 847.0 (some 4.0), .energy 1010.0 (some 3.0), .energy 1061.9 (some 1.2),
   .energy 1120.2 (some 1.6), .energy 1190.0 (some 4.0), .energy 1253.0 (some 3.0), .energy 1300.0 (some 6.0),
   .energy 1427.6 (some 2.0), .energy 1483.12 (some 0.05), .energy 3562.9 (some 2.0), .energy 3720.0 (some 6.0),
   .energy 3892.0 (some 8.0), .energy 4060.0 (some 30.0), .energy 4299.0 (some 5.0), .energy 4484.0 (some 3.0),
   .energy 4724.0 (some 5.0), .energy 4875.731 (some 0.012), .energy 20415.719 (some 0.006), .energy 21115.588 (some 0.003)]

theorem intervals_Y : statuses inputsY =
    [.outside] ++ List.replicate 38 .inside := by
  decide +kernel

def inputsZr : List Input :=
  [.energy 0.433283 (some 0.000089), .energy 6.634126 (some 0.000005), .energy 13.13 none, .energy 23.17 (some 0.004),
   .energy 34.41836 (some 0.00006), .energy 80.348 (some 0.007), .energy 96.38 (some 0.04), .energy 112.0 (some 2.0),
   .energy 133.7 (some 0.5), .energy 153.0 (some 2.2), .energy 172.02 (some 0.05), .energy 214.9 (some 0.4),
   .energy 236.252 (some 0.025), .energy 426.0 (some 3.0), .energy 470.0 (some 3.0), .energy 520.0 (some 3.0),
   .energy 573.0 (some 3.0), .energy 622.0 (some 3.0), .energy 690.0 (some 3.0), .energy 745.0 (some 3.0),
   .energy 803.0 (some 4.0), .energy 863.0 (some 4.0), .energy 922.0 (some 4.0), .energy 1092.0 (some 3.0),
   .energy 1144.7 (some 1.2), .energy 1205.4 (some 1.7), .energy 1277.0 (some 5.0), .energy 1344.0 (some 3.0),
   .energy 1392.0 (some 7.0), .energy 1525.1 (some 2.2), .energy 1582.37 (some 0.05), .energy 3788.0 (some 2.1),
   .energy 3950.0 (some 7.0), .energy 4127.0 (some 9.0), .energy 4300.0 (some 30.0), .energy 4553.0 (some 5.0),
   .energy 4744.0 (some 3.0), .energy 4991.0 (some 5.0), .energy 5146.935 (some 0.014), .energy 21516.471 (some 0.006),
   .energy 22236.712 (some 0.004)]

theorem intervals_Zr : statuses inputsZr =
    [.outside, .missingUncertainty, .missingUncertainty] ++ List.replicate 37 .inside := by
  decide +kernel

/-- Replacing an absent error by zero changes an unknown box into a known box. -/
theorem zirconium_missing_is_not_zero :
    let z1 := inputsZr[1]!
    let z2 := inputsZr[2]!
    classify z1 z2 = .missingUncertainty ∧
    classify z1 (.energy 13.13 (some 0)) = .inside ∧
    classify z1 z2 ≠ classify z1 (.energy 13.13 (some 0)) := by
  decide +kernel

theorem krypton_unbound_is_not_missing :
    classify .unbound (.energy 1 none) ≠ .missingUncertainty := by
  decide +kernel

#print axioms inside_everywhere
#print axioms outside_everywhere
#print axioms box_inside_sound
#print axioms box_outside_sound
#print axioms intervals_Kr
#print axioms intervals_Rb
#print axioms intervals_Sr
#print axioms intervals_Y
#print axioms intervals_Zr
#print axioms zirconium_missing_is_not_zero
#print axioms krypton_unbound_is_not_missing

end VOTKP.Element8Intervals
