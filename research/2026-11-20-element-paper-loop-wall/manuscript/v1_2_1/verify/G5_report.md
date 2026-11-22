# G5 verification report: 09_colour, 13_russell, 14_ledger, 15_prior_art, 16_lean, 18_sources

Verifier: G5. Sources read only. Scripts: /home/claude/paper_v12/verify/scripts/g5_bmn_screw.py (beta-Mn screw recompute). Lean was rebuilt in a scratch copy (/tmp/g5lean) with /opt/lean/lean-4.34.1-linux/bin/lean using lean/run_checks.sh: 140 and 117 theorem builds OK, source scan OK, 11 controls rejected (each for the right reason: the statement is false, e.g. C_inside gives "grind failed" on the negated goal). TwoFaceForms.lean (3) and BoundaryAgreement.lean (11) also compile, with standard axioms only.

Paths below are relative to /home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/ (call it ELEM) unless stated. EJ pages = /home/claude/paper_v12/verify/ej_pages.md (present; used). Mixin repo = /home/claude/mixin-colors (present).

## A. WRONG, OVERSTATED, UNTRACEABLE (first)

| file | quoted claim | verdict | evidence / correction |
|---|---|---|---|
| 13_russell | "current-induced magnetisation and the circularly polarised Raman shift both reverse between the two hands (Furukawa et al. 2017)" | WRONG | Furukawa, Shimokawa, Kobayashi, Itou, Nat. Commun. 8, 954 (2017) has no Raman measurement; it reports a current-polarity-dependent 125Te NMR shift on a right-handed (P3_121) crystal only, and notes opposite spin textures of the two hands as a symmetry expectation (fetched nature.com/articles/s41467-017-01093-3). The direct absolute-hand measurement already in the repo is Tanaka et al. 2010 (circularly polarised resonant diffraction, ELEM/batch11/screw/README.md). Circularly polarised Raman of chiral Te is a different paper (Ishito et al., arXiv:2212.02720; journal not confirmed). |
| 13_russell | "cos theta = 1/(3Q) ≃ 0.500001652" | WRONG | Source says cos² of the angle = 1/(3Q) = 0.500001652 (origin/claude/sm-ball-20261111:research/2026-11-11-standard-model-ball/NOTES_SM_IN_THE_BALL_20261111_v1.md:33; ATLAS_REPORT_1.md:205 gives 0.5000016525). cos theta itself is about 0.70711. Fix: cos²θ. |
| 14_ledger | "At depth parameter 109 the twin-chain turn was still changing" | WRONG (almost certainly lost superscript) | T2_twin_turn_REPORT.md (origin/claude/sm-ball-20261111:research/2026-11-12-harness/reports/): cut-off reached 1e9 (first twin pair at or above 10^9 is 1000000007; 3,424,504 steps), turn 12.2695 deg, moved 0.1970 deg between 1e7 and 1e9, kill line fired. Should read 10^9. |
| 09_colour | "methane's 2 : 1 is the one point where the two ladders meet" | WRONG | The alkane ladder (3n+1)/2 = 2, 3.5, 5, 6.5, 8 (arithmetic correct) meets her even ladder 2, 4, 6, 8 at two points: 2 (methane) and 8 (pentane). |
| 16_lean | table row "`smith_identity`, `gam_inverse`" and the claim that every statement is core-only, no Mathlib | WRONG for smith_identity | `smith_identity` is not in any of the four files named. LoopWall.lean line 7 says it is "proved for reals in votkp-lean `VOTKP.Smith.smith_identity`" (origin/main:VOTKP/Smith.lean:42, a real-analysis, Mathlib theorem on tanh and log). `gam_inverse` is in LoopWall.lean (verified). Fix: drop smith_identity from the core-only table or say it lives in the Mathlib part of votkp-lean. |
| 16_lean | "Running `sh run_checks.sh` in the `lean/` folder builds: ... TwoFaceForms.lean ... BoundaryAgreement.lean" | WRONG | lean/run_checks.sh builds only LoopWall, OpeningMap, Audit, AuditMap and the controls. TwoFaceForms.lean is in lean/ but is not built by it (compiles when run directly). BoundaryAgreement.lean is not in lean/: it is at ELEM/russell/prediction_review_20261121/consistency/BoundaryAgreement.lean, built by consistency/check.sh. |
| 16_lean | "The axiom audit prints only propext, Classical.choice, Quot.sound for every theorem" | OVERSTATED | lean/run_checks_output.txt has 89 audited theorems (Audit.lean 75 prints + AuditMap.lean 14), against 140 + 117 theorems. The 11 BoundaryAgreement and 3 TwoFaceForms theorems are audited in the separate logs (consistency/lean_audit.txt, complete_kernel_log.txt). All printed audits are standard-axioms-only, so the content is right but "every theorem" in run_checks is not. |
| 16_lean | "A further 75 named theorems across 11 self-contained research modules" | OVERSTATED | complete_kernel_log.txt: 11 modules, 75 theorems, but its first two modules are TwoFaceForms (3) and BoundaryAgreement (11), already counted above. Only 61 are further. The 75/11 numbers themselves are correct (russell/prediction_review_20261121/complete_kernel_log.txt line 13). |
| 14_ledger | item 1: "it is the one equal-face cutoff for which the sum and product forms of the two-face rule agree (Lean-proved)" | OVERSTATED | Scope in the source: uniqueness among two specific named continuations (additive x+y-2t and product-of-odds) at a common threshold t, over rational squared reflections (consistency/README.md; BoundaryAgreement.lean `uniqueInteriorBoundary`, `wrongThird`). manuscript CHECKLIST D12 requires the qualifier "of the two named extensions". |
| 18_sources | "*What Russell Saw* and *Russell, Corrected* (November 2026)" | WRONG (date of the first) | russell/prediction_review_20261121/RUSSELL_VACANCIES_v1_20261121.md line 3: *What Russell Saw* is dated 26 September; *Russell, Corrected* is 3 November. |
| 13_russell | "Russell's numbers match the Rowland-scale iron tables of his day, so he was reading real published spectra" | OVERSTATED | history_ledger/IRON_COLUMNS_v1.md: Kayser 1910 gives concrete Rowland entries rounding to Russell's tenth for one example per column (3 lines: 4859.9, 5191.6, 5328.2). The same file says "Russell's acquisition source remains unknown". Supported: "at least one line per column matches"; not supported: that he used those tables. |
| 13_russell | "two raters coded 24 masked Russell verdicts" | OVERSTATED (omission) | spatial_mirror_pilot/README.md: the two raters were two Codex AI workers with fresh contexts, "not independent human historians". Counts 23 of 24, 20 agreed-even, 10 T / 10 F are right. |
| 09_colour | "In Elizabeth's Mixin system the secondary colours sit at a degree of polarisation 1/√2" | OVERSTATED (source found; attribution too strong) | Source: /home/claude/mixin-colors/deep-dive/t4_two_books_light.py (header line 20, check C) and t4_result.json `C_recipes` (Green2, Cyan4, Yellow6, Magenta8 all DOP 0.707107; Brown0 DOP 0; Red+Black 0.707107; 2Red+Black 0.745356). It is a result of Claude's mapping of her primaries to linear polarizers at 0/45/90/135 deg with incoherent mixing, PASS to 1.1e-16. The repo's own limits: "Polarization is not hue", and the model files call the states "abstract pure states or polarization encodings; not derived optical hues". Her notebook pages do not mention Mixin or degree of polarisation (ej_pages.md note). Same value also appears in his Colour Selects the Leader ledger (origin/claude/matter-disk:matter-disk/corpus-notes/colour_selects_leader.md:23). Fix wording: "In the polarisation encoding of the Mixin labels (mixin-colors deep dive) the secondaries sit at DOP 1/√2." Mixin repo is not on the votkp-lean branches; it is the separate mixin-colors repo (HEAD 140df68). |
| 09_colour | "where her page turns from easier to harder" (wall between 4:1 and 6:1) | OVERSTATED | EJ page 5/6: only "2 easier", "10 harder" under 2 4 6 8 10; no turning point is marked. The table arithmetic is right (Γ² 0, 0.111, 0.360, 0.510, 0.605; wall 3+2√2 = 5.828). |
| 09_colour | "Her questions, answered. Layered ... conveyor belts ... inserted charge ... too close to the ceiling ... speed of light and the charge" | UNTRACEABLE | None of these questions is on the seven transcribed notebook pages (ej_pages.md). They may come from messages the user relayed; needs the user's pages or messages. |
| 09_colour | "We reached the split separately" (matter/memory vs E+/E-) | UNTRACEABLE | Her page 1 does say "Matter = positive, Memory = negative, Matter + Memory = Firework" (verified). That the user's two books were reached independently is a statement about history; only the user's own say-so (memory: the two books are his, from the connection-energy work) can confirm it. |
| 09_colour | "the columns 1, 3, 7, 9 of her grid are the possible last digits of every prime above 5, and gap 2, the twin primes, is her tinder" | UNTRACEABLE on these pages | ej_pages.md note: "columns 1,3,7,9 ... last digits of primes" and the "twin primes" reading are Claude's reading of her grid; her words are "2 = Tinder", "Kindling is a twin segment with a ton of gaps". The user's memory says her separate page on end digits, gaps and codes (primes cut at twin pairs) is hers, which supports "her prime-gap work" but is a different page. Mark as reading, or have the user confirm. |
| 09_colour | "in the October finite-film test a frozen reflection threshold scored 87%" | OVERSTATED (date and object) | origin/claude/sm-ball-20261111:paper/votkp_v3_1/code/closure_reports/REPORT_ledger.md:55 (CLOSE C3): frozen threshold |Γ| = 0.856 on the Smith radius, 171 film cases, kill line accuracy under 85%, scored 87% (rerun 0.871); registered 23 September ("23 Sep unless stated"). Not shown to be October. It is a threshold on |Γ| for film bump labels, not a bulk-reflectance threshold. |
| 15_prior_art / 18_sources | Lyu, Keitel, Harman, *Phys. Rev. Research* 7, L042071 (2025) | UNTRACEABLE (volume and article number) | Authors, title "Periodic table for highly charged ions" and DOI 10.1103/bppp-53g1 confirmed (arxiv.org/abs/2504.11237; journals.aps.org URL exists) but the APS page could not be fetched, so 7 and L042071 are unconfirmed. |
| 15_prior_art | "I found no published use of ω = η, η/χ = 1/√2 or IE/EA = 3+2√2 as a boundary; the nearest published special ratio is IE/EA = 3" | UNTRACEABLE | Absence claim; the one point I could test (Pineda-Urbina has no (I-A)/(I+A), no η/χ, no ω = η, no IP/EA threshold) is verified, but "nearest special ratio is 3" has no source in my search. |
| 18_sources | "*The Ledger Outlives the Metric* (edition 7)" | UNTRACEABLE | corpus-notes/gravity.md read "Gravity_Ledger_Full_Research_Edition_6_20260924.pdf" (24 September). No edition 7 found. |
| 18_sources | "*The Offset Speed Limit* and *The Weight Between* (v1.1, 26 October 2026)" | UNTRACEABLE | corpus-notes/offset_speed_limit.md: "no copy of the paper text exists on Drive"; only the 2026-10-26 "Five separate papers v1" listing. v1.1 not confirmed. (The Offset Belongs to the Boundary v31 is confirmed: the_offset_belongs_to_the_boundary_v31.pdf in the Zenodo-current Drive folder.) |
| 18_sources | Galactic paper title and "17 September 2026" | OVERSTATED (version) | Title and 17 Sep date match the user's memory (v2, 2026-09-17). The same programme also has Research revision 4 (25 Sep 2026) titled "...with a Verified Interface Block: Transient Amplification and a Testable Filament Hypothesis" (corpus-notes/filament.md). The paper should say which. The memory also records a correction owed on that paper (PSR J1744-2946 is not at the Snake), which does not touch 13_russell's Jordan-block maths. |
| 18_sources | zirconium "J. Chem. Phys. 147 (2017)", yttrium "J. Chem. Phys. 158, 084303 (2023)" | PARTIAL | Zr is Fu, Li, Luo, Chen, Ning, JCP 147, 064306 (2017) (Wikipedia EA data page citation); add the article number. Y: Zhang, Lu, Tang, Ning, "Electron affinity of atomic scandium and yttrium...", JCP 158 (issue 8), 2023, DOI 10.1063/5.0124882; article number 084303 not shown by the source, issue 8 is consistent. |
| 18_sources | Souza-Wilkens-Martin (2000); Resta (2006); Müller (2009); Al Shorman (2013); McLaughlin (2017); Crandall (1979); Moon (1983); Storm (2026); Laporte (1987); Harvey and Lemmon (2005); Pettersson (1982); Moore NBS (1985); Toffoli (2022); Bohr (1922); storage-ring 205Tl (2024); bare 187Re (1996); Re-Os mass (2021); Yerokhin, Patkóš, Pachucki (2022); NIST ASD v5.12 | UNTRACEABLE (incomplete citations) | Given only as author and year, with no title, journal, volume or page, so nothing can be confirmed. Yerokhin, Patkóš, Pachucki 2022 matches arXiv:2206.14161 (title "QED calculations of energy levels of helium-like ions with 5 ≤ Z ≤ 30", June 2022) but the journal reference was not shown. Full details needed. |

## B. VERIFIED, with evidence

### 09_colour
| claim | evidence |
|---|---|
| 41 elements with optical data; 35 metals all above 1/2, 6 non-metals (B, C, Si, Ge, Se, Te) all below | ELEM/ptable/ptable_data.json, `optic.mean_R` and `optic.metal`: recomputed 35/6; all metals > 0.5, all non-metals < 0.5. Also origin/main:research/2026-11-07/README.md ("metals 35/35, non-metals 0/6"). |
| niobium 0.5026, tellurium 0.4940 | ptable_data.json: Nb 0.5026405 (lowest metal; next Bi 0.5275), Te 0.4940088 (highest non-metal; next Ge 0.4857). |
| data are the vacuum-disk paper v6 refractive-index sets | ptable_data.json `source`: "optics from the vacuum-disk paper v6 (refractiveindex.info)". |
| 39 pairs similar in bulk, rank correlation 0.64 | origin/main:research/2026-11-07/README.md line 16: "39 bulk-matched metal pairs ... Spearman ρ = 0.64". |
| osmium at 650 nm: 0.48460 and 0.52845 | batch16/materials/optics.csv lines 4 and 7 (Os ordinary 0.48460484, extraordinary 0.52845247, 0.65 µm). |
| R-1/2 has the sign of (n-3)²+κ²-8; `circle_identity` in OpticalWall.lean | batch8/material_transport/OpticalWall.lean:11-12 (compiled; standard axioms). Note the file is among the 75-theorem modules, not the 140/117/3/11. |
| drum: Γ = 4/10 and E-/E+ = 16/100; midpoint 5, half-gap 2, Γ = 2/5 | arithmetic; her words on page 4: "to go from 3:7 ... requires a 4 drum to get 3 to activate 7". |
| matter positive / shell and sections; memory negative / recipe; matter + memory = firework | EJ page 1, verbatim. |
| pilot hole: memory photon runs ahead A to B, picks best path, returns to A before matter makes the run | EJ page 1 ("sonar", "instantly returns to A for Matter to make the most efficient run"). |
| ratios 2:1, 4:1, 6:1, 8:1, "gap is the oxygen amount", 2 easier, 10 harder, 1:1 "furthest away from itself" | EJ pages 5/6 and 7 (page also writes "1:1 3:3"). |
| tinder / kindling / firewood roles; "Efficiency is Fastest OR Maximum Energy ... Can't be both" | EJ pages 3, 5/6. |
| alkane oxygen (3n+1)/2 = 2, 3.5, 5, 6.5, 8 | arithmetic (CnH2n+2 + (3n+1)/2 O2). |
| Shiraishi, Saito, Tasaki 2016 and Pietzonka, Seifert 2018 | PRL 117, 190601 (arXiv:1605.00356, Shiraishi, Saito, Tasaki, "Universal trade-off relation between power and efficiency for heat engines"); Pietzonka and Seifert, "Universal trade-off between power, efficiency, and constancy in steady-state heat engines", PRL 120, 190602 (arXiv:1705.05817; pubmed 29799237). |
| "a recent Pareto-front result bounds the efficiency at maximum power by one half of the maximum efficiency, with zero power at maximum efficiency" | Almanza-Marrero, Roldán, Manzano, "Universal Pareto fronts and trade-off relations in multi-objective optimization of thermal machines" (arXiv:2603.19885): η at maximum power "universally bounded by half of the maximum efficiency"; bound η ≤ (1+√(1-P))/2 gives zero power at η = 1. The paper credits earlier derivations (its Refs. 6 and 50), so "recent" is fine but it is not the origin. |
| α ≈ 1/137 and the (Zα)² correction | standard; not paper-specific. |

### 13_russell
| claim | evidence |
|---|---|
| beta-Mn: P4_132 and P4_332; shortest-contact orbit step 2.3743 Å; χ = +9.9306 Å³; reversal keeps, mirror flips | gpt_batches/batch6_Fe_to_Zn_junction_and_screw.md lines 76-110 (COD 1539039, a = 6.3145 Å, Mn1 step 2.374319, χ +9.930608); recomputed independently by scripts/g5_bmn_screw.py: step 2.374319, χ 9.930608, reversed 9.930608, mirror -9.930608. |
| trigonal Se, P3_121, record 1534711, bond 2.30066 Å, χ +11.1638 stays/flips | checks/check_se_screw_v1.py header and check_se_screw_v1_output.txt (forward 11.1638, reversed 11.1638, mirror -11.1638, bond 2.30066). |
| trigonal Te, P3_121, record 2020222, bond 2.8345 Å, χ +21.2240; independent P3_221 gives -21.990034 | batch11/screw/tellurium_screw.txt and README (group 152: 2.834506 Å, +21.224043, reversal +21.224043, mirror -21.224043; group 154: -21.990034); batch11/materials/crystals.csv line 28 (Te, 2020222, P 31 2 1). The P3_221 model is Wyckoff 1963 (COD 9008580), a different refinement from Adenis et al. 1989, so "independently refined" is fair. |
| `chi_reverse`, `chi_mirror` exist | lean/LoopWall.lean (compiled). |
| Barron: true chirality odd under mirror, even under time reversal | Barron, "True and false chirality and parity violation", Chem. Phys. Lett. 123, 423-427 (1986) confirmed (eprints.gla.ac.uk/139209). |
| iron columns: 23 per column, 21/20/19 of 23 at ±0.20 Å | history_ledger/IRON_COLUMNS_v1.md and iron_controls_v1.csv (Fe I, ±0.2, zero shift: 21, 20, 19). |
| translation control, shifts -50..-5 and +5..+50; medians 7, 5, 5; maxima 12, 12, 10; 1/93 | iron_controls_v1.csv (medians 7.0, 5.0, 5.0; max 12, 12, 10; 92 controls, 0 at least as good). |
| Nave et al. extraction reproduces 21/20/19; ionised iron 2, 4, 2 | IRON_COLUMNS_v1.md table (Fe I Nave Table 4: 21, 20, 19; Fe II: 2, 4, 2). |
| Kayser 1910, at least one line per column rounding to Russell's tenth on the Rowland scale | IRON_COLUMNS_v1.md Kayser table (4859.928, 5191.629, 5328.236). Kayser, ApJ 32, 217 (1910) and Nave et al., ApJS 94, 221 (1994) are consistent with the ADS bibcodes in that file; Nave arXiv astro-ph/9404049 "A new multiplet table for Fe I" confirmed. |
| 5269.6 Å coincides with Fraunhofer E identified as iron 5269.551 Å in Abbot, *The Sun* (1911) | IRON_COLUMNS_v1.md (Abbot Table III p. 89, Sept 1911; Nave 5269.5374 Å). Not independently checked in Abbot's book. |
| octave values: O 9.320, S 4.988, Se 4.826, Te 4.571, F 5.123, Li 8.724, Li IE1 over F EA 1.585, Po 5.703 | ptable_data.json (`anion.z0` O 9.320327, S 4.987718, Se 4.826311, Te 4.571476, F 5.122566, Li 8.723766; Li IE1/F EA = 1.58524); Po 5.703 on the provisional affinity: batch17/polonium/scores.csv (5.70285; bracket 5.7024-5.7033). |
| vacancies at Tc, Pm, At, Fr; Bohr 1922 already shows them; Russell also leaves surplus places | RUSSELL_VACANCIES_v1_20261121.md lines 9-24 (Tc 43, Pm 61, At 85, Fr 87 "Bohr 1922 had" each; surplus places at Hf interval and Pt-Au). |
| 282 + 104 entries, 199 laws, 386, 132 of 585 | history_ledger/RUSSELL_LEDGER_REVIEW_v1.md table lines 11-14 (104, 282, 199; total 585; 132). |
| Schwarzschild κ_r²/Ω² = 1-6GM/(c²r); p_eff = 2+6GM/(c²r), 3 at the ISCO | algebra re-derived (3-p = 1-6M/r). |
| Jordan block: norm formula, gain above one exactly at κ > 2, t* = √(κ²-4)/|μ| | re-derived: ln norm = -bt + asinh(|μ|t/2); derivative at 0 gives κ > 2; stationary point √(4+x²) = κ. Matches memory (galaxy-holes v2). |
| e^η = 5: γ = 13/5, v = 12/13, ρ = 2/3 | arithmetic. |
| Koide Q = 0.666664463 | NOTES_SM_IN_THE_BALL_20261111_v1.md:33 (see the cos² correction above). |
| no exact cone hit among 117,186 tree nodes to depth 7 and 23,100 turn axes to depth 6 | origin/claude/sm-ball-20261111:research/2026-11-11-standard-model-ball/NOTES_SM_IN_THE_BALL_20261111_v3.md:108-109, 116; run2/cone_turn_02.out ("turn axes counted: 23100; within 1e-10 of cos² = 1/2: 0"). |
| 48 integral quaternions of norm five | r4(5) = 8(1+5) = 48. |
| spinor check residual 5.04×10^-7; flat-torus D² = (2π)²[...], eta zero; Schur effective hopping | spinor_recovery/check_spinor_recovery_v1_output.txt lines 6 and 7 (5.038154e-07; J_eff matches formula; D² 9.8696 = (2π)²/4). |
| twin discrepancy 7.0×10^-5 | origin/claude/moving-matrix-of-balls:research/the-ball-is-the-tree/tb_check_01_output.txt line 4 ("largest twin difference 7.0e-5"). The "2 log 3 path length" was not separately located. |
| Galactic paper: stable spectrum with transient gain; two-dimensional block | memory (galaxy-holes-paper) and re-derivation. |

### 14_ledger
| claim | evidence |
|---|---|
| E = 2/3 gives z_E = 3 and Γ_E = 1/2 | arithmetic: Γ_E = E/(2-E) = (2/3)/(4/3). |
| 81-row sheet: one exception at 2/3 (boron), two at 0.63 (arsenic, polonium) | origin/claude/sm-ball-20261111:research/2026-11-13-space-step/LEDGER_RAW_20261106.md item 6. |
| 35 metals, Spearman E vs log DC +0.072; E vs optical phase about +0.78 | same file item 4 (+0.072; +0.783) and item 9 (+0.785). |
| phase cutoff 0.661 rad, 41 members, fitted | same file item 2 ("41/41 at 0.661 rad (fitted)"). |
| silicon and germanium melting in density brackets; hydrogen, xenon near Herzfeld; expanded alkalis metallic | same file item 7 table. |
| signed optical-track area clockwise in 39 of 41; 60-material test 56 clockwise, 3 counterclockwise, 1 flat | same file items 1 and 8. |
| fixed sign-wall classifier misses 25 of 41 | same file item 2 (QWALL-01). |
| outlier rates 0.02 (f-block) to 0.44 (Zn-Cd-Hg); scalar-relativistic correlation weak pooled, convergence failures | same file items 10, 11 (R3 +0.087; list of non-converged runs). |
| knot census 353/251 vs printed 354/253 | origin/claude/sm-ball-20261111:research/2026-11-12-harness/PROGRESS.md line 22. |
| cap-fill bound survived, exact laws failed, 330-case control | PROGRESS.md lines 13-14 ("F1 lower envelope proven ... 0/330 violations; F1/F5/F6 killed"). |
| 24 runnable opposite controls, 13 fired, 11 did not; 5 unrunnable; 4 skipped | harness/reports/T4_opposites_REPORT.md lines 3-4. |
| two-step group: 0 elliptic words at the wall and outside, 240 inside (words up to length 10) | ELEM/connections/what_transport_keeps_connections.md lines 160-169 (118,096 words; nitrogen faces 240 elliptic; wall 0; carbon 0). The 240 is for one inside case (nitrogen's faces). |
| equality per pass at 6.26913 | PROGRESS.md line 39 (z* = 6.26913, y³-4y-2 = 0); T8 report ln z* = 1.83564. |
| exceptional-point condition of the two-moment closure matches the loop wall; full chain moves it | harness/reports/T13_neutrino_wall_REPORT.md B2 (holds exactly) and B3 (full-chain wall at kappa_c = 2k/π). |
| window [5.80790, 5.86654) silver to silicon | ELEM/README.md lines 12-13 (5.8079 and 5.8665); PREDICTION_FRANCIUM_20261121.md line 16 (5.80790, 5.86654); CLAUDE_REVIEW.md:188 (5.8079020598, 5.8665387761). |
| 3,570 ordinary steps, only eight outside, each a first core opening (Li, Be, B, C, Na, K, Rb, Cs) | recomputed from ptable_data.json: 3570 steps, outside exactly those eight; README.md line 12. |
| 53 of 65 adopted anion rungs outside; heavy-anion prediction 7 of 7 | ptable_data.json: 65 anions, 53 outside; README.md ("All seven adopted experimental point values agree"). |
| seven address classes; out-and-out class Li, B, C, Na, K, Rb, Cs | CLAUDE_REVIEW.md:585; recomputed from ptable_data.json. |
| holmium-dysprosium reverses order between 56+ and 57+ | CLAUDE_REVIEW.md line 481 (q = 56 +1951.4 eV, q = 57 -4518.6 eV). |
| neutrino papers *The Neutrinos at the Wall* and *When the Neutrinos Leave* | memory (neutrinos-at-the-wall) and work_atlas/STATUS.md (neutrinos-leave-lean). |

### 15_prior_art and 18_sources
| claim | evidence |
|---|---|
| Lyu, Keitel, Harman: relativistic-orbital filling, cell = isoelectronic sequence, no ratios of ionisation energies | arxiv.org/pdf/2504.11237 ("constructed purely based on the successive electron occupation of relativistic orbitals"). |
| *Atoms* 14, 60 (2026) follow-up studies scaling | da Silva, Da Silva, Matsushita, Caramori, "Thresholded Zipf Scaling Across 14 Highly-Charged-Ion Isoelectronic Sequences", *Atoms* 14, 60 (18 July 2026); builds on Lyu et al. |
| Pineda-Urbina, *Atoms* 14, 48 (2026): ΔSCF-DFT map for 26 main-group atoms H to Kr; χ = (IP+EA)/2, η = (IP-EA)/2, ω = μ²/2η; electrodonating and electroaccepting powers; no ratio, no threshold | Kayim Pineda-Urbina, *Atoms* 14(7), 48, DOI 10.3390/atoms14070048; full title adds ": Validation, Basis-Set Sensitivity, and Diagnostic Anionic States". Section 3.1 and eqs 3-6 confirmed in the PDF. |
| Washburn, Simons, Allahyarov, arXiv:2605.00028 (2026): noble-gas-centred axis, golden-ratio cosh function J(ρ) = cosh(ρ ln φ) - 1, IE1, EA, Mulliken χ, Pearson η | arxiv.org/abs/2605.00028 (Jonathan Washburn, Megan Simons, Elshad Allahyarov, submitted 22 Apr 2026). It also appears as *Symmetry* 18, 1087 (2026), which could be added. |
| Parr and Pearson, JACS 105, 7512 (1983); Parr, von Szentpály, Liu, JACS 121, 1922 (1999) | Titles "Absolute hardness: companion parameter to absolute electronegativity" and "Electrophilicity index" confirmed by search (DOI 10.1021/ja00364a005 and ja983494x); vol/page as cited consistent with the search records. |
| Resta and Sorella, PRL 82, 370 (1999) | arxiv.org/abs/cond-mat/9808151 page: Phys. Rev. Lett. 82, 370 (1999), "Electron Localization in the Insulating State". |
| Otero-de-la-Roza, Martín Pendás, Johnson, JCTC 14, 4699 (2018) | "Quantitative Electron Delocalization in Solids from Maximally Localized Wannier Functions", JCTC 14(9), 4699-4710, 2018 (digibuo.uniovi.es). Author order on that record is Johnson first; the standard citation order is as the paper has it; check once. |
| Onishi and Fu (2025) | "Quantum weight: A fundamental property of quantum many-body systems", Phys. Rev. Research 7, 023158 (2025). |
| Zimborás et al. (2013) | Sci. Rep. 3, 2361, "Quantum transport enhancement by time-reversal symmetry breaking" (arXiv:1208.4049). |
| Ning and Lu (2022) | J. Phys. Chem. Ref. Data 51, 021502 (DOI 10.1063/5.0080243). |
| arsenic PRL 134, 043001 (2025) | Blondel and Drag, "Quantum offset of velocity imaging-based electron spectrometry and the electron affinity of arsenic", PRL 134, 043001 (2025). |
| selenium JCP 164, 054303 (2026) | Zhang, Jie, Chen, Liu, Ning, "Revisiting the electron affinity of selenium", JCP 164(5), 054303 (DOI 10.1063/5.0311920). |
| rhodium Chin. Phys. B 35, 063202 (2026) | Chen, Zhang, Jie, Liu, Ning, "Accurate electron affinity of atomic rhodium and fine structure of its anion", Chin. Phys. B 35(6), 063202 (2026). |
| Yerokhin and Shabaev (2015) | "Lamb shift of n = 1 and n = 2 states of hydrogen-like atoms, 1 ≤ Z ≤ 110", J. Phys. Chem. Ref. Data 44, 033103 (arXiv:1506.01885). |
| Schweiger et al. (2024) holmium-dysprosium | Nature Physics (2024) "Penning-trap measurement of the Q value of electron capture in 163Ho for the determination of the electron neutrino mass" (s41567-024-02461-9). |
| Jung et al. (1992) bare 163Dy | PRL 69, 2164 (1992) "First observation of bound-state β- decay". |
| COD records 1539039 (β-Mn), 1534711 (trigonal Se), 2020222 (trigonal Te) | 1539039: batch6 note; 1534711: check_se_screw_v1.py header; 2020222: batch11/materials/crystals.csv line 28. |
| KnotInfo database 2026.9.1 | R1_versions.md (database_knotinfo 2026.9.1, Dirac Time v3.1 reproducibility note); not re-opened. |
| Zenodo record 24432624; branch commit 02515d0 | ELEM/manuscript/v1_2/RECORD.md line 19 (published by Jeromie as record 24432624); release_sources/READ_FIRST.md line 16; `git log` shows 02515d0 "Archive full joint review, pinned ball-model sources and original Zenodo deposit" (21 Nov 22:45), one commit behind the branch head. |
| Dirac Time v3.0.1 (25 Sept 2026) | corpus-notes/dirac_gigantefermion.md line 2 ("25 September 2026 ... Long Form v3.0.1"). v3.1 (26 Sept) rests on R1 only. |
| Non-normality concept DOI 10.5281/zenodo.22803572 | corpus-notes/nonnormality.md line 10; user memory. |
| VOTKP v2.9 13 Oct 2026; Volume v1 7 Nov 2026 | R1_versions.md line 89 (relaying v1.1b); not re-opened in primary. |
| IQGT v7.3, UPG v3.2, What Transport Keeps edition 3, Matter at a Scale v5, Offset v31 | corpus-notes/iqgt.md:1 (v7.3); R4_framework.md:225 (UPG v3.2) and :275 (edition 3, 6 Sept); corpus-notes/matter_at_a_scale.md:1 (v5); Drive folder listing (v31). |
| Work Atlas: 181 results, 80 with Lean proof, 46 repositories | work_atlas/STATUS.md: "181 results, 80 with a Lean proof found"; 49 repo-branch rows over 46 distinct repositories (recounted). |

### 16_lean (counts and names)
| claim | evidence |
|---|---|
| LoopWall 140 theorems; OpeningMap 117; TwoFaceForms 3; BoundaryAgreement 11 | `grep -c '^theorem'`: 140, 117, 3, 11; rebuild output "BUILD OK: 140 theorems", "OpeningMap, 117 theorems". |
| every named theorem in the table exists | grep of every name: all present in LoopWall.lean except `smith_identity` (above); `francium_straddles`, `frozen_prediction_Rb_Sr` are in OpeningMap.lean (the paper's table does not say which file, fine); `two_face_*` in TwoFaceForms.lean; the 11 BoundaryAgreement names (`witnessInterior`, `witnessTie`, `witnessProduct`, `halfScaling`, `uniqueInteriorBoundary`, `wrongThird`, `midInterior`, `midMargins`, `strictCounterexample`, `productAntitone`, `rationalThreeWayControl`) all present. |
| `k_opening_Li` ... `k_opening_Ne` | present (Li through Ne and further to P). |
| 433 noble-core openings; every ordinary ladder Sc to At | README.md line 84 ("433 in all"); batch10/mixed_map/README.md (433 faces); OpeningMap.lean has `ladder_*_all_inside` for all 65 elements Z = 21..85 (checked against the table). |
| TwoFaceForms split: t = 0.5005, x = 0.9999, y = 0.0005 gets different verdicts | TwoFaceForms.lean `two_face_forms_split_at_midpoint` (product form false, sum form true); compiles. |
| 11 false controls and their list | lean/controls/ has exactly those 11 files; all rejected (re-run). In-file refutations: `refute_*` exist for 9 of the 11 (N, F, C, Ne, screened-7, odd power, Mg L, Si rung 0, Ca M); the Fr upper end is covered by `francium_straddles` and the bare-S case by `readouts_control`; a tenth `refute_K_M_inside` is not among the 11. |
| source scan: no sorry, admit, native_decide, axiom | run_checks.sh output "SCAN OK" (re-run). |
| unproven items listed (Dy, Tm affinities, Pm theory, Sm lower bound, preliminary Po) | CLAUDE_REVIEW.md lines 542, 548; CODEX_RESPONSE_v1.md line 3. |

## C. Notes for the main session (not verdicts)
- The EJ transcription file note records that the pages say nothing about Mixin or degree of polarisation; 09_colour's "Mixin and the wall circle" paragraph therefore cannot be credited to her pages, only to the polarisation encoding in the mixin-colors deep dive.
- Memory items used: the user's statement that the two books are his framework and that Elizabeth's prime/twin-pair page is hers (profile of /people/elizabeth.md); the galaxy-holes memory for the Galactic paper title, date and the correction still owed. Nothing else from memory was needed.

## Counts
Section A (non-VERIFIED): 25 rows = WRONG 7, OVERSTATED 9, UNTRACEABLE 8, PARTIAL 1.
Section B (VERIFIED rows, several claims per row): 89 rows.
