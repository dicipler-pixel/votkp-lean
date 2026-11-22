# G3 verification report: 08_elements.md and 17_tables.md

Paper: "What the Peel Keeps" v1.2. Files checked: /home/claude/paper_v12/build/src/08_elements.md and 17_tables.md. Nothing in the paper was edited.

Sources used, all read only:
- the threshold archive /home/claude/votkp-lean/data/element_thresholds_20261011.json.gz (sha256 75e67478...; the 118 records, 85 of them H to At)
- the adopted electron affinities with widths (element_data_v1.js, ptable_data.json, batch12 to 17 affinities.csv, russell/.../H_to_At_thresholds.csv)
- the repo element folder, abbreviated R/ below: research/2026-11-20-element-paper-loop-wall/
- /tmp/vk/v3_3.txt
- the Lean files, with the recorded build output in lean/run_checks_output.txt

Scripts, all under /home/claude/paper_v12/verify/scripts/ and run with `python3 -I`:
- g3_core.py: counts
- g3_recompute.py: affinity ledger, boxes, windows
- g3_openings.py: opening map and address classes
- g3_screening.py: S and sigma
- g3_loop.py: loop, francium, gold and mercury
- g3_tables.py: Appendix B and D

## A. Non-VERIFIED rows (WRONG, OVERSTATED, UNTRACEABLE)

| file | quoted claim | verdict | evidence / correction |
|---|---|---|---|
| 08 (anion rung paragraph) | "Silicon's anion rung is the closest call: Γ = 0.70873 against the wall at 0.70711" | WRONG | Silver is closer. Γ0(Ag) = 0.70622, which is 0.00089 from the wall; Γ0(Si) = 0.70873, which is 0.00162 away. In z the distances are Ag 0.0205 and Si 0.0381. R/batch11/robust/CUTOFF_H_CS.md:24 says "silver k=0 remains the closest anion, distance 0.020525"; R/batch12/chemistry/audit.txt gives Ag +0.0046 eV against Si -0.0091 eV in affinity. Silicon is the closest outside rung; silver is the closest rung overall. The Γ and Lean numbers themselves are right (`rung0_Si_low` and `rung0_Si_high` exist, lean/LoopWall.lean:230-231). |
| 08 (screened core series) | "removing the 5Z/8 term moves the crossing to about 9.47, between fluorine and neon" | OVERSTATED | I solved z_core = 3+2√2 numerically. Removing only the 5Z/8 term (keeping +0.157666) gives Z* = 9.5478. 9.47 (9.4700) is reached only when the whole core numerator is the bare Z²/2, i.e. both 5Z/8 and the 0.157666 constant are dropped. That is Lean's `IcoreBare` (lean/LoopWall.lean:139-141: "crossing between 9 and 10"). Both values lie between fluorine and neon. The same wording appears in 05_two_votkps.md:44. The wording should say "unscreened core Z²/2". |
| 08 (opening map, DERIVED paragraph) | "After its first element each sequence is inside at once." | OVERSTATED | True for the neon, argon, krypton and xenon cores (g3_openings.py: first inside index 1). The helium core stays outside for four elements (Li, Be, B, C), as the same paragraph and the table say ("4, 1, 1, 1 and 1 steps"). |
| 08 (strongest ordinary step) | "changes rank inside the second and third rows: ... Mg to Al ... K to Ca" | WRONG (period labels) | Mg and Al are period 3; K and Ca are period 4. The swaps themselves are verified (lean/LoopWall.lean:245 and :300; Al strongest is the helium-core opening at index 11, K strongest is the argon-core opening, Ca strongest is the helium-core opening). The phrase should read "third and fourth rows". |
| 08 (prediction tested) | "PREDICTION TESTED. Written at 09:24 on 21 November 2026, before the numbers were opened ..." | OVERSTATED (scope) | Time and content verified (R/CLAUDE_REVIEW.md:363-376; R/README.md:16). The source labels it "side-agent values, untested on the archive". R/holdouts/heavy_anions_protocol.md says these were "informed predictions using remembered chemistry values, rather than a laboratory blind test" and that the eight are correlated, not independent trials. R/holdouts/RESULTS.md says "the predictions used prior knowledge of chemistry". The paper's passage does not carry that scope. |
| 08 (frozen Rb/Sr call) | "I wrote the call down: rubidium outside, strontium inside" | OVERSTATED (attribution) | Call and timing verified, with the line "I left those energies uninspected" (R/gpt_batches/batch4b_matched_junction.md:36, tagged "HYPOTHESIS — frozen prediction"). It sits in the gpt_batches file, written in an AI collaborator's voice, not in a dated Jeromie-authored record. Both outcomes hold (6.5331 and 3.8878; `frozen_prediction_Rb_Sr`, lean/OpeningMap.lean:4291). The attribution "I" should be confirmed with Jeromie. |
| 08 (window section) | "The carbon and nitrogen K-resonance areas already show the distinction: their reported areas overlap within quoted uncertainties." | OVERSTATED (reads backwards) | R/batch8/README.md:21 says: "The K-resonance areas overlap in their reported uncertainties. Comparison-disk closure does not imply a measured disappearance of the inner-shell channel." The overlap means the measured areas do not separate carbon from nitrogen. "Already show the distinction" says the opposite. |
| 08 (francium) | "Only a measured IE2 in [23.654, 23.893) eV ... would separate the exact wall from every other allowed cutoff" | OVERSTATED | R/PREDICTION_FRANCIUM_20261121.md says "Only a value inside that 0.24 eV band separates the wall from the other cutoffs the data allow". A value inside the band separates the wall only from the cutoffs on the far side of that value, not from "every other" cutoff. The band edges are right: 5.8079020598 × 4.0727411 = 23.6541 and 5.8665387761 × 4.0727411 = 23.8929. |
| 08 (francium) | "IE2(Fr) < 23.738 eV" | OVERSTATED (rounding) | Exact threshold is 4.0727411 × (3+2√2) = 23.7376747 eV. Rounding up to 23.738 is harmless only as a display value; the source also writes 23.738. Noted only. |
| 08 (opening map table and text) | "Rubidium and caesium already appear in my dated November VOTKP paper, whose Figure 35 places the non-helium core-line crossings after their alkali metals" | VERIFIED with a note | /tmp/vk/v3_3.txt (v3.3, 12 Nov 2026): "Figure 35. The step that opens each closed core ... the others cross directly after the alkali metal; francium starts inside." Note that v3.3 says "francium starts inside" while v1.2 says it "straddles". That is a deliberate update, not an error. |
| 08 (RECOGNISED, anion rung) | "the nearest published special ratio is IE/EA = 3" | UNTRACEABLE | The only source is the internal note R/QUANTUM_CHEMISTRY_LINKS.md:26-27 ("validity bound in Gázquez and co-workers"). A web search returned the Gázquez, Cedillo and Vela electrodonating and electroaccepting powers paper, but I could not read the passage that states the I = 3A condition. The Parr and Pearson 1983 and Parr, von Szentpály and Liu 1999 citations are real: JACS 105, 7512 and JACS 121, 1922, "Electrophilicity Index", DOI 10.1021/ja983494x. |
| 08 (RECOGNISED) | "Among the alkaline earths only beryllium and magnesium have no stable anion" | OVERSTATED (scope) | True for Be, Mg, Ca, Sr, Ba in the ledger (Ca, Sr, Ba bound; Be, Mg none). Radium is outside the H to At table and has no affinity entry, so "among the alkaline earths" is only established through barium. |
| 08 (Reproducibility) | "the historical CSVs have 3,739 rows because the early magnesium ladder omitted its blank anion slot" | UNTRACEABLE | The 3,740 rebuilt rows are verified (R/russell/prediction_review_20261121/H_to_At_thresholds.csv has 3,741 lines with header, i.e. 3,740 rows; table_v1_1/README.md says "3,740-row"). I could not find 3,739 or the Mg blank-slot statement in any file. The Mg k=4 display 0.12800 against 0.127953665550 is verified (R/checks/check_batch3_v1_output.txt:1). |
| 08 (Reproducibility) | "The data supplement carries the full threshold table, a one-row-per-element index, the field-level discrepancy file and a standalone reconstruction script." | UNTRACEABLE | No Zenodo or supplement manifest in the paths I was given. Outside this group's sources. |
| 17 Appendix B and D, scandium | Appendix D EA 0.17938, IE/EA 36.5787; Appendix B anion cell 36.5787 (0.9468) | WRONG (small) | The paper itself says the adopted EA is 0.179378 eV and the zero-rung ratio is 36.579123 (verified: R/.../H_to_At_thresholds.csv:232 gives EA 0.179378, z = 36.579123415). The two tables use the rounded display EA 0.17938 (z = 36.57872). Γ0 = 0.94678 and ω/η = 0.5578 are unchanged. The appendix cells should read 36.5791. |
| 17 Appendix B, 6 cells | Li K opening 14.0290; Cl K opening 4.5210; V argon-core 1.9627; Eu krypton-core 1.1798; Pr anion 50.0797; P anion 14.0457 | WRONG (last-digit rounding) | Exact values: Li 14.028949 (should show 14.0289); Cl 4.520950 (4.5209 under round-half-up of the exact value); V 1.962650 (1.9626); Eu 1.179750 (1.1797); Pr 50.079648 (50.0796). Li, Cl, V, Eu and Pr are double-rounding artefacts (rounded to 5 places, then to 4). P is 14.045754 with the adopted EA 0.746609, so it should show 14.0458. Appendix D repeats the P and Pr values (14.0457 and 50.0797). No classification changes; Γ values agree. |
| 17 Appendix C, 19 cells | e.g. Z=15 S 0.61967, Z=22 S 0.62939, Z=28 σ 0.50057, Z=47 S 0.67906 | WRONG (last-digit) | Recomputing from the archive with 1 Ha = 27.211386245988 eV, 65 of 84 rows match to all printed digits. The other 19 differ by one unit in the fifth decimal (Z = 15, 22, 26, 28, 29, 31, 33, 34, 36, 37, 39, 40, 42, 44, 45, 46, 47, 49, 55). Probably a different conversion or rounding path. The five event positions and the Z-by-Z signs are unaffected. |
| 17 Appendix B | row names and prose spelling: "Aluminum" and "Cesium/Caesium" | note | Appendix B and D use "Aluminum", while 08 uses "aluminium" and "caesium". Spelling only. |
| 08 (opening map, RECOGNISED) | "Palladium's anion rung is its own filled 4d^10 opening" and "filled 3d^10 and 4d^10 openings decline across their rows" | VERIFIED | The 3d^10-core column is 2.626 to 1.852 for Z = 29 to 36, strictly falling; the 4d^10-core column is 2.836 to 1.697 for Z = 47 to 54, strictly falling (g3 inline computation). R/CLAUDE_REVIEW.md:186 says "the filled 4d^10 opening first appears as palladium's anion rung". |

## B. Verified items (grouped; paper sentence, then evidence)

Counts, from g3_core.py and the repo scan:
- "3,655 positive-index energies are 290 experimental, 847 semiempirical and 2,518 theoretical": VERIFIED, g3_core.py gives 3655 with E 290, S 847, T 2518.
- "3,655 − 85 = 3,570 ordinary steps": VERIFIED.
- "2,144 adjacent pairs Rn to Og, giving 5,714": VERIFIED. My naive count gave 2,167; the repo scan R/russell/prediction_review_20261121/ground_state_search/scan.py (which requires q+1 present, positive energies; the Rf, Db, Sg, Bh, Hs, Mt and Ds ladders have gaps) prints "all 5714 ... H–At 3570 ... Rn–Og 2144 ... incomplete 23 overlaps 1".
- "65 anion rungs adopted; 67 numeric with the Dy 0.015 and Tm 0.032 estimates": VERIFIED. The ledger holds 65 adopted entries (Z list lacks 66 and 69), and 67 numeric once the estimates are added.
- "Eight ordinary steps and 53 of the 65 anion rungs lie outside (55 of 67)": VERIFIED. g3_recompute.py gives 8 ordinary, 53 of 65, 55 of 67. The eight are Li 14.0289, Be 8.4507, B 6.8381, C 6.0795, Na 9.2013, K 7.2858, Rb 6.5331, Cs 5.9471.
- "Of 3,637 numeric comparisons, 3,614 have two quoted widths; all keep their wall side": VERIFIED. 3,637 numeric; 3,614 with a box; bad = 0 across all boxes; 284 rectangles cross z = 1.
- "Rank of 12 inside rungs": VERIFIED. Inside rungs are F, S, Cl, Se, Br, Ag, Te, I, Ir, Pt, Au, At.
- "Gallium to bromine: outside, outside, outside, inside, inside; arsenic above germanium": VERIFIED. Ga 19.92, Ge 6.41, As 12.17, Se 4.83, Br 3.51; As IE 9.789 above Ge 7.899 and EA 0.804 below 1.233.
- "Neon's helium-core ratio strictly greater than five": VERIFIED. 5.0014.

Windows:
- Ordinary central [5.6396654003, 5.9471008342), nitrogen k=5 to caesium k=1: VERIFIED, g3_recompute.py.
- All numeric central [5.8079020598, 5.8665387761), silver to silicon: VERIFIED.
- Complete-rectangle window [5.8080102725, 5.8665142305): VERIFIED. Ordinary box [5.6396892625, 5.9470854253) also matches R/holdouts/cutoff_window_through_At.csv.
- "with silicon's 2024 isotope-resolved affinity the upper edge is 5.866513048": VERIFIED, R/batch10/robust/cutoff_results.txt:26 (5.866513048392).
- "The window is 0.059 wide and 3+2√2 = 5.8284 sits inside": VERIFIED. Width 0.05864; wall 5.82843.
- "Caesium is the first ordinary step that a cutoff of 6 gets wrong": VERIFIED.
- "Across all 5,714 central ratios no ratio separates the wall from the registered midpoint rival; of 5,691 pairs with both widths, one interval overlaps (francium); 23 lack a width": VERIFIED, scan output "central hits 0 overlaps 1 incomplete 23".

Opening map (g3_openings.py):
- Ratios 101, 100, 92, 74, 49, 17 = 433, first elements and values (Li 14.029, Na 9.201, K 7.286, Rb 6.533, Cs 5.947, Fr 5.500), outside sets, and crossing positions after 4, 1, 1, 1, 1 steps: VERIFIED. The crossings are C to N, Na to Mg, K to Ca, Rb to Sr, Cs to Ba.
- "All 433 openings are certified in OpeningMap.lean": VERIFIED. Counting `inside (` and `outside (` in the core theorems gives He 101, Ne 100, Ar 92, Kr 74, Xe 49, Rn 17 = 433. Build recorded as "BUILD OK: OpeningMap, 117 theorems".
- "Francium range 5.03 to 5.97 straddles the wall": VERIFIED. Box [5.0335, 5.9665] from 22.4 ± 1.9 and IE1; `francium_straddles` exists.
- "The first ratio falls core by core: 14.03, 9.20, 7.29, 6.53, 5.95": VERIFIED.
- "Caesium (5.95) is the smallest outside ordinary value": VERIFIED.
- "Bare hydrogenic floors 4, 9/4, 16/9, 25/16, 36/25, 49/36 all inside": VERIFIED.
- "Mg and Ca all-ordinary-inside; so are Sc to Zn, Ga, Sr, Y to Ag, In, Sn": VERIFIED. 76 elements have all ordinary steps inside, including these; `mg_all_inside` and `ca_all_ordinary_inside` exist.

Loop and Lambert numbers (g3_loop.py, mpmath 30 digits):
- Equal-face border z = 3+2√2; Γ = 4/5 and 3/5 for a = 9, b = 4 tangent pair; b*(a) formula: VERIFIED. sinh(½ ln 9) sinh(½ ln 4) = 1 exactly; b*(7) and b*(12) also give product 1.
- "Γa²+Γb²<1 iff interior meeting": VERIFIED algebraically (sinh h = Γ/√(1−Γ²)).
- z = 6 gives Γ = 5/7; z = 1/6 gives −5/7; Γ = 2/3 at z = 5; ratio 4 gives 3/5: VERIFIED (`two_thirds_iff`, `hydrogenic_limit`, lean/LoopWall.lean:79-83).
- "carbon's held, other face swept: opens at z = 5.591156": VERIFIED (5.5911562008).
- "rubidium held, other face swept: opens at 5.222848": VERIFIED (5.2228475290).
- "carbon on one face, nitrogen on the other: open, barely (+0.00309)": VERIFIED as Γ1²+Γ2²−1 = +0.003093 (R/connections/checks_transport/check_loop_selection_v1_output.txt:19). The table does not name the quantity; the text above it defines the open condition as Γa²+Γb² > 1, so the reading is natural. In sinh a · sinh b − 1 terms the value is +0.00621.
- Carbon and nitrogen helium-core ratios 6.0795 and 5.6397 and "both faces open / closes": VERIFIED (sinh² = 1.061 and 0.954).
- Rb 6.5331, Sr 3.8878, "rubidium's on one face, strontium's on the other closes": VERIFIED (sinh product − 1 = −0.2074).

S and σ (g3_screening.py):
- Definitions, identity Z(S−σ) = (h − Z²/2) − σ²/2, `readouts_identity` (lean/LoopWall.lean:309), `bare_S_above_sigma` control: VERIFIED. The identity was also checked numerically to 1e-9 for all 84 elements.
- Event positions: σ crosses 5/8 between Ne and Na; S crosses σ between Al and Si; S crosses 5/8 between Ar and K; σ falls through ½ between Ni and Cu; σ negative between Pd and Ag: VERIFIED.
- "S = 5/8 − 0.157666/Z, σ = 5/8 + 0.037646/Z": VERIFIED. 0.037646 = 0.1953125 − 0.157666 (σ coefficient 0.0376465).
- "Z* = (4σ²/α²)^{1/4} = 13.0 for σ = 0.617": VERIFIED, 13.0039.
- "without recoil the σ = 5/8 event moves to between fluorine and neon": VERIFIED. R/QUANTUM_CHEMISTRY_LINKS.md:90-92 states it, and a leading-order recoil estimate with Ne mass 19.99 to 20.18 gives σ(Ne) = 0.62489 < 0.625.
- "They pass near 0.617": VERIFIED. S and σ are 0.6167 and 0.6179 at Al, 0.6182 and 0.6148 at Si.
- "Appendix C" claims in 08 ("full table is in the appendix"): see the Appendix C row above.

Screened series:
- Z* = 6.538 (6.5385): VERIFIED.
- The formula (Z²/2 − 5Z/8 + 0.157666)/(Z²/8 − (290/729)Z + 0.2505) is the Lean `Icore`/`Ival` (lean/LoopWall.lean:134-135): VERIFIED.
- Z = 6 outside, Z = 7 inside, `screened_six_outside` and `screened_seven_inside`: VERIFIED.
- Screened ratios against the archive: 6.09547 against 6.07953 (0.262%), 5.64841 against 5.63967 (0.155%), 5.35859 against 5.35283 (0.108%), 5.15546 against 5.15101 (0.086%), 5.00518 against 5.00135 (0.077%). VERIFIED, so "0.08 to 0.26 percent" holds.

Anion rung:
- Γ0 = η/χ and ω/η = 1/(2Γ0²): VERIFIED, `gam_anion_rung` and `omega_eta_wall`.
- χ/η = √2 at the wall: VERIFIED.
- (I+A)² − 2(I−A)² = −(I² − 6IA + A²): VERIFIED, lean/LoopWall.lean:528-529.
- Critical A = I(3−2√2): VERIFIED. At Po I = 8.41807 it is 1.444312474 eV (R/holdouts/RESULTS.md).
- x* = χ/(2η) = 1/(2Γ0) = 1/√2 at the wall, drop χ²/(4η): VERIFIED.
- ΔNmax = χ/η = 1/Γ0 = √2, "twice the threshold-matched value": VERIFIED.
- Silver ω/η 1.0025 and silicon 0.9954: VERIFIED.
- Ca, Sr, Ba affinities 0.02455, 0.05206, 0.14462 eV and z = 249.0, 109.4, 36.0: VERIFIED.
- "In the gravity ledger the anion rung's metric determinant is IE × EA": VERIFIED, R/connections/gravity_connections.md:108 and :114.

Heavy anions:
- Au 3.996, Pt 4.216, Ir 5.733, At 3.857 inside; Os 7.830, Bi 7.731, Pb 20.79 outside: VERIFIED (R/holdouts/heavy_anion_scores.csv; `heavy_anion_prediction`).
- Po: JyvIS 11,905.631(9) cm^-1, A = 1.4761101164 eV, z = 5.702874: VERIFIED.
- Po: critical A 1.444312474 eV: VERIFIED.
- Po: barium-donor/polonium-acceptor 5.2117/1.476110 = 3.531: VERIFIED (5.21166/1.47611 = 3.5306).
- "Gold and platinum form monatomic anions in real compounds": traceable to R/QUANTUM_CHEMISTRY_LINKS.md:37 ("aurides, platinides"); no primary citation in the repo.
- Holdout rule: trained H to Xe, 20 of 20 outside correct, 0 of 4 inside, balanced accuracy 0.50, misses Ir, Pt, Au, At: VERIFIED, R/russell/prediction_review_20261121/address/address_review.md and results.txt ("majority ([20, 0, 4, 0], 0.833, 0.5)").
- "strongest opening deeper than first eligible core for 70 of 83 elements": VERIFIED. results.txt first-versus-dominant pairs: 17+6+17+30 = 70 different of 83.
- "1,304 to 366 indistinguishable pairs": VERIFIED (extended ledger, with Dy and Tm estimates included).

Address (g3_openings.py):
- Class table 7, 1, 45, 12, 18, 1, 1 (sum 85): VERIFIED. Member lists:
  - out/out: Li B C Na K Rb Cs
  - none/out: Be
  - out/in: 45
  - in/in: F S Cl Se Br Ag Te I Ir Pt Au At
  - none/in: 18, N Ne Mg Ar Mn Zn Kr Cd Xe Pm Sm Dy Ho Er Tm Yb Hg Po, consistent with the paper's list of noble gases from neon on, magnesium, nitrogen, zinc, mercury
  - out/none: H
  - none/none: He

Francium and gold/mercury (g3_loop.py):
- Fr 23.738 (23.7377); [23.654, 23.893); (23.73768111, 23.77348109) with the IE1 half-width: VERIFIED (R/russell/.../ground_state_search/REPORT.md:13).
- NIST [22.4] ± 1.9: VERIFIED in the archive.
- z = 5.361114977 and IE2 = 21.834433307 eV from z_next = 2 z_last − z_previous: VERIFIED. R/russell/.../francium/REVIEW.md:7 and R/russell/.../FR_SECANT_HINDCAST_v1.md.
- Alkali hindcast: K 4.3737 (actual 7.2858), Rb 5.3702 (6.5331), Cs 5.7804 (5.9471), 0 of 3: VERIFIED.
- Gold 4.00189784 and mercury 3.99780412: VERIFIED.
- Intervals [4.001832223, 4.001963460] and [3.997740439, 3.997867804]: VERIFIED.
- All 82 consecutive boxes Li to At strictly descending: VERIFIED. Both heavy inputs in each pair are T grade: VERIFIED.
- Secant inside 2 of 15 (Lu, Hg); corrected spinor formula 0 of 15: VERIFIED, R/holdouts/k_opening/scores.csv.

Transfer test:
- 72 of 72, 14 of 24, 15 of 24: VERIFIED (R/batch9/fingerprint/FINGERPRINT.md, R/batch13/fingerprint/score.txt).
- Primary boxes 11 certain correct, 3 certain miss, 10 ambiguous: VERIFIED.
- Ce2+ primary contrast 0.018854 and required class below −0.163945: VERIFIED (R/batch13/fingerprint/xenon_predictions.csv: Ce q = 2, D = 0.0188541018, offset 2; boundary −0.16394532).
- 605 removals Ba to Tb, 595/9/1, Gd 1, 2, 1 removed by the alternative sequence: VERIFIED, R/batch13/traits/README.md:14 and :20.
- K = Σ min(a,b), R = Σ (b−a)+, N_after = K+R, ‖a−b‖1 = 2R+1: VERIFIED, README.md:8-10.

Physical checks:
- Ho/Dy: Q(56) = +1.9514 keV, Q(57) = −4.5186 keV, increment −6.470 keV, 11 and 10 electrons at 56+, restarts from 38+/39+/40+ keep the bracket, scale 0.01 erases the crossing: VERIFIED, R/batch14/materials/holmium_dysprosium_decay.md and R/batch14/mass_anchors/README.md.
- Pb/Tl: crossing between 79+ and 80+; 2.329 keV; 31.0715 keV (31,071.5295 eV, tl_pb_decay.csv last row); 31.1(5) keV published: VERIFIED.
- Re: 63.005 keV, 9.756 keV, −7.285 keV, 2s channel straddles zero: VERIFIED, R/batch15/materials/RHENIUM_DECAY.md:43 and :47.
- Nd two dhcp sites with first twelve distances and second moments equal, differing third moment: VERIFIED, R/batch12/site_symmetry/README.md.
- Po alpha/beta six neighbours, shortest +0.268%, volume −2.656%: VERIFIED, R/batch17/materials/README.md:63-67.
- Os at 650 nm 0.4846 and 0.5285: VERIFIED, R/batch16/materials/README.md:44-47.
- At-197 +4215 MHz and −1868 MHz: VERIFIED, R/batch17/materials/README.md:105.
- Yb coexisting refinements lengthen contacts while volume falls: VERIFIED, R/batch14/materials/ytterbium_structure.md:16 (contact differences +0.0503 and +0.0457 Å with volume differences negative).

Reproducibility:
- 3,655 cells match the archive, 3,740 rebuilt rows: VERIFIED (3,740-row CSV).
- Mg k = 4 0.12800 against 0.127953665550: VERIFIED.
- Se 1e-27 discrepancy: VERIFIED, R/batch12/chemistry/audit.txt:5 (the two values differ at about 1e-27).
- Corrections V k = 11, Cr k = 9 and k = 20, Ni k = 21, Cu k = 5: VERIFIED, R/README.md:161-168. No classification changes.
- 2,114 of 2,115 ASD records agree, Nd 5.5250(6) to 5.52475(5): VERIFIED, R/checks/audit_second_hour.txt and R/SECOND_HOUR_20261121.md.

Citations and framing:
- Parr and Pearson 1983 (JACS 105, 7512); Parr, von Szentpály and Liu 1999 (JACS 121, 1922): real references (web search confirmed the 1999 one; the 1983 DOI is in R/QUANTUM_CHEMISTRY_LINKS.md:21).
- "the electron's spinor (Dirac) structure" wording: in line with the brief; no "relativity" appears in either file.
- No "CN" abbreviation and no slash pairs in the prose. Slash-pair check: the section headers "DERIVED / FAILED TRANSFER", "DERIVED / CONTROL" and the 08 line "Parr, von Szentpály and Liu" use slashes as label separators only. The brief says "no slash pairs"; these label slashes are section tags and may need a decision by the caller.

## C. Spot checks and full checks of the appendix tables (against the archive)

- Appendix B (85 rows): every row checked programmatically, not sampled. For each row, first IE, the anion cell (z, Γ, bold flag), and the K, L, argon, krypton and xenon-core opening cells (z, Γ, bold flag) were recomputed from the archive with the adopted affinities. 79 of 85 rows match exactly. The other 6 differ only in the last printed digit of one cell (Li, P, Cl, V, Pr, Eu; see section A). Bold flags are all correct. Dy and Tm carry "estimate", Po carries "preliminary", none matches the ledger. The Sc anion cell is off in the fourth decimal as above.
- Appendix C (84 rows, Z = 2 to 85): every row recomputed. 65 match to the printed digits, 19 differ by one in the fifth decimal (see section A). Sign column S−σ agrees in every row; the S = σ sign change falls at Al to Si as stated.
- Appendix D (65 rows): every row recomputed. EA, IE/EA, Γ0, ω/η and side agree, and the table is ordered by IE/EA. Differences: Sc (36.5787 against adopted 36.5791), P 14.0457 (14.0458) and Pr 50.0797 (50.0796). 12 inside rows then 53 outside rows, matching the 12 inside and 53 outside counts.
- A 20-row random sample was not needed, because all rows of each appendix table were checked. For the brief's "at least 20 random rows" requirement: all 85, 84 and 65 rows exceed it.

## D. Counts

- Claims checked: about 160 sentence-level claims and numbers across 08_elements.md and 17_tables.md (plus 234 appendix table rows checked in full).
- VERIFIED: about 140, including the VERIFIED-with-note rows.
- WRONG: 5 (silicon "closest call"; "second and third rows"; Sc appendix cells; 6 Appendix B last-digit cells; 19 Appendix C last-digit cells).
- OVERSTATED: 8 (9.47 wording; "inside at once"; prediction scope; frozen-call attribution; K-resonance overlap; francium "every other cutoff"; 23.738 rounding; alkaline earths scope).
- UNTRACEABLE: 3 (IE/EA = 3 published special ratio; 3,739 rows with Mg blank slot; data supplement contents).
- Open to the caller: whether the "/" label separators in the DERIVED / ... tags count as the forbidden slash pairs.
