# VOTKP complete test ledger (tag: ledger), 12 Nov 2026

Scope: finishes DOSSIER_T8 using Appendix D of v2.9/v3.0, all 21 PREREG files, TEST_LOG, TEST_RECORD, CHECK_REPORT_V29, the 7 Nov PATH_NOTES, NOTES_06/07/08, rounds 5-6, and the 10-12 Nov script headers. No web. Nothing run except sha256 and arithmetic (scripts saved here: `verify_prereg_sha.py` + `.out`).
His framework first: kills are stated in his terms (peel step z, Smith point G, half line G^2 = 1/2, two books). Grades are the sources' own.

## Conventions

- Kill-line source tag: **[R]** = text read in the registration file in this pass (matches Appendix D unless a note says otherwise). **[S]** = script header. **[TL]** = TEST_LOG/TEST_RECORD declaration (v0.1 tests T-A..T-S have no registration file; the paper's kill lines were "fixed in v0.1 section 15", which is not on disk). **[D]** = dossier/Appendix D wording only; no registration or header text on disk.
- abs(x) written for the modulus.
- Rerun column, from CHECK_REPORT_V29: **REPRO** = reproduced (exact, or float tails only); **DIFF** = differs (value given); **NOT RERUN** = needs snappy/spherogram/nucleardatapy (reason given); **NO SCRIPT** = no script in package; **OUT OF SCOPE** = 7-12 Nov work, after the v2.9 package (not covered by CHECK_REPORT_V29; I read the stored outputs only, did not rerun).
- "2nd/opp" = was an opposite or second setup ever run (Y with what / N).
- Registration times (UTC, 23 Sep unless stated) come from the file stamps in Appendix D and the PREREG files. "Run" = the same day unless stated; no run timestamps are stored for most scripts.

---------------------------------------------------------------------
## A. THE TABLE

### A1. v0.1 test plan T-A..T-S (23 Sep; declared in TEST_LOG)
Header of TEST_LOG: kill lines for T-A..T-J "fixed in paper v0.1 section 15 at about 13:46Z". T-E, T-F, T-K..T-S carry their own declaration times below (14:06Z onward), so these were declared 20 to 50 minutes after the stated 13:46Z. See C1 item 25.

| Name | Reg / run | Tests | Kill line | Outcome | Script | Rerun | 2nd/opp |
|---|---|---|---|---|---|---|---|
| T-A adjoint Jones, 5 HOMFLY-blind pairs | 13:46Z? / 23 Sep | coloured number separates and orders the five pairs | [TL] "a pair equal at the phase with different volume" | 5/5 separated and ordered; abs(J3) 0.914/6.197, 18.01/23.96, 46.11/52.36, 73.07/79.85, 107.84/122.63 | ta_adjoint.py, ta_census.py, ta_controls.py | NOT RERUN (spherogram) | Y: q = e^(8 pi i/15) reading separates 5/5, orders 3/5 |
| T-A+ census | same / same | one coloured number vs volume, knots to 10 crossings | none (census) | Spearman 0.992; Vol = 2.979 ln abs(J3) - 0.658; 4.87% mean; 205 knots | ta_census.py | NOT RERUN | Y: other q reading Spearman -0.08, 34.7% |
| T-K | 14:14:38Z / 23 Sep | frozen line on 60 unseen 11-crossing knots | [TL] "error > 10% or Spearman < 0.9" | 2.847% (recomputed from JSON), 0.992, max 10.3% | tk_holdout.py | NOT RERUN (snappy); recomputed from stored JSON: 2.847% | N (seed 11 only) |
| T-K2 | 14:37:58Z | same on 40 12-crossing knots | same | 2.942%, 0.993, max 13.5% | tk2_holdout.py | NOT RERUN; recomputed 2.942% | N |
| T-N | 14:19:24Z | is 8 pi/15 special | [TL] "some theta more than 0.3 rad away beats 0.992 by more than 0.005" | best 0.9922 at theta 1.6755 (stored tn.log); window 1.46-2.42 rad | tn_phase.py | NOT RERUN (stored log read) | the scan is the second setup |
| T-P | 14:28:09Z | colour adds beyond ordinary Jones | [TL] "best J_2 Spearman >= 0.992" | best J_2 0.982 (theta ~2.47); at 8 pi/15 0.258; margin 0.010 | not identified | NO SCRIPT | 60 phases |
| Controls (Perko; K-T/Conway) | 23 Sep | colour and volume agree on pairs | [TL] "colour differs, or volume differs" | abs(J3) 8.568882 both; 57.430110 both; vol 5.638772949 / 11.219117725 | ta_controls.py | NOT RERUN | N |
| T-J 11 / (<=10 vs 11) / 12 | 23 Sep | HOMFLY vs Alexander+Jones: first blind pair | [TL] "first such pair" | 0 pairs, 548/552 (4 hit 60 s cap); new blind pair 10_155 / K11n37; 12: 0 pairs, 2075/2176 | tj_blind11.py, tj_cross.py, tj_merge12.py | NOT RERUN (snappy/spherogram) | Y: within-set and cross-set |
| Blind pairs at 11 (44 pairs) | 23 Sep | volume vs colour on blind pairs | none stated | vol separates 28, 16 same-volume; colour 3 separates 24 of 26 computable pairs (TL: "48 of 52 rows"); exceptions K11a196/K11a216, K11n4/K11n21; J4 separates both | j4_sparse.py | NOT RERUN | Y: J4 |
| T-E | 14:06:52Z | A-polynomial volume integral, 4_1 | [TL] "integral differs from 2.029883212819307 beyond quadrature error" | 2.0298832128193074, diff 4e-16 | none | NO SCRIPT (TEST_LOG only) | N |
| T-E2 | 14:18:02Z | pi m(A) = Vol for 5_2 | [TL] "abs(pi m(A_5_2) - Vol) > 1e-8" | diff 1e-10 (no log located) | none | NO SCRIPT | N |
| T-F | 14:07:39Z | P_1 integer coefficients | [TL] TEST_LOG "non-integer coefficients"; TEST_RECORD "coefficients further than 0.01 from integers, or residual > 1e-4" | 4_1 zero (1e-14); 3_1 -t^-2+2t^-1-2+2t-t^2 (5e-13) | tf_mmr2.py | REPRO (tf_mmr2); tf_mmr predecessor DIFFERS (not a paper number) | two earlier set-ups failed numerically and were rerun |
| T-D | 23 Sep | energy rises with Q at fixed knot | [TL] "not monotone" | monotone every family; T(3,4) 7.857/8.272/8.761 at Q = 12/13/14 | none (literature, Sutcliffe 2007) | NO SCRIPT | read twice |
| T-B (Run 03) | 13:56:22Z | level carries response | [R] "T1 beats S2 in the majority of the 9 ... for ANY of the four targets, with a 95% interval excluding zero" | radius 9/9, atomic radius 9/9 static; hardness 8/9; EA 4/9; K=10 kNN MAE 0.347 vs 0.541 | run03.py | REPRO | Y: 2022-2025 affinities (run03_ea2026: EA 4/9, hardness 6 to 5, REPRO) |
| T-M | 14:17:16Z | alpha vs IE1 | [TL] "R^2 < 0.5" | ln alpha = 10.284 - 3.036 ln IE1, R^2 0.906 (0.9055 rerun), n = 86 | item4_rerun_01.py | REPRO | Y: 2025 table check |
| T-I | 13:56Z (Run 03 file) | noble-gas resets | [R] "fewer than 6 of 6 on a functional removes that functional" | IE1 6/6; no-anion 6/6; alpha 6/6; covalent radius 4/6 removed; atomic radius 2/6 (3 not scorable) | run03.py | REPRO | N |
| T-S | 14:38:10Z | first-step reset at alkalis | [TL] "fewer than 6/6" | 6/6: Li 2.641, Na 2.219, K 1.986, Rb 1.877, Cs 1.783, Fr 1.705 | none by name | NO SCRIPT | N |
| T-L | 14:14:53Z | Run 01 robust over 36 variants | [TL] "T1 fails to beat S2 in a majority of the 36 variants" | 35/36; only loss K=10 cosine k=5 unscaled (S2 0.548 vs T1 0.435) | tl_robust.py, run01_robust_infold.py | REPRO (35 of 36) | the 36 are the second setups |
| T-O | 14:27:43Z | extrapolate to period 6 | [TL] "T1 <= S2, or T1 < 0.5" | K=6 tie 0.667/0.667 (fires); K=10 18/18 vs 16/18 | c1_depth.py | REPRO (K=6 12/18, K=10 18/18 per CHECK) | Y: K=6 and K=10 |
| T-H | 23 Sep | prior art for reset ridges | none | physics known (Lyu-Keitel-Harman 2025); map not found | literature | NO SCRIPT | N |
| Ridge census | 23 Sep | ridge vs depth | none | r=10 92/92, 18 84/84, 28 74/74, 36 66/66, 46 56/56, 54 14/48, 60 22/42, 68 34/34 | th_ridge60.py | REPRO | N |
| T-Q | 14:35:44Z | thinning peel non-monotone | [TL] TEST_RECORD "claim needs >= 1, generic needs >= 6 of 12"; TEST_LOG "< 6 of 12" | 6/12 (Cu 450, 550; Au 450; Pt 450, 550, 650); Ag never | not identified | NO SCRIPT (no AppD row under this name) | N |
| T-C, T-G | v0.1 | deep peel on measured stages; common peel matrix | none | blocked (data not fetched); never run | none | NO SCRIPT | n/a |
| Prior-art cross-check | 23 Sep | published colour law on our abs(J3) | none | their frozen formula 3.60% (12 cr), 9.87% (11), 34.6% (<=10) vs ours 4.87/2.85/2.94 | TEST_LOG | NO SCRIPT | n/a |

### A2. Run 01-03, Snell, Smith, CLOSE, WIDE (23 Sep)

| Name | Reg / run | Tests | Kill line | Outcome | Script | Rerun | 2nd/opp |
|---|---|---|---|---|---|---|---|
| Run 01 ONION-ATLAS-01 | 11:35:18Z / 23 Sep | peel features T1/T2 beat same-data static S2 for group recovery | [R] "T1/T2 do not beat the SAME-DATA static coordinate S2 ... for the majority of (K, k) settings" | 0.95 vs 0.49 (v0.1); 0.951 vs 0.508 in-fold (v2.9 prints 0.51); K=3 0.515/0.412, K=6 0.738/0.415 | onion_atlas_01.py, 01b, run01_infold.py | REPRO | Y: 36 variants; shuffled 0.039 control (ESR) |
| Run 02 ONION-ATLAS-02 (polarizability) | 12:27:12Z / 23 Sep | peel beats static for alpha | [R] K1 "T1 beats S2 in 0 of 9 settings" is the kill form (K1, K2, K3 registered; K2 six noble-gas minima 6/6; K3 grade 3 of 9). File not in Appendix D table or in SHA256SUMS | 0/9; K2 6/6 | onion_atlas_02.py | REPRO | N (only the target changed in Run 03) |
| Depth ladder (CLOSE C1) | 17:12:55Z | accuracy vs K | [R] "at any K, a miss outside that set, OR the contained-set rule explains fewer than 80% of misses pooled over K" (Appendix D prints only the first clause) | 0.22 at K=1 to 0.89 at K=11; 1.00 at K=8-10; 62 of 65 misses explained; Hf, Ta only at 11-12 | c1_depth.py | REPRO | N |
| CLOSE C2 film height | 17:12:55Z | first-order bump height | [R] first-order height within 20% on the 6 bump cases AND Spearman >= 0.8 of order by A against bump height (Appendix D prints only "height error > 20%") | max 0.6%; 12/12 | c2_film.py | REPRO | N |
| CLOSE C3 Smith radius | 17:12:55Z (detail 17:14:56Z) | frozen threshold abs(G) = 0.856 | [R] kill accuracy < 85% | 87% frozen (rerun 0.871); 171/171 first-order; worst 3.1%; best threshold 0.994 at 0.9175 (v0.2 says 0.93, v2.9 0.92) | c3_general.py, film_baseline.py | REPRO | Y: held-out thresholds 0.977/0.959 (post-hoc) |
| CLOSE C4 colour ladder | 17:12:55Z | volume-different pair equal at J2, J3, J4 | [R] "a volume-different pair equal at J2, J3 and J4" | 21/21 J3-blind pairs separated by J4 in the stored file; certificate 21/21 equal Laurent polynomials (14 direct, 7 mirrored) | c4_ladder12.py, certify_ladder.py | NOT RERUN (snappy); stored file J4 differs 21 of 21 | Y: J2, J3, J4 |
| Snell K1 turning set | 17:02:17Z | turning set vs window rule | [R] null "outer electrons > 6" (flags 8, contains all 6); Appendix D calls it "window rule" | 1 hit vs 6 | run_snell.py | REPRO | N (two filling rules only) |
| Snell S2 labels | 17:02Z | confusion labels | [R] chance | 0/6 | run_snell.py | REPRO | N |
| Snell S3 | 17:02Z | refraction vs reflection | [R] "no threshold in abs(G) or arg G separates bump from no-bump with at most one error" | Spearman 0.613/0.680; threshold errors 0 vs 4 | s3_and_null.py | REPRO | N |
| Snell deep ridges | 17:02Z | 28 > 18 | none, no verdict line | flat | none | NO SCRIPT | N |
| WIDE N1 nuclear ridges | 22:15:53Z | magic ridges | [R] "any of (a)-(d) fails in the measured-only arm" (N2) | 6/6 measured, 5/6 with extrapolated | nuc_onion.py | REPRO (np repr only) | N |
| WIDE f-block cross-series | 22:15:53Z | f-block | [D] "<= 3/14 both ways" | 2/14 and 3/14 | fblock.py | REPRO | N |
| WIDE matter-wave slab | 22:15:53Z | closed form vs matrix | [D] | 3.5e-16; 400/400 | matter_wave.py | REPRO | N |
| WIDE shell evolution (4-point) | 22:15:53Z | exotic-cell coverage | [R] as above (any of four fails) | no measured coverage; raw step supports all four (post-hoc) | nuc_posthoc.py | REPRO (partly script) | N |
| Smith (171) first-order echo, baseline, circle Thm 6.2, oblique | 17:02Z | model checks | none | 171/171 within 3.1%; 9e-13; Airy = matrix 6e-16 | audit_exact.py, film_oblique.py | REPRO | N |
| HOMFLY vs A+J to 13; KnotInfo consistency; engine vs KnotInfo | v0.5 | census | none | 0 through 12; 19 at 13; 0 of 12,965; 0 of 18 | cat01_hom13.py, verify_hom13.py, chk_homfly.py | REPRO | N |

### A3. NUC, PART, ROUND-02, ADM, TIME, DATA, THIN (23-24 Sep)

| Name | Reg / run | Tests | Kill line | Outcome | Script | Rerun | 2nd/opp |
|---|---|---|---|---|---|---|---|
| NUC-01 Part 1 shape | 22:57:34Z | SHAPE beats NPNN and DVPN | [R] "SHAPE fails to beat BOTH NPNN and DVPN in both models (point estimate), or its advantage interval includes zero against both in both models" (Appendix D shortens) | SHAPE 0.649 vs NPNN 0.831: killed | nuc01.py | NOT RERUN (needs nucleardatapy); stored nuc01_output.txt read | N |
| NUC-01 Kill 2 level to radius | 22:57:34Z | LEVEL beats SHAPE | [R] "LEVEL does not beat SHAPE in both models" | 1 of 2 (MAE shape 0.0364 / level 0.0344 lin; 0.0334 / 0.0370 knn) | nuc01.py | NOT RERUN | N |
| NUC magic ridges | same | ridges | [D] "< 5/6 above the 90th pct" | 6/6 measured, 5/6 extrapolated | nuc_onion.py | REPRO | N |
| H-01 echo weight | 24 Sep 00:13Z (PART) | echo weight separator | [R] "abs(1 - G^2) fails to beat abs(G) held out" | 0.743 vs 0.977/0.959 | h01_lorentz_separator.py, h01b_midpoint.py | REPRO | N |
| P-01 tight-knot lengths vs lattice | 00:13Z | lattice agreement | [R] "abs(R_knot - R_lat) > 3 sigma" (statistical error only; inputs read before the file was written) | 3.14 sigma corrected, 2.37 uncorrected (v1.2 says 2.8 combined) | p01_p02.py | REPRO | Y: both length sets |
| P-02 constituent axis | 00:13Z | reproduction | none | H- 2.892, D- 2.892, Ps- 3.036 | p01_p02.py | REPRO | N |
| NUM-01 (ROUND-02) | 01:07Z | numerator vs denominator | [R] "numerator fails to beat denominator" | N 0.392 vs D 0.267 (two parser corrections) | num01_run.py | REPRO | N |
| CAT-01 | 24 Sep | categorified rung | [D] "volume-different blind pair left unseparated" | 233 of 253 unseparated; thin same-signature 0 of 2,525 separated | cat01_hom13.py, cat01_mechanism.py | REPRO | N |
| ADM-01 A-poly at L=1 | 08:26Z | simple root missing | [R] | none (3 knots) | apoly_L1.py | REPRO | N |
| ADM-01 WALL-01 | 08:26Z | entry away from a root | [R] | 0 of 17,360 | wall01.py | REPRO | N |
| ADM-01 parity | 08:26Z | roots change by +-2 | [R] | 16,656/16,656 | jump02.py | REPRO | N |
| SIG-01 | 08:26Z | signature function separates thin same-signature pairs | [R] "separates none of 2,525" | 1: 13a_3542 / mirror of 13a_4018, certified exactly (the dossier's "3545" was an image misread) | sig01_02.py, verify_sig_pair.py | REPRO (pair certified); verify_sig_all/chirality NOT RERUN | N |
| SIG-02 torus maxima | 08:26Z | maximizer | [R] "a torus knot not the maximizer at some n" | unique maximizer every n | sig01_02.py | REPRO | N |
| TIME-01a | 10:02Z | torus counts | [R] "count != abs(sigma)/2" | 135/135 | time01a.py | REPRO | N |
| TIME-01b pump | 10:02Z | charge per cycle | [R] "charge per cycle off an integer by > 1e-3" | Chern 1.000000; real time 0.99895 (miss 1.05e-3 as registered) | time01b.py | REPRO | Y: midpoint sampling 1.00014-1.00016 (post-hoc) |
| TIME-01c | 10:02Z | 13-crossing window | [R] "no representation inside" (names 13a_3542 and 13a_4018) | 1 per knot inside alpha 0.10971-0.11522; none below | time01c.py | DIFF: outside-window counts (13a_3542 at alpha 0.18: 29 stored, 30 rerun); inside-window REPRO | N |
| TIME-01d above | 10:02Z | above the wall | none | stored N=4, rerun N=3 | time01d_above.py | DIFF (N=4 vs N=3) | N |
| TIME-01d/e (post-hoc) | 10:02Z | longitudes | none | -0.0145346 vs -0.0171689 at alpha 0.11247 | time01e_refine.py | REPRO (tails) | N |
| DATA-01 period 6 | 10:50Z | perturbation of data | [R] "median < 16/18 or 5th pct < 14/18 at K=10" (prereg Arms M and P are descriptive; Appendix D has only an "E-only arm" row) | median 17/18, 5th pct 15/18, 18/18 in 14% | data01.py | REPRO | Y: Gaussian 17/15, uniform 17/16, shared 18/17 (post-hoc) |
| DATA-01 run 01 | 10:50Z | | [R] "median < 0.90 at K=10" | 0.918 | data01.py | REPRO | N |
| DATA-01 E-only arm | 10:50Z | | none | not possible: no test element beyond | data01.py | REPRO | N |
| THIN-01 P1 continuous | 12:16Z | same side of bulk | [R] "P1 >= 13/15 same side and median abs(dR) <= 0.02" | 11/15; median 0.0104: killed on side | thin01.py | REPRO | Y: 10-20 nm 6/6, 35 nm 5/6 (post-hoc; registration omitted Ciesielski 35 nm) |
| THIN-01 P2 percolation | 12:16Z | thin vs thick | [R] "P2 median > 2x P1" | 1.3x (0.0138): killed | thin01.py | REPRO | N |

### A4. RHYTHM T01-T20 (reg 24 Sep 12:58Z, [R] PREREG_RHYTHM_20; scripts blockA.py T01-T10, blockB.py T11-T20, rerun all verdicts match)

Rerun for the whole block: REPRO (blockA float tails only, 14 digits; blockB default DIFFERS only for T11/T20 = corrected loader, see T11; RHYTHM_AS_RUN=1 reproduces byte for byte).

| Name | Kill line | Outcome | 2nd/opp |
|---|---|---|---|
| T01 shell share Z 87-110 | "< 50%" | 0.846, passed | N |
| T02 one screening quantum | "max/min > 1.5" | 1.90, killed | N |
| T03 column law period 6 | "median error > 10%" | 7.5% (32 stages), passed | N |
| T04 Pt, Au, Hg | "ratio > 2" | 2.28, killed | N |
| T05 Fr and Ra | "a miss > 0.3 eV" | 0.553, 0.989 eV; gaps 1.554, 2.143 eV at 119, 120; killed | N |
| T06 Janet ridges | "Janet <= noble" | 0.004 vs 0.477, killed | N |
| T07 octave of eight | "< 50% for Z 21-86" | 0.00 (1.00 for Z 3-20), killed | N |
| T08 swing ratio | "ratio > 30% from mean" | 0.657-0.909, mean 0.813, passed | N |
| T09 twice Slater | "outside 0.70 +- 0.15" | 1.160, killed | N |
| T10 magic vs oscillator | "< 2x" | 0.198 vs -0.011, passed | N |
| T11 resistivity | "level <= shape" | corrected loader n=44: 0.709 vs 0.970 KILL; as run n=49: 3.068 vs 0.985 PASS | Y (same test, other handling): 5.03/0.985 and 1.109/1.052 pass (sensitivity.py) |
| T12 molar volume | "level <= shape" | 0.414 vs 0.231, passed | N |
| T13 hydrogen-like radius | "loses on either radius" | 0.164 vs 0.087; 0.220 vs 0.104, killed | N |
| T14 stiffness slope | "outside [1.2, 2.2]" | 1.31, passed | N |
| T15 surface G(550 nm) | "solid >= atom" | 0.0855 vs 0.0993, passed | N |
| T16 superheavy groups | "<= 4 of 7" | 4 of 7 (Mt, Ds missing counted as misses; registration silent), killed | N |
| T17 Madelung anomaly | "anomalous <= normal" | 0.854 vs 0.713, passed | N |
| T18 equal octaves | "both octave rhythms worse" | 0.125, 0.157 vs 0.052, killed | N |
| T19 half-filled dip | "<= 3 of 5" | 3 of 5, killed | N |
| T20 one key | "< 3 of 4" | 1 of 4, killed | N |

### A5. RUSSELL-WAVE (14:43Z), RUSSELL-WAVE-2 (14:50Z), R7 (16:13Z), 24 Sep ([R]; scripts wave.py, wave2.py, r7.py, posthoc_*.py; all REPRO)

Disclosures in the registration: the first 42% of The Universal One was read before registration; one data look at atomization enthalpies of 11 elements. S1-S3 come from a post-hoc candidate; the hydrogen check (352 vs 218 kJ/mol) is post-hoc.

| Name | Kill line | Outcome | 2nd/opp |
|---|---|---|---|
| T1 crest | "< 5 of 5" | 5 of 5, passed (partly seen) | N |
| T2 contraction to tone 4 | "<= 3 of 5" | 0 of 5, killed | N |
| T3 wave vs neighbours | "wave >= neighbours" | 61.4 vs 47.5 kJ/mol, killed | N |
| T4 one wave per row | "one wave worse" | 130.4 vs 58.9, killed | N |
| T5 two heights | "either trend fails" | 521 to 208; 505 to 865, passed (partly seen) | N |
| T6 group left out | "wave >= neighbours" | identical to T3 by construction | N |
| T7 melting | "wave >= neighbours" | 275.2 vs 193.7 K, killed | N |
| T8 two cuts | "< 80%" | 3 of 4 measured, killed; 18 of 24 all grades (post-hoc) | N |
| S1 melting scale | "CV > 0.10 or not best" | 0.163, killed | N |
| S2 stiffness scale | same | 0.475, killed | N |
| S3 one constant | "> 1.1x five heights" | 25.9 vs 27.5, passed (same data) | N |
| R7 row-7 forecast | "either outside, or either value missing (then: not testable)" | Fr not tabulated; Ra -26.9% vs tolerance 35.9%: NOT TESTABLE | N |
| Post-hoc: row swing, fourth tone, hydrogen | none | CV 0.031, 25.9 vs 43.8; leave-one-row-out max 6.5%; fourth tone smallest in 0 of 5 rows; ratio 1.62 | n/a |

### A6. G-02 and 6/8 Oct registrations

| Name | Reg / run | Tests | Kill line | Outcome | Script | Rerun | 2nd/opp |
|---|---|---|---|---|---|---|---|
| G-02 glueball | 25 Sep 03:24Z (file has no stamp) | length-set ratios vs lattice | [R] "median error > 5% for both length sets" | J++ 9.36%, 10.40%; 0++ tower 24.23%, 25.88%: killed every arm; 6 of 19 ratios in [1.2, 2.0], chance 0.125 | g02_run.py, g02_why.py | REPRO | N (one-parameter readings post-hoc: constant -37%, power +25%, per loop +8-9%) |
| WALL-RESIDUE-01 form 1 | 6 Oct | Spearman (z, group) | "any row with Spearman (z, group) > -0.8" | -1.000 rows 2-6, passed | wall_residue_01.py | REPRO | N |
| WALL-RESIDUE-01 form 2 | 6 Oct | CV of Delta Z_eff | "CV of Delta Z_eff > 10% in two or more rows" | 3.6, 10.4, 106.2, 73.9, 96.5%: killed | same | REPRO | N (two wall kinds found after; not re-registered) |
| F-WALL-01 | 6 Oct | 4f jump position | "4f jump outside the p-d interval in more than 2 of Tl-Rn set" | outside 6 of 6; all 12 row-6 negative | f_wall_01.py | REPRO | Y: three removal orders (JJ-02F) |
| FIVE-EIGHTHS-01 | 6 Oct | residual exponent | "residual exponent outside 3.5-4.5 over Z = 10-40" | 4.302 (4.328 over 40-86), passed | five_eighths_01.py | REPRO | N |
| PEEL-STAGGER-JJ-02 | 12 Oct | stagger p, d, f | kill lines in script header | p 264/316, d 110/158, f 0/36 killed, maxima 1,827/2,036 vs null 1,145 | stagger_jj_02.py | REPRO; independent code 260/316, 110/154, f 0/36, 1,791/1,960 vs 1,274 | Y: f under two alternative orders (0 and 1 of 36) |
| TF-RESID-01 s1 | 8 Oct 16:36:14Z | residual vs raw at K=10 | [R] "scores at least the raw ... Killed if residual accuracy < raw accuracy" (Appendix D truncates; script prints ">= raw") | 0.951 vs 0.951: passes as registered | tf_resid_01.py | REPRO | N (pchip variant identical) |
| TF-RESID-01 s2 | 16:36Z | envelope alone | "envelope > 0.20 at K=10" | 0.000, passed | same | REPRO | N |
| STEP-23-01 | 8 Oct 16:41:07Z (after post-hoc TF_INSHELL_01) | median step | "median outside [0.85, 1.20]" | 1.051, 1,225 steps, passed | step_23_01.py | REPRO | N |

### A7. Remaining Appendix D rows (v2.x)

| Name | Kill / grade | Outcome | Script | Rerun |
|---|---|---|---|---|
| Thm 8.2 split | identity [D] | 5,714 steps to 4.1e-16; walls 3/5 ... 13/85 | split_theorem_check.py | REPRO |
| Colour-3 certificate | [D] "a coefficient differs" | 21/21 equal; J4 differs 21/21 | certify_ladder.py | NOT RERUN (snappy) |
| Thm 3.1(4), four-reading certificate | proof | 200/200; 2000/2000; 0/2000 with three poles between probes | proof_checks_3_1_and_5_6.py | REPRO |
| Mass gaps | | abs(G) 1.074, 1.220, 1.025 | mass_gaps_smith.py | REPRO |
| Gold metamer / singular-vector pair | model target | dE 8.60, dE00 8.27; sigma_max 5.38e-3; 18.4 vs 5.3 | metamer_check.py | REPRO |
| Gold labels all datasets (post-hoc) | | rise at 450 nm 15/15; 550 rises 1.8e-4 and 1.65e-5 | thin01_complete.py | REPRO |
| Column misses (post-hoc) | | sign 20/22; corr 0.03 pooled, 0.58 within groups | insertion_rule.py, column_residual_vs_Z2.py | REPRO |
| reverse_peel_results.json | | 5,725 assertions | check_reverse_peel.py | REPRO (max_metric_error 1.29e-10 vs 1.09e-10 stored; README records it) |
| TF constants, in-shell steps, bare law | computed | q 5.2211, a_TF 1.2875; 1.039/1.088; bare 2.74-2.94 | tf_constant.py, tf_inshell.py, tf_ladder.py | REPRO |
| Negative controls (sec 18) | 46 listed | | | NOT CHECKED |
| Lean (140 theorems) | | | | NOT BUILT (no toolchain) |

### A8. 7 Nov exploratory runs (PATH_NOTES, origin/main research/2026-11-07; PN states "nothing graded yet"; kill lines were NOT written before these runs, except where stated; scripts in research/2026-11-07/scripts/; all OUT OF SCOPE for rerun)

| Name | Tests | Kill line | Outcome | Script | 2nd/opp |
|---|---|---|---|---|---|
| BRANCH-CUT-01 | K#K vs K#mirror(K) Levine-Tristram | none | parallel signature 2x K at 400/400 phases; opposed 0 at every phase; spectrum paired to 4e-15 | branch_cut_01*.py | control 4_1 |
| FLIP-KEY-01/02 | rigid-body climb | none | 0.577350 = sqrt((I3-I2)(I2-I1)/(I1 I3)) Omega; Montgomery -0.562448297 vs -0.562448306 | flip_key | N |
| SILENT-WALLS-01 | Table 6 double walls | none | 575 double roots, 494 silent, 81 jump +-4 | | N |
| TILT-01 | projector tilt | none | mirrors locked at 45 deg; eps 0.03 median 0.57 deg | | N |
| OPTICS-01 | P3 line abs(G)^2 = 1/2; X02 | none | metals 35/35 above, non-metals 0/6 above; closest Nb 0.506, Te 0.486 | optics_01 | N |
| FILM-PHASE-01 | Smith phase gap vs film colour gap | none | 39 pairs, Spearman 0.64 | film_phase_01.py | N |
| PRESSURE-LINE-01 | 2/3 line under squeeze | none | molecular solids 0.89 (n=6, p 0.02); gases pending | pressure_line_01.py | N |
| GEO-PHASE-01 | turn = signed area on Smith disk | none | area negative 38/41; rho -0.99 | geo_phase_01.py | N |
| FILM-GEO-LINK-01 | colour gap vs phase gap | none | gap ~ (phase gap)^0.34; residual rho -0.52 | film_geo_link_01.py | N |
| KNOT-VOLUME-01/02/03 | Jones string as light, 2,970 knots | none | climb rho 0.854; R^2 0.708 / 0.734 / 0.810 / 0.826; turn -0.02; abs(signature) 0.83 | knot_volume_01..03.py | Y: opposite count -0.07 |
| HANDEDNESS-01 | winding sense | none | Drude 9 cases, Lorentz 6 cases, same sense | handedness_01.py | N |
| KNOT-CS-01/02 | does the turn carry Chern-Simons | none | whole-string turn vs CS r 0.04 / 0.01 (null 0.02); zero angles 0.07, 0.08 | knot_cs_01/02.py | Y: single points N=3..10: r 0.16 at N=3, ~0.03 else |
| CIRCUIT-POLY-01/02 | spanning-tree polynomial | Kirchhoff check Q(1) = det | 1846/1846; redrawn 3/50 unchanged; reduced alternating 180/180; climb vs volume 0.34 | circuit_poly_01/02.py | Y: reduced-alternating repair |
| SURFACEOLOGY-01 | reproduction of hidden zero, u-equations | none | 14 terms sum to 0; u-equations 4e-16 | surfaceology_01.py | n/a |
| SHAPE-DISK-01/02 | volume as distance from vacuum | none | rho -0.998 on 2777 tetrahedra; well constant 1.2990 vs 3 sqrt3/4 = 1.29904; knot-level median 0.27% | shape_disk_01/02.py | N |
| WINDING-CS-01 | CS from winding integers (reproduction of Neumann 2004) | none | CS 2.4e-14 on 79/79; continuous part only: matched 1 of 79 | winding_cs_01.py | Y: windings dropped |
| ROOTS-DISK-01/02 | geometric solution nearest vacuum | none | 11/11 (31/31 weaker pass) | roots_disk_01/02.py | N |
| DRAWING-POLY-01..05, DRAWING-ROBUST-01..04 | potential read off the drawing | none (check on 4_1 volume) | top value = SnapPy on 79/79; 13/13 diagram independent | drawing_poly_01..05, drawing_robust_01..04 | Y: 3 drawings |
| COLOUR BRIDGE | knots and metals in one frame | none | metals 96% beyond the line (median 2.79); knots median 0.50; winding = thickness/247 nm, 0 mismatches on 3660 grid | colknot_*.py | N |
| TORUS-CHECK-02 | prediction written before the lookup: Micheletti's new knots are torus knots | prediction | 10_124, 15n_41185 both volume 0 | torus_check_02.py | N |
| WINDINGS/BOWL/LADDER series | CS exact; bowl series; ladder | none | CS 454/454 to 2.7e-14; bowl+cubic+quartic median 0.076%; ladder nearest vacuum 31/31 | FLAT-*, BOWL-*, ROOTS-LADDER-* | Y: hyperbolic-distance opposite far worse |
| HOMFLY-BOOKS-01/02 | HOMFLY with light | none | plain torus climb 0.036; opposite sl(N) lines: R^2 0.795 to 0.830 to 0.838 | homfly_books_01/02.py | Y: the sl(N) opposite |

### A9. 10 Nov: round 4 "four holes" (NOTES_06) and open-question tests (NOTES_07). All OUT OF SCOPE for rerun. Kill lines are script headers [S] unless marked.

| Name | Tests | Kill line | Outcome | Script | 2nd/opp |
|---|---|---|---|---|---|
| HALF-LINE / LADDER-WALL-01 | beyond-line steps sit at closed cores | "more than 10% of beyond-line steps at non-closed N, or fewer than half of closed-core openings beyond the line" | 109 elements, 5,737 steps, 8 beyond, 8 of 8 at a closed core, 8 of 694 closed-core openings; clause 2 fires | ladder_wall_01.py | Y: per-core table of openings that stay inside |
| PLASMA-WALL-01 | E_wall vs ladder readings | "abs(Spearman) < 0.5 for every ladder reading" | +0.057, -0.279, +0.261 (n=30): fired | plasma_wall_01.py | Y: phase at 2 eV +0.545/-0.436/-0.584; 1/E_wall is rank-flip only (not scored separately) |
| PHASE-LADDER-02 | phase at three energies separates alkalis | "one-sided Mann-Whitney p > 0.01, or any two energies (1.5, 2.0, 2.5 eV) disagreeing in direction" | p = 2.7e-06 at each; Cs>Rb>K>Na>Li | phase_ladder_02.py | Y: even abs(G)^2 reading p 0.091/0.099/0.099 |
| TIME-WALL-01 | fade formula | "formula off by more than 1e-20 relative on random two-part fades, or half-bend ratio differing from 3+2 sqrt2" | worst 1.41e-48 (50 digits); headline text says "20 digits" | time_wall_01.py | Y: three parts, no single ratio |
| DEFECT-WALL-01 | identities | "any remainder nonzero, or a random real (s,v) gives k > dM^2/4, or a positive matrix has discriminant <= 0" | passed; 0 of 200,000 | defect_wall_01.py | N |
| COLOUR-PEEL-01 | two-channel stretch | "identities > 1e-9, or any two-channel stretch with abs(tau') >= abs(tau), or a misclassification" | 22 toward white, 0 away | colour_peel_01.py | Y: 02, 03 |
| COLOUR-PEEL-02 | three channels | "stretch rate toward not above away" | 0 of 20,000 (unit weights) | colour_peel_02.py | Y |
| COLOUR-PEEL-03 | Exner weights | strict "stretch only toward white" | 861/882/933 stretches; toward 4.97-5.59%, away 3.25-3.36%: fails in strict form | colour_peel_03.py | Y |
| HIDDEN-G-01 | sign of g | "g counts only if held-out RMS(H) <= 0.5 RMS(L) and the pole lies outside the range; killed by one counted g > 0 family" | g < 0 in 62/62 and 84/84 | signs/hidden_g_01.py | Y: 1/z gives g > 0 61/61 |
| HIDDEN-G-02 (knots) | g negative real; pole at -1/tau | real: 4 of 45 hold, killed; pole: 1 of 45, killed | | signs/hidden_g_02.py, hidden_g_03.py | Y: HIDDEN-G-03, stable fits 15 of 16 |
| limit_m2 (two-term rule) | limit set | one presentation whose limit set differs | 417 of 417; "d = 2q" fails 134 of 1,696 | signs/limit_m2_01..04.py | Y |
| limit_real | simple roots reached | | 134 of 134 | signs/limit_real_03..06.py | N |
| never_rule_03/04/05 | R3/R4 predictions | R3 predicts NEVER for 25; sign change in 0 of 25 | T1 141/141; T2 195/195; R3 predicts 32, all 32 never; 0 of 25; R4 fitted on 55/21, 71/21, 75/29 | signs/never_rule_03..05.py | Y: R3 opposite (a<c) killed, 7 right 9 wrong |
| never_golden_03, verify_signs_01..05, never_border_06 | golden 89/34 | | 89/34 TURNS; earlier "never" came from coefficient trimming; 233/89 band points withdrawn; NEVER stands at border | | Y |
| split_signs | theta-chirality A-C | A any disagreement; C "arithmetic prediction killed by one knot" | A 199/199; first C form killed 127 of 137; F4-corank repair 137/137 (fitted on 22, tested on 115) | signs/split_signs_01/02.py | Y: second setup 31 of 54 fails |
| TORUS-STAIR-01 | roots on the staircase | "a root with abs(2pq alpha - round) > 1e-9, or a wrong count" | seven torus knots pass | torus_stair_01.py | N |
| TORUS-LABEL-02 | label count | "distinct-value count != (p-1)(q-1)/2 or a value not hit exactly twice" | k^2 mod pq fails 47 of 53; mod 4pq collapses 27 of 53 | torus_label_02.py | N |
| TORUS-DIRS-03 | arc ends | "any arc whose two ends differ" | 0 disagreements, p<13, q<20 | torus_dirs_03.py | N |
| JOIN-K-01 | join values | "any printed root or direction not hit" | all match (q=3,5,7) | join_k_01.py | N |
| TORUS-ROOTS-01 | rational roots of 8_19, 10_124 | "a non-degenerate rational root outside the predicted set" | passed; 8_19 {11/12, 2/3}, 10_124 {14/15, 11/15}; 22,000 starts (sum of four runs) | torus_roots_01.py | Y: TORUS-ROOTS-02 diagnostic (no kill) |
| SILENT-WALLS-02 | silent walls have nullity 1 | "a silent double wall with nullity 1" | 376 of 494: killed as stated; repaired TOUCH 376 / OPPOSED CROSSING 118 | silent_walls_02.py | Y: the repaired split |
| SILENT-WALLS-03 | second Alexander polynomial | "any double root where root of the second Alexander polynomial disagrees with nullity 2" | 575/575 | silent_walls_03.py | N |
| WALL-NILPOTENT-04 | kernel dimension | "a kernel dimension differing from the listed nullity" | 198/198 | wall_nilpotent_04.py | N |
| NEVER-TURN-01 | never-turners inside the spread | "never-turners sit inside the spread" | 0, 0.121, 0.132, 0.117 vs 0 to 0.222: fired | never_turn_01.py | N (opposite "turners share something" not run) |
| NEVER-TURN-02 | control | | 7 never / 19 turn | never_turn_02.py | N |
| NEVER-TURN-03 | families | "one member on the wrong side" | A, B, C held; D golden failed (89/34) | never_turn_03.py | Y |
| BOWL-HALF-01 | half line in the bowl | "neither the circle average nor the error shows anything at 1/2" | fired for the bowl; 99.7% of 2,777 tetrahedra inside | bowl_half_01.py | N |
| DIELECTRICS-01 | dielectrics near real axis | ">90% within 10 degrees of the real axis" | 80%; not fired ("PARTLY") | dielectrics_01.py | N |
| CHAIN-TURN-01 | real turn in 95% band | "real inside the central 95% band at ratio 5 and 7" | all four inside: fired | chain_turn_01.py | Y: CHAIN-TURN-02 |
| CHAIN-TURN-02 | signed turn vs band | outside the band | -0.1829/+0.2045 (5), -0.2168/+0.2426 (7) | chain_turn_02.py | the opposite |
| CHAIN-WHOLE-03 | longer range | "the angle or the axis keeps drifting between 10^5 and 10^7" | 9.87, 11.62, 12.07, 12.08 deg at 10^5, 10^6, 10^7, 2x10^7; axis creeping; write-up says "settles" | chain_whole_03.py | N |
| DEFECT-JOIN-01 | limits vs 4 sin^2(pi j/d) | "an m=1 limit with no match" | eight m=1 values match; open m>1 | defect_join_01.py | N |

### A10. 11-12 Nov element tests (Appendix D v3.0 Sections 22-24; scripts on branch origin/claude/sm-ball-20261111, elements/; build copies of shell_screen_04 and esr_check_01 identical). OUT OF SCOPE for rerun; stored .out read.

| Name | Reg / run | Tests | Kill line [S] | Outcome | 2nd/opp |
|---|---|---|---|---|---|
| ELEMENT-BALL-01 K1 | 11 Nov | largest step at a noble-core boundary | "in >= 90% of elements"; NOBLE = {0,2,10,18,36,54,86,118} | 101/101, passes | N |
| ELEMENT-BALL-01 K2 | 11 Nov | whole-shell blocks near the wall | "median abs(G^2 - 1/2) at most half that of random blocks, p < 0.01 (5000 shuffles)" | median 0.4040 vs random 0.2965, ratio 1.362, p = 1.0000: fails | Y, run but with no kill line written: shell blocks past the wall 0.296 vs random 0.338 (p 0.9804). Appendix D prints "killed in the opposite direction" |
| ELEMENT-BALL-01 K3 | 11 Nov | steps on the wall to 2% | count only | 1: Cs (G2 0.5071) | N |
| CORE-OPEN-02 | 11 Nov | crossing valence order | "no order across periods (non-monotone)" | period 2 valence 1-4; periods 3-6 valence 1; period 7 none (Fr 5.50 inside) | N |
| ISO-CROSS-03 | 11 Nov | one crossing per line | "any line crosses the wall more than once" | cores 2, 10, 18, 36, 54: 1 each; core 86: 0 | N |
| SHELL-SCREEN-04 A, B | 11 Nov | identity / arithmetic | script says first kill cannot fire | identity | n/a |
| SHELL-SCREEN-04 C | 11 Nov | He-core series crossing | "the crossing falls anywhere but between Z=6 and Z=7, or any measured z for Z=5..10 is missed by over 2%" | crossing 6.538, misses 0 (B +0.55%, C +0.26%; Be +1.55% at Z=4, outside range) | Y: 5/8 removed gives 9.470 |
| SHELL-SCREEN-04 D | 11 Nov | Zc/Zv alkalis | "Zc/Zv spread over 2% for Na, K, Rb, Cs" | 1.11% (2.0222 to 2.0448); not fired. Second-order numbers (0.157666, 0.250500) are "recalled literature values, not looked up"; Fr needs IE2 > 23.738 eV, archived 22.4 +- 1.9 [S] | N |
| ESR-CHECK-01 | 12 Nov | recount of ESR counts | none stated beyond identity of counts | 5,847, 7,021, 5,714, 5,584, 311/919/4,617, 5,691, 156/60, 103/7/8 OK; 675 adjacent steps (8 cross) OK; "closed-core openings (adjacent, true index)" 433 vs printed 675: DIFFERS; compressed 682 vs printed 694 | N |

### A11. Rounds 5-6 (Yang-Mills read; NOTES_08; folders under in2 and research/). OUT OF SCOPE for rerun. Not in the paper's Appendix D (build_v30 text has no window wall / pendulum / yang).

| Name | Tests | Kill line [S] | Outcome | Script | 2nd/opp |
|---|---|---|---|---|---|
| WINDOW_WALL_01 | C<=8 certificate window bound | "(a) any of the 58 stored accepted targets has d - r > W(s) ... (b) W'(0) <= 0 on a graph and coupling where a stored target exists" | 0 in excluded cells; smallest slack 0.000276 | window_wall_01.py | Y: certified_02 |
| WINDOW_WALL_CERTIFIED_02 | exact-interval version | any stored accepted target in an excluded cell | 0 | window_wall_certified_02.py | the second setup |
| tail_check_01 | complete-tail eigenvalues | "any K_m eigenvalue above the Schur one, claimed z above the true E1, or a wrong count" | not hit | tail_check_01.py | N |
| three_axis_01 | three-axis floor | "ratio below the floor, or the smallest eigenvalue differing by more than 1e-10" | not hit | three_axis_01.py | Y: one axis with a zero direction |
| B128-FLOOR-CHECK-01 | 3 - Re chi on w != 0 | "any grid point with w != 0 and 3 - Re chi < 4 - 1e-12; delta = (2/3)(3 - Re chi) mismatch > 1e-12" | min 4.000000000000 at w = +-1; delta error 1.776e-15 | b128_floor_check_01.py | N |
| QUANTUM-PENDULUM-GAP-02 | gap vs sqrt(2 kappa lam) | "gap/w does not tend to 1 as lam grows" | 0.9328, 0.9677, 0.9841, 0.9921 at lam 8..512; gap - (w - k/2) = +0.231..+0.248 (data follow w - kappa/4, header says w - kappa/2) | quantum_pendulum_gap_02.py | N |
| open_tests_05 T1 (B75) | concavity | "E0 not concave in kappa, or E0+E1 not concave" | holds; E1 alone not concave (min d2 -34.5) | open_tests_05.py | N |
| open_tests_05 T2 (Ky Fan chord) | gap bound | "bound > true gap anywhere" | 0 violations; chord loses 12.3% (kappa 1.75) to 33.0% (kappa 1.00) (arith_checks.out); ledger says "15 to 33%" in both v1 and v2 | | N |
| open_tests_05 T3 (B160) | ratio (E2-E0)/(E1-E0) | "r not settling as lam grows" | 1.61183 to 1.50425 at lam 2 to 512 | | N |
| open_tests_05 T4 (B189) | gap - 2 sqrt(kappa lam) linear in kappa | "not ~ linear in kappa at small kappa" | c = 0.629 .. 0.664 | | Y: b189_constant_06 |
| B189-CONSTANT-06 | is c constant | "small-kappa limits of c differ by more than 0.02 between kappa*lam = 16, 64, 256" | c depends on kappa/sqrt(kappa lam); Richardson limit 0.6250 = 5/8 (arith_checks.out); ledger v1 "c ~ 0.63", v2 "5/8" | b189_constant_06.py | N |
| open_tests_05 T5 | E = n^T B B^T n with lam sum | "ratio not -> 1" | per block | | N |
| ONE-PLAQUETTE-PHASE-01 | gap/(2 sqrt lam) | "gap/(2 sqrt lam) not tending to 1"; "E0, E1 move by > 1e-8 between N and N+10" | 0.845 (lam 0.5) .. 0.980 (lam 256) | one_plaquette_phase_01.py | N |
| LARGE-FIELD-FLOOR-02 | floor m(delta) | "any large-field grid point with 3 - Re chi < m(delta) - 1e-9" | violation <= 8.9e-16 over delta/pi 0.05..1.00; m(1) = 4 | large_field_floor_02.py | N |
| SMALL-FIELD-GAP-03 | small-field gap | normalisation check: one plaquette mu = 4 | strips mu_min 4 to 2.008; tori 4 sin^2(pi/L) | small_field_gap_03.py | N |
| SNELL-SMITH-TREES-04 | strong-coupling (4/3) girth; strip band [2,6]; Smith coordinate | no kill line in header (three exact checks) | double cube 5.3333; evanescent exactly for mu < 2 or mu > 6; z = 3.732 at mu = 0 | snell_smith_trees_04.py | N |

---------------------------------------------------------------------
## B. SHA-256 OF THE REGISTRATION FILES

Script `verify_prereg_sha.py`, output `verify_prereg_sha.out`. Full 64-hex values are in the .out.

| File | First 16 (computed) | Appendix D first-16 | SHA256SUMS_PREREG.txt |
|---|---|---|---|
| PREREGISTRATION_RUN03 | 5ba89445522479ac | same | same |
| PREREGISTRATION_SNELL_PEEL_01 | 0bcc63fba69a1215 | same | same |
| PREREGISTRATION_ONION_ATLAS_01 | 978b6afd6fc0a49d | same | same |
| PREREG_CLOSE_01 | e48838ba3258acd7 | same | same |
| PREREG_WIDE_01 | 7ce4e8e66d372788 | printed c185f407aec8c11e: MISMATCH | line matches the package copy; original c185f407aec8c11e... noted in a comment |
| PREREG_NUC_01 | f27cb2cf39c2dfaa | same | same |
| PREREG_PART_01 | 97e333b609edcc8d | same | same |
| PREREG_ROUND_02 | 70b264a9aa049b70 | same | same |
| PREREG_ADM_01 | 473cd0d4cf76ec64 | same | same |
| PREREG_TIME_01 | 2308df74354f085c | same | same |
| PREREG_DATA_01 | 09413606c99ccb98 | same | same |
| PREREG_THIN_01 | 099d083bd259d52e | same | same |
| PREREG_RHYTHM_20 | 702f49c35c4c92d0 | same | same |
| PREREG_RUSSELL_WAVE | 6c734cf2bbc6d487 | same | same |
| PREREG_RUSSELL_WAVE_2 | 65226d523634acd3 | same | same |
| PREREG_R7 | f3c1093c7cb7ab07 | same | same |
| PREREG_G02 (v10) | 3ce6f9540261e3a5 | same | same |
| PREREG_TF_RESID_01 | 8177b47eef8bb7cb | same | same |
| PREREG_STEP_23_01 | a902cdb04c1d893e | same | same |

18 of 19 match all three. The one exception is WIDE: the shipped file is a relabelled copy (two headings changed), so the printed 16 hex belong to a file the package does not contain; the original cannot be verified from the package. The mismatch is disclosed in the SHA256SUMS comment.

Not in Appendix D and not in SHA256SUMS_PREREG.txt: `PREREGISTRATION_ONION_ATLAS_02.md` (b5dd4ead5a0b43eb..., stamped 12:27:12Z, registers Run 02 K1-K3); `work/v11/checks/PREREG_G02.md` (a duplicate of the v10 file, same hash 3ce6f954...); `TEST_LOG.md` (1c0e37716ce08b3d...). The v21 `.sha256` files carry the stamps 2026-10-08T16:36:14Z (TF_RESID) and 16:41:07Z (STEP_23). The paper lists the v21 files under v21/scripts, but they sit in work/v21/ (CHECK_REPORT sec 7).

---------------------------------------------------------------------
## C. THREE LISTS

### C1. Tests stated differently in two places (both wordings, both numbers)

Resolved from the dossier (no longer open): SIG-01 label is 13a_3542 in Appendix D, PREREG_TIME_01 and CHECK_REPORT (the dossier's 3545 was an image misread). TF-RESID-01 statement 1 is registered as "at least the raw", so equal values pass as registered; the "unsatisfiable kill" objection came from Appendix D's truncated wording. 5,737 vs 5,714 reconciles: 5,737 - 5,714 = 23 nonadjacent pairs.

1. Run 01 baseline: 0.49 (v0.1 abstract) vs 0.51 (v2.9, scaling per fold); rerun 0.508 in-fold, 0.500 in run03.py (0.952 vs 0.500).
2. Smith threshold: 0.93 (v0.2 sec 6.4) vs 0.92 (v2.9); frozen registered value 0.856 with 87% (rerun 0.871); best 0.994 at 0.9175; held-out 0.977/0.959; v1.2 abstract "96-98%".
3. T-M: R^2 0.91 (v0.2 abstract) vs 0.906 (body, TEST_LOG) vs 0.9055 (rerun).
4. T-J blind pairs: TEST_LOG "24 of 26 pairs" vs "48 of 52 rows"; v0.2 "285 pairs through twelve"; v0.5 "354"; Appendix D "233 of 253"; v0.1 "five pairs".
5. Colour ladder: TEST_RECORD "colour 4 separates the two colour-3-blind pairs"; v0.2 "21 pairs separated by J4 (2 at 11, 19 at 12)"; Appendix D "0 of 21" J4-blind.
6. Colour-3 certificate: Appendix D "14 direct, 7 mirrored" vs IC10 M1 "wrong direct/mirror split".
7. T-F kill: TEST_LOG "non-integer coefficients" vs TEST_RECORD "coefficients further than 0.01 from integers, or residual > 1e-4".
8. T-Q kill: TEST_LOG "< 6 of 12" vs TEST_RECORD "claim needs >= 1, generic needs >= 6"; no Appendix D row.
9. CLOSE C1 kill: registered "a miss outside that set, OR the contained-set rule explains fewer than 80% of misses pooled over K" vs Appendix D first clause only.
10. CLOSE C2: registered two halves (height within 20% AND Spearman >= 0.8) vs Appendix D "height error > 20%" only.
11. Snell K1: registered null "outer electrons > 6" vs Appendix D "window rule".
12. NUC-01 Part 1 kill: registered "... in both models (point estimate), or its advantage interval includes zero against both in both models" vs Appendix D short form.
13. DATA-01: registration Arms M and P (descriptive) vs Appendix D "E-only arm" row, no Arm P row.
14. TF-RESID-01 s1: registered "at least the raw" / kill "residual accuracy < raw accuracy" vs Appendix D "scores 0.951 vs 0.951, as printed" with a "<" kill text vs script print ">= raw".
15. THIN-01: v0.7.1 abstract flipped, v0.8 flipped back; IC07 2e "six" vs seven gold datasets; IC07 3f "rises at all measured sets, none at 550" vs 3 local sets rising at 550 (3.1e-5, 2.1e-6, 1.8e-4; the rerun prints 1.8e-4 and 1.65e-5); 3i "three groups" vs Ciesielski 35 nm films omitted by the registration.
16. NUM-01 "level is the denominator" rewritten v0.7.1, reverted v0.8.
17. RHYTHM T11: 0.709 vs 0.970 KILL (corrected loader, n=44) vs 3.068 vs 0.985 PASS (as run, n=49; five lower bounds read as values); other handlings 5.03/0.985 and 1.109/1.052 pass.
18. RHYTHM T16: Mt, Ds counted as misses (4 of 7) vs registration "did not say how missing data count".
19. P-01: 3.1 sigma (3.14 corrected) and 2.4 (2.37 uncorrected) vs v1.2 "2.8 sigma combined", still called failed against the registered 3-sigma line.
20. TIME-01b: 0.99895 (miss 1.05e-3, registered) vs 1.00014-1.00016 midpoint (post-hoc).
21. TIME-01c/d: stored counts vs rerun counts outside the window (13a_3542 at alpha 0.18: 29 vs 30) and above the wall (N = 4 vs N = 3).
22. CHAIN-WHOLE-03: kill "keeps drifting" and numbers 9.87 to 12.08 deg (axis "still creeping") vs write-up "settles".
23. Time-wall grade: headline "CHECKED to 20 digits" vs section 3b "CHECKED at 50 digits"; printed worst error 1.41e-48.
24. Closed-core denominator: 8 of 694 (FOUR_HOLES, ladder_wall_01) vs 8 of 675 (Appendix D, ESR; "true charge indices") vs 682 compressed (ESR-CHECK) vs 433 "closed-core openings (adjacent, true index)" (ESR-CHECK DIFFERS). 675 + 23 = 698, not 694.
25. "Closed core" set is three different sets: ELEMENT-BALL-01 NOBLE {0,2,10,18,36,54,86,118}; LADDER-WALL-01 and ESR-CHECK {2,10,18,28,36,46,54,60,68,78,86}.
26. ELEMENT-BALL-01 K2: output "median 0.4040 vs random 0.2965" (ratio 1.362) and "shell blocks past the wall 0.296 vs random 0.338" are two different quantities with near-equal numbers; Appendix D prints both ("0.404 against 0.297", "0.296 against 0.338") and says "killed in the opposite direction", while the script header has no kill line for the opposite.
27. "K1/K2" names: Run 02 ONION-ATLAS-02 K1/K2/K3 vs ELEMENT-BALL-01 K1/K2/K3, different tests with the same labels. Run 02's file is missing from the Appendix D hash table.
28. TEST_LOG header "kill lines for T-A..T-J fixed in paper v0.1 section 15 at ~13:46Z" vs T-E and T-F own declarations at 14:06:52Z and 14:07:39Z.
29. Ky Fan loss: "15 to 33%" (ledger v1 and v2) vs printed numbers 12.3% (kappa 1.75) to 33.0% (kappa 1.00); v2 says "wording fixed" but keeps 15.
30. B189 constant: ledger v1 "c ~ 0.63" vs v2 "c_inf = 5/8" (Richardson 0.6250 in arith_checks.out; the c values depend on kappa/sqrt(kappa lam)).
31. Pendulum gap: brief "sqrt(2 kappa lam) - kappa/4" vs script header "w - kappa/2"; data (+0.231..+0.248) follow kappa/4.
32. Window wall: ATLAS_READ_BRIEF "in Lean" vs WINDOW_WALL.md "Not a Lean theorem".
33. Negative pivot: package METHOD "exactly one negative pivot at z = 57.9" vs recorded_results 2 for N = 14 and 15, 1 only at N = 16 with 2-3 refinements.
34. TORUS-ROOTS-01 "22,000 starts" (sum of four runs) vs far fewer converged.
35. Fr: archived 22.4 +- 1.9 [S] vs ratio reading 22.67-23.18 eV vs wall need 23.738 eV vs RHYTHM T05 miss 0.553 eV vs R7 "not tabulated".
36. PREREG v21 files: the paper lists them under v21/scripts; in the package they sit under work/v21/. The README says the same.

### C2. Kills never retried in another setup or direction, with the single most natural opposite as a one-line kill-line proposal

Each proposal is written as a kill line before any run. "Not retried" = no second setup or opposite found in any source read.

A. Elemental and early
1. Run 02 polarizability 0/9: opposite = level-only feature. Kill: level-only (ln IE1) does not beat the peel shape in at least 7 of 9 settings.
2. NUM-01 0.392 vs 0.267: second numerator definition. Kill: ratio-to-neighbour numerator fails to beat the denominator at K=10.
3. NUC-01 shape 0.65 vs 0.83 and level-to-radius 1 of 2: other dataset. Kill: shape does not beat NPNN on the AME2020 holdout it was not fitted on.
4. H-01 echo weight 0.743: opposite weight. Kill: abs(G) alone does not beat abs(1 - G^2) on the same held-out metals (0.977 vs 0.743 already points this way, so this is a confirmation).
5. f-block cross-series 2-3/14: other row pairing. Kill: pairing 4f with 5f by Z offset gives 3 or fewer of 14 both ways.
6. Snell rules: third filling rule. Kill: a rule from the registered 8-electron contained set fails to beat the window rule on the 6 known turns.
7. CAT-01 233 of 253: other categorified invariant. Kill: Khovanov rank at the J4-blind pairs separates fewer than half of the 21.
8. THIN-01 P1 and P2: apply the frozen rule to the omitted Ciesielski 35 nm and 10-20 nm films in a new registration. Kill: same side of bulk in fewer than 13 of 15 films.
9. RHYTHM T02, T04, T05, T06, T07, T09, T13, T16, T18, T19, T20: first retry for those that fire; for each, the opposite is "the level reading wins". Kill (generic): the level reading does not beat the peel shape on the same data in at least 2 of 3 handlings.
10. RUSSELL T2, T3, T4, T7, T8, S1, S2: opposite = no-wave baseline. Kill: wave does not beat a plain row-mean baseline by 20% on T3 and T7 data.
11. G-02 glueball killed every arm: opposite = ratio test not length test. Kill: ratio of first to second J++ state from the loop lengths differs from lattice by more than 5%.
12. P-01: other fit family. Kill: abs(R_knot - R_lat) > 3 sigma with the combined error (2.8 sigma already below the line), registered before running.
13. WALL-RESIDUE-01 form 2: re-register "two wall kinds". Kill: CV of Delta Z_eff above 10% inside either kind in two or more rows.
14. TIME-01b real time 0.99895: midpoint rule registered first. Kill: midpoint charge off 1 by more than 1e-3.
15. Depth law "outer > K": other shell rule. Kill: a contained-set rule with K+1 explains fewer than 80% of misses at K=11-12.
16. Run 03 radius, hardness: other model class. Kill: random forest static beats peel in fewer than the same 9 of 9 and 8 of 9.
17. T-O at K=6 tie: new split. Kill: T1 does not exceed S2 on 5 random seeds of the K=6 split.
18. DATA-01 E-only arm: run when data exist. Kill: median below 16/18 on the extrapolated elements.
19. T-C and T-G never run: they need the NIST fetch; no opposite exists until then.

B. 10-12 Nov
20. LADDER-WALL-01 (clause 2 fired): opposite listing. Kill: the beyond-line count at closed-core openings exceeds the count of openings that stay inside, by Z, in fewer than half of the cores (the per-core table exists but no kill was written for it).
21. PLASMA-WALL-01: 1/E_wall alone. Kill: abs(Spearman) of 1/E_wall against each of the three ladder readings below 0.5 (this is a rank flip, so expect sign only; register the three numbers).
22. NEVER-TURN-01: turners share something. Kill: no KnotInfo field separates the 19 turners from the 4 never-turners with at most one error.
23. Golden family [2,1^n,2] through the clock: Kill: the clock reading of 89/34 differs from the turn reading at 120 digits.
24. 233/89: degree-116 root finder not run. Kill: any root of the degree-116 polynomial lies on the unit circle at 1e-30.
25. ELEMENT-BALL-01 K2: split blocks into shell and screening parts (Thm 8.2). Kill: shell part median abs(G^2 - 1/2) not at most half that of random blocks, p < 0.01.
26. COLOUR-PEEL-03 strict form: other weights. Kill: stretch rate toward white not above away at the registered tolerance with CIE weights.
27. HIDDEN-G knots, other family class. Kill: g negative real in fewer than 40 of 45 on a non-Whitehead family.
28. CHAIN-WHOLE-03: 10^8 and 10^9. Kill: angle moves more than 0.1 degree between 10^7 and 10^9.
29. BOWL-HALF-01: bowl feature at 1/2 FAILED-DIVERTED; opposite = outer region. Kill: neither the circle average nor the error shows anything at 1/2 in the 8 outside tetrahedra's region.
30. DIELECTRICS-01 (80% vs 90%, not fired): more dielectrics. Kill: below 90% within 10 degrees on a new set of 40 dielectrics.
31. SILENT-WALLS lopsidedness 233/143: Kill: the lopsidedness is not predicted by the Smith-point position of the wall, on a fresh 200 walls.
32. TORUS-ROOTS-01 (passed): 8_19 and 10_124 miss 2 and 3 roots in the drawing search; Kill: a homotopy search finds fewer than 3 and 4 directions.
33. ONE-PLAQUETTE gap, SHELL-SCREEN-04 D: Fr row untested; Kill: IE2 of Fr 23.738 eV or lower by the registered measurement.

### C3. Results that passed a registered test (with margin where it is thin)

Kills that did not fire, with the registered line:
- Run 01 0.951 vs 0.508 at K=10; 35/36 variants; DATA-01 median 17/18 (kill < 16/18) and 0.918 (kill < 0.90): margin one count and 0.018.
- TF-RESID-01 s1 0.951 vs 0.951 ("at least"): passes with zero margin; s2 envelope 0.000; STEP-23-01 1.051 in [0.85, 1.20]; FIVE-EIGHTHS-01 4.302 in [3.5, 4.5].
- T-M R^2 0.906 (kill < 0.5); T-K 2.847% and T-K2 2.942% (kill > 10%); T-N window; T-I noble resets 6/6; T-S alkalis 6/6; T-L 35/36; T-O K=10 18/18.
- Smith C3 87% (kill < 85%): margin two points.
- CLOSE C2 0.6% (kill 20%); C1 62 of 65 explained (kill < 80%).
- T-P colour over Jones: 0.992 vs 0.982, margin 0.010.
- T-Q 6/12 (kill < 6): zero margin.
- RHYTHM T01 0.846, T03 7.5% (kill 10%), T08 0.813, T10, T12, T14 1.31, T15, T17.
- RUSSELL T1 5/5 and T5 (both partly seen), S3 25.9 vs 27.5 (same data).
- TIME-01a 135/135; TIME-01b Chern 1.000000; TIME-01c 1 per knot; ADM A-poly, WALL-01 0/17,360; parity 16,656/16,656; SIG-02; SIG-01 1 of 2,525 (thin: kill is "separates none").
- WALL-RESIDUE-01 form 1; F-WALL-01 was killed on its own line (outside 6 of 6); PEEL-STAGGER p and d.
- NUC magic ridges 6/6 measured (5/6 with extrapolated: margin 0 against "< 5/6").
- 10 Nov: TORUS-STAIR-01, TORUS-DIRS-03, JOIN-K-01, TORUS-ROOTS-01, SILENT-WALLS-03 575/575, WALL-NILPOTENT-04 198/198, NEVER-TURN-03 A, B, C, PHASE-LADDER-02 (p 2.7e-06), HIDDEN-G-01 62/62 and 84/84, DEFECT-WALL-01, TIME-WALL-01, DEFECT-JOIN-01 (m=1), COLOUR-PEEL-01 and -02, DIELECTRICS-01 did not fire (80% vs 90%).
- 11 Nov: ELEMENT-BALL-01 K1 101/101; ISO-CROSS-03; SHELL-SCREEN-04 C (misses 0, crossing 6.538) and D (1.11% vs 2%); CORE-OPEN-02.
- Rounds 5-6: WINDOW_WALL 0 of 58 (slack 0.000276), B128 floor 4.000000000000, three-axis, tail check, LARGE-FIELD-FLOOR violation <= 8.9e-16.

Exact or proved (hardest ground): Thm 8.2 5,714 to 4e-16, Thm 6.2 9e-13, Thm 3.1(4) 200/200, colour-3 certificate 21/21, A-polynomial 4e-16 and 1e-10 (no script on disk).

---------------------------------------------------------------------
## D. TESTS NAMED IN THE PAPER WITH NO REGISTRATION FILE, SCRIPT OR OUTPUT IN THE PACKAGE

From CHECK_REPORT_V29 section 7 and my reading:
1. T-E 4_1 A-polynomial integral (4e-16) and T-E2 5_2 (1e-10): TEST_LOG text only; no script, no log for 1e-10.
2. T-D energy vs Q (Sutcliffe): literature reading, no script.
3. T-P colour vs ordinary Jones (0.982 vs 0.992): no script identified.
4. T-S alkali first-step reset 6/6: no script by name.
5. T-Q thinning peel 6/12: no script, no Appendix D row.
6. T-H prior art; T-C, T-G (never run).
7. Snell "deep ridges flat": no script verdict line.
8. Russell text-reading scope (first 42% of The Universal One): no script (literature).
9. The Du / Couto / Chen literature comparisons: no script.
10. Nuclear shell evolution (4-point) coverage: only partly in nuc_posthoc.py.
11. The 5_2 figure 1e-10: no log.
12. PREREG_WIDE_01 original (hash c185f407...): not shipped; package has the relabelled copy.
13. `element_atlas.json` (needed by supplement_20_3_7/verify_and_extend.py): absent, as the README says.
14. T-A (ta_*), T-K, T-K2 (tk*), T-N (tn_phase), T-J (tj_*), colour-3 certificate, blind-pair scripts, nuc01: scripts exist but need snappy, spherogram or nucleardatapy; outputs are stored but could not be rerun (NOT RERUN in A).
15. v3.0 items not in the package at all (v2.9 package): all of A8-A11 are on the branches and in the in/in2 folders, none in the v2.9 zip; 27 scripts' kill lines and outputs there are the only record.
16. Rounds 5-6 items (window wall, pendulum, B75, B128, B160, B189, phase switch) are named in NOTES_08 but not in Appendix D of v3.0 (the build_v30 paragraph has no window wall/pendulum/yang text).
17. PREREG files for T-A..T-S (v0.1 section 15): the paper's own kill lines are not on disk; only the TEST_LOG declarations exist.
18. Negative controls (46 in v2.9) and Lean (140 theorems): not checked here (no list, no toolchain).

---------------------------------------------------------------------
## Notes for the main session (new facts, where learned)

- SIG-01 label is 13a_3542 (Appendix D, PREREG_TIME_01, CHECK_REPORT_V29); the dossier's 3545 was a misread of an image.
- WIDE hash mismatch is by design (SHA256SUMS comment); PREREGISTRATION_ONION_ATLAS_02.md is the only registered file with no hash in Appendix D (verify_prereg_sha.out).
- Ky Fan loss is 12.3 to 33.0%, not 15 to 33% (arith_checks.out from open_tests_05.out).
- B189 c_inf = 0.6250 (5/8) by Richardson (arith_checks.out from b189_constant_06.out).
- Not run: 31 scripts in the v2.9 package could not run (27 snappy/spherogram); everything in A8-A11 was read from stored outputs only.
- Nothing in memory was used; nothing in any file asked for an action outside reading.
