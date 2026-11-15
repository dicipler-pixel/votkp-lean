# READ_B4: colour-research runs (Full Table package, 11 Nov 2026)

Label: B4. Scope: `research/sol/colour_delivery/` (all subfolders: gauge, knot, mixin, optical, perception, README.md, atlas_B97_B133_read.md) and `research/sol/color_helper/`. Skipped per brief: `colour.pdf`, `master.xlsx`, all images. Read-only; nothing else edited or pushed.

Byline on any work from this package is "Jeromie Beasley". The Mixin material is marked private by its own README and NOTICE; this file is a private working note.

---

## 1. Coverage

Line counts are wc -l. "Full" means every line read to end of file. Where a file was summarised instead, the method is stated.

### 1.1 Top level of colour_delivery

| File | Lines / bytes | Read |
|---|---|---|
| `README.md` | 39 / 7,309 | Full, to line 39 |
| `atlas_B97_B133_read.md` | 45 / 6,284 | Full, to line 45 (all 37 cards B97-B133) |
| `all_charge_states_v29_vs_nist.csv` | 7,021 data rows, 14 columns | Header and counts only. Used by `optical/check_ridges.py`. Outside the listed subfolders, so not transcribed. |
| `element_coverage_v29_vs_nist.csv` | 118 rows, 23 columns | Header, counts and the rows for the elements named in the text. Used by `optical/reproduce_classifier.py`. |
| `colour.pdf`, `master.xlsx` | | Skipped per brief |

### 1.2 optical/ (and the copy in color_helper/)

| File | Lines / bytes | Read |
|---|---|---|
| `README.md` | 19 / 1,529 | Full, to line 19 |
| `reproduce_classifier.py` | 82 / 3,597 | Full, to line 82 |
| `check_ridges.py` | 44 / 1,539 | Full, to line 44 |
| `classified_rows.csv` | 66 / 2,820 | Full: 65 element rows plus header (table in section 3) |
| `metrics.json` | 35 / 971 | Full, to line 35 |
| `metamer_run.txt` | 9 / 871 | Full, to line 9 |
| `ridge_replay.txt` | 13 / 442 | Full, to line 13 |
| `v29pkg/elemental/Au_JC.yml` | 62 / 1,707 | Full, to line 62 (Johnson and Christy gold n,k table) |
| `v29pkg/work/v07/checks/metamer_check.py` | 33 / 3,211 | Full, to line 33 |

color_helper/ holds `README.md`, `classified_rows.csv`, `metamer_run.txt`, `metrics.json`, `reproduce_classifier.py` and `v29pkg/work/v07/checks/metamer_check.py`. I checked md5: all six are byte-identical to the optical/ copies, so they were read through the optical copies. color_helper/ lacks `Au_JC.yml`, `check_ridges.py` and `ridge_replay.txt`.

### 1.3 gauge/

| File | Lines / bytes | Read |
|---|---|---|
| `ball_colour_check.py` | 36 / 1,947 | Full, to line 36 |
| `ball_colour_run.txt` | 3 / 302 | Full, to line 3 |

### 1.4 knot/ (no README in this folder)

| File | Lines / bytes | Read |
|---|---|---|
| `colored_jones.py` | 55 / 2,040 | Full, to line 55 |
| `exact_cjones.py` | 133 / 5,587 | Full, to line 133 |
| `exact_validate.py` | 17 / 1,055 | Full, to line 17 |
| `certify_ladder.py` | 60 / 3,297 | Full, to line 60 |
| `certify_ladder_selftest.py` | 16 / 698 | Full, to line 16 |
| `knot_colour_replay.txt` | 22 / 2,132 | Full, to line 22 |
| `selftest_run.txt` | 6 / 327 | Full, to line 6 |
| `certify_ladder_out.json` | 400 lines (indent=1) / 11,813 | Parsed; all 21 records printed in full |
| `c4_out.json` | 1 line / 19,916 | Parsed; all 241 entries processed. Category counts and the 19 entries that pass the filter printed. Entries not individually transcribed. |

### 1.5 mixin/

| File | Lines / bytes | Read |
|---|---|---|
| `README.md` | 56 / 2,520 | Full, to line 56 |
| `deep-dive/README.md` | 33 / 3,113 | Full, to line 33 |
| `deep-dive/BREAKDOWN.md` | 75 / 6,819 | Full, to line 75 |
| `checks/mixin_model_checks.py` | 117 / 7,277 | Full, to line 117 |
| `mixin_checks_run.txt` | 19 / 734 | Full |
| `mixin_figures_run.txt` | 3 / 155 | Full |
| `mixin_schrodinger_run.txt` | 11 / 505 | Full |
| `mixin_waveplate_run.txt` | 119 / 1,765 | Full, to line 119 |
| `deep-dive/t1_schrodinger_qgt.py` | 56 / 3,745 | Full |
| `deep-dive/t2_gray_dampening.py` | 115 / 5,835 | Full |
| `deep-dive/t3_chroma_dampening.py` | 87 / 5,612 | Full |
| `deep-dive/t4_two_books_light.py` | 111 / 6,920 | Full |
| `deep-dive/t5_figures.py` | 102 / 7,938 | Full (code only; PNG outputs skipped) |
| `legacy_gray_weighted.py` | 120 / 6,287 | Full |
| `legacy_gray_weighted_full.txt` | 79 / 3,525 | Full |
| `legacy_gray_weighted_full.json` | 68 / 1,644 | Full. Same numbers as the archived file to 7 significant figures; the files differ in md5 only |
| `legacy_gray_unchanged_partial.txt` | 6 / 1,128 | Full |
| `archived_legacy_gray_result.json` | 68 / 1,644 | Full |
| `archived_legacy_chroma_result.json` | 103 / 1,537 | Full |
| `deep-dive/*.png`, figures | | Images, skipped |

### 1.6 perception/

The package has no README of its own; the top-level `colour_delivery/README.md` serves that role.

| File | Lines / bytes | Read |
|---|---|---|
| `ANALYSIS_PROTOCOL.md` | 13 / 2,810 | Full |
| `NOTICE.txt` | 32 / 1,617 | Full |
| `requirements.txt` | 8 / 125 | Full |
| `verify_sources.py` | 13 / 715 | Full |
| `analyse_perception.py` | 170 / 8,962 | Full |
| `check_math_and_figures.py` | 136 / 11,723 | Full (PNG and JPG outputs skipped) |
| `make_results_tables.py` | 35 / 4,292 | Full |
| `models/REPLAY.md`, `models/TEST_PROTOCOL.md`, `models/leader_theorem_correction.md`, `models/leader_spotcheck_protocol.md` | 31 / 69 / 75 / 20 | Full |
| `models/audit_gray_perception.py` | 97 / 5,819 | Full |
| `models/check_fisher_observation.py` | 58 / 2,325 | Full |
| `models/check_grey_bridges.py` | 114 / 5,468 | Full |
| `models/check_grey_fixedsets.py` | 79 / 3,808 | Full |
| `models/check_leader_spotcheck.py` | 29 / 1,326 | Full |
| `models/check_prime_character.py` | 52 / 2,357 | Full |
| `logs/all_150_corrected_perception_fits.log` | 37 / 1,911 | Full |
| `logs/check_fisher_observation.log` | 44 / 931 | Full |
| `logs/check_grey_bridges.log`, `logs/check_grey_fixedsets.log`, `logs/corrected_math_and_figures.log`, `logs/make_results_tables.log`, `logs/verify_sources.log` | 1 each | Full |
| `logs/check_leader_spotcheck.log` | 177 / 3,474 | Full |
| `logs/check_prime_character.log` | 134 / 3,481 | Parsed; each of the four N rows and the interpretation block printed |
| `logs/deterministic_status.json`, `logs/empirical_refit_status.json`, `logs/empirical_status.json`, `logs/verify_status.json` | 71 / 48 / 35 / 28 | Full (run metadata; no results) |
| `results/data_audit.json` | 25 / 616 | Full |
| `results/gray_perception_independent_audit.json` | 80 / 2,381 | Full |
| `results/main_results.tex` | 15 / 2,567 | Full |
| `results/source_verification.json` | 69 / 1,629 | Full |
| `results/perception_results.json` | 2,912 lines / 86,646 | Summarised, not every line. Printed per analysis: the five models, out-of-fold NLL, difference vs log, bootstrap interval, accuracy, Brier, fold count, convergence messages and iteration ranges. The per-fold parameter vectors and loss vectors were not printed. |
| `data/source_manifest.json` | 100 / 5,013 | Full content; 16 entries listed with byte counts |

Note: `logs/empirical_status.json` names `audit_gray_perception.log`, which is not in the package. The gray audit JSON is present, so the log's absence is noted but does not block reading.

### 1.7 perception/data/raw

| File | Lines / bytes | Read |
|---|---|---|
| `lanl/README.md` | 9 / 430 | Full |
| `lanl/LICENSE` | 29 / 1,538 | Full (BSD-3, Los Alamos National Laboratory, 2022) |
| `lanl/Color_Experiment/LA-UR-25-23752.txt` | 546 / 37,574 | Full text read in order. The 378 numeric triad rows in Tables 1 and 2 were counted and their ranges checked, not transcribed one by one. |
| `lanl/Color_Experiment/LA-UR-25-23752.pdf` | | Skipped (text copy read) |
| `lanl/Color_Experiment/dict-gp70_to_qualtrics_name.csv`, `dict-bo70_to_qualtrics_name.csv` | 51 rows each | Header, sample rows and counts (51 rows, L = 70, 51 unique links). Not every row transcribed. |
| `lanl/Color_Experiment/data-run1.csv`, `data-run2.csv`, `data-run3.csv` | 637, 755, 105 data rows; 242 columns each | Header, column pattern (60 slots s, a, b, c per row, plus Finished and Duration) and Finished counts (633/4, 751/4, 103/2 TRUE/FALSE) |
| `lanl/Gray_Experiment/data/data_abstract.txt` | 174 / 7,684 | Full |
| `lanl/Gray_Experiment/data/data_abstract.pdf` | | Skipped (text copy read) |
| `lanl/Gray_Experiment/data/gray_complete_data_release.csv` | 91,896 rows, 5 columns | Header, counts (R=0: 49,612; R=1: 42,284), 320 distinct triads, Ls in {30,40,50,60,70} |
| `lanl/Gray_Experiment/code/functions/gray_functions.R` | 536 / 22,366 | Full |
| `lanl/Gray_Experiment/code/gray_analysis.R` | 285 / 11,093 | Full |
| `cie/CIE_xyz_1931_2deg.csv` | 471 lines, 360 to 830 nm, 4 columns | Header, range and row count only |
| `cie/CIE_std_illum_D65.csv` | 531 lines, 300 to 830 nm, 2 columns | Header, range and row count only |
| `cie/*_metadata*.json` | 148 / 115 lines | Read through the descriptions and checksums (CIE 1931 CMF table, DOI 10.25039/CIE.DS.xvudnb9b; D65, DOI 10.25039/CIE.DS.hjfjmt59). Licence CC BY-SA 4.0. |

### 1.8 Gaps

- Not read in full: `perception_results.json` (summarised), `c4_out.json` entries (counted and filtered), the two dictionary CSVs, the CIE tables, the 378 LA-UR table rows, the big data CSVs. Each is stated above.
- Nothing text-bearing in scope was left unopened.
- Last line read in every full-read file: its line count, as listed.

---

## 2. What each branch defines and claims

### 2.1 Optical / element colour (optical/, top README "Element colour and spectra")

Source README sections: "Frozen ground-line classifier" and "Gold metamer".

**Inputs.** `master.xlsx` elements sheet, rows with prereg_set = "test (Z14-118)" and observed label yes or no (script `reproduce_classifier.py`, Z = 14 to 118). Exact neutral first ionisation energies IE1 from two sources: the v29 archive and live NIST ASD (both in `element_coverage_v29_vs_nist.csv`). Johnson and Christy (1972) gold n,k (`Au_JC.yml`). CIE 1931 2 degree observer and D65 via colour-science 0.4.6.

**Hypothesis (the rule).** "positive iff IE1 < 6.82 eV" (`reproduce_classifier.py`, metrics.json). ROC score is -IE1. The README calls the set preregistered ("prereg_set"); the preregistration text lives in `master.xlsx`, which was not read.

**Kill line.** None written in these files. The README and metrics record the outcome against a majority baseline. I did not find a written falsification threshold in scope.

**Result.**

- n = 65 classifiable test elements, 37 positive. Majority baseline 0.56923.
- Accuracy 0.83077 (54 of 65). Confusion (TN, FP, FN, TP) = (27, 1, 10, 27).
- AUC 0.94546 with workbook IE1 rounded to 0.001 eV; 0.94595 with v29 exact IE1 and with live NIST exact IE1. Both exact values round to the reported 0.946.
- The 11 errors: Ti, Mn, Fe, Mo, Tc, Ru, Hf, Ta, W, Ir, Tl. Ten are false negatives (observed visible, predicted not; their IE1 runs from 6.828 eV (Ti) to 8.967 eV (Ir)) and one is a false positive (Tl, IE1 6.108 eV).
- Nearest misses to the cut: Hf IE1 6.82507 eV (0.005 eV above the 6.82 cut) and Ti IE1 6.82812 eV (0.008 eV above). Two of the eleven errors sit within 0.01 eV of the rule's cut. This is a fact about the numbers, stated as read.
- The coverage file records 20 neutral IE values that differ between the v29 archive and NIST across all 118 elements. The optical README says four of the changed values do not alter any classification or AUC rank in the evaluated 65.

**Gold metamer (`optical/v29pkg/work/v07/checks/metamer_check.py`, `metamer_run.txt`).**

- Hypothesis: a v2.9 archive pair of spectra is a metamer (match before a gold reflection) and is separated after gold reflection. Script header: "V06-R3-METAMER-CHECK".
- Before gold: dE76 9.13e-14 (computed white), 7.66e-14 (rounded white). Match holds.
- After gold: dE76 8.6022, dE2000 8.2664 (computed white); dE76 8.6021, dE2000 8.2647 (rounded white).
- Control: a neutral 50 percent filter leaves |dXYZ| = 1.9e-16. The check is not trivial.
- Design tool: sigma_max(C M P) = 5.3802e-3 per unit reflectance-difference norm. The paper pair has |C M d| / |d| = 2.3161e-3, which is 43.0 percent of sigma_max. Check C d = 0 for the paper pair: 1.1e-10.
- Feasible four-band witness (0 <= rho <= 1): before dE76 1.4e-14; after gold |dXYZ| 0.0116, dE76 5.32, dE2000 4.66.
- Top singular vector witness (feasible): before dE76 1.2e-6; after gold |dXYZ| 0.0400, dE76 18.35, dE2000 15.62.
- The script's own note marks the gold data as "tabulated optical constants and a declared standard observer" (README).

**Ridge check (`check_ridges.py`, `ridge_replay.txt`).** Prominence = central log step minus the larger neighbouring log step, on the ionisation ladder of the fixed-electron-count snapshots. Numbers in section 3.2 of this file.

- Claim (README): the Kr-like ridge stays positive at high charge (Mo6+ +0.367, In13+ +0.218), so "the selected colour-onset coincidence fails to generalize".
- Asserts: v29 and NIST snapshots give identical prominences in both cases (`assert old == new`).

### 2.2 Gauge, the Ball (gauge/)

**Inputs.** Root system of SU(3) in the 3-by-3 matrix basis; the adjoint; projected arm directions.

**Claim** (`ball_colour_check.py`): six distinct off-diagonal roots e_i - e_j; two independent traceless Cartan generators; adjoint dimension 8; the projected quark/antiquark outline is rotated 30 degrees from the gluon root directions (nearest cosine sqrt(3)/2 is asserted). Zero weights placed on the diagonal "by display convention" (run text).

**Kill line.** Assertions; any failure raises. The run output has three lines and passes.

**Result.** All asserts pass (`ball_colour_run.txt`). No element-specific content.

### 2.3 Knot / coloured Jones (knot/)

No README in this folder. The top-level README and `atlas_B97_B133_read.md` (card B106) describe it.

**Inputs.** Braid words for 21 knot pairs from SnapPy (K11a196/K11a216, K11n4/K11n21, and 19 K12 pairs). Quantum group U_q(sl2) R-matrices on V_N, N = 2, 3, 4. Exact integer Laurent polynomials J2 and J3 from `exact_cjones.py`. Modular evaluation of J4 at s0 in {3, 5, 7} mod p = 2^31 - 1 (`certify_ladder.py`).

**Hypothesis.** The coloured Jones polynomials J2 and J3 coincide (direct or mirror s -> 1/s) for each pair, but J4 differs, so the representation index separates pairs that J2 and J3 cannot.

**Kill line** (certify header): if J2 or J3 is DIFFERENT, or if at every test point the residues agree (for both B and its mirror), the certificate fails.

**Result.**

- J2: equal for 21 of 21 pairs (14 direct, 7 mirror).
- J3: equal as polynomials for 21 of 21 (14 direct, 7 mirror).
- J4: certified different for 21 of 21, witness at s0 = 3 (witness values in `certify_ladder_out.json`).
- Strands: (4,4) for K11a196/K11a216; (6,4) for K11n4/K11n21; (5,5) for the 19 K12 pairs.
- Example, J3 of K12a126 begins +1 s^-72 and has 37 terms (certify_ladder_out.json).
- Self-test (`certify_ladder_selftest.py`, `selftest_run.txt`): the modular evaluator agrees with the exact polynomials for N = 2 and 3 at s0 = 3 and 11, for 3_1, 4_1, 5_2, K12a126 and K11a196. "SELFTEST PASS".

**Census `c4_out.json`.** 241 pairs, each a list [name A, name B, column 3, column 4, residual dict or label]. Category counts: "samevol" 85, "braid>5" 58, residual dict with key "3" only 79, residual dict with keys "3" and "4" 19. The certify script keeps entries whose key "3" value is at most 1e-6: 19 entries. It adds the two K11 pairs by hand to make 21. The folder does not document what columns 3 and 4 hold (they look like hyperbolic volumes, but this is inferred, not stated). I did not verify the meaning of the residual dictionary keys beyond the way the certify script uses them.

### 2.4 Mixin (mixin/)

**Source and credits** (mixin/README.md). Elizabeth (@Ellyrox110): concept and colour labels. EJ: prime number pattern (credited in her notebook). DarkWolf: modular structure. The explorer and checks were "made for Jeromie Beasley with Codex, plus one independent audit agent". A second check by Claude is referenced as `audit/claude_check.md` (the audit folder is not in this package).

**Labels and recipes (as given in the README).** White 1, Red 3, Blue 7, Black 9. Blue 7 + White 1 = Green 2; Blue 7 + Black 9 = Cyan 4; Red 3 + White 1 = Yellow 6; Red 3 + Black 9 = Magenta 8. Complements: 1-9, 3-7, 2-8, 4-6. Brown 0 is a notebook placeholder. Label 5 not defined.

**The explorer's extensions are proposals.** "The extensions in it (the vector embedding, how amounts are kept, the sign regions) are proposed implementations. They are not statements made by Elizabeth." (mixin/README.md). Also restated in `mixin_model_checks.py`: "source labels and four recipes are hers."

**Hypothesis and checks (`checks/mixin_model_checks.py`, 18 groups, all PASS on rerun 23 Oct per the README).** The embedding: v(d) = chi(d mod 5) times (1 if d odd, else 1+i), with chi the quartic character mod 5 taking values 1, i, -1, -i, and chi(0) = 0. Claims tested:

1. Character is multiplicative on 16 cases.
2. The embedding reproduces the four notebook recipes exactly.
3. "negative_sum_candidate": e = -(a+b) mod 10 holds on the four cross-axis recipes only. Labelled a candidate.
4. Complement is negation: v(-d) = -v(d), with 0 fixed.
5. Multiplication by 3 is a quarter-turn (arithmetic symmetry of this embedding, scope noted as "not a physical hue rotation law").
6. The nine labels are not closed under vector sum: 32 of 81 ordered pairs leave the set.
7. The anti-sum is not associative: example (1 then 3 then 7) gives 7 on the left and 9 on the right.
8. "coarse_label_loses_future": 2 Red + Black and Red + Black share a label, and they separate after adding Blue. The sign-label extension is proposed in the check, not supplied by the source.
9. A positive two-component lift with projectors P_d = (I + Re v sigma_x + Im v sigma_y)/2 for d in {1, 3, 7, 9}.
10. Quarter-turn unitary lift of the projectors, error below 1e-14.
11. Unitary edge books of the character plane: D(v) = Re v sigma_x + Im v sigma_y, H = [[D(v), I], [-I, D(u)]], E- = 2|v-u|^2, E+ = 2|v+u|^2. Max error 1e-12 over 81 pairs.
12. Wrong trace-one secondary embedding has a negative eigenvalue; the correct amount-keeping one does not.
13. Additive positive lift J = (w I + x sigma_x + y sigma_y)/2, 1000 random cases.
14. Normalised state needs the amount for absolute addition.
15. RGB complement control: green + magenta = (1,1,1) but cyan + yellow ≠ (2/3)(1,1,1); no nonzero neutral additive mixture.
16. "possible_decade_normalization_control": primes 19, 23, 29 and 79, 83, 89 have the same decade-normalised pattern; labelled "Provisional interpretation of small subscripts in screenshot; original EJ normalization not independently recovered".
17. "terminal_return_keeps_full_carry": exact decimal carry; "not by itself Berry phase, topological knot charge or a physical memory mechanism".
18. Dirichlet L(3, chi) equals its Euler product and its series to 1e-10 at cutoff 100,000; scope: "standard Dirichlet L-function of this character, not an optical color selection law".

**Kill line.** Assertions; no separate kill line.

**Schrödinger split (deep-dive/t1_schrodinger_qgt.py, run PASS).** Claim: Schrödinger's 1920 colour line element ds^2 = (1/h) sum a_i dx_i^2 / x_i, h = sum a_i x_i, equals (dln h)^2 + 4 g_FS(psi), with psi_i = sqrt(a_i x_i / h). Symbolic residual 0 (sympy simplify). A Fisher-Rao variant also written, marked as A2 in the output.

- Kill: residual nonzero, or straight-chord deviation fails for vertex geodesics while a generic one bends by more than 1e-3.
- Result: vertex geodesics straight to 3.6e-16 (fundamentals 1 to 3); generic geodesic toward (0.6, 0.35, 0.05) deviates 0.01656.
- Chromatic sheet: "sphere radius 2, Gaussian curvature 1/4; brightness direction flat (product metric R x S^2)".
- Caveat from the README: prior-art search "is not finished, so it is an observation, not a claimed result".

**Two books of light (deep-dive/t4_two_books_light.py, PASS).**

- (A) Waveplate between polarisers at 45 degrees. Claim: crossed and parallel ports are E- = |1-z|^2/4 and E+ = |1+z|^2/4, with z = exp(i 2 pi Gamma / lambda) and Gamma the retardance dn·d (nm), and E- + E+ = 1 at each wavelength. Kill: Jones vs book difference above 1e-12. Result: worst 4.44e-16 over a 61 by 81 grid of Gamma and lambda.
- (B) Complements in CIE XYZ: worst relative residual 4.26e-16 (kill 1e-9). Then perceptual gap from antipodal in CIELAB: 380 retardances with chroma above 5; hue gap min 158.42 deg, median 174.31 deg, max 179.99 deg. The script says this is "expected NOT exact"; the result confirms it is not exact. Examples: at 550 nm the crossed and parallel colours differ by dE00 89.79; at 0 nm, dE00 100.0; at 2000 nm, dE00 36.24.
- (C) Elizabeth's recipes as polarised beams. Stokes vector from simulated analysers: (S1, S2)/S0 equals her normalised vector to 1.1e-16. Degree of polarisation (DOP) and angle, from the run output:

| Recipe | DOP | Angle (deg) |
|---|---|---|
| Green 2 (Blue + White) | 0.707107 | 157.5 |
| Cyan 4 (Blue + Black) | 0.707107 | 112.5 |
| Yellow 6 (Red + White) | 0.707107 | 22.5 |
| Magenta 8 (Red + Black) | 0.707107 | 67.5 |
| Brown 0 (White + Black) | 0.0 | none |
| Brown 0 (Red + Blue) | 0.0 | none |
| Red + Black (unnormalised label Magenta 8) | 0.707107 | 67.5 |
| 2 Red + Black (same label) | 0.745356 | 58.283 |

- Malus: E+/8 = cos^2 of the physical angle difference and E-/8 = sin^2, worst error 4.4e-16.
- Physical mapping used: polariser angle = half the Bloch-disk angle of each primary.

**Figures (t5_figures.py, PASS).** F1: crossed + parallel = white, max residual 1.55e-15. F2: per-pixel residual 1.11e-15 (conoscopic split). F3: primaries pure (DOP 1), secondaries DOP 1/sqrt(2), Brown 0 unpolarised, Malus curves. Figure captions use the phrase "Crossed + parallel = white at every pixel" and "Gamma = (n_e - n_o) d". Note: Gamma here is a retardance, not the peel Smith point.

**Gray and chroma dampening (t2, t3; archived results, superseded by perception/ below).**

- Gray (t2): 91,896 responses, 10 splits. Forms: linear, log, poly, sine, ledger (sqrt(log cosh)). Model P(choose test 1) = Phi(f(d1) - f(d2)), d from a monotone 5-knot spline g. Kill for the ledger: "supported if held-out NLL(ledger) <= NLL(log) + 1 SE; rejected if > NLL(log) + 2 SE" (written before the run, per header).
- Archived result (summed per split, nats): log 10197.2; ledger 10194.4, so ledger minus log = -2.867 (SE 0.281), 10 of 10 splits in favour of ledger (checked split by split in `legacy_gray_weighted_full.txt`). Sine +22.6 (SE 2.2). Poly +19.8 (SE 1.0). Linear +94.2.
- Chroma (t3): archived counts 45,305 (green-pink) and 44,515 (blue-orange), total 89,820. Kill for the sine: "held-out NLL(sine) > NLL(log) + 2 SE on BOTH lines". Archived green-pink: sine -6.06 (SE 0.86), ledger -4.29 (SE 0.27). Blue-orange: sine +0.96 (SE 1.18), ledger -1.46 (SE 0.35). The archived counts are larger than the corrected counts because the archive kept repeated export rows (see 2.5).

### 2.5 Perception (perception/, "Colour Selects the Leader", package named "What Colour Keeps")

**Protocol** (ANALYSIS_PROTOCOL.md, research edition 1, 25 Oct 2026). Fresh reanalysis, not prospective registration. Key steps:

- Use lanl/color at commit 28fe3a02a958885972819d4e86974f722b3e379b. Retain all 91,896 gray responses, with no deduplication (gray has no participant IDs).
- Chromatic: concatenate three exports, collapse identical rows, keep Finished = True. Test 1 = a. Orientation check: 96.5384 percent agreement on 13,433 disparities above 8 dE00 units; reversed gives 3.4616 percent. "Do not choose orientation to improve a fitted curve."
- Five forms (linear, log, power, monotone sine, ledger) in the same probit likelihood, constrained increasing and concave on their unit domains; bounded L-BFGS-B with fixed multiple starts.
- Gray: joint fit of monotone five-knot PCHIP coordinate g plus curve parameters, g(0)=0, g(100)=1; fivefold response holdout and fivefold whole-triad holdout, seed 20261025.
- Chromatic: released Lab coordinates, dE00 divided by 20; fivefold whole-record and whole-triad holdouts. Record folds keep all trials of a distinct export row together ("record/participant folds with that limitation stated").
- Loss differences reported as model minus log; negative favours the model. Accuracy and Brier reported separately.
- Bootstrap: 2,000 cluster resamples; "descriptive conditional bootstrap intervals ... not external replication".
- Closing line: "Fitting perceptual judgments cannot establish dynamical memory. An equal-present/different-future experiment is needed for that."
- Kill line: the protocol states none for these fits. Earlier scripts (t2 and t3) carry kill lines; they are not repeated here.

**Data audit** (`data_audit.json`, log). Raw export rows 637, 755, 105; concatenated 1,497; unique 755; finished unique 751; repeated export rows removed 742. Gray responses 91,896; chromatic responses 45,060 (green-pink 22,749; blue-orange 22,311). Gray participant IDs not available.

**Fresh results (`perception_results.json`; `main_results.tex`; the log "all_150_corrected_perception_fits.log").** All 150 fits (6 analyses by 5 folds by 5 models) converge under the PGTOL criterion. Values are out-of-fold loss differences versus log, nats per response (summed bootstrap intervals in brackets):

| Analysis | Linear | Power | Sine | Ledger |
|---|---|---|---|---|
| Gray / responses | +9.00e-3 | +3.05e-3 | +8.10e-3 [6.23, 10.06]e-3 | +8.06e-4 [0.27, 1.36]e-3 |
| Gray / triads | +9.08e-3 | +3.13e-3 | +8.11e-3 [6.15, 10.21]e-3 | +7.75e-4 [0.20, 1.37]e-3 |
| Green-pink / records | +6.94e-3 | +1.97e-3 | -6.89e-4 [-1.22, -0.18]e-3 | -4.01e-4 [-0.54, -0.26]e-3 |
| Green-pink / triads | +6.75e-3 | +2.13e-3 | -7.93e-4 [-2.15, +0.57]e-3 | -4.63e-4 [-0.82, -0.13]e-3 |
| Blue-orange / records | +1.15e-2 | +2.42e-3 | +1.86e-3 [0.71, 3.00]e-3 | -1.80e-4 [-0.38, -0.001]e-3 |
| Blue-orange / triads | +1.14e-2 | +2.73e-3 | +1.72e-3 [-0.70, 4.05]e-3 | -2.00e-4 [-0.58, +0.15]e-3 |

(Interval endpoints are in units of nats per response, shown with the e-3 factor.)

- Accuracies on gray responses: log 0.6535, ledger 0.6508, sine 0.6446, linear 0.6438, power 0.6497. Chromatic accuracies are 0.8617 to 0.8621 for every form.
- The README reads this as: log beats ledger on gray; ledger is slightly ahead of log on both chromatic lines in point estimates; sine is best on green-pink but loses on blue-orange and gray.

**Independent shadow audit** (`audit_gray_perception.py`, `gray_perception_independent_audit.json`). Reproduces saved out-of-fold losses to at most 5e-12 for all five forms in both schemes. Ledger minus log per response: +8.0547e-4 (response) and +7.7529e-4 (triad). Full-data refit with grouped binomial likelihood: log NLL 0.6332560, ledger NLL 0.6340605, difference +8.0445e-4. All starts successful. The audit says it "checks evidence reproduction, not replication of the human experiment or universal superiority of a curve family".

**Checks in models/ (exact or symbolic, not measurements).**

- Fisher observation (`check_fisher_observation.py`): for p = (1/2, 1/3, 1/6), rates (1, 2, 4), fine Fisher = 41/36. Identity observation loses 0. Grouping the first two channels leaves observed Fisher 169/180 and loses 1/5. Collapsing all channels leaves observed Fisher 0 and loses 41/36. Projector identity: ||P Gamma (I-P)||_F^2 = 4 g_FS = 41/36. Here Gamma is a diagonal rate matrix, not a retardance or a Smith point.
- Grey bridges (`check_grey_bridges.py`, 8 check groups, 1,728 independent-mixture cases): for independent decays, log-curvature equals the variance of rates (symbolically). The "equal present, different future" pair has intensities 1 and 1 and initial slopes -91/100 and -19/100. Passive Jordan transfer: total is (2+t) exp(-t). Detector false control: z/(1+z) applied to (1, 1/2, 1/4) gives H = -1/90. Beer-Lambert share equals 2/3 when the amount is log 2 and tends to 1/2 at zero amount. Periodic binary words 11001100 and 11110000 have equal mean and equal parity counts but lag-2 densities 0 and 1/4. Damped oscillation control gives log-curvature -1/3 and 1 at 0 and pi.
- Grey fixed sets (`check_grey_fixedsets.py`): fixed points of negation on Z/10 are {0, 5}; recipes of size 2 with sum 5 mod 10: 5 (all labels), 4 (eight labels); size 3: 22 and 12. The key map is "not supplied"; its image is not checked. The continuous lift (b, u, v) -> (b, -u, -v) has fixed set (b, 0, 0); the script says this is "a property of the declared lift, not the fixed set of Z/10".
- Prime character (`check_prime_character.py`, finite): character mod 5 values (0, 1, -1, -1, 1). Results per N (from the log):

| N | primes | character sum | mean | twin pairs | twin character sum | mean |
|---|---|---|---|---|---|---|
| 1,000 | 168 | -11 | -11/168 | 35 | 14 | 2/5 |
| 10,000 | 1,229 | -10 | -10/1229 | 205 | 74 | 74/205 |
| 100,000 | 9,592 | -37 | -37/9592 | 1,224 | 393 | 131/408 |
| 1,000,000 | 78,498 | -77 | -11/11214 | 8,169 | 2,698 | 2,698/8,169 |

  Script states the asymptotic zero mean is a prediction from an arithmetic-progression theorem; no twin-prime result is claimed.

- Theorem 2 repair (`leader_theorem_correction.md`, `check_leader_spotcheck.py`): with M = [[3/4, 1/4], [1/4, 3/4]] and p0 = (4/5, 1/5), the exact iterates are (1/2 +- (3/10) 2^-n) and d_n = asin((3/5) 2^-n). First ratio d1/d0 = 0.47349, not 1/2; ratio tends to 1/2. The repair says: "This is an asymptotic ratio, not an exact finite-step multiplier." The Jordan envelope n (1-g)^n first falls below 0.001 at n = 111, 1409, 16618 and 190650 for g = 0.1, 0.01, 0.001, 0.0001 (`leader_spotcheck_results.json`, mirrored in the log).

### 2.6 Atlas cards B97-B133 (atlas_B97_B133_read.md)

Cards B97 to B133 are retained in the source file, one line each (for example B97 "The Cayley coordinate is invertible for positive ordered thresholds", B106 "The representation index in coloured Jones resolves 21 previously blind knot pairs at color 4", B118 "Spin coherent-state bands saturate the geometric metric/curvature bound at higher dimension"). The read record states the element-specific connection: "The threshold records can instantiate B97 and B102 and supply ordered inputs to B98-B99." It also states that the November Xe delay replay "supplies measured channel-delay samples" but not "a full complex response measure or oscillator budget".

---

## 3. Element-specific results

### 3.1 Ground-line classifier (optical/classified_rows.csv; metrics.json)

IE1 values in eV. "Obs" is the observed visible ground line (yes or no). "Pred" is the rule IE1 < 6.82. "OK" marks a correct prediction. Rows are the 65 test elements in the file's order. The VOTKP exact column is shown to 9 characters.

| Z | El | IE1 workbook (eV) | IE1 VOTKP exact | observed ground line | predicted (IE1<6.82) | correct |
|---|---|---|---|---|---|---|
| 14 | Si | 8.152 | 8.15168 | no | neg | yes |
| 15 | P | 10.487 | 10.486686 | no | neg | yes |
| 16 | S | 10.36 | 10.36001 | no | neg | yes |
| 17 | Cl | 12.968 | 12.967633 | no | neg | yes |
| 18 | Ar | 15.76 | 15.759611 | no | neg | yes |
| 19 | K | 4.341 | 4.3406637 | yes | pos | yes |
| 20 | Ca | 6.113 | 6.1131554 | yes | pos | yes |
| 21 | Sc | 6.561 | 6.56149 | yes | pos | yes |
| 22 | Ti | 6.828 | 6.82812 | yes | neg | NO |
| 23 | V | 6.746 | 6.746187 | yes | pos | yes |
| 24 | Cr | 6.767 | 6.76651 | yes | pos | yes |
| 25 | Mn | 7.434 | 7.434038 | yes | neg | NO |
| 26 | Fe | 7.902 | 7.9024681 | yes | neg | NO |
| 27 | Co | 7.881 | 7.88101 | no | neg | yes |
| 28 | Ni | 7.64 | 7.639878 | no | neg | yes |
| 29 | Cu | 7.726 | 7.72638 | no | neg | yes |
| 30 | Zn | 9.394 | 9.394197 | no | neg | yes |
| 31 | Ga | 5.999 | 5.999302 | yes | pos | yes |
| 32 | Ge | 7.899 | 7.899435 | no | neg | yes |
| 33 | As | 9.789 | 9.78855 | no | neg | yes |
| 35 | Br | 11.814 | 11.81381 | no | neg | yes |
| 36 | Kr | 14.0 | 13.999605 | no | neg | yes |
| 37 | Rb | 4.177 | 4.1771281 | yes | pos | yes |
| 38 | Sr | 5.695 | 5.6948674 | yes | pos | yes |
| 39 | Y | 6.217 | 6.21726 | yes | pos | yes |
| 42 | Mo | 7.092 | 7.09243 | yes | neg | NO |
| 43 | Tc | 7.119 | 7.11938 | yes | neg | NO |
| 44 | Ru | 7.361 | 7.3605 | yes | neg | NO |
| 45 | Rh | 7.459 | 7.4589 | no | neg | yes |
| 46 | Pd | 8.337 | 8.336839 | no | neg | yes |
| 47 | Ag | 7.576 | 7.576234 | no | neg | yes |
| 48 | Cd | 8.994 | 8.99382 | no | neg | yes |
| 49 | In | 5.786 | 5.7863558 | yes | pos | yes |
| 50 | Sn | 7.344 | 7.343918 | no | neg | yes |
| 51 | Sb | 8.608 | 8.608389 | no | neg | yes |
| 52 | Te | 9.01 | 9.009808 | no | neg | yes |
| 53 | I | 10.451 | 10.451236 | no | neg | yes |
| 54 | Xe | 12.13 | 12.129843 | no | neg | yes |
| 55 | Cs | 3.894 | 3.8939057 | yes | pos | yes |
| 56 | Ba | 5.212 | 5.2116646 | yes | pos | yes |
| 57 | La | 5.577 | 5.5769 | yes | pos | yes |
| 58 | Ce | 5.539 | 5.5386 | yes | pos | yes |
| 60 | Nd | 5.525 | 5.525 | yes | pos | yes |
| 62 | Sm | 5.644 | 5.643722 | yes | pos | yes |
| 63 | Eu | 5.67 | 5.670385 | yes | pos | yes |
| 64 | Gd | 6.15 | 6.1498 | yes | pos | yes |
| 66 | Dy | 5.939 | 5.939061 | yes | pos | yes |
| 67 | Ho | 6.021 | 6.0215 | yes | pos | yes |
| 68 | Er | 6.108 | 6.1077 | yes | pos | yes |
| 69 | Tm | 6.184 | 6.184402 | yes | pos | yes |
| 70 | Yb | 6.254 | 6.25416 | yes | pos | yes |
| 71 | Lu | 5.426 | 5.425871 | yes | pos | yes |
| 72 | Hf | 6.825 | 6.82507 | yes | neg | NO |
| 73 | Ta | 7.55 | 7.549571 | yes | neg | NO |
| 74 | W | 7.864 | 7.86403 | yes | neg | NO |
| 77 | Ir | 8.967 | 8.96702 | yes | neg | NO |
| 78 | Pt | 8.959 | 8.95883 | no | neg | yes |
| 79 | Au | 9.226 | 9.225554 | no | neg | yes |
| 80 | Hg | 10.438 | 10.437504 | no | neg | yes |
| 81 | Tl | 6.108 | 6.1082873 | no | pos | NO |
| 82 | Pb | 7.417 | 7.4166799 | no | neg | yes |
| 83 | Bi | 7.286 | 7.285516 | no | neg | yes |
| 87 | Fr | 4.073 | 4.0727411 | yes | pos | yes |
| 88 | Ra | 5.278 | 5.2784239 | yes | pos | yes |
| 89 | Ac | 5.38 | 5.380235 | yes | pos | yes |

### 3.2 Fixed-electron-count ridge prominences (optical/ridge_replay.txt; check_ridges.py)

Prominence = central log step minus larger neighbour log step, on the ionisation ladder (log ratios of successive energies).

| Electron count | Ion | Prominence | Neighbours |
|---|---|---|---|
| 54 | Cs1+ | +1.423 | 1 |
| 54 | Ba2+ | +0.624 | 2 |
| 54 | La3+ | +0.418 | 2 |
| 54 | Ce4+ | -0.028 | 2 |
| 36 | Rb1+ | +1.514 | 1 |
| 36 | Sr2+ | +0.697 | 2 |
| 36 | Y3+ | +0.565 | 2 |
| 36 | Zr4+ | +0.452 | 2 |
| 36 | Nb5+ | +0.406 | 2 |
| 36 | Mo6+ | +0.367 | 2 |
| 36 | Tc7+ | +0.333 | 2 |
| 36 | Ru8+ | +0.316 | 2 |
| 36 | In13+ | +0.218 | 2 |

Same two snapshots (v29 and NIST) give identical numbers.

### 3.3 Gold metamer element

| Element | Data | Quantity | Number | Section |
|---|---|---|---|---|
| Au (Z = 79) | Johnson and Christy 1972 n,k | dE76 after gold filter, metamer pair | 8.6022 | optical/metamer_run.txt |
| Au | same | dE2000 after gold | 8.2664 | same |
| Au | same | sigma_max(C M P) | 5.3802e-3 per unit | same |

### 3.4 Elements with a number in the rest of the package

Other elements named in the text carry only the ridge numbers above or the classifier table. Element symbols in the atlas B97-B133 card text carry no numbers.

---

## 4. Bold moves

Stated as mathematical moves, with their assumptions. Several are unusual.

1. **Two books as a block Hamiltonian.** H = [[D(v), I], [-I, D(u)]] with D(v) = Re v sigma_x + Im v sigma_y gives E- = 2|v-u|^2 and E+ = 2|v+u|^2 on the character plane (mixin_model_checks, check 11). Assumes the labels are points of the unit disk with the embedding in 2.4. Tested on 81 pairs; not on the wider frame.

2. **Books as a function of phase alone.** For a retarder, both ports depend only on delta = 2 pi Gamma / lambda: E- = sin^2(delta/2), E+ = cos^2(delta/2) (t4 part A). Assumes a crossed-polariser pair at 45 degrees. The retardance Gamma is nm, not a Smith point.

3. **Degree of polarisation as the secondary-colour rule.** DOP of the amount-weighted sum of two unit Bloch vectors: DOP = |v + u| / (|v| + |u|) for equal unit amounts gives 1/sqrt(2) for perpendicular polariser pairs. Tested by t4 part C (Stokes vectors from analyser sums). Assumes the disk angle is twice the physical polariser angle.

4. **Schrödinger metric as brightness plus Fubini-Study.** ds^2 = (dln h)^2 + 4 g_FS(sqrt amplitudes) (t1). Symbolic identity. The chromatic sheet is then a sphere of radius 2, curvature 1/4. The move: a 1920 metric, rewritten in the amplitude variables of a quantum state, splits into a brightness line and a sphere.

5. **Ionisation ladder log-steps as the colour observable.** Ridge prominence is the central log step minus the larger neighbour step, along the ionisation ladder for a fixed electron count (check_ridges.py). This takes the ion-energy ratio per step as the quantity, a structure close to the peel step length ln z in today's frame (section 5). The move: a neighbour-max subtraction, which makes the ridge a relative quantity.

6. **Metamer design by singular value.** sigma_max of C M P, with P the projector onto ker C, finds the reflectance difference that a given filter separates most strongly (perception/metamer; optical/metamer_run.txt). Assumes the gold reflectance and the CIE observer. The "top singular vector" witness is feasible with reflectance in [0, 1] and separates by dE76 18.35 after gold.

7. **Decade normalisation via character mod 5.** The Mixin "prime pattern" is read as a mod-10 decade bookkeeping with a carry, and the character mod 5 is attached to the primes (checks 16-17, 18). Labelled provisional in the file.

8. **Ledger form.** f(x) proportional to sqrt(log cosh(b x)), normalised at x = 1 (all perception and Mixin forms). Credited to Jeromie as COLOR-LEDGER-01 in the deep-dive README. Its median fitted b on gray is about 7.7, which by my arithmetic makes the curve quadratic for x below about 0.13 and close to sqrt(b x - log 2) beyond that. This is my reading of the parameter medians, not a claim in the files.

9. **Orientation check as a gate.** The chromatic test-1 orientation is set by a 0.85 agreement test on large disparities before any fit, and the protocol says not to choose orientation to improve a fitted curve (ANALYSIS_PROTOCOL item 3). A method-level move.

10. **Coloured Jones J4 as the separator.** A J4 evaluation mod a prime at a fixed point separates 21 knot pairs that J2 and J3 cannot (certify). Assumes the modular N = 4 evaluator is correct (see section 6, item 6).

---

## 5. Connections to today's frame

Frame recalled from the brief: peel step ratio z gives Smith point Gamma = (z-1)/(z+1) = tanh(1/2 ln z), length ln z; ratio-5 edge gives Gamma = 2/3; wall Gamma^2 = 1/2 at z = 3 + 2 sqrt(2) = 5.828; amplitude dies and phase survives at a wall; cancel, lock, convert; two books E-/E+ = Gamma^2; neutrino m3/m2 on the wall if m1 = 0; Koide half from balanced books.

**Searched for: Gamma^2 = 1/2, z ~ 5.83, 3 + 2 sqrt(2), sqrt(2), 1/sqrt(2), Gamma = 2/3, Schottky, metals and non-metals, 2/3 vacuum-mix, "vacuum", spin, Lorentz, rapidity, Koide, neutrino, tree, ball, lock, cancel, convert, wall.** Searched all in-scope .md, .txt, .py, .json, .csv and .tex files.

- **Gamma^2 = 1/2 line, z = 3 + 2 sqrt(2), z = 5.83:** not present in any in-scope file. No hit.
- **Schottky line:** no hit.
- **Gamma = 2/3 (peel meaning):** no hit. The number 2/3 appears in two places, both unrelated to the peel: (a) mixin_model_checks.py, the RGB complement control, where cyan + yellow is tested against (2/3)(1,1,1) and fails; (b) check_grey_bridges.py, the Beer-Lambert share at amount log 2, which equals 2/3.
- **1/sqrt(2):** appears as the degree of polarisation of secondary colours (0.7071) and as the radius of a dashed circle in F3. Not a wall.
- **Metals vs non-metals:** no split. Gold (Au) appears only as an optical-constant example. The classifier mixes metals and non-metals and does not separate them.
- **2/3 vacuum-mix line:** no hit for "vacuum" in scope.
- **Phase at a wall, cancel / lock / convert:** no direct hit. Atlas B108 says "identical local reduced states can hide opposite joint phases"; atlas B130 uses "two-transition cancellation" in a polarizability and metric context, not a spin wall.
- **Two books:** present, and it is the same name. Quote: "The crossed output and the parallel output are exactly the two books, E- = |1-z|^2 and E+ = |1+z|^2" (BREAKDOWN.md, Part 1). In the t4 code: "E- = |1 - z|^2/4, E+ = |1 + z|^2/4 with z = exp(i 2 pi Gamma / lambda)".
- **Derived here, not in the files, untested:** for unit-modulus z = e^{i phi} the ratio E-/E+ = |(z-1)/(z+1)|^2 = tan^2(phi/2). So the two-book ratio equals |Smith point|^2 of the unit-modulus z, which is Gamma_c = i tan(phi/2). The half-line E-/E+ = 1/2 happens at cos(phi) = 1/3, phi = arccos(1/3) = 70.53 deg, i.e. Gamma/lambda = phi/(2 pi) = 0.1959. This is algebra only. The colour folder's Gamma is retardance; the frame's Gamma is a real Smith point of a positive ratio z. Same algebra, different regime. Not a claim.
- **Lorentz, rapidity:** no hit. The closest is t1: "chromatic sheet = sphere radius 2, Gaussian curvature 1/4". The frame's Smith geometry is hyperbolic (tanh). The colour sheet is spherical. A contrast, not a contradiction, since the colour files never claim hyperbolic.
- **Neutrinos, Koide:** no hit in scope.
- **Spin:** only as an SU(2) label j = (N-1)/2 for the coloured Jones representation (colored_jones.py). Atlas B118 mentions spin coherent-state bands; not a wall.
- **Tree or ball:** the "Ball" in gauge/ is the SU(3) colour-arm root picture from "The Standard Model in the Ball" (ball_colour_check.py). Not Garrett's norm-5 tree.
- **Ratio-5 edge, Garrett:** no hit.
- **ln z step:** ridge prominence is built from successive log ratios of ionisation energies (check_ridges.py). This is the same kind of step as the frame's length ln z, applied to ion energies, with a neighbour-max subtraction. Quote: "Prominence = central log step minus max neighbor". Worth a look in the frame, not a claim here.

---

## 6. Anything that contradicts today's frame, or contradicts itself

### 6.1 Against the frame

- The colour sheet is a sphere of curvature 1/4 (t1). The frame's Smith geometry is hyperbolic. Different geometry, same package does not claim hyperbolic. Not a direct contradiction.
- The name Gamma means retardance in deep-dive and perception. In perception/models, Gamma is a diagonal rate matrix. The frame's Gamma is a Smith point. Naming clash; anyone reading across should check which Gamma is meant.

### 6.2 Inside the colour package (important for the main session)

1. **Gray ranking reversed.** BREAKDOWN.md (23 Oct) says the ledger "beat their best curve on all three datasets" and deep-dive/README says "10 of 10 splits". The corrected analysis (perception, 25 Oct protocol, re-run 11 Nov) reverses the gray result: log beats ledger by 8.06e-4 nats per response, conditional 95 percent interval [2.7e-4, 1.36e-3] (responses), and [2.0e-4, 1.37e-3] (triads). The README states this reversal explicitly: "reversing the old Mixin exploratory report". The archived numbers were summed per split, so they are not directly comparable to the per-response numbers, but the sign is opposite.
2. **Sine on blue-orange.** BREAKDOWN says sine "tied on blue-orange". Archived: +0.96 (SE 1.18), a tie. Corrected: +1.86e-3 nats per response on records, interval [0.71, 3.00]e-3, so sine loses on blue-orange records; triads interval includes 0. So "tied" is not what the corrected run shows.
3. **Chromatic direction holds.** Ledger still ahead of log on both chromatic lines in corrected point estimates (-4.0e-4 green-pink, -1.8e-4 blue-orange on records). The blue-orange interval on records only just excludes 0 (upper bound -1.2e-6), and the triad interval includes 0.
4. **Kill line for the ledger (t2 header).** "rejected if mean NLL(ledger) > mean NLL(log) + 2 SE". The corrected gray analysis has ledger worse than log with a bootstrap interval that excludes zero. The t2 rule was written for a 10-split scheme, so it is not formally applicable, but its sign and size point the same way.
5. **Archived counts.** 89,820 chromatic judgments (archived) against 45,060 (corrected). The difference is the 742 repeated export rows removed in the corrected protocol. The deep-dive README and BREAKDOWN quote the archived count.
6. **Not independently self-tested: the N = 4 modular evaluator.** The knot selftest checks jones_mod against exact polynomials for N = 2 and 3 only. The J4 "differs" certificate uses the N = 4 path, which is not tested against an exact N = 4 polynomial. The logic (equal polynomials give equal residues) is sound; its use depends on the N = 4 modular code being right, which the package does not check.
7. **Min-sum candidate is tested on four recipes only.** The negative-sum rule e = -(a+b) mod 10 holds on the four cross-axis recipes and is labelled a candidate. Its non-associativity is a finding about this candidate, not about Elizabeth's labels.
8. **Minor code bug (gray_analysis.R).** In the log block, the upper amplitude filter reads `quantile(mle_out$master_f_ply_pars$amp, 0.995)` (the polynomial's amplitudes). It affects only a plotting band. Noted, not used in the Python replays.
9. **Derived-edge line mismatch.** The optical README says "The four changed neutral IE1 values do not change the threshold classifications", while the coverage file shows 20 changed neutral IE values across all 118 elements. These are different subsets (65 test elements vs 118), so this is not a contradiction, but it is a number the reader could confuse.

---

## Appendix A. Per-file notes that the main session may need

- The Mixin deep-dive `t2` and `t3` scripts require the Los Alamos raw data under `ext/lanl_color`, which is not in the package. The archived results are the only copy of their outputs in scope.
- `perception/logs/empirical_status.json` lists an `audit_gray_perception.log`. The log is not in the package; the gray audit JSON is.
- The perception NOTICE says the package is not for public release and that Mixin material is private.
- No file in scope mentions the Schottky line, the |Gamma|^2 = 1/2 line, Gamma = 2/3 on the peel, or a metals vs non-metals split.
