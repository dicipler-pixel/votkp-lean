# READ A3: VOTKP / Elemental Peeling, five versions (11 Nov 2026 brief)

Reader label A3. Byline on every version: "Jeromie Beasley".

## 1. Coverage

Decoded from Drive into /home/claude/sm/votkp_reads/src/A3/ (base64 to bytes). Text extracted into /home/claude/sm/votkp_reads/text_A3/ (HTML tags, scripts and styles stripped; LaTeX source kept as written in the file).

| File (Drive id) | Version / date | Chars of text read | Read in full |
|---|---|---|---|
| VOTKP_Elemental_Peeling_Paper_v0_1_Package_20260923.zip (1jvN1eUJ7b78O3t1OAPc2UJWraDfnMW-q) | v0.1 working draft, 23 Sep 2026 | 59,647 (paper .md inside the zip) | Yes, every line, lines 1-824 |
| VOTKP_ELEMENTAL_PEELING_PAPER_v0_2_20260923.html (1FVCmXAPrvyx_-_qpJoR6CU4C-cYuaWoS) | v0.2, 23 Sep 2026 | 48,488 | Yes, every line |
| VOTKP_ELEMENTAL_PEELING_PAPER_v0_5_20260924.html (1Y0eaQXAy6bW0_vNzTNm3-exfENSWoX39) | v0.5, 24 Sep 2026 | 88,316 | Yes, every line, lines 1-2986 |
| VOTKP_TEST_RECORD_v1_20260923.html (1So3QoAiYAAkxVL-uGhIJ_5Dd11VySTtG) | Test record v1, 23 Sep 2026 | 14,380 | Yes, every line |
| VOTKP_Gap_Research_20260925.html (1nQnMRsVSUYsSegaMYMvhY2O777ofLyNZ) | Gap research follow-up (titled "VOTKP v1.0: closing the remaining gaps"), 25 Sep 2026 | 15,788 | Yes, every line |

Total text read: 226,619 characters.

Not read: (a) the v0.1 .html inside the zip (595 KB, same paper as the .md, not read separately); (b) figures (PNG/SVG) and figure .py scripts in the zip; (c) the scripts/*.py, CSV and JSON data files in the zip and the scripts named in each appendix; (d) the figure images inside the v0.2 and v0.5 HTML. Every number and claim in this report comes from the text. The v0.2 and v0.5 HTML figures are captions only in the text.

Referenced items not in this set: the "v1.0 independent audit" and its registered G-02 test, the pre-registration files, the Lean source, and the NUM_01_RESULTS file. Where the Gap Research file cites these, I report the citation and mark it unchecked.

## 2. What each version defines and claims

### v0.1 (23 Sep 2026, byline Jeromie Beasley, "Working draft")
- Central object VOTKP(K,Psi) = (T, L, G, E) (abstract; Part III §9). Four layers: topology T, field loading L, geometry G, realization cost E.
- Peel as operational (§2.1); three peel classes: channel, coordinate, physical (§2.2); knot move classes (§2.3).
- §3 Theorem 3.1 (finite linear predictive quotient): O v = (Rv, RLv, ..., RL^{n-1}v); quotient V/N is the minimal autonomous summary. Table 1 lists reduced-equal, rich-different witnesses.
- §4.1 same-spin pair density n2 = n n - |gamma|^2 vanishes at coincidence. §4.2 quantum metric g_ij and "Delta_allowed(O)". §4.3 side-coupled contact conductance 0.180144 G0 to G0. §4.4 Theorem 4.1: mu_eff(r) = mu_b + (c^2/delta)(1-2r); critical occupation r_c = (1/2)(1 + mu_b delta/c^2).
- §5.1-5.10: positive-channel peel; form tomography; Schur boundary memory; memory kernel; transfer silence (nilpotent shift q=5); four-reading optical certificate; phase-reference recovery ("Intensity can erase phase"); cumulants (c3 = p1 - 3p2 + 2p3); two-level impossibility bound (Delta = 79,600,000/400,039,601 approx 0.19898); one-energy snapshots.
- §6.1-6.4: interface operator K_Sigma; "A Snell-like law" sqrt(g_par) sin(theta) = const; receiver metamer (gold); film thinning r(d) = (Gamma + r12 p^2)/(1 + Gamma r12 p^2) with a non-monotone reflectance (Au 450 nm: 0.408191 at 200 nm, peak 0.426742 at 58.2093 nm, 0.163082 at 10 nm).
- §7-8: calibration (Cu, Ag, Au, Pt); ten-element pilot (§7.2); ionization onion atlas, Run 01 (peel shape T1 vs static S2: 0.95 vs 0.49 at K=10; kill condition passed); reset ridges at 2, 10, 28, 46, 68; Run 02 polarizability (peel loses 9 of 9; K2 six noble-gas minima, 6 of 6).
- §9 Pre-named tests T-A to T-J with kill conditions, none run in v0.1.
- §10-12: HOMFLY engine, P(4_1), P(3_1), P(8_19); scan of 250 prime knots to 10 crossings finds no Alexander+Jones-equal, HOMFLY-different pair (§10.3); skein and band peels (§10.4-10.5); field loading W = z^alpha w^beta/(z^p + w^q), Hopf charge Q = alpha q + beta p, eight exact preimage counts (Table 5); volume by class (SnapPy 0 for 3_1, 5_1, 8_19); Table 6 five volume-separated pairs; colour law Vol ~ 3.25 ln(|J3(e^{8 pi i/15})| + 36.97) - 1.72 (cited, §12.4); A-polynomial volume form omega (§12.5), torus control omega = 0; MMR loop expansion (§12.6).
- §13 realization layer (polystyrene topology; Leigh molecular-knot nitrogen deletions).
- §14-15: common pattern; "It does not claim" a Z <-> K correspondence; test plan T-A to T-J; §16 permanent negative controls (15 items).
- Appendix A proofs (A.1-A.7); Appendix B Lean checkpoint (49 declarations, 3 modules); Appendix C ideas held for later (includes "Kelvin's vortex atoms"); Appendix D literature.

### v0.2 (draft, 23 Sep 2026, "Claude's version written from Jeromie Beasley's research programme")
- Abstract adds four organizing results: records are vectors; peel shape is a reflection coordinate, Gamma_k = tanh((1/2) ln(IE_{k+1}/IE_k)) (Theorem 8.1); failures resolve on ladders; refraction is not reflection.
- §6.3-6.4 reflection coordinate Gamma = (1-N)/(1+N); Theorem 6.1 echo expansion; R(d) = |Gamma|^2 + 2 Re[Gamma-bar (1-Gamma^2) r12 p^2] + O(|p|^4); 171 metal/wavelength/substrate cases; threshold |Gamma| approx 0.93 gives 99.4%.
- §8.3 depth ladder (accuracy 0.22 at K=1 to 0.89 at K=11, 1.00 at K=8-10); 62 of 65 misses explained by "outer > K" rule.
- §8.4 ridge census table (prominence by depth). §8.5 run 03 table; ln alpha = 10.28 - 3.04 ln IE1, R^2 = 0.906 over 86 elements. §8.6 reset table.
- §9 Snell test (failed): turning set 1 hit vs 6; confusion labels 0 of 6; refraction vs reflection correlation 0.61-0.68 falls to 0.02-0.03 after detrending.
- §11.2 HOMFLY census to 12 crossings: 250 / 548 of 552 / 2075 of 2176; 105 knots exceed engine. Cites Dlotko, Gurnari, Sazdanovic for 53.7% vs 53.4% at 15 crossings.
- §12 Hopf charges on T(3,4): 7, 10, 11, 13, 15; energies 7.857, 8.272, 8.761 at Q=12,13,14.
- §13.3 colour law with the frozen offset-free line Vol = 2.979 ln|J3| - 0.658 (fit on 205 knots to 10 crossings). Table 5 volume pairs.
- §13.4 colour ladder: 21 pairs identical on J2 and J3 separated by J4 (2 at 11 crossings, 19 at 12 crossings).
- §13.5 A-polynomial: figure-eight 2.0298832128193074; 5_2 check; §13.6 P1(4_1) = 0; P1(3_1) = -t^{-2}(t^2+1)(t-1)^2.
- Appendix D test ledger with pre-registration timestamps; run 02 "peel claim killed; split found".

### v0.5 (draft, 24 Sep 2026, "Claude's version")
- Abstract: five results. Adds: 354 blind pairs through twelve crossings (285 + 5 + 63 + 1), hyperbolic volume separates 253; the addition law (Theorem 15.1); four pre-registered extensions that failed (nuclear shape, tabulated strengths, relativistic echo weight, tight knots).
- §6.3-6.4 with the film thinning peel; the 171-case test now reports held-out 0.96-0.98 with each metal's threshold set without it; "always predicting a bump scores 0.725".
- §8.5 numerator test NUM-01: denominator (energy of strongest ground-level line) 0.267; numerator 0.392; registered kill triggered.
- §8.6 reset table (same as v0.2).
- §9 Snell test (same results as v0.2).
- §11.2 HOMFLY first separating power at thirteen crossings: KnotInfo census of 12,965 prime knots; 19 pairs at 13 crossings; 18 knots involved; 12 pairs have Alexander 1; all pairs differ in volume.
- §11.3-11.4 Khovanov and knot Floer categorified rung (CAT-01): 233 of 253 volume-different blind pairs stay blind through 12 crossings; thin knots of equal signature: 0 of 2,525 separated.
- §13.2-13.6 as v0.2; figure-eight; loop numerator P1 integrality.
- §15 "Where particles enter": 15.1 electron is the unit removed; 15.2 Theorem 15.1 (peel steps add as rapidities), Corollary 15.2 (peel coordinate is a hyperbolic length), Corollary 15.3 (film has same algebraic form), radar reading (Bondi k = sqrt(z_k)), order-of-peeling identity, associator formula for reduced products (checked to 1e-15), zero-phase stack telescopes, film order effect up to 0.16 in R; 15.3 mass-ratio table (H-, D-, Ps-); scale blindness (Theorem 15.4); 15.4 nuclear onion (NUC-01 failed); 15.5 Kelvin, Tait, Skyrme-Faddeev, tight knots (P-01: published corrected version 3.1 sigma, uncorrected 2.4 sigma); 15.6 anyons, hopfions, vortex knots; 15.7 sphaleron, Skyrme, gluon knots; 15.8 electron not modelled as a knot; 15.9 Og, element 119, Lr, f-block (killed).
- Appendix D test ledger extended to pre-registrations at 22:57:34Z and 24 Sept 00:13Z, 01:07Z.

### TEST_RECORD v1 (23 Sep 2026)
- Scoreboard of T-A, T-A+, T-K, T-K2, T-N, T-P, controls, T-J (11, 12), blind pairs 11 (44 pairs: 16 equal volume, 28 different volume; colour 3 separates 24 of 26 computable), T-E, T-E2, T-F, T-D, T-B, T-M, T-I, T-S, T-L, T-O (killed at 6 steps), T-H, ridge census, T-Q (thinning, 6/12), T-C and T-G blocked (need data pages).
- States "Which numerator produced each table entry was not verified; only the energies were read twice" (section 1.7).

### Gap Research (25 Sep 2026, "VOTKP v1.0: closing the remaining gaps")
- Determination: one limited replication (atomization row height), two exact boundary results (atom-to-film optical sufficiency counterexample; Maxwell sheet bridge), no new proof of the universal physical bridge.
- §1 atomization relation A_p = sum_Z E_at f(x_Z) / sum_Z f(x_Z)^2 with f(x) = 4x(1-x); candidate coefficient (96.4853321233/3) kJ/mol per eV, identified after looking at the data. Reproduced on two full JANAF rows (Li-F, Na-Cl); "post-hoc", "not a blind test".
- §2 H_theta = R_theta diag(0,1) R_theta^T; transition strengths 0, 1/8, 1/4 at theta = 0, pi/8, pi/4 with identical spectra. Sheet bridge r = (n0 - nb - Z0 sigma)/(n0 + nb + Z0 sigma); synthetic sigma = 0.003 + 0.002i gives R = 0.23463 vs 0.04 for glass.
- §3 Hydrogen loop basis (Mathur and Sreeraj): j(j+1) = (n^2-1)/4; affine fit E_H = E_loop - 1 gives +1 at n=3 vs Coulomb -1/9 (difference 10/9; I re-derived this, it is correct). SU(3) plaquette: <f|V|0> = -kappa/2 (re-derived, correct); seeded Monte Carlo -0.5073 - 0.0034i.
- §4 BESIII X(2370) and a Sigma-Sigma-bar counteranalysis; no knot-operator overlap supplied.
- Decision ledger (§ end).

## 3. Element-specific results (every element with a number in the five versions)

Quantities: IE = ionization energy (eV); "tau_1" = ln(IE2/IE1) (peel step, first); "step" = ln of shell jump; Gamma = tanh(tau/2); R = normal-incidence reflectance; "bump" = reflectance rise before fall on thinning.

| Element (symbol, Z) | Quantity | Number | Section |
|---|---|---|---|
| Hydrogen (H, 1) | H-: theory tau = ln(IE/EA) | 2.89134, Gamma 0.89483 | v0.5 15.3 |
| Deuterium D- | tau | 2.89180(10), Gamma 0.89488 | v0.5 15.3 |
| H- (measured) | tau | 2.89206(2), Gamma 0.89491 | v0.5 15.3 |
| Positronium Ps- | tau theory / measured | 3.0361 / 3.0355(4); Gamma 0.9084 / 0.9083 | v0.5 15.3 |
| H- to Ps- shift | tau | +0.143 | v0.5 15.3 |
| proton to deuteron | tau shift | -2.6(1.0) x 10^-4 (specific mass shift residual 1.55(62) cm^-1) | v0.5 15.3 |
| Helium (He, 2) | tau_1 | 0.7945 (Gamma 0.3776 by my arithmetic) | v0.5 15.5 |
| Lithium (Li, 3) | IE1 5.39, IE2 75.64; tau_1 | 2.641 (Gamma 0.8669) | v0.2 8.6; v0.5 8.6, 15.5 |
| Lithium (Li, 3) | polarizability trend | alkali first-step maximum | v0.1 8.3 |
| Beryllium (Be, 4) | correlation hole | about 2 A base; 4-5 A at 21 eV plasmon (cited, not computed) | v0.1 4.1; v0.2 4; v0.5 4, 15.1 |
| Oxygen (O, 8) | IE_6, IE_7; ratio | 138.1189, 739.32697; 5.35283 (v=6) | v0.1 Table 3 |
| Aluminium (Al, 13) | IE_3, IE_4; ratio | 28.447642, 119.9924; 4.21801 (v=3) | v0.1 Table 3 |
| Aluminium (Al, 13) | film | strong reflector, no bump; echo weight 0.57-0.87 | v0.5 15.2 (H-01) |
| Sodium (Na, 11) | tau_1 | 2.219 (Gamma 0.8039) | v0.2 8.6; v0.5 8.6 |
| Sodium (Na, 11) | 10 steps IE1 to IE11 | Gamma 0.9938; distance ln(IE11/IE1) = 5.77 | v0.5 15.2 |
| Sodium (Na, 11) | film | strong reflector, no bump (Al, Mo, Ta, Zn, Mg, Pb group) | v0.5 15.2 |
| Magnesium (Mg, 12) | nuclear N=20 closure | gone at Mg (nuclear, Z=12) | v0.5 15.4 |
| Argon (Ar, 18) | IE_8, IE_9; ratio | 143.4567, 422.6; 2.94584 (v=8) | v0.1 Table 3 |
| Argon (Ar, 18) | tau_1 at element | 0.561 | v0.5 15.9 |
| Argon (Ar, 18) | ridge at 18 electrons | prominence 0.533 near / 0.191 mid / 0.052 deep | v0.2 8.4; v0.5 8.4 |
| Potassium (K, 19) | tau_1 | 1.986 (Gamma 0.7586, past the wall) | v0.2 8.6; v0.5 8.6 |
| Calcium (Ca, 20) | nuclear N=34 | present only in Ca (nuclear) | v0.5 15.4 |
| Calcium (Ca, 20) | nuclear N=28 | 0.40-0.42 (Ar, K, Ca) | v0.5 15.4 |
| Scandium (Sc, 21) | polarizability line share | 121% of alpha from listed lines | v0.5 8.5 |
| Chromium (Cr, 24) | nuclear N=28 | falls to 0.19 at Cr | v0.5 15.4 |
| Iron, Cobalt, Nickel, Mo, Nb, Ti, V, W, Co, Os, Ir, Rh, Pd, Ta, Zn, Pb (film set) | film bump | no bump for Al, Mo, Ta, Zn, Mg, Pb; each in 171-case table | v0.2 6.4; v0.5 6.4 |
| Copper (Cu, 29) | IE1 | 7.726380 eV | v0.1 Table 2; v0.2 Table 2; v0.5 Table 2 |
| Copper (Cu, 29) | shell step (k=11) | 101.67 eV | same |
| Copper (Cu, 29) | R at 450 / 550 / 650 nm | 0.538 / 0.624 / 0.935 | same |
| Copper (Cu, 29) | film bump | 450 and 550 nm (bump) | v0.2 6.4; TEST_RECORD T-Q |
| Zinc (Zn, 30) | film | no bump | v0.5 15.2 |
| Silver (Ag, 47) | IE1 | 7.576234 eV | Table 2 |
| Silver (Ag, 47) | shell step (k=11) | 83.46 eV | same |
| Silver (Ag, 47) | R at 450 / 550 / 650 nm | 0.980 / 0.983 / 0.990 | same |
| Silver (Ag, 47) | film | |Gamma| > 0.99, never bump | v0.2 6.4; TEST_RECORD T-Q |
| Gold (Au, 79) | IE1 | 9.225554 eV | Table 2 |
| Gold (Au, 79) | shell step (k=11) | 79.80 eV | same |
| Gold (Au, 79) | R at 450 / 550 / 650 nm | 0.408 / 0.792 / 0.957 | same |
| Gold (Au, 79) | film at 450 nm, n_s=1.5 | R = 0.408191 (200 nm), 0.426742 (58.2093 nm, max), 0.163082 (10 nm) | v0.1 6.4 |
| Gold (Au, 79) | Hovel check (Au on Si/SiO2) | percolation near 6-7 nm; 200 nm oxide | Gap §2 (cited) |
| Gold (Au, 79) | Gamma and bump | bump at 450 nm; interband absorption lowers |Gamma| | v0.2 6.4; v0.5 6.4 |
| Gold (Au, 79) | swap with titania (gold facing light) | R = 0.509 vs 0.433 at 550 nm | v0.5 15.2 |
| Gold (Au, 79) | receiver metamer | (0.15340748, 0.16429085, 0.08396012) vs (0.15895741, 0.15556920, 0.08525305) | v0.1 6.3; v0.5 6.2 |
| Platinum (Pt, 78) | IE1 | 8.95883 eV | Table 2 |
| Platinum (Pt, 78) | shell step (k=10) | 75.5 eV | same |
| Platinum (Pt, 78) | R at 450 / 550 / 650 nm | 0.588 / 0.641 / 0.678 | same |
| Platinum (Pt, 78) | film bump | at 450, 550 and 650 nm (all three) | v0.2 6.4 |
| Rhodium (Rh, 45) | IE_9, IE_10; ratio | 135.0 (C), 207.51; 1.53711 (v=9) | v0.1 Table 3 |
| Ruthenium (Ru, 44) | IE_8, IE_9; ratio | 110.0 (C), 178.41; 1.62191 (v=8) | v0.1 Table 3 |
| Tellurium (Te, 52) | IE_6, IE_7; ratio | 69.1, 124.2; 1.79740 (v=6) | v0.1 Table 3 |
| Hafnium (Hf, 72) | IE_4, IE_5; ratio | 33.37, 68.37; 2.04885 (v=4) | v0.1 Table 3 |
| Hafnium (Hf, 72) | depth miss beyond K=10 | Hf, Ta miss at 11-12 | v0.2 8.3; v0.5 8.3 |
| Tantalum (Ta, 73) | depth miss beyond K=10 | as Hf | v0.2 8.3 |
| Krypton (Kr, 36) | IE_8, IE_9; ratio | 125.802, 233.0; 1.85212 (v=8) | v0.1 Table 3 |
| Krypton (Kr, 36) | tau_1 at element | 0.554 | v0.5 15.9 |
| Lead (Pb, 82) | IE_4, IE_5; ratio | 42.33256, 68.8; 1.62523 (v=4) | v0.1 Table 3 |
| Polonium (Po, 84) | IE_6, IE_7; ratio | 69.1 (C), 108.0 (C); 1.56295 (v=6) | v0.1 Table 3 |
| Radon (Rn, 86) | tau_1 at element | 0.569 | v0.5 15.9 |
| Radon (Rn, 86) | polarizability | 35 a.u. (Pershina, cited) | v0.5 15.9 |
| Xenon (Xe, 54) | tau_1 at element | 0.548 | v0.5 15.9 |
| Xenon (Xe, 54) | ridge at 54 electrons | -0.028 mid, -0.004 deep (vanishes) | v0.5 8.4 |
| Neon (Ne, 10) | tau_1 at element | 0.642 | v0.5 15.9 |
| Neon (Ne, 10) | covalent radius reset | fails (noble gas minimum 4/6) | v0.2 8.6 |
| Oganesson (Og, 118) | IP1, IP2; tau_1 | 8.888, 16.195 eV; tau_1 = 0.600 (Gamma 0.2913 by my arithmetic) | v0.5 15.9 |
| Oganesson (Og, 118) | polarizability | about 58 a.u. (Pershina 2008, predicted) | v0.5 15.9 |
| Element 119 | IP1 | 4.784 eV (predicted) | v0.5 15.9 |
| Lawrencium (Lr, 103) | IP1 | 4.96 eV (measured, Sato et al.) | v0.5 15.9 |
| Francium (Fr, 87) | tau_1 at element | 1.705 (Gamma 0.6924, below the wall) | v0.2 8.6; v0.5 8.6 |
| Rubidium (Rb, 37) | tau_1 | 1.877 (Gamma 0.7345) | v0.2 8.6 |
| Caesium (Cs, 55) | tau_1 | 1.783 (Gamma 0.7121) | v0.2 8.6 |
| Sparse-data elements | grade D | Tc, Pm, Po, At, Rn, Fr, Ra, Ac, superheavy | v0.1 2.4 |
| Ni-like closure (28 electrons) | ridge prominence | 0.284 near / 0.487 mid / 0.478 deep | v0.2 8.4 |
| Pd-like closure (46 electrons) | ridge prominence | 0.266 / 0.358 / 0.149 | v0.2 8.4 |
| 60-electron closure ([Kr]4d10 4f14) | predicted weak ridge, Z >= 88 | estimated stages only | v0.2 8.4 |
| Carbon, boron, beryllium K-shell openings | (from the frame, not in these versions) | no number in these versions | absent |

Also listed without numbers: Au "gold-air interface" surface response (Feibelman, cited); Ce, Zr, Hf allotropes (Appendix C only); "Ag never shows" bump.

Shape/level split (paper's own table, v0.2 8.5 and v0.5 8.5): covalent radius peel-beats-static 0 of 9; atomic radius 0 of 9; hardness 1 of 9; electron affinity 4 of 9 (mixed).

## 4. Bold moves (the mathematical move, its assumptions, and whether a later version dropped it)

1. Peel steps as rapidities (v0.5 Thm 15.1, Cor 15.2, Cor 15.3). The move: take Gamma = tanh(tau/2) with tau = ln(IE_{k+1}/IE_k), so tanh addition gives Gamma_{k->l} = Gamma_k (+) ... (+) Gamma_{l-1}, where (+) is the velocity-addition law. Assumes real Gamma (the atomic chart is real). The film version uses the same algebra with complex Gamma, and the hyperbolic reading holds only for real Gamma (v0.5 15.2 says so explicitly). The reading as a Poincare-disk distance is absent from v0.1 and v0.2 (both carry Theorem 8.1 without the rapidity reading). Added in v0.5.
2. Echo weight as derivative of the composition: d(Gamma (+) x)/dx at x=0 equals 1 - Gamma^2 = sech^2(tau/2) = 1/gamma^2 (v0.5 Cor 15.3). Assumes the film map r = (Gamma+x)/(1+Gamma x). Present in v0.2 as Theorem 6.1 (echo expansion, with 1-Gamma^2 = t01 t10) and in v0.5 with the rapidity reading added. The separator built on it (H-01) was killed in v0.5 (0.743 vs 0.96-0.98). The move survives as algebra; the predictive use was killed.
3. Front-surface echo gives a non-monotone thinning peel (v0.1 6.4 and v0.2 6.4). The move: R(d) = |Gamma|^2 + 2 Re[...] first order, so thinning can raise R before it falls. Assumes r12 phase; the bump is explained by a sign of Re[Gamma-bar (1-Gamma^2) r12 p^2]. Survived into v0.5 and TEST_RECORD (6 of 12; 171 cases).
4. Associator of reduced products (v0.5 15.2): (x*y)*z - x*(y*z) = P[x(I-P)(yz) - (I-P)(xy)z]. Checked to 1e-15. The move: what one reduction discards can reappear in the next; zero-phase film stacks telescope (order drops out), but phase restores order. Added in v0.5.
5. Dual-step decomposition for the film at zero phase: r = r01 (+) r12 (+) ... = tanh((1/2) ln(N0/Nn)). Telescopes exactly. Added in v0.5.
6. Mass-ratio axis for the peel coordinate (v0.5 15.3): a two-step peel M+ e- e- gives tau = ln(IE/EA); scale blindness (Thm 15.4: multiplying all masses by lambda multiplies energies only). Added in v0.5.
7. HOMFLY first classifies at 13 crossings; thin knots' Khovanov and knot Floer determined by Jones, Alexander and signature (v0.5 11.2 and 11.4). The move: a thin knot has all generators on one diagonal, so the graded Euler characteristic fixes every rank. Added in v0.5 (CAT-01 killed the "categorified rung separates all volume-different pairs" claim: 233 of 253 stay blind).
8. Colour phase window (v0.2 13.3; v0.5 13.3; TEST_RECORD T-N): a single evaluation at t = e^{8 pi i/15} predicts volume; window 1.46-2.42 rad; the same phase read as q fails (34.7%). Survived in all versions.
9. Torus control: omega = 0 identically on L = epsilon M^{-k} (v0.1 12.5; v0.2 13.5; v0.5 13.5). The move: the torus knot's A-polynomial potential is zero while T and L are nontrivial. Present in all versions.
10. A-polynomial integral check for the figure-eight: 2 int_0^{pi/3} log|L| dtheta = 2.0298832128193074 vs SnapPy 2.029883212819307 (v0.1 12.5 says it "should return" the volume and marks it Open, T-E; v0.2 and v0.5 state it as Exact). The Kashaev limit (2.734, 2.271, 2.106 at N = 50, 200, 800) appears only in v0.1 12.3.
11. Gap Research: the one-third row coefficient (JANAF) and the hydrogen-loop affine map E_H = E_loop - 1 (fit on n=1,2). Both are post-hoc fits by the paper's own admission; the affine map predicts +1 at n=3 against -1/9. Not in v0.1 to v0.5.

Dropped later (in one version, not the next): v0.1 §5.10 "one-energy snapshots" stays; v0.1 §8.1 "Run 01 kill condition" stays; v0.1 "Ar/Kr/Xe resets fade in deep ions" was replaced in v0.2 by a ridge census with numbers; v0.2 "285 pairs through 12 crossings" is changed in v0.5 to 354 pairs (adding 5 pairs through 10 and 63 across crossing numbers); v0.2 "Snell test" kept as a failure.

## 5. Connections to today's frame (quoted lines only; no softening)

Frame items present in these versions:

- Tanh form of the step. v0.2 Thm 8.1: "Gamma_k = (z_k - 1)/(z_k + 1) = tanh(tau_k / 2)". Same as frame "Gamma = (z-1)/(z+1) = tanh(1/2 ln z)". Frame length ln z = paper's tau_k; quoted: "the peel coordinate tau_k = ln(IE_{k+1}/IE_k) is the Smith log-impedance" (v0.5 Thm 8.1, paraphrase of the statement; the quoted words are in the theorem).
- Rapidity and Lorentz. v0.5 15.2: "In that language Gamma_k is a velocity and tau_k/2 a rapidity." And "Successive peel steps compose as successive boosts." And "Bondi's factor is k = e^{tau_k/2} = sqrt(z_k)." And Cor 15.3: "this is sech^2(tau/2) = 1/gamma^2, with gamma = cosh(tau/2) the Lorentz factor of the equivalent rapidity."
- Wall arithmetic in the paper's own formulas (my derivation from these lines; the paper does not state it). Since 1 - Gamma^2 = 1/gamma^2 (Cor 15.3), the wall Gamma^2 = 1/2 is gamma^2 = 2, i.e. cosh(tau/2) = sqrt(2), so tau = 2 arccosh(sqrt 2) = ln(3 + 2 sqrt 2) = 1.76275, z = 3 + 2 sqrt 2 = 5.8284, and sqrt(z) = 1 + sqrt 2 (checked: (1+sqrt2)^2 = 3+2sqrt2). Bondi's factor at the wall is 1 + sqrt 2. This is a derivation from the paper's formulas, labelled as mine.
- Alkali steps across the wall (my arithmetic on the paper's tau_1 values, v0.2 8.6 / v0.5 8.6): Li 2.641 (Gamma 0.8669), Na 2.219 (0.8039), K 1.986 (0.7586), Rb 1.877 (0.7345), Cs 1.783 (0.7121): all past 1/sqrt 2 = 0.7071. Fr 1.705 (0.6924) is below. The paper's list of "six largest values" includes Fr, which sits below the wall. Quoted line: "the six largest values in the table: Li 2.641, Na 2.219, K 1.986, Rb 1.877, Cs 1.783, Fr 1.705" (v0.2 8.6).
- Shell-jump threshold (not the wall). v0.2 Fig 1 caption: "cream points are shell jumps (Gamma > 0.5)". v0.5 8.1: "A shell jump means a high-reflection layer: Gamma from about 0.5 up to 0.87 for the alkali first step."
- Phase survives where amplitude is lost. v0.1 5.7: "Intensity can erase phase." And "A response can look information-poor because the instrument discarded the quadrature it needed." v0.5 15.2: "Only the phase makes order matter." v0.5 Fig 12 caption: "Order matters only through the phase between additions." This is the closest analogue to "phase crosses what amplitude cannot", but it is not a wall statement.
- Film threshold. v0.2 8.1 (figure) and v0.5 6.4 test: "the boundary sits near |Gamma| approx 0.93", "99.4% in sample", "0.96-0.98 with each metal held out". Calibration threshold |Gamma| <= 0.856 (v0.2). These are the paper's own walls for films, not 1/sqrt2.
- Spin, statistics. v0.5 15.8: "spin 1/2 and Fermi statistics" listed as requirements for an electron knot model (not met). v0.5 15.5: "bosons and fermions give the same helium-like peel (tau = 0.7945 for He). The first ridge needs a third fermion."
- Two books. The echo weight 1 - Gamma^2 = t01 t10 (v0.2 6.4; v0.5 6.4): "The factor 1-Gamma^2 = t01 t10 is the round trip through the front surface." Gamma^2 + (1 - Gamma^2) = 1 is an identity. The paper's test H-01 used |1 - Gamma^2| as a separator and killed it (v0.5 15.2: "The echo weight is the worse separator"). This is a point where the frame's book split and the paper's echo weight meet. Not stated by the paper as a book split.
- Tree or ball. Not in these versions. The Smith disk is read as the Poincare disk (v0.5 Cor 15.2: "On the Smith disk read as the Poincare disk, the distance from the centre to w is d(0,w) = 2 artanh|w|"). This is a hyperbolic ball of dimension 2, not a tree. Connection by structure only.
- Neutrinos, Koide, lambda-type spin walls: absent.
- Two checks that matched the frame: Garrett edge ratio 5 is Gamma = 2/3 by the paper's formula (not in these versions; my computation).

## 6. Anything that contradicts today's frame

1. The paper's atomic chart is real: "Because every z_k > 1, each Gamma_k lies on the positive real radius, so the atomic reflection chart has no phase." (v0.2 8.1, repeated in v0.5 8.1). The frame's "phase crosses what amplitude cannot" needs a phase on the disk; on the real radius the paper has none. The frame's wall lies on this real radius (Gamma = 1/sqrt 2), but the atomic record carries no phase there.
2. Thresholds differ: the paper's shell-jump cut is Gamma = 0.5 (v0.2 Fig 1; v0.5 8.1), its calibration threshold is 0.856 and its film boundary is 0.93. None is 1/sqrt 2 = 0.707. The paper does not use the 0.707 wall anywhere.
3. The paper's mechanism for failures is resolution (depth or colour), not a wall. v0.2 8.3: "A short peel fails by resolution." v0.5 16: "In each case the failure at the lower rung was fully explained by what that rung could not reach." The frame's cancel/lock/convert is not in the paper.
4. Refraction (turning) was tested as an alternative to reflection and killed (v0.2 9; v0.5 9: "turning set ... 1 hit, 9 false and 5 missed"). The frame's wall behaviour is "parabolic on it, does not close past it", which is a turning-type claim; the paper's own turning test failed for the atomic record.
5. Echo weight as separator killed (v0.5 H-01: 0.743 vs 0.96-0.98). If the frame's two-book split used 1 - Gamma^2 as a separator on films, the paper already tested and rejected it.
6. Frame's "8 of 5,737 steps past the wall": no such count in any version. The versions list the six largest tau_1 only. Be, B, C K-shell openings: absent. I cannot confirm or deny these numbers from these versions.
7. The paper's v0.5 "Lr lowest of actinides" and v0.5 "f-block does not transfer" are the paper's own kills; they do not touch the wall.

Internal inconsistencies noted for the main session (not against the frame):
- v0.2 abstract says "285 pairs of distinct knots through twelve crossings are identical on HOMFLY, Alexander and Jones"; the 285 excludes the 5 pairs through 10 crossings listed in v0.2 Table 5 context. v0.5 gives 354 (= 285 + 5 + 63 + 1).
- v0.2 abstract "polarizability alpha propto IE1^{-3.04} (R^2 = 0.91)"; body gives R^2 = 0.906 (rounding).
- v0.1 §8.2 "Ar, Kr, Xe resets ... fade in deep ions" vs v0.2/v0.5 "Ar and Kr shrink tenfold, Xe vanishes, Ni-like 28 grows" (wording change, same data).
- v0.1 §12.5 states the figure-eight integral "should return 2.0299 [Open, T-E]"; v0.2 and v0.5 state it as [Exact]. TEST_RECORD T-E: passed.
- Gap Research: the one-third coefficient is labelled post-hoc and the file says so; the derivation is not given.

## 7. Notes for the main session

- Memory: no memory items were used for this reading. The frame came from the brief.
- Scripts were not run. All arithmetic I quote beyond the paper's text (the wall derivation, the six alkali Gamma values, Og Gamma, He Gamma, the affine-map check, the SU(3) Haar value) was checked with python3 -I or by hand, as stated inline.
- Files written: /home/claude/sm/votkp_reads/READ_A3.md (this file); decoded sources in /home/claude/sm/votkp_reads/src/A3/; extracted text in /home/claude/sm/votkp_reads/text_A3/; helper scripts /home/claude/sm/votkp_reads/scripts/decode_A3.py and strip_A3.py. No Drive, GitHub or other file was edited or pushed.
