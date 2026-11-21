# The Offset Belongs to the Boundary and The Loop Wall: a checked map of connections

Prepared 21 November 2026 for Jeromie Beasley. Local working file only. Nothing was written to GitHub or Drive and nothing was committed.

## 0. Which versions were read

- **The offset paper.** The task brief named v27 as the latest version. Drive holds later ones: v28, v29, v30 and **v31** (6 September 2026). The 13 October `CURRENT_PAPERS_20261013.md` index lists v31 as the version on Zenodo (record 22555919, `the_offset_belongs_to_the_boundary_v31.pdf`, 92 pages). I read **v31 in full** and **v27 in full** (`_v27_submission.pdf`, 60 pages). I used v27 for the material v31 dropped:
  - the rail angle ψ with ũ = tan(ψ/2);
  - the offset angle χ with Tr K_A = gd⁻¹(χ);
  - the second-cocycle data;
  - the arithmetic-Kakeya "four facts".
- **How the notes in the brief compare with the text:**
  - K_A = log[(1−C_A)/C_A], Tr K_A = log P(N_A=0) − log P(N_A=L): found (v31 Eq. 7 and 11).
  - |Tr K_A| = 2 artanh(v/√(Emin Emax)): found. It is graded [R] in v27. In v31 it is proved for every fixed connected gapped model (Theorem E7).
  - Spacing Δ = 4πK(ũ)/K′(ũ) with ũ = tan(ψ/2): this is v27 notation (Eq. 31, Sec 6.3). v31 writes Δ* = 4πK(m)/K(1−m) with m = k_e² and k_e = Emin/Emax (Eq. 92), and does not mention ψ.
  - Ladder phase as an Abel map: found (v31 Eq. 95–96, v27 Eq. 19–20). Graded R+V (recognised and verified).
  - Census A = 2c/π²: found (v27 Eq. 33; v31 Eq. 103 and Sec 7.10, where it is phrased as "consistent with 2c/π²").
  - S = P∘R: found (v27 Theorem 10 and Sec 8). v31 has Theorem 5 and Sec 3.7, where the written realization is said to be antiunitary.
  - K_A = cT + bI: found. It is v27's "road", and v31 Sec 7.1 says it holds only on cut-localized modes.
  - ε = ln((1−ν)/ν): found.
  - **Sign:** v31 Eq. 12 is λ = 2ν − 1 = −tanh(ε/2). The brief's "Γ = tanh(ε/2)" is the same relation written for Γ := 1 − 2ν. I use that sign throughout so that it matches the element paper.
  - Gluing, sublattice, L mod 4 and the 2D seams: all found.
- **The element paper.** Repo `votkp-lean`, branch `element-paper/loop-wall`, folder `research/2026-11-20-element-paper-loop-wall/`. I read `README.md`, `QUANTUM_CHEMISTRY_LINKS.md`, `CLAUDE_REVIEW.md`, `REVIEW_GUIDE_20261121.md` and `SECOND_HOUR_20261121.md` in full. I skimmed `lean/LoopWall.lean` (every theorem statement read, proofs skimmed) and read the text of the v8 page (`VOTKP_Element_Paper_Loop_Wall_v8_20261121.html`) in full.
- **Two Trees.** `two-trees/lean/PeelTrees.lean` proves the threshold at sample ratios: `schottky_five_below` (z = 5 sits below Γ² = 1/2) and `schottky_seven_above` (z = 7 above). It also proves the boost entries cosh = (1+Γ²)/(1−Γ²) and sinh = 2Γ/(1−Γ²). A general theorem that Schottky holds exactly above Γ² = 1/2 was **not found** in that file. Only the threshold at those two ratios is proved there.

## 1. The one formula both papers share

The element paper's peel reflection is the Cayley map:

  Γ(z) = (z − 1)/(z + 1) = tanh(½ ln z),  z = (1 + Γ)/(1 − Γ),  Γ(1/z) = −Γ(z),  Γ(Γ(z)) = −1/z.

The offset paper uses this same map in at least eight places without naming it. Seen this way, its whole set of moduli is a set of peel reflections of ratios of the Rice–Mele chain. The loop wall Γ² = ½ can then be read off at each place. This is the spine of the map below.

## 2. Summary table

| # | Connection | Grade |
|---|---|---|
| E1 | The finite boundary asymmetry a_N is Γ(P_empty/P_full). The offset τ = ln z = 2 artanh a_N. v31's Hankel ratio is also read through Γ (Eq. 68). | EXACT |
| E2 | Every entanglement level is a peel step: z_i = (1−ν_i)/ν_i, ε_i = ln z_i, Γ_i = 1 − 2ν_i = tanh(ε_i/2) | EXACT |
| E3 | Reversal: v → −v, or a one-site translation, sends z → 1/z and Γ → −Γ, and keeps Γ² | EXACT |
| E4 | Protected zero: τ = 0 ⇔ z = 1 ⇔ Γ = 0 (the matched junction) | EXACT (formula); the protecting mechanisms differ (S2) |
| E5 | Dimerization modulus u = Γ(t1/t2). The intercept variable u0 = Γ(t2/t1). The Abel-map amplitude sin φ = u/k_e is a ratio of two reflections. | EXACT |
| E6 | Combined modulus k_e = Γ(e^{1/ξ_c}). The Ising field h = Γ(Emax/Emin) = e^{−1/ξ_c}. The Landen step is the Cayley map. | EXACT |
| E7 | Offset angle tan(χ/2) = γ. sec χ = cosh τ = (1+γ²)/(1−γ²) is the Two Trees boost entry, and 2 sec χ = z + 1/z. | EXACT |
| **E8** | **The loop wall on the Rice–Mele rail:** t1² + t2² + v² = 6 t1 t2 ⇔ k_e² = ½ ⇔ the mid-gap transfer matrix has trace magnitude 6 ⇔ Δ* = 4π exactly. On the dimerized line this is t2/t1 = 3 + 2√2. | **EXACT** (measured spacing 4π to 10⁻¹⁹) |
| E9 | The wall as the offset paper's census window: \|ε\| ≤ ln(3+2√2) ⇔ ν(1−ν) ≥ 1/8 (half-power = half the maximum variance) | EXACT |
| E10 | Two faces γ = \|v\|/Q and δ = \|t1−t2\|/Q satisfy γ² + δ² = k_e. The element paper's loop-closing test is then the offset paper's connected regime. | EXACT algebra; meaning STRUCTURAL |
| **E11** | **The offset itself against the wall:** γ² = ½ ⇔ 2v² = Emin Emax. At equal hopping this is v = 2t/√3, where τ∞ = ln(3+2√2). Finite blocks converge to it. | **EXACT** (measured) |
| E12 | Chemistry form: a_N = (s0 − s1)/(s0 + s1) is "hardness over electronegativity" of the boundary site's vacancy and occupation pair | EXACT algebra, different objects → STRUCTURAL |
| E13 | Element "third reading" (second moment of ‖P_ij‖²) for the Rice–Mele chain = ∫ g^P_kk dk/2π, v31's intrinsic projector metric (Eq. 20) | EXACT (Parseval; checked to 10⁻¹⁵) |
| E14 | v31 Conjecture E6's step ratio ρ = Γ(w)², w = √((Emax+Emin)/(2Emin)): a returned power | EXACT algebra (the conjecture itself stays R+V) |
| S1 | The interior cancels and the boundary survives: Schur reduction (offset) against telescoping rapidities and peel-inside versus junction-on-face (element) | STRUCTURAL |
| S2 | Symmetry protection: S = P∘R against the matched junction. Reflection alone protects a ratio; it does not protect a log-odds. | STRUCTURAL, with a lesson running back to the element paper |
| S3 | Even and odd halves: F_even/F_odd and the two Z₂ labels (offset) against Γ²/sign Γ and screw sign (element) | STRUCTURAL |
| S4 | Junction sum rule against the offset's even partner Tr(C_A − C_A²) = cut-crossing Σ\|P_ij\|² | EXACT identity, STRUCTURAL role |
| S5 | Gluing quantum ±2τ∞ = reversing one peel step's direction | STRUCTURAL (exact given the paper's sign theorem) |
| S6 | Schur elimination of the interior against the element's eliminated-layer (Löwdin, Feshbach) peel identity | STRUCTURAL |
| S7 | 2D kink charge flips under reversed displacement; screw sign flips under mirror | STRUCTURAL-weak / LEAD |
| S8 | Shared method: kill condition first, positive control beside every null, frozen predictions, exact-arithmetic Lean with false controls, cutoff windows | Method |
| L1–L6 | Leads, listed in Sec 5 | LEAD |

## 3. EXACT connections, each with the reason the check proves it, then the check

The grades follow the brief. EXACT means the same formula, shown by algebra. Each check is a script in `checks_offset/`, with its output beside it.

### E1. The offset is a peel reflection of empty against full

**Statement.** v31 Theorem 9 defines a_N = (m_N − p_N)/(m_N + p_N), where m_N = s0 is the vacancy Schur complement of the added site and p_N = s1 is its occupation Schur complement. It proves τ_{A_N} = log(m_N/p_N) = 2 artanh a_N. With z := m_N/p_N, which equals P_empty/P_full once the protected even interior cancels (Theorem 8), this is exactly the element paper's

  Γ(z) = (z−1)/(z+1) = tanh(½ ln z),

with τ playing the part of ln z = 2h. The common scale d_N = (m+p)/2 is the mean of the two thresholds. v31's equal-hopping proof uses the same map again: Eq. 68 is â_n = (ℛ_n − 1)/(ℛ_n + 1) = Γ(ℛ_n), where ℛ_n is a ratio of Hankel determinants. Its limit ℛ∞ = (√M + √e)/(√M − √e) gives Γ(ℛ∞) = √(e/M) = √k_e.

The Lean certificates are twins. The offset side has `scalarOffset_eq_logRatio`, `asymmetry_eq_tanh`, `common_factor_exact` and `logRatio_neg`. The element side has `gam`, `gam_inverse`, `gam_reverse`, and `smith_identity` in `VOTKP/Smith.lean`.

Prior art inside the corpus: atlas card B153 ("The offset is a rapidity: τ = 2 artanh a") and card B204 ("Adding one site moves the offset by log(s0/s1)"). Both are listed in `paper/votkp_v3_2/code/atlas_map/CARD_INDEX.md`. What is new here is that this rapidity is the loop-wall Γ, and the readings of the wall that follow from that.

**Why the check proves it.** The identity is algebra. What the run tests is that the paper's own objects, built from v31's Appendix C covariance, obey it with the printed sign conventions, and that z really is the Schur ratio s0/s1.

**Result** (OFFSET-LW-01, 110 digits, reference (0.6, 1, 0.4)):
- |a − Γ(z)| ≤ 4×10⁻¹¹² at L = 5, 9, 13, 17.
- |z − s0/s1|/z ≤ 5×10⁻⁹⁶.
- τ₁₇ = 0.881157076037163154637, which equals v31's printed 0.881157076037163154636968… This is the positive control.
- OFFSET-LW-07 gives Γ(ℛ∞) − √k_e ≈ 10⁻⁴¹ at three equal-hopping points.

### E2. Every entanglement level is a peel step

**Statement.** v31 Eq. 7 and 12 say e^{ε_i} = (1−ν_i)/ν_i and 2ν_i − 1 = −tanh(ε_i/2). So each level is a peel step with ratio z_i = (1−ν_i)/ν_i (vacancy odds), rapidity h_i = ε_i/2 and reflection Γ_i = 1 − 2ν_i. A thermal occupation ν = 1/(1+e^ε) gives Γ = tanh(ε/2). Run backwards, every element peel step is a fermionic level: its occupation is ν_k = 1/(1+z_k) = IE_k/(IE_k + IE_{k+1}) and its entanglement energy is ε_k = ln z_k.

**Check** (OFFSET-LW-01): over all 17 levels of the reference block, max |2ν − 1 + Γ(z_i)| = 8×10⁻¹¹². Applied to single levels, the wall is |ε| = ln(3+2√2) = 1.762747. **Exactly one of 17 levels is inside: the central rung ε = 0.99706.** That one level carries **72.0%** of the block's entanglement entropy (0.5828 of 0.8098). Every other level has |ε| ≥ 7.1.

### E3. Reversal

**Statement.**
- v31 Theorem 4: τ(−v) = −τ(v).
- v31 Proposition 6: translating an odd interval by one site negates its spectrum.
- In peel terms both are z → 1/z, Γ → −Γ, with Γ² kept. This is element `gam_reverse` and `power_even`.
- The element paper's sentence "a ledger of Γ² alone cannot tell the two orders apart" is the offset paper's Sec 12.6 point that squaring τ or taking its absolute value gives different functionals and hides a real sign.

**Check** (OFFSET-LW-01, L = 17): z(v)·z(−v) − 1 = −2×10⁻⁹⁶. z(start 0)·z(start 1) − 1 = 8×10⁻⁹⁷, and the two Γ² agree to 3×10⁻⁹⁷.

### E4. The protected zero is the matched junction

**Statement.** τ = 0 ⇔ P_empty = P_full ⇔ z = 1 ⇔ Γ = 0. This is element `matched_junction` (gam 1 = 0) and offset `protected_zero_of_pairing`.

**Check:** for the protected even block (L = 16), z − 1 = −2×10⁻⁹⁷. The protecting mechanisms are not the same; see S2.

### E5. The dimerization modulus is a peel reflection

**Statement.**
- u = (t1 − t2)/(t1 + t2) (v31 Sec 7.5) is Γ(t1/t2).
- The intercept variable u0 = (1 − r)/(1 + r), r = t1/t2 (v31 Eq. 113), is Γ(t2/t1) = −u. So the exact rational series h(u0)/(π/8) = 1 − (5/8)u0² − (9/64)u0⁴ − (65/1024)u0⁶ − … is a power series in the peel reflection of the hopping ratio.
- The Abel-map amplitude sin φ = u/k_e (v31 Eq. 95) is the ratio of two peel reflections, Γ(t1/t2)/Γ(e^{1/ξ_c}).

**Check** (OFFSET-LW-02): u − Γ(t1/t2) = 0 and u0 − Γ(t2/t1) ≤ 3×10⁻⁵², at three hopping ratios.

### E6. The combined modulus and the Ising field are peel reflections

**Statement.**
- v31 Eq. 19 gives ξ_c = 1/(2 artanh k_e), so k_e = tanh(1/(2ξ_c)) = Γ(e^{1/ξ_c}): the modulus is the reflection of the correlation rail.
- The inner branch point h = (1 − k_e)/(1 + k_e) (v31 Sec 7.4) equals Γ(Emax/Emin), the reflection of the band-edge ratio, and equals e^{−1/ξ_c}.
- The descending Landen step h = (1−k)/(1+k) is −Γ(k).
- The Cayley map has order four: Γ(Γ(z)) = −1/z.

**Why the check proves it.** h is taken as the root of the symbol quadratic t1t2w² + (t1² + t2² + v²)w + t1t2 = 0, not from the formula. It is compared with Γ(Emax/Emin), and both are compared with the **"Matched h" column printed in v31 Sec 7.4**. That last comparison is against the paper.

**Result** (OFFSET-LW-02): all five printed values agree to every printed digit:

| Substrate | Computed h | Printed h |
|---|---|---|
| (0.6, 1, 0.4) | 0.489206414021 | 0.489206414 |
| (0.5, 1, 0.3) | 0.448035875161 | 0.448035875 |
| (0.7, 0.9, 0.2) | 0.70153161108 | 0.701531611 |
| (0.8, 0.8, 0.5657) | 0.499991411655 | 0.499991412 |
| (0.3, 1, 0.4) | 0.255690650045 | 0.255690650 |

The identities k_e = Γ(e^{1/ξ_c}) and h = e^{−1/ξ_c} hold at the 10⁻⁵² floor.

### E7. Offset angle, Two Trees boost, second-cocycle trace

**Statement.** v27 Eq. 16 sets tan(χ/2) = γ and gives Tr K_A = gd⁻¹(χ). In peel terms this reads Γ = tan(φ/2) with φ = gd(ln z). Then:
- sec χ = cosh τ = (1+γ²)/(1−γ²). This is the Two Trees boost entry cosh = (1+Γ²)/(1−Γ²) in `PeelTrees.lean`.
- 2 sec χ = z + 1/z.
- At the wall Γ² = ½ this gives sec χ = 3, so the "second unimodular matrix" of v27 (trace 2 sec χ, the object of open problem OP3) has **trace 6 = z_w + 1/z_w**. That is the element paper's wall polynomial z² − 6z + 1 = 0 written as a trace.

**Check** (OFFSET-LW-01): sec χ − cosh τ = 2×10⁻¹¹¹ and 2 sec χ − (z + 1/z) = 3×10⁻¹¹¹.

### E8. The loop wall on the Rice–Mele correlation rail (the strongest new result)

**Statement.** Because k_e = Γ(e^{1/ξ_c}) (E6), the loop wall applied to the correlation rail is k_e² = ½. All of the following are the same condition:
- Emax² = 2Emin².
- **t1² + t2² + v² = 6 t1 t2**, which is ρ = (t1² + t2² + v²)/(2t1t2) = 3.
- In the rail language of v27 Sec 6.3: sec ψ = 3, rails 3 ± 2√2, and the mid-gap cell transfer matrix has trace magnitude 6 (v27 OP3: −tr M(0) = 2 sec ψ).
- On the dimerized line v = 0 it is r² − 6r + 1 = 0 with r = t1/t2. **That is the element paper's `wall_quadratic` z² − 6z + 1 = 0 with z = t2/t1.**
- The returned power is m = k_e². The transmitted power is 1 − m = 4t1t2/Emax² = κ̃², v27's band-frame modulus (Eq. 29–30). So the wall is where the elliptic parameter equals its complement, m = 1 − m = ½. There K(m) = K(1 − m), and v31's spacing Δ* = 4πK(m)/K(1−m) equals **4π exactly**. The Ising parameter η_I = 2π (v31 Eq. 94).
- ξ_c = 1/ln(3+2√2) = 0.5673 cells.

In words: **the element paper's half-power wall is the offset paper's self-dual elliptic modulus.** On the dimerized line (t2/t1 = 3 + 2√2) the spacing 4π is a proved endpoint result (Eisler's quantization, [F5] in v31). Across the interior, v31 grades Eq. 92 as R+V, so measuring the interior wall points is a new out-of-sample test of that formula.

**Why the check proves it.** The algebraic equalities are evaluated at five points on the locus. The transfer matrix is built explicitly from the site equations, not taken from the formula. The spacing is then *measured* from finite even blocks: the central rungs ε_{k+2} − ε_k of the two interleaved cut towers. The kill condition was written before the run: a relative deviation from 4π above 10⁻⁶ at an interior wall point, while the reference control passes, would mean Eq. 92 fails there.

**Result** (OFFSET-LW-03, 160 digits):
- Algebra at t1 = 0.1716 (v = 0), 0.1787 (v = 0.2), 0.2161 (v = 0.5), 0.3542 (v = 1.0) and 1.0 (v = 2.0): every equality holds to 10⁻¹⁶⁰, with det M = 1.
- Positive control (0.6, 1, 0.4), L = 48: measured 8.13852480895 against Eq. 92 8.13852480895 (relative 6×10⁻¹⁵). v31's own table prints 8.138524807 measured.
- Dimerized wall point, L = 28: 12.5663706155 and 12.5663706132 (relative 9×10⁻¹¹; finite-size, shrinking with L).
- **Interior wall point v = 0.5, L = 28: 12.5663706144 (relative 1.3×10⁻¹⁹). Interior wall point v = 1.0: relative 1.1×10⁻¹⁹.** 4π = 12.5663706144.
- The kill condition was not met. Eq. 92 holds at the interior wall points.

### E9. The wall as the offset paper's exact census window

**Statement.** v31 Eq. 100 gives ε ≤ ν ≤ 1 − ε ⟺ |ε_i| ≤ ln[(1−ε)/ε]. At the floor ε = (2 − √2)/4 = 0.146447, (1 − ε)/ε = (2+√2)/(2−√2) = 3 + 2√2. So **the loop wall is the census window at floor (2−√2)/4.**

Equivalently, since ν(1 − ν) = (1 − Γ²)/4, the wall is ν(1 − ν) = 1/8: half the maximum single-level variance. "Half the power reflected" (element) is "half the maximum number fluctuation" (offset).

**Check** (OFFSET-LW-01 and -06):
- The script asserts, level by level, that the three forms of "inside" agree: |ε| < ln z_w, Γ² < ½ and ν(1 − ν) > 1/8.
- On the element archive, the 8 outside ordinary steps have ν(1−ν) between 0.0621 (lithium) and 0.1232 (caesium), all below 1/8.

### E10. Two faces and the connected regime

**Statement.** Put γ = |v|/Q and δ = |t1 − t2|/Q, with Q = √(Emin Emax). Then γ² + δ² = (v² + (t1−t2)²)/(Emin Emax) = Emin/Emax = k_e.
- The element paper's two-face closing test Γ₁² + Γ₂² < 1 (`MixedFaces.lean`) therefore becomes k_e < 1, which holds exactly when t1t2 > 0. That is the offset paper's connected regime (v31 Sec 3.1).
- Contact is t1t2 = 0: the decoupled chain, where finite blocks reach occupations 0 and 1 and the offset's strict domain (v31 Eq. 6, Theorem E1) fails.
- On the isospectral circle of v31 Eq. 46, γ = sin θ √k_e and δ = |cos θ| √k_e.
- The reference substrate (0.6, 1, 0.4) has mass angle 45°, so γ = δ: it is the Rice–Mele "equal-face" point, and 2γ² = k_e = 0.343 < 1.

**Grade:** EXACT algebra. Reading δ as the second face is my construction; δ is not an observable named in the offset paper. So the meaning is STRUCTURAL.

**Check** (OFFSET-LW-04): the sum minus k_e is ≤ 10⁻¹²¹ at five substrates. At t1 = 10⁻⁶ the sum approaches 1 (1 − sum = 1.7×10⁻⁶). The circle forms hold to 10⁻¹²¹.

### E11. The offset itself on and beyond the wall

**Statement.** τ∞ = 2 artanh γ ≥ ln(3+2√2) ⇔ γ² ≥ ½ ⇔ 2v² ≥ Emin Emax. Since γ² = k_e sin²θ ≤ k_e on its isospectral circle, being outside requires k_e > ½. At equal hopping γ² = k_e, so **γ² = ½ exactly at v = 2t/√3**, where the offset equals ln(3+2√2) = 1.7627471740.

**Why the check proves it.** v31 Theorem E7 proves the limit. Building the finite odd blocks shows the concrete substrate reaching the wall. The kill condition: |τ₂₁| differing from 2 artanh γ by more than 10⁻⁶.

**Result** (OFFSET-LW-04):

| Substrate | \|τ_L\| at L = 5, 9, 13, 17, 21 | Limit and gap |
|---|---|---|
| On the wall, v = 2/√3 | 1.76274182, 1.76274717363, 1.76274717403905, 1.76274717403909, 1.76274717403909 | τ∞ = 1.76274717403909; last − τ∞ = −3×10⁻²² |
| Beyond, v = 1.5 | → 2.06343706889556 | γ² = 0.6, outside; gap −3×10⁻²⁵ |
| Reference-like, v = 0.4 | → 0.9515411 | γ² = 0.196, inside |

So **a Rice–Mele chain can carry an offset exactly on the loop wall, and beyond it.** The paper's own reference substrate is inside (γ² = 0.1715).

### E12. The chemistry form of the boundary pair

**Statement.** The element paper's chemistry form is Γ₀ = (IE − EA)/(IE + EA) = η/χ, with ω/η = 1/(2Γ₀²), the wall at ω = η and ΔN_max = 1/Γ₀. The same algebra applied to the offset's boundary pair gives:
- a_N = ((s0 − s1)/2)/((s0 + s1)/2): a "hardness over electronegativity" of the added site's vacancy and occupation.
- "ω/η" = 1/(2a_N²), with the wall at 1.
- "ΔN_max" = coth(τ/2).

**Grade:** STRUCTURAL. The formula is identical, but the objects are not: probabilities of a Gaussian region against energy differences of an atom.

**Check** (OFFSET-LW-01, L = 17): s0 = 5.652×10⁻⁸, s1 = 2.342×10⁻⁸, (s0−s1)/(s0+s1) = 0.41412387656654931061 = tanh(τ/2). "ω/η" = 2.915, so the reference boundary is on the hard side of the wall.

### E13. The element "third reading" is the offset paper's projector metric

**Statement.** The element paper (README item 20, v8 Sec 7) writes the localization second moment as Var(X) = ½ Σ‖P_ij‖²(x_i − x_j)² with cell-centre positions. v31 uses the orbital-position-free Bloch gauge (Eq. 16). By Parseval,

  ½ Σ_R R²‖P(R)‖_F² = ½∫ dk/2π Tr(∂_kP ∂_kP) = ∫ dk/2π g^P_kk,

which is the integral of v31 Eq. 20's intrinsic metric, g^P = ¼|∂d̂|². This connects the element paper's "third reading" to the offset paper's projector geometry, and it stays inside his intrinsic metric: no spacetime metric enters.

**Why the check proves it.** The two sides are computed independently: real-space Fourier blocks from quadrature, against a k-space integral of the analytic derivative of d̂. Positive control: the half-filled one-band chain must reproduce the element paper's 8/π².

**Result** (OFFSET-LW-05): 0.228639254356804 against 0.228639254356805 (difference 10⁻¹⁵). Control: 0.81056946976 against 8/π² = 0.81056946914.

### E14. The remainder conjecture's step ratio is a returned power

**Statement.** v31 Conjecture E6's candidate is ρ = ((√(M+e) − √(2e))/(√(M+e) + √(2e)))² = Γ(w)², with w = √((Emax + Emin)/(2Emin)). The convergence factor per odd step is a returned power Γ².

**Check** (OFFSET-LW-07): all four printed ρ values are reproduced as Γ(w)² to every printed digit (0.005430335405, 0.02768429499, 0.2793728502, 0.5674378981). The near-critical row (1, 1, 0.02) has ρ = 0.567 > ½: its convergence step is "outside the wall".

Aside (algebra only): ρ = ½ exactly when (Emax + Emin)/(2Emin) = (3+2√2)² = 17 + 12√2, i.e. k_e = 0.014938. 17 + 12√2 is (1+√2)⁴, the Apéry rail of the ladder paper; that recognition comes from the ladder-paper record. The rewriting is exact. Whether the wall means anything for convergence is a LEAD (L5).

## 4. STRUCTURAL connections

**S1. The interior cancels; the boundary survives.**
- The offset's Theorem 8 cancels the complete-cell determinant and leaves the boundary pair s0/s1.
- In the element paper, the half-log rapidities of one atom telescope: Σ_k h_k = ½ ln(IE_last/IE_first). Checked to 9×10⁻¹⁶ over all 85 atoms (OFFSET-LW-06). That one is trivial; the offset version is not.
- The element paper keeps two kinds of jump apart: the peel jump inside the ball and the junction jump on the face. The offset paper keeps the block apart from the interface term Z_AB.
- Same shape, different objects.

**S2. Symmetry protection, and a lesson running back to the element paper.** Both zeros are z = 1 (E4), but they are protected differently.
- The element junction is transparent because two identical neighbours give equal clocks. That is a reflection across the junction, and for a ratio of two scalars reflection alone is enough.
- The offset paper shows that **reflection alone does not protect the log-odds**. Its mirror-symmetrised disorder gives 5.65 and 7.00, against 0.41 and −0.90 for the unsymmetrised control (v27 Sec 7; reported, not rerun here). The particle–hole part P of S = P∘R is needed, because the trace compares empty against full.
- If the element paper ever builds junction offsets from projector compressions rather than scalar clocks, the protecting operation has to carry the particle–hole exchange, not only the mirror.

**S3. Even and odd halves.**
- Offset: τ = −2F_odd. Every even term, including the Gaussian decay of the formation probabilities, cancels (v31 Theorem 4). There are two independent Z₂ labels: the signature η(K_A), fixed by the left cut, and sign τ, flipped by L mod 4. Both sit beside one continuous amplitude (v31 Sec 3.6).
- Element: Γ² and the wall classification are even under reversal; sign Γ is odd. The screw sign χ = (d₀×d₁)·d₂ is even under reversal and odd under mirror.
- The operation tables differ. In the offset, a one-site translation flips both labels and growth by a cell flips only the trace sign. In the element, reversal flips Γ only and mirror flips χ only.
- STRUCTURAL ("two labels, one amplitude"), not one formula.

**S4. Sum rules.**
- The element junction sum rule Σ_{j≠i}‖P_ij‖² = Tr(C_i − C_i²) is the per-site case of an exact region identity: Tr(C_A − C_A²) = Σ_{i∈A, j∉A}|P_ij|² = Σ_i ν_i(1 − ν_i) = Σ_i (1 − Γ_i²)/4.
- That is the region's number variance written as a cut-crossing sum: the even partner of the offset's odd log-odds. Compare the corpus bridge C_A − C_A² = BB† recorded on 16 September (census–Cayley bridge).
- Check (OFFSET-LW-05): site sums agree to 2×10⁻¹⁵. Region A = 17 sites: 0.600944885924559 against 0.600944885924552 against Σ(1−Γ²)/4 = 0.600944885924559.
- The identity is exact. Its role (zeroth moment in the element paper, even partner in the offset paper) is STRUCTURAL.

**S5. The gluing quantum is a reversed peel step.** With an even, protected partner (τ_B ≈ 0), Z_AB = τ_{A∪B} − τ_A takes one of three values:
- 0 when the two odd blocks carry the same sign: rapidities add, ratios multiply;
- ±2τ∞ when one is reversed. In peel terms, reversing one step costs 2h.

This reads v31's gluing table (Sec 10.2) through E3. It is exact given the paper's sign statements, and STRUCTURAL as a description.

**S6. Elimination.**
- The offset's Schur complement s1 = C_xx − c†C_B⁻¹c is a conditional occupation left on the kept site after eliminating the interior.
- The element paper's QUANTUM_CHEMISTRY_LINKS lists Löwdin partitioning and Feshbach projection as the established forms of its spinor-peel elimination. The recovered peel identity ι†A²ι − (ι†Aι)² = (QAι)†(QAι) is its compression defect.
- The shared lesson is stated in both. Offset Sec 6.5: dropping the outer levels changes the trace. CLAUDE_REVIEW: "Deleting a mode loses its phase; eliminating it properly keeps it."
- STRUCTURAL.

**S7. Kink charge and screw sign.**
- The offset's 2D staircase charge flips when the top-row displacement is reversed (∓0.364145 at width 8; v31 Sec 11.4).
- The element's screw sign flips under mirror; Γ flips under reversal.
- Which of the two (mirror type or reversal type) the kink flip is has not been decided. LEAD; the test is in Sec 6.

**S8. Shared method and instruments.** Both papers:
- write the kill condition before the run;
- carry a positive control beside every null (offset method note M08; element: 11 false controls);
- certify finite algebra in Lean with only propext, Classical.choice and Quot.sound, with deliberately false controls rejected;
- keep frozen predictions (element: the heavy-anion prediction written before the numbers; offset: gluing kill conditions);
- bracket thresholds by cutoff windows (element: the silver–silicon window; offset: the exact occupation cutoff and the Clausius ten-percent threshold);
- separate measured, derived and recognised in their grades.

## 5. LEADs (plausible, untested or underdefined)

- **L1. Element census with entropy weights.** Weight each peel step by the fermionic entropy s(ln z) of v31 Sec 7.9. Exploratory run (OFFSET-LW-06): the 8 outside steps carry 0.118% of the total weight, against 8/3570 = 0.224% by count. This is a number, not a finding. *Decisive test:* define the element-ladder "census coefficient" (steps inside a floor ℓ per unit ln Z, or per shell) and ask whether entropy weighting removes the shell structure the way it removes π² in the offset paper.
- **L2. A second cocycle (OP3) shaped as the Two Trees boost.** E7 shows that the matrix OP3 asks for has the shape of a peel boost with z = P_empty/P_full: trace 2 cosh τ, Lorentz entries from PeelTrees. The shape alone is trivial, since any matrix with eigenvalues e^{±τ} has it. v27 already killed every real-energy cell transfer matrix. *Decisive test:* find a boundary object whose transport matrix has rapidity τ and is selected without fitting. One example: the transfer of the Schur pair (s0, s1) under growth by one cell, which E14 says contracts with returned power ρ.
- **L3. Schottky and the cascade.** PeelTrees shows the Schottky threshold at Γ² = ½ for sample ratios (5 below, 7 above). Outside the wall the faces do not meet, and the generated group has no relation. The offset's cascade "does not compound". This is underdefined: offset boosts need axes before a ping-pong test means anything. *Test once defined:* two boundary boosts of rapidity τ∞ on the axes fixed by the two cuts; check freeness against γ² = ½.
- **L4. The bond face δ = |t1 − t2|/Q.** Is 2 artanh δ the large-block limit of some boundary log-odds, for example of a bond-centred cut or a dimer-occupation observable? If so, E10 becomes a statement about two observables, not one observable and one construction. *Decisive test:* compute candidate finite-block log-odds on the isospectral circle and compare with 2 artanh(|cos θ|√k_e).
- **L5. The wall on the convergence step.** ρ = Γ(w)² crosses ½ at k_e = 0.014938 (E14). *Test:* see whether the measured n(1 − |R_n/R_{n−1}|/ρ) behaviour or the precision cost changes character across ρ = ½ (between the (1, 1, 0.1) and (1, 1, 0.02) rows).
- **L6. The speed-limit dictionary.** The local notes `research/2026-11-13-space-step/T14_dirac_time/NOTES.md` give a single-level form of the companion "Offset Speed Limit" bound with the dictionary C = (1+G)/2 marked "UNTESTED". E2 supplies that dictionary exactly per level, with G = 2ν − 1 = −Γ. I did not read the companion paper, so its statement is untested here.

## 6. What was checked and set aside, and what was not found

- **Near-coincidence (reported, not a connection).** At the reference substrate:
  - γ = 0.4141239 against √2 − 1 = 0.4142136 (difference −9.0×10⁻⁵);
  - τ∞ = 0.881157 against ln(1+√2) = 0.881374 (difference −2.2×10⁻⁴);
  - e^{τ∞} = 2.41369 against 1 + √2 = √(3+2√2), the face apex of the wall;
  - χ = 44.991° against 45°.

  All four are one coincidence. At mass angle 45° γ² = k_e/2, so it reduces to k_e = 0.342997 against 2(3 − 2√2) = 0.343146. The substrate was chosen arbitrarily, and no test could promote this.
- **Spinor vocabulary.** The Rice–Mele chain is a two-component (sublattice) lattice spinor with mass v, and its intercept comes from a chiral zero mode. The element screening events need the electron's spinor (Dirac) structure (the α²Z⁴/8 term). These are different spinors and no formula is shared. Set aside.
- **Affine relation K_A = cT + bI.** No counterpart was found in the element paper.
- **Clausius region and the β·Δ against L/ξ law.** No counterpart was found.
- **Census coefficient A = 2c/π².** No element counterpart. Only the method (counting against a floor) carries over, as E9 and L1.
- **2D seams.** No element counterpart beyond S7.

## 7. The strongest connections, and the tests that would decide the leads

1. **E8: the loop wall is the self-dual modulus of the entanglement ladder.** The element paper's half-power condition Γ² = ½, applied to the Rice–Mele correlation rail, is k_e² = ½. That is t1² + t2² + v² = 6t1t2, a mid-gap transfer matrix of trace magnitude 6, and ladder spacing exactly 4π. On the dimerized line it is t2/t1 = 3 + 2√2, the element wall ratio itself. Measured: 4π to 10⁻¹⁹ at two interior points, which is also a new out-of-sample confirmation of v31's Eq. 92 there.
2. **E1 with E2: one Cayley map runs both papers.** The offset is the rapidity of P_empty/P_full, every entanglement level is a peel step, and the Hankel proof reads its ratio through Γ. Together with E5 and E6, every modulus of the offset paper (u, k_e, h, γ) is a peel reflection of a natural ratio of the chain. In the reference block exactly one level, the central rung, sits inside the wall, and it carries 72% of the entropy.
3. **E11: the offset itself can sit on the wall.** At equal hopping with v = 2t/√3, the proved endpoint is exactly ln(3+2√2), and finite blocks converge to it to 10⁻²². This gives the element paper's wall a concrete place on the offset paper's substrate.

The tests that would decide the leads are given with each LEAD in Sec 5. The most informative is **L4**: find, or fail to find, a boundary observable whose limit is 2 artanh δ. That decides whether E10 reflects physics or bookkeeping. **S7** needs one run: apply the x-mirror (composed with the sublattice exchange the coupled-row model needs) to the width-8 staircase and see whether the sign flip is mirror-type or reversal-type.

## 8. Check scripts (each has `# SCRIPT: NAME` at the top; outputs saved beside them)

All are in `/home/claude/connections/checks_offset/`:
- `offset_lw_01_rapidity.py` (OFFSET-LW-01): E1, E2, E3, E4, E7, E12 and the near-coincidence.
- `offset_lw_02_moduli.py` (OFFSET-LW-02): E5 and E6, against v31's printed "Matched h" column.
- `offset_lw_03_wall_on_rice_mele.py` (OFFSET-LW-03): E8, with the measured spacing and kill condition.
- `offset_lw_04_faces_and_offset_wall.py` (OFFSET-LW-04): E10 and E11.
- `offset_lw_05_sum_rule_metric.py` (OFFSET-LW-05): S4 and E13, with the 8/π² control.
- `offset_lw_06_archive_census.py` (OFFSET-LW-06): reproduces 3,570 ordinary steps and 8 outside from `data/element_thresholds_20261011.json.gz`; also E9 and S1 on the archive, and L1.
- `offset_lw_07_hankel_and_remainder.py` (OFFSET-LW-07): E1b and E14, against v31's printed ρ values.

Each `*_output.txt` holds the verbatim run output. All scripts use mpmath 1.3.0 and numpy and need no repository checkout. OFFSET-LW-06 takes the archive path as an argument.

## 9. Sources read

| Source | Version | Read |
|---|---|---|
| `the_offset_belongs_to_the_boundary_v31.pdf` (Drive id 1m6BQbDAK7h1FjPeLWYSf_w0IoAEKS5ut, current-papers folder; Zenodo 22555919) | v31, 6 Sep 2026, 92 pp | **In full** (text via pdftotext) |
| `the_offset_belongs_to_the_boundary_v27_submission.pdf` (Drive id 1M28nG4RnVuHjZPWUArkGEQcWQ94ViLoB) | v27, 60 pp | **In full** |
| `CURRENT_PAPERS_20261013.md` (Drive) | 13 Oct 2026 | In full (to confirm v31 is the Zenodo version) |
| v14–v26, v28–v30 of the offset paper (Drive) | various | Not read; listed by title only |
| Element paper `README.md`, `QUANTUM_CHEMISTRY_LINKS.md`, `CLAUDE_REVIEW.md`, `REVIEW_GUIDE_20261121.md`, `SECOND_HOUR_20261121.md` | branch `element-paper/loop-wall`, 21 Nov 2026 | In full |
| `lean/LoopWall.lean` | 140 theorems | All statements read; proofs skimmed |
| `VOTKP_Element_Paper_Loop_Wall_v8_20261121.html` | v8 | Text in full (figures not inspected) |
| `two-trees/lean/PeelTrees.lean` | repo copy | Header and the Schottky and boost lemmas only |
| `data/element_thresholds_20261011.json.gz` | archive | Read by script (Z = 1–85) |
| `paper/votkp_v3_2/code/atlas_map/CARD_INDEX.md`, `research/2026-11-11-standard-model-ball/atlas/ATLAS_B97_B207_READ_20261111_v1.md` | local | Lines on cards B150–B153, B176, B191, B204–B207 only |
| `research/2026-11-13-space-step/T14_dirac_time/NOTES.md` | local | Offset-related lines only |
| GitHub dicipler-pixel | — | Only `votkp-lean` (local clone) is available in this session. The operator-first repository holding `OperatorFirst.Offset*.lean` is not attached and was not fetched. The Lean catalogue printed in v31 Appendix A was used instead. |
