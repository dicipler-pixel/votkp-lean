# READ A3b: VOTKP / Elemental Peeling, v0.3 and v0.4 (packages dated 23 Sep 2026)

Reader label A3b. Brief: /home/claude/sm/votkp_reads/BRIEF.md. Extracted to /home/claude/sm/votkp_reads/src/A3b/v03 and /home/claude/sm/votkp_reads/src/A3b/v04.

## 1. Coverage

| File | Version | Read in full | Notes |
|---|---|---|---|
| VOTKP_Elemental_Peeling_Paper_v0_3_Package_20260923.zip, paper .md (`VOTKP_ELEMENTAL_PEELING_PAPER_v0_3_20260923.md`, 806 lines) | v0.3 | yes, every line (lines 1-806) | about 53,600 bytes of text |
| Same package, paper .html (1.6 MB) | v0.3 | no, structural check only | Scripts and base64 images stripped leave about 55,500 characters of text. It contains the same headings and key numbers as the .md (checked: Table 3 header, §15.2, Og 8.888). Not read line by line. |
| Same package, figures/*.png (8 files) | v0.3 | no | Images, skipped per brief |
| Same package, logs/ (CLOSE_01, SNELL_SMITH_v1, TEST_LOG, WIDE_01) | v0.3 | CLOSE_01, SNELL_SMITH_v1, WIDE_01 yes; TEST_LOG.md (20 KB) no | TEST_LOG not read |
| Same package, preregistrations/ (5 files) | v0.3 | no | Not read |
| Same package, scripts/ (about 75 .py files) | v0.3 | only scripts/wide/nuc_posthoc.py and scripts/elemental/chk_ie.py | Remaining scripts not read |
| VOTKP_Elemental_Peeling_Paper_v0_4_Package_20260923.zip, paper .md (806 lines) | v0.4 | yes, by diff against v0.3 | Full `diff` of the two .md files: only 5 lines differ (line 5 date/label; line 575 heading "nuclei, matter waves"; line 605 heading "One reflection identity for light, electrons and matter waves"; line 759 table row "Matter-wave slab echo"; line 803 script name `matter_wave.py`). Body text is otherwise identical to v0.3. |
| v0.4 paper .html | v0.4 | structural check only | Same as v0.3 |
| v0.4 scripts/wide/matter_wave.py | v0.4 | diff against v0.3 wavicle.py | Identical except the header comment line (`WIDE-W-MATTER-WAVE` replaces `WIDE-W-WAVICLE`) |
| v0.4 logs, preregistrations, other scripts | v0.4 | no, same byte sizes as v0.3 files | Listed sizes match v0.3 exactly, so treated as unchanged; not separately read |

Not read: the remaining scripts (knot engines, close/tests/snell/elemental batches), TEST_LOG.md, the preregistration files, all images, the HTML line by line.

## 2. What the version defines and claims (v0.3 section by section; v0.4 identical except as noted)

- **Abstract (lines 8-47).** Five results: records are vectors (knots; atom ionisation peel shape vs level); peel shape is a reflection coordinate, Γ_k = tanh(½ ln(IE_{k+1}/IE_k)) (eq. at line 23); failures resolve on ladders; the same onion peels nuclei and matter waves; refraction is not reflection. Quote: "Peel shape is a reflection coordinate." Grade labels at line 47.
- **§1 Central question (lines 53-69).** Separations kept: "knot topology ≠ field loading ≠ geometric volume ≠ physical volume ≠ energy / response"; "subspace refraction ≠ boundary reflection."
- **§2 What a peel is (lines 73-90).** Operational peels; Δ𝓡_s = 𝓡_s − 𝓡_{s+1}; evidence levels and data grades A-D; "Missing data stay missing."
- **§3 Records (lines 94-116).** Theorem 3.1 finite linear predictive quotient (proof A.1); Table 1 reduced-equal, rich-different witnesses.
- **§4 Exclusion, spacing, coupling (lines 124-151).** Same-spin pair density n⁽²⁾ = n n − |γ|² (line 126); quantum metric g_ij (line 132); Δ_allowed(O) (line 136); Theorem 4.1 occupation sets a response curvature, μ_eff(r) = μ_b + (c²/δ)(1−2r) (line 149), r_c = ½(1 + μ_bδ/c²). Static polarisability as curvature (line 151).
- **§5 Finite peel theorems (lines 155-187).** 5.1 positive-channel peel; 5.2 form tomography; 5.3 Schur boundary memory; 5.4 memory kernel; 5.5 transfer silence (q = 5 example); 5.6 four-reading optical certificate; 5.7 phase reference, z = (I₀⁺−I₀⁻)/4a + i(I_{π/2}⁺−I_{π/2}⁻)/4a; 5.8 cumulants c₃ = p₁−3p₂+2p₃; 5.9 reduced-record impossibility bound T_s(x) = (x−s)²/(x⁴−2sx³+2), Δ ≈ 0.19898; 5.10 one-energy snapshots.
- **§6 Two-sided surface (lines 189-247).** Interface operator K_Σ (line 195); receiver metamer with gold (6.2); reflection coordinate Γ = (1−N)/(1+N) (line 213); thinning film echo, r(d) = (Γ + r₁₂p²)/(1 + Γ r₁₂p²) (line 221); Theorem 6.1 echo expansion, R(d) = |Γ|² + 2 Re[Γ̄(1−Γ²)r₁₂p²] (line 229); "The factor 1−Γ² = t₀₁t₁₀" (line 231). Calibration 12/12; generalisation 171 cases; boundary |Γ| ≈ 0.93, 99.4% (line 244).
- **§7 Calibration set (lines 249-258).** Table 2: Cu, Ag, Au, Pt with IE₁, shell step, R at 450/550/650 nm.
- **§8 Ionisation onion as reflection atlas (lines 260-371).** Theorem 8.1 (line 264-266): τ_k = ln(IE_{k+1}/IE_k), Γ_k = tanh(τ_k/2). Line 268: "so the atomic reflection chart has no phase." Run 01 (peel shape, 0.95 at K=10). Depth ladder (line 299). Ridge census (table at lines 314-322). Run 02 polarisability: "The peel shape loses to the static record in 9 of 9 settings" (line 336). Level law ln α = 10.28 − 3.04 ln IE₁, R² = 0.906 (line 353). Table 4 noble-gas resets.
- **§9 Refraction layer, Snell test (lines 373-386).** Pre-registered; killed on three registered tests (turning set, confusion labels, deep ridges). Spearman 0.61-0.68 against Γ_k; detrended 0.02-0.03.
- **§10-14 Knot layers (lines 390-569).** VOTKP vector (line 394); HOMFLY adds no separation through 12 crossings (line 450); Hopf charge Q = αq + βp on T(p,q) (line 468); Sutcliffe energies 7.857, 8.272, 8.761 (line 476); adjoint Jones volume law, Hughes et al. (line 514); offset-free line Vol = 2.979 ln|J₃| − 0.658 (line 522); colour ladder, 21 pairs, J₄ separates all (line 530); A-polynomial volume (line 544); loop expansion P₁ (line 555); polymer and molecular-knot realisation table (line 564-569).
- **§15 Going wide (lines 575-616).** 15.1 nuclear onion with S_2n and τ_N = ln(S_2n(N)/S_2n(N+2)) (line 581); pre-registered magic-number test 6/6 (line 591); closures fade away from stability (line 593-599). 15.2 wavicle identity, Theorem 15.1 (line 607): r = −tanh(τ/2), τ = ln(k₂/k₁). 15.3 new elements (line 613-616). f-block transfer killed (line 616).
- **§16-18.** Common pattern; open problems; 16 negative controls.
- **Appendices A-F.** Proofs A.1-A.10 (A.8 at line 692-696). Lean checkpoint (Appendix B, line 704-710): "covers the finite algebra only." Test ledger D (lines 727-760). Literature E. Scripts F (line 799-804).

**Differences v0.3 to v0.4** (diff): section 15 and 15.2 headings renamed (from "wavicles" to "matter waves" and "one reflection identity"); the matter-wave row in the test ledger; the script name. Substance unchanged. The paper text itself still says "Matter waves" in the abstract in both versions (line 35).

## 3. Element-specific results

Values are as printed. [Exact] = computed in the package; [Cited] = taken from a source; Γ values marked (A3b) were computed by me from the printed τ or IE values with Γ = tanh(τ/2) or Γ = (z−1)/(z+1).

| Element (symbol, Z) | Quantity | Number | Section / source |
|---|---|---|---|
| Copper (Cu, 29) | IE₁ | 7.726380 eV | §7 Table 2 [Exact, NIST] |
| Cu | shell step IE₁₂−IE₁₁ (k=11) | 101.67 eV | §7 Table 2 |
| Cu | R at 450 / 550 / 650 nm | 0.538 / 0.624 / 0.935 | §7 Table 2 |
| Cu | thin-film bump | bump at 450 and 550 nm | §6.4 |
| Silver (Ag, 47) | IE₁ | 7.576234 eV | §7 Table 2 |
| Ag | shell step (k=11) | 83.46 eV | §7 Table 2 |
| Ag | R at 450 / 550 / 650 nm | 0.980 / 0.983 / 0.990 | §7 Table 2 |
| Ag | thin-film | no bump; |Γ| > 0.99 (free-electron) | §6.4 |
| Gold (Au, 79) | IE₁ | 9.225554 eV | §7 Table 2 |
| Au | shell step (k=11) | 79.80 eV | §7 Table 2 |
| Au | R at 450 / 550 / 650 nm | 0.408 / 0.792 / 0.957 | §7 Table 2 |
| Au | thin-film | bump at 450 nm | §6.4 |
| Gold | surface response centroid | 2-6 eV, directly measured | §6.1 [Cited, PNAS 2025] |
| Gold | metamer after Johnson-Christy | (0.15340748, 0.16429085, 0.08396012) and (0.15895741, 0.15556920, 0.08525305) | §6.2 [Exact] |
| Platinum (Pt, 78) | IE₁ | 8.95883 eV | §7 Table 2 |
| Pt | shell step (k=10) | 75.5 eV | §7 Table 2 |
| Pt | R at 450 / 550 / 650 nm | 0.588 / 0.641 / 0.678 | §7 Table 2 |
| Pt | thin-film | bump at all three wavelengths | §6.4 |
| Beryllium (Be, 4) | pair correlation hole | about 2 Å base, 4-5 Å near 21 eV plasmon | §4 [Cited, arXiv 2601.20814] |
| Li (3) | τ₁ (first peel step) | 2.641; Γ = 0.867 (A3b) | §8.6 Table 4 |
| Na (11) | τ₁ | 2.219; Γ = 0.804 (A3b) | §8.6 |
| K (19) | τ₁ | 1.986; Γ = 0.759 (A3b) | §8.6 |
| Rb (37) | τ₁ | 1.877; Γ = 0.735 (A3b) | §8.6 |
| Cs (55) | τ₁ | 1.783; Γ = 0.712 (A3b) | §8.6 |
| Fr (87) | τ₁ | 1.705; Γ = 0.692 (A3b) | §8.6 |
| Ne (10) | τ₁ (noble band) | 0.642 | §15.3 |
| Ar (18) | τ₁ | 0.561 | §15.3 |
| Kr (36) | τ₁ | 0.554 | §15.3 |
| Xe (54) | τ₁ | 0.548 | §15.3 |
| Rn (86) | τ₁ | 0.569 | §15.3 |
| Noble gases (6) | polarisability minimum; IE₁ maximum; no bound anion | 6/6 each | §8.6 Table 4 |
| Noble gases | covalent radius minimum | 4/6 only (fails Ne, Kr); removed | §8.6 |
| Oganesson (Og, 118) | IP₁ / IP₂ | 8.888 / 16.195 eV [Cited, Guo et al. 2021] | §15.3 |
| Og | τ₁ / Γ | 0.600 / 0.291 | §15.3; WIDE_01 log |
| Og | polarisability | about 58 a.u. vs Rn about 35 [Cited, Pershina 2008] | §15.3; WIDE_01 log says "NOT a polarizability minimum" |
| Element 119 | IP₁ | 4.784 eV [Cited, arXiv 2509.05509] | §15.3 |
| Lawrencium (Lr, 103) | IP₁ | 4.96 eV [Cited, Sato et al. 2015] | §15.3 |
| Ca (20) | nuclear τ at N=20 / N=34 / N=32 | 0.38 / 0.45 / 0.43 | §15.1 (post-hoc) |
| K (19) | nuclear τ at N=20 / N=32 / N=28 | 0.34 / 0.42 / 0.40-0.42 | §15.1 (post-hoc) |
| Mg (12) | nuclear τ at N=20 | 0.15 (typical non-magic 0.12), closure gone | §15.1 |
| Ar (18) | nuclear τ at N=28 | 0.40-0.42 | §15.1 |
| Cr (24) | nuclear τ at N=28 / N=32 | 0.19 / 0.12 | §15.1 |
| Sc (21) | nuclear τ at N=34 | 0.21 | §15.1 |
| Ne (10), F (9) | nuclear τ at N=16 | Ne 0.60; F 1.24 | §15.1 (WIDE_01 log: F 1.24, Ne 0.60, Na 0.44, Mg 0.40) |
| Na (11) | nuclear τ at N=16 | 0.44 | WIDE_01 log |
| Al (13), Si (14), P (15), S (16) | nuclear τ at N=20 | Al 0.21; Si-P-S 0.34-0.35 | WIDE_01 log |
| Magic-number ridges (N = 8, 20, 28, 50, 82, 126) | mean prominence | 0.188, 0.110, 0.141, 0.209, 0.244, 0.221; non-magic 90th pct 0.000 | §15.1 Table, measured-only [Exact] |
| Nuclear largest Γ_N | max step | 0.44 (vs 0.87 for alkali first step) | §15.1 |
| Atomic depth-ladder misses, K=5/6 | element list | Re, Os, Ir, Pt, Au, Hg | §8.3 |
| Atomic depth-ladder misses, K=7 | element list | Os, Ir, Pt, Au | §8.3 |
| Hf, Ta | misses at K=11-12 | outside rule (estimated stages) | §8.3, CLOSE_01 |
| Ridge census | Ar-like, Kr-like closures; Xe-like; Ni-like (28); Pd-like | shrink ~10x; vanish in deep ions; grow with charge; peaks mid-depth | §8.4 |
| Slater Z_eff (Snell test) | N 2p, Fe 3d, Fe 4s, Zn 4s, Na 3s | 3.90, 6.25, 3.75, 4.35, 2.20 | SNELL_SMITH_v1 log |
| Lanthanide / actinide transfer | recovery | 2-3 of 14 (killed) | §15.3, WIDE_01 F |
| 19 further metal films | Al, Be, Cr, Co, Fe, Ir, Mo, Nb, Ni, Os, Pd, Rh, Ta, Ti, V, W, Zn, Mg, Pb | per-metal R not printed in paper; 171 cases pass at first-order echo | §6.4 |

Element-level Γ for Cu, Ag, Au, Pt at each wavelength is not printed; only R values are. Tables 2 and the film bump summaries are the only element-level film data in the text.

Checked but not recorded as output: scripts/elemental/chk_ie.py lists claimed IE values for Pb, Al, Rh, Ar, Po, Ru, Te, Hf, Kr, O. The package has no output for it. Not verified by me.

## 4. Bold moves

1. **The ionisation onion as a real Smith chart.** IE ratios z_k = IE_{k+1}/IE_k are read as Smith impedances on the positive real radius, so τ = ln z is a hyperbolic length (Theorem 8.1, lines 264-266). The move: a shell jump is a high-reflection layer (line 271). The assumption: IE data carry no phase, so the chart is one-dimensional. Line 268 states this.
2. **One Smith radius for three peels.** Light at a metal film, an electron leaving an ion, and a matter wave at a step all share the reflection coordinate (Theorem 15.1, line 607; §6.4 echo). The move is an identity, r = −tanh(τ/2), with τ = ln(k₂/k₁). The assumption: a step potential or a real surface; complex potential for the absorbing slab.
3. **Thin-film echo as the mechanism for a non-monotone peel.** The first-order back-surface echo, with 1−Γ² = t₀₁t₁₀ as the round trip (line 231), predicts when reflectance rises before it falls. Tested 171/171 (line 242).
4. **Nuclear peel by neutron pairs** with S_2n ratios, same Γ = tanh(τ/2) (line 579-581). The move: magic numbers become the six strongest ridges with no shell model input.
5. **Resolution ladder.** A failed short window is explained by the outer shell lying beyond the window (line 306), and the colour ladder repeats the pattern (§13.4, line 534). Both failures are said to be resolution failures, not refusals of the idea.
6. **Refraction and reflection split** (§9). The geometric Snell layer is tested separately and killed under two filling rules (SNELL log). The move is to keep the two layers apart and show they share only a trend (lines 384-386).
7. **Fixed-ratio A-polynomial volume.** ω = log|L| d arg M − log|M| d arg L, with 2∫log|L| dθ equal to Vol(4₁) to 4×10⁻¹⁶ (line 544). The move: a Mahler measure integral returns the volume. Assumption: |M| = 1 path to the complete structure.
8. **Torus control.** On a branch L = εM^{−k}, ω = 0 (A.10). The potential vanishes while topology does not.

## 5. Connections to today's frame

**Strongest direct match, the Smith point.** The paper's Γ_k = tanh(½ ln z_k) (line 23; and Theorem 8.1, line 266: "Γ_k=(z_k−1)/(z_k+1)=tanh(τ_k/2)") is the frame's Γ = (z−1)/(z+1) = tanh(½ ln z). Same object, same notation for z.

**The wall Γ² = ½.** Not present in this version. The nearest thresholds on the paper's own disk are:
- film bump boundary |Γ| ≈ 0.93, 99.4% (line 244);
- calibration threshold |Γ| ≤ 0.856 (line 243);
- Snell-Smith log: bump iff |Γ| ≤ 0.8235, no bump iff |Γ| ≥ 0.8897 (SNELL_SMITH_v1 log);
- the log's wording: "the bump appears when bulk reflectance |Γ|² is below ~0.7-0.8, so light reaches the back surface."
These are all in |Γ| between 0.82 and 0.93, not at 1/√2 = 0.707. The film data do not test the frame's wall.

**Alkali first steps against the wall (A3b).** Using the paper's own τ₁ values (line 368), Γ for Li, Na, K, Rb, Cs is 0.867, 0.804, 0.759, 0.735, 0.712, all above 1/√2. Fr (τ = 1.705, Γ = 0.692) is below. So the paper's own sixth-largest step lies just under the wall, and the five alkalis lie above it. Consistent with the frame's list of five alkali first steps past the wall. Beryllium, boron and carbon K-shell steps (the frame's other three) do not appear in this version, so untested here.

**Phase at a wall.** Line 268 is the one direct conflict: "Because every z_k>1, each Γ_k lies on the positive real radius, so the atomic reflection chart has no phase." The frame's "phase crosses what amplitude cannot" needs a complex Γ. The optical and matter-wave sections do carry phase: p² = e^{4πiNd/λ} (line 219) and e^{2ik₂d} (line 607). So phase is present in the film and step cases and absent from the atomic chart as built.

**Round-trip interference.** Line 233: "the echo from the back surface interferes with the front reflection and can lift R above its bulk value before it falls." This is the nearest mention of interference between a reflected branch and a returning branch. It does not use cancel/lock/convert.

**Lorentz/rapidity.** Not named. But τ = 2 artanh Γ (line 266) is the hyperbolic length on the Smith disk. That is structurally the form a rapidity takes. Observation by me, not in the text.

**Cancel, lock, convert; two books; the tree/ball; Koide; neutrinos; spin.** Not in the text. Spin appears only as "spin-orbit torque" on hopfions (line 482). The "reduced agrees, rich differs" structure (Table 1, line 106-116; §5.9, line 181-187) is a two-record structure, the nearest analogue to two books, but it is not framed that way.

## 6. Contradictions with the frame

1. **Phase on the atomic chart** (line 268, "no phase"). Conflicts with the frame's phase-at-a-wall, unless the atomic chart is not the one that carries phase. The paper itself puts phase only in the optical and matter-wave cases.
2. **Fr** (τ₁ = 1.705) lies below 1/√2 by the paper's own numbers. If the frame's eight past-wall steps include Fr, the frame and this version disagree. The frame's list named five alkali (Li, Na, K, Rb, Cs), which agrees with this version.
3. **Film bump threshold.** The paper's bump boundary lies at |Γ| ≈ 0.82-0.93, so a bulk reflectance of 1/2 (|Γ| = 0.707) would sit inside the bump regime. That does not contradict the frame, but it means the frame's wall is not the film boundary in this version.

No direct contradiction with Γ = tanh(½ ln z), the Smith step length ln z, or the claim that a peel step's Γ depends on the ratio alone.

## 7. Caveats

- Figures, preregistration files, TEST_LOG.md, and most scripts were not read. Element values in them could differ from the paper text.
- The HTML was checked structurally, not read line by line. Its visible text (about 55,500 characters) matches the .md on the key items checked.
- Γ values marked (A3b) are my arithmetic from the paper's printed τ values.
