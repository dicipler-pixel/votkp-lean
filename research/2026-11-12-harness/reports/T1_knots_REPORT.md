# knot_v29 report (draft written mid-run; final section appended when the 11/12-crossing rescan finishes)

Installed (pip --break-system-packages): snappy 3.3.2, spherogram 2.4.1 (as snappy dependency), snappy_15_knots 1.2.1, knot_floer_homology 1.2.2, database_knotinfo 2026.9.1 (already present), nucleardatapy 1.0.2, plus `tables` 3.11.1 (listed in the package requirements, needed by nuc01's HDF5 read). All installed; none failed. snappy and spherogram versions equal the package pins. Python 3.13, sklearn 1.9.1 (package pins 3.11 / 1.8.0).
Setup: copy of pristine package in tree/; each script run in its own folder, VOTKP_ROOT=<tree>/work, MPLBACKEND=Agg, timeout 540 (runner.py). Outputs in run/. Stored outputs read from /home/claude/check_v29/pkg. `diff -rq` of pristine vs rerun tree: only one data file changed, work/close/c4_out.json (float noise, below).

## One row per script
"stored" = stored output file in package; timing tags and the plink/tkinter warning stripped before comparing (cmp.py).
| Script | Ran | vs stored | vs paper |
|---|---|---|---|
| adm/certify_pair | yes 1s | identical | 13a_3542 / 13a_4018 mirror: sigma_w -2 vs +2 inside window, 0 outside; matches paper 11.5 |
| adm/time01_checks | yes 2s | identical | HOMFLY chirality checks, 2000/2000 points |
| adm/verify_sig_all | yes 64s | identical | 12965 signature functions, 0 unparsable, 7 braid-sign exceptions of 4226 |
| adm/verify_sig_chirality | yes 2s | identical | consistent |
| close/c4_ladder12 | yes 419s | same structure on all 100 PAIR lines and the 241 distinct blind pairs, 98 volume-different computable, 19 J3-blind, J4-blind 0; numeric tails differ by <=1.2e-10 relative (e.g. 92.15150533156478 stored vs 92.15150533156793; near-zero entries 5.87e-11 vs 2.66e-11); no separated/unseparated flips; only timing differs in RESULT line | colour ladder consistent |
| close/certify_ladder | yes 96s | identical after timing removal (21 pairs, all "J4 differs: True") | paper 21 of 21 |
| close/certify_ladder_selftest | yes 2s | no stored file for this variant (stored file belongs to v10 variant, different print format) | SELFTEST PASS (5 knots agree at s0=3,11) |
| close/exact_validate | yes 34s | no stored file for this variant; first lines equal the v10 stored file | rel. errors up to 2.4e-13 |
| v10/checks/certify_ladder | yes | identical after timing removal | 21 of 21 |
| v10/checks/certify_ladder_selftest | yes | identical | pass |
| v10/checks/exact_validate | yes | 2 lines differ: K11n4 N=3 largest rel diff 2.4e-13 rerun vs 2.5e-13 stored (and overall line same) | exact vs float agree ~1e-13 |
| tests/j4_sparse | yes 4s | identical to j4.log | N=4 diffs 166.66, 353.50 |
| tests/ta_adjoint | yes 48s | J3, J4, volumes, |J3| at phase identical to the stored v08 audit log; only the J2 residual differs: 5_1/10_132 8.5e-14 vs 1.2e-13, 8_8/10_129 6.6e-14 vs 8.2e-14, 8_16/10_156 5.1e-14 vs 1.0e-13, 10_25/10_56 2.7e-13 vs 2.4e-13, 10_40/10_103 6.0e-13 vs 5.2e-13 (all < 1e-12, as paper requires) | 5 of 5 separated by J3 and ordered; |J3| at t=e^{8 pi i/15}: 0.914/6.197, 18.01/23.96, 46.11/52.36, 73.07/79.85, 107.84/122.63 equals TEST_LOG; the ten values rise with the volumes 0, 4.057, 7.801, 8.902, 10.579, 11.163, 11.876, 12.399, 12.889, 13.875 |
| tests/ta_census | yes 46s | identical (timings only) | |
| tests/ta_controls | yes 1s | one number: 10_161/10_162 N=3 min mirror max diff 1.10e-11 rerun vs 1.34e-11 stored (floating noise, a null control) | |
| tests/tj_blind11 | yes 27s | json unchanged by the rerun (identical to stored) | |
| tests/tj_cross | yes 274s | uses stored scan_11 rows: <=10 vs 11 same A+J different HOMFLY none; same all three (10_155, K11n37*) | |
| tests/tj_merge12 | yes 270s | uses stored scan rows: 12 vs 12: 0 different HOMFLY, 506 same-all-three; <=10 vs 12: 0, 86; 11 vs 12: 0, 42 (matches the stored log) | |
| tests/tk_holdout | yes 34s | identical to tk.log, json unchanged | 60 knots mean rel err 2.85%, Spearman 0.992, max 10.3% (paper 2.85%) |
| tests/tk2_holdout | yes 4s | identical to tk2.log, json unchanged | 40 knots 2.94%, Spearman 0.993, max 13.5% (paper 2.94%) |
| tests/tn_phase | yes (~400s) | identical to tn.log | window theta 1.457-2.421 rad (Spearman 0.905 ... 0.937), best theta 1.6755 = 8pi/15 Spearman 0.9922; 0.3-1.27 and 2.6-3.0 near zero or negative. Paper: window 1.46-2.42, 8pi/15 best: matches |
| votkp/chk_fig8 | yes 63s | no stored file | Vol 4_1 2.029883212819307 = 2D(e^{i pi/3}); MMR and Kashaev lines |
| votkp/chk_geom | yes | no stored file | volumes: 4_1 2.029883212819, 5_2 2.828122088331, 8_8 7.801341224, 10_129 8.901516637, 8_16 10.579021917, 10_156 11.163390642, 10_25 11.875779604, 10_56 12.398802156, 10_40 12.888740330, 10_103 13.874789570, 5_1 flat (0), 10_132 4.056860224; 10_161 = 10_162 5.638772949 isometric True. Match the five-pair volumes in the ta_adjoint line |
| votkp/chk_pairs | yes | braids.json unchanged | 5_1 vs 10_132 same Alexander, Jones, HOMFLY True; 8_8 vs 10_129 and 4_1 vs 11n19 print False because the script does not mirror (the paper pairs are 8_8 / mirror of 10_129): not a mismatch, scan10 handles mirrors |
| votkp/scan10 | yes 177s | scan10.json unchanged | <=10 crossings: none with same Alexander+Jones but different HOMFLY; same-all-three includes the five pairs (5_1/10_132, 8_8/10_129*, 8_16/10_156*, 10_25/10_56*, 10_40/10_103*) and 10_161/10_162* |
| tests/scan_11_12 | TIMEOUT at 540s (about 300 of 2728 knots done at ~1.5 s/knot) | not comparable | rerun in pieces, see final section |
| tests/scan_part | exit 1 with no arguments (needs cross LO HI) | | used as the resumable piece form |
| nuc/nuc01 | first run failed: missing `tables`; after installing it, failed in sklearn because nucleardatapy 1.0.2 inserts None into sys.path. Run through nuc_launch.py (drops None entries only, runs nuc01.py unchanged) | numbers differ, see below | |

## nuc01 (rerun vs stored nuc01_output.txt, rerun first)
Header lines identical (434 nuclei, 0.52 deformed, n=309). Classification balanced accuracy: lin SHAPE 0.651 vs 0.649; lin NPNN 0.827 vs 0.831; lin LEVEL 0.419 vs 0.448; lin DVPN 0.440 vs 0.441; lin A 0.456 vs 0.498; shuffled 0.515 vs 0.494; knn SHAPE 0.624 vs 0.621; knn NPNN 0.754 vs 0.775; knn DVPN 0.559 vs 0.581; knn A 0.657 vs 0.647; knn LEVEL 0.450 vs 0.455. Paper/ledger 0.65 vs 0.83: reproduced (0.651 / 0.827), KILL 1 triggered True in both. Charge radius MAE (fm): lin SHAPE 0.0361 vs 0.0364, LEVEL 0.0344 both, NPNN 0.0314 vs 0.0313; knn SHAPE 0.0328 vs 0.0334, LEVEL 0.0373 vs 0.0370, NPNN 0.0337 vs 0.0360; baseline 0.0362 both. Level beats shape in lin (0.0344 < 0.0361) and not in knn (0.0373 > 0.0328) in the rerun; stored 0.0344<0.0364 and 0.0370>0.0334: same verdict, 1 of 2. Cause not isolated (sklearn 1.9.1 vs 1.8.0, nucleardatapy download version); differences are in the third digit.

## Other checks
- A-polynomial volume of 4_1: no package script computes it. apoly41.py (own script, textbook A-polynomial of 4_1) gives 2 Int_0^{pi/3} log|L| = 2.02988321281930725; paper 2.0298832128193074 differs by 1.5e-16; SnapPy volume 2.029883212819307. 5_2 volume 10^-10 claim: not computed (no 5_2 A-polynomial in package; untested). 5_2 SnapPy volume 2.828122088331 (chk_geom).
- Signature census: verify_sig_all matches stored (12965 functions). The 17,360 roots / 513 even-multiplicity roots / torus knots as maximizers come from wall01, jump01/02, sig01_02 (not snappy scripts; check_v29 report already had them identical; SIG-02 stored output shows torus knots T(2,3), T(2,5), T(3,4)=8_19, T(2,7), T(2,9), T(3,5)=10_124, T(2,11), T(2,13) as unique maximizers where they exist, 34 maximizers and no torus knot at 12 crossings). Not rerun by me.
- TIME-01 window counts: time01_checks identical. time01c / time01d_above differences reported in check_v29 (counts outside the window, N above upper wall 3 vs stored 4) are not snappy scripts and were not rerun here.
- T(3,4) Hopf charges 7,10,11,13,15 and G-02 glueball: not in my script list; not run.

## Final section: 11 and 12 crossing rescan (scan_11_12 in resumable pieces, via scan_part.py unchanged)
- scan_11_12.py alone: TIMEOUT at 540 s (about 300 of 2728 knots). Rerun with the package's own scan_part.py in pieces of 150 down to 37 knots (scanchunks.py), every piece finished.
- Fresh rows: 11 crossings 548 of 552 knots (missing K11a247, K11a343, K11a362, K11a363: they hit the 60 s per-knot cap); 12 crossings 2076 of 2176 (100 capped). Stored rows hold 548 and 2075; the same knots are absent there. Fresh vs stored: 0 rows differ above 1e-6 relative (max difference 0); only K12a564 (+ mirror) is in the fresh set and not in stored.
- tj_cross on fresh rows: <=10 vs 11 same Alexander+Jones but different HOMFLY: none; same all three: (10_155, K11n37*), (10_155*, K11n37). Equals stored.
- tj_merge12 on fresh rows: 12v12 0 different HOMFLY, 506 same-all-three; <=10 v 12 0 and 86; 11 v 12 0 and 42. Equals stored log. Kill line (a pair equal on Alexander+Jones with different HOMFLY) not triggered.
- Pair count, own script count354.py (distinct unordered pairs, mirrors identified, <=12 crossings): 353 pairs equal on all three, volume separates 251 (102 same volume), using fresh rows and also using stored rows (identical). PAPER: 354 and 253. MISMATCH: 353 vs 354 and 251 vs 253. Likely cause for the pair count: the paper's 354 comes from the KnotInfo census (ROUND_02_KNOT_RESULTS.md), while the numeric scan lacks the 104 capped knots; I did not test which pair is missing. The 251 vs 253 not explained (volume tolerance 1e-6, flat-volume knots set to 0 in my count); untested against KnotInfo volumes.
- Five pairs (5_1/10_132, 8_8/10_129*, 8_16/10_156*, 10_25/10_56*, 10_40/10_103*): all five equal on the three invariants in scan10 and separated by the volumes in chk_geom (0 flat vs 4.0569, 7.8013/8.9015, 10.5790/11.1634, 11.8758/12.3988, 12.8887/13.8748). 5_1 volume is 0 (torus), SnapPy marks it flat, i.e. "separated" there means torus vs hyperbolic.
- T(3,4) Hopf charges 7,10,11,13,15: no script in my list (Skyrme-Faddeev layer); untested. G-02 glueball: not in my list; untested. Signature/Alexander census (even multiplicity, 513, torus maximizers): not snappy scripts, stored outputs read only (513 and 17,360 in ADM_01_RESULTS_v2.md; torus maximizers in sig01_02_output.txt); verify_sig_all reran identical. TIME-01 window counts: time01_checks reran identical; counts time01c/time01d_above not rerun by me (earlier check_v29 report: differ outside window, 1 per knot inside matches).
- 5_2 A-polynomial volume 1e-10: not computed (untested). 4_1: 1.5e-16 from paper's value with my own computation.
