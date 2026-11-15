# READ A7: VOTKP colours, Matter/Gases (two editions), vacuum disk v6

Label A7. Brief: /home/claude/sm/votkp_reads/BRIEF.md (11 Nov 2026). Source copies: /home/claude/sm/votkp_reads/src/A7/. Extracted text: /home/claude/sm/votkp_reads/txt/A7/. Page renders for the equations: /home/claude/sm/votkp_reads/img/A7/. Scripts: /home/claude/sm/votkp_reads/scripts/decode_a7.py. No other file was edited and nothing was pushed.

---

## 1. Coverage

| # | File (Drive id) | Version / date | Size | Read in full |
|---|---|---|---|---|
| 1 | VOTKP_colours_of_the_elements.pdf (1_vu9tiwnItOyUXSjxNZoyBeOjlvO2RGb) | Colour team report compiled 1 Nov 2026 from nine colour bots; reads VOTKP v2.9 (13 Oct 2026). 11 pages. | 54,227 characters of text layer (pdftotext -layout), 574 lines | Yes, every text line including Sections 1–8 and the 118-row appendix. Figures 1–3 are images; only their captions were read, the images were not viewed. |
| 2 | Matter_Gases_VOTKP_Deep_Dive_20261103.pdf (1lxdlQCZlczP0Gq7FbUoBupE7aInp0LGF) | Research review dated 3 Nov 2026. 13 pages. | 33,229 characters of text layer, 630 lines | Yes. Display equations are missing from the text layer, so pages 2, 3, 4, 5, 7, 8 and 10 were rendered and viewed as images (equations, tables, the figure on page 8). Pages 1, 6, 9, 11, 12, 13 were read from the text layer; page 6 was rendered but not viewed, and it has a table and prose only. |
| 3 | Matter_Gases_VOTKP_Formal_Edition_20261103.pdf (1aF-rgjIBnASwpxy5Xg3ntNg_kLirGshN) | Formal research edition dated 3 Nov 2026. 58 pages. | 187,861 characters of text layer, 3,238 lines | Yes, lines 1–3238 (sections 1–17, appendix, all 34 Lean declarations). Equations are in the text layer as Unicode. Figures 1–2 are images; captions read, images not viewed. |
| 4 | votkp_vacuum_disk_v6_source_with_equations.md (1VoHQCV1mePmjyBGJLn42AdZ__FW7lkCK) | v6, dated 10 Nov 2026. Markdown source with equations. | 59,332 bytes, 668 lines | Yes, lines 1–668 (abstract, sections 1–12, references, Appendices D and E, and the "set aside in v6" section). The figure PNGs (fig1–fig4) are referenced but not in the download; captions were read. |

Relation of the two Matter/Gases files. The Formal edition is not a revision of the Deep Dive. They share the same date and some numbers, but the Formal edition is a 58-page theorem document (B1–B13, D1–D7, G1–G9, R1–R4, K1–K4, P1–P3, Lean L1–L34) and the Deep Dive is a 13-page review with prediction-first numerical controls. How I checked overlap: I compared every numeric value that appears in both texts.

| Quantity | Deep Dive | Formal edition | Same? |
|---|---|---|---|
| He ladder I0, I1 | 24.587389011 eV, 54.4177655282 eV (p.3) | same (§11.1) | yes |
| He binding sum | 79.0051545392 eV | 79.0051545392 eV (§11.1) | yes |
| He Γ | 0.377575066984 | 0.37757506698375054 (§11.1) | yes |
| He neutral fraction, 10/20/50 kK | 99.937400% / 28.978059% / 0.000873% | 0.999374 / 0.289781 / 8.73350e-6 (§11.1) | yes (rounded) |
| Xe 75.36 eV difference | 114.323 ± 35.0164 as | same (§5.4 end, §11.1) | yes |
| Xe 4d3/2 and 4d5/2 separately | 142.758 and 28.435 as; 95% interval 45.7–183.0 as | not stated | Deep Dive only |
| Xe channel table, 8 rows | figure 3 on p.8 | not stated | Deep Dive only |
| Thermal boundary numbers (128-site, T = 0, 0.5, 2) | table p.6 | not reproduced as a table | Deep Dive only |
| Lean / B1–B13, D1–D7, G1–G9, R1–R4, K1–K4, P1–P3 | not present | present | Formal only |
| Withdrawal of "repair/replacement" wording and the framework-fidelity audit (§1, §16) | not present | present | Formal only |

Conclusion of the check: the two are mostly different documents. The Formal edition repeats the Deep Dive's helium and Xe-difference numbers without change and adds the theorems, the Lean inventory and the dependency audit. The Deep Dive's "repair" wording (p.5 "applied here to repair the proposed extension") is not in the Formal edition, which replaces it.

---

## 2. What each version defines and claims

### 2.1 VOTKP colour report (1 Nov 2026)

This is a report from nine bots, not a paper. It tests whether the colours of the elements follow from VOTKP's ionisation-ladder record.

- §1 "The short version": "VOTKP never gives any element a visible colour." It keeps the gold metamer (§6.2) and relativistic gold (§8.8). Colour comes from a separate optical record (§8.5, §20.3.4).
- §2 "What VOTKP is now": the shape τ_k = ln(IE_{k+1}/IE_k) and level ln IE_1. The key move: "Read each ratio as an impedance and the step becomes a reflection Γ = tanh(τ/2)". Steps add by Einstein's velocity-addition law (Theorem 8.1, §15.2).
- §3 "The big colour picture": "colour" in §§11–13 is the coloured-Jones index, a name clash. Gold metamer ΔE*ab 8.60 (7.4–9.2 over 14 datasets). Relativistic gold edge 2.46 eV (504 nm).
- §4 Findings by block (s, p, d, f, superheavy, display colours). Flame colours are molecular for B, Ca, Sr, Ba. f-block colours are f–f and charge transfer. Superheavy colours are predictions only. CPK colours are marked [convention].
- §5.1 Red's pre-registered test on Z 14–118. Rule: positive if NIST lists an E1 line from the exact ground level with A_ki ≥ 1×10⁶ s⁻¹ between 380 and 780 nm, predicted positive when IE_1 < 6.82 eV. Results: AUC 0.946, accuracy 0.831 (baseline 0.569), r = 0.936, |ρ(Γ₁)| 0.352 against |ρ(ln IE₁)| 0.897. Verdict PASS on all five criteria, with 65 classifiable elements.
- §5.2 White's 36-electron check (exploratory, not pre-registered). The ridge does not vanish in the Kr-like series; it is still +0.22 at In¹³⁺, while colour starts at Nb⁵⁺ and Mo⁶⁺.
- §6 Next steps: an oxidation-state colour layer; an optical record from NIST A_ki; dataset sensitivity in the film test; coinage-metal colour edge.
- §7 Housekeeping: Zenodo text stale ("Version 2.0"); Lean README says version 1.1; §15.9 τ vs Γ notation; Ca missing from the resonance table; §15.2 Ta.
- §8 Questions for Jeremy (20 questions merged from nine bots).
- Appendix: one line per element for all 118.

### 2.2 Matter, Gases and VOTKP: Deep Dive (3 Nov 2026)

- Thesis (p.1): "VOTKP records the internal energy structure; a gas supplies an independently variable state, environment and transport regime." The older "gas = gapless, matter = gapped" is too broad.
- p.2 "The connection the papers actually support": the display identity Γ_q = (I_{q+1} − I_q)/(I_{q+1} + I_q) = tanh(½ log(I_{q+1}/I_q)); inverse I_q = I_0 ∏_{j<q} (1+Γ_j)/(1−Γ_j); binding sum B_q = Σ_{r≥q} I_r. Table of what each record determines (atomic anchor, gas state, channel response, boundary record, memory kernel).
- p.3 Helium gas test. Saha with ground-state weights U = (1, 2, 1) and self-consistent n_e = n_He(p1 + 2p2). Saha displayed as n_{q+1}/n_q = (2/(n_e λ_e³))(U_{q+1}/U_q) e^{−I_q/(k_B T)}, λ_e = h/√(2π m_e k_B T). Populations at 10, 20, 50 kK, density 10²² m⁻³. Second solver agreement below 8×10⁻¹⁶.
- p.4 Zero and span. H → aH with P fixed leaves projector quantities unchanged. Thermal covariance needs (H, μ, T) → (aH, aμ, aT); numerical checks 2.45×10⁻¹⁵ (ground state) and 2.39×10⁻¹⁵ (thermal with T scaled). Fixed-T thermal case differs by 0.713660 (Frobenius). Mass-extension a³ density scaling explicitly declared as an extension.
- p.5 Boundary census. Identity C_A − C_A² = (C − C²)_A + C_AB C_BA; X_A = C_AB C_BA; 0 ≤ X_A ≤ C_A(1−C_A) ≤ I/4; thresholded count N^∂_ε = #{λ(X_A) ≥ ε(1−ε)}; bound N^∂_ε ≤ Tr X_A/(ε(1−ε)); Tr X_A = Σ_{i∈A,j∈B} |C_ij|²; Wick: Tr X_A = −Cov(N_A, N_B).
- p.6 False control. Disconnected sites with C = 0.3 I: raw count 32, boundary count 0. Table over T with uniform and gapped rings (128 sites, antiperiodic). 32 random contractions: block identity error 1.95×10⁻¹⁶.
- p.7 Normality and memory. Hermite closure generator L = −νQ − ikM with commutator norm 4.89897949 (nonnormal) yet contractive. Memory kernel Σ(z) = B(zI − D)⁻¹B†, K(t) = B e^{−iDt/ħ} B†. Hidden source term required.
- p.8 Xenon channel table, recovered from the Nature Communications source-data ZIP (Zhong et al. 2020). At 75.36 eV: 142.758 as (4d3/2), 28.435 as (4d5/2), difference 114.323 ± 35.0164 as, descriptive 95% interval 45.7–183.0 as, "not evidence that the lower confidence limit exceeds 100 as". Seven higher rows include zero.
- p.9 Recent literature (Tong–Kuwahara–Gong 2026 clustering theorem; Jarema et al.; Kafle et al. spin/charge gap; Zhao et al. dissipation; Li–Chen–Zhai abstract only; Yao et al. pair correlations).
- p.10 Retain / repair table. Derivative sign: "Remove the extra leading minus" (§5 of Matter v5); the corrected SPARC derivative is shown as a display, value −0.5882352941.
- p.11 Next research programme and "Decisive failure conditions".
- p.12–13 Reproduction, evidence coverage, references.

### 2.3 Formal research edition (3 Nov 2026)

- §1 Source integrity. Records a preparation-time admission from another assistant about a ledger investigation, and states that this edition "withdraws any implication that those additions replace or correct" the Direction–Spin–Throughput / connection-energy framework.
- §2 Conventions and evidence classes (analytic theorem, Lean-checked, model computation, published-data reproduction, open physical claim).
- §3 Finite boundary census for positive contractions: B1 F_A = T_A + X_A; B2 0 ≤ X_A ≤ F_A ≤ I/4 with ‖B‖ ≤ 1/2; B4 N^∂ ≤ N^raw with equality for projectors; B5 θ N^∂ ≤ Tr X_A; B8 near-projector comparison with τ = ‖C − C²‖; B9 same local covariance, different boundary correlation (P_A extension); B10 Var(N_A) = Tr(A − A²), Cov(N_A, N_B) = −Tr X_A; B11 counterexamples (disconnected thermal, classical non-Gaussian, entanglement invisible to C); B12 "Even the full boundary-strength record does not determine later response"; B13 4 Tr X_A ≤ I_G(A:B) ≤ Tr X_A/(δ(1−δ)).
- §4 Smith-disk coordinate: D1 Γ_b(λ) = √(1 − 4λ) with λ = (1 − Γ_b²)/4, and "λ ≥ ε(1−ε) ⟺ Γ_b ≤ 1 − 2ε"; for pure states Γ_b = |1 − 2ν| (sign forgotten). D3 idempotent algebra survives opening; D4 radial count with R_b(λ) = √|1 − 4λ|; D5 every square A is the compression of the idempotent [[A, I],[A − A², I − A]]; D6 Cayley–tanh with branch condition |Im W| < π/2 for principal log.
- §5 Atomic records and Saha: G1 bijection (0,∞)^Z → (0,∞) × (−1,1)^{Z−1}, with Γ_q = (I_{q+1} − I_q)/(I_{q+1} + I_q) and inverse I_q = I_0 ∏(1+Γ_j)/(1−Γ_j); G3 unique positive neutral solution; G4 density response d log x / d log N = μ/(μ+V) ∈ (0,1); G6 temperature response; G7 scaling covariance (S_q, N, x) → c(S_q, N, x); corollary G7a: no function of the anchored record fixes mean charge at all densities. R1 exact reduced retained equation with hidden source J(t); R2 positive channel measure dM(λ) = B dE_D(λ) B†; R3 equal spectra and coupling footprint give survival 0 vs 1/32 at t = π/4; R4 kernel-only evolution underdetermined.
- §6 Reverse recovery G8–G9: L_q = log(n_q n_{q+2}/n_{q+1}²) = log(U_q U_{q+2}/U²_{q+1}) − β(I_{q+1} − I_q); inverse two-temperature construction; partition correction and excited-state opposite U_1(T) = 2 + 4 exp(−10 eV/k_BT) (registered before running).
- §7 Finite-moment theorem M1: equal moments of order < m, different response F_q(t) − F_p(t) = δ e^{−iat}(1 − e^{−iht})^m. §7.2 reflected distributions (3,7,1,5)/16 and (5,1,7,3)/16 have equal intensities and different complex responses.
- §8 Gas transport witness K1–K4: same density, flow and stress, different third moment (ΔM3 = 96aυ0³ρ); free-streaming density contrast Δn = −16aηρ* e^{−σ²k²t/2} sin(kx) sin³(kv0 t); erasure by velocity reset gives factor e^{−νs}.
- §9 Petermann: P1 K = 1 + |d|²/|E|² ≥ 1; P2 for unbroken SSH band K = 1 + u²/(E(0)E(π)), so K = 2 iff E(0)E(π) = u²; P3 partition counterexample with w = 0.
- §10 Independent audit of the incoming disk extension: endpoint filter changes the massive exit (massive ⟨K⟩ = 1.0580 at δ = 10⁻⁸ and 1.0224 at δ = 10⁻⁹); massless stable at 2.0000 for filters 10⁻⁶–10⁻⁹.
- §11 Reproduction table (22 earlier checks; 34 Lean declarations, 5 false controls rejected). Helium Γ = 0.37757506698375054; at 30–32 kK the inverse returns this across densities 10¹⁸–10²⁶ m⁻³.
- §12 Literature. §13 Open Math OS handoff (bounded tasks). §14 references. §15 Lean scope: positive sources contain no sorry or native_decide. §16 Dependency audit: framework fidelity "remains unverified". §17 Lean declaration inventory L1–L34.

Difference from the Deep Dive, in one line: the Formal edition keeps the Deep Dive's numbers but replaces its "repair" framing with explicit scope limits and adds theorem-level proofs.

### 2.4 Vacuum disk v6 (10 Nov 2026)

- Abstract: VOTKP "began as the volume of the knot potential" and "became the vector of traits kept under peeling". The paper joins them through the two books of Q = g − (i/2)Ω on a Smith-type disk whose centre is the vacuum and whose rim is ground.
- §1 Sources: IQGT v7.3.1; Dirac Time v3.1; VOTKP v2.9. Definitions: g = ½Tr(VW) (climb); Ω = +i Tr(Π[V, W]) (turn); Γ = (z − 1)/(z + 1) = tanh(½ ln z). Tennis racket: "the axis changes, the direction stays".
- §2 Vacuum disk G(z) = (z − w)/(z − w̄), w = e^{iπ/3}, V_0 = D(w) = 1.0149416064. Proposition 1 (a)–(d): G(w) = 0; real z gives |G| = 1 (flat pieces on the rim); mirrors give |G(z̄)| = 1/|G(z)|; T(z) = 1/(1 − z) gives G(Tz) = e^{2πi/3} G(z).
- §3 Decay. Theorem 2 bowl series D(z) = V_0 − (3√3/4)|G|² + (√3/8)(G³ + Ḡ³) + (3√3/16)|G|⁴ + O(|G|⁵). Closed-form coefficients c_ab = Im[(1 − ω^a)(1 − ω^b)]/(2ab); remainder |R| ≤ 0.70|G|⁵ on |G| ≤ 0.9999 (ball arithmetic). Knot law: median error 0.076% over 12,954 knots, with no fitted parameter.
- §4 Geometries of a knot (31 hyperbolic knots, 291 solutions): true geometry is the root nearest the vacuum (31 of 31).
- §5 Direction: Neumann's formula; Chern–Simons exact in 454 of 454 runs after a branching fix; "Decay (volume) is continuous: distance from the vacuum. Direction (twist) is integer".
- §6 Polynomial P_K(x) = ∏(x − e^{λV_0(ρ)}) read off PD drawings: top root = SnapPy complex volume on 79 of 79 knots; torus knots give pure-direction roots with direction = −4pq·α_end² mod 1 (arc end points); table of torus roots (3_1: 5/6; 5_1: 1/10, 9/10; 7_1: 3/14, 5/14, 13/14; 8_19: 2/3, 11/12; 10_124: 11/15, 14/15).
- §7 Light strings: Jones climb vs volume ρ = 0.854; HOMFLY along sl(N) lines; circuit polynomial Q(z) with Q(1) = det K on 1,846 alternating knots.
- §8 Lessons from surfaceology (Arkani-Hamed et al.); u-variables are cross-ratios with u_C + ∏u_D = 1.
- §9 Colour on the same disk: reflection Γ = (1 − N)/(1 + N) for 41 elements from refractiveindex.info. Schottky line |Γ|² = 1/2 separates metals (35 of 35) from non-metals (0 of 6). Hidden phase: phase gap predicts colour gap under film at ρ = 0.64; rim pairs under-read (ρ = −0.52). Film winding is an integer index of the substrate, grows by one per 247 nm; selenium is the one element inside the circle.
- §10 Electron: SL(2, C) and the −1 on the longitude (79 of 79 knots); braided spinor from three routes (knot, rest mass, braiding); hinge: "These are the same winding read two ways"; kept phase as Cheeger–Chern–Simons class (theorem side) and Dirac-determinant phase (conjecture side). "the pairing cancels the even record and only the odd datum survives".
- §11 Molecular knots: 5 of 6 privileged self-assembled knots are torus knots.
- §12 Ledger (labels each item REPRODUCTION / NEW READING / NEW RESULT / CONJECTURE).
- §13 Open problems (8 items).
- Appendix D (scripts), Appendix E (eleven machine-precision checks and one reproduction), set-aside section (zeta zeros, CBD(2), NTT, Goldbach, Schumann, ML-KEM, and two circular inherited claims, plus the set-aside spin-lift π²/2 idea and the set-aside η argument).

---

## 3. Element-specific results

### 3.1 Numbers attached to named elements (colour report, Deep Dive, Formal edition, vacuum disk v6)

| Element (symbol, Z) | Quantity | Number | Where |
|---|---|---|---|
| He (2) | first ionisation threshold I_0 (E, evaluated) | 24.587389011 eV | Deep Dive p.3; Formal §11.1 |
| He (2) | second threshold I_1 (T, theoretical) | 54.4177655282 eV | Deep Dive p.3; Formal §11.1 |
| He (2) | binding sum I_0 + I_1 | 79.0051545392 eV | Deep Dive p.3; Formal §11.1 |
| He (2) | peel step Γ_0 = (I_1 − I_0)/(I_1 + I_0) | 0.377575066984 | Deep Dive p.3; Formal §11.1 |
| He (2) | neutral fraction, n = 10²² m⁻³, 10 / 20 / 50 kK | 99.937400% / 28.978059% / 0.000873% | Deep Dive p.3 |
| He (2) | neutral fraction at 20 kK, density 10²⁰ → 10²⁴ m⁻³ | 0.5680% → 87.6482% | Deep Dive p.3 |
| He (2) | Γ bias from fixed-partition inversion, synthetic U_1 | −0.0114256334763 (restored to 1.4×10⁻¹⁴) | Formal §11.3 |
| Xe (54) | 4d3/2 delay estimate at 75.36 eV | 142.758 as | Deep Dive p.8 |
| Xe (54) | 4d5/2 delay estimate at 75.36 eV | 28.435 as | Deep Dive p.8 |
| Xe (54) | 4d3/2 − 4d5/2 difference | 114.323 ± 35.0164 as; descriptive 95% interval 45.7–183.0 as | Deep Dive p.8; Formal §11.1 |
| Xe (54) | inner 4d-hole threshold | about 67.5 eV, spin–orbit partner about 2 eV | Deep Dive p.8, p.11 |
| Xe (54) | neutral valence thresholds (different comparison) | 12.13 eV and 20.98 eV | Deep Dive p.11 |
| H (1) | Balmer line | 656.3 nm | colour App. |
| Li (3) | flame line, carmine; closed-shell Li+ colourless | 670.8 nm | colour §4 |
| Na (11) | D lines, yellow flame | 589.0 / 589.6 nm | colour §4 |
| K (19) | resonance line, lilac flame | 766.5 nm | colour §4 |
| Rb (37) | "named for its deep-red line" | 780.0 nm edge | colour §4, App. |
| Ca (20) | slightly yellow metal b* | +6.6 (computed) | colour §4 |
| Sr (38) | strongest atomic line, blue; flame crimson (molecular, disputed) | 460.7 nm | colour §4 |
| Ra (88) | NIST resonance line matched to Runge & Precht 1903 | 482.593 nm | colour §4 |
| B (5) | flame green from BO₂; weak yellow line | 582.1 nm | colour §4 |
| Ne (10) | orange glow carried by 585 and 640 nm | 585 and 640 nm | colour §4 |
| In (49) | indigo pair 451/410 nm, spin–orbit split | 2,212.6 cm⁻¹ | colour §4 |
| Tl (81) | green line, ends on 6p3/2 | 535.0 nm | colour §4 |
| Tl (81) | false positive in Red's rule (line just under cut-off) | 377.7 nm | colour §5.1 |
| Ti (22) | threshold cases in Red's rule | IE_1 6.828 eV (Ti), 6.825 eV (Hf) against 6.82 eV cut | colour §5.1 |
| Al, Si, P (13, 14, 15) | only misses at K = 10 in Run 01 | no number given | colour §4 |
| Cr (24) | first peel step, larger than neighbours V and Mn | Γ₁ 0.418 (V 0.369, Mn 0.356) | colour §4 |
| Cu (29) | colour chroma C* | ≈ 18 (computed) | colour §4 |
| Os (76) / Ir (77) | colour b* | −7 to −9 / +2.4 (computed) | colour §4 |
| Dy to Yb (66–70) | first peel step Γ₁ (near-constant) | 0.321–0.325 | colour §4 f-block |
| Eu (63) | IE_3, largest early step | 24.84 eV | colour §4 f-block |
| Lr (103) | first peel step (groups with Al, In, Tl) | Γ₁ 0.491 | colour §4 f-block |
| No (102) | line in UV, outside visible | 333.8 nm | colour §4 |
| Rn (86) | first peel step, τ₁ and Γ₁ | τ₁ 0.569, Γ₁ 0.277 | colour §7 |
| Au (79) | gold metamer ΔE*ab (paper 8.60) | 8.6022 | colour §3, §6.2 |
| Au (79) | relativistic edge (interband) | 2.46 eV (504 nm) | colour §3 |
| Au (79) / Hg (80) | relativistic column miss | 19.5% / 17.5% | colour §1 (paper §8.8) |
| Ag (47) / Au (79) / Cu (29) | interband colour edge | 3.8 / 2.5 / 2.1 eV | colour §6 |
| Zn (30) | film test, |Γ(650)| | 0.935 (Werner) vs 0.859 (Querry) | colour §4, §6 |
| In (49) | film label sits on a boundary | 0.918–0.926 | colour §4 |
| Ga–Kr (31–36) | wall in shell-closure record | 0.457 → 0.252 | colour §3 (Grey) |
| Ta (73), Mo (42), Pt (78) | dataset-sensitive film labels | no number | colour §4 |
| Bi (83) | iridescent oxide tarnish (untested film case) | no number | colour §4 |
| Db (105) | longest-lived isotope Db-268 | about 29 hours | colour §4 |
| Db (105) | predicted richest visible set | blue-violet, 458.5 nm | colour §4, App. |
| Cn (112) | predicted liquid, gap | 6.4 eV | colour §4 |
| Fl (114) | predicted semiconductor, gap | 0.8 eV | colour §4 |
| Og (118) | predicted solid, gap | 1.5 eV | colour §4 |
| Mc (115) | predicted lowest line | 544.2 nm (green) | colour §4 |
| Nh (113) | predicted thallium-green analogue | about 840 nm (IR) | colour §4 |
| Ce (58) | 54-electron ridge at Ce⁴⁺ (vanishes) | −0.028 | colour §5.2 |
| Cs (55) | 54-electron ridge at Cs⁺ | +1.423 | colour §5.2 |
| Ba (56) | 54-electron ridge at Ba²⁺ | +0.624 | colour §5.2 |
| La (57) | 54-electron ridge at La³⁺ | +0.418 | colour §5.2 |
| Rb (37) | 36-electron ridge at Rb⁺ (one-sided) | +1.514 | colour §5.2 |
| Sr (38) | 36-electron ridge at Sr²⁺ | +0.697 | colour §5.2 |
| Y (39) | 36-electron ridge at Y³⁺ | +0.565 | colour §5.2 |
| Zr (40) | 36-electron ridge at Zr⁴⁺ | +0.452 | colour §5.2 |
| Nb (41) | 36-electron ridge at Nb⁵⁺ | +0.406 | colour §5.2 |
| Mo (42) | 36-electron ridge at Mo⁶⁺ | +0.367 | colour §5.2 |
| Tc (43) | 36-electron ridge at Tc⁷⁺ | +0.333 | colour §5.2 |
| Ru (44) | 36-electron ridge at Ru⁸⁺ | +0.316 | colour §5.2 |
| In (49) | 36-electron ridge at In¹³⁺ | +0.218 | colour §5.2 |
| Ti, Hf, Mn, Fe, Mo, Tc, Ru, Ta, W, Ir (d-block misses) | Red's rule misses | no number beyond the names | colour §5.1 |
| Se (34) | film winding; the one element inside the circle \|r₁₂\| = \|r₀₁\| | no number beyond the 247 nm film step | vacuum v6 §9 |
| Te (52), P (15), Se (34), I (53), Br (35), S (16) | molecular solids crossing the 2/3 line under squeeze; metallization ranks | ρ = 0.89 | vacuum v6 §9 |
| Si (14), Ge (32), B (5) | network solids already on the 2/3 line; need a flip | no number | vacuum v6 §9 |
| 41 elements (names not listed) | reflection tracks on the disk | Γ = (1 − N)/(1 + N) | vacuum v6 §9 |

Ion ridges reproduce White's 54-electron numbers exactly in the colour report (Cs⁺ +1.423, Ba²⁺ +0.624, La³⁺ +0.418, Ce⁴⁺ −0.028), which the report used as its check.

### 3.2 Every element the colour report gives a number to (appendix, 118 rows)

Swatch tags: none = colourless; calc = computed by a bot from tabulated optical constants [model]; guess = illustrative swatch [guess]; n/o = no observation. Key line = visible line in nm from NIST ASD unless marked predicted. Source: colour report appendix, pp. 9–11.

| Z | Symbol | Swatch | Key visible line (nm) |
|---|---|---|---|
| 1 | H | none | 656.3 red (Balmer) |
| 2 | He | none | 587.6 yellow |
| 3 | Li | guess | 670.8 red |
| 4 | Be | guess | 457.3 blue (weak) |
| 5 | B | guess | 582.1 yellow (weak) |
| 6 | C | guess | 505.2 green |
| 7 | N | none | 746.8 red (barely visible) |
| 8 | O | none | 777.2 / 615.8; aurora 557.7 green |
| 9 | F | none | 685.6 deep red |
| 10 | Ne | none | 585.2 / 640.2 (the glow colour) |
| 11 | Na | guess | 589.0 / 589.6 yellow (D lines) |
| 12 | Mg | guess | 518.4 green |
| 13 | Al | guess | 396.2 / 394.4 violet |
| 14 | Si | guess | 390.6 violet |
| 15 | P | guess | 460.2 blue (P II) |
| 16 | S | guess | 545.4 green (S II) |
| 17 | Cl | guess | 479.5 blue (Cl II) |
| 18 | Ar | none | 763.5 / 750.4 deep red |
| 19 | K | calc | 766.5 deep red; 404.4 violet |
| 20 | Ca | calc | 422.7 violet |
| 21 | Sc | guess | 390.7 violet |
| 22 | Ti | calc | 399.9 violet |
| 23 | V | calc | 437.9 violet |
| 24 | Cr | calc | 425.4 violet; 520.8 green |
| 25 | Mn | calc | 403.1 violet |
| 26 | Fe | calc | 382.0 violet |
| 27 | Co | calc | 389.4 violet; 512.9 green |
| 28 | Ni | calc | 547.7 green |
| 29 | Cu | calc | 521.8 green |
| 30 | Zn | calc | 481.1 blue |
| 31 | Ga | guess | 417.2 violet |
| 32 | Ge | guess | 422.7 violet |
| 33 | As | guess | 545.1 green (weak) |
| 34 | Se | guess | 473.1 blue |
| 35 | Br | guess | 635.1 red |
| 36 | Kr | none | 587.1 yellow; 557.0 green |
| 37 | Rb | calc | 780.0 deep red (edge); 420.2 violet |
| 38 | Sr | guess | 460.7 blue |
| 39 | Y | guess | 410.2 violet |
| 40 | Zr | calc | 389.0 violet; 468.8 blue |
| 41 | Nb | calc | 405.9 violet |
| 42 | Mo | calc | 550.6 / 553.3 green |
| 43 | Tc | guess | 485.4 cyan |
| 44 | Ru | guess | 420.0 violet |
| 45 | Rh | calc | 385.7 violet |
| 46 | Pd | calc | 421.3 violet |
| 47 | Ag | calc | 546.6 green |
| 48 | Cd | guess | 643.8 red |
| 49 | In | calc | 451.1 blue; 410.2 violet |
| 50 | Sn | guess | 452.5 blue |
| 51 | Sb | guess | 563.2 green |
| 52 | Te | guess | 683.8 red |
| 53 | I | guess | 511.9 green |
| 54 | Xe | none | 462.4 / 467.1 blue |
| 55 | Cs | guess | 455.5 / 459.3 blue |
| 56 | Ba | guess | 553.5 green |
| 57 | La | guess | 625.0 orange |
| 58 | Ce | guess | 569.9 yellow |
| 59 | Pr | guess | 495.1 cyan |
| 60 | Nd | guess | 463.4 blue |
| 61 | Pm | n/o | 652.0 red |
| 62 | Sm | guess | 429.7 violet |
| 63 | Eu | guess | 459.4 blue |
| 64 | Gd | guess | 422.6 violet |
| 65 | Tb | guess | 432.6 violet |
| 66 | Dy | guess | 421.2 violet |
| 67 | Ho | guess | 410.4 violet |
| 68 | Er | guess | 400.8 violet |
| 69 | Tm | guess | 409.4 violet |
| 70 | Yb | guess | 398.8 violet; 555.6 green |
| 71 | Lu | guess | 451.9 blue |
| 72 | Hf | guess | 382.1 violet |
| 73 | Ta | guess | 468.2 blue |
| 74 | W | calc | 400.9 violet |
| 75 | Re | guess | 422.7 violet |
| 76 | Os | calc | 426.1 violet |
| 77 | Ir | calc | 380.0 violet |
| 78 | Pt | calc | 381.9 violet |
| 79 | Au | calc | 460.8 blue; 627.8 red |
| 80 | Hg | calc | 435.8 violet-blue; 546.1 green |
| 81 | Tl | guess | 535.0 green |
| 82 | Pb | calc | 405.8 violet |
| 83 | Bi | calc | 472.3 blue |
| 84 | Po | guess | 417.1 violet |
| 85 | At | n/o | none visible (UV only) |
| 86 | Rn | none | 745.0 red |
| 87 | Fr | n/o | 718.0 red (D2) |
| 88 | Ra | guess | 482.6 blue |
| 89 | Ac | guess | 418.0 violet |
| 90 | Th | guess | 576.1 yellow |
| 91 | Pa | guess | 694.6 red (unranked) |
| 92 | U | guess | 381.2 violet |
| 93 | Np | guess | 697.2 red |
| 94 | Pu | guess | (74 lines, unrankable) |
| 95 | Am | guess | 605.5 orange |
| 96 | Cm | guess | (43 lines, unrankable) |
| 97 | Bk | guess | 505.7–558.1 green group |
| 98 | Cf | guess | (15 lines, unrankable) |
| 99 | Es | guess | 516.2 green |
| 100 | Fm | n/o | about 398 violet edge (levels, Sewtz 2003) |
| 101 | Md | n/o | none |
| 102 | No | n/o | 333.8 (UV, not visible) |
| 103 | Lr | n/o | about 451 blue (theory only) |
| 104 | Rf | n/o | none |
| 105 | Db | n/o | 458.5 blue (predicted) |
| 106 | Sg | n/o | 410.1 violet (predicted) |
| 107 | Bh | n/o | 443.8 violet (predicted, weak) |
| 108 | Hs | n/o | 641 red (predicted, unreliable) |
| 109 | Mt | n/o | 410.0 violet (predicted, weak) |
| 110 | Ds | n/o | 458.5 blue (predicted, weak) |
| 111 | Rg | n/o | UV only (predicted) |
| 112 | Cn | n/o | UV only (predicted) |
| 113 | Nh | n/o | UV; about 840 IR (predicted) |
| 114 | Fl | n/o | UV only (predicted) |
| 115 | Mc | n/o | 544.2 green (predicted) |
| 116 | Lv | n/o | 403.4 violet edge (predicted) |
| 117 | Ts | n/o | UV only (predicted) |
| 118 | Og | n/o | UV only (predicted) |

The colour report's appendix was typed row by row from the extracted text. A script parse of the column layout was tried and rejected because the column offsets shift from page to page. Spot checks against the text: 41 Nb 405.9, 58 Ce 569.9, 79 Au 460.8 and 627.8, 113 Nh 840 IR.

Elements the Deep Dive and Formal edition mention without numbers: Ne and Xe only as reference conventions (Deep Dive p.8). The vacuum v6 names no further elements. The Formal edition's only element is helium.

---

## 4. Bold moves

These are the mathematical moves, with their assumptions, not softened claims.

1. Colour report: the visible-line rule uses the level IE_1 and not the peel shape. Assumption: an atom in a gas, a ground-level E1 line with A_ki ≥ 10⁶ s⁻¹, 380–780 nm. Result: AUC 0.946 for −IE_1 against 0.606 for the shape. The move reads colour off a single threshold, not off the Smith step. Version: colour report §5.1, pre-registered 11:25 CST.
2. Colour report: a per-step rapidity reading. "Steps add by Einstein's velocity-addition law, so a whole peel is a hyperbolic length (Theorem 8.1, §15.2)." Assumption: each ratio is read as an impedance Γ = tanh(τ/2), so a whole peel adds in τ. The velocity-addition law is the group law of the hyperbolic metric.
3. Deep Dive p.4: scale covariance by (H, μ, T) → (aH, aμ, aT), which leaves Fermi covariances fixed (2.39×10⁻¹⁵). Plus a declared extension with electron mass scaled by a and density by a³, which the text labels as not a cosmological equivalence.
4. Deep Dive p.5 and Formal B5/B13: the thresholded census N^∂_ε counts cross-boundary squared singular values above ε(1−ε). For pure states this equals the count of occupations ν in [ε, 1−ε]. For a Gaussian state it is bounded by Tr X_A / (ε(1−ε)) and by mutual information. Assumption: number-conserving fermionic Gaussian, gauge-invariant.
5. Formal D1: the boundary coordinate Γ_b = √(1 − 4λ) where λ is an eigenvalue of X_A, so the threshold λ ≥ ε(1−ε) becomes Γ_b ≤ 1 − 2ε. The coordinate sends a positive covariance eigenvalue to a point on a real half-diameter. Its sign is forgotten for projectors: Γ_b = |1 − 2ν|.
6. Formal D5: every square matrix A is the (1,1) compression of the idempotent [[A, I],[A − A², I − A]], so idempotence alone imposes no positivity. The explicit example C = [[2, 1],[−2, −1]] has X_A = −2 and radial coordinate 3.
7. Formal P2 (exact): for the unbroken SSH band, K = 1 + u²/(E(0)E(π)), so K = 2 exactly when E(0)E(π) = u². P3 is the counterexample: with w = 0 the compressed projector stays in {0, 1}, so no exit occurs at K = 2. The move is to separate the band average from the spatial exit.
8. Formal K1–K4: two velocity distributions with the same density, flow and stress (through third-order moment matching) differ in later density; the density contrast decays by exactly e^{−νs} under a velocity reset during a separate preparation interval.
9. Vacuum v6 Prop. 1(d): the axis switch T(z) = 1/(1 − z), acting on G as multiplication by e^{2πi/3}, so the three labels of a tetrahedron sit at 120° on one circle. The tennis-racket switch is exact on the disk.
10. Vacuum v6 Thm 2: the bowl coefficients are c_ab = Im[(1 − ω^a)(1 − ω^b)]/(2ab), giving 3√3/4 = |1 − ω|³/4. Assumption: the closed form is verified exactly through degree 4 and by ball arithmetic through degree 40.
11. Vacuum v6 §6: the direction of a torus-knot root is −4pq·α_end² mod 1, where α_end is the end point of a Dirac-time arc. The formula predicted 2/3 (8_19) and 11/15 (10_124) before either was found on the disk.
12. Vacuum v6 §10: the pairing Γ P_+ Γ = P_− gives a symmetric spectrum, so η = 0 and the paired operator keeps no phase. The move is to say only the unpaired odd operator can carry the kept phase. Status: conjecture on the field side.

---

## 5. Connections to today's frame

The frame items are quoted here where a line of these texts carries them. Nothing is stated that the text does not say.

Γ = tanh(½ ln z), the Smith step:
- Vacuum v6 §1: "The Smith coordinate Γ = (z−1)/(z+1) = tanh(½ ln z) puts any impedance-like quantity on a disk".
- Colour report §2: "Read each ratio as an impedance and the step becomes a reflection Γ = tanh(τ/2)".
- Deep Dive p.2 display: Γ_q = (I_{q+1} − I_q)/(I_{q+1} + I_q) = tanh(½ log(I_{q+1}/I_q)).
- Formal D6: "For 𝑧 = 𝑒^𝑊 ≠ −1, the Cayley expression is tanh(𝑊/2)", with |tanh(W/2)| < 1 iff cos(Im W) > 0 on the principal branch.
- Formal G1: "Multiplying adjacent ratios telescopes", so the inverse I_q = I_0 ∏(1+Γ_j)/(1−Γ_j) is additive in ln z.

Ratio z = 5 (Γ = 2/3) and the wall Γ² = ½ (z = 3 + 2√2):
- The four texts contain no z = 3 + 2√2 and no Γ² = ½ wall in the frame's sense.
- The nearest matches, which I did not verify as the same object: vacuum v6 §9 "The Schottky line. |Γ|² = 1/2, averaged over the visible, separates metals (35 of 35 above) from non-metals (0 of 6 above)." For a real Γ, |Γ|² = 1/2 is the frame's wall point Γ = 1/√2. So the frame's wall point lies on the Schottky circle, but the paper's Γ is the reflection (1 − N)/(1 + N), a different quantity.
- Vacuum v6 Figure 1 caption: "The dashed circle is |G|² = 1/2." Same number, but G is the Möbius disk coordinate of §2, not the Smith Γ.
- Vacuum v6 §9, the "2/3 vacuum-mix line": "Molecular solids crossing the 2/3 vacuum-mix line under squeeze rank their measured metallization pressures". The line is not defined in the text I read. Whether it is the frame's Γ = 2/3 (the ratio-5 edge) cannot be checked from these texts.
- Formal D1 arithmetic (mine): with λ = ν(1 − ν), Γ_b² = ½ corresponds to λ = 1/8, which is ν = (1 − 1/√2)/2 ≈ 0.14645 for a pure state. This is a derived relation, not stated in the Formal edition.
- Highest first-step Γ₁ in these texts: Lr, 0.491. None of the listed Γ₁ reaches 0.707. The frame's eight past-wall first steps (Li, Na, K, Rb, Cs, Be, B, C) are given no Γ value in these texts, so they cannot be tested here.

Phase at a wall; cancel, lock, convert:
- Vacuum v6 §9, the pinned phase at the rim: "near ground the phase is present but pinned" (LOCKED-like).
- Vacuum v6 §9: "Bulk colour hides the phase of Γ, and a thin film writes it back."
- Vacuum v6 §10: "the pairing cancels the even record and only the odd datum survives" (CANCELLED-like).
- Vacuum v6 §10: "Memory is the geometric phase the field keeps around a loop" (CONVERTED-like, the record kept as a phase).
- Formal §7.2: "an intensity-only detector can erase a distinction that a phase-resolved readout retains." This is the amplitude-dies, phase-survives point in a finite model.

Two books per edge:
- Vacuum v6 §1: "a climb (metric, size) and a turn (curvature, phase)".
- Vacuum v6 §5: "The two books separate in the knot's own geometry."
- Vacuum v6 §1: "A loop that comes back still remembers, through its phase (IQGT Ex. 6.5)."
- Formal §1 uses "tennis-racket/two-books constructions" only as a name for the framework, and says the framework's fidelity is unresolved (see §6 below).

Tree/ball:
- Vacuum v6 references list "J. Beasley, Two Trees in One Ball, v4, Zenodo" but the paper does not use it in the body text.
- Deep Dive and Formal do not mention trees or balls.

Lorentz and rapidity:
- Vacuum v6 §10: "the double cover of the Lorentz group".
- Colour report §2: "Steps add by Einstein's velocity-addition law".

Spin:
- Colour report §4: "Two of the prettiest atomic colours are spin–orbit physics" (indium, thallium).
- Deep Dive p.2: "A spin gap concerns spin excitations." and p.8 "spin-orbit partner" for Xe.
- Vacuum v6 §10: the spin lift carries a −1 on the longitude (79 of 79 knots).

Neutrinos and Koide: none of the four texts mentions a neutrino or Koide. The grep for both returned no hits.

---

## 6. Anything that contradicts or complicates the frame

1. The colour report's pre-registered result puts visible ground-state colour on the level IE_1, not on the peel shape: |ρ(Γ₁)| = 0.352 against |ρ(ln IE₁)| = 0.897. If the frame assigns optical phase to Γ at the wall, this text says the Smith step alone does not carry colour for ground-state lines. The report says so itself: "The peel shape tracks it only weakly".
2. The vacuum v6 paper uses Γ three times for three objects: the Smith step (§1), the Möbius coordinate G (§2), and the reflection (1 − N)/(1 + N) (§9). "The rim" is |G| = 1 in §2 and |Γ| = 1 in the frame. These are not the same disk. Any identification of the rims has to be made explicitly.
3. The "2/3 vacuum-mix line" in vacuum v6 §9 and §10 is used without a definition in the text.
4. The vacuum v6 §4 claim that the geometric root is always the one nearest the vacuum is a reading, and the paper marks it so. It is not a contradiction, but the frame's ladder of steps does not assume a nearest-root rule.
5. Torus knots in vacuum v6 have zero decay and pure direction. The frame's closure at the wall is "parabolic on it". The text does not connect the two; they are not identified here.
6. Formal §1 and §16: the Formal edition records a user-reported dispute about another assistant's ledger runs, does not confirm the dispute, and says "Framework fidelity therefore remains unverified". It also says its surrogate models "neither identifies the author's connection-energy observable". So none of the Matter/Gases texts should be read as implementing the frame's two-book edge structure (E⁻/E⁺ = Γ²). That structure is not in these texts.
7. Deep Dive p.7 says "The older paper's statement that a gas at rest is normal is not generally true", and Formal §16.4 lists the same qualification. This corrects the older Matter v5 text and does not touch the frame.
8. Colour report §5.2: "the ridge–colour link did not generalise". The colour onset and the ridge loss are separate events in the Kr-like series. This complicates any reading where a wall both removes a ridge and opens colour.
9. The Schottky test in vacuum v6 §9 rests on 35 metals and only 6 non-metals, so the separation is a small-sample result.

---

## 7. Checks I ran (arithmetic only, from the numbers in the texts)

- He: z = I_1/I_0 = 54.4177655282 / 24.587389011 = 2.2132389; ln z = 0.7944570; Γ = (z−1)/(z+1) = 0.3775751, tanh(½ ln z) = 0.3775751. Matches the Deep Dive and Formal Γ to all printed digits. Γ² = 0.14256, well inside the disk, not near the wall 1/√2 = 0.70711.
- Wall: z = 3 + 2√2 = 5.8284271, Γ = 0.7071068 = 1/√2, Γ² = 0.5. Matches the frame.
- Rn: tanh(0.569/2) = 0.27706, matching the colour report's Γ₁ = 0.277. So the report's τ-to-Γ step is consistent.
- Vacuum v6 Thm 2 constant: |1 − ω|³/4 = 1.2990381 = 3√3/4. Matches.
- Xe: 142.758 − 28.435 = 114.323, matching the difference table. Normal 95% interval 114.323 ± 1.96 × 35.0164 = (45.69, 182.96), matching the Deep Dive interval 45.7–183.0 as.

## 8. Not read or limited

- Colour report figures 1–3 and the vacuum v6 figures fig1–fig4: images, not viewed.
- Formal edition figures 1–2: images, not viewed.
- Deep Dive page 8 figure: viewed as a rendered page; the channel values read from the plot are approximate.
- Deep Dive: the display equations on pages 2, 3, 4, 5, 7, 8 and 10 were read from rendered pages, not from the text layer. Page 6 was rendered but not viewed.
- No Drive file was modified.
