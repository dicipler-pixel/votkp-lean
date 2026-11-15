# NOTES 04: Tree, Ball and Light mixer (Light mixer) and The Standard Model in the Ball (SM ball)

Reader notes, 11 Nov 2026. Both pages are by Jeromie Beasley, three.js mixers on Garrett's ratio-5 tree in the Poincare ball (radius RB = 4). "LM" = Light mixer text file, "SM" = SM-ball html. Line numbers: LM = lines of Tree_Ball_Light_Mixer_own_code.txt; SM = lines of The_Standard_Model_in_the_Ball.html. Unicode escapes in LM (Γ etc.) decoded here. Everything below is what the code and text say; I ran small independent python checks (marked "my check") and judge nothing.

## 1. COVERAGE

- LM text file: 236,662 chars, 3,817 lines (3,818 incl. final empty). Structure found:
  - lines 1-46: page head, CSS, panel HTML (incl. the "Models, sources and executed checks" details block, line 45). Read in full.
  - lines 47-3792: NOT the page's own code. It is leftover three.js library (GLSL shader chunks, lines 47-3570; minified three.js lines 3571-3792 incl. 3650/3684/3708 post-processing and bloom classes). I did not read these character by character (192,413 chars). I scanned all of them with keyword searches (Garrett, Koide, twin, Jeromie, SU(3), rapidity, helicity, ln 5, Gamma, tanh, wall, Higgs, oscillator, tune-out, phase, Smith, Snell, Drude, Lorentz, reflect, optical). The only hits were stock three.js (reflectedLight, refract, V_GGX_SmithCorrelated, an iridescence "phase" in lines 183-188). No own data or maths in that region.
  - line 3793 (11,671 chars): tail of three.js (OutputPass class, first ~700 chars) then ALL the page's own code starts at "var xo=[{n:"e"..." (particle table) ... through its first eye (end) title/grade/eq. Read in full in 6000-char slices.
  - lines 3794-3805: rest of own code (eyes end, particles, wall, higgs, light, response, stage/loop). Read in full.
  - lines 3806-3817: three.js licence comment, closing tags. Read.
  - Not available: the three data: links in line 45 (math_tests.py, math_report.json, math_review.md) are "data:REMOVED" so their contents are not in the file. The original html (/home/claude/in/html/Tree_Ball_Light_Mixer.html) was not opened (not needed; nothing was unclear).
- SM html: 34,685 chars, 294 lines. Read in full (whole file via Read; no line truncated).
- My independent checks (python3 -I, nothing from the files executed): compared the two stored ROWS tables numerically; recomputed Koide cos^2, the six mass ratios, the slope, the first/last-10 means, the twin-prime word, the commutator trace formula in 2x2 and 4x4.

## 2. OBJECTS AND DEFINITIONS

### 2.1 Shared geometry (identical in both pages)
- Ball radius RB = 4 (SM line 86; LM var Ot=4). Arms i, j, k drawn as (x, -z, y): AI=(1,0,0), AJ=(0,0,-1), AK=(0,1,0); DIAG = normalize(AI+AJ+AK) (SM 102). Arm colours 0xff8d7c, 0x63d3ff, 0xf2c14e. Comment: "to match the One Tree, One Ball mixer" (SM 101).
- Step rapidity rap = ln 5 (SM 114). Hyperboloid point v=(v0,v1,v2,v3), start O=(1,0,0,0).
- Boost of a hyperboloid point along axis ax by r: v0' = cosh r v0 + sinh r v[ax+1]; v[ax+1]' = sinh r v0 + cosh r v[ax+1] (bv, SM 115).
- Ball map Wb(v) = RB/(1+v0) * (v1, v3, -v2) (SM 116). So radius = RB tanh(eta/2) for rapidity eta.
- Hyperbolic geodesic between p, q: ip = -p0q0+p1q1+p2q2+p3q3, d = acosh(max(1,-ip)), point(t) = [sinh((1-t)d) p + sinh(t d) q]/sinh d (geoS, SM 117-118).
- Tree: depth 3 (words of length 1 to 3 drawn), 6 letters k = 0..5, arm = k>>1, sign = (k&1 ? -1 : +1); reduced words only (skip k with (k^1) equal to the last letter). Word position pt(wd): v=O; for i = len-1 down to 0: v = bv(v, wd[i]>>1, sign*ln5) (letters applied right to left). Each edge = geodesic in 6 segments, colour by arm, brightness 0.55*0.7^(word length before the step) (SM 120-124). Same code in LM (To, zn, xs, wo block).
- Level circles: for L = 1..4, a circle of radius RB*(5^L - 1)/(5^L + 1) in the x-z plane, opacity .18 (SM 109). (my check: .6667, .9231, .9841, .9968.) This equals RB tanh(L ln5 / 2).
- Wall sphere: radius RB/sqrt 2, red wireframe, opacity .035, always drawn. SM comment: "the half-line wall Gamma^2 = 1/2: the sphere of radius RB / sqrt 2" (SM 110-111). LM draws the same mesh (xg).
- Rim = ball surface, radius RB; massless eta = infinity sits there (radiusOf(Infinity) = RB).
- Particle position (both pages): radius = RB tanh(eta/2) with eta = arccosh(E/m), E = 10^slider MeV (slider 2.2 to 6.5, default 5.3 = 199.5 GeV by my check); massless -> RB; clamp to 0.999 RB.
  - SM etaOf: m<=0 -> Infinity; E<=m -> 0 (drawn at the centre); else acosh(E/m) (SM 142).
  - LM yo: m<=0 -> Infinity; E<m -> NaN (particle hidden, readout "unavailable: E < rest mass"); E=m -> 0 ("at rest (E = m)") (LM line 3793 end).
- Direction rule (directionOf / Mo), identical in both:
  - Reading A (arms = generations): bosons (incl. photon, Higgs, W, Z, gluons) on DIAG. Fermion of generation g: arm = ARMS[g]; perp1 = normalize(DIAG - arm (DIAG.arm)); perp2 = normalize(arm x perp1); angle u=0, d=pi/2, l=pi, n=3pi/2; dir = normalize(arm + 0.28 cos(ang) perp1 + 0.28 sin(ang) perp2). Antiparticle: negate.
  - Reading B (arms = colours): quarks: three copies per quark, along ARMS[c] (r,g,b), plus offset 0.06*(gen-1) * normalize(arm x DIAG); anti: negate arm. Leptons and colour-neutral bosons on DIAG: lepton dir = normalize(DIAG + 0.16 cos(ang) p1 + 0.16 sin(ang) p2), p1 = normalize(x-hat - DIAG (DIAG.x)), p2 = DIAG x p1, ang = gen*2.094 + (neutrino ? 1.047 : 0). Gluons: six "charged" directions normalize(ARM_a - ARM_b), a != b, plus two neutral on DIAG labelled " x2 neutral"; in A one entry " (8)" on DIAG. A colour hexagon is drawn at radius 0.98 RB in the plane perpendicular to DIAG through the projected +-arms, vertex order [0,5,2,1,4,3,0].
- Wall loop (both pages): word [[0,1],[2,1],[0,-1],[2,-1]] with step r = ln z: B1 B2 B1^-1 B2^-1, arms 0 and 2 (i and k drawn axes), k-th corner = prefix product applied to centre. Slider z 1.05 to 20, default 5. Trace printed as tr = 2 - 4 sinh^4(r/2) (computed from the formula, not from matrices). Gamma^2 of the step = tanh^2(r/2) = ((z-1)/(z+1))^2. (my check: 2x2 SL(2) commutator trace equals 2 - 4 sinh^4(r/2) exactly at z = 1.5, 5, 3+2sqrt2, 10; at z=5: -0.56, Gamma^2 = 0.4444; at z=3+2sqrt2: trace -2, Gamma^2 = 0.5. The 4x4 trace of the same word is the square of the 2x2 trace: 0.3136 at z=5, 4.0000 at the wall.)
- Koide arrow: normalize(sqrt(m_e) AI + sqrt(m_mu) AJ + sqrt(m_tau) AK) with m_e = 0.51099895, m_mu = 105.6583755, m_tau = 1776.93 (MeV); cone about DIAG, height = radius = 0.99 RB/sqrt 2 (half-angle 45 degrees, cos^2 = 1/2). Printed "cos^2 angle((sqrt me, sqrt mmu, sqrt mtau),(1,1,1)) = 0.5000017". (my check: (sum sqrt m)^2/(3 sum m) = 0.500001652; so the printed number is right.)

### 2.2 The twin-prime chain (Eye "end", both pages)
- Twin-prime list TW: all a in 11..199999 with a and a+2 prime (sieve to 200002). word = TW[1..40] (so first member 11 is skipped; list starts 17, 29, 41, 59, 71, 101, 107, 137, 149, 179, 191, 197, 227 ...), each mapped by a mod 10: {1:0, 7:2, 9:4}, i.e. axis letters +x, +y, +z only (AXW lists all six, only even indices used). (my check: first 12 letters = [2,4,0,4,0,0,2,2,4,4,0,2]; 2158 twin-prime lower members below 200000.)
- 4x4 boost B(n, eta) = [[cosh, sinh n^T],[sinh n, I + (cosh-1) n n^T]]. L_k = L_{k-1} B(axis, ln5) (right multiplication; "each along the next arm in its own frame", "L = B(p) . R" in the eq line). Point p_k = first column of L_k. Animated for the first 12 boosts in float64 only (SM comment: readouts use the 80-digit rows).
- Spin arrow: n = unit spatial part of p_k; Rm = B(-n, acosh p0) . L_k (rest-frame rotation); spin = spatial block of Rm applied to s0 = (0, 1/sqrt2, 1/sqrt2); drawn (s0, s2, -s1). Travel arrow = unit spatial part of p_{k+1}, drawn (p1, p3, -p2). Walker eased with t^2(3-2t) along geodesic of 40 samples; 1.6 s per step; loops over 12 steps.
- Stored run (both pages carry identical numbers, my check max relative difference 0.0): 39 rows (eta, lab turn, rest-frame turn), source label "80-digit run SM-END-PHASE-02", reading label "B35". Script SM-END-PHASE-02 is not in either file. First row eta = 2.598653876441405 (my check: equals acosh(cosh^2(ln 5)), i.e. the rapidity AFTER THE SECOND boost; row 39 eta = 48.85358272627524 is after boost 40). So row j belongs to boost j+1; 39 rows = "39 turn differences" (LM says this).
- Definitions as the text gives them: "lab turn of travel per step" alpha_n ~ e^(-eta_n); "turn in the particle's own frame" omega_n approx constant. Readout "ball radius tanh(eta/2)" is shown as "1 - fmt(1 - tanh(eta/2))". Chart: x = 40 + (eta-2)/48 (W-60); lab turn on log10 axis y = 20 + (-log10 v)/22 (H-50); own turn linear y = H-30 - v/1.6 (H-60).

Stored table (SM lines 83; LM Mn gives the same values in other notation). Columns: boost index j+1 of the row, rapidity, lab turn (rad), own-frame turn (rad).

| row | eta | lab turn | own turn |
|---|---|---|---|
| 1 | 2.598653876441405 | 0.3671738338182192 | 0.8364486591584582 |
| 2 | 3.558871249391167 | 0.13720144047726116 | 1.042716155287771 |
| 3 | 4.798587940178389 | 0.0369838427456457 | 0.8964995432924969 |
| 4 | 5.974764316042137 | 0.011757984713600724 | 0.9865475539606943 |
| 5 | 7.562274652025785 | 0.0007413779315226654 | 0.24022467061473887 |
| 6 | 8.52008631409348 | 0.0009572238220417165 | 1.173511979672355 |
| 7 | 10.092085749872519 | 7.62658852535486e-05 | 0.31399799796551364 |
| 8 | 11.052051947823886 | 7.61011085727818e-05 | 1.1729484959940886 |
| 9 | 12.624222825175131 | 6.049198319642413e-06 | 0.31335693640672385 |
| 10 | 13.585552548562948 | 6.0409056707655675e-06 | 1.1721019156714252 |
| 11 | 14.568648050708935 | 2.2592190695302968e-06 | 1.1571947266646276 |
| 12 | 16.14263470394749 | 1.7515868468931695e-07 | 0.3057230261629157 |
| 13 | 17.12506008835307 | 1.7528001755820104e-07 | 1.1576638186352122 |
| 14 | 18.698994768176526 | 1.359938717725037e-08 | 0.30594464276828454 |
| 15 | 19.659623756297187 | 1.3904917456842233e-08 | 1.1725792700684299 |
| 16 | 21.23184729918621 | 1.1044969919637879e-09 | 0.3131441476192106 |
| 17 | 22.193014416657665 | 1.1038990035803185e-09 | 1.1722173750389395 |
| 18 | 23.176099444177144 | 4.1284768657304663e-10 | 1.1572042892115164 |
| 19 | 24.255304958845272 | 1.3894160975119428e-10 | 1.0845851002317062 |
| 20 | 25.8363710843343 | 9.716078892739238e-12 | 0.27381141933555425 |
| 21 | 27.444657209732487 | 4.002883486702235e-13 | 0.05541030624153394 |
| 22 | 28.412084378993224 | 2.1978252104544342e-12 | 1.167983950421594 |
| 23 | 29.984845939689755 | 1.733018513801047e-13 | 0.31089930812853206 |
| 24 | 30.94070965407954 | 1.7533222204453115e-13 | 1.1757702936223737 |
| 25 | 31.923818828079632 | 6.556970707061755e-14 | 1.1571874525899206 |
| 26 | 33.00364547357844 | 2.2050985963429652e-14 | 1.0840769531327126 |
| 27 | 34.58475501983482 | 1.540983923901502e-15 | 0.27360372896795554 |
| 28 | 35.59837165755037 | 1.6601632367924254e-15 | 1.1353749637143895 |
| 29 | 36.56193606336065 | 6.347131500551913e-16 | 1.1706012757207724 |
| 30 | 38.13439240369768 | 5.025712955101153e-17 | 0.31217489616734456 |
| 31 | 39.15581228350802 | 4.7304440778291884e-17 | 1.1296181468597752 |
| 32 | 40.120806841935476 | 1.8070621042599793e-17 | 1.16963415206221 |
| 33 | 41.36015893513257 | 4.891034821699917e-18 | 0.9332033269439083 |
| 34 | 42.53652331868876 | 1.5549350670161634e-18 | 0.998059842310132 |
| 35 | 43.734235946442986 | 4.65229647536363e-19 | 0.976941783962508 |
| 36 | 45.32308659931677 | 2.8673342796393606e-20 | 0.2335346413137186 |
| 37 | 46.93169213986661 | 1.1717656048530401e-21 | 0.04710698638269036 |
| 38 | 47.89801836708666 | 7.574710398518257e-21 | 1.1687316017269338 |
| 39 | 48.85358272627524 | 2.9133981320385346e-21 | 1.1759699294710393 |

My checks on the table: slope of ln(lab turn) against eta over all rows with lab turn > 0 = -1.00608 (printed "-1.006"); mean own-frame turn first 10 rows 0.81484, last 10 rows 0.81450, ratio 0.9996 (printed "0.81 rad" in SM text and "1.000" as first of "1.000 . 1.097 . 1.039"). The other two entries of "slope ... three ends: -1.006 . -1.000 . -1.000" and "last 10 / first 10: 1.000 . 1.097 . 1.039" refer to two more runs not in these files (cannot be checked here).

### 2.3 Particle table (SM lines 61-81; LM var xo, comment lost in minification)
Source comment (SM 61-62): "Particle masses in MeV (PDG 2024 central values; quarks: MSbar for u, d, s at 2 GeV, c, b at their own mass, t pole). Neutrino masses are not measured; 0.05 eV is used only to draw them. Photon and gluon are massless."
Masses in MeV as printed: e 0.51099895; mu 105.6583755; tau 1776.93; neutrinos 5e-8 each (0.05 eV); u 2.16; c 1273; t 172570; d 4.70; s 93.5; b 4183; W+- 80369.2; Z 91188.0; H 125200; photon 0; gluon 0. Kinds/types: lepton gen 0,1,2 type l (charged) or n (neutrino); quark gen 0,1,2 type u (u,c,t) or d (d,s,b); bosons; flags ew (W,Z), higgs, gluon. Neutrino names: SM "ve, vmu, vtau"; LM "v1, v2, v3". Colours as hex (charged leptons 0xbfe6ff, neutrinos 0x9affc8, up 0xff9d7a, down 0xffd27a, W/Z 0xd6a8ff, H white, photon 0xfff3a0, gluon 0x8affff).

## 3. EYES / SCENES AND RESULTS

Panel texts, grade lines, equations and explanatory text quoted from the code (short quotes; full strings are in the source lines cited).

### 3.1 SM ball, header (SM 40)
Title "The Standard Model in the Ball". Subtitle: "Garrett's ratio-5 tree of peel steps in the Poincare ball, with every particle placed by its mass". Mode buttons: "A . arms are generations", "B . arms are colours". Four eyes: end, particles, wall, higgs (hash #particles/#wall/#higgs, default end). Footer "Drag to turn, scroll or pinch to zoom."

### 3.2 SM Eye 1 "The end becomes a phase" (SM 162-194)
- Grade: "CHECKED . run SM-END-PHASE-02 (80 digits) . reading B35".
- Eq lines: "L_n = L_(n-1) . B(arm, ln 5)      L = B(p) . R" / "lab turn of travel per step alpha_n ~ e^(-eta_n)" / "turn in the particle's own frame omega_n ~ constant".
- Text: spin climbs the twin-prime chain's word, one ln 5 boost per step, "each along the next arm in its own frame (the tree is the same from every ball)". "the lab turn per step falls exactly as e^(-rapidity), slope -1.006." Own-frame turn "averages 0.81 rad per step over the first ten steps and over the last ten alike. The amplitude dies at the wall; the phase goes on."
- Readouts: step on the chain "k+1 (of 40 in the run)"; rapidity eta (3 d.p.); ball radius tanh(eta/2) as "1 - ..."; lab turn this step (rad); turn in own frame this step (rad) [each from ROWS[k], k = 0..11]; "at step 40: eta = 48.85, lab turn 2.9e-21, own turn 1.18" (from last row); "slope ln(lab turn) / eta, three ends: -1.006 . -1.000 . -1.000"; "own-frame turn, last 10 / first 10: 1.000 . 1.097 . 1.039".
- Key text: "gold path: the chain's end . rose: spin . blue: travel direction . red mesh: the half-line wall Gamma^2 = 1/2".
- Grade as the source gives it: checked (80-digit run, script not included). The chart and slope/mean numbers match the stored rows (my check above).

### 3.3 SM Eye 2 "Every particle in the ball" (SM 205-230)
- Grade: "ASSIGNMENT . positions exact for the chosen reading".
- Eq: "radius = tanh(eta/2),   eta = arccosh(E / m)" / "massless: eta = infinity, on the rim" / "A: generation -> arm     B: colour -> arm".
- Text: same energy E for all; heavy near centre, light at rim; photon and gluons on the rim; A: arm = generation, generation-blind bosons on (1,1,1); B: arm = colour, "every quark appears three times", leptons and colour-neutral bosons on the diagonal; "Antiparticles point the opposite way."
- Controls: common energy E slider (2.2 to 6.5 in log10 MeV, default 5.3; label shows MeV below 1000, else GeV with 1 d.p. below 10 GeV, 0 d.p. above), "show antiparticles" checkbox.
- Readouts: reading of arms; top, Higgs, Z, b, tau, mu, e: "eta x.xx . r y.yyyy" (r = tanh(eta/2) 4 d.p.), "rim", or "at rest (centre)"; "nu (0.05 eV, drawing value)"; "photon, gluons: on the rim".
- Gluon labels: A "g (8)"; B six unlabelled charged + "g x2 neutral". Antiparticle label prefix an overline character.
- No computed pass/fail; an assignment.

### 3.4 SM Eye 3 "The wall and the generations" (SM 234-257)
- Grade: "PROVED (BallJoins J4) . CHECKED (mass ratios) . known (Koide 1981, Foot)".
- Eq: "loop of two equal perpendicular steps:  tr = 2 - 4 sinh^4(r/2)" / "wall: tr = -2 at z = 3 + 2 sqrt2,  Gamma^2 = 1/2" / "Koide:  cos^2 angle((sqrt m_e, sqrt m_mu, sqrt m_tau), (1,1,1)) = 0.5000017".
- Text: "Step out along one arm, out along another, back, back. Below the wall the loop closes as a pure turn; on the wall it is parabolic; past it the loop no longer closes even up to a turn. Garrett's step z = 5 is inside. Every step from one generation to the next is past it: z from 16.8 (mu->tau) to 589 (u->c)." In reading A the lepton sqrt-mass vector sits on the 45-degree cone about (1,1,1) "which is the wall value cos^2 = 1/2 (Koide's relation; the fact is old, the match to the wall line is the new reading, and a matching fraction does not make two invariants the same)."
- Readouts: step ratio z (3 d.p.); "Gamma^2 of the step" = tanh^2(r/2) (4 d.p.); loop trace; classification ("closes as a pure turn (elliptic)" if |tr| < 2 - 1e-9; "parabolic: on the wall" if | |tr| - 2 | < 0.02; else "does not close (hyperbolic)"); "the wall: z = 3 + 2 sqrt2 = 5.8284"; "Garrett's step: z = 5 . inside"; generation steps as z = ratio of masses: mu->tau 16.8177, d->s 19.8936, s->b 44.738, c->t 135.562, e->mu 206.768, u->c 589.352 ("all past the wall"); "Koide cos^2 (reading A): 0.5000017 (wall: 0.5)", "not drawn in reading B". (my check: ratios of the table masses = 16.81769, 19.89362, 44.73797, 135.56167, 206.76828, 589.35185; all agree to the printed digits.)
- Grades: trace/wall = proved elsewhere (BallJoins J4, not in these files; my check reproduces the formula), mass ratios checked, Koide cos^2 value reproduces; Koide match to the wall line = "new reading" (SM text).

### 3.5 SM Eye 4 "Crossing the wall inward: the Higgs" (SM 260-278)
- Grade: "RECOGNISED . Standard Model at tree level (m ~ v)".
- Eq: "m_W = g v / 2,   m_Z = sqrt(g^2 + g'^2) v / 2,   m_f = y_f v / sqrt2" / "v: 0 -> 246 GeV" / "massless: 2 helicity states (a phase)   massive spin 1: 3 states".
- Text: v from 0; at v=0 every particle massless on the rim "where only the helicity phase is kept"; as v grows W, Z, fermions move inward; "W and Z pick up a third, longitudinal state as they cross"; "This is the wall crossed the other way: the phase becomes a full turn record again."
- Maths: each particle's mass scaled m*v (v in 0..1, shown as 246 v GeV), eta = arccosh(E/(m v)); W,Z get three small dots circling the particle (ang = 1.5 t + i 2pi/n, radius .22); n = 2 if m = 0 or r > 0.995 RB, else 3. Readouts: v, m_W = 80.369 v GeV, m_Z = 91.188 v GeV, m_top = 172.57 v GeV (2 d.p.), per-W/Z "2 (helicity +-1, on the rim)" or "3 (inside)", "photon stays on the rim, 2 states". Higgs and gluons are not drawn in this eye.
- Grade: recognised (standard textbook), not derived.

### 3.6 LM header and sources (LM 35-45)
Title "Tree, Ball and Light". Subtitle: "Garrett's ratio-5 tree . phase, response and retained history; Jeromie Beasley . corrected research view . 11 November 2026". Intro: "Corrected derivative of the supplied mixer. Original data and v3 negative tests preserved. Colour B means internal SU(3), separate from optical/material colour." Mode buttons: "A . assigned generations", "B . SU(3) colour weights". Details block: "Source models: Dirac Time section 11; Light Keeps the Ledger 7.2 sections 4.8-4.9f; Offset Speed Limit. Geometry: corrected ratio-5 Ball mixer. Optical and phase operators are attached finite models, not a derivation from the tree." "Independent matrix checks: 909 optical frequency points, 9 environment scales, 100 phase states. All pass." Evidence files named math_tests.py, math_report.json, math_review.md (contents not in the text file). "Lossless poles and singular offsets are marked, not clamped to finite values." WebGL, or a Canvas fallback projecting the same 3D scene.
Six eyes in order: light (default), response, end, particles, wall, higgs. LM sets location.hash on every switch. Controls also refresh readouts on input/click.

### 3.7 LM Eye "Light . phase becomes a signal" (LM line 3801-3803, code in 3803)
- Grade: "EXACT FINITE MODEL . attached to tree geometry".
- Eq: "|psi_phi> = (|01> + e^(i phi)|10>)/sqrt2,  H = kappa sigma_x,  hbar = 1" / "c(t) = [1 + sin(2 kappa t) sin phi]/2" / "g = kappa^2 sin^2 phi,   tau-dot^2 <= 4g/[c(1-c)]".
- Text: "Two preparations start with identical local occupations and total excitation. Their correlation phases are +phi and -phi. The same later exchange reveals opposite signals. The highlighted tree route locates this attached experiment; its boost word does not generate phi or kappa. Motion along the route is a visual guide, not photon speed."
- Code (ai.phase(phi, kappa, t)): s = sin phi; c = (1 + sin(2 kappa t) s)/2; cd = kappa cos(2 kappa t) s; g = kappa^2 s^2; tau = ln((1-c)/c) and bound = 4g/(c(1-c)) and rate = -cd/(c(1-c)) only when 1e-12 < c < 1-1e-12, else null.
- Controls: stored phase phi in [0, pi] (default pi/2, label shows phi/pi 3 d.p.), exchange coupling kappa in [0,2] step .01 default 1, time t in [0, 6.28] (autoplays at 0.65 per second, wraps at 6.28), buttons Play/pause, Reset time, "Zero-phase control" (phi=0).
- Readouts: "model units: hbar = 1; t in inverse reference energy"; "c(+phi) / c(-phi)" (5 d.p.); "signed offset tau(+phi)" (5 d.p.) or "singular: empty/full limit"; "actual metric g" (6 d.p.); "tau-dot^2 / bound" (5 d.p.) or "undefined at singular offset"; "inequality slack" = max(0, bound - rate^2) in exponential 2 d.p.; "phase-only control phi=0: g = 0 and c = 1/2, even when kappa > 0"; status playing/paused.
- Drawing: two dots at the end anchor of the tree path, displaced (+-0.65, (c-0.5)*2, 0), scale .18+.65 c; two arrows directed (cos phi, sin(+-phi), 0) "retained input phase"; chart of c(+phi), c(-phi) over t 0..6.28, y 0..1, gold cursor at t. Key: "Dot size and displacement show occupation, not physical position."
- Anchor path Wc(): from the centre, one boost of ln 5 along each of axes 0, 1, 2 in turn, each as 30-segment geodesic, cyan line; anchor = end point (the point ijk-boost). Purely a location marker.
- My check (algebra, not in the file): c(-phi) = 1 - c(+phi), so tau(-phi) = -tau(+phi); the inequality holds because c(1-c) = (1 - sin^2(2kt) sin^2 phi)/4 and 4g c(1-c) = k^2 sin^2phi (1 - sin^2(2kt) sin^2phi) >= cd^2. The page itself gives no proof; its grade is "exact finite model" with 100 phase states checked (details block).
- "light" here = a two-mode single-excitation state (|01>,|10>) with an exchange coupling and a stored relative phase. No reflection coefficient, Smith chart, Snell, refractive index, metal or element data.

### 3.8 LM Eye "Light . tune-out and environment" (LM 3803-3805)
- Grade: "EXACT THREE-LEVEL RESPONSE . declared spectral intervention".
- Eq: "Delta = (a, 2a),   |d|^2 = (1/a, 4/a),   sum Delta |d|^2 = 9" / "g = 2/a^3,   alpha(x) = 2/(a^2 - x^2) + 16/(4a^2 - x^2)" / "tune-out: x/a = sqrt(4/3), while g > 0".
- Text: "A calibrated lossless ground-state probe couples two transitions. Their signed responses cancel between poles, although geometric coupling survives. Increasing confinement a moves a conserved oscillator-strength measure upward. This is an environment model, not a fitted pressure law or an elemental spectrum. Resonance bands are excluded: this model has no damping."
- Code ai.optical(a, e) with e = x/a: g = 2/a^3; x = a e; pole = min(|e-1|,|e-2|) < 0.015; terms = [2/(a^2 - x^2), 16/(4a^2 - x^2)]; F = 9.
- Controls: environment / confinement scale a in [1,2] step .01 default 1; probe energy x/a in [0.05, 2.4] default 1.1547005383792515; buttons "Exact tune-out" (x/a = sqrt(4/3)), "Subgap probe" (0.6), "Reset environment" (a = 1).
- Readouts: probe energy x (5 d.p.); gaps Delta1 / Delta2 = a / 2a; metric g (6 d.p.); channel responses (the two terms, 5 d.p.) or "excluded resonance band"; total response alpha (7 d.p.) or "not evaluated at resonance"; "oscillator budget F: 9 (conserved)"; "subgap secant, y=0 -> 0.25" = (n(.25) - n(0))/.25 with n(y) = 2/(a^2 - y) + 16/(4a^2 - y), printed with "> 0" (y = x^2); "metric loss from a=1" = 2 - g; interpretation: "lossless pole: no finite prediction" / "positive channels below gap" (x/a < 1) / "signed channels between / above poles".
- Drawing: two opposing arrows (channel 1, 2) with length .1 + 1.8 (2/pi) atan(|term|/8) pointing by sign; gold torus scaled sqrt(g/2) ("geometry persists", metric strength sqrt g); chart of alpha (cyan) and g (coral) over x/a 0..2.4, y -20..20.
- My checks (algebra): sum Delta |d|^2 = a(1/a) + 2a(4/a) = 9 for every a; alpha = 0 exactly at x^2 = 4a^2/3 (terms -6/a^2 and +6/a^2); g = 2/a^3 equals sum |d|^2/Delta^2 = 1/a^3 + 1/a^3 (the page does not say how g is built; this is my reading). Static alpha(0) = 6/a^2.
- Terms like "tune-out", "oscillator strength", "gap" are atomic-spectroscopy words; the page states the model is not an elemental spectrum.

### 3.9 LM Eye "Direction convergence and retained turns" (end; LM 3793-3795)
- Same title field in code: "Direction convergence and retained turns". Grade identical to SM end: "CHECKED . run SM-END-PHASE-02 (80 digits) . reading B35".
- Eq: "L_n = L_(n-1) . B(arm, ln 5)      L = B(p) . R" / "sampled lab direction increments: ln alpha versus eta slope approx -1" / "rest-frame rotation increments remain finite in this run".
- Text: "The stored 40-boost run contains 39 turn differences. Its lab direction increments have fitted log-slope -1.006; rest-frame rotation increments stay finite on average. These are geometric angles, not quantum amplitudes. The rejected helicity-locking test stays rejected. Zero induced turn is not zero particle spin, and inverse transport rotations do not create a spin singlet."
- Readout differences from SM: "step on the chain: k+1 (12 animated; 40 in stored run)"; step 1 uses eta = ln 5 and says "no prior boost"; step k+1 >= 2 uses row k-1 of the stored table; labels "lab turn since prior boost" / "rest-frame turn since prior boost"; "after boost 40 (39 turn differences): eta = 48.85, lab turn 2.9e-21, own turn 1.18"; the "three ends" slope and last/first-10 lines unchanged. Key: "red mesh: finite commutator step wall Gamma^2 = 1/2; outer rim: radius 1".

### 3.10 LM Eye "Every particle in the ball" (LM 3795-3797)
- Grade/eq as SM Eye 2. Text changes: "Give every available particle the same energy E; species with E below their rest mass are unavailable and hidden." Added: "Antiparticle directions are a display assignment. B denotes internal SU(3) colour weights, not optical colour. The boost generators fail the su(3) algebra test: dimension 6, not 8. Neutrino mass labels share a drawing placeholder, not an oscillation spectrum." Readouts: "unavailable: E < rest mass", "rim (massless display)", "at rest (E = m)", "nu1,2,3 (same drawing placeholder)".
- The dimension-6 claim is stated in text only; the test itself is in the v3 evidence not in the file.

### 3.11 LM Eye "The wall and the generations" (LM 3797-3799)
- Same grade line and equations as SM Eye 3 (the eq text still says "wall: tr = -2 at z = 3 + 2 sqrt2, Gamma^2 = 1/2" and the Koide line).
- Text: "The four-step word is a boost commutator. Elliptic means conjugate to a rotation about an interior fixed point, not necessarily a closed path at the centre. Its finite step wall is Gamma^2 = 1/2 (radius 1/sqrt2), distinct from the massless radius-1 boundary. Koide is a separate positive pole-mass encoding: balanced centered books (B200), not the edge-book ratio wall (B189). V3 reports that integer generation levels and a tree-selected Koide cone failed their stated tests; the finite-depth searches found no exact cone hits."
- Readout classification changed: "elliptic: conjugate to a rotation" / "near parabolic boundary (display tolerance)" (0.02) / "hyperbolic: no interior fixed point". Koide line: "0.5000017 (balanced centered books)". Same six generation ratios, "Garrett's step: z = 5 . inside". Key: "red cone: separate Koide encoding (B200)".

### 3.12 LM Eye "Assigned Higgs mass scaling" (LM 3799-3801)
- Grade unchanged "RECOGNISED . Standard Model at tree level (m ~ v)"; eq unchanged.
- Text: "This schematic scales supplied W, Z and fermion masses linearly with a Higgs-value parameter at fixed couplings. It does not simulate an electroweak transition or derive Yukawa couplings. Every positive-mass spin-1 state has three polarizations, however close its velocity coordinate lies to the rim; the exactly massless vector illustration has two. The longitudinal mode requires the full gauge/Higgs theory. The finite commutator wall is unrelated to this massless boundary. Neutrino scaling is only a chosen placeholder beyond the minimal Standard Model."
- Code: states = 2 only when m*v = 0, else 3; E < m*v: hidden with "unavailable: E < rest mass". Same readouts m_W 80.369 v, m_Z 91.188 v, m_top 172.57 v.

## 4. FAILED OR SET ASIDE (as the pages state them; evidence files not present)
- "The rejected helicity-locking test stays rejected" (LM end eye). Failure condition not given in the file.
- "The boost generators fail the su(3) algebra test: dimension 6, not 8" (LM particles eye) - so reading B (colour = arm) is a display assignment only.
- "V3 reports that integer generation levels and a tree-selected Koide cone failed their stated tests; the finite-depth searches found no exact cone hits" (LM wall eye).
- "Zero induced turn is not zero particle spin" and "inverse transport rotations do not create a spin singlet" (LM end eye): set-aside readings.
- "Optical and phase operators are attached finite models, not a derivation from the tree" and "its boost word does not generate phi or kappa" (LM light eye): the light/response models are not derived from the tree.
- LM removes SM's claims: the Koide match to the wall (SM) becomes "separate encoding"; "wall crossed the other way" for the Higgs becomes "unrelated".
- LM response eye: "not a fitted pressure law or an elemental spectrum"; resonance bands excluded (no damping).

## 5. OPEN QUESTIONS the sources list
Neither page has an explicit open-questions list. Statements that read as limits: neutrino masses not measured (0.05 eV drawing value only); Higgs eye does not derive Yukawas or simulate a transition; longitudinal mode "requires the full gauge/Higgs theory"; the "three ends" runs (other two) and the 80-digit script are not in the pages; B35, B189, B200, J4, V3 are references to ledgers outside these files.

## 6. ELEMENTS HOOKS
- No atoms, ionisation ladders, shells, screening, alkali metals, francium, 5/8, or "space between" anywhere in either page (searched). No metal or element data. No reflection coefficient, Smith chart or Snell law in the code (Smith/refract hits in LM are three.js graphics only).
- The wall Gamma^2 = 1/2: SM Eye 3 eq line and code (SM 235, 247-256); sphere of radius RB/sqrt2 drawn in both pages permanently (SM 111); LM text (3799) "finite step wall Gamma^2 = 1/2 (radius 1/sqrt2), distinct from the massless radius-1 boundary". The wall comes from the trace of the loop B1 B2 B1^-1 B2^-1 of two equal perpendicular boosts, step ratio z: tr = 2 - 4 sinh^4(r/2), r = ln z, tr = -2 at z = 3 + 2 sqrt2 = 5.8284 where Gamma^2 = tanh^2(r/2) = 1/2. Readout label in both: "Gamma^2 of the step".
- Rim: |Gamma| = 1 / radius RB is where eta = infinity (massless photon and gluons sit there). In LM the rim is explicitly kept apart from the wall.
- z = 3 + 2 sqrt2: SM 235, 255; LM 3799. Garrett's step z = 5 "inside" (Gamma^2 = 4/9 by my check).
- Peel step: only in SM subtitle ("Garrett's ratio-5 tree of peel steps"); the tree step is B(arm, ln 5).
- Gamma^2 = 1/2 also appears as the Koide value cos^2 = 1/2 (SM says "the match to the wall line is the new reading"; LM says Koide is a separate encoding, B200, not the ratio wall B189).
- Generation steps as step ratios z (mass ratios): mu->tau 16.8177 ... u->c 589.352 ("all past the wall"). These are ratios of lepton/quark masses, not atomic quantities.
- Light mixer light eyes: phase c(t) = [1 + sin(2 kappa t) sin phi]/2; three-level response with Delta = (a, 2a), F = sum Delta |d|^2 = 9, tune-out x/a = sqrt(4/3); "confinement a" is an environment scale; says "not an elemental spectrum". "Optical colour" is mentioned only to separate it from SU(3) colour B.
- "geometry persists" label on the metric ring: g = 2/a^3 stays positive at tune-out where alpha = 0.

## 7. CONTRADICTIONS OR SLIPS
1. Row offset in SM Eye 1: step k+1 (k = 0..11) is drawn from boost k+1 but its readouts use ROWS[k]; ROWS[0] has eta = 2.5987 = after boost 2 (my check). So SM's displayed rapidity/turn for step k+1 belong to boost k+2. LM corrects this (step 1 = ln 5 "no prior boost"; step k+1 uses row k-1) and calls rows "turn differences" (39 rows for 40 boosts). SM still says "of 40 in the run" and "at step 40" using the last row (boost 40) - consistent only for the last.
2. SM Eye 4 title and text say the Higgs onset is "the wall crossed the other way"; the radius where massless things sit is the rim (RB), the wall is at RB/sqrt2. LM states "The finite commutator wall is unrelated to this massless boundary." Direct disagreement between the two pages.
3. Koide: SM says the lepton sqrt-mass cone sits on "the wall value cos^2 = 1/2" (and "the match to the wall line is the new reading"); LM says it is "a separate ... encoding (B200), not the edge-book ratio wall (B189)" and that tree-selected Koide cone tests failed. Number 0.5000017 itself is correct (my check).
4. SM etaOf returns 0 for E <= m, so a particle with E below its rest mass is drawn at the centre (e.g. top at the low end of the slider, 10^2.2 = 158 MeV); LM hides it. Same in SM Eye 4 with m*v.
5. SM Eye 4: onRim = (m = 0 or r > 0.995 RB) gives W/Z only 2 states when very near the rim even though massive; LM says three for every positive mass.
6. SM text "falls exactly as e^(-rapidity), slope -1.006": a fitted slope is not "exactly" (LM says "fitted log-slope -1.006" and "approx -1").
7. SM text "The amplitude dies at the wall": the lab turn decays continuously with eta; no feature at the wall radius RB/sqrt2 is computed in this eye. (Statement as printed; nothing in the code ties the decay to the wall.)
8. LM eq line 1 of the wall eye still prints "Koide: cos^2 angle(...) = 0.5000017" while the text says Koide is separate; and "Elliptic" is relabelled but the eq still says "wall: tr = -2 at z = 3 + 2 sqrt2" for a 4x4 loop whose 4x4 trace equals the square of the printed trace (4 at the wall by my check). The printed trace is the SL(2) trace; the page does not say which representation.
9. The readout "step ratio z" for generation steps uses plain mass ratios while the particle placement uses eta = arccosh(E/m); the page does not say why a mass ratio is the step ratio of a loop. (Not wrong; unexplained.)
10. SM level circles are drawn only in the x-z plane and are "tree level" radii tanh(L ln5/2); the loop/wall sphere is full 3D.
11. Neutrino names differ (SM nu_e, nu_mu, nu_tau vs LM nu1, nu2, nu3); the LM page also drops the PDG-source comment (minified), so the masses are uncommented there.
12. Header of SM claims "every particle placed by its mass" at a common energy E (default 199.5 GeV by my check); only particle masses and E set position; no couplings.

## 8. THINGS A LATER READER WOULD WALK PAST
- The stored 39-row table (SM line 83; LM Mn in line 3793) is the only numerical evidence for the end eye; both pages give it, identical to the last digit; script SM-END-PHASE-02 not included.
- The only quantitative lab-turn law is the slope -1.00608 and the own-frame mean 0.8148 / 0.8145 (my recomputation matches the printed -1.006 and 0.81).
- LM line 3799: "Koide ... not the edge-book ratio wall (B189)" and "tree-selected Koide cone failed their stated tests": answers whether the Koide cone is on the wall; it says no in LM.
- LM line 3795: "Zero induced turn is not zero particle spin" and rejected helicity-locking: the tree-end "phase" is explicitly geometric, not a quantum amplitude.
- LM line 3797: boost generators give dimension 6, not su(3) dimension 8: the colour reading B is only a display assignment.
- LM line 3801-3803: sin(2 kappa t) sin phi occupancy, g = kappa^2 sin^2 phi, the inequality tau-dot^2 <= 4g/[c(1-c)], and the zero-phase control (g = 0, c = 1/2 even when kappa > 0): the phase alone is the signal.
- LM line 3803-3805: the three-level model has sum Delta|d|^2 = 9 independent of a, tune-out at x/a = sqrt(4/3) independent of a, and g = 2/a^3 (metric decreases with a: "metric loss from a=1" readout). The page labels "geometry persists" at tune-out.
- The wall formula tr = 2 - 4 sinh^4(r/2) reproduces exactly in my check; it gives the wall z = 3 + 2 sqrt2 for any commutator of equal perpendicular boosts, so it is a property of the step ratio only, independent of the tree arms used.
- LM and SM both draw the same fixed sphere RB/sqrt2 in every eye, so the wall is visible in the light eyes as well though the light eyes never use it.
- Provenance strings to chase elsewhere: "Dirac Time section 11", "Light Keeps the Ledger 7.2 sections 4.8-4.9f", "Offset Speed Limit", "BallJoins J4", "reading B35", "B189", "B200", "V3", "SM-END-PHASE-02", "One Tree, One Ball mixer".
