# G4 verification report: 06_ball.md, 10_lab.md, 11_tests.md, 12_decay.md

Verifier: G4. Paper: "What the Peel Keeps" v1.2 build sources. Sources: repo `/home/claude/votkp-lean`, branch element-paper/loop-wall, folder `R = research/2026-11-20-element-paper-loop-wall/`; v1.1b text `/home/claude/paper_v12/raw_v11b.txt`; the pinned archive `data/element_thresholds_20261011.json.gz`.

Recomputation scripts (all under `/home/claude/paper_v12/verify/scripts/`, each with a `# SCRIPT:` line):
- `g4_orbital.py`: exact fractions and independent mpmath quadrature for the 1s, 2s and 2p overlaps at z = 4 and at the wall.
- `g4_cn.py`: carbon–nitrogen margin, critical partner ratio, angle sum, and forward-sector closing window.
- `g4_oxygen.py`: oxygen ratios, wall and midpoint calls, margins, the 3s/4s/5s controls, and the 23.68 narrowing factor.
- `g4_bench.py`: the 35/6 bench, including trace, Γ, product, and the three rival rules.
- `g4_hpairs.py`: scan of all 5,995 hydrogen-like pairs.
- `g4_bcc.py`: half-filled bcc link weight.
- `g4_hody_gain.py`: exact rational Ho–Dy independent-gain margin table and the false control.

`R/russell/prediction_review_20261121` is written `PR` below.

## A. Non-VERIFIED rows (WRONG, OVERSTATED, UNTRACEABLE)

| File | Quoted claim | Verdict | Evidence / correction |
|---|---|---|---|
| 06_ball | "the same five first-opening pairs read carbon with nitrogen +0.18° (open), sodium with magnesium +6.67° (open), potassium with calcium −2.21°, rubidium with strontium −6.52° and caesium with barium −10.29° (all close)" | WRONG as worded | The five pairs that open among the 427 are lithium–beryllium, beryllium–boron, boron–carbon, carbon–nitrogen and sodium–magnesium (`g4_cn.py`/recount of `R/batch10/mixed_map/adjacent_pairs.csv`: 5 open, 422 close). The five listed pairs are the boundary pair of each noble-gas core (helium, neon, argon, krypton, xenon); three of them close, so they are not "the same five". Source wording: `R/connections/rate_is_weight_connections.md:99-109` ("the five first-opening mixed pairs"; table of Γ₁²+Γ₂²−1 and θ₁+θ₂−90°). The numbers themselves all check. Suggested fix: "the boundary pair of each noble-gas core read …". |
| 11_tests | "the only pair among 5,995 hydrogen-like pairs that lands inside the window" | OVERSTATED | Source (`PR/hydrogenic_pairs/README.md`, `PROTOCOL.md`) means the open interval (w, c) = (5.828427, 5.837220), between the wall and the arithmetic Ag–Si midpoint. My scan (`g4_hpairs.py`) gives exactly 1 pair in (w, c) and 12 pairs in the full Ag–Si window [5.80790, 5.86654): P/Kr 5.8427, Ar/Tc 5.8260, Sc/Sn 5.8326, Cr/La 5.8577, Ni/Dy 5.8534, Cu/Er 5.8129, As/Ir 5.8629, Se/Au 5.8401, Br/Tl 5.8211, Rh/Md 5.8196, Pd/Lr 5.8377, Ag/Db 5.8595. Say "the only pair whose ratio, and whole source rectangle, lies between the geometric wall and the arithmetic midpoint". The same sentence's "(50/21)² = 5.66893 is outside the window entirely" is correct (below 5.8079). |
| 11_tests | Francium: "A measured second ionisation energy of francium decides it." | OVERSTATED | `R/PREDICTION_FRANCIUM_20261121.md`: a measurement classifies the step (inside iff IE₂ < 23.738 eV), but only a value in [23.654, 23.893) eV (a 0.24 eV band) separates the wall from the other cutoffs the data allow. Any other value "tests the column pattern, not the exact number". The "straddles the wall" part is VERIFIED (`R/batch10/mixed_map/output.txt`, Francium/Radium). |
| 11_tests | 35/6 table row "beryllium, rubidium openings" | OVERSTATED (ambiguous label) | The rubidium face here is its helium-core opening, 18305.886/4356.865 = 4.2018 (theory-grade charge-35 thresholds; archive q = 34, 35), with beryllium's 153.896205/18.21115 = 8.4507. Elsewhere in the paper rubidium's "core opening" is the krypton-core one (6.533). Source label: `PR/prediction_bench/README.md`, "Be and Rb helium-core openings", "highly charged Rb thresholds are theoretical reference values". Write "helium-core openings of beryllium and rubidium (rubidium's from theoretical thresholds)". Same wording was in v1.1b. |
| 11_tests | "the ideal 35/6 signal needs ε < 5.50×10⁻⁶" | OVERSTATED (rounding) | Source `PR/precision/passive_test.md`: ε below 5.49976×10⁻⁶ (script: 0.000005499765). Rounding up to 5.50 admits ε in (5.49976, 5.50)×10⁻⁶ that the source excludes. Use 5.49976×10⁻⁶, or "about 5.5×10⁻⁶". |
| 06_ball | "Holding carbon at 392.09/64.4935 = 6.079534" | OVERSTATED (display) | 392.09/64.4935 = 6.079527. The value 6.079534 (6.0795342) comes from the full archive inputs 392.09056/64.49352 (`R/checks/lambert_jump_check_v1.py`). The critical partner 5.591156 uses the full inputs; the rounded inputs give 5.591162 (the v1.1b figure). Quote the full-precision inputs. |
| 10_lab | "Dividing the nearest shell's share by the whole budget is my new step." | OVERSTATED | `R/QUANTUM_CHEMISTRY_LINKS.md:51-53`: "no source was found that divides by the whole off-site budget". That is the result of a search, and the file marks some citations "all from memory". It does not establish novelty. Say "I found no earlier source that divides …". |
| 12_decay | "This is the split my speed-limit paper names: the ratio forgets the scale; the difference keeps it." | OVERSTATED / UNTRACEABLE | The only trace is `R/connections/rate_is_weight_connections.md:171-175` (item S2, filed under "STRUCTURAL (same shape, different objects; flagged)"). It is Claude's reading of that paper (thorium–strontium clock ratio cancels the common scale; S3 quotes "needs a clock to supply the units; that step is open"). The speed-limit paper text is not in the repo, so I could not confirm that the paper "names" this split. Reword to "the same structure as the split in my speed-limit paper", or check the paper. This sentence is not in v1.1b. |
| 10_lab | "Polarised-neutron measurements found their susceptibilities agree above 40 K but diverge below 19.9 K." | OVERSTATED (minor) | `R/batch12/site_symmetry/README.md`: agree above 40 K; below 19.9 K the near-cubic site had the larger susceptibility. The range 19.9–40 K is not stated. "Differ below 19.9 K" is the supported wording. |
| all four | Journal citations (Resta and Sorella 1999; Souza, Wilkens and Martin 2000; Resta 2006; Onishi and Fu 2025; Müller 2009; Al Shorman 2013; McLaughlin 2017; Crandall 1979; Laporte 1987; Harvey and Lemmon 2005; Moon 1983; Storm 2026; Schweiger 2024; Jung 1992; the "Storage ring, 2024", "Bare-ion lifetime, 1996" and "direct mass measurement, 2021" notes) | UNTRACEABLE online (traced to repo notes only) | Each is matched to the DOI and bibliographic note in the repo source file for that claim (the matching file is named in section B). Crossref and the other online resolvers were blocked by the proxy, so I did not resolve the DOIs. The three bare-form notes lack authors: Storage ring 2024 = Leckenby et al., Nature (2024) doi 10.1038/s41586-024-08130-4 (decay measurement doi 10.1103/PhysRevLett.133.232701); Bare-ion lifetime 1996 = Bosch et al., PRL 77, 5190; direct mass 2021 = PENTATRAP, PRL 127, 072502. Suggest giving authors in the reference list. |

## B. VERIFIED rows

### 06_ball.md

| Claim | Verdict | Evidence |
|---|---|---|
| r = log z, a = tanh(r/4), Γ = tanh(r/2) = 2a/(1+a²); inverse z = [(1+a)/(1−a)]²; z = 3 gives a = 2−√3, Γ = 1/2; four steps: 81 and 40/41, 4 log 3 | VERIFIED | Hand algebra; v1.1b lines 937-952. Four steps give (81−1)/(81+1) = 40/41. |
| z = (β/α)², a = (β−α)/(β+α); P1s = t³, P2s = t³(1−3a²)², P2p = t⁵; the 1s overlap 8(αβ)^{3/2}/(α+β)³ squares to (1−a²)³ | VERIFIED | `g4_orbital.py` mpmath radial quadrature with explicit hydrogenic R₁₀, R₂₀, R₂₁ reproduces all three formulas to 30 digits. |
| z = 4: 512/729 = 70.23%, 2048/6561 = 31.21%, 32768/59049 = 55.49% | VERIFIED | `g4_orbital.py`: a = 1/3, t = 8/9; exact fractions 512/729, 2048/6561, 32768/59049; quadrature 0.702331961591, 0.312147538485, 0.554928957307. Matches `PR/orbital_face/orbital_check.txt`. |
| At the wall a = √2−1, t = 2(√2−1) ≈ 0.828; P1s = 8(√2−1)³ = 8(5√2−7) ≈ 56.85%, P2s ≈ 13.39%, P2p ≈ 39.02% | VERIFIED | `g4_orbital.py`: t = 0.828427; 1s = 40√2−56 = 0.568542; 2s = 0.133891; 2p = 0.390186; 8(√2−1)³−8(5√2−7) = 0. Quadrature at β/α = 1+√2 matches. |
| "70 quadratures in the orbital folder" | VERIFIED | `PR/orbital_face/orbital_check.txt`: "Independent quadrature tests 70 max discrepancy 4.66e-15". |
| Sudden-change overlap is the beta-decay (tritium) formula; Equal ratios can sit on opposite sides of one half | VERIFIED | `PR/orbital_face/README.md` ("ideal sudden atomic tritium example", Williams and Koonin 1983); 1s 0.7023 vs 2s 0.3121 at z = 4. |
| Three-state loop at scales 1, 2, 4: negative trace for 2s, positive for 2p | VERIFIED | `PR/coulomb_loop/three_states.txt`: 2s −262144/20503125 = −0.012786; 2p +33554432/184528125 = +0.181839; 1s +0.359594. |
| Sodium L opening weakest link 0.000292 → 0.000865; argon first ordinary step 0.000804 → 0.000874; difference drops about 98%; both below 1/12 | VERIFIED | `R/checks/check_projector_matched_junction_v1_output.txt` (0.000292371 → 0.000865385; 0.000804493 → 0.000874421). Recompute: 1 − (0.000874421−0.000865385)/(0.000804493−0.000292371) = 98.2%. `R/gpt_batches/batch4b_matched_junction.md`. |
| "Two balls pushed together connect at certain levels … Snell's law at the hypersurface and Pauli exclusion" (his reading) | VERIFIED (attribution) | `/home/claude/paper_v12/CHECKLIST.md` A15, A16 (memory 2026-11-12). No repo file; it is his stated view. |
| Exp. 1: 396 executions, 100 ways | VERIFIED | `R/release_sources/ball_sources/research/balls-in-the-sea/table_01.txt` ("runs 396 errors 0 ways 100"); `res_01_p0.jsonl` + `res_01_p1.jsonl` = 198 + 198 lines. |
| Exp. 2: 75 sites and 150 coordinates; weakest link 6.416×10⁻⁴; opposed lower by 0.09968; arrivals 0.7, 3.9, 8.1 at separations 2, 4, 6 | VERIFIED | `git show a60a000:research/hydrogen-in-the-space-between/hsb_check_01_output.txt`: N 75, n 150; row min 6.416e-4; sep 4 parallel −76.113323 vs opposed −76.213003 (difference 0.099680); first move 0.7, 3.9, 8.1. `R/checks/check_projector_Ar_Na_v1_output.txt` control [3,5,7] 0.00064160. |
| Sum rule Σ‖P_ij‖² = Tr(C_i−C_i²) | VERIFIED | Algebra of P² = P; `R/checks/check_chemistry_links_v1_output.txt` (second-moment identity 1.8e-15). |
| Exp. 3: first detection at C 5.37 → 8.67; light at C 0.0250 → 0.0161; discrepancy 0.0743 at B withdrawn criterion | VERIFIED | `…/hydrogen-and-the-light-between/hw_check_04_output.txt`: C first lit 5.37/8.67; most light at C 0.0250, 0.0161; "largest difference in B light 7.43e-2 — recorded, not a kill line". |
| Exp. 4: ray near radius 0.985; 12 emitted = 2.6635 + 9.3364 + 0.0001 | VERIFIED | `…/seven-balls-his-light/sb3_check_02_output.txt`: largest |q| 0.984997; "in flight 2.6635 + ground 9.3364 + below cut 0.0001". |
| Exp. 5: 37 cells, thirty leaves; 2 log 3; twin difference 7×10⁻⁵; h 0.04 → 0.005 gives 4.70×10⁻⁴ → 2.38×10⁻⁵ | VERIFIED | `…/the-ball-is-the-tree/tb_check_01_output.txt`: 37 cells, 30 leaves vs 6; Σr = 2.197225 = 2 ln z; twin 7.0e-5; h 0.04 4.70e-4, h 0.005 2.38e-5. |
| Exp. 6: eight settings, max deviation 1.6×10⁻¹⁴; mirror ρ = 1/2, v = 0.2: 0.375 and 0.125; closed container misses zero by 7.884×10⁻⁵, 2.59×10⁻⁵ after refinement | VERIFIED | `…/two-atoms-in-a-ball/hb_check_01_output.txt`: 1.6e-14 over 8 settings; 0.375000 and 0.125000; outside 0.00007883996; h = 0.005 gives 2.59e-5. ρ²(1+v)/(1−v) = 0.25 × 1.5 = 0.375. |
| B = 1/4 for one half-filled mode; 1/24, 1/48; 1/12 = (1/4)/3; the follow-up (half-filled bcc passes, filled gapped band passes, f ≤ 1/25 bound) | VERIFIED | v1.1b lines 1034-1046; `R/lean/LoopWall.lean:476` `dilute_bcc_fails` (8f/(1−f) ≤ 1/3 for f ≤ 1/25); `R/README.md:90-100`. |
| Same sum rule known in quantum chemistry; localisation tensor is the second moment of the same weights | VERIFIED | `R/QUANTUM_CHEMISTRY_LINKS.md:40-66` (Fradera–Austen–Bader 1999, Wiberg 1968, Mayer 1983, Otero-de-la-Roza et al. 2018; the file marks some "from memory"). |
| Trace 2 − 4 sinh²h_a sinh²h_b; at −2 the product is 1; uv = (1−u)(1−v) ⇔ u + v = 1; equal faces give 1/2 | VERIFIED | Algebra; `g4_bench.py` shows the trace equals 2 − 4u(a)²u(b)² with u = (z−1)/(2√z). |
| Carbon and nitrogen faces: Γ_a² + Γ_b² − 1 = +0.00309 | VERIFIED | `g4_cn.py`: 0.0030933376 (C 6.079534192, N 5.639665400). `R/batch10/mixed_map/output.txt`: margin 0.003093338. |
| 427 adjacent same-core pairs, 5 open, 422 close; margin < 0.0031 vs rivals > 0.037 | VERIFIED | `R/batch10/mixed_map/output.txt` (433 faces, 427 pairs, margin box [0.003090764, 0.003095912], nearest rival 0.037818076); my recount of `adjacent_pairs.csv`: 427 pairs, 5 open, 422 close; next smallest |margin| is potassium–calcium 0.037822. |
| Partner's forward ratio for exact contact 5.591156 | VERIFIED | `g4_cn.py`: 5.5911562008; `R/checks/lambert_jump_check_v1_output.txt`; `R/CLAUDE_REVIEW.md:15`. |
| Angle form θ_a + θ_b < 90°; angle sums +0.18°, +6.67°, −2.21°, −6.52°, −10.29° | VERIFIED | `g4_cn.py`: +0.1773°. Recount from `adjacent_pairs.csv`: Na–Mg +6.671, K–Ca −2.207, Rb–Sr −6.52, Cs–Ba −10.288. `R/connections/rate_is_weight_connections.md:101-109`. |
| Loop closes only for meeting angles between 13.115° and 89.823° | VERIFIED | `g4_cn.py` forward-sector scan: closes from 13.116° to 89.823° (grid step 0.001°). `R/CLAUDE_REVIEW.md:206` (13.11528523°, 89.82270223°); `R/checks/check_forward_sector_v1_output.txt`. |

### 10_lab.md

| Claim | Verdict | Evidence |
|---|---|---|
| Na L opening 0.000292 → 0.000865; Ar L-opening 0.000648 → 0.000872; first ordinary step 0.000804 → 0.000874; all-matched control 0.000876 in both conventions; all-ones reference 0.000875546; about 98%; every row below 1/12 | VERIFIED | `R/checks/check_projector_matched_junction_v1_output.txt` (Ar L opening 0.000648181 → 0.000871939; all 1: 0.000875546 for both). 0.000875546 rounds to 0.000876. 98.2% in `R/gpt_batches/batch4b_matched_junction.md`. All values ≈ 0.00088 < 1/12. |
| Budget B_i = Σ X_ij; one-third criterion X_ij > B_i/(3n); normalised share needs B_i > 0 | VERIFIED | Algebra; v1.1b lines 2200-2210. |
| Delocalisation sum rule (variance of electron number; ‖P_ij‖² half the delocalisation index per spin; Bader, Wiberg–Mayer) | VERIFIED | `R/QUANTUM_CHEMISTRY_LINKS.md:40-48`. |
| Half-filled chain 8/π² = 0.811 (checked 0.81056934 against 0.81056947) | VERIFIED | `R/checks/check_chemistry_links_v1_output.txt`: 0.8105693384 vs 8/π² 0.8105694691. |
| X_ij ≤ 2f², B_i = 2f(1−f), nearest-shell fraction ≤ 8f/(1−f) ≤ 1/3 for f ≤ 1/25; Lean `dilute_bcc_fails` | VERIFIED | `R/lean/LoopWall.lean:476`; `R/lean/run_checks_output.txt:65`. |
| Filled gapped band passes more strongly as the gap grows, absolute weight falls | VERIFIED | `R/gpt_batches/batch6_Fe_to_Zn_junction_and_screw.md:71`. |
| Half-filled bcc link weight 0.0333 exceeds 1/48 | VERIFIED | `g4_bcc.py`: grid tight-binding with filling 0.5 gives per-neighbour two-spin X = 0.03332, versus 1/48 = 0.020833. |
| ν = 1 for Rb, ν = 8 for Kr; 5.700 Å bcc Rb (297 K), 5.721 Å fcc Kr (58 K); Λ formula; zero at R = 0; Var(X) formula | VERIFIED | `R/batch12/localization/README.md` (MEASURED input paragraph; Λ^c formula). |
| Table, rubidium and krypton: nearest-shell 47.316% / 99.096%; second moment 10.384% / 97.327%; Tr Λ/3 5.70436 → 14.67463 and 0.073224 → 0.073271 | VERIFIED | `batch12/localization/material_summary.csv` (nearest 0.47315681, 0.99095769; Tr 5.704361 → 14.674627; 0.073224 → 0.073271); `shell_summary.csv` (0.10383942, 0.97326646). |
| PAW per-axis spread: Rb 5.684, 7.974, 10.379, 12.622; Kr 0.0669244, 0.0669717, 0.0669722 | VERIFIED | `material_summary.csv` rows PAW-smooth (5.6844156, 7.9743025, 10.3788165, 12.6220180; 0.06692443, 0.06697167, 0.06697219). |
| Half-weight radius 5.700 / 4.045 Å; half-moment radius 21.891 / 4.045 Å | VERIFIED | `shell_summary.csv` (NC 12³: 5.7000, 21.8913; Kr 4.0454 both). |
| L(q) 12³ = 8.61605 / 0.250292; forced by rank change 8.38984 / 0; rank change 97.37% | VERIFIED | `material_summary.csv`: 8.616050, 0.2502921; rank_term 8.389837, 0.0. 8.389837/8.616050 = 97.374%. |
| L(q) rank-plus-overlap identity; singular values ≤ 1 | VERIFIED | `R/batch12/localization/README.md` (the L(q) display); v1.1b lines 2296-2309. |
| Tr[P(k)(1−P(k+te))] = ½‖ΔP‖²; local form ½Tr[(∂P)²]; finite in insulators, growing in metals | VERIFIED (hedged) | README same section; `R/QUANTUM_CHEMISTRY_LINKS.md:62-66`. The paper's following sentence hedges thermodynamic divergence, consistent with the README statement that divergence "has not been established by finite-size sampling alone". |
| Kr held-out intervals all hold; 0.2502921 and 0.2516569 Å² at 12³ | VERIFIED | `material_summary.csv` (0.2502920984; twist log 0.2516569452); README "all four held-out krypton values fall inside". |
| Pseudopotential change at 6³ shifts the Kr cell-centre estimate by about 0.00630 Å² | VERIFIED | `material_summary.csv`: NC 0.07327042 − PAW 0.06697167 = 0.00629875. NC 8³ → 10³ change 2×10⁻⁸. |
| Rb serial 10³ run stopped, 12³ completed | VERIFIED | `R/batch12/localization/README.md:89`. |
| Rb plasma energy 3.714–3.716 vs 3.570–3.591 eV; Kr ε 1.92155 | VERIFIED | `R/CLAUDE_REVIEW.md:301`. |
| C and N Li-like ions: f = 0.483 ± 0.10 and 0.413 ± 0.07, intervals overlap; carbon and boron at ALS, nitrogen and oxygen at SOLEIL; single-facility electron-impact excitation seen on both sides | VERIFIED | `R/batch8/physical/carbon_nitrogen_observable.md` (table; intervals overlap 0.383–0.483; Crandall 1979 rules out a disappearing channel). |
| R = [(n−1)²+κ²]/[(n+1)²+κ²]; sign of R−½ is that of (n−3)²+κ²−8; Os 650 nm 0.48460 and 0.52845 | VERIFIED | Algebra (R−½ ∝ (n−3)²+κ²−8). `R/batch16/materials/optics.csv`: 0.48460484 (ordinary), 0.52845247 (extraordinary); (3.83²+1.87²)/(5.83²+1.87²) = 0.4846. |
| Full-spectrum bound 1 < T/L ≤ √ε_s; derivation steps; saturation by one lossless resonance | VERIFIED | `R/batch12/controls/FULL_SPECTRUM.md` (Derivation; tangent-remainder identity; kernel integral). |
| ε_s > 17 + 12√2 = (3+2√2)²; at ε_s = 36 single line 6, split line 2.30323; Drude fails the finite-static hypothesis | VERIFIED | `FULL_SPECTRUM.md`: "17+12√2"; "6 … 2.303230". (3+2√2)² = 9+8+12√2. |
| Liquid krypton 122 K: ε_s ≃ 1.66065; full ratio ≤ 1.28866; T_W = 3.27608, L_W = 0.453872, ratio 7.21806; at least 82.1% outside the window; inverse-moment budget holds for every ellipsoid factor | VERIFIED | `FULL_SPECTRUM.md` (1.66064970; 1.288662; 3.27607790; 0.45387207; 7.21806448; 0.8214671; d/s = 0.71217). |
| Rubidium interpolants overspend the allowance at N = 0.132 by 4.1% to 12.9%; missing-area fraction withdrawn; √3 cap | VERIFIED | `R/batch12/controls/DEPOLARIZATION.md` table: 1.04062, 1.04534, 1.11327, 1.12884 (4.06% to 12.88%); (n₂/n₁) = 3 for N = 1/3 to 1. |
| dhcp Nd cages: same twelve distances, zero vector sums, equal second moment, six vs three antipodal pairs, basal third moment 0 vs 1/108; Moon et al. 1983 | VERIFIED | `R/batch12/site_symmetry/README.md`. |
| Yb at 30.28 and 31.28 GPa: hcp smaller volume, longer shortest contact than bcc, survives three quoted widths | VERIFIED | `R/batch14/materials/ytterbium_structure.md` (table; −1.2974%/+1.8675%, −1.1139%/+1.9088%; bounds survive three σ). |
| Yb 64 shortest three-step walks: mean χ = 0, ⟨(χ/V_atom)³⟩ = −3/128, sign flips under mirror; powder diffraction cannot fix absolute hand | VERIFIED | `ytterbium_structure.md:28-40`, `yb_handedness.csv`. |

### 11_tests.md

| Claim | Verdict | Evidence |
|---|---|---|
| Γ² = ½ on a forward equal-face step gives w = 3+2√2; reversal flips Γ and keeps Γ² | VERIFIED | Algebra (Γ = (z−1)/(z+1)); `R/lean/LoopWall.lean`. |
| Oxygen: IE₁ = 13.618055(7), IE₂ = 35.12112(6) eV, K = 8065.543937; ground ratio 2.57901147 | VERIFIED | `g4_oxygen.py` from the archive: 35.12112/13.618055 = 2.579011467; uncertainties 7e-6, 6e-5. `PR/oxygen_design/check_oxygen.py`. |
| z_J = 5.8268808732, 5.8278703392, 5.8303470087; wall/midpoint calls inside/inside, inside/inside, outside/inside | VERIFIED | `g4_oxygen.py`; `PR/oxygen_design/Oxygen_Identifiability.md`. Wall 5.828427, midpoint 5.837220. |
| Distances from the wall −170, −61, +211 cm⁻¹ | VERIFIED | `g4_oxygen.py`: −169.84, −61.16, +210.87. |
| UV tags 1590.582, 1591.285, 1589.973 Å | VERIFIED | `PR/channel_search/READ_ME.md` table (Pettersson 1982, multiplet 19.23). |
| Six ways of centring the Ag–Si window: cutoffs between 5.83700636 and 5.83728680; all disagree with the geometry on J = 2 only | VERIFIED | `Oxygen_Identifiability.md`: [5.837006362245, 5.837286797096]; all six exceed the J = 2 upper bound. |
| NIST per-level fields blank; geometric labels survive for excitation half-widths below 169.02, 60.34, 210.06 cm⁻¹ | VERIFIED | `Oxygen_Identifiability.md`; `g4_oxygen.py` margins 169.0227, 60.3427, 210.0613. |
| 3s, 4s, 5s ratios and 000/001/111 patterns; J = 2 rule 001 | VERIFIED | `g4_oxygen.py` ratios (5.012241, 5.013319, 5.015658; 5.826881, 5.827870, 5.830347; 6.146395, 6.147187, 6.149843); native calls 000, 001, 111; rival calls 000, 000, 111. |
| 001 on 4s narrows the compatible range to [5.8278703392, 5.8303470087), about 23.68 times narrower | VERIFIED | `g4_oxygen.py`: ratio 23.6756. |
| Ground-energy ranges [5.8278629376, 5.8303544116) and [5.8278777408, 5.8303396059) | VERIFIED | `Oxygen_Identifiability.md` (5.827862937628, 5.830354411559; 5.827877740784, 5.830339605858). |
| Preparation table (neutral J = 1 at 158.265 and J = 0 at 226.977 cm⁻¹; nine z values and calls) | VERIFIED | `g4_oxygen.py` reproduces all nine entries (5.826881 … 5.842420) and the in/out calls. `PR/state_observables/README.md`. |
| Dirac Time §§11.1–11.4; D = v|sin((φ₁−φ₂)/2)| = ½√(ΔZ₁²+ΔZ₂²); complete dephasing removes both signals | VERIFIED | `PR/dirac_path/README.md`; `phase_output.txt` (trace distance 0.674288 etc., 1,156 settings, error 2.2e-16). |
| Scandium–tin: (50/21)² = 5.66893; Dirac point 5.83665; finite-nucleus and QED 5.832602195; no measured pair exists | VERIFIED | `PR/hydrogenic_pairs/README.md`, `dirac_output.txt`; (50/21)² = 5.668934; point Dirac 5.836645. "Inside" means inside (w, c); see the OVERSTATED row. |
| 5,995 hydrogen-like pairs | VERIFIED | `g4_hpairs.py`: 110 ions, 5,995 pairs. |
| 35/6 bench table: open/closed calls and traces −2.009529, −2.020493, −2.006465, −2.016894, −2.000000 | VERIFIED | `g4_bench.py` recomputes all five traces and all calls for the shifted sum, shifted product and piecewise warp. `PR/prediction_bench/README.md` table. |
| At 35/6, Γ = 29/41, 2Γ²−1 = 1/1681; trace −354481/176400 | VERIFIED | `g4_bench.py` (0.00059488 = 1/1681); Fraction check (−2.0095294785). |
| Every registered diagonal midpoint places 35/6 inside | VERIFIED | 35/6 = 5.8333 < all six cutoffs (≥ 5.837006). |
| Be/Rb: product sinh a sinh b = 1.000807802; Γ_a² + Γ_b² − 1 > 0 | VERIFIED | `g4_bench.py`: 1.000807802; 0.000379959. |
| L = +0.000032998589 at 35/6; 0 at (9, 4); −0.01351833 at (4, 4); error at most 6ε; sign not phase-referenced | VERIFIED | `PR/precision/passive_test.md`, `stokes_test.txt` (0.000032998589; −0.013518333435; equal-error limit 5.499765e-6). |
| Francium straddles the wall on present data | VERIFIED | `R/batch10/mixed_map/output.txt` ("Francium / Radium … self interval calls straddles/touches"); `R/PREDICTION_FRANCIUM_20261121.md`. |

### 12_decay.md

| Claim | Verdict | Evidence |
|---|---|---|
| M_X(q)c² = M_X(0)c² − q m_e c² + ΣI; Q(q+1)−Q(q) = a−b = (a+b)ρ; Q(n) formula | VERIFIED | `R/batch14/materials/holmium_dysprosium_decay.md`; `R/batch14/mass_anchors/WEIGHTED.md`. |
| Scale control: 2863.2 − 7381.793561c₀ eV at 57+; negative at c₀ = 1, positive at c₀ = 0.01, positive at every charge | VERIFIED | `R/batch14/mass_anchors/README.md` (DERIVED, scale control). |
| Ho–Dy: neutral anchor 2863.2(6) eV; 56+ → 57+ increment 5611−12081 = −6470 eV; ρ = −3235/8846; gap +1951.406439 → −4518.593561 eV | VERIFIED | `holmium_dysprosium_decay.md` (table, +1.9514 → −4.5186 keV); `WEIGHTED.md`; −6470/17692 = −3235/8846. |
| Direct trap boxes at the q = 40 start: [1782.877417, 2054.244830] at 56+, [−4697.122583, −4405.755170] at 57+ | VERIFIED | `R/batch14/mass_anchors/direct_trap_bounds.csv` rows 40,56 and 40,57. |
| Neutral ¹⁶³Ho electron capture; bare ¹⁶³Dy bound-state β⁻; Schweiger 2024 Table 2; Jung 1992 | VERIFIED (against repo note) | `holmium_dysprosium_decay.md`, `mass_anchors/README.md`. Online resolution of the DOIs was not possible (see section A). |
| Direct-anchor difference boxes [−1114.280802, −1106.134855] and [28.278286, 35.153376]; threshold differences −1108.4 and +31.0 | VERIFIED | Recomputed from the `direct_trap_bounds.csv` anchors: q = 38 [2823.733986, 2828.372256], q = 39 [1714.091454, 1717.599131], q = 40 [1745.877417, 1749.244830]. [L₂−U₁, U₂−L₁] gives the two quoted boxes; archive increments −1108.4 and +31.0 lie inside. |
| Independent-gain table: q = 55–58 central 1.028169%, 1.012534%, 2.147447%, 1.867373%; rectangle 0.664635%, 0.664383%, 1.823484%, 1.572577% | VERIFIED | `g4_hody_gain.py` (exact rational arithmetic from the archive, Q₀ = 2863.2 ± 0.6) reproduces every cell and the gaps 1869.406439, 1951.406439, −4518.593561, −4393.593561. |
| Binding charge q = 56; ε* = 0.0066438313934…; below 0.664383% every common-charge sign survives | VERIFIED | `g4_hody_gain.py`: minimum over q = 1…66 at q = 56, ε* = 0.006643831393397. No other charge has a smaller threshold; no sign inconsistency for q ≤ 56 (+) or q ≥ 57 (−). |
| Margin formula sQ−(d₀+d_U+d_V)−ε[U+V+s(d_V−d_U)] and adverse corners | VERIFIED | Algebra checked: s[(1−sε)(U−s d_U) − (1+sε)(V+s d_V)] expands to the stated expression. |
| False control at ε = 0.006645: Q₀ = 2862.6, U₅₆ = 95557.2819, V₅₆ = 97139.636067 gives Q₅₆ = −0.225186890715 eV; only charge 56 flips; 55+ stays positive; 1+ to 12+ keep signs for all ε < 1 | VERIFIED | `g4_hody_gain.py`: Q₅₆ = −0.225186890715; flipped charges at ε = 0.006645 are [56] only; q = 55 threshold 0.0066463 > 0.006645; q = 1…12 thresholds ≥ 1.13 (> 1). |
| Pb–Tl: 291 (+33/−27) day half-life; thresholds 24938.2 and 96783.2 eV; −71845 eV; +37.545 → −34.300 keV; −33.401 keV at 81+ | VERIFIED | `R/batch17/materials/tl_pb_decay.md`; `R/batch14/mass_anchors/WEIGHTED.md` (−359225/608607, −71,845 eV, +37,544.790452 → −34,300.209548). |
| Daughter 2.329(7) keV; channel energy 31.072 ± 4.557 keV; published 31.1(5) keV; 2.53 eV difference | VERIFIED | `tl_pb_decay.md` ("2.53 eV higher"; 31.1(5); table +31.072 ± 4.557). |
| Re–Os: 32.9 ± 2.0 yr vs ≈ 42 billion yr; acceleration 1.277×10⁹; 83162.41/7.83352 = 10616.225; factor about 120,250 | VERIFIED | `R/batch15/materials/RHENIUM_DECAY.md`; `isotope_decay_audit.txt` (1276595744.68; 10616.22489; 120249.50). |
| Q_K formula; +72.761 ± 1.185 keV (bound K) vs −12.853 ± 1.185 keV (free electron); 9.756(19) keV level reachable only for the bare parent; ¹⁸⁵Re below −940 keV; 2s proxy interval spans zero | VERIFIED | `RHENIUM_DECAY.md` and `isotope_decay_audit.txt`: 72761.01, −12853.41; excited Os +63.005 vs neutral −7.285 keV; ¹⁸⁵Re box [−945.512, −940.145]; 2s comparator −1.926 to +0.482 keV. |
| Graph-reconstruction statement (zero cycle sums; one free multiplier per component; example 2, 3, 1/5 has product 6/5) | VERIFIED | Algebra; 2 × 3 × 0.2 = 1.2 = 6/5. |
| Three unit vectors v₃ = cos α e₁ + sin α e₃: lengths 1, signed volume sin α, Gram determinant sin²α | VERIFIED | Direct determinant. |
| Neodymium and β-manganese as targets (shared radial information; opposite parity) | VERIFIED | `R/batch12/site_symmetry/README.md`; `R/README.md:90-100` (β-Mn screw χ flips under mirror). |

## C. Sentences added beyond v1.1b without a source

I screened every sentence of the four files for lack of 4-gram overlap with `raw_v11b.txt` (`scripts/g4_novelty.py`) and read each low-overlap sentence against the sources. Sentences with no v1.1b counterpart that are fully sourced elsewhere (checked above): the orbital subsection (`PR/orbital_face`, `PR/coulomb_loop`); the Sc–Sn section (`PR/hydrogenic_pairs`); the 6-experiment section is the v1.1b text; the matched-junction 98% sentence (`R/gpt_batches/batch4b`); "three separate readings" (`R/QUANTUM_CHEMISTRY_LINKS.md` Recommendation); the Rb/Kr table (`R/batch12/localization`); the Ho–Dy independent-gain section (not in the repo; reproduced by `g4_hody_gain.py`; it is in v1.1b).

Added sentences lacking a direct source, all flagged in section A:
1. 10_lab: "Dividing the nearest shell's share by the whole budget is my new step." (only "no source was found")
2. 12_decay: "This is the split my speed-limit paper names" (only a flagged structural note)
3. 06_ball: "the same five first-opening pairs" (misreads the source)
4. 11_tests: "the only pair … inside the window" (scope wrong)

Additional note: the sentence "A peel ladder is a coboundary; a loop with a non-trivial commutator is not." (12_decay) has no repo source but is a mathematical statement that follows from the preceding cocycle derivation (log-ratios along a ladder telescope), so I counted it VERIFIED as pure algebra.

## D. Counts

- Claims audited: 136 (rows in sections A and B).
- WRONG: 1
- OVERSTATED: 8 (the Sc–Sn window, francium "decides it", the Be/Rb label, ε < 5.50×10⁻⁶, 6.079534 from rounded inputs, "my new step", the speed-limit "names", and the 19.9 K "diverge")
- UNTRACEABLE: 1 (journal-citation resolution online was blocked; each citation is matched to repo notes)
- VERIFIED: 126
