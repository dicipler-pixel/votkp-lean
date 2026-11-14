# Check report: VOTKP v2.9 code, proofs and data package (v29code.zip)

Checked 12 November 2026. Package: `/home/claude/in/.../research/sol/v29code.zip` copied to `/home/claude/check_v29/v29code.zip`, unzipped to `/home/claude/check_v29/pkg/` (kept pristine). Every rerun was made in a second copy, `/home/claude/check_v29/tree/`, so no stored output was overwritten. Raw stdout and stderr of every rerun: `/home/claude/check_v29/rerun/<folder>__<script>.out` and `.err`. Runner, comparer and report generators: `runall.py`, `compare.py`, `mkreport.py`, `writemd.py` in the same folder. No web was used for the checks; pip was used only to install packages (see Environment). No agents were spawned. Nothing outside `/home/claude/check_v29` was modified.

## 1. Inventory

| Item | Count |
|---|---|
| Folders | 160 (29 under `work/`) |
| Files | 1,105 (all 1,104 entries of `MANIFEST_SHA256.txt` re-hashed: 1,104 OK) |
| Python scripts (`.py`) | 214 in total: 167 under `work/`, `stagger/`, `v22/`, `supplement_20_3_7/`, `supporting_records/` (the replay set); 11 under `independent_checks/`; 2 under `lean/votkp-lean/scripts/`; `run.py`; the other 32 are 30 figure scripts plus `build.py` and `fix_v05.py`, and `rerun_all.py` (see skipped group below) |
| Stored script outputs | 109 `*_output*.txt` / `*_out.txt` files outside `independent_checks/`, 20 `.log`, 49 `.json` (data and results), 5 `.csv`, 2 `.pkl`; plus 107 `.stdout` and 107 `.stderr` audit logs in `independent_checks/v08_audit/audit_logs/`; 5 `relocation_test*_output.txt` records |
| Pre-registration files | 21 `PREREG*.md` / `PREREGISTRATION*.md` (19 listed in Table 10 and hashed in `SHA256SUMS_PREREG.txt`, plus `PREREGISTRATION_ONION_ATLAS_02.md` and a second copy of `PREREG_G02.md` in v11), 2 `.sha256` files (v21); all 19 Table-10 hash prefixes re-checked against `SHA256SUMS_PREREG.txt` and against the files: 19 OK (the `PREREG_WIDE_01.md` line hashes the shipped relabelled copy, 7ce4e8e66d372788, as Table 10 says; the registered original c185f407aec8c11e is not shipped) |
| README / replay | `README.md` (layout, replay command `python run.py work/<folder>/<script>.py`, paper map, reruns, "Not in this zip"), `DATA_MANIFEST.md`, `VOTKP_v2_9_Paper_Map_and_Inventory.xlsx`, `run.py` |
| Requirements | `requirements.txt`: Python 3.11.15, numpy 2.4.4, scipy 1.17.1, sympy 1.14.0, mpmath 1.3.0, scikit-learn 1.8.0, matplotlib 3.10.9, PyYAML 6.0.3, colour-science 0.4.7, mendeleev 1.3.0, database_knotinfo 2026.9.1, snappy 3.3.2, spherogram 2.4.1, pandas 3.0.2, Pillow, pynucastro 3.1.0, opencv, plus linetools (only num01_parse), nucleardatapy and tables (only nuc01) |
| Lean | `lean/votkp-lean`: 32 `.lean` files, 50 files in all; not built (see section 6) |
| Figures | 34 PNG in `figures/` (not checked) |

Of the 214 `.py` files: **167 were run** (replay set), **4 more** independent-check scripts were run, **2 more** runs were made with the documented environment switches (`RHYTHM_AS_RUN=1`, `TF_INTERP=pchip`), and **43 were not run** by choice or necessity (30 figure scripts, 2 paper-build tools `build.py` and `fix_v05.py`, the launcher `run.py` used only as the pattern for how scripts are launched, the harness `work/v12/checks/rerun_all.py`, 2 Lean helper scripts, 7 independent-check scripts whose input directories are absent). 167 + 4 + 43 = 214.

## 2. Environment and method

Python 3.13.18 (package asks for 3.11.15). numpy 2.5.3, scipy 1.18.1, pandas 3.0.5, scikit-learn 1.9.1, matplotlib 3.11.2, mpmath 1.3.0, sympy 1.14.0 (sympy was missing and was installed), PyYAML 6.0.3, Pillow 12.3.0. Installed with `pip install --break-system-packages` because scripts import them: mendeleev 1.3.0, colour-science 0.4.7, database_knotinfo 2026.9.1, pynucastro 3.1.0, all at the pinned versions of `requirements.txt` (with their pure-Python dependencies). The numpy, scipy, pandas, scikit-learn and matplotlib versions are newer than the pins. snappy, spherogram, nucleardatapy and linetools are not installed and were not improvised.

Each script was run as `README` says (`run.py` semantics): working directory = its own folder, `VOTKP_ROOT=<tree>/work`, `MPLBACKEND=Agg`, `timeout 600`. Arguments only where the package gives them (`stagger_jj_02*.py` with the threshold archive; `check_reverse_peel.py` with the NIST CSV). Two workers in parallel. No script hit the 600 s limit (slowest: `tf_mmr.py` 322 s, `time01c.py` 261 s, `wall01.py` 153 s). Comparison: exact text diff against the stored output; if different, after dropping warning lines and `[Ns]` timing stamps; if only numbers differ, digit agreement of every differing number; where a script has no stored output of its own, against the sibling stored copy (`work/v06/checks/c2_film_output.txt`, `c3_general_output.txt`) or the v0.8 audit log of the same script, or the regenerated data file compared byte by byte against the stored copy. Paper numbers were read from the Appendix D ledger in `NOTES_13` and the body numbers in `NOTES_11` and `NOTES_12`.

## 3. Counts

| | Scripts |
|---|---|
| Found (`.py` in package) | 214 |
| Replay set attempted | 167 |
| Ran to completion (exit 0) | 136 |
| Matched stored output exactly (text or byte-identical regenerated data file) | 102 |
| Matched except floating-point tails or numpy-2 repr only | 13 |
| Differ from stored output | 4 (blockB default, time01c, time01d_above, tf_mmr) |
| Ran, no stored output to compare (libraries, loaders, or paper-number check only) | 17 |
| Not runnable here | 31 |
| Extra: independent-check scripts run | 4 (all 4 match: `stagger_check`, `peaks_check` from `independent_checks/stagger_reproduction`, `continuum_glueball_comparison`, `fig8_fast_verify` from `audit_logs`) |

Every registered test in the task list that can run offline reproduced the paper number (section 5 lists the four scripts whose rerun text differs; none of them changes a registered ledger verdict).

## 4. One row per script

Path is relative to the package root. Column "Matched stored output" says what the rerun was compared with. Column "Paper number" says what was checked against the ledger or body (MATCH) or leaves "-" where the script has no number in the notes.

| Script | Ran | Matched stored output | Paper number | Did not run: why |
|---|---|---|---|---|
| `stagger/stagger_jj_02.py` | yes (33s) | identical | MATCH: p 264/316, d 110/158, f 0/36 KILLED, peaks 1827/2036, null 99.9th pct 1145 |  |
| `supplement_20_3_7/verify_and_extend.py` | no | - | - | not runnable: missing data file supplement_20_3_7/original_atlas/element_atlas.json (the original element_atlas.json; README also says it is in no package) |
| `supporting_records/atlas_cauchy_reading/cauchy_controls.py` | yes (0s) | identical (regenerated data file byte-identical: control_results.json) | - |  |
| `supporting_records/penrose_comparison/comparison_checks.py` | yes (0s) | no stored output | stdout equals stored comparison_checks.json; no ledger number |  |
| `v22/check_reverse_peel.py` | yes (1s) | v22/reverse_peel_results.json: all values equal except round-off (<=1e-12 relative) and max_metric_error 1.2941e-10 now vs 1.0858e-10 stored | MATCH: 5725/5725 checks pass |  |
| `work/adm/apoly_L1.py` | yes (0s) | identical | MATCH A(1,M) numerators 3_1, 4_1, 5_2 (A-poly at L=1 row) |  |
| `work/adm/certify_pair.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/adm/eta01.py` | yes (1s) | identical | no ledger number found |  |
| `work/adm/jump01.py` | yes (0s) | identical | companion of jump02; no separate ledger number |  |
| `stagger/stagger_jj_02f.py` | yes (51s) | identical | MATCH: f killed under both alternative orders (0 and 1 hits of 36) |  |
| `work/adm/sig01_02.py` | yes (1s) | identical | MATCH SIG-01: 1 of 2,525 separated (13a_3542 / 13a_4018); 12,965 parsed |  |
| `work/adm/time01_census.py` | yes (0s) | identical | 85 separated by signature function; 30 pure flips (no ledger number) |  |
| `work/adm/time01_checks.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/adm/verify_sig_all.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/adm/verify_sig_chirality.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/adm/verify_sig_pair.py` | yes (0s) | identical | MATCH independent certified pair 13a_3542 / mirror 13a_4018 (exact arithmetic) |  |
| `work/adm/jump02.py` | yes (131s) | identical | MATCH parity: 16,656 simple roots change by +-2 |  |
| `work/cat/cat01_hom13.py` | yes (1s) | identical | MATCH HOMFLY-different 0 through 12, 19 at 13; CAT-01 233 of 253 unseparated (253 - 20) |  |
| `work/cat/cat01_mechanism.py` | yes (1s) | identical | MATCH 231 of 231 thin same-signature pairs (<=12) not Kh-separated |  |
| `work/cat/cat01_partition.py` | yes (1s) | identical (regenerated data file byte-identical: cat01_partition.json) | - |  |
| `work/cat/hom13_detail.py` | yes (1s) | identical | MATCH thin same-signature pairs not separated by Kh/HFK (231 and 1735) |  |
| `work/adm/wall01.py` | yes (152s) | identical | MATCH WALL-01 0 of 17,360; A(1,M) three knots, extra u=-1 |  |
| `work/cat/verify_hom13.py` | yes (9s) | identical | MATCH 0 of 12,965 inconsistent |  |
| `work/close/c1_depth.py` | yes (5s) | identical | MATCH K=6 12/18, K=10 18/18, Hf and Ta only at K=11-12 |  |
| `work/close/c2_film.py` | yes (3s) | identical | MATCH first-order bump height error max 0.6%, 12/12 (Au 450: 0.01855) |  |
| `work/close/c3_general.py` | yes (3s) | identical | MATCH 171 cases, frozen rule 0.871, 171/171 first-order, worst height 3.1%, best threshold 0.994 |  |
| `work/close/c4_ladder12.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/close/certify_ladder.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/close/certify_ladder_selftest.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/close/colored_jones.py` | yes (0s) | no stored output | - |  |
| `work/close/exact_cjones.py` | yes (1s) | no stored output | - |  |
| `work/close/exact_validate.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/close/homfly.py` | yes (0s) | no stored output | - |  |
| `work/elemental/chk_ie.py` | yes (18s) | identical | MATCH NIST ionization values equal the paper claims |  |
| `work/elemental/chk_linked.py` | yes (19s) | no stored output | - |  |
| `work/elemental/chk_math.py` | yes (1s) | agrees except float tails | - |  |
| `work/elemental/chk_optics.py` | yes (0s) | identical | - |  |
| `work/elemental/chk_step3.py` | yes (8s) | agrees except float tails | - |  |
| `work/cat/load_ki.py` | yes (112s) | identical (regenerated data file byte-identical: ki13.pkl) | - |  |
| `work/elemental/onion_atlas_01b.py` | yes (34s) | identical | MATCH T1 0.515/0.738/0.951 at K=3/6/10 vs S2 0.397/0.415/0.492 |  |
| `work/elemental/onion_atlas_01c.py` | yes (22s) | identical | - |  |
| `work/elemental/onion_atlas_01.py` | yes (66s) | identical (regenerated data file byte-identical: onion_atlas_01_results.csv + element_records.json) | group K=10 T1@S3set 0.906 row; full table = onion_atlas_01_results.csv (byte-identical) |  |
| `work/gap_review/audit_v10_g02.py` | no | - | - | not runnable: hard-coded path /workspace/scratch/f3000538ab1c/audit_v10 (the v1.0 package) not present |
| `work/gap_review/v10_flux_loop_toy.py` | yes (0s) | v10_flux_loop_toy.json: Monte Carlo means agree to 15-16 digits | - |  |
| `work/gap_review/v10_gap_research.py` | yes (0s) | identical (regenerated data file byte-identical: v10_gap_research.json) | stored json regenerated byte-identical; no ledger number |  |
| `work/gap_review/v10_sheet_bridge.py` | yes (0s) | identical (regenerated data file byte-identical: v10_sheet_bridge.json) | - |  |
| `work/nuc/nuc01.py` | no | - | - | not runnable: needs python package nucleardatapy (and its FRDM2012 HDF5 data via pytables): not installed, needs a network download |
| `work/numer/num01_parse.py` | yes (0s) | identical (regenerated data file byte-identical: ground_lines.json (96,003 bytes)) | - |  |
| `work/numer/num01_run.py` | yes (21s) | num01_table.json: S, Sraw agree to 15-16 digits | MATCH NUM-01 N 0.392 vs D 0.267 |  |
| `work/particles/chk_gpt_0923.py` | no | - | - | not runnable: hard-coded path /home/claude/elemental/element_records.json not present (the file is in the package at work/elemental/element_records.json, but the script was not altered) |
| `work/particles/h01_lorentz_separator.py` | yes (0s) | identical | MATCH H-01 w leave-one-metal-out 0.743 vs /Gamma/ 0.977 |  |
| `work/particles/h01b_midpoint.py` | yes (0s) | identical | MATCH 0.743 vs 0.959 |  |
| `work/particles/p01_p02.py` | yes (0s) | identical | MATCH P-01 2.37 sigma uncorrected, 3.14 corrected; P-02 H- 2.892, D- 2.892, Ps- 3.036 |  |
| `work/elemental/onion_atlas_02.py` | yes (30s) | identical (regenerated data file byte-identical: onion_atlas_02_results.csv) | - |  |
| `work/rhythm/blockA.py` | yes (50s) | agrees except float tails (4 numbers, worst pair -0.19473608058786568 vs -0.19473608058786607, 14 digits) | MATCH T01 0.846, T02 1.90, T03 7.5%, T04 2.28, T05 Fr 0.553 / Ra 0.989 eV (gaps 1.554, 2.143), T06 0.004 vs 0.477, T07 0.00/1.00, T08 0.657-0.909 mean 0.813, T09 1.160, T10 0.198 vs -0.011 |  |
| `work/rhythm/blockB.py` | yes (49s) | DIFFERS | MATCH (default = corrected loader): T11 0.709 vs 0.970 KILL, T12 0.414/0.231, T13 0.164/0.087 and 0.220/0.104, T14 1.31, T15 0.0855/0.0993, T16 4/7, T17 0.854/0.713, T18 0.125/0.157/0.052, T19 3/5, T20 1/4. Default output equals blockB_corrected_output.txt; RHYTHM_AS_RUN=1 reproduces stored blockB_output.txt (3.068 vs 0.985) byte for byte |  |
| `work/rhythm/posthoc2.py` | yes (45s) | identical | post-hoc; byte-identical |  |
| `work/rhythm/posthoc.py` | yes (48s) | identical | post-hoc T-rows; byte-identical |  |
| `work/rhythm/rhythm_explore.py` | yes (25s) | identical | exploration; byte-identical |  |
| `work/rhythm/rdata.py` | yes (48s) | no stored output | - |  |
| `work/rhythm/spacing_candidates.py` | yes (18s) | identical | byte-identical |  |
| `work/rhythm/sensitivity.py` | yes (52s) | identical | sensitivity of T11 handlings; byte-identical (two other handlings 5.03/0.985 and 1.109/1.052 are in this output) |  |
| `work/russell/posthoc_groupmean.py` | yes (48s) | identical | MATCH 25.9 vs 43.8 |  |
| `work/russell/posthoc_hydrogen.py` | yes (50s) | identical | byte-identical; ratio 1.62 |  |
| `work/russell/posthoc_record.py` | yes (49s) | identical | MATCH 18 of 24 all grades |  |
| `work/russell/posthoc_scale.py` | yes (49s) | identical | MATCH row-swing CV 0.031 |  |
| `work/russell/posthoc_split.py` | yes (47s) | identical | post-hoc splits; no separate ledger number beyond T3/T7 |  |
| `work/russell/wave.py` | yes (48s) | identical | MATCH T1 5/5, T2 0/5, T3 61.4/47.5, T4 130.4/58.9, T5 521->208 and 505->865 (printed 504.6->732.2->864.6), T6, T7 275.2/193.7, T8 3 of 4 |  |
| `work/snell/run_snell.py` | yes (10s) | identical | MATCH turning set 1 hit vs 6, confusion 0/6 |  |
| `work/snell/s3_and_null.py` | yes (0s) | identical | MATCH Spearman 0.613 / 0.680 (paper 0.61-0.68); threshold errors 0 vs 4 |  |
| `work/snell/slater_geom.py` | yes (0s) | no stored output | - |  |
| `work/tests/colored_jones.py` | yes (0s) | no stored output | - |  |
| `work/tests/homfly.py` | yes (0s) | no stored output | - |  |
| `work/tests/j4_sparse.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/russell/wave2.py` | yes (48s) | identical | MATCH S1 CV 0.163, S2 0.475, S3 25.9 vs 27.5 PASS |  |
| `work/tests/scan_11_12.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/tests/scan_part.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/tests/ta_adjoint.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/tests/ta_census.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/tests/ta_controls.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/tests/run03.py` | yes (32s) | identical (regenerated data file byte-identical: run03_results.csv) | MATCH Run 03 static wins radii (0/9), hardness 1/9, EA 4/9, noble IE1 6/6, covalent radius 4/6; K=10 group 0.952 |  |
| `work/tests/tf_mmr2.py` | yes (0s) | agrees except float tails | MATCH P_1 coefficients integers (0,-1,2,-2,2,-1,0), 4_1 zero |  |
| `work/tests/th_ridge60.py` | yes (0s) | identical | MATCH ridge census (54 vanishes, 18 and 36 shrink, 28 grows) |  |
| `work/tests/tj_blind11.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/tests/tj_cross.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/tests/tj_merge12.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/tests/tk2_holdout.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/tests/tk_holdout.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/tests/tl_robust.py` | yes (8s) | identical | MATCH 35/36 |  |
| `work/tests/tn_phase.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/time01/longitude.py` | yes (0s) | no stored output | - |  |
| `work/time01/reps.py` | yes (0s) | no stored output | - |  |
| `work/time01/time01a.py` | yes (56s) | identical | MATCH TIME-01a 135/135 (47+45+43) |  |
| `work/time01/time01b.py` | yes (4s) | identical | MATCH Chern 1.000000; real time 0.9990 (0.99895) |  |
| `work/time01/time01b_digits.py` | yes (4s) | identical | MATCH 0.99895421 |  |
| `work/time01/time01b_refine.py` | yes (22s) | identical | MATCH midpoint sampling 1.00016, 1.00014 (paper 1.00014-1.00016) |  |
| `work/tests/tf_mmr.py` | yes (322s) | DIFFERS | numerical-fit predecessor of tf_mmr2; not a paper number |  |
| `work/time01/time01c.py` | yes (261s) | DIFFERS | MISMATCH outside the registered window (see mismatches); inside window MATCH 1 per knot, 3 near the upper wall |  |
| `work/time01/time01c_walls.py` | yes (2s) | identical | MATCH window alpha 0.10971-0.11522 |  |
| `work/time01/time01c_confirm.py` | yes (70s) | identical | confirmation of window counts |  |
| `work/time01/time01d_above.py` | yes (20s) | DIFFERS | MISMATCH N above upper wall (see mismatches) |  |
| `work/time01/time01d_check.py` | yes (14s) | agrees except float tails (8 numbers, worst pair 3.2e-16 vs 1.4e-15, 0 digits) | 1e-16 tails only |  |
| `work/time01/time01d_mirror.py` | yes (16s) | identical | mirror check, byte-identical |  |
| `work/time01/time01d.py` | yes (82s) | agrees except float tails (18 numbers, worst pair 6.5e-16 vs 4.5e-16, 0 digits) | values equal to 3 digits; 1e-16 commutator tails differ |  |
| `work/v06/checks/audit_exact.py` | yes (0s) | identical | MATCH identity 9.09e-13 over 15610 cases; 171/171 criterion in film_baseline |  |
| `work/time01/time01e_refine.py` | yes (13s) | agrees except float tails (2 numbers, worst pair 1.14e-58 vs 6.43e-59, 0 digits) | MATCH theta/2pi -0.0145346 and -0.0171689 at alpha 0.11247 |  |
| `work/v06/checks/data01_depthlaw.py` | yes (12s) | identical | MATCH depth law holds K<=10 (central values 1.000) |  |
| `work/v06/checks/facts_lookup.py` | yes (1s) | identical | facts check; no ledger number |  |
| `work/v06/checks/film_baseline.py` | yes (0s) | identical | MATCH labels agree 171, 0.994 at 0.9175, held-out thresholds 0.977/0.959 |  |
| `work/v06/checks/film_crossings.py` | yes (0s) | identical | Au 450 crossings, max excess 1.85e-2 (paper rise 0.0185) |  |
| `work/v06/checks/film_oblique.py` | yes (0s) | identical | MATCH 5.66e-16 (paper 6e-16) |  |
| `work/v06/checks/run01_infold.py` | yes (13s) | identical | MATCH Run 01 K=10: T1 0.951 vs static 0.508 (K=3 0.515/0.412, K=6 0.738/0.415) |  |
| `work/v06/checks/run01_infold_ci.py` | yes (3s) | identical | - |  |
| `work/v06/checks/run01_robust_infold.py` | yes (38s) | identical | MATCH 35 of 36 variants |  |
| `work/v06/checks/time01b_digits.py` | yes (5s) | identical | - |  |
| `work/v07/checks/bump_location.py` | yes (0s) | identical | byte-identical |  |
| `work/v06/checks/data01.py` | yes (77s) | identical | MATCH DATA-01 period 6 K=10 median 17/18, 5th pct 0.833 (15/18), 18/18 in 14%; Run 01 K=10 median 0.918; E-only arm: no test element beyond K=5/6 |  |
| `work/v07/checks/thin01.py` | yes (0s) | identical | MATCH P1 11/15, median 0.0104; P2 1.3x (0.0138); 10-20 nm 6/6 median 0.0137 |  |
| `work/v07/checks/metamer_check.py` | yes (1s) | agrees except float tails (1 numbers, worst pair 1.9e-16 vs 2.0e-16, 1 digits) | MATCH dE76 8.60, dE2000 8.27, sigma_max 5.38e-3, paper pair 43.0%, flat-baseline 18.35 vs 5.32, neutral 2e-16 |  |
| `work/v07/checks/thin01_complete.py` | yes (1s) | identical | MATCH rise at 450 nm in 15/15 datasets, 550 rises 1.8e-4 and 1.65e-5, metamer 7.41-9.15, Werner 2.98; 35 nm same side 5/6 |  |
| `work/v07/checks/thin01_descriptive.py` | yes (1s) | identical | MATCH post-hoc relative error 12.0% (<10 nm) vs 1.6% (>=20 nm) |  |
| `work/v08/checks/r7.py` | yes (45s) | identical | MATCH: Fr not tabulated; Ra -26.9% vs tolerance 35.9%; NOT TESTABLE |  |
| `work/v10/checks/certify_ladder.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/v10/checks/certify_ladder_selftest.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/v08/checks/split_theorem_check.py` | yes (46s) | identical | MATCH: 5714 steps, 4.1e-16; walls 3/5 ... 13/85 |  |
| `work/v10/checks/data01_models.py` | yes (9s) | identical | MATCH post-hoc models Gaussian 17/15, uniform 17/16, shared 18/17 (18/18 in 12.0% in this own-stream run vs 14% in registered data01.py) |  |
| `work/v10/checks/exact_cjones.py` | yes (0s) | no stored output | library |  |
| `work/v10/checks/exact_validate.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/v10/checks/column_residual_vs_Z2.py` | yes (30s) | identical | MATCH corr 0.03 (22 elements), 0.58 (10 elements) |  |
| `work/v10/checks/level_tracks_line.py` | yes (1s) | identical | MATCH corr 0.902; 0.228 vs 0.282, 0.267 |  |
| `work/v10/checks/mass_gaps_smith.py` | yes (1s) | identical | MATCH /Gamma/ 1.074, 1.220, 1.025 |  |
| `work/v10/checks/proof_checks_3_1_and_5_6.py` | yes (2s) | identical | MATCH: 200/200; 2000/2000; 0/2000 with three poles between probes |  |
| `work/v10/checks/insertion_rule.py` | yes (61s) | identical | MATCH sign agrees in 20 of 22 |  |
| `work/v10/checks/row_loro.py` | yes (48s) | identical | MATCH heights 521.3...208.0; max leave-one-row-out error 6.5% (others 18.5-50.3%) |  |
| `work/v10/checks/slight_changes.py` | yes (0s) | identical | MATCH within rounding: constant -37% / +21.8%, power +25.1%; per-loop +8.0% and +9.4% (corrected), +9.1% and +10.3% (uncorrected) |  |
| `work/v10/checks/russell_volume_readings.py` | yes (16s) | identical | MATCH fourth tone smallest in 0 of 5 rows (both radii) |  |
| `work/v11/checks/g02_run.py` | yes (0s) | identical | MATCH G-02 J++ 9.36% / 10.40%; 0++ tower 24.23% / 25.88%; 6 of 19 base rate is in g02_why/other file |  |
| `work/v11/checks/g02_why.py` | yes (0s) | identical | - |  |
| `work/v11/checks/loop_basis.py` | yes (0s) | identical | MATCH affine map misses n=3 by 10/9 |  |
| `work/v11/checks/rows_janaf.py` | yes (0s) | identical | MATCH -0.210% and -0.099%; predicted +0.07% and -1.05% |  |
| `work/v11/checks/thin_end.py` | yes (4s) | identical | MATCH exact to order d (0); 1 nm errors scale as d^2 |  |
| `work/v12/checks/gold_film_450.py` | yes (0s) | identical | MATCH R 0.408191 (200 nm), 0.426742 (58.21 nm), 0.163082 (10 nm), rise 0.018551 |  |
| `work/v10/checks/split_explained.py` | yes (53s) | identical | MATCH R2 0.705 / 0.593, out-of-sample 0.522 |  |
| `work/v20/scripts/f_wall_01.py` | yes (48s) | identical | MATCH 0 of 6 inside the p-d interval (6 of 6 outside); all 12 row-6 4f-wall dZeff negative |  |
| `work/v20/scripts/item4_rerun_01.py` | yes (21s) | no stored output | MATCH alpha fit ln a = 10.284 - 3.036 ln IE1, R2 0.9055 (paper 0.906, -3.04) |  |
| `work/v20/scripts/five_eighths_01.py` | yes (51s) | no stored output | MATCH FIVE-EIGHTHS-01 exponent 4.302 (Z 10-40), 4.328 (40-86); He 0.001 eV, Li -0.004 eV |  |
| `work/v20/scripts/run03_ea2026.py` | yes (34s) | identical | MATCH EA 4/9 unchanged; hardness static-better 6 -> 5 |  |
| `work/v20/scripts/wall_residue_01.py` | yes (49s) | no stored output | MATCH Spearman -1.000 rows 2-6; CV 3.6, 10.4, 106.2, 73.9, 96.5% (form 2 killed) |  |
| `work/v21/scripts/tf_constant.py` | yes (0s) | identical | MATCH q 5.22113, a_TF 1.2875 eV, classical-ion limit 1.0157 |  |
| `work/v21/scripts/step_23_01.py` | yes (50s) | identical | MATCH STEP-23-01 median 1.051, 1,225 steps, quartiles 0.928-1.409, passed |  |
| `work/v21/scripts/tf_ladder.py` | yes (13s) | identical | MATCH bare law 6.26...2.94 (2.74-2.94 at m=4-20), TF ion 1.62-2.35, median NIST/TF 3.941 at m=1 |  |
| `work/v21/scripts/tf_resid_01.py` | yes (3s) | identical | MATCH TF-RESID-01 0.951 vs 0.951 passed; envelope 0.000; level minus envelope 0.529, 0.646, 0.721; TF_INTERP=pchip also byte-identical to stored |  |
| `work/votkp/chk_fig8.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/votkp/chk_geom.py` | no | - | - | not runnable: needs python package snappy (SnapPy stack, not installed; not improvised) |
| `work/votkp/chk_homfly.py` | yes (0s) | identical | MATCH engine vs KnotInfo HOMFLY; skein residuals 1e-16 |  |
| `work/votkp/chk_pairs.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/votkp/chk_ratmap.py` | yes (0s) | identical | - |  |
| `work/votkp/dbg.py` | yes (0s) | no stored output | - |  |
| `work/votkp/exact_links.py` | yes (0s) | identical | - |  |
| `work/votkp/exact_poly.py` | yes (2s) | identical | - |  |
| `work/votkp/homfly.py` | yes (0s) | no stored output | - |  |
| `work/votkp/scan10.py` | no | - | - | not runnable: needs python package spherogram (SnapPy stack, not installed; not improvised) |
| `work/wide/fblock.py` | yes (0s) | identical | MATCH f-block 2/14 and 3/14 |  |
| `work/wide/matter_wave.py` | yes (0s) | agrees except float tails | MATCH 3.51e-16 (paper 3.5e-16); first-order predictor 400/400 (390/400 show an echo) |  |
| `work/wide/nuc_onion.py` | yes (1s) | same values; numpy-2 repr np.float64(..) only | MATCH magic ridges 6/6 measured, 5/6 with extrapolated; values equal, only numpy-2 repr np.float64(..) |  |
| `work/wide/nuc_posthoc.py` | yes (1s) | same values; numpy-2 repr np.float64(..) only | values equal to audit log, only numpy-2 repr differs; coverage statement is post-hoc |  |
| `work/v21/scripts/tf_inshell.py` | yes (47s) | identical | MATCH medians 1.039 (Z 50-69), 1.088 (Z 70-86) |  |

Extra runs outside the 167-row set:

| Script | Ran | Matched stored output | Paper number |
|---|---|---|---|
| `work/rhythm/blockB.py` with `RHYTHM_AS_RUN=1` | yes | identical to `blockB_output.txt` (byte for byte) | MATCH as-run T11 3.068 vs 0.985 (PASS as run) |
| `work/v21/scripts/tf_resid_01.py` with `TF_INTERP=pchip` | yes | identical to `tf_resid_01_pchip_output.txt` | robustness rerun |
| `independent_checks/stagger_reproduction/stagger_check.py` (CSV, R0) | yes | JSON identical to `out_R0.json` | MATCH independent p 260/316, d 110/154, f 0/36 |
| `independent_checks/stagger_reproduction/peaks_check.py` | yes | no stored file in that folder | MATCH 1791 of 1960, null 99.9th pct 1274 |
| `independent_checks/v08_audit/audit_logs/continuum_glueball_comparison.py` | yes | identical to `continuum_glueball_comparison.txt` | P-01 ratios 1.3028 / 1.2746 vs 1.4373 |
| `independent_checks/v08_audit/audit_logs/fig8_fast_verify.py` | yes | identical to `fig8_fast_verify.txt` | Volume 2.029883212819307 |

Skipped without running (43): 30 figure scripts (`fig_*`, `figs_*`, `v2_figs_01`; pure drawing), paper-build tooling `work/paper2/build.py` and `work/v05/fix_v05.py`, `work/v12/checks/rerun_all.py` (harness that reruns 19 scripts already run here, including the not-runnable `nuc01`), `run.py` (launcher), `lean/votkp-lean/scripts/verify.py` and `verify_energy_data.py` (need the Lean toolchain), and 7 independent-check scripts: `relocation_harness/v10_reloc_v10.py` and `v11_reloc_v11.py` (need `work/v10/pkg/...` and `work/v11/pkg/...`, the old v1.0/v1.1 packages), `v08_audit/audit_runner.py`, `audit_sweep.py`, `independent_verify.py`, `build_evidence.py` (need the v0.8 package under `audit_v08/` and `audit_run/`, `deliverables/`), `audit_logs/integrity_verify.py` (needs `upload/VOTKP_Elemental_Peeling_Paper_v0_8_Package*`). Exact missing path in each is in the `.err` files under `rerun/independent_checks__*`.

## 5. Mismatches (both values)

Four reruns differ from the stored output text (items 1 to 4); a further group differs only at rounding level (list after item 4). None of these changes a registered ledger verdict.

1. **`work/time01/time01c.py`** (13-crossing representation count outside the window). Stored `time01c_output.txt` vs rerun, counts N of representations at grid points outside the window alpha in (0.10971, 0.11522). Knot 13a_3542: alpha 0.18: 29 stored, 30 rerun; 0.26: 61 vs 65; 0.30: 46 vs 47; 0.34: 18 vs 19. Knot 13a_4018: 0.12: 3 vs 4; 0.14: 10 vs 9; 0.22: 62 vs 60; 0.26: 66 vs 64; 0.30: 47 vs 46; 0.34: 18 vs 16. Lines for the inside of the window are identical (one per knot, three at alpha 0.11472), which are the numbers the ledger row "TIME-01c 13-crossing window" states; the ledger itself says "counts above the window incomplete". The script has no random seed (numerical root finding), so the difference is most likely library-version dependence of the root finder; untested which.
2. **`work/time01/time01d_above.py`** (above the upper wall 0.11522). Stored: 13a_3542 alpha=0.11552 N=4, theta/turn = [-0.027685, 0.001108, 0.352938, 0.445428]; 13a_4018 alpha=0.11527 N=4, theta/turn = [-0.35203, -0.273039, -0.034787, 0.000124]. Rerun: N=3 for both, the near-zero entries 0.001108 and 0.000124 absent, the other values identical to 6 digits. A near-zero longitude is dropped or kept at a threshold. Not a registered row (post-hoc, outside the window).
3. **`work/tests/tf_mmr.py`** (numerical fit of the P_1 coefficients of the trefoil, predecessor of the exact `tf_mmr2.py`). Stored (v0.8 audit log; the package has only development logs `tf*.log`) 3_1 coefficients t^-3..t^3: 48.0882-3.8962j, -243.5184+129.9578j, 415.3007-523.8546j, ...; rerun 48.093-3.9023j, -243.5285+130.0012j, 415.2784-523.9618j, ...; agreement 3 to 4 digits; max fit residual 3.83e-03 in both. This is an ill-conditioned fit; the paper number (P_1 integers 0,-1,2,-2,2,-1,0) comes from `tf_mmr2.py`, which reproduces to 1e-13 residual (4.69e-13 stored, 4.68e-13 rerun).
4. **`work/rhythm/blockB.py`** (default run). Stored `blockB_output.txt`: T11 n=49, level 3.068, peel shape 0.985, PASS; T20 resistivity n=49. Rerun default: T11 n=44, level 0.709, peel shape 0.970, KILL; T20 n=44. This is the documented design: the default loader is the corrected one, the rerun equals `blockB_corrected_output.txt` exactly and equals the ledger (0.709 vs 0.970, killed); `RHYTHM_AS_RUN=1` reproduces the stored as-run file byte for byte (extra run above). Listed for completeness, not an error.

Rounding-level differences (all agree to the printed precision of the paper):

- `work/rhythm/blockA.py`: Au column-law residual -0.19473608058786607 stored, -0.19473608058786568 rerun (14 digits; 4 numbers differ in the last digits).
- `work/time01/time01d.py`, `time01d_check.py`: commutator tails such as 6.5e-16 vs 4.5e-16, 3.2e-16 vs 1.4e-15; `time01e_refine.py`: certified residual 1.14e-58 stored vs 6.43e-59 rerun (the theta values -0.0145345761398439... agree in all printed digits).
- `work/v07/checks/metamer_check.py`: neutral-filter / identity residual 1.9e-16 vs 2.0e-16.
- `work/elemental/chk_math.py`: 4.80e-16 vs 4.82e-16 and -3.75e-16 vs -3.44e-16; `chk_step3.py`: 1.01e-16 vs 9.82e-17 and 5.05e-17 vs 4.91e-17; `work/wide/matter_wave.py`: worst |diff| 4.72e-16 in the v0.8 audit log vs 3.51e-16 rerun (the paper prints 3.5e-16, which matches the rerun; the stored package has no output file for this script).
- `v22/check_reverse_peel.py` results JSON: `max_metric_error` 1.0858286492165803e-10 stored vs 1.2941286930967522e-10 rerun. The package README already records this exact pair (1.09e-10 vs 1.29e-10, tolerance 1e-8). Other differences in that JSON are at 1e-12 relative or below (`bath_ODE` relative_error 0.004067049732868442 vs 0.004067049732867741).
- `work/gap_review/v10_flux_loop_toy.json`, `work/numer/num01_table.json`: 15 to 16 digits.
- `work/wide/nuc_onion.py`, `nuc_posthoc.py`: values identical, only the numpy-2 representation `np.float64(0.24)` for `0.23999999999999999`.

## 6. What was not run, stated plainly

**Not runnable here (31 scripts).** 27 need snappy and/or spherogram, which are not installed (not improvised): `work/adm/certify_pair.py`, `work/adm/time01_checks.py`, `work/adm/verify_sig_all.py`, `work/adm/verify_sig_chirality.py`, `work/close/c4_ladder12.py`, `work/close/certify_ladder.py`, `work/close/certify_ladder_selftest.py`, `work/close/exact_validate.py`, `work/tests/j4_sparse.py`, `work/tests/scan_11_12.py`, `work/tests/scan_part.py`, `work/tests/ta_adjoint.py`, `work/tests/ta_census.py`, `work/tests/ta_controls.py`, `work/tests/tj_blind11.py`, `work/tests/tj_cross.py`, `work/tests/tj_merge12.py`, `work/tests/tk2_holdout.py`, `work/tests/tk_holdout.py`, `work/tests/tn_phase.py`, `work/v10/checks/certify_ladder.py`, `work/v10/checks/certify_ladder_selftest.py`, `work/v10/checks/exact_validate.py`, `work/votkp/chk_fig8.py`, `work/votkp/chk_geom.py`, `work/votkp/chk_pairs.py`, `work/votkp/scan10.py`. These cover the registered knot-side tests that need SnapPy: the colour-3 certificate (`certify_ladder`, `exact_validate`, `certify_ladder_selftest`), the held-out 11/12-crossing volume test (`tk_holdout`, `tk2_holdout`, `scan_11_12`, `scan_part`, `tj_*`), the adjoint Jones five pairs (`ta_*`), the phase 8pi/15 scan (`tn_phase`), the signature-function verifiers that need spherogram (`verify_sig_all`, `verify_sig_chirality`, `certify_pair`, `time01_checks`), and `scan10`, `chk_geom`, `chk_fig8`, `chk_pairs`. For these the stored outputs were only read, not reproduced. Where the paper number could be recomputed from a stored result file it was: the held-out 11-crossing and 12-crossing mean relative errors recomputed from `tk_holdout.json` (60 knots) and `tk2_holdout.json` (40 knots) are 2.847% and 2.942% (paper 2.85% and 2.94%); `certify_ladder_output.txt` lists 21 pairs all with "J4 differs: True" (paper 21 of 21); `tn.log` ends `RESULT theta 1.6755 Spearman 0.9922`.

- `supplement_20_3_7/verify_and_extend.py`: missing data file supplement_20_3_7/original_atlas/element_atlas.json (the original element_atlas.json; README also says it is in no package).
- `work/gap_review/audit_v10_g02.py`: hard-coded path /workspace/scratch/f3000538ab1c/audit_v10 (the v1.0 package) not present.
- `work/nuc/nuc01.py`: needs python package nucleardatapy (and its FRDM2012 HDF5 data via pytables): not installed, needs a network download.
- `work/particles/chk_gpt_0923.py`: hard-coded path /home/claude/elemental/element_records.json not present (the file is in the package at work/elemental/element_records.json, but the script was not altered).

Other things not done: the Lean library was not built (no Lean/lake toolchain; `lean/votkp-lean/scripts/verify.py`, the 140 theorems, 15 false controls, axioms list and the GitHub Actions run are untested here); figures 1 to 34 were not regenerated or viewed; the README claim that eleven scripts reproduced byte for byte includes SnapPy scripts that could not be rerun here; `work/v12/checks/rerun_all.py` was not run as a harness (its 19 scripts were run individually, except `nuc01`); `work/numer/num01_parse.py` ran on the packaged Morton tables (`work/numer/src`) and regenerated `ground_lines.json` byte-identical (96,003 bytes), but the claim that these came from linetools 0.3.2 was not tested; the two external datasets (Swedish National Data Service xenon scans `seqxx.csv`, `seqxxe.csv`) and OpenAI `openai/math` files are not in the package and nothing depending on them was checked; the PDF/HTML paper was not compared with the notes beyond the numbers listed.

## 7. Paper numbers for which no script was found (or only a stored record)

- **A-polynomial of 4_1: integral vs volume, 4e-16; pi.m(A) of 5_2, 1e-10.** Recorded in `work/tests/TEST_LOG.md` (Result T-E: 2.0298832128193074 vs SnapPy 2.029883212819307, difference 4e-16) but no script in the package computes the integral or the Mahler measure. `fig8_fast_verify.py` reproduces the 4_1 volume 2.029883212819307 (Lobachevsky) only. The 5_2 figure 1e-10: no script or log located.
- **Energy versus Q (Sutcliffe), "monotone".** Literature reading recorded in `TEST_LOG.md` (E = 5.242 ... 7.614 for the trefoil, T(3,4) 7.857, 8.272, 8.761); no script.
- **Colour versus ordinary Jones, 0.982 vs 0.992.** Recorded in `TEST_LOG.md` (T-P; best ordinary-Jones Spearman 0.982 near theta 2.47); the script that produced it is not identified (the SnapPy-dependent `tn_phase.py` / `ta_*` family is the likely home; untested).
- **Phase 8pi/15 "best found"**: `tn_phase.py` needs snappy; stored `tn.log` gives 0.9922 at theta 1.6755; not rerun.
- **Adjoint Jones, five pairs 5/5 separated and ordered**: `ta_adjoint.py` needs spherogram/snappy; stored audit log only.
- **Held-out 11/12 crossings 2.85% / 2.94%**: script needs snappy; recomputed from stored JSON (section 6), not rerun.
- **NUC-01 (0.65 vs 0.83 N_p N_n; level to charge radius 1 of 2)**: `nuc01.py` needs `nucleardatapy`; the stored output `nuc01_output.txt` shows SHAPE 0.649, NPNN 0.831, charge-radius MAE shape 0.0364 / level 0.0344 (lin) and 0.0334 / 0.0370 (knn), i.e. level beats shape in 1 of 2 as the ledger says. Read, not rerun.
- **Ledger rows with no script in the package at all (literature or hand reading):** the Russell-text reading scope; the Du / Couto / Chen literature comparisons; "Nuclear shell evolution (4-point), no measured coverage" is only partly in `nuc_posthoc.py` (its output says "measured-only"); "Snell deep ridges, flat" is in the `run_snell.py` K3 table but no single printed verdict line.
- **Scripts named in the paper but placed differently:** `element_atlas.json` (needed by `verify_and_extend.py`) is absent, as the README says; the paper lists `PREREG_TF_RESID_01.md` and `PREREG_STEP_23_01.md` under v21/scripts but they are in `work/v21/`, and `rdata.py` is in `work/rhythm/` (README says both).

## 8. Registered tests: checklist from the task

| Test | Script run | Result |
|---|---|---|
| Run 02 polarizability 0/9 | `onion_atlas_02` | "K1 main: T1 beats S2 in 0 of 9 settings"; K3 grade 3 of 9; match |
| Run 01 group classification, K=10, 0.951 vs 0.51 | `run01_infold`, `onion_atlas_01b`, `run03`, `tf_resid_01` | 0.951 vs 0.508 in-fold; 0.952 vs 0.500 in `run03`; match |
| DATA-01 | `data01`, `data01_models`, `data01_depthlaw` | median 17/18, 5th pct 15/18, 18/18 in 14% (registered stream); 0.918 run 01; post-hoc models 17/15, 17/16, 18/17; match |
| RHYTHM T01-T20 incl. T05 Fr / Ra | `blockA`, `blockB` | all 20 verdicts and numbers match; Fr miss 0.553 eV, Ra 0.989 eV, gaps 1.554 and 2.143 eV at 119 and 120; match |
| RUSSELL T1-T8, S1-S3 | `wave`, `wave2`, `posthoc_*` | all match (T3 61.4 vs 47.5, T7 275 vs 194, S1 0.163, S2 0.475, S3 25.9 vs 27.5) |
| R7 | `r7` | Fr not tabulated, Ra -26.9% vs tolerance 35.9%; match |
| TF-RESID-01 | `tf_resid_01` | 0.951 vs 0.951 (the script prints ">= raw", the paper notes "as printed"); envelope 0.000; match |
| STEP-23-01 | `step_23_01` | 1.051, 1,225 steps; match |
| FIVE-EIGHTHS-01 | `five_eighths_01` | 4.302 and 4.328; match |
| WALL-RESIDUE-01 | `wall_residue_01` | -1.000 rows 2-6; CV 3.6, 10.4, 106.2, 73.9, 96.5%; match |
| F-WALL-01 | `f_wall_01` | 6 of 6 outside the interval, all 12 row-6 values negative; match |
| split_theorem_check | `split_theorem_check` | 5,714 steps, 4.1e-16 (paper 4e-16); match |
| THIN-01 and film / gold | `thin01`, `thin01_complete`, `thin01_descriptive`, `gold_film_450`, `thin_end`, `c2_film`, `c3_general`, `film_*` | all match (11/15, 0.0104; 1.3x; 6/6; 5/6; gold 0.018551; Theorem 6.3) |
| Snell test | `run_snell`, `s3_and_null` | 1 hit vs 6; 0/6; Spearman 0.613 and 0.680; match |
| Metamer check | `metamer_check` | 8.60 / 8.27, sigma_max 5.38e-3, 43%, 18.35 vs 5.32; match |

