# READ_A1: VOTKP / Elemental Peeling, three early versions

Label: A1. Brief: /home/claude/sm/votkp_reads/BRIEF.md (11 Nov 2026).

## 1. Coverage

| File (Drive id) | Version and date on the paper | Pages | Text read | Read in full |
|---|---|---|---|---|
| Elemental_Peeling.pdf (1NS4tS91uim1WT84nmN5XNqiZaNs_QbWX) | "Combined research manuscript 1.0", 8 Sep 2026 | 13 | 45,611 characters (pdftotext -layout) | Yes, every text line |
| Elemental_Peeling_v2.html (1ybSGKXDeV9qiCiU6cdt33yI3G_spPDHx) | "Research revision 2.0", 8 Sep 2026 | HTML, 2,145 lines | 79,272 characters after tag stripping | Yes, every text line |
| Elemental_Peeling_v3.pdf (1wPn_XmhFvh_5asXigrCwiQ6Qzl3G5m-M) | "Research revision 3.0", 8 Sep 2026 (PDF metadata: Revision 3, 8 Sep 2026) | 37 | 132,691 characters (pdftotext -layout) | Yes, every text line, abstract through bibliography and Appendices A to D |

Not read: raster figures (v1 Figure 1, p.7; v3 Figures 1 to 6, pp.11, 15, 19, 20, 29, 30). The brief says skip images, so only their captions were read. Bibliography entries were read as text. Lean sources, scripts and data archives referenced in the text were not in these files and were not read.

Caveat: the PDF text layer drops some radicals and glyphs. Where a value depends on one, I checked the formula (noted in section 6). The v2 HTML contains doubled LaTeX alt-text; I read the rendered sequence only.

Byline check: all three versions and the v3 PDF metadata give "Jeromie N. Beasley" (with middle initial). The brief and the stored byline rule say "Jeromie Beasley". This is a mismatch in every version.

## 2. What each version defines and claims

**v1 (Combined research manuscript 1.0).** Sections 1 to 9 and Appendices A to C.
- Sec. 1: frames the question "what changed in the specimen, and what information about that change remains accessible?"
- Sec. 2 (Def. 1, Prop. 1, Eqs. 1 to 2): recorded peeling process; three mechanisms; affine energy rescaling Eq. (1); threshold census N_ε with C0 and C1 example; fixed-channel filtration (Prop. 1), with the proof written out.
- Sec. 3 (Eqs. 3 to 10, Props. 2 to 3): Feshbach–Schur reduction Eq. (4); UPG redistribution operator Eq. (5), with "F = 0 if and only if the feedback kernel vanishes identically"; contacted boundary S(E) Eq. (7); graph projector P_S Eq. (8); distance identity Eq. (9); compression K_S Eq. (10).
- Sec. 4 (Eqs. 12 to 17, Props. 3 to 4): exact two-orbital pair H_s, W Eq. (12); T_s(x) Eq. (13); Prop. 3 pair identities, including "T+(1/10) = 8100/19981" (Eq. 14); Prop. 4 prediction bound (Eq. 16, 0.09949015); continuous coupling peel Eq. (17); thermopower via L_j.
- Sec. 5 (Eqs. 18): elemental data, Cu/Ag/Au/Pt ionization increments; optical reflectances; the electronic-sheet conductance Eq. (18).
- Sec. 6: physical geometry; covariant derivative Eq. (19).
- Sec. 7 (Eqs. 20 to 24): Gram map and orientation Eq. (20); singular angle Eq. (21); FOFT flow Eq. (22); Riesz vs range projector Eq. (23); positive-inner-product ladder Eq. (24).
- Sec. 8: verification counts (550 evaluations, 1,700 assertions, etc.); Lean counts; physical programme.
- Sec. 9 and App. A: conclusion; source map.
- App. B (Eqs. 25 to 26): exact remainder identities.

Claim (v1 abstract): "We prove a corresponding limit on prediction from the common scalar record." The pair is identical in conductance G0/2, Fano factor 1/2, gap and optical strength, yet slopes are opposite.

**v2 (Research revision 2.0, HTML).** Adds the following to v1's material.
- Optical positive certificate for removed coupling: Prop. 2 (four-reading certificate), with D = B0 − B1 and β_m formula; the explicit signed example giving B0 = 9, B1 = 3, D = 6, L = 1, β = (6, 3). Finite-precision bound on lost coupling.
- Elemental stress controls: "The shell jump survives" with margins M_c (Eq. unnumbered, "M_c = D_m − c(u_{m+1} + u_m) − max ..."); table of M_3 values.
- Gold-film optical peel: brightens before dimming (R(200 nm) = 0.408191, R(58.209 nm) = 0.426742, R(10 nm) = 0.163082).
- Contact orientation reverses optical-current relation: T(E;θ,α) and correlations +1, 0, −1 at α = 0, π/4, π/2.
- Sign of orbital removal depends on probe energy (g = 0.8, e_d = 0.3, γ = 1).
- Prop. 3 (boundary graph lift), Prop. 4 (equal reduced readings), Prop. 5 (prediction limit).
- Prop. 6 (paired detunings, general contacts), Prop. 7 (two-reference reconstruction, sharp conditioning, Eq. 29).
- Prop. 8 (robust thermally averaged margin, Eq. 34 region).
- Counterfamily "Why a complete boundary snapshot is still insufficient" (ρ family).
- Prop. 9 (finite channel recovery with declared channel bound), Eqs. for c1, c2, c3, and the four-channel counterexample.
- UPG: source recovery, 539-cell raw-detector audit (d_eff), calibration identifiability (Eq. "L C L* = T"), "A projector does not specify a generator", normalization and peeling example.
- Appendix-style "Source map", "UPG source recovery", "Reproduction".

Claim (v2 abstract): "The earlier matched-response pair extends to unequal contacts and has a rigorous positive prediction margin after thermal averaging and bounded Hamiltonian perturbations."

**v3 (Research revision 3.0, PDF).** Keeps v2's results and adds new sections.
- Sec. 2.4: signed changes; pole-count bound replaces positivity (Eq. 3, Prop. 3 with Q = Σ D(y_j)², Eqs. 4 to 6); exact third-reading repair (D(y) with zeros at y = 2, 3; Q = 64/1521).
- Sec. 2.5: phase references restore the quadrature; scalar balanced reconstruction (Eq. 7); OTKP domain control.
- Sec. 3 to 6: elemental data, shell jump, optical stress, paired pair, Grassmannian lift (same content as v2, renumbered).
- Sec. 7.1 to 7.5: paired family, two references, thermal margin, complete-snapshot insufficiency, channel recovery (Props. 7 to 10).
- Sec. 8, 9: geometry and reduction (Gram, singular angle, FOFT, ladder), same as v2.
- Sec. 10 (new): projector-history record. Separates support loss from rotation (Eq. 56). History accumulator Q_τ and identity M_τ = r a_τ + h_τ − 2 Tr(P Q_τ) (Eqs. 57 to 59). Phase-history vs intensity-history paths (Eqs. 60 to 63). Dynamical feedback vs stored history (Eqs. 65 to 66).
- Sec. 11 (new): accessible work through a control graph. Prop. 11 gives W_w = Tr(ρH) − Σ p↓ E↑ per connected component (Eq. 67). Examples with identical Laplacian spectra and work 0 vs 3. Excitation-swap receiver with W_B = ϵ max(0, 2p − 1) (Eq. 72). Qubit coherence example (Eq. 73).
- Sec. 12 (new): nonlinear peel. Three-parameter potential V_s (Eq. 74), Prop. 12 (linear invisibility, H_s(0) = diag(1.44, 1, 0.81)), Prop. 13 (three-force recovery, Eq. 76).
- Sec. 13 (new): three-body map. Jacobi coordinates, mass formulas for α and β, the axis classification Eq. (exact), the cone gap h = √(β(α − β)), the orbit integration.
- Sec. 14: verification counts; Lean status (no fresh Lean build in v3).
- App. A to D: source map; UPG recovery; exact scalar remainder; reproduction.

Claim (v3 abstract): "Recovery of the later three-body manuscript enables a fully specified Jacobi reconstruction and an exact classification of its coincidence axes."

**Changes across versions.** v1 to v2: adds optical certificate, M_c margins, gold-film brightening, contact-orientation sign reversal, probe-energy sign, two-reference reconstruction, channel recovery with counterexample, and UPG raw-data audit. v2 to v3: nothing in v2's results is removed in the text I read. Equation numbers shift between versions (v1 Eq. 12 is v2 Eq. 19 is v3 Eq. 24; v1 Eq. 16 is v2 Eq. 14 is v3 Eq. 19). UPG material moves from the main text (v2 Sec. "UPG source recovery") to Appendix B (v3).

## 3. Element-specific results

Elements named with numbers. Z values are the standard atomic numbers, added by me; the versions do not print Z. Section numbers: v1 / v2 / v3.

| Element (symbol, Z) | Quantity | Number | Section (v1 / v2 / v3) | Versions carrying it |
|---|---|---|---|---|
| Copper (Cu, 29) | NIST ionization: later increment after 11 removals, outer config 3d10 4s1 | 101.67 eV | v1 §5.1 / v2 "Atomic spacing" / v3 §3.1 | all |
| Copper | Shell-jump margin M_3 | 53.32 eV (u_m + u_{m+1} = 1.15 eV) | v2 "shell jump survives" table / v3 §4.1 | v2, v3 |
| Copper | Semi-infinite normal-incidence reflectance, measured constants | 0.538 (450 nm), 0.624 (550 nm), 0.935 (650 nm) | v1 §5.2 / v2 / v3 §3.2 | all |
| Silver (Ag, 47) | Later increment after 11 removals, config 4d10 5s1 | 83.46 eV | as above | all |
| Silver | M_3 | 39.90 eV (u sum 2.52 eV) | v2 / v3 §4.1 | v2, v3 |
| Silver | Reflectance, measured | 0.980 (450), 0.983 (550), 0.990 (650) | as above | all |
| Gold (Au, 79) | Later increment after 11 removals, config 5d10 6s1 | 79.80 eV | as above | all |
| Gold | M_3 | 40.50 eV (u sum 2.40 eV) | v2 / v3 §4.1 | v2, v3 |
| Gold | Reflectance, measured constants | 0.408 (450), 0.792 (550), 0.957 (650) | as above | all |
| Gold | Film at 450 nm, substrate n = 1.5: R(200 nm), R(58.209 nm), R(10 nm) | 0.408191, 0.426742, 0.163082 | v2 "brightens before dimming" / v3 §4.2, Eq. (10) | v2, v3 |
| Gold | Film absorbed fraction at 650 nm: 200 nm, ~20 nm, 10 nm | 0.0434782, 0.0621058, 0.0511145 | v2 / v3 §4.2 | v2, v3 |
| Gold | Two thicknesses with equal R = 0.415 at 450 nm: 44.117737 nm and 86.928161 nm | transmitted 0.106060 vs 0.0114675; reflection phase difference 0.0808052 rad | v2 / v3 §4.2 | v2, v3 |
| Gold | Johnson–Christy films: measured thickness 18.5 to 50 nm; thickness-independent constants 25 to 50 nm; continuum control 10 to 200 nm | range numbers | v2 / v3 §4.2 | v2, v3 |
| Gold | Occupation factor tanh[Δ/(4k_BT)] at Δ = 0.04 eV, 300 K (element not named; the optical example) | 0.368613 | v2 / v3 §4.3 | v2, v3 |
| Platinum (Pt, 78) | Later increment after 10 removals, config 5d9 6s1 | 75.50 eV | as above | all |
| Platinum | M_3 | 6.20 eV (u sum 2.00 eV) | v2 / v3 §4.1 | v2, v3 |
| Platinum | Reflectance, fitted (Rakić) constants | 0.588 (450), 0.641 (550), 0.678 (650) | as above | all |
| Cu, Ag, Au, Pt | Unbracketed NIST entries: four for Cu, two each for the others | counts | v2 / v3 §4.1 | v2, v3 |

Not in any version: a shell wall, closure, colour as a number (CIE 1931 is described, no values), film phase numbers beyond the 0.0808052 rad, a Γ or z for any element, ionization-ratio steps, or the 5,737-step set from today's frame. The "Au" films and the "goldene" references (refs 14, 15) are cited, not computed.

Note: the Au and Pt jumps are isolated-ion NIST thresholds. The versions say so explicitly (v1 §5.1: "It does not identify isolated-ion thresholds with interband transitions").

## 4. Bold moves (mathematical)

1. **Sign of the thermally relevant pair difference at √2** (v2 Eq. "robust-gap"; v3 Eq. 37). Using T−(x) = T+(−x), the difference reduces to Δ(x) = 4x(2 − x²) / [(x⁴ − 2x³ + 2)(x⁴ + 2x³ + 2)]. I checked the numerator algebra by hand: (x⁴+2)(4x) − 2x³(2x²+2) = 8x − 4x³. Assumptions: unit lead widths, the fixed contacts of Eq. (24) / (12), zero-energy reference. Later versions keep it; it is not dropped.
2. **Two calibrated scalar references reconstruct the quadrature** (v2 Prop. 7; v3 Prop. 8, Eqs. 33 to 36). The compression K_θ = (2I − e^{−iθ}S − e^{iθ}S†)/4 at two phases gives A = I − 2K_0 and B = (I − 2K_φ − cos φ(I − 2K_0)) / sin φ. The constant 2/√(1 − |cos φ|) is minimal at φ = π/2. Assumptions: unitary S, Hermitian measurement errors, calibrated coordinates.
3. **Channel count from three cumulants with a declared bound** (v2 Prop. 9; v3 Prop. 10). Newton identities give the cubic with roots equal to the transmissions. Counterexample: A = (1/5, 1/2, 4/5) and a four-channel set with the same (p1, p2, p3) = (3/2, 93/100, 129/200). Explicitly: "the channel bound cannot be inferred silently." Assumptions: zero temperature, unidirectional injection, energy-independent channels.
4. **Signed responses detected by sampling a grouped residue matrix** (v3 §2.4, Prop. 3). Q = Σ D(y_j)² has ker Q = ∩ ker A_m. Opposite residues at the same pole cancel at every frequency. Assumption: known pole count ℓ ≤ r.
5. **Projector-history accumulator with a rank-change correction** (v3 §10.2). M_τ(t) = r a_τ + h_τ − 2 Tr(P Q_τ). Omitting h_τ when rank changes gives zero where the true value is M_1(1) = e^{−1/2} − e^{−1} = 0.2386512185 (I rechecked this value).
6. **Ideal work depends only on control-graph components** (v3 Prop. 11, Eq. 67). Example with identical Laplacian spectra {0, 0, 2, 2} and work 0 vs 3 (I checked both values by hand). Assumption: arbitrary-duration control; the chain limit s → 0 is discontinuous because of this.
7. **A nonlinear peel invisible to all linear probes** (v3 Prop. 12, 13). Three attenuation parameters leave the common linear susceptibility unchanged; three forces recover them exactly (checked the formulas by hand). Assumption: the stated polynomial potential.
8. **Mass-weighted axis classification** (v3 §13.2). α = β iff equal masses; for (1, 2, 3), α = 49/72, β = 1/2, and the cone gap h = √13/12 gives gap/radius = 2√13/3 = 2.40370085 (checked). Assumption: the declared Jacobi map and metric; the paper says the historical helper was not recovered.

Strongest element results (section 3 items): Au film thickness pair with equal R = 0.415 but different transmission and phase; the M_3 margins for Cu, Ag, Au, Pt; the Au brightening sequence. Boldest moves for a wall reading: items 1 and 2.

## 5. Connections to today's frame

Each line is quoted below with its location. Quotes are under 15 words.

- **√2 crossing.** v2 (robust-gap section, Eq. "robust-gap"): "its sign is positive on 0 < x < √2 and negative above √2" (v3 Eq. 37 text is the same). This is a sign change at √2 of T− − T+, which is not Γ² = ½ and has no Γ identification in the text.
- **The number ½.** v2 Prop. 4 item 1 / v3 Prop. 5 item 1: "both have G/G0 = T = 1/2". This is a transmission value at zero energy, not a Γ² wall. Same number, different role; no identification is made.
- **Γ² = ½ as reflectance (untested).** If the frame's Γ is a normal-incidence amplitude, then Γ² is the R of the semi-infinite table. The table at 450 nm has Au 0.408 (below ½), Cu 0.538 and Pt 0.588 (above ½). This is an observation from the printed table only, not tested against the frame.
- **Cancel.** v3 §2.4: "Opposite changes A and −A at the same pole cancel at every frequency." Related to the frame's CANCELLED, but the version does not treat it as a spin partner.
- **Phase and amplitude.** v1 §3.3 and v2/v3 §5.3: "Squaring has removed the sign of X." The graph projector keeps the phase record; the compression K_S loses its sign. Structurally similar to "phase survives where amplitude dies" but the version does not use the word wall.
- **Phase is relative.** v3 §2.5: "The phase is relative to the reference." and "A lone quantum ray's global phase leaves its projector unchanged." The frame's "phase survives" must be a relative phase to fit this version.
- **Two readings, opposite signs.** v1 §4 / v2 Prop. 4 / v3 Prop. 5 item 4: slopes T′_s(0) = −s for s = ±1. The paired H_s is a pair with opposite signs. The version gives no ratio E⁻/E⁺, so this is structural only.
- **Spin.** v1 §4: "Consider two noninteracting, spin-degenerate two-orbital models." Spin enters only as a degeneracy factor in the counting formulas (v2/v3 §7.5 "spin multiplicity").
- **Tree or ball, Lorentz or rapidity, neutrinos, Koide.** Not present in any of the three versions. The Riemannian/Lorentz question does not arise (the version works with Hermitian and unitary objects only).
- **Threshold λ-census.** v1 §2.1 (Eq. 2): N_ε counts eigenvalues in [ε, 1−ε]; the window is at ε = 0.1 in the example. A numeric threshold, not the Γ² wall.

## 6. Anything that contradicts today's frame, and checked discrepancies

No direct contradiction with the frame was found. Items that need care:

- **Global phase.** v3 says global phase is not physical (quoted above). The frame's "phase survives" must mean relative phase to a fixed reference.
- **Ionization steps.** The frame's 5,737-step set and its 8 past-wall steps (Li, Na, K, Rb, Cs, Be, B, C) are not in these files. The versions use only 10 to 11 successive removals per element and give increments in eV, not ratios. The frame's z cannot be computed from the paper, so the test is untested.
- **Discrepancy: d = 2 in v3.** v3 §7.1 reads "For the original g = 1 pair, d = 2". v2 reads d = √2. The formula √8 g²/(1 + g⁴) gives √2 at g = 1, and the stated g = 0.1 value 0.014141 = d/2 matches √2 scale. Treat v3's "d = 2" as a dropped radical or a misprint.
- **Checked, consistent: v3 Eq. (63) separation.** The text says "greater than 0.727". The printed bound 4√(2k) ε a_τ with k = 2, ε = 0.05, a_τ = 1 − e^{−1} gives 1.233009 − 2 × 0.25277 = 0.7274. So the number is consistent once the radical covers 2k.
- **Checked, consistent: v3 §10.3** at τ = 1: 1.233008643848, half-value 0.616504.
- **Checked, consistent: v3 Prop. 9** margin: 0.040124, matching "exceeding 0.0401".
- **Checked, consistent: v2 Prop. 2 example** (B0 = 9, B1 = 3, D = 6, β = (6, 3)).
- **Checked, consistent: v3 Prop. 10 example** (p1 = 3/2, p2 = 93/100, p3 = 129/200 for A; F = 19/50).
- **Glyph loss, not an error: v3 §13.2** "a = 5/7 = 0.8451542547" is √(5/7); the decimal confirms the root.
- **v3 §13.4 self-disclaimer.** The paper says its recomputed orbit "does not reproduce v3's −4.463 or its slope 2.16280". Not a contradiction with the frame; a flagged inconsistency inside the paper.
- **Byline** (see section 1): "Jeromie N. Beasley" in all three versions.
- **Data credit.** The raw detector data are "credited to Uusnäkki and coauthors" (v2 and v3 App. B). They are not the author's own measurements.
- **Lean status.** v1 claims 16 finite declarations compiled at commit 3eb373797a26; v2 says no local Lean executable was available; v3 says no fresh Lean build. Earlier certificates are not re-verified in these files.
