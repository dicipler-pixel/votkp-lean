# READ_A8: Matter, Then On Down (VOTKP reads)

Label: A8. Memory: not used. Originals untouched; copies in /home/claude/sm/votkp_reads/src/A8/, text in /home/claude/sm/votkp_reads/text_A8/.

## 1. Coverage

| File | Read | Notes |
|---|---|---|
| cb26e5eb matter_then_on_down_v2.pdf (23 pp) | Full (text_A8/v2.txt) | Narrative spine; offset, rim distance, Petermann |
| f8a17bd4 matter_then_on_down_v4.pdf (86 pp) | Full in earlier pass; sections 7, 9.3, 9.4, 10 and the element table re-checked | Latest paper |
| cafaae8f Atlas_II_Past_the_Wall HTML | Full | W1–W9 cards |
| dc165c60 Russell_Corrected HTML | Full | Seven plates |
| bf39b821 Matter_Combined_Assessment HTML | Full | |
| dd4fce2b Matter_Reconciled_Review HTML | Full | |
| 8f41f04d Matter_Combined_Checks.zip (zip1/) | build_comparison.py read in full; combined_checks.py and JSON listed, not re-run | |
| 60d29b12 Matter_Review_Sources_and_Checks.zip (zip2/) | build_review.py read; reviews/*.md read; code JSON checked earlier | |
| matter_all_we_have (inventory) | Full | |
| combined_docx (Combined Edition) | Full | |
| v3 (zip2 copy, text v3_zip2.txt) | Sections 1–7 and Appendix A (lines 1–560) read in full | Lean and script tail (lines 560–1900) matched against v4 by grep, not read line by line |

Frame terms grepped across all text: no hits for √2, 2√2, 3+2√2, 5.83, 1/√2, Γ²=½, Koide, C, N, francium, Fr, relativistic, alkali, Rb, K, Cs. "Wall" appears only as the spectral/geometric wall (v4 §9.4), the critical wall (figures) and the rim.

## 2. Section-by-section claims

- **v2 / v3 §1 (zero, span, census).** "A = 2c/π²" for an interval [T]. Measured 0.202692 (c=1) and 0.103689 (c=½) against 2/π² and 1/π².
- **v3 §2.1, Prop. 1.** "Γ = tanh(ε/2) = 1 − 2ν", "∫H dε = π²/3" [T], checked to 1.1e−16 (s01).
- **v3 §2.2, eq. (3)–(4).** Defect split C_A − C_A² = (C−C²)_AA + X_A; "Tr X_A ... is the coupling energy E_B". Offset speed limit τ̇² ≤ 4gS [T]. "If P H (1 − P) = 0 the offset is frozen."
- **v3 §2.3 / v4 §2.4 (warm ring).** Raw count 2→24→64, boundary count 2→0→0; Tr X_A = 0.170835 at T=0.5. Combined assessment corrects "no boundary" to "zero channels above threshold".
- **v3 §2.4 (gas).** Γ0 = 0.377575066984 "at every density from 10¹⁸ to 10²⁶ m⁻³" [R]; naive read-back biased to 0.366149 with T-dependent partitions.
- **v3 §3 Thm 2.** "Peel steps add like velocities", u ⊕ v = (u+v)/(1+uv) [T]. Ising c=½ ladder is a constant peel step [V].
- **v3 §4 (atom).** Helium thresholds 24.587389011 and 54.4177655282 eV; binding sum 79.0051545392 eV; Γ0 = 0.377575066984. Sodium: eleven thresholds, walk end 0.9938 (v4: 0.9937851).
- **v3 §5 / v4 §7 (nucleus).** "|Γ| − 1 = 2s/(S_next − s)" exact [T]. "A negative ratio has Im W = π exactly." Random complex z: zero mismatches over 4000 draws.
- **v3 §6.1–6.2 (opened SSH).** "⟨K⟩ = 1 + u²/(E(0)E(π))" [T]; exit at v = 0.468 for u = 0.5 [V]; massive-band exit filter-dependent (0.27164 / 0.16917 / 0.12272) [V].
- **v3 §6.3 (quarter-turn).** "⟨K⟩ = sec²(½ Im τ)" [T]; census rotation does not match this formula away from exit, 4e−6 to 3.4e−2 [V].
- **v3 A.10 (last peel step).** "Γ = 5/(8Z−5)" for helium-like ions, first order; needs Z ≥ 2 (not stated in text).
- **v3 A.9 (scale blindness).** Stated for "a nonrelativistic Coulomb system" only.
- **v3 A.12–A.15 (rim, Cayley pole, quarter turn).** "S2/S1 = −1 ⇔ S1 + S2 = 0"; "|Γ| < 1 ⇔ Re z > 0".
- **v4 §9.1 (Theorem 9.1).** Defines "Rb(λ) = |1 − 4λ|" but the example "YA = −2 and Rb = 3" needs the square root (|1−4(−2)| = 9).
- **v4 §9.4 (two kinds of wall).** Opened-matter exit is spectral: eigenvalues ±√(1−γ²) turn imaginary at γ=1; Petermann factor (1−γ²)⁻¹. Geometric wall: spectrum stays real.
- **v4 §10 (even/odd halves).** Prop. 10.1: census and Γb even under complement; Γ and τ odd; g = Re Q even, Ω = 2 Im Q odd.
- **Combined Edition §6 (joint proposition).** H = ωσx, P±(0) = (I±σy)/2: ν± = (1 ± sin 2ωt)/2, τ± = ∓2 artanh(sin 2ωt). My arithmetic confirms τ̇² = 16ω²/cos² = 4gS for both (g = ω², S = 4/cos²).
- **Combined Edition §7 (IQGT).** Q_Π(V,W) = Tr(ΠVW) is a Frobenius inner product; |Ω| ≤ 2√(g(V,V)g(W,W) − g(V,W)²) [T]. Lean-checked per the paper.
- **Atlas II W1.** Edge at kept/erased cut: Γ = −1, "the rim, with equal books" (E⁻ = E⁺).
- **Atlas II W2.** "s = ½ at k(τ_rim − τ₀) = 2.30614"; share "starts at four fifths on the kept moment" (not verified here).
- **Atlas II W4.** Operator share ½ at L_max = 1.
- **Russell Corrected.** "E = ½mv² + ½kx²": "the two stores average equal shares: ½ and ½"; "V_eff = −GM/r + L²/2r²".
- **matter_all_we_have G2 (PASS).** "γ² = u²/(E(0)E(π)) = K̄ − 1 exactly", worst 2.8e−14 over 20000 samples. Ties the exit line to B153's rapidity.
- **matter_all_we_have G1 (not run).** Offset speed limit on the neutrino ledger edge P H(1−P): kill line τ̇² > 4gS by 1e−9.
- **build_review.py / build_comparison.py.** Builders only; they hard-code dates and the "Jeromie Beasley" footer. No new numbers.

## 3. Element-specific results

| Element | Z | Quantity | Number | Section |
|---|---|---|---|---|
| H-like | 1 (general Z) | I_H = Z²/2 Hartree | formula | v3 A.10 |
| He | 2 | I, I' thresholds | 24.587389011, 54.4177655282 eV | v3 §4 |
| He | 2 | Γ0 | 0.377575066984 | v3 §4, §2.4 |
| He | 2 | binding sum | 79.0051545392 eV | v3 §4 |
| He | 2 | last step, first order (my arithmetic at Z=2) | 5/11 = 0.4545 (≈20% off exact 0.3776) | v3 A.10 |
| He (general Z) | Z | last peel step | 5/(8Z−5) | v3 A.10 |
| Na | 11 | peel walk end, 11 thresholds | 0.9938 (0.9937851) | v3 §4, v4 fig |
| 5He | 2 | Γ (S_first −734.8 keV, S_next 20577.6) | +1.074062 (|Γ| 1.074) | v4 §7 |
| 5Li | 3 | Γ (−1966.1, 19813.9) | +1.220318 | v4 §7 |
| 8Be | 4 | Γ (−91.8, 7366.6) | +1.025238 | v4 §7 |
| 7Li | 3 | Γ (7251.1, 5664.4) | −0.122852 (inside) | v4 §7 |
| 4He | 2 | Γ (20577.6, 5493.5) | −0.578576 (inside) | v4 §7 |
| 12C | 6 | appears only as parent ladder of 8Be | no value | v4 §7 |
| C, N, Fr, K, Rb, Cs | 6, 7, 87, 19, 37, 55 | none | not in paper | — |

Signed Γ for 7Li and 4He: the Reconciled Review (line 108) notes v3's table printed magnitudes; v4 gives signs.

## 4. Bold moves

1. One coordinate, four lands: threshold, offset, scalar edge and Hawking pair share Γ = tanh(½ ln ratio) (inventory bridge table; v3 §1, §3).
2. Unbound nuclei are half-turn peels: Im W = π for negative ratios (v3 §5), exact rim distance 2s/(S_next − s).
3. The exit line: E(0)E(π) = u² ⇔ ⟨K⟩ = 2 ⇔ γ = 1 ⇔ B153 rapidity diverges (matter_all_we_have G2, PASS).
4. Speed budget does not choose the future: two projectors with equal coupling energy move offsets in opposite directions (combined §6).

## 5. Connections to today's frame

- **Γ² = ½ wall = z ≈ 5.83.** My arithmetic: z = 3 + 2√2 = (1+√2)² gives Γ = (z−1)/(z+1) = 1/√2 and Γ² = ½. Equivalently ε = ln z = 2 arsinh 1 and Γ = tanh(arsinh 1). The paper never states this circle; its only rim is |Γ| = 1.
- **Census on that circle.** ν(1−ν) = (1−Γ²)/4 = 1/8 there; Γb = √(1−4λ) = 1/√2 at λ = 1/8.
- **C/N, francium, relativistic alkalis.** Not in these files. Re-running the frame's z values through Γ²: C (6.08) 0.515 > ½ (crosses); N (5.64) 0.488 < ½; Fr (5.50) 0.479 < ½; Cs (5.95) 0.507 > ½; Rb, K, Na all above. The pattern matches your run, which implies the wall is Γ² = ½ in this coordinate. Caveat: the paper's theorems are stated for nonrelativistic Coulomb systems only (v3 A.9, A.10, A.11), so a relativistic alkali such as Fr is outside their proved scope.
- **Phase at a wall, quarter and half turns.** Sector flip (B186) = quarter turn; half turn = Cayley pole = unbound (A.12); v4 §9.4 spectral vs geometric wall.
- **Two books and rim.** Equal books at the rim (atlas W1), share ½ at k(τ−τ0) = 2.30614 (W2).
- **Neutrinos.** Neutrino state starts at |Γ_eff| = 2 and drains in (W2); edge at kept/erased cut is Γ = −1.
- **Lorentz/rapidity.** Peel steps add like velocities (v3 Thm 2); γ = |v|/√(E_min E_max) is the rapidity of the exit line (G2).
- **Spin.** Only two-level Pauli/Bloch models (joint proposition, P1). No spin physics.
- **Koide, tree/ball, lock/convert/cancel:** no treatment found.

## 6. Contradictions with the frame or internal inconsistencies

1. v3 §1 says the two census coefficients "bracket 1/π² from both sides"; both values lie above prediction (v4 corrects to "2.3% above").
2. v3 §2.2 and v4 §10 table print Γb = 1 − 4λ; the root is needed (A.6 has it).
3. v3 §1 prints "c = 21"; should be c = ½ (v4 fixed).
4. v3 A.2 and v4 line 1423 print "Scut = 6c ln(ξ/a)"; should be (c/6). The A.2 derivation uses c/6.
5. v4 Theorem 9.1: Rb = |1−4λ| with example Rb = 3 for λ = −2 (needs the root).
6. v3 A.10 is first order only; at Z = 2 it misses exact Γ0 by about 20%.
7. Frame's "Γ² = ½ wall": not in the paper; the paper's rim is |Γ| = 1, so the circle needs its own card.
8. Lean run 41729732315 cited but not verified (matter_all_we_have).
