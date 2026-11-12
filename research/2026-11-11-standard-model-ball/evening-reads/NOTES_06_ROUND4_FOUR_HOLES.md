# NOTES 06 — round 4, "the four holes" (10 Nov 2026), folder VOTKP_round4_four_holes_20261110_v1

Reader notes. Everything below is what the files say. Where I add arithmetic on printed numbers it is marked (mine). Nothing executed from the folder; text read with cat/head/sed and one `python3 -I` pass that only parsed hidden_g_01.out.

---------------------------------------------------------------------
## 1. COVERAGE

Folder: /home/claude/in/VOTKP_round4_four_holes_20261110_v1/round4/ (90 files incl. 3 .pkl, skipped as instructed; 12 .json census dumps not opened, they duplicate the .out chunks).

Read IN FULL:
- FOUR_HOLES_20261110_v1.md (7,150 B), FOUR_HOLES_20261110_v2.md (11,297 B), EQUATION_FILE_ENTRY_20261110_four_holes_v1.md (1,343 B), READ_RECORD_10_COLOUR_SELECTS_THE_LEADER_v1_2_20261110_v1.md (4,290 B), signs/SIGNS_REPORT_20261110_v1.md (22,373 B).
- Main-folder scripts and outputs, all in full: ladder_wall_01, phase_ladder_02, plasma_wall_01, time_wall_01, defect_wall_01, colour_peel_01/02/03, verify_signs_01..05 (.py and .out).
- signs/: hidden_g_01/02/03 (.py, .out), limit_m2_01 (.py, .out), limit_m2_02 (.py via diff against 01; .out lines 1-80 only: header, identities, tallies, d-candidate table, first rows of the "not covered" list; the remaining rows repeat the limit_m2_01 table), limit_m2_03/04 (.py,.out), limit_real_03/04/05/06 (.py,.out; a few very long lines cut at ~260-300 characters), riley_exact.py and riley_exact_w.py (headers only, first 15-20 lines), never_census_02.py (full), never_census_02 five .out chunks (header + every NEVER line + all summary lines; individual TURN lines not read one by one), never_census_01.py (first ~60 lines: header, scan, roots_band, work, main), never_census_01 three .out chunks (summary/NEVER/roots-only/border lines only), never_rule_03.py (first 60 lines) and .out (full; some lines truncated at 700-900 chars), never_rule_04.py (first 40 lines) and .out (full), never_rule_05.py (first 45 lines) and .out (full), never_golden_03 (.py,.out), never_border_06 (.py,.out), split_signs_01.py (to the end of Part C, truncated at 260 columns) and .out (from Part B on; Part A lines 1-23 not read separately, the numbers are in the report), split_signs_02 (.py,.out).
- NOT read: the three .pkl files; the .json census dumps; the full per-knot TURN lines of the census chunks; the printed "FULL TABLE p <= 31" of limit_m2_02.out (identical content to limit_m2_01.out, which I read).

---------------------------------------------------------------------
## 2. OBJECTS AND DEFINITIONS

(The source's own words in quotes are under 15 words.)

- **Half line** G^2 = 1/2, i.e. peel ratio z = 3 + 2 sqrt 2 = 5.828 (FOUR_HOLES v1/v2 Headline; DEFECT-WALL-01 part C solves |dM| = 4 for z and returns [3 - 2 sqrt2, 3 + 2 sqrt2], "G^2 there: [1/2, 1/2]").
- **Smith point / Gamma** G = (z - 1)/(z + 1) = tanh(tau/2), z = e^tau (FOUR_HOLES 2a; COLOUR-PEEL-01 header; DEFECT-WALL-01 B). Peel distance tau = |ln z - ln z'| (VOTKP 8.1 cited).
- **Meridian pair (Two Trees)**: a = [[s,1],[0,1/s]], b = [[s,0],[-v,1/s]]; commutator number k = 2 - tr[a,b] (DEFECT-WALL-01 header).
- **Defect of the squared meridian** dM = 2 - (s^2 + s^-2). Identity A: k = v(s^4 - s^2 v - 2 s^2 + 1)/s^2 = -v(v + dM) (DEFECT-WALL-01 out line A). Real climb step z = s^2 = e^tau: dM = -4 sinh^2(tau/2) = -4 G^2/(1 - G^2). Turn step s = e^{i theta/2}: dM = +4 sin^2(theta/2) (out lines B). So dM is NEGATIVE on the climb and POSITIVE on the turn (see section 7).
- **UPG defect/guard split**: delta = |lambda - 1|^2, delta + g^2 = 4 (FOUR_HOLES 2e; READ_RECORD_10 "bears on" item 1). Crossed fraction = delta/4. Colour eq. (6): crossed = |1-u|^2/4, parallel = |1+u|^2/4, budget |1-u|^2 + |1+u|^2 = 4 (READ_RECORD_10, section 3).
- **Max of k on the real slice**: max over real v of k is dM^2/4 at v = -dM/2; k = 4 has a real v iff (dM - 4)(dM + 4) >= 0, i.e. |dM| >= 4 (DEFECT-WALL-01 out). Unit-circle meridian: max k found 3.999508, cap 4 only at theta = pi.
- **Ladder step** z_q = IE_{q+1}/IE_q (LADDER-WALL-01); `Nleft` = Z - (q+1) electrons left when the larger threshold is paid. Closed-core counts used by the script: {2,10,18,28,36,46,54,60,68,78,86}.
- **Bare shell-wall** (VOTKP Thm 8.2 as quoted in LADDER-WALL-01 header): G_sh = (2n-1)/(n^2 + (n-1)^2), z -> (n/(n-1))^2; n = 2 gives z = 4, G^2 = 9/25 < 1/2. Bare values listed in HIDDEN-G-01: N=2: 4, N=10: 2.25, N=28: 1.778, N=60: 1.5625.
- **Optical reflection** G = (1-N)/(1+N), N = n + ik; |G|^2 = R (normal incidence), so the half line on the disk is R = 1/2 (PLASMA-WALL-01 header). "Phase" = |angle(-G)| in degrees (PHASE-LADDER-02 code). Photon energy E = 1.23984/lambda.
- **E_wall** = last photon energy at which R falls below 1/2 for good (PLASMA-WALL-01).
- **Share / Hilbert / Schrodinger** (COLOUR-PEEL-01 header): share balance s1 - s2 = (z-1)/(z+1) = G; Hilbert distance = |ln z - ln z'|; Schrodinger distance = |phi - phi'| with cos phi = G = tanh(tau/2); d phi = (1/2) sech(tau/2) d tau. Whole climb line has Schrodinger length pi (FOUR_HOLES 2a).
- **Exner luminous weights** a = 43.33, 32.76, 1 (COLOUR-PEEL-03 header); with weights p_i = a_i x_i / h, "white" in share space is x proportional to 1/a.
- **Colour eq. (7)** two decaying parts: ratio reads elapsed time at the gap; tau = gap * t (TIME-WALL-01). **Eq. (8)** bend of log brightness = squared Fisher speed; for two parts (ln I)'' = (gap/2)^2 (1 - G^2) (TIME-WALL-01; READ_RECORD_10 section 8).
- **Riley relation, types A and B** (SIGNS_REPORT Q2 "Method"; limit_m2_01 header): t = tr(ab) = s^2 + s^-2 - v; k = v(t - 2). k stays finite as s -> infinity only if v ~ kappa/s^2 (type A) or t - 2 ~ kappa/s^2 (type B). w = t - 2. v and w are the two roots of X^2 + dM X + k = 0 (identity i), so k = v*w, v + w + dM = 0, tr(ab^-1) - 2 = v.
- **Chebyshev identity (ii)**: tr[a, c^m] - 2 = S_{m-1}(tr c)^2 (tr[a,c] - 2), S_{m-1}(2) = m. Used with c = ab (type B) or c = ab^-1 (type A).
- **Never-turner definition** (NEVER-TURN-02 as restated in never_census_02.py HEAD): the pair turns at x iff some real root v of the Riley relation at s = e^x has v > 0, t = tr(ab) > 2 and k = v(t-2) < 4. NEVER = no such root on the grid x = 0.1..1.5 step 0.1, then 2, 2.5, 3, 3.5, 4. Band = {v < A/2} + {w < A/2}, A = v + w, k = r(A - r) < 4; each half read in the variable where its roots are small.
- **Hidden level model** (HIDDEN-G-01 header; VOTKP 5.3/5.9): Model H: z(a) = kappa - g/(a - d) (3 numbers); Model L: z(a) = alpha + beta a. VOTKP 5.3 with a scalar hidden level gives A + BC/(a - d), g = -BC; a Hermitian coupling has BC = |B|^2 > 0 so g < 0.
- **Split roots**: nullity-2 double roots of the Alexander polynomial on the unit circle; label "equal" (signature jumps by 4) or "opposite" (silent). Level discriminant d; equal iff d > 0 (SPLIT-SIGNS-01 header).
- **The golden family** [2, 1^n, 2]: 13/5 (n=2), 21/13 (n=3), 55/21 (n=5), 89/34 (n=6), 233/89 (n=8) (NEVER-GOLDEN-03).

---------------------------------------------------------------------
## 3. RESULTS BY HOLE

Grade words as in the source: PROVED (exact algebra), CHECKED (numerics, size given), READING, FAILED (kill fired).

### Headline (FOUR_HOLES v1/v2): "The half line G^2 = 1/2 is one number seen from five places."
1. Two Trees: commutator of two equal perpendicular steps is parabolic at z = 3 + 2 sqrt2 (his theorem 5.4).
2. UPG: meridian defect |delta| = 4 exactly there. PROVED (DEFECT-WALL-01).
3. Two Trees knots: k = -v(v + delta); on the real slice k reaches 4 iff |delta| >= 4. PROVED.
4. Atoms: of 5,737 ladder steps only 8 beyond it. CHECKED (LADDER-WALL-01).
5. A fade: bend of log-brightness (gap/2)^2 (1 - G^2) halved exactly there. PROVED, CHECKED to 20 digits (TIME-WALL-01; the output shows the worst relative error 1.41e-48 and the half-bend solved to 20 printed digits).
"Earlier appearances already on record: the vacuum-disk metal / non-metal line (35 of 35 against 0 of 6) and the bowl." (stated, not re-derived here.)

---
### HOLE 1 — ATOM TO KNOT

**ladder_wall (LADDER-WALL-01).**
- What was tried: place every ladder step IE_{q+1}/IE_q of every element in the archived NIST thresholds (votkp-lean/data/element_thresholds_20261011.json.gz) against z = 3 + 2 sqrt2; split by electrons-left N and by closed core.
- Kill line (written first): "the half line marks shell openings" dies if more than 10% of beyond-line steps are at non-closed N, or fewer than half of closed-core openings are beyond the line. Opposite: list closed-core openings that stay inside, by Z.
- Numbers (out): 109 elements with >= 2 thresholds; 5,737 steps; beyond z > 5.828: 8; all 8 at a closed core N (8 of 8); closed-core openings beyond the line: 8 of 694.
 - Per core: N=2: 101 openings, 4 beyond (Z = 3,4,5,6), largest z 14.03 (Z=3), smallest 3.888 (Z=103). N=10: 93, 1 beyond (Z=11), largest 9.20. N=18: 85, 1 (Z=19), largest 7.29. N=28: 75, 0, largest 2.63 (Z=29). N=36: 72, 1 (Z=37), largest 6.53. N=46: 64, 0, largest 2.84. N=54: 56, 1 (Z=55), largest 5.95. N=60: 50, 0, largest 2.13. N=68: 42, 0, 2.16. N=78: 32, 0, 2.19. N=86: 24, 0, largest 5.50 (Z=87).
 - Beyond-line steps NOT at a closed core: [] (empty).
 - K-shell opening (N=2) z by Z: 3: 14.029, 4: 8.451, 5: 6.838, 6: 6.08, 7: 5.64, 8: 5.353, 9: 5.151, 10: 5.001, 11: 4.886, 12: 4.794, 13: 4.719, 14: 4.657; "bare limit 4".
- Where it stands (FOUR_HOLES 1a): the eight are Li, Na, K, Rb, Cs first steps plus Be, B, C K-shell openings. First step of alkali: Li 14.03, Na 9.20, K 7.29, Rb 6.53, Cs 5.95; Fr 5.50 "is inside". N = 5.64 inside. "The half line marks shell openings" is FAILED (8 of 694). Statement: "no bare shell opening reaches the half line. A step is beyond it only when one electron sits alone outside a closed core and the core screens it well." (Note the 8 include Be, B, C, where the K-shell opening is not "one electron outside a closed core"; see section 7.)

**plasma_wall (PLASMA-WALL-01).**
- Tried: rank-correlate E_wall (last half-line crossing of R = |G|^2) against three ladder readings: IE1, first step z1 = IE2/IE1, sum of thresholds down to the closed core ("valence sum"). Optical data from /home/claude/data_ri_repo/database/data/main (refractiveindex-style yml tables), best-spanning track per element covering 0.38-0.78 micron.
- Kill (written first): |Spearman rho| < 0.5 for every ladder reading -> E_wall is NOT read from the ladder. Opposite: 1/E_wall (rank flips sign only) and the low-energy side, phase of G at 2 eV against the same readings.
- Numbers (out): 41 elements with a track through the visible; 30 with a last crossing inside the tabulated range. Spearman E_wall vs IE1 rho = +0.057 (p 0.766); vs z1 = -0.279 (p 0.135); vs valence sum = +0.261 (p 0.164); n = 30. KILL FIRED -> FAILED.
 - Opposite (phase at 2 eV, n = 30): vs IE1 -0.436 (p 0.0161); vs z1 +0.545 (p 0.00183); vs valence sum -0.584 (p 0.000712).
 - Never above 1/2: B, Se. No final crossing in range: Be, Cr, Ge, In, Mo, Na, Os, Rh, Zn.
 - E_wall table (eV) for alkalis in the list: Cs 2.50, Rb 3.28, K 3.85, Li 5.12 (Na absent). Others e.g. Au 2.44, Cu 3.05, Ag 3.69, Al 15.14, Si 14.44, C 0.10.
- Where it stands (FOUR_HOLES 1b): "The optical wall energy is not in the ladder." Set-aside item 1 in the equation-file entry; diverted to the optical phase.

**phase_ladder (PHASE-LADDER-02).**
- Tried: the ladder has exactly five neutral atoms whose first step lies beyond the half line (Li, Na, K, Rb, Cs). Do they carry the largest optical phase? One-sided Mann-Whitney of beyond-line atoms against the rest (41 elements) at 1.5, 2.0, 2.5 eV.
- Kill (written first): one-sided p > 0.01, or any two energies disagreeing in direction. Opposite: same test on |G|^2 (the even reading); if equally separating, phase adds nothing.
- Numbers (out), phase in degrees:
 - 1.5 eV: Cs 56.5, K 44.4, Li 28.5, Na 31.3, Rb 50.0; rest median 14.8, max 28.6; one-sided p = 2.7e-06. Top seven: Cs 56.5, Rb 50.0, K 44.4, Na 31.3, Ca 28.6, Li 28.5, C 24.6. Even |G|^2: 0.762, 0.974, 0.928, 0.984, 0.924 (order Cs,K,Li,Na,Rb); rest median 0.778; two-sided p = 0.091.
 - 2.0 eV: Cs 78.6, K 61.2, Li 38.4, Na 42.5, Rb 69.1; rest median 19.3, max 39.5; p = 2.7e-06. Top seven: Cs 78.6, Rb 69.1, K 61.2, Na 42.5, Ca 39.5, Li 38.4, Cu 34.1. |G|^2: 0.649, 0.945, 0.908, 0.972, 0.871; p = 0.099.
 - 2.5 eV: Cs 100.6, K 77.6, Li 49.2, Na 52.6, Rb 88.8; rest median 24.2, max 52.0; p = 2.7e-06. Top seven: Cs 100.6, Rb 88.8, K 77.6, Na 52.6, Ca 52.0, Li 49.2, Au 43.0. |G|^2: 0.494, 0.93, 0.858, 0.95, 0.823; p = 0.099.
- Where it stands (FOUR_HOLES 1c): CHECKED. "5 of the top 6 optical phases at 1.5, 2.0 and 2.5 eV (Ca is the one intruder)". Within the five the order is reversed exactly: "nearer the line on the ladder, larger phase (Cs > Rb > K > Na > Li)". Even reading does not separate (p about 0.09). Caution stated once in the file: five atoms; the physics underneath is known (alkalis are the free-electron metals with the lowest plasma energies); what is new "is only that the ladder's half line picks them and the odd reading finds them where the even reading does not."
- **"Alkali optical phase" result: PRESENT** (this is it). Bridge statement (FOUR_HOLES, What this settles): the atom has a record that carries a phase, it is the optical one, tied to the ladder through the half line = "the atom side of a bridge". Knot side is READING only: "the same line is where a knot's meridian pair can first reach the top of the turning band. No atom-to-knot map is claimed."

**hidden_g (HIDDEN-G-01/02/03), hole 4 item "sign of g in z(a) = kappa - g/(a - d)" — atoms and knots.**

HIDDEN-G-01 (atoms).
- Data: element_thresholds_20261011.json.gz, 118 elements. Family = fixed electron count N; a = Z; z = IE(Z,N)/IE(Z,N+1) (the peel step between ions holding N+1 and N electrons; VOTKP Thm 8.1, Gamma = (z-1)/(z+1)); 98 families with >= 12 points.
- Kill (written first): per family fit on points with index mod 4 != 2, predict mod 4 == 2. The sign of g counts only if held-out RMS(H) <= 0.5 * RMS(L) and the fitted pole d lies outside the fitted range of a. Claim under test: g < 0 in every counted family; killed by one counted family with g > 0. Opposite: z -> 1/z (step read downward). Second setup: fit lowest 70% of Z, predict top 30%.
- Numbers (out):
 - MAIN: 98 families; verdict counts in 62; g < 0 in 62, g > 0 in 0; no verdict 36 (25 of those g < 0). By kind: closed-core (shell opening) 7 g<0, 0 g>0; inside a shell 55 g<0, 0 g>0. 
 - OPPOSITE (1/z): counts in 61; g < 0 in 0, g > 0 in 61; no verdict 37 (10 with g < 0).
 - SECOND SETUP (extrapolation): counts in 84; g < 0 in 84, g > 0 in 0; no verdict 14. Sign agrees between MAIN and SECOND in 60 of 62.
 - Table values (selected): N=1 kappa 1.0024, g -1.2408, d 0.976; N=2 kappa 3.9151, g -8.4711, d 2.161; N=10 kappa 2.0984, g -6.5290, d 10.076; N=18 kappa 0.9520, g -5.5522, d 18.132; N=36 0.9742, -5.4916, 36.017; N=54 0.8998, -3.6960, 54.278; N=60 0.9802, -2.5536, 58.727; N=86 0.7734, -4.2967, 86.093. N=28 not counted (kappa 1.6164, g -2.2881). No-verdict families with g > 0: N = 6, 14, 32, 40, 44, 48, 62, 66, 68, 69, 78 (all small positive g, "False").
 - kappa at closed cores vs bare (n/(n-1))^2: N=2 3.915 (bare 4), N=10 2.098 (bare 2.25); N=18 0.952, N=36 0.974, N=54 0.9, N=60 0.98, N=86 0.773 (bare values are given only for N=2, 10, 28, 60).
 - Report-level numbers I re-parsed from the MAIN table (mine): counted families with kappa within 0.05 of 1: 55 of 62; median (d - N) = -0.2215; |d - N| < 1 in 54 of 62. These agree with SIGNS_REPORT Q4.
- Where it stands: CHECKED, "g is negative in every family that counts" (62 of 62; 84 of 84). READING (report): g < 0 is the Hermitian sign of VOTKP 5.3, but it is "also what plain screening gives (z falls toward kappa as Z grows), so it confirms the reading without separating it from screening"; "The opposite run shows the sign belongs to the direction the step is read: read downward, every g is positive."

HIDDEN-G-02 (knots).
- Data: no stored fitted kappa, g, d for knots existed on disk; shapes generated with SnapPy along Dehn-filling families. Family = (link, cusp, slope type, tetrahedron); a = filling integer in slope (1,a), |a| = 3..40 (where geometric); complex kappa, g, d. L5a1 (Whitehead link) with (1,a) gives twist knots 6_1, 8_1, 10_1 (identified for a = 2, 3, 4). Pole prediction from the unfilled cusp shape tau: d = -1/tau for (1,a), d = -tau for (a,1), tau read from SnapPy, not fitted.
- Kill (written first): "g negative real" means |Im g| <= 0.05|g| and Re g < 0; a family counts only if held-out RMS(H) <= 0.5 RMS(L); one counted family with g not negative real kills it. Opposite: slopes (a,1). Second setup: L6a2, L7a5, L7a6, both cusps.
- Numbers (out): 48 (family, tetrahedron) fits; 45 count; counted with g negative real: 4; counted with Re g < 0: 19, Re g > 0: 26. arg(g)/pi over counted fits runs from -1.000 to 0.972. Pole check: median |d - d_pred| = 0.990; within 0.15 of d_pred: 1 of 45 (the one is L7a5 cusp 1 tet 1, 0.103). Fitted kappa equals the cusped shape to 3-4 digits in counted fits. The 3 uncounted fits: L7a5 cusp 0 tet 3, L7a6 cusp 0 tet 3, L7a6 cusp 1 tet 3 (g about 0.009 / -0.008, tiny).
 - L5a1 (tau = 2.0000+2.0000i, predicted d = -0.25+0.25i), cusp 1 slopes (1,a), 76 fillings: tet0 kappa 1+1i, g +0.0007+1.5783i (arg +0.5 pi); tet1 kappa 0.5+0.5i, g +0.7915+0.0006i; tet2 g -0.7915-0.0001i (arg -1, the "negative real" one); tet3 g +0.0012-1.5849i. Cusp 0: g = -1.5830, -0.7924i, +0.7892i, +1.5830 pattern. Opposite slopes (a,1): g values about (+3.09+3.06i), (+1.56-1.53i), (-1.51+1.56i), (-3.07-3.12i), predicted pole -2-2i.
 - L6a2 tau = 1.7321i (pole 0.5774i): g = +1.8015, -1.7975, +0.9012+1.5601i. L7a5 tau = 0.5698+2.6143i; L7a6 tau = 3.4656+1.5851i; g mostly complex.
- The 4 that pass are "forced by the symmetry of L5a1 and L6a2" (report).
- Where it stands: "g is negative real" KILLED (4 of 45). "Pole at d = -1/tau (cusp shape)" KILLED (1 of 45).

HIDDEN-G-03 (knots, second setup for the kills).
- Kill (for "the kills were artefacts"): g and d from |a| = 20..100 must agree with those from |a| = 3..40 to 5% of |g| and 0.1 in d. Also printed dz/du = -g tau/(2 pi i), with u = 2 pi i/(1 + a tau).
- Numbers (out): stable fits 15 of 16 (the unstable one: L7a6 cusp 0 tet 3, d jumps -2.761 -> 18.527 and g ~ 0). L5a1 cusp 1, |a| = 20..100: g = +1.5711i (tet0), +0.7856 (tet1), -0.7856 (tet2), -1.5711i (tet3); dz/du = -0.5001-0.5001i, -0.2501+0.2501i, +0.2501-0.2501i, +0.5001+0.5001i.
- Where it stands: "For the Whitehead family the four values are g = +i pi/2, +pi/4, -pi/4, -i pi/2 (1.5711 and 0.7856 at |a| = 20 to 100, against pi/2 = 1.5708 and pi/4 = 0.7854). CHECKED to 4 digits." Both kills stand.
- READING (report): "atoms give a real g, knots a complex one; that is a difference between the two sides and it lines up with hole 1 (atom steps are collinear, knot pieces are not)." In the terms of read record 08 "the tetrahedron is an open channel" (record 08 not in this folder).
- Missing: original fitted kappa, g, d "that item 2 refers to are not on disk"; family not named. The vacuum-disk knots-to-10-crossings shape table "is not a one-parameter family and cannot be used".

---
### HOLE 2 — COLOUR

Read: Colour Selects the Leader v1.2 (Drive file id 1EW965Z2ANFBygPzdhRBmfch9txrdQPVZ, 231,674 characters) per READ_RECORD_10: read in full abstract, sections 1-15, references, Appendix 17 (Lean table); NOT read line by line: Appendix 16 (printed scripts/outputs, about 140,000 chars), only COLOUR-LEADER-01 opened for its sampler.

**colour_peel_01 (COLOUR-PEEL-01).**
- Tried: for two channels, the paper's two rulers (Hilbert metric, contracted by every strictly positive map; Schrodinger chromatic metric, "955 of 20,000" stretched) are the two coordinates of one peel step; identities checked on random pairs, and a prediction: a pass stretches Schrodinger's metric on a close pair iff c * cosh(tau/2)/cosh(tau'/2) > 1 (c = local Hilbert contraction), forcing |tau'| < |tau| (pair carried toward white).
- Kill line: (1) any identity off by > 1e-9; (2) any two-channel stretch with |tau'| >= |tau|; (3) formula misclassifies any pass. Opposite: stretches among passes carried AWAY from white must be 0. Three channels = exploration only.
- Numbers (out): 20,000 pairs; max errors: balance - Smith point 3.33e-16; Hilbert - |ln z - ln w| 8.88e-16; Schrodinger - |phi - phi'| 1.06e-11; cos(phi) - tanh(tau/2) 4.44e-16. Close-pair passes (2 channels): Hilbert stretched 0; Schrodinger stretched 22 (0.1%); formula agrees on 20000 of 20000; stretches toward white 22, away 0. Three channels (generic pairs, uniform(.05,5)): Hilbert 0, Schrodinger 0 stretched "(paper recorded 955 of 20,000)"; base rate toward white 0.829.
- Standing: 2a PROVED and CHECKED ("worst error 1e-11"); 2b CHECKED (22 of 22 toward white, 0 away).

**colour_peel_02 (COLOUR-PEEL-02).**
- Second setup with the paper's own sampler (M = uniform(0,1)+1e-3, colours uniform(0.01,1)) because setup 1 found no three-channel stretches. Kill: if stretch rate among toward-white passes is not above that among away passes (ratio <= 1), the two-channel mechanism does not carry to three. Opposite: count stretches among away passes.
- Out: 2 channels: Schrodinger stretched 7 of 20000, Hilbert 0; toward white 13615 passes, 7 stretched (0.05%); away 6385, 0 stretched. 3 channels: Schrodinger stretched 0 of 20000, Hilbert 0 (toward white 16594 passes, away 3406; none stretched). Note: still 0 in three channels with unit weights.

**colour_peel_03 (COLOUR-PEEL-03).**
- Third setup: paper's sampler AND its luminous weights (Exner 43.33, 32.76, 1); same seed as the paper (1920) not reproducible ("generator had been advanced"), so compared in size not digit. Kill: (1) dies if unit and Exner weights give comparable counts; (2) dies if the stretch rate among toward-share-white passes is not higher than among away passes. Opposite: count among away passes.
- Out (20,000 passes each):
 - Exner seed 1: stretched 861; toward share-white 11744 passes, 584 stretched (4.97%); away 8256, 277 (3.36%).
 - Exner seed 2: 882; toward 11821, 616 (5.21%); away 8179, 266 (3.25%).
 - Exner seed 3: 933; toward 11834, 661 (5.59%); away 8166, 272 (3.33%).
 - Unit weights seeds 1,2,3: 0, 0, 0 stretched (toward 16664/16622/16665; away 3336/3378/3335).
 - Exner reversed (1, 32.76, 43.33) seed 1: 936; toward 11895, 690 (5.80%); away 8105, 246 (3.04%).
 - Weights (10,10,1) seed 1: 220; toward 12343, 172 (1.39%); away 7657, 48 (0.63%).
- Standing: (1) survives (weights, not geometry, make the count: 0 vs about 861-933); (2) "stretch only toward white" in three channels FAILED in strict form: "5.0-5.8% of toward-white passes and 3.0-3.4% of away passes". "The lean is there; the rule is not." (2c). Correction for the colour paper (2d, recorded not applied): the "955 of 20,000" count needs Exner's weights; Exner 861 / 882 / 933, unit weights 0 / 0 / 0, three seeds each; "the sentence stands for the weighted metric and should name the weights" (READ_RECORD_10).
- Note on percent range: the written 5.0-5.8 and 3.0-3.4 include the "Exner reversed" run (5.80, 3.04); the three Exner seeds alone are 4.97-5.59 and 3.25-3.36 (mine).

**Other colour results in FOUR_HOLES (2e, 2f), exact:**
- 2e "The crystal is the defect" PROVED: crossed fraction = delta/4; at the trefoil's two walls (alpha = 1/12, 5/12, omega = M^2) crossed fraction 1/4, defect 1, clock d = 6. (DEFECT-WALL-01 final line: [0.24999999999999994, 0.24999999999999994].)
- 2f "Positive channels cannot turn" PROVED: strictly positive 2x2 map has discriminant (a-d)^2 + 4bc > 0, always hyperbolic. Theorem 2's three cases: settles exponentially (hyperbolic), settles as 1/n (parabolic, Jordan tie), never settles (elliptic, swap). DEFECT-WALL-01 part D: 0 of 200,000 positive maps (entries uniform(1e-6,10)) with discriminant <= 0. The "0 of 200,000 in the random search for a counterexample" is this.
- "What this settles" (READING): hue is a climb-side record; it can pick a leader, cannot carry a hand; the turn-side record of light is the pair of polarisation ports (paper section 13: "one port cannot see an orientation; two can").
- Still open: a pure phase theta is the same at every wavelength, so a turn gives a grey split sin^2(theta/2), not a colour; a colour needs a length (retardance in nm). "The knot supplies the phase and nothing supplies the length."

---
### HOLE 3 — TIME

**time_wall (TIME-WALL-01) and defect_wall (DEFECT-WALL-01).**

time_wall:
- Recovery (3a): VOTKP 13.7 "No Hamiltonian here makes a knot's meridian phase the driven parameter; that bridge is open." Dirac Time 9.4 and Colour section 12 prove projector geometry blind to H -> sH + cI so no rate comes from the geometry (Lean: `rescale_same_eigenvectors`, `rate_shift_unique`). "What the knot fixes is the gear, L = (-1)^a M^(-pq) (Dirac Time Thm 13.1), and a constant is read only between two branches."
- Tried: I(t) = a e^{-g1 t} + b e^{-g2 t}; bend (ln I)'' vs (gap/2)^2 (1 - G^2), G = tanh(tau/2) the Smith point of the ratio, tau = gap * t. Consequence: from equal start the bend has halved when ratio = 3 + 2 sqrt2 at t*gap = ln(3 + 2 sqrt2) = 1.7627. Ratio "bend now / largest bend" needs no gap. "1 - G^2 is the transmitted fraction of the step."
- Kill: formula off by more than 1e-20 relative on random two-part fades, or half-bend ratio differing from 3 + 2 sqrt2. Opposite: three parts (expected to fail; counted).
- Numbers (out): 50 digits, 200 random fades: worst relative error 1.41e-48. Equal start, gap 0.37: bend halves at t*gap = 1.7627471740390860505 = ln(3+2 sqrt2) (all 20 printed digits); ratio there 5.8284271247461900976 = 3 + 2 sqrt2. Three parts, largest/smallest part when bend has halved: 17.056, 16.648, 14.181, 3.65, 3.613, 5.83 ("no single ratio").
- Standing: PROVED, CHECKED at 50 digits (3b). One formula for both books (READING): z(t) = e^((D gamma + i D omega) t): tau = D gamma * t climb side ("the leaf clock"), theta = D omega * t turn side ("the beat").
- Still open: "A declared drive. Nothing here supplies one."

defect_wall (DEFECT-WALL-01) — joins for holes 2 and 3, exact sympy:
- A. k + v(v + dM) = 0 exactly. B. dM + 4G^2/(1-G^2) = 0; dM + 4 sinh^2(tau/2) = 0; dM - 4 sin^2(theta/2) = 0. C. |dM| = 4 solved: z = 3 - 2 sqrt2, 3 + 2 sqrt2, G^2 = 1/2 at both. max over real v of k = d^2/4 at v = -dM/2; k = 4 has real v iff (d-4)(d+4) >= 0.
- Numeric guards: 200,000 random real (s = e^{U(-2,2)}, v uniform(-30,30)): k > dM^2/4 in 0. Unit-circle meridian: max k 3.999508, k >= 4 count 0.
- Kill: any identity leaves a nonzero remainder; random real (s,v) gives k > dM^2/4; a positive matrix with discriminant <= 0. Opposite: random positive matrix that turns (none). All passed.

---
### HOLE 4 — SIGNS (second worker; SIGNS_REPORT; four questions Q1-Q4)

**Q4: hidden_g** — see Hole 1 block above (sign of g, atoms vs knots).

**Q2: limit_m2 and limit_real (the m^2 in the commutator limits).**

Earlier lead (report): DEFECT-JOIN-01 matched the eight m = 1 limits to 4 sin^2(pi j/d), d = 6, 4, 3, 10, 14. "The values 1/2, 1/4, 1/9, phi^2/4, phi^-2/4 matched nothing." The lead d = 2q rested on 6_1, 7_2 (q = 5) and 8_1 (q = 7).

Method (limit_m2_01 header): substitute v ~ kappa/s^2 (type A) or t - 2 ~ kappa/s^2 (type B) into the exact integer Riley polynomial (sympy ring over ZZ; two-variable ring in s, v), take the leading coefficient in s -> polynomials P_A(kappa), P_B(kappa) whose roots are all candidate limits, no digits. Each irreducible factor matched to 4 sin^2(pi j/d)/m^2 at 60 digits (d <= 240, m <= 12, smallest m first).

Identities (PROVED, sympy, limit_m2_01 out): (i) v + (t-2) + dM = 0; v(t-2) - k = 0; tr(ab^-1) - 2 - v = 0. (ii) tr[a,c^m] - 2 - S_{m-1}(tr c)^2 (tr[a,c] - 2) = 0 for m = 1..6 on generic SL(2) matrices; S_{m-1}(2) = 1,2,3,4,5,6 for m = 1..6. VERIFY-SIGNS-01 re-proves (ii) for m = 1..4 (remainder 0, S at tr c = 2: 1, 2, 3, 4).

Where m^2 comes from (report, PROVED given (ii)): with c = ab (B) or ab^-1 (A), tr[a,c] = tr[a,b] and tr c -> 2, so lim (2 - tr[a, c^m]) = m^2 * k_inf. "The clock value belongs to the commutator of the meridian with the m-th POWER of c; k itself is that value divided by S_{m-1}(2)^2 = m^2." The main worker's suggestion that m^2 is the quadratic in v is NOT it; the quadratic X^2 + dM X + k = 0 gives the A/B pairing (A and B are its two roots, same quadratic as k = -v(v + dM)).

Two-term rule (written before the census run, read off p <= 41): for p/q (q odd), r = q (type B) or r = p - q (type A); if p = 2 r m +- 1 then the nonzero limits are exactly k_inf = 4 sin^2(pi j/(2r))/m^2, 0 < j < r, j = r mod 2.
- Kill: one presentation with p = 2 r m +- 1 whose exact nonzero limit set differs from the predicted set. Opposite: types swapped.
- limit_m2_01 (p <= 61, 394 presentations, 21 s): 565 clock-value factors, 473 zero factors; mismatches 0; counts: A: m=1 30, m=2 14, m=3 10, m>=4 36; B: m=1 30, m=2 16, m=3 10, m>=4 77; opposite (types swapped) 89 true / 134 false. d-candidates over 565: d = 2q (given q) holds 73; any of four forms of q 98; d = q (any form) 72; d = p 0; d = 2p 0; d divides 2q or 2(p-q) 399 of 565. 189 presentation/type pairs with nonzero limits not covered.
- limit_m2_02 (p <= 101, 1,053 presentations, 308 s): 1,696 clock-value factors, 1,470 zero, 9 "positive, no clock value". m of the clock-value factors: m=1 1195, 2 253, 3 101, 4 53, 5 30, 6 20, 7 14, 8 10, 9 6, 10 6, 11 4, 12 4. Two-term: A 84+50+24+16 = 174 all True; B 141+50+26+17 = 234 True plus 9 False. The 9 are p/3 with p = 77, 79, 83, 85, 89, 91, 95, 97, 101 (m = 13 to 17, beyond matcher cap m <= 12). Opposite 149 True / 268 False. d-candidates over 1,696: d = 2q (given q) 134 / 1,562 fail; any form of q 182 / 1,514; d = q 148 / 1,548; d = p 0 / 1,696; d = 2p 0 / 1,696; d divides 2q or 2(p-q) 1,103 / 593; d divides 2q alone 343; d divides 2(p-q) alone 760. 612 presentation/type pairs not covered.
- limit_m2_03: stopped on missing import (NameError: ring), kept. limit_m2_04: exact polynomial check of the 9: P_B = 1 - m^2 k for 77/3 (m=13: 1 - 169k), 79/3 (13), 83/3 (14: 1 - 196k), 85/3 (14), 89/3 (15: 1 - 225k), 91/3 (15), 95/3 (16: 1 - 256k), 97/3 (16), 101/3 (m=17: 1 - 289k); "exact matches: 9 of 9". Total 417 of 417.
- Standing (4b): "d = 2q" FAILED as a general rule (134 of 1,696). What holds exactly, 417 of 417 with p <= 101: if p = 2rm +- 1 with r = q (type B) or r = p - q (type A), limits are 4 sin^2(pi j/2r)/m^2, 0 < j < r, j = r mod 2. "d = 2q is true as stated only inside the two-term rule: type B with r = q, where the factor's d divides 2q. Type A uses 2(p - q)." Every one of the 1,696 nonzero limit factors is a clock value (after the 9 cap cases). Outside the two-term families the rule for d and m is open (612 presentation-type pairs at p <= 101; their d such as 4, 6, 10 "come from inner pieces of the continued fraction", with multiplicities).
- Table sample (limit_m2_01 out, factor as (d, m, [j])^multiplicity): 5/3 B (6,1,1); 7/3 A (4,1,1), B (6,1,1); 9/5 A (4,1,1), B (10,1,(1,3)); 11/3 B (6,2,1); 13/5 A (6,1,1)^2, B zero; 13/7 A (3,1,1)(6,1,1), B (14,1,(1,3,5)); 17/3 B (6,3,1); 23/3 B (6,4,1); 29/3 B (6,5,1); 31/3 B (6,5,1); 59/29 (not in p<=31 table; in real_03).

limit_real_03/04/05/06 — are the exact limits reached by REAL branches (the paper's own method KNOT-COMM-ASYM: real roots v at s = e^x, x = 12, 200 digits; limit approached to about e^-24 ~ 4e-11, so 8-digit agreement is the test):
- limit_real_03 (FAILED, kept): used never_turn_02.riley_coeffs (trims leading coefficients below 1e-25 of the largest); reported "no real branch" for 17/3 = 8_2 whose limit 1/9 is printed in Two Trees census 8.8. Also lost 41/7, 23/3, 29/5, 27/7, 47/3 and all type B of 59/29. Control failed.
- limit_real_04 (exact coefficients, v only): control 17/3 passes (1/9 REAL). 62 exact limit values tested; reached by a real branch 41. Still "no real branch" for 41/7 (3 values), 47/3 (1/64 = 0.015625), 59/29 type B (14 values), 13/5, 25/9 (value 1, multiplicity 2), 23/13 A (1, mult. 2). Cause: root finder loses the v ~ s^2 cluster.
- limit_real_05 (type A read in v, type B read in w = tr(ab) - 2): prediction (elementary) "a SIMPLE root of the limit polynomial is always reached by a real branch; a repeated root may or may not be." Kill: a simple-root value with no real branch within 1e-8, or a real band branch with 1e-6 < k < 4 away from every exact value. Tally: A simple real 47; A repeated real 4, not real 8; B simple real 55; B repeated real 4, not real 3. Kill list empty; strays empty. Time cap reached before 41/7 (400 s).
- limit_real_06 (41/7, 47/3, 59/29 only): 41/7 B (14,3,1),(14,3,3),(14,3,5) real; 47/3 B (6,8,1) real; 59/29: all 14 type A real (types incl. (3,1,1), (6,1,1), (5,1,1), (5,1,2), (10,1,1), (10,1,3), (30,...)) and type B 18 values real in the tally (A simple real 14, B simple real 18). Kill list and strays empty.
- Standing (report): simple roots: 134 of 134 reached by a real branch (102 in real_05, 32 in real_06). Repeated roots: 8 reached, 11 not. Example: 6_3 = 13/5 has (kappa - 1)^2 in type A and no real branch, "which is why it never turns". "No real band branch sits away from an exact value." 59 presentations, p <= 25 plus seven larger (35/29, 39/29, 31/13, 29/17, 41/7, 47/3, 59/29).
- Open: general rule for d and m outside the two-term families; "Why the m = 1 value is the clock 4 sin^2(pi j/2r): untested here."

**Q3: never_census / never_rule / never_golden / never_border (which two-bridge knots never turn).**

never_census_01 (superseded, kept): exact integer coefficients, sign-change pass first, roots second at 80 digits (v for x <= 1.5; v and w for x >= 2). Chunks p 3-37: 87 knots, TURN 60, NEVER 27 (including torus 3..37); p 39-49: 59 knots, TURN 48, NEVER 11 with TURN "by roots only" 47/9, 49/9, 49/17 at x = 4.0; p 51-57: 44 knots, TURN 39, NEVER 5, roots-only turns 53/5, 53/17, 55/21 at x = 3.5. These six are the false turns later withdrawn.

never_census_02 (repaired): root-finder-free pass 1 (sign change of exact polynomial along half band, uniform + logarithmic points, 240 points + 159 log points); pass 2 (only if pass 1 silent at every x) 80-digit roots in both views; a root-only hit needs a sign change at 160 digits across r(1 -+ 1e-6) else "UNCONFIRMED". CONTROL/KILL: Two Trees census 8.8 must give 19 turn / 7 never. Torus knots p/1 run only for p <= 21 (control, all never; centre argument of Two Trees Thm 8.7 for all p).
- Chunk results: p 3-45: 111 knots, TURN 88, NEVER 23 (10 torus); p 47-55: 52, TURN 45, NEVER 7; p 57-63: 47, TURN 41, NEVER 6; p 65-69: 40, TURN 35, NEVER 5; p 71-75: 45, TURN 41, NEVER 4. No roots-only turns; no unconfirmed hits (all chunks).
- Report totals: all two-bridge knots p <= 75 up to mirror and q <-> 1/q: 285 non-torus; 250 TURN, 35 NEVER (sum of chunks: 295 knots, 10 torus; matches).
- Control: census 8.8 reproduces 19 turn / 7 never; nine-crossing additions 27/5, 29/9, 55/21 reproduce (report). 43/5 NEVER (earlier 40-digit false turn).
- **The 35 non-torus never-turners:** 13/5, 17/5, 23/5, 25/9, 27/5, 29/9, 33/5, 37/5, 37/13, 41/9, 41/13, 43/5, 43/9, 47/5, 47/9, 49/9, 49/17, 53/5, 53/17, 55/21, 57/5, 59/9, 61/9, 61/21, 63/5, 63/13, 65/9, 65/21, 67/5, 67/9, 67/13, 71/21, 73/5, 73/25, 75/29. Continued fractions printed, e.g. 13/5 [2,1,1,2], 17/5 [3,2,2], 55/21 [2,1,1,1,1,1,2], 71/21 [3,2,1,1,1,2], 75/29 [2,1,1,2,2,2].
- Real-root-free grid x = 0.1..1.5 step 0.1, then 2, 2.5, 3, 3.5, 4 (XS order in the scripts starts 0.8, 0.5, 1.2, ...).

never_border_06: the three never-turners flagged with a near-real complex pair in the half band (37/13, 61/21, 63/13) re-run at 160 digits. Kill (for NEVER): a real band root at 160 digits at any grid x, or an imaginary part dropping by more than a factor 10 between 80 and 160. Out: real band roots 0 at both; smallest log10 relative |Im| identical at 80 and 160: 37/13 -8.6855 (at x = 4.0); 61/21 -15.6342 (x = 4.0); 63/13 -8.6855 (x = 4.0). "true complex pair. NEVER stands."

never_rule_03 (rules scored on 285 knots; T1, T2, R3 written before the run, read off p <= 55):
- T1 (one-way): Alexander polynomial has a real positive root -> TURN. Reason given: at s^2 = root the real slice passes through a reducible representation (v = 0, k = 0) and v changes sign, so the band is entered at x = (1/2) ln(root). Result: applies to 141 knots, TURN 141, NEVER 0. Matches entry points printed in Two Trees census 8.8: 6_1 at x = 0.350 vs (1/2) ln 2 = 0.347; 8_1 at 0.285 vs (1/2) ln((7 + sqrt13)/6) = 0.285 (report: arithmetic on printed values, not a new run). "Checked, not proved here."
- T2 (one-way): a limit polynomial P_A or P_B has a nonzero root of odd multiplicity -> TURN (a real branch stays in the band as x -> infinity). Applies to 195, TURN 195, NEVER 0. T1 or T2 together decide 232 of 285; undecided 53 = 35 NEVER + 18 TURN (the 18: 29/11, 33/23, 37/11, 45/17, 51/11, 51/35, 53/19, 53/37, 57/17, 59/11, 59/23, 61/19, 61/23, 65/47, 65/51, 69/47, 73/11, 73/51).
- **R3 (two-way, non-torus): NEVER iff p/q = a +- 1/(b + 1/c), a odd >= 3, b and c even >= 2, a > c.** In ordinary continued fractions: [a, b, c] and [a-1, 1, b-1, c]. Predicts 32; all 32 never; 0 wrong; misses 3 (55/21, 71/21, 75/29); 282 of 285. By sign and range: "+" p<=55: 9, "-" p<=55: 10, "+" p>55: 6, "-" p>55: 7 (all True).
 - R3 opposite (a < c): predicts 16, 7 right, 9 wrong (31/7, 45/7, 47/11, 55/13, 59/7, 69/11, 71/11, 71/17, ...; script prints first 8); 248 of 285.
 - R3 without a > c: predicts 41, 32 correct, 9 false; 273 of 285.
 - Earlier families: [a,2,2] a odd: 6 of 6, misses 29 (256 right); [a,1,1,2] a even (= a+1 - 1/(2+1/2)): 7 of 7, misses 28; [a,m,2] m even: 13 of 13, misses 22.
 - Non-separating features (value: NEVER / TURN): p mod 4: 1 -> 20/123, 3 -> 15/127; p mod 8: 1 12/63, 3 8/66, 5 8/60, 7 7/61; p prime: 23/144 vs composite 12/106; q^2 = +1 / -1 / other mod p: 1/12, 2/10, 32/228; palindromic cf: 3/5 vs 32/245; last cf entry even: 35/138 and odd 0/112 (one-way); parity pattern: "oee" 15/0, "eooe" 17/4 (best 4 wrong); signature 0: 7/58 vs 28/192; |sig| = 2 genus: 15/82 vs 20/168; all Alexander roots on unit circle: 17/84 vs 18/166; real negative Alexander root: 0 of 285; genus 1: 0/62.
 - "No real Riley root in the turning range" is the definition and cannot be scored separately.

never_rule_04 (R3 outside the range it was read from, 77 <= p <= 101; capped): R3 predicts NEVER for 25; sign change found in 0 of 25 (80 digits, re-evaluated at 160). 11 near misses (a <= c) predicted TURN: turns proved in 7 of 11 (79/19, 81/13, 87/7, 91/11, 93/11, 95/23, 101/7, all at x = 0.8); 4 silent (77/9, 83/5, 93/5, 95/9), each of which also has a qualifying R3 form. Root finder run on only 4 knots (77/5, 77/9, 97/21, 99/29) and only x = 0.5, 0.8, 1.2, 2.0: no confirmed real band root; no near-real pairs. Kill: any sign change in (i), any silent near miss counted against R3 (reported), any confirmed band root in (iii). "For p > 75 'never' is not established, only not contradicted." R4 predictions 97/21 = 5 - 8/21 and 99/29 = 3 + 12/29: sign scan silent.

never_rule_05 (R4, written after R3 missed exactly 55/21, 71/21, 75/29, so those three are FITTED): NEVER iff p/q = a +- 1/E, a odd >= 3, E = [e1, ..., e_2n] continued fraction with even entries, even length, entries pairing up by sign (e1 e2 > 0, e3 e4 > 0, ...; sign may change only between pairs), e1 > 0, and for n = 1 the size clause a > e2. No size clause known for n >= 2. Out: n = 1 predicts 32 never, 32 never, 0 turn; n = 2 predicts 3 (55/21 = 3 - 1/[2,2,-2,-2]; 71/21 = 3 + 1/[2,2,-2,-2]; 75/29 = 3 - 1/[2,2,2,2]), all never; n = 3: none; all n: covers 35 of 35, missed [], false positives 0. Opposite (unpaired sign patterns): n = 1 predicts 69 never, 8 never / 61 turn; n = 2: 64, 8 never / 56 turn (the 8 are knots that also have a paired form). Predictions for 77 <= p <= 101: 97/21 and 99/29 (untested except capped never_rule_04).

never_golden (NEVER-GOLDEN-03): exact coefficients; sign change of exact polynomial at 200 and again 400 digits. Guess under test: n = 2, 5, 8 never; n = 0, 3, 6 turn. Out:
 - n=2, 13/5 (degree 6): no sign change (NEVER per census). n=3, 21/13 (degree 10): TURN, x = 0.8 in w, 2 changes at 200 and 400 digits, bracket r in (0.0289202, 0.0315493), k ~ 0.09854. n=5, 55/21 (degree 27): no sign change (NEVER per census). n=6, 89/34 (as 89/55, degree 44): **TURN**, x = 0.8 in w, 3 changes at 200 and 400 digits, bracket r in (0.00210358, 0.00262911), k ~ 0.008288. n=8, 233/89 (degree 116): no sign change on grid at 200 digits; not decided.
 - Direct test of the NEVER-TURN-05 band point of 233/89 (x = 0.8, v = 1.1301089, k = 2.288): sign of exact Riley polynomial at v(1 - 1e-4) and v(1 + 1e-4): +1, +1 at 200 digits and +1, +1 at 400 digits -> not a root.
 - R4 membership: 13/5 = 3 - 1/[2,2] paired -> NEVER; 21/8 = 3 - 1/[2,2,-2] unpaired -> TURN (this is the odd-q presentation of 21/13 per the script); 55/21 = 3 - 1/[2,2,-2,-2] paired -> NEVER; 89/34 = 3 - 1/[2,2,-2,-2,2] unpaired -> TURN; 233/89 = 3 - 1/[2,2,-2,-2,2,2] paired -> NEVER (untested).

verify_signs (VERIFY-SIGNS-01..05, main worker's independent check, shares no code with the second worker):
- Check 1: Chebyshev identity remainder 0 for m = 1..4. Check 2: 89/34 TURNS: relation w a = b w built directly from the two-bridge word, signs e_i = (-1)^floor(i q/p), all four matrix entries at 120 digits; convention validated on figure-eight 5/3 at v = 0 (residual 0.0 at s^2 = Alexander root; 0.718 at s = 1.3).
- 01: scanned only 0 < v < 0.02 on one entry; found 0 band points (wrong region).
- 02: scanned whole band 0 < v < -dM on every entry at x = 0.8 (-dM = 3.15492894239) but used q = 34 (even) in an odd-q word formula, so tested the wrong word; 0 roots.
- 03 and 04: switched to odd q = 55 (89/34 = 89/55 up to mirror); both crashed with ZeroDivisionError in mpmath's root polisher (anderson, then illinois); outputs are tracebacks.
- 05 (plain bisection, 130 digits, odd q = 55): x = 0.8: 3 sign changes, real band roots at v = 2.98638431427445283 (tr(ab) - 2 = 0.1685446281, k = 0.5033390337), v = 3.13863223271297524 (0.01629670968, k = 0.05114937828), v = 3.15246785369279845 (0.002461088697, k = 0.007758503002); all-entry residuals 4.96e-129, 7.5e-128, 1.72e-127. x = 1.2: v = 9.02518587896350025 (k = 0.8006102951), 9.11282563615208679 (k = 0.009738856517), 9.11388014097768898 (k = 0.0001293528755); residuals 1.94e-126, 9.8e-126, 1.97e-123. Kill: no bracketed root in the band, or other entries not vanishing (> 1e-80). Survived.
- FOUR_HOLES v2 Correction: 89/34 "was recorded as a never-turner at 120 digits. It turns." Cause: earlier script dropped tiny leading coefficients. "The 'band points' reported for 233/89 were not roots. The golden-family guess ... is alive again; 233/89 is undecided."
- The report adds: "A never verdict would need the root finder at degree 116, which was not run."

**Q1: split signs (equal or opposite at the 199 split roots; split_signs_01/02).** Included for completeness because it is hole 4.
- List rebuilt (KnotInfo via database_knotinfo): 199 nullity-2 double roots, one per knot; 81 equal (jump -4: 73, +4: 8 — printed as signature-at-root minus before: -2 73, +2 8), 118 opposite. 193 of 199 are factor t^2 - t + 1; the other six: 2t^2-3t+2 (2 equal), 3t^2-5t+3 (1 equal), three quartics (1 opposite each). 22 nullity-2 roots of multiplicity 3 to 5 outside the list.
- Kill conditions written first: A any disagreement between recomputed and KnotInfo label; B a candidate separator only if no value holds both labels; C arithmetic prediction killed by one knot of its clean stratum on the wrong side.
- Part A CHECKED 199 of 199; for 193 roots at zeta6 the discriminant d computed exactly over Q(sqrt -3): equal iff d > 0, 193 of 193 (78 equal d>0, 115 opposite d<0) — "the definition re-checked on a third column, not a finding."
- Part B tables (equal / opposite): second Alexander multiplicity 1: 81/118; root-of-unity order 6: 78/115, not roots of unity: 3/3; signature before root mod 4: 0: 50/84, 2: 31/34; signature before: -2 31/23, 0 50/84, 2 0/11; knot signature: 0: 0/62, -2: 5/14, 2: 1/21, -4: 31/11, 4: 5/7, -6: 19/1, 6: 2/2, -8: 16/0, -10: 2/0; Delta = f^2: 1/11 vs 80/107; unit-circle roots of cofactor: 0 34/62, 2 27/35, 4 18/18, 6 2/3; alternating Y 43/63, N 38/55; symmetry: amphichiral (all kinds) 0/11, reversible 58/69, chiral 23/38; concordance order: 1: 0/13, 2: 0/7, 4: 0/1, infinite 21/16, not listed 60/81; four-genus 0: 0/31, 1: 0/66, 2: 40/18, 3: 18/3, 4: 18/0, 5: 5/0; fibered Y 30/74, N 51/44. Sweep of every KnotInfo field with <= 40 values: no perfect separator; best is double slice genus, 20 on the minority side. Connected sums K#K vs K#mirror: "no instance: KnotInfo lists prime knots only".
- One-way rows (reproductions through signature bounds, not findings): amphichiral, finite concordance order, four-genus <= 1 force opposite; knot signature 0 gives opposite 62 of 62 (not forced by a bound they ran; CHECKED on this list only).
- Why simple candidates cannot work (READING, standard): K#K and K#mirror(K) have the same Alexander module and opposite labels; "The separator has to see the form, not the module."
- Part C arithmetic separator (factor t^2 - t + 1): prediction as first written from Hilbert reciprocity for (d, -3): sign of d = chi3(unit part) * prod over p = 2 mod 3 of (-1)^(v_p(d)); inputs: linking form of double branched cover on its 3-part (from V + V^T) and primes p = 2 mod 3 at odd power in g(zeta6), g = Delta/(t^2 - t + 1)^2; signature function not used. First form KILLED: 127 of 137 in clean stratum (3 not dividing g(zeta6)); all 10 misses at g(zeta6) = +-2. (Also: primes p = 2 mod 3 at odd power in d agree with those in g(zeta6) in 178 of 193; mine, from the .out.) Repair made after seeing misses: corank of V^T - omega V over F_4 (omega primitive cube root of unity, prime (2, t^2+t+1)); corank 2 -> (-1)^(v_2(g)); corank 3 -> +1. Repaired rule clean stratum: 137 of 137 (43 equal rule +1, 94 opposite rule -1); 115 of 115 on knots with v_2(g) even, 22 of 22 on the 22 knots with v_2(g) odd it was read from. Opposite (correction inverted): 115 of 137. Second setup (3 divides g(zeta6)): 31 of 54 and 1 of 2: FAILS. Failure condition: "the double cover's 3-part mixes the two levels with the cofactor's 3-part." Rule (clean stratum): equal sign exactly when chi3(product of the two 3-part units) x (-1)^(# odd primes p = 2 mod 3 at odd power in g(zeta6)) x (-1)^(v_2(g(zeta6)) if F4-corank is 2) = +1. F_4 corank vs v_2(g) tally: (v2, corank): (0,2) 146, (1,2) 16, (1,3) 15, (2,2) 14, (3,2) 2. Full list: rule correct on 137; 56 with 3 | g(zeta6); 6 other factors.

---------------------------------------------------------------------
## 4. FAILED OR SET ASIDE (with failure conditions)

From EQUATION_FILE_ENTRY_20261110_four_holes_v1.md (8 items; "kept, not discarded") and FOUR_HOLES v2 "Set aside" (7 items, grouped differently):
1. Optical wall energy E_wall(element) from the ladder: |rho| < 0.5 on IE1, z1, valence sum (+0.06, -0.28, +0.26; n = 30). Diverted to optical phase (5 of top 6, p = 2.7e-6).
2. "Stretch only toward white" in three channels: dphi = (1/2) sech(tau/2) d tau forces it for two channels (22 of 22); fails for three: 3.0-3.4% of away passes stretch (Exner weights).
3. "Half line = shell opening": 8 of 694 closed-core openings beyond z = 3 + 2 sqrt2; bare limit z = 4 inside.
4. "d = 2q" for commutator limits: fails 134 of 1,696 (holds); survives only as r = q in the two-term rule p = 2rm +- 1.
5. "g negative real on knots": fails, 4 of 45 hold; g complex (Whitehead family +-i pi/2, +-pi/4).
6. "Pole of the knot fit at -1/(cusp shape)": fails, 1 of 45.
7. Split-root sign from reciprocity, first form: fails 127 of 137 correct (10 misses, all at g(zeta6) = +-2); repaired with an F_4-corank term (fit on 22 knots, tested on 115). Fails where 3 divides g(zeta6): 31 of 54.
8. Coefficient trimming in never_turn_02-05: leading coefficients below 1e-25 of the largest were dropped; real branches lost. "89/34 'never' withdrawn (it turns); 233/89 'band points' withdrawn."
Also recorded as failed in scripts: limit_real_03 (trimming), limit_real_04 (v-only polyroots loses the v ~ s^2 cluster; missed 41/7, 47/3, 59/29), never_census_01 six false roots-only turns (47/9, 49/9, 49/17, 53/5, 53/17, 55/21; 47/9 at 80 digits spurious real root v ~ A, k ~ 4e-10, none at 160 or 320), the 40-digit false turn of 43/5, R3 opposite (a < c) killed (7 right, 9 wrong), R3 without a > c killed (9 false nevers), R4 opposite killed (unpaired signs), d-candidates d = q, p, 2p, 2q killed, limit_m2_03 (import error), verify_signs_02 (wrong word), 03/04 (crash).
- Not a set-aside but killed in Q4 of report: knots "g negative real" and "pole at -1/tau".

---------------------------------------------------------------------
## 5. OPEN QUESTIONS THE SOURCE ITSELF LISTS

FOUR_HOLES v2 "What is still open after this round":
- A length for colour and a drive for time: "the same missing calibration".
- The knot side of the half-line bridge ("no atom-to-knot map is claimed").
- Commutator limits outside the two-term families; proof of R3; the size clause of R4; 233/89.
- Split roots where 3 divides g(zeta6).
- Colour paper Appendix 16 not read line by line; "VOTKP v2.9 later sections, UPG in full, June originals still unread."
SIGNS_REPORT additionally:
- Q1: no rule for the 56 roots where 3 divides g(zeta6) nor for the 6 roots at other factors (2t^2-3t+2 twice, 3t^2-5t+3, three quartics); whether the F_4-corank correction is right at other inert primes (5, 11, ...) untested; on all 199 no separator is perfect or near-perfect.
- Q2: general d, m rule (612 presentation-type pairs); why the m = 1 value is the clock 4 sin^2(pi j/2r).
- Q3: proof of R3; size clause of R4 n >= 2; T1 given with a reason, checked not proved; whether a knot that turns always stays in the band as x -> infinity "was not tested beyond the paper's 26".
- Q4: the original fitted kappa, g, d (if from another family, name it); only (1,a) and (a,1) fillings of four links run.
FOUR_HOLES v1/v2 hole 3: "A declared drive. Nothing here supplies one." Hole 2: a length (retardance in nm) for colour.

---------------------------------------------------------------------
## 6. ELEMENTS HOOKS

- **Alkali metals and francium.** FOUR_HOLES 1a (v1 and v2, line "First step of the alkali atoms"): Li 14.03, Na 9.20, K 7.29, Rb 6.53, Cs 5.95 beyond z = 5.828; "Fr 5.50 is inside". Source: ladder_wall_01.out core N=86: largest z 5.50 (Z=87), 0 beyond; core N=54: 5.95 (Z=55), core N=36: 6.53 (Z=37), N=18: 7.29 (Z=19), N=10: 9.20 (Z=11), N=2: 14.03 (Z=3). Francium has no optical track in the phase test (41 elements) and no E_wall.
- **Alkali optical phase** (PHASE-LADDER-02 / FOUR_HOLES 1c): five atoms beyond the half line on the ladder hold 5 of the top 6 optical phases at 1.5, 2.0, 2.5 eV; p = 2.7e-06 each; order reversed within the five (Cs > Rb > K > Na > Li by phase; ladder z Cs 5.95 < Rb 6.53 < K 7.29 < Na 9.20 < Li 14.03). Even reading |G|^2: p 0.091 / 0.099 / 0.099. Caution in the source: five atoms; alkalis are the lowest-plasma-energy free-electron metals.
- **The wall Gamma^2 = 1/2 / z = 3 + 2 sqrt2** appears in: DEFECT-WALL-01 (|dM| = 4), TIME-WALL-01 (bend halves at ratio 3 + 2 sqrt2, t*gap = ln(3 + 2 sqrt2) = 1.7627471740390860505), LADDER-WALL-01, PLASMA-WALL-01 (R = 1/2 is the half line on the disk), PHASE-LADDER-02.
- **Shells and the bare K-shell limit**: LADDER-WALL-01 header and FOUR_HOLES 1a: VOTKP Thm 8.2 hydrogen-like shell wall G_sh = (2n-1)/(n^2 + (n-1)^2), z -> (n/(n-1))^2, n = 2: z = 4, G = 3/5, G^2 = 9/25 < 1/2. Observed K-shell opening z: Li 14.03, Be 8.45, B 6.84 (6.838), C 6.08, N 5.64 (inside), O 5.353, F 5.151, Ne 5.001, Na+ 4.886 (Z=11), Mg 4.794, Al 4.719, Si 4.657 ... down to smallest 3.888 at Z = 103. Be, B, C beyond the line (the other three of the eight).
- **Screening / metals vs non-metals**: LADDER-WALL-01 header ("any step beyond it is beyond because of screening"); FOUR_HOLES 1a ("only when one electron sits alone outside a closed core and the core screens it well"); HIDDEN-G-01 report line ("also what plain screening gives"); FOUR_HOLES headline "vacuum-disk metal / non-metal line (35 of 35 against 0 of 6)" (earlier record, not re-derived); PLASMA-WALL-01 (R = 1/2 as metal line, "mean visible |G|^2 separates metals from non-metals at 1/2" from the vacuum-disk paper). Never above 1/2: B, Se; no final crossing: Be, Cr, Ge, In, Mo, Na, Os, Rh, Zn.
- **Ionisation ladders**: LADDER-WALL-01 (109 elements, 5,737 steps), HIDDEN-G-01 (98 isoelectronic families N, a = Z, pole d near N). kappa near 1 in 55 of 62 counted; N = 2: kappa 3.9151 (bare 4); N = 10: 2.0984 (bare 2.25); pole sits at the neutral point (median d - N = -0.22; |d - N| < 1 in 54 of 62).
- **Colour of matter**: COLOUR-PEEL series is about colour as a sphere of shares (not atoms). FOUR_HOLES 2e: crossed fraction 1/4 at the trefoil walls ("the crystal is the defect"); "a colour needs a length (retardance in nanometres)". Exner luminous weights 43.33, 32.76, 1.
- **The rim |Gamma| = 1**: not named in these files. The climb line has Schrodinger length pi (2a).
- **5/8, "space between"**: not present in these files (grep for "5/8" and "space between" found nothing).
- **Optical tracks used**: refractiveindex-style database at /home/claude/data_ri_repo/database/data/main (yml "tabulated nk"), per element best-spanning track covering 0.38-0.78 micron; 41 elements. Thresholds file: votkp-lean/data/element_thresholds_20261011.json.gz (118 elements).

---------------------------------------------------------------------
## 7. CONTRADICTIONS OR SLIPS (not fixed)

1. **Value of k for 89/34 at x = 0.8.** SIGNS_REPORT and NEVER-GOLDEN-03: "k ~ 0.0083" (0.008288 is the k at the right end of the bracket r in (0.00210358, 0.00262911)); VERIFY-SIGNS-05: roots with k = 0.5033, 0.0511, 0.00776 (0.007758503002); FOUR_HOLES v2 says "k = 0.5033, 0.0511, 0.0078". verify_signs_01 header also says "k near 0.0083". The two numbers are for different things (bracket end vs root), and NEVER-GOLDEN-03 prints the bracket only.
2. **Sign of "defect" delta.** FOUR_HOLES/UPG call delta = |lambda - 1|^2 (positive, delta + g^2 = 4). The script dM = 2 - (s^2 + s^-2) is -4 sinh^2(tau/2) (negative) on the real climb and +4 sin^2(theta/2) on the turn circle. The headline says |delta| = 4; "k reaches 4 iff |dM| >= 4" requires dM <= -4 (climb), since dM <= 0 for real s and dM in [0, 4] on the unit circle. As printed, the positive form |lambda - 1|^2 equals dM only for unimodular lambda.
3. **v2 internal grade for time.** Headline says "CHECKED to 20 digits" for the bend; section 3b says "CHECKED at 50 digits". The script prints worst error 1.41e-48 over 200 fades (50 digits) and the half-bend time to 20 digits; both statements are true of different parts.
4. **Colour percentages.** FOUR_HOLES 2c "5.0-5.8% toward-white, 3.0-3.4% away" includes the "Exner reversed" run; the three Exner seeds give 4.97-5.59% and 3.25-3.36%.
5. **LADDER-WALL header sentence** "in the bare limit NO shell opening reaches the half line except n = 1 -> none" is garbled in the script; the intended content is the n = 2 value z = 4, G^2 = 9/25.
6. **"One electron alone outside a closed core"** (FOUR_HOLES 1a conclusion) does not describe Be, B, C (K-shell opening with two electrons left, beyond the line with z 8.45, 6.84, 6.08) even though the same paragraph lists them among the 8. The 8 steps: Li is both a first alkali step and an N=2 opening, so "Li, Na, K, Rb, Cs first steps" and "Be, B, C K-shell openings" are 5 + 3 = 8 only because Li is counted once.
7. **Borderline re-check scope.** never_border_06 re-ran only 37/13, 61/21, 63/13 ("flagged three"). The census_02 chunks also flag 49/17 (log10 |Im| -12.2, -10.6, -9.1, -7.6) and 73/25 (-19.1, -16.7, -14.3, -11.9) as NEVER with a near-real pair; these were not re-run at 160 digits in this folder (the report mentions only the three). Also the census_01 chunk had several other borderline NEVERs (13/5, 23/5, 25/9, 33/5, 37/13, 41/9, 43/5, 43/9) around 1e-8.4 to 1e-11.9.
8. **limit_m2_01 header mentions "part 5 checks samples at 200 digits"**; that part is not in the script, it is limit_real_03..06.
9. **Report vs script file locations**: SIGNS_REPORT says scripts are in /home/claude/work/agent_signs/; scripts import from that path and never_turn_02.py in /home/claude/work/ (not in this folder). limit_real_03 execs never_turn_02.py which is not in the folder; the main folder lists only round4/ files.
10. **verify_signs 01-04** are failed runs preserved; FOUR_HOLES v2 cites only VERIFY-SIGNS-05.
11. **v1 vs v2.** v1's Hole 4 is a placeholder ("summarised below when returned"); v2 fills it. v2's set-aside list has 7 items; the equation-file entry has 8 (pole-of-fit and g-real are separate items there, combined in v2 item 5; trimming is item 8 there, 7 in v2).
12. **Report's "Hole 4 q2 (a) table first row**: "d = 2q (the given q) holds 134" counts clock-value FACTORS, not presentations; the 417 figure counts presentations.
13. **Two uses of "m".** The report's Q2 limits use m = order of the c-power; limit_m2 matcher cap m <= 12 produced 9 apparent mismatches (all p/3, m = 13..17).
14. **R3 in the golden family**: report table says R4 at n = 3 gives "turn" because 21/8 = 3 - 1/[2,2,-2] has length 3 (odd). But 21/13 is the knot; the script labels "n=3 21/8 = 3 - 1/[2,2,-2]" whereas elsewhere the knot is called 21/13 (21/8 is its q -> p - q form: 21 - 13 = 8). Not an error, just two presentations.
15. **PLASMA-WALL-01 carbon value**: C E_wall = 0.10 eV and Si phase@2eV = 0.1 degrees appear in the table (range for C 0.01-29998.5 eV, for Si 0.00-40.0 eV); not commented in the source. Treated as data.

---------------------------------------------------------------------
## 8. THINGS A LATER READER WOULD WALK PAST

1. **E_wall ordering among alkalis matches the ladder step ordering** (mine, arithmetic on printed PLASMA-WALL-01 numbers; not stated in the source): E_wall Cs 2.50 < Rb 3.28 < K 3.85 < Li 5.12 eV (Na has no final crossing) and z1 Cs 5.95 < Rb 6.53 < K 7.29 < Li 14.03. Both increase together within the alkalis, while the 30-element Spearman is -0.28 (so the ladder-wide failure is outside the alkalis). The source only reports the global failure and the reversed order of phase.
2. **Phase at 2 eV against z1 is rho = +0.545 (p 0.00183) over 30 elements**, against IE1 -0.436, valence sum -0.584 (plasma_wall_01.out last three lines); this is where the diversion to optical phase began (PHASE-LADDER-02 header: "its opposite ... gave rho = +0.545 with z1").
3. **The opposite reading in HIDDEN-G-01 flips every sign**: z -> 1/z gives g > 0 in 61 of 61 counted; so "g < 0" is a statement about the direction of the step (upward ratio of larger/smaller IE), not about atoms alone. The knot side has no such direction fixed.
4. **The 8 beyond-line closed-core steps appear in only five core classes** (N = 2: Z = 3-6; N = 10: Z = 11; N = 18: Z = 19; N = 36: Z = 37; N = 54: Z = 55). Cores N = 28, 46, 60, 68, 78, 86 have no step beyond the line though N = 86 (Fr) reaches 5.50, "inside". The K-shell opening z falls monotonically with Z: 14.029, 8.451, 6.838, 6.08, 5.64, 5.353, 5.151, 5.001, 4.886, 4.794, 4.719, 4.657 toward "bare 4" (smallest 3.888 at Z = 103, below the bare limit 4).
5. **kappa in the atom families is near 1 almost everywhere (55 of 62)** while the closed-core families N = 2 and N = 10 give kappa 3.9151 and 2.0984 (near bare 4 and 2.25) — the fitted constant behaves like the bare shell-wall for the first two shells only; N = 18, 36, 54, 60, 86 give 0.952, 0.974, 0.900, 0.980, 0.773 (bare given for 28 and 60 only).
6. **Colour: the 955-of-20,000 count is a property of the luminous weights, not the geometry.** Unit weights: 0 of 20,000 in all three seeds and in COLOUR-PEEL-01 and -02. With Exner reversed (1, 32.76, 43.33): 936; with (10,10,1): 220. So the effect scales with weight imbalance (all three of these facts are only in colour_peel_03.out).
7. **Two-channel Schrodinger stretches are rare** (22 of 20,000 close pairs in setup 1; 7 of 20,000 in setup 2) and all toward white; the three-channel stretches need weights.
8. **T1 mechanism and census entry points**: a knot with a real positive Alexander root enters the band at x = (1/2) ln(root) (6_1: 0.350 vs 0.347; 8_1: 0.285 vs 0.285), stated once in never_rule_03.py header and the report's "Still open" block.
9. **The 3 R3 misses 55/21, 71/21, 75/29** all have continued-fraction signs/forms with a 4-entry even block; they are exactly the three R4 n = 2 instances, i.e. R4 n = 2 was fitted to these (never_rule_05 header). 55/21 is the n = 5 member of the golden family.
10. **Silent knots for p > 75 are not proofs**: never_rule_04 only shows no sign change; the report says "never" is "not established, only not contradicted".
11. **Opposite-test counts hide in outputs**: R3 opposite 9 wrong of 16; R4 opposite 8 never in 69 and 8 never in 64 are knots that also have a paired form.
12. **Simple vs repeated limit roots**: 134 of 134 simple limit values reached by real branches; repeated roots 8 reached, 11 not (limit_real_05 tally: A repeated 4 real / 8 not; B repeated 4 / 3). 13/5, 25/9, 23/9 (^4), 25/11 (A (10,1,1)^2, (10,1,3)^2) have repeated limit roots with no real branch; 19/7 and 29/17, 31/13 have repeated roots with real x2 branches.
13. **limit_m2_01 out shows 9/5, 11/5, 13/7 ... 2-term examples**, e.g. 11/5 A (3,1,1) and (6,1,1) and B (10,1,(1,3)); 59/29 = [2, 29] has 14 type-A limits (3,6,5,5,10,10,30 x4,15 x4 values) reached by real branches while its 14 type-B limits 4 sin^2(j pi/58) are real only in the w-polynomial (limit_real_06): the type-B no-real-branch verdict in limit_real_03/04 was a root-finder artefact.
14. **The hole-4 corank table**: (v2g, c4) counts (0,2) 146, (1,2) 16, (1,3) 15, (2,2) 14, (3,2) 2 only in split_signs_02.out.
15. **HIDDEN-G-03 prints dz/du = -g tau/(2 pi i)** for each tetrahedron; for L5a1 cusp 1 the four printed values are -0.5001-0.5001i, -0.2501+0.2501i, +0.2501-0.2501i, +0.5001+0.5001i. The file gives no interpretation of them.
16. Memory used: none of the stored user facts were needed for these notes beyond the brief; nothing in the files asked for any action outside reading.
