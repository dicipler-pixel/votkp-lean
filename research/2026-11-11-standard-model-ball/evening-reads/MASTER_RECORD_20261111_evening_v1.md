# Master record — full reads of 11 Nov 2026 (evening), v1
Jeromie Beasley. Prepared with AI assistance (Claude, Anthropic). Thirteen readers, one notes file each; this file is the integration. A line marked [reader] is a reader's own arithmetic and has not been rerun.

## 1. Coverage
| Notes | Read in full | Not read / limit |
|---|---|---|
| 01, 02 | Two Trees in One Ball v4, body and scripts appendix | Lean files themselves (only the generator script) |
| 03 | One Tree One Ball, Two Trees One Scale, Seiberg-Witten mixer, BallJoins.lean, SeibergWitten.lean and its chain files | Lean not run |
| 04 | Tree Ball Light Mixer (own code), Standard Model in the Ball | leftover library code keyword-searched only |
| 05 | Full Table maths reviews, scope, Luna report and logs | referenced scripts absent from the folder |
| 06 | Round 4 four holes: reports, every script header and output | .pkl files; census .json dumps (outputs duplicate them) |
| 07 | 10 Nov session outputs, read records 01-09, piecing maps, open-question tests v1-v3, Recoveries | body of build_recoveries.py |
| 08 | SU(3) Connection Energy, rounds 5 and 6, Dirac read record | integer pivot lists; no code run |
| 09 | Element data: thresholds, 104-118 dossiers, archive against live NIST, manifest (487 hashes match) | equations of the Matter deep dive (images) |
| 10 | Colour paper and colour delivery folder | raw LANL / CIE data (identified only) |
| 11, 12, 13 | VOTKP v2.9, all 165 pages viewed as images, display equations transcribed | one exponent on p84 unreadable |

Notes 05, 07, 09, 10 and 13 mention material the package marks private (Mixin, perception). They are held out of this public folder. Not assigned tonight, because full read records from the morning exist: atlas cards B97-B207, Dirac Time v3.0.1, the Matter paper, VOTKP v1.1 and v2.1.

## 2. Three things called "wall", two things called "5/8", three disks
- Wall A, the shell wall of VOTKP v2.9 Thm 8.2: Gamma_sh = (2n-1)/(n^2+(n-1)^2) = 3/5, 5/13, 7/25, 9/41, 11/61, 13/85.
- Wall B, the half line Gamma^2 = 1/2, z = 3 + 2 sqrt 2: Two Trees Thm 5.3, 5.4, 8.6; BallJoins J3, J4. It is in NO page of VOTKP v2.9, no colour file, no element data file.
- Wall C, in the colour spreadsheet: the first big ladder step of K, Rb, Cs.
- 5/8 (a): the He-like first-order screening term, VOTKP v2.9 sec 15.10, IE_last = Z^2/2 - 5Z/8 - ... Hartree; test FIVE-EIGHTHS-01 passed (residual exponent 4.30, Dirac term).
- 5/8 (b): the B189 limit c_inf in round 6. The ledger prints "about 0.63"; 5/8 is not printed or certified there. [reader] Richardson on the printed values gives 0.6244 to 0.6249. No link between (a) and (b) has been tested.
- Three disks (handoff notes sec 2): Smith Gamma_S = (z-1)/(z+1); vacuum disk G = (z-w)/(z-w-bar); the chiral grading. "Never carry a statement from one to another without redoing it." The 10 Nov record and Recoveries item 06 pair the vacuum-disk line |G|^2 = 1/2 (knot tetrahedra) with metals 35/35 from the reflection coordinate. That pairing breaks the rule and must be redone before it is used.

## 3. Elements: what the reads establish
- The shell and screening split is VOTKP v2.9 Thm 8.2, checked on 5,714 steps to 4e-16, and called there a bookkeeping identity.
- v2.9 on the alkalis: jump in effective charge 1.10, 1.88, 2.31, 2.89, 3.31 down the column (grows). Across a row the screening part falls from alkali to noble gas (rank correlation -1, five rows). Two kinds of screening under one shell part: closed p core (1 to 3, grows down), filled d shell (under 1, shrinks along the row). f shell not a third kind (registered, killed).
- Not stated in v2.9 (searched in notes 11-13): that the charge RATIO Zc/Zv is the same for Na, K, Rb, Cs (2.022, 2.024, 2.045, 2.032; SHELL-SCREEN-04). Still to check against v2.9 Figure 13, where the points are drawn.
- Eight steps past wall B out of 5,737: first steps of Li, Na, K, Rb, Cs and the K-shell openings of Be, B, C. "Wall B marks shell openings" failed that way (8 of 694).
- Alkali optical phase (PHASE-LADDER-02): the five atoms past wall B hold 5 of the top 6 optical phases at 1.5, 2.0, 2.5 eV (p = 2.7e-06 each); order Cs > Rb > K > Na > Li; the even reading |Gamma|^2 does not see it (p 0.09 to 0.10). Same order as the wall margins of SHELL-SCREEN-04 (Cs +0.020 ... Na +0.413). The link is a reading, untested.
- Wall energy from the ladder: failed that way (Spearman +0.06, -0.28, +0.26, n = 30).
- Colour of elements follows the IE1 level: rule IE1 < 6.82 eV, AUC 0.946, accuracy 0.831 against 0.569.
- Francium: Fr+ 22.4 +/- 1.9 eV (semi-empirical). [reader] Gamma box 0.6685 to 0.7129 contains 1/sqrt 2; caesium's box does not. v2.9 T05 (column line in ln IE1) killed: Fr missed by 0.55 eV, Ra by 0.99 eV; cause given there: filled f shell and relativistic 7s contraction. Francium has no optical track, so the phase test cannot be run on it.
- Archive against live NIST: 4 of 7,021 slots differ (S, Ca, Nd, Np neutrals). All alkali, Fr, Ra rows identical.
- Sign of g in z(a) = kappa - g/(a - d): reading the step downward (z to 1/z) flips every g to positive, 61 of 61.
- Tree and ball: the boost generators fail the su(3) algebra test (dimension 6, not 8); helicity locking rejected; no rational direction lies on the Koide 45 degree cone (mod-4 descent); Koide's 1/2 and wall B's 1/2 are different objects.
- No file read tonight derives a link between atoms and the tree.

## 4. Labels corrected on tonight's own run (SHELL-SCREEN-04)
- Parts A and B reproduce v2.9 Thm 8.2.
- Part C uses the same 1/Z series as v2.9 sec 15.10 and FIVE-EIGHTHS-01. New there: only the placing of the wall B crossing (Z* = 6.538 with the 5/8, 9.47 without).
- Part D (constant alkali charge ratio) is the one candidate new observation.
- The francium reading (22.67 to 23.18 eV) is a different construction from T05, but T05's cause applies to it; francium's archived ratio 2.010 already sits below the Na-Cs band. Graded weak.

## 5. [reader] items to rerun before use
- Gap between planes of two orthogonal axes closes exactly at z = 3 + 2 sqrt 2 (cosh delta = sinh^2(l/2)).
- At ratio 5 the distance from the centre to the commutator's fixed point is arcosh 3 = 2 ln(1 + sqrt 2) (checked at z = 5 only).
- All 19 turning knots enter the commutator band by x <= 0.725 < ln(1 + sqrt 2) (read from printed outputs).
- Seiberg-Witten wheel: M(1,0) M(1,-1) M(0,1) = -I; of 27 ordered triples from {1,7,9} only the cyclic rotations of 1,7,9 close.
- Among the four alkalis with a crossing, E_wall rises with the ladder step (Cs 2.50, Rb 3.28, K 3.85, Li 5.12 eV).
- Dropped solutions on 10_124 hold rational 2/3, 5/6, 9/10, 2/5, uncommented.
- The "2 x denominator" pattern appears twice: a 2pq cycle (read record 07) and d = 2q (open questions sec 11).

## 6. Slips, for the ledger (nothing changed in any paper)
Two Trees v4: CLAIMS file stale (three proved items listed open); "488,281 reduced words" counts first-letter-i words only; sign error in a script comment on (7+24i)/25; area report understates three outputs and omits a script error at 6_1; 60-digit band run gives false hits for 8_8; abstract's "proved and optimal" beside "checked in Lean" (only the ping-pong is in Lean); zero set of the relator area rests on a grid check.
Mixers: SM page readouts off by one, particle at centre when E < m, near-rim W/Z given two states, "wall crossed the other way" (Light mixer corrects all four); Seiberg-Witten wheel colour keyed one class off the other scenes; "J10" cited, BallJoins stops at J8; Two Trees One Scale test numbers hard-coded with no script; ROWS has 39 rows, text says 40.
Round 4: 89/34 k printed 0.0083, verified 0.007758; defect sign negative on the climb against |lambda-1|^2 in the text; "one electron alone outside a closed core" does not describe Be, B, C; 49/17 and 73/25 flagged near-real and not rerun; "955 of 20,000" depends on the Exner weights.
10 Nov record: piecing maps predate every test; "median 0.50" cannot hold beside 99.7% inside the line; 494 silent roots credited to VOTKP, which prints 513; NEVER-TURN-03 ran 11 tests and reports 7; 8_8 fits none of the three families; 233/89 run has no output; CHAIN-WHOLE-03 has no equation-file entry; Two Trees v4 had no read record until tonight.
Rounds 5, 6: Ky Fan loss printed 15 to 33%, output gives 12.3 to 33.0%; pendulum data follow w - kappa/4, script prints w - kappa/2; window wall "in Lean" in one file, "not a Lean theorem" in another; SU(3) method note's single negative pivot at z = 57.9 holds at one grid size only; one recorded cross-check not in the shipped scripts; only 1 of 12 round-6 tests is exact.
VOTKP v2.9: step index from 1 in the text, from 0 in Appendix G; Appendix B "all machine-checked" then lists unformalised items; envelope share stated two opposite ways (p85, p86); 5_2 volume to the tenth digit only; Fig 6 285 pairs against 354 in the text; Russell T3 and T6 identical by construction.
Element data: Lv, Ts values differ between helper and table; Nh second threshold equals Rf third (23.84); step counts 5,737 (109 elements) against 5,714 (118) not reconciled.
Colour: deep-dive README still says ledger beats log on grey (corrected replay reverses it); archived chroma trial count doubled by overlapping exports.

## 7. Open, in order
1. Is the constant alkali charge ratio in v2.9 Figure 13, and does it hold on the second members (Mg+ 1.539, Ca+ 1.553, Sr+ 1.577, Ba+ 1.577, Ra+ 1.498)?
2. Does the alkali optical phase track the wall margin? Kill line to be written before the run.
3. Redo "the same circle in light" inside one disk (section 2, three disks).
4. The space fraction E = 1 - V_own/V against Gamma: write the map first; find RECOVERED_ELEMENT_DATA_20261106.csv.
5. Reconcile 5,737 and 5,714.
6. The two 5/8s: test for a link, or record that there is none.
