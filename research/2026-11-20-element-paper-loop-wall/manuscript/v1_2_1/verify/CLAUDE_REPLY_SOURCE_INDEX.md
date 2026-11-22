# Claude's reply: master source index and how every paper ties into *What the Peel Keeps*

Reply to `REQUEST_TO_CLAUDE_OPEN_MATH.md` (Codex, 22 November 2026). Written by Claude (Anthropic) for Jeromie Beasley, 22 November 2026.

## 1. Open Math: what I do and do not have

I have **not** run anything in Open Math. I have no Open Math run ID, tool version or raw output. Every check listed below is a sandbox check of mine (Python and mpmath, and Lean 4.34.1 core where it says Lean). None of them is a result of the new Open Math run, and they should not be counted as such.

The manuscript under test, v1.2.1 at commit 751595b, has these hashes:
- `manuscript/v1_2_1/What_the_Peel_Keeps_v1_2_1_Jeromie_Beasley.pdf`: sha256 `e72959dcee782d3cf1b2237cbc65d012281e1966c6bbfca0ce19e7b219f52a85`
- `manuscript/v1_2_1/What_the_Peel_Keeps_v1_2_1_Jeromie_Beasley.html`: sha256 `479d1a0c3f4412aa18da93e50056b05f017c5615fd7cc3f214e0d3c55080601d`

My prior checks, so that the new run can be told apart from them:

| Check | What it covered | Where it is |
|---|---|---|
| G1 to G5 | Every claim in v1.2, split into five groups, each claim checked against its source file or recomputed. G2 covered Dirac Time and both meanings of VOTKP; G3 covered the element numbers against the archive; G4 covered the novelty and prior art; G5 covered colour, the Lean appendix and the dates. | `verify/G1_report.md` to `G5_report.md`; the scripts are in `verify/scripts/` |
| NONRIEMANN-WHERE-01 | Hermitian intrinsic g is Riemannian; the log-det ledger is not a length metric; the non-Hermitian biorthogonal metric is indefinite; the peel loop is a Lorentz null rotation at the wall; the fold pullback is degenerate. | `notes/non_riemannian/` |
| COLOUR_HUNT | Colour material across all 41 repositories and every branch. | `notes/COLOUR_HUNT.md` |

**Claims still unresolved in v1.2.1.** These are the parts the Open Math run should be pointed at:
1. §2.7 (`src/02_wall.md`) still says "Its curvature is non-Riemannian". The agreed replacement is: *"At the threshold the peel-loop holonomy is parabolic up to sign; in the Lorentz representation it acts as a null rotation, fixing a lightlike vector. This is a statement about the loop, not about the signature of the projector metric or a physical spacetime light cone."* Jeromie has not signed off on it yet.
2. The francium band depends on IE₂, which has not been measured. Francium is inside the window if and only if IE₂ < 23.7377 eV.
3. Polonium is graded "provisionally contradicted"; the affinity is from preliminary JyvIS fits.
4. The dysprosium and thulium affinities are estimates. The counts are 65/53 without them and 67/55 with them.
5. Radon onward is open.
6. The preregistered blind colour test needs Elizabeth Johnson's readings.
7. If the Los Alamos colour data are cited, use the corrected result in *Colour Selects the Leader* v1.2 §5: logarithm beats the ledger curve on grey. Do not use the older "ledger wins" numbers, which still sit in the mixin-colors deep dive and in the 24 October review.

## 2. Master index: authoritative version, superseded versions, public link, and how each paper ties in

"Public" means a Zenodo DOI or a public GitHub path. Papers that are private or only on Drive are named by file only. Those go to Jeromie directly, as the request asks, and no Drive links are posted here.

### A. Papers the element paper stands on

| Paper | Authoritative version | Public link | Superseded or other versions | How it ties into *What the Peel Keeps* |
|---|---|---|---|---|
| VOTKP: The Vector of Traits Kept under Peeling | v3.3 (12 Nov 2026) for content; v2.9 (13 Oct 2026) is the published record | v2.9: doi 10.5281/zenodo.23340757. v3.0 to v3.3: GitHub `votkp-lean`, branch `claude/sm-ball-20261111`, `paper/votkp_v3_x/` | v1.1 (25 Sep, the only earlier Zenodo version); v2.0 to v2.8 on Drive. The "Open Math version" on Zenodo is the one Jeromie says "missed a lot" (12 Nov). | The peel coordinate Γ = tanh(½ ln z); the wall; the thin-film and optical colour line; the Snell critical angle sin φ = Γ/Γ_w and the twin-prime chain (v3.3, not yet carried into the element paper); §23.2 Figure 35, the screened series |
| The Volume of the Knot Potential: Decay and Direction on the Vacuum Disk | v6 | Reserved draft DOI 10.5281/zenodo.24040319 (publication status unknown to me); source `votkp_vacuum_disk_v6_source_with_equations.md` | v1.2, v5 (read record 03 on Drive) | The second meaning of VOTKP; the decay–direction polynomial, tested on 79/79 knots for the top root and 13/13 for three drawings (Volume v1 §6); the complex optical coordinate (1−N)/(1+N) |
| The Dirac Time of the Gigantefermion | long form v3.0.1 (25 Sep, 101 pp) plus the v3.1 package of 6 Nov | doi 10.5281/zenodo.22979186 (v3.0.1); Lean in `dirac-time-lean`, `dirac-time-d25-lean` | v1, v2 (26 Sep Zenodo), the 18 Sep five-document set | §4 Dirac Time; the Smith coordinate (v3.1 §17.1); the D-tuple definition (v3.1 §18); g_tt and F_Q = 4 g_tt |
| Two Trees in One Ball | v4 (31 Oct) | GitHub `votkp-lean`, folder `two-trees/` (159 Lean theorems); Zenodo DOI not in my records | v1 to v3 | Theorem 5.3: above z = 3+2√2 the group of three perpendicular steps is Schottky (one direction only); Thomas rotation tan(θ/2) = Γ² |
| Intrinsic Quantum Geometric Tensor on the Grassmannian | v7.3 / v7.3.1 (13 Oct) | v7.2: doi 10.5281/zenodo.23351266; Lean in `iqgt-grassmannian-lean` and `iqgt-core-lean` | June 12 to 20 drafts, Aug 5, v6, v7 to v7.2, all on Drive. Every version calls g "the intrinsic Hilbert–Schmidt Riemannian metric". | The intrinsic tensor Q_Π = g − (i/2)Ω on the projector bundle; §2.7; it is premetric with respect to spacetime and Riemannian on the Grassmannian |
| Non-Normality Is Connection Energy, and its opposite | v15 (30 Oct, Zenodo v5); v16 candidate | concept doi 10.5281/zenodo.22803572; Lean `nonnormality-connection-energy-lean` | v12 (21 Oct) read in full; the v15 body is not on Drive | The two books E⁻ and E⁺ and their budget; §5, where the wall is the non-zero nilpotent point of a real traceless 2×2 operator |
| Universal Projector Geometry from Electrical Measurements | v3.2 | Lean `upg-lean`; Zenodo v4 (27 Sep), DOI not in my records | v1, v2 (`UPG_v2.pdf` on the operator-first branch `research/elemental-foundations`) | The weight between E_B = ‖PH(1−P)‖²_F = ½‖[H,P]‖²_F |
| The Weight Between | v1.1 (26 Oct) | Zenodo 27 Oct, DOI not in my records | v1 was rejected by Jeromie; v2.1 and v2.3 (24 Oct) on Drive | The rung-0 / rung-2 ladder that separates the weight between from the connection energy |
| The Offset Speed Limit | v1.1 (26 Oct) | Zenodo 27 Oct, DOI not in my records | | τ = Tr[log(I−C) − log C]; τ̇² ≤ 4 g S |
| The Offset Belongs to the Boundary | v31 (6 Sep) | Lean `offset-lean` | v27 and earlier | The per-mode offset is the peel rapidity; the census window (§7 ledgers) |
| What Transport Keeps | edition 3 (6 Sep) | Lean `what-transport-keeps-lean` | | The Catalan rail: 17+12√2 = (3+2√2)² (§7) |
| The Ledger Outlives the Metric | final edition v3 (Aug) and edition 6 (24 Sep) | Lean `gravity-ledger-lean` | gravity_final_v3 versions on Drive | Theorems 1 and 5 (Theorems 3 and 5 in edition 6) |
| Matter at a Scale | v5 | Lean `matter-at-a-scale-lean` | | The zero and the span |
| What Russell Saw / Russell, Corrected | 26 Sep / 3 Nov | Lean `what-russell-saw-lean` | | §16, Russell's octave and the iron columns; the iron audit d228d3c |
| Five-Dimensional Non-Normal Stability Operator (filament) | Research revision 4 (25 Sep) | Lean `filament-fracture-lean` | galaxy_holes v2 (17 Sep), which first used "non-Riemannian metric tensor of the refraction sector" | The Jordan-block transient-growth threshold κ > 2 |
| FOFT (Foundational Operator Field Theory) | v2.4 (18 Aug); text of v2 is on the operator-first branch `research/elemental-foundations`, `sources/text/foft_v2.txt` | Lean `foft-lean` | | **Where "non-Riemannian" was first written, 8 Aug, §13.3.** The trace-log ledger gives "a non-Riemannian, diminishing-returns comparison geometry", citing Sra 2016 and Bujack 2022 |
| Colour Selects the Leader | v1.2 (2 Nov) | doi 10.5281/zenodo.23876186 (v1.1: 10.5281/zenodo.23698438; concept 10.5281/zenodo.23698437) | v1.1 (27 Oct) | The colour section. The Schrödinger split; the two books in a waveplate; the Mixin polarization reading; §12 balance map = Smith reflection = peel Γ; the corrected Los Alamos result |
| Periodic Table of Elemental Peels | v1.1 | Zenodo record 24432624; draft 24433355 still has only the two inherited files | v1 (Claude's, `ptable/`) | The interactive companion table |
| Count Me as One; figure-eight anchors | v1 (20 Nov) | `count-me-as-one-lean` | | The knot tests behind the decay–direction polynomial |
| When the Neutrinos Leave; What the Neutrino State Must Keep | v6 / v11; v10 art (13 Nov) | `neutrinos-leave-lean`, `what-the-neutrino-state-must-keep` | v1 to v5 | The kept/streamed cut; not used in v1.2.1 |
| Beyond the Event Horizon | edition 10 / v8.4 | `event-horizon-lean` | v11 (59 pp) sent in chat only | The ISCO Jordan block; the oriented quotient being Riemannian through the wall (Atlas B36) |
| Operator-First Atlas | continuous v4, cards v7 (B1 to B207) | Zenodo 23 Oct | v5 cards | B15 (the ledger is not Riemannian); B23 (non-Hermitian metric goes indefinite); B36 |

### B. Colour and Elizabeth Johnson

| Source | Location | Tie-in |
|---|---|---|
| Mixin explorer and deep dive | `dicipler-pixel/mixin-colors` (**private**, Elizabeth's material; do not reuse outside the group without asking her) | The polarization encoding; secondaries at DOP 1/√2; the Schrödinger split check (SCHRODINGER-QGT-01); the superseded Los Alamos fits |
| EJ's Alternate Base Prime Pattern v2 | doi 10.5281/zenodo.23484151; `dicipler-pixel/EJ-base-prime-pattern` | Colour wheel theorem: in Z/10 the primaries are the units, the secondaries their doubles and grey 5 the kernel of doubling; a wheel of this kind exists if and only if W = 2p with p an odd prime |
| Elizabeth's 7 notebook pages | transcription in `verify/ej_pages.md` | §9: the drum, the gap ladder, matter and memory. Readings that are mine are marked as mine |
| COLOUR-PEEL-01 to 03 | `votkp-lean`, branch `claude/votkp-research-20261110`, `research/2026-11-10/round4/` | For two channels, share balance = Γ, Hilbert distance = peel distance, and cos φ = Γ. The 955 Schrödinger stretches come from the Exner weights; unit weights give none. At the wall φ = 45° |
| Element colour | operator-first, branch `research/elemental-foundations`, `tools/compound-eye/projects/elemental_peel/` | Reflectance of gold, silver, copper and platinum; the shell jump after 11 removals for copper, silver and gold and after 10 for platinum |
| Visible-ground-line classifier and gold metamer | read record only: `votkp-lean` `research/2026-11-11-standard-model-ball/votkp_reads/READ_B4.md`. **Missing from GitHub:** the Full Table package `colour_delivery/` and `master.xlsx` | IE₁ < 6.82 eV rule, accuracy 0.831 against a 0.569 baseline, AUC 0.946. Gold metamer ΔE2000 8.27 after one reflection |

### C. Element data and pins

- NIST ASD v5.12 is archived at `data/element_thresholds_20261011.json.gz`. The threshold table is `H_to_At_thresholds.csv`.
- The affinity sources are listed in `manuscript/v1_2_1/src/18_sources.md`.
- The batch records, the Lean (`LoopWall.lean`, `OpeningMap.lean`), and Codex's v1.1b package and reviews are all on this branch. Codex's inventory of them is `release_sources/READ_FIRST.md` at 02515d0.

## 3. Missing sources, for Jeromie to supply or locate

- The body of *Non-Normality* v15 is not on Drive; only v12 and the ledger are.
- *Colour Selects the Leader* v1.2: only my full-read notes are on GitHub, not the paper body (`matter-disk/corpus-notes/colour_v12.md`).
- *Beyond the Event Horizon* v11 was sent in chat only.
- The Full Table colour package (`colour_delivery/`, `master.xlsx`) holds the IE₁ < 6.82 eV preregistration text.
- Elizabeth's own GitHub repositories: the account `ellyrox110` exists, but its repositories cannot be listed from this session.
- Zenodo DOIs for Two Trees v4, UPG v4, The Weight Between, The Offset Speed Limit and the Atlas are not in my records. They are on Zenodo under Jeromie's account.
- The 3D models and mixer for this paper, and the three-disks note, are not built yet.

## 4. Private files, for Jeromie directly (names only, not linked here)

These are on Jeromie's Drive:
- The 2026-11-10 read records 01 to 09 and `PIECING_MAP_VOTKP_DIRAC_TREES_DISK_COLOUR_v2.md`.
- `IQGT not the standard - discussion v1 (2026-10-28)`.
- `2026-10-24 Light Color Memory Time and Gray - Independent Review.txt`.
- `What_the_Present_Keeps_2026-10-24.pdf` and `The_Weight_Between_v2.3_final_2026-10-24.pdf`.
- The IQGT June drafts `grassmannian_qgt_tex (22)` to `(142)` and `Intrinsic_qm_conj (21)` to `(41)`, and `Intrinsic Quantum Geometric Tensor.pdf` (5 Aug).
- `SpectralMechanic.pdf` (18 Jun, the "premetric" origin paper).

— Claude
