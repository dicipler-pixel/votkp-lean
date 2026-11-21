# What Transport Keeps and The Loop Wall: the connection map

Jeromie Beasley's papers *What Transport Keeps* (research edition 3, 6 September 2026) and *The Loop Wall: Peeling the Elements from Hydrogen to Astatine* (element paper, page v8, 21 November 2026). Mapped 21 November 2026. Element names and "crossing number" are written in full.

## 0. Finding the paper

- **Title.** The paper is *What Transport Keeps: Projector selection, conserved pairings, and spectral geometry after the Ramanujan Challenge*, follow-up research edition 3, 6 September 2026, 22 pages. Zenodo version DOI 10.5281/zenodo.22543487 (all versions 10.5281/zenodo.22543486).
- **Newest version.** Edition 3 is the newest text. The GitHub companion `dicipler-pixel/what-transport-keeps-lean` (last commit 7 October 2026) names edition 3 as the Zenodo version in its `PROVENANCE.md` and gives the checksums of the Zenodo files. The newest Drive copy, `What_Transport_Keeps(2).pdf` (in the current-papers folder, modified 11 October 2026), carries a creation date of 6 September 2026 and reads "Follow-up research edition 3". `What_Transport_Keeps (3).html` (the Zenodo HTML) has the same text.
- **Not papers.** Drive also holds "What the Transport Keeps" films and a song (2 to 3 November 2026). These are not paper versions and were not used.
- **Where I searched.**
  - Drive: title and full-text searches for "transport keeps", "Transport_Keeps" and "Keeps". No copy sits in "nov 26 updates" or "oct 26 updates". The copies are in the current-papers folder and in older folders.
  - GitHub: `gh search code` is blocked in this session (GraphQL and global search are refused). `list_repos` found `what-transport-keeps-lean`, which I cloned read-only. The local `votkp-lean` repo has three files that mention the paper.
  - Zenodo: the API was refused by the session proxy, so the Zenodo record could not be opened directly.
- **Local copies.** Downloaded to `/home/claude/connections/src_transport/` and text-extracted with pdftotext.

## 1. The two papers in one paragraph each

**What Transport Keeps.** Transport, selection, pairing and readout are separate questions about one construction.
- A trace-normalised Gram matrix H_N = B_N* B_N / Tr picks a line when its limit has a gap: 1 − Tr(Q_N Q) ≤ 2η_N/δ (Theorems 1 and 2).
- Tied growth has three outcomes: a fixed line, a rotating line, or an unresolved block.
- A dual pairing ℓᵀx is conserved under x → Ax, ℓ → A⁻ᵀℓ, and a readout error bound separates selection error from readout sensitivity (Theorem 3).
- A coboundary keeps the pairing but not an untransformed Euclidean metric (Theorem 4).
- Catalan calibration: the exact cancellation A U₀⁻ᵀ f = 450√π (G, 1), and the rail λ± = 17 ± 12√2 = sec ψ ± tan ψ.
- A discrete plaquette identity sits beside a nonzero eigenline curvature F_b with Σ_b F_b = 0 (Theorem 6), plus exact band asymptotics (Theorem 6a).
- Rank-one stress S = 1 − |u*v|², with κ = 1/|v*u| and S = 1 − κ⁻² (Proposition 7).
- Projective distance ‖P_v − P_w‖²_F = 2 sin²θ and the capacity census (Proposition 8).
- Fixed levels with a moving projector: metric 1/4, transition strength d² sin²ϑ (Proposition 9).
- Boundary elimination K_Σ = D_Σ − CA⁻¹B − GE⁻¹F and its sensitivity (Proposition 10).
- Catalan as a rail integral, G = ½∫₀^{π/2} log λ₊(ψ) dψ (Proposition 11).
- The grade legend is [T] [V] [C] [D] [H].

**The Loop Wall.**
- Peel ratio z = IE_{k+1}/IE_k, reflection Γ = (z − 1)/(z + 1) = tanh h, h = ½ ln z.
- The loop wall is Γ² = ½, that is z = 3 + 2√2. Two faces close the loop iff sinh h_a sinh h_b < 1, iff Γ₁² + Γ₂² < 1.
- Reversal sends Γ to −Γ and keeps Γ². Among ordinary steps, only first core openings are outside.
- At the anion rung, Γ₀ = η/χ and the wall is ω = η.
- Junction sum rule Σ_{j≠i}‖P_ij‖² = Tr(C_i − C_i²). Localization second moment ½Σ‖P_ij‖²(x_i − x_j)².
- Screw sign χ = (d₀×d₁)·d₂, even under reversal and odd under a mirror.
- Three-mode loop: identical spectra at ±Φ with opposite circulation.
- 257 Lean theorems.
- Earlier work: the VOTKP v3.2 loop results (trace 2 − 4 sinh⁴(r/2), Petermann factor K = 1/(1 − 2Γ²)) and Two Trees (Schottky above Γ² = ½).

## 2. The loop as a transport (used throughout)

The element paper's loop is two perpendicular half-steps. In the 2×2 transports of determinant one:
- A = diag(e^{h_a}, e^{−h_a}). Its axis is the imaginary axis of the upper half-plane.
- B = [[cosh h_b, sinh h_b], [sinh h_b, cosh h_b]]. Its axis is the unit semicircle, which meets the first axis at right angles at the corner i.
- The loop holonomy is the group commutator W = A B A⁻¹ B⁻¹.

This is a WTK transport in WTK's own sense: a product of invertible steps, read through the fixed Euclidean instrument of WTK assumption A1. Every check below uses this one construction, which is built in `check_loop_selection_v1.py`. It is a frame choice: the instrument sits at the loop's corner. Where a result depends on that choice, it is flagged.

## 3. Every connection, graded

Grades: **EXACT** means the same formula, shown by algebra (and checked). **STRUCTURAL** means the same shape on different objects, flagged. **LEAD** means plausible and untested.

| # | Connection | Grade |
|---|---|---|
| 1 | Loop-wall polynomial = parabolic boundary of the loop holonomy; tr W = 2 − 4 sinh²h_a sinh²h_b | EXACT |
| 2 | Loop wall = where WTK's line selection (Theorems 1 and 2, the three tied outcomes) switches on for the loop | EXACT (numerically demonstrated; the mechanism is algebra) |
| 3 | WTK rank-one stress of the loop: S = Γ_a² + Γ_b², κ² = 1/(1 − Γ_a² − Γ_b²) = cosh² d | EXACT in the corner frame; frame-dependent by WTK's own Theorem 4 |
| 4 | Per face, WTK stress S = Γ², κ = cosh h; WTK tensor law versus the loop's additive closing sum | EXACT (face); STRUCTURAL (the composition laws differ) |
| 5 | Two Trees: Schottky above the wall = every word transport selects a line | STRUCTURAL, finite evidence (all words to length 10); full proof is the ping-pong argument |
| 6 | Rail: Γ = tan(ψ/2); the wall sits at sec ψ = 3 (cos ψ = 1/3); Catalan's rail root is (3 + 2√2)² | EXACT |
| 7 | WTK Proposition 11 rewritten in Γ: G = ∫₀¹ 2 artanh Γ/(1 + Γ²) dΓ | EXACT (change of variable, checked to 40 digits) |
| 8 | Second rail map: loop holonomy eigenvalues −λ±, sec ψ_W = 2 sinh⁴h − 1; rail starts at the wall; sec ψ_W = 17 at Γ² = 3/4 | EXACT algebra; the Catalan coincidence is a LEAD |
| 9 | Localization second moment = WTK projector metric ½Tr[(∂P)²] along the position twist = small-s WTK distance | EXACT (orthogonal projectors only, WTK A5) |
| 10 | Junction (delocalization-index) sum rule versus WTK Theorem 6 curvature sum rule | STRUCTURAL (same method, different sums) |
| 11 | Γ² = ½‖P_fwd − P_rev‖²_F (forward and reversed peel lines); the wall is WTK separation ε = ½, capacity 4 | EXACT formula; the encoding is STRUCTURAL |
| 12 | WTK Proposition 9 two-level: R = cos²ϑ, T = sin²ϑ = transition strength; the wall at ϑ = π/4 | STRUCTURAL (Γ = cos ϑ is an identification) |
| 13 | WTK Theorem 3 readout bound applied to Γ₀ = η/χ: fixes the silicon and silver calls | EXACT application |
| 14 | WTK Theorem 4 coboundary: a peel ladder telescopes, Σh_k = ½ ln(IE_last/IE_first) | EXACT (one-line algebra, checked on data) |
| 15 | WTK "curvature needs two parameters" ↔ the loop needs two faces; WTK flat plaquette versus the non-flat loop commutator | STRUCTURAL |
| 16 | Three-mode loop elimination = WTK Proposition 10 (Schur boundary reduction and sensitivity) | EXACT |
| 17 | Same energies, opposite circulation ↔ WTK "fixed levels, changing response"; curvature odd in Φ | EXACT (after a repair); STRUCTURAL as a principle |
| 18 | WTK conserved pairing in two dimensions = oriented area; the screw sign χ is an oriented volume | STRUCTURAL (mirror-odd alike; respond differently to reversal) |
| 19 | Memory and record: "what survives / what is distinguishable / what the readout retains" ↔ Γ² kept, sign of Γ is the direction record | STRUCTURAL |
| 20 | Junction "belongs on the face" and the 98% closure ↔ WTK Proposition 10 "the interface retains loading from both sides" | LEAD |
| 21 | Γ-coordinate as the physical measure WTK leaves open in Proposition 11 [H]; split of G at the wall | LEAD |
| 22 | Berry-type curvature (time-odd, orientation-odd) versus Γ (reversal-odd) and χ (mirror-odd): a third parity class | LEAD |
| 23 | Selection speed near the wall ∝ arcosh(sec ψ_W) (slow selection near the wall) | LEAD |
| 24 | Shared methods: exact rational certificates without irrationals; interval corner proofs; Lean with false controls; evidence-grade legends | STRUCTURAL (method) |

## 4. The connections in detail

### 4.1 The loop wall is the parabolic boundary of the loop holonomy (EXACT)

**Why the check proves it.** If tr W − (2 − 4 sinh²h_a sinh²h_b) reduces to zero symbolically, then three things follow at once:
- |tr W| < 2 (elliptic, a turn) is exactly sinh h_a sinh h_b < 1, the element paper's two-face closing condition.
- tr W = −2 (parabolic, a Jordan block) is the border.
- For equal faces, substituting sinh²h = (z − 1)²/(4z) must factor out z² − 6z + 1, the Lean polynomial of `wall_quadratic`.

**Result** (`check_loop_selection_v1.py`):
- The difference is 0.
- For equal faces, tr W + 2 has numerator −(z + 1)²(z² − 6z + 1).
- So tr W = −2 exactly at z = 3 + 2√2 = 5.828427125.
- The sign of Γ₁² + Γ₂² − 1 agrees with the sign of |tr W| − 2 on carbon with nitrogen (+0.003093 against +0.049836), on sodium with magnesium, and on 2,000 random face pairs (0 disagreements).
- In Γ, tr W = −2(Γ_a²Γ_b² + Γ_a² + Γ_b² − 1)/((1 − Γ_a²)(1 − Γ_b²)) (sympy).

This is the Lambert-quadrilateral statement written as a transport. The trace formula is the classical Fricke commutator-trace identity, so the algebra is standard; the use is his.

### 4.2 The wall is where WTK's selection switches on (EXACT; numerically demonstrated)

**Why the check proves it.** WTK's diagnostic is H_N = (W^N)*(W^N)/Tr. Its top line either converges or it does not. WTK names three tied outcomes. If 1 − Tr(Q_N Q_{N+1}) behaves as follows, the wall is WTK's selection threshold for the loop:
- inside the wall, it stays order one forever;
- at the wall, it falls polynomially;
- outside, it falls exponentially.

Also, WTK Theorem 2 says the selected right line must be the dominant left eigenvector read as a column (the seed covector a*).

**Result:**

| Faces | Γ₁² + Γ₂² | tr W | 1 − Tr(Q_N Q_{N+1}) |
|---|---|---|---|
| nitrogen's helium-core opening ratio on both | 0.976587 | −1.642 (turn) | still 0.578 at N ≥ 300: no line |
| the wall itself | 1 | −2.000000000 | 1.3e−6 (N = 10) → 6.1e−13 (N = 399), about N⁻⁴ |
| carbon's on both | 1.029600 | −2.503 (run) | machine zero by N = 50 |
| carbon's with nitrogen's (mixed) | 1.003093 | −2.050 (run) | machine zero by N = 50 |

- **Theorem 2.** 1 − Tr(Q₆₀ aaᵀ) = 0 to rounding in both outside cases.
- **Which inside outcome.** Inside, W is far from orthogonal in this frame (‖WWᵀ − I‖ = 55.3). So the inside outcome is WTK's rotating line (control 2), not the unresolved block (control 3). The unresolved block would need an orthogonal W, which happens only if the instrument sits at the turn's fixed point (see 4.3).

**Reading.** In WTK's words, outside the wall the loop is a transport that forgets every direction but one. Inside, it keeps turning and selects nothing. At the wall, it selects slowly through a Jordan block. Carbon with nitrogen is "open" in the element paper, and it is a WTK-selecting transport here, only just.

### 4.3 The loop's WTK stress is the closing sum (EXACT in the corner frame)

**Why the check proves it.** Inside the wall, W has complex eigenvalues. Each spectral idempotent is the rank-one Π = r lᵀ/(lᵀr). WTK Proposition 7 gives κ = ‖Π‖ = ‖l‖‖r‖/|lᵀr| and S = 1 − κ⁻². Sympy simplifies κ²(1 − Γ_a² − Γ_b²) to exactly 1, which proves:
- S = Γ_a² + Γ_b²;
- equal faces give S = 2Γ², κ² = 1/(1 − 2Γ²), the VOTKP v3.2 Petermann factor;
- the wall is where κ diverges. WTK says it plainly: "at zero overlap this idempotent is undefined".

**Result** (`check_loop_petermann_stress_v1.py`):
- Symbolic product: 1.
- Numeric κ² against 1/(1 − Γ₁² − Γ₂²), equal to nine digits:
  - nitrogen's ratio on both faces: 42.711281022 both ways;
  - potassium with calcium (argon-core openings): 26.439625341 both ways;
  - rubidium with strontium (krypton-core openings): 8.973682239 both ways;
  - z = 3: 2; z = 5: 9.
- Frame check (WTK A1 and Theorem 4):
  - rotating the frame leaves κ² = 42.711281022;
  - a non-orthogonal boost of the frame gives 113.53.
- So the identity holds in the frame whose instrument sits at the loop's corner. Geometrically, κ² = cosh² d(corner, fixed point of W). This was checked on four cases, all to nine digits, and matches VOTKP's "cosh² of the centre's distance".

**Two consequences.**
- The 12 November atlas reader marked "S of the loop equals 2Γ²" as "the reader's identification, untested" (card B148). It is now tested, with the frame named.
- WTK's warning that stress is not invariant under a non-orthogonal gauge becomes concrete here: the WTK instrument is a point of the hyperbolic plane.

### 4.4 Per face: WTK stress S = Γ², and the composition laws differ (EXACT, then STRUCTURAL)

**Why the check proves it.** Take the face's Minkowski-dual pair u = (cosh(h/2), sinh(h/2)), v = (cosh(h/2), −sinh(h/2)). Their normalised overlap is sech h, so WTK's S = tanh²h = Γ² and κ = cosh h. WTK's tensor law 1 − S(a⊗b) = (1 − S_a)(1 − S_b) must then hold.

**Result:**
- Carbon's face: S = Γ² = 0.514799846667, κ = cosh h = 1.435620116708.
- Nitrogen's face: S = Γ² = 0.488293490899.
- Tensor law: 0.248280076677 both ways.
- But the loop's closing quantity is S_a + S_b = 1.003093 (additive), not WTK's tensor stress 0.751720.

**Grade.** The face identity is EXACT. The two composition rules are different shapes: WTK multiplies "misses" under a tensor product, while the loop adds stresses under a commutator. STRUCTURAL, and worth saying so.

### 4.5 Two Trees, read backwards through WTK (STRUCTURAL; finite evidence)

**Why the check proves it.** A word's powers have a WTK-selected line iff the word is hyperbolic. I enumerated every reduced word up to length 10 (118,096 words). The expected pattern:
- zero elliptic words outside the wall and some inside;
- outside, the smallest margin should belong to the commutator.

If that pattern appears, the wall is the selection threshold for the whole two-step transport, as Two Trees' Schottky statement implies.

**Result** (`check_schottky_words_v1.py`):
- Nitrogen's faces: 240 elliptic words.
- At the wall: 0 elliptic words; the smallest margin is −2.3e−13, on a conjugate of the commutator (parabolic).
- Carbon's faces: 0 elliptic words; the smallest margin is 0.503, at BBBBAbabbb, a conjugate of the commutator (compare tr W = −2.503 in 4.2).
- Finite length is evidence only. The proof for all lengths is the ping-pong argument: circles of radius 1/sinh h are disjoint iff sinh h ≥ 1.

**Prior art.** Dominated splittings of 2×2 products is the general theory here. A search turned up "Geometric conditions for matrix domination in two dimensions" ([arXiv 1907.00347](https://arxiv.org/html/1907.00347v2)). I did not read it.

### 4.6 The rail: Γ = tan(ψ/2), and the wall sits at sec ψ = 3 (EXACT)

**Why the check proves it.** Put a step ratio on WTK's rail, λ₊ = z = sec ψ + tan ψ. With T = tan(ψ/2), sympy reduces (λ₊ − 1)/(λ₊ + 1) − T to 0. So the peel reflection is tan of half the rail angle, and the rail angle is the Gudermannian of the full rapidity r = ln z. Then:
- Γ² = ½ gives sec ψ = (1 + Γ²)/(1 − Γ²) = 3;
- λ± = 3 ± 2√2, the wall and its reverse branch;
- (3 + 2√2)² = 17 + 12√2, the Catalan rail root.

**Result** (`check_rail_reflection_v1.py`):
- The difference is 0.
- sec ψ = 3 at the wall, ψ = arccos(1/3) = 70.5287793655°.
- (3 + 2√2)² = (1 + √2)⁴ = 17 + 12√2.
- Γ of the Catalan root = 2√2/3 = tanh(2h*), where h* = arsinh 1 is the wall half-step.

**Meaning.** The Catalan rail's rapidity is exactly twice the wall's rapidity, which is four wall half-steps. Atlas card B149 had noted the shared unit 1 + √2 as "an arithmetic coincidence". The identity Γ = tan(ψ/2) is what makes it a single coordinate rather than a coincidence. Like WTK, I make no claim that this identifies Catalan's constant with anything physical.

### 4.7 WTK Proposition 11 written in Γ (EXACT)

**Why the check proves it.** Substitute ψ = 2 arctan Γ and log λ₊ = 2 artanh Γ into WTK's G = ½∫₀^{π/2} log λ₊ dψ. This gives G = ∫₀¹ 2 artanh Γ/(1 + Γ²) dΓ. The substitution is exact. Quadrature confirms it.

**Result:** 0.9159655941772190150546035149323841107741 against Catalan's constant; difference 0 at 45 digits. The integrand is the peel half-step artanh Γ weighted by dψ/dΓ. The search for prior art on this specific form was inconclusive; it is a direct change of variable of a classical integral.

### 4.8 A second rail map, from the loop holonomy (EXACT algebra; LEAD coincidence)

**The algebra.** Outside the wall, W has eigenvalues −λ±, with λ₊λ₋ = 1 and λ₊ + λ₋ = 4 sinh⁴h − 2. So sec ψ_W = 2 sinh⁴h − 1.
- The rail begins (ψ_W = 0) exactly at the wall.
- sec ψ_W = 17 needs sinh²h = 3, that is Γ² = 3/4 and z = 7 + 4√3.

**Flags.**
- The eigenvalues are negative: the loop runs with a half-turn.
- The two rail maps (4.6 and this one) are different and must not be mixed.
- The Γ² = 3/4 match is a LEAD, with no meaning claimed.

### 4.9 The localization second moment is WTK's projector metric (EXACT, orthogonal projectors)

**Why the check proves it.** For an orthogonal projector P and position X constant on sites, take P(s) = e^{−isX} P e^{isX}. Then ∂P = −i[X, P]. The algebra gives:
- ½Tr[(∂P)²] = Tr(PX(1 − P)X) = ½Σ‖P_ij‖²(x_i − x_j)²;
- this is the s → 0 limit of WTK §6's distance ½‖P(s) − P‖²_F divided by s².

**Result** (`check_localization_metric_v1.py`; a random rank-5 projector on 6 sites with 2 orbitals each):
- Commutator form, Tr(PX(1 − P)X) and the site sum all equal 17.421346791144.
- A finite-difference derivative gives 17.421346775967.
- The WTK distance at s = 10⁻³ gives 17.4213088.
- The junction sum rule error is 2.8e−16.

**Negative control** (an oblique idempotent, WTK A5):
- the commutator and trace forms still agree (22.2914);
- the site-weight form gives 233.36.

So the element paper's identity is tied to Hermitian P, which is what WTK A5 says about the positive metric.

**What this joins.** The element paper's "third reading" is the WTK/IQGT metric of the occupied projector along a position twist. The element paper already records that the computed number is the cell-centre projection on its partition. That flag stays.

### 4.10 Two sum rules (STRUCTURAL)

- **Element paper.** The junction sum rule comes from P² = P: Σ_j P_ij P_ji minus the self-term.
- **WTK.** Theorem 6's Σ_b F_b = 0 comes from inserting a complete eigenbasis and cancelling antisymmetric pairs.
- **Grade.** Same method (insert completeness, drop the diagonal) on different sums: a budget against an antisymmetric cancellation. Both are checked to machine precision in the scripts (2.8e−16 and 0.0).

### 4.11 Γ² as a WTK projective distance (EXACT formula, STRUCTURAL encoding)

**Why the check proves it.** Encode a peel a → b as the line through (√b, √a), and its reverse as the line through (√a, √b). Sympy gives ½‖P_fwd − P_rev‖²_F = ((a − b)/(a + b))² = Γ². So the returned power is WTK's projective separation sin²θ between a peel and its reverse. The wall Γ² = ½ is the separation ε = ½ at which WTK's real projective line holds exactly 4 lines (computed: ⌊π/arcsin√½⌋ = 4).

**Result:**
- Silicon's anion rung has separation 0.50230 (above ½, outside).
- Silver's has 0.49875 (below, inside).
- The WTK distance is symmetric, so it cannot see the sign of Γ. The sign is the orientation of the turn from one line to the other. This matches the element paper's even and odd halves.
- The square-root encoding is a choice, hence STRUCTURAL in meaning.

### 4.12 WTK Proposition 9 as the reflect/transmit split (STRUCTURAL)

**Why the check proves it.** In WTK's two-level model the ground-state diagonal weight is ⟨g|D|g⟩²/d² = cos²ϑ, the transition weight is |⟨e|D|g⟩|²/d² = sin²ϑ, and they sum to 1. If Γ = cos ϑ, these are R = Γ² and T = 1 − Γ², and the wall R = T falls at ϑ = π/4.

**Result:**
- At ϑ = 45°: 0.5 against 0.5.
- Silicon's Γ₀ (ϑ = 44.868°) gives R > T, outside.
- Silver's (ϑ = 45.072°) gives R < T, inside.
- The identification Γ = cos ϑ is mine, not WTK's or the element paper's.

### 4.13 WTK's readout bound fixes the closest anion calls (EXACT application)

**Why the check proves it.** Γ₀ = (IE − EA)/(IE + EA) is a WTK readout: p = (1, −1), q = (1, 1), x = (IE, EA). WTK Theorem 3 gives a guaranteed worst case for any input error r. If that bound is smaller than the distance to the wall, no point of the uncertainty box can flip the call.

**Result** (`check_readout_bound_v1.py`):
- Silicon: distance 1.626e−3, WTK bound 5.45e−6 (exact corner excursion 1.04e−6).
- Silver: distance 8.83e−4, bound 6.24e−6 (corners 4.67e−6).
- Both calls are fixed by WTK's bound alone.
- In WTK's terms, the denominator qx = IE + EA = 2χ is large, so Γ₀ = η/χ is a well-conditioned instrument. This uses the archive ionization uncertainties and the electron-affinity uncertainties encoded in the element folder (silicon 0.0000007 eV, silver 0.00002 eV).

### 4.14 A peel ladder is a coboundary (EXACT)

- z_k = U(k + 1)/U(k) with U = IE. By WTK Theorem 4 the cumulative half-step depends only on the endpoints.
- Checked on archive ladders: carbon (5 steps), iron (25) and caesium (54) all match ½ ln(IE_last/IE_first) to 12 digits.
- This is trivial algebra, but it explains 4.15.

### 4.15 Curvature needs two directions (STRUCTURAL)

- **WTK:** "A varying frame along a single path does not require nonzero curvature. Curvature is tested by a two-parameter connection."
- **Element paper:** a single peel ladder is a coboundary (4.14), so it carries no holonomy. The loop needs two faces, and its holonomy tr W ≠ 2 is the curvature.
- **Contrast with WTK's own field.** WTK's Catalan field is flat as a plaquette (L(n+1,k)T(n,k) = T(n,k−1)L(n,k)) yet has nonzero spectral curvature. The loop is the opposite case: a non-commuting pair whose commutator is not the identity.
- **Grade.** Same principle on different objects.

### 4.16 The three-mode loop elimination is WTK Proposition 10 (EXACT)

**Why the check proves it.** Eliminate mode 3 as WTK's exterior block, with E = (0 − λ) and D = H₁₂ − λ. If all of the following hold, the recovered spinor-peel elimination is WTK's boundary reduction with WTK's sensitivity formula:
- det K(λ) vanishes at every true eigenvalue;
- the reduced link equals J + J²e^{−iΦ}/λ and the diagonal shift equals J²/λ;
- a finite-difference dK/dλ equals WTK's −I − GF/λ².

**Result** (`check_three_mode_schur_curvature_v1.py`):
- det K is 7e−16, 4e−16 and 1e−15 at the three eigenvalues.
- The link and the shift match to 10 digits.
- The sensitivity residual is 1.8e−10.
- Atlas card B48 already lists WTK Proposition 10 as the Schur seam. This check ties it to the element paper's loop.

### 4.17 Same energies, opposite circulation (EXACT after a repair; STRUCTURAL as a principle)

**Kill condition, written before the run.** The WTK Theorem 6 curvature must flip sign under Φ → −Φ while the spectra agree.

**First result.** In the parameter plane (Φ, ε) it did **not** flip. The values were identical at ±Φ (for example, band 1 gave −0.13755 at both). The reason: reversing Φ both conjugates H and reverses one parameter axis, and the two signs cancel. The claim was wrong for that plane.

**Repair.** Use the real plane of two on-site energies (ε₁, ε₂) at fixed flux. There H(−Φ) = conj H(+Φ) on the same axes.
- Result: F_b(+Φ) = (−0.2333, +0.2208, +0.0125) and F_b(−Φ) = (+0.2333, −0.2208, −0.0125).
- The sum is 0 in both cases, the spectra are equal, and |F(+Φ) + F(−Φ)| ≤ 2.5e−18.
- The sum-over-states formula also matched the projector formula Tr(P[∂P, ∂P]) by finite differences.
- Deletion control: dropping mode 3 removes Φ, so F = 0 identically.

**Reading.** This is WTK's opening sentence ("an electronic system can keep its energy levels and change how it responds") realised by the element paper's loop. The curvature is a direction record invisible to the energy ledger: odd like the sign of Γ, while the spectrum is even like Γ².

### 4.18 Oriented area and screw sign (STRUCTURAL)

**Why the check proves it.** For determinant-one steps, sympy gives A⁻ᵀ = JAJ⁻¹. So WTK's dual covector is J times a transported vector, and the conserved pairing is the oriented area det[x, y]. The area is conserved under transport (checked: −0.090251243478 before and after). It flips under a mirror and under swapping the pair.

The screw sign χ is an oriented volume det[d₀, d₁, d₂]. On a helix: +3.1177 forward, +3.1177 for the reversed path, −3.1177 mirrored.

**Grade.** Same kind of object (mirror-odd oriented measure), but different behaviour under reversal. STRUCTURAL only.

### 4.19 Memory and record (STRUCTURAL)

- **WTK's conclusion:** "The rail describes a growth scale. The projector describes what remains distinguishable. The pairing describes what a readout can retain."
- **The element paper:**
  - the ratio z is the growth scale;
  - Γ² and the wall call are what remains distinguishable;
  - the sign of Γ is the record a Γ²-only ledger forgets.
- **The Dirac Time notes** (`research/2026-11-13-space-step/T14_dirac_time/NOTES.md`) already place "What Transport Keeps" as §3 and gloss it as close to the loop's "every direction drawn onto one fixed direction". Section 4.2 makes that gloss exact for the loop holonomy outside the wall.

### 4.20 to 4.23 Leads, with the test that would decide each

- **4.20 Junction on the face (LEAD).**
  - Moving the peel ratio from the faces into the ball closes about 98% of the sodium-against-argon gap. WTK Proposition 10 says a boundary operator must carry loading from both sides.
  - **Test:** build the hydrogen-cell junction as an explicit three-block operator (interior atom, seam, exterior atom). Compute K_Σ = D_Σ − CA⁻¹B − GE⁻¹F. Check whether the matched-junction rule (Γ = 0 for equal clocks) and the 98% closure come out of K_Σ without the hand placement.
- **4.21 The measure (LEAD).**
  - WTK leaves open, as [H], which physical coupling fixes the weight in its rail integral. In Γ the weight is 2/(1 + Γ²) = dψ/dΓ.
  - The integral splits at the wall into 0.445424765 inside and 0.470540829 outside (0.4863 of G inside). No meaning is claimed.
  - **Test:** derive a weight from a coupling in the element data (for example, a transmission T = 1 − Γ² per face) and see whether it reproduces 2/(1 + Γ²) without being chosen to.
- **4.22 A third parity class (LEAD).**
  - Γ is reversal-odd and mirror-even. χ is mirror-odd and reversal-even. The WTK curvature is time-odd (4.17) and odd under swapping its two parameter axes.
  - **Test:** find an operation on peel data that acts as complex conjugation. Then check whether Γ's sign and the curvature's sign flip together.
- **4.23 Selection speed (LEAD).**
  - Outside the wall, WTK's selection error decays like (λ₋/λ₊)^{2N} = e^{−4N arcosh(sec ψ_W)}, which slows to polynomial at the wall.
  - **Test:** measure the decay rate on the archive's core-opening pairs and compare it with 4 arcosh(2 sinh²h_a sinh²h_b − 1).

### 4.24 Shared methods (STRUCTURAL, method)

- **Exact arithmetic without irrational constants.** WTK keeps G and log 2 as free symbols; LoopWall writes the wall as z > 3 ∧ (z − 3)² > 8, with no √2.
- **Exact interval enclosures** with matching endpoint signs. WTK Appendix C uses 84 enclosures of qG − p; the element paper uses the corner test 2(b − a)² against (a + b)².
- **Lean audits with false controls.** WTK's companion repo: 49 theorems and 2 false controls ("45 (G, 1)", roots multiplying to 2). The element paper: 257 theorems and 11 controls.
- **Evidence-grade legends.** WTK uses [T] [V] [C] [D] [H]; the element paper uses DERIVED, MEASURED, RECOGNISED, HYPOTHESIS and PREDICTION TESTED.
- **WTK's "kill condition before the run" discipline.** Used in 4.17, where it caught a false claim.

## 5. The strongest connections

1. **The loop wall is WTK's selection threshold for the loop (4.1 and 4.2, EXACT).** The element paper's two-face closing condition is exactly the elliptic/parabolic boundary of the commutator transport. WTK's own three outcomes appear on measured core-opening ratios:
   - a rotating line inside (nitrogen's faces);
   - slow selection at the wall;
   - strict selection outside (carbon's faces, and carbon with nitrogen, which is only just outside).

   Two Trees' Schottky statement is the all-words version (4.5, finite evidence to length 10).
2. **The loop's WTK stress is the closing sum (4.3, EXACT in the corner frame).** S = Γ_a² + Γ_b² and κ² = 1/(1 − Γ_a² − Γ_b²) = cosh² d(corner, centre of the turn). This joins WTK Proposition 7, the VOTKP Petermann factor and the element paper's mixed-face test in one formula. WTK's Theorem 4 caveat (instrument dependence) is made concrete.
3. **The rail coordinate (4.6 and 4.7, EXACT).** Γ = tan(ψ/2): the wall sits at sec ψ = 3, Catalan's rail root is (3 + 2√2)², and Catalan's constant is ∫₀¹ 2 artanh Γ/(1 + Γ²) dΓ. Close behind are 4.9 (the localization moment is WTK's metric) and 4.16 (the three-mode elimination is WTK Proposition 10).

## 6. Not found or not checked

- WTK does not mention ionization energies, elements, hardness, the loop wall, Γ² = ½ or Two Trees. Every connection above is a map I constructed, graded as such.
- The loop construction (A, B and their commutator) is taken from the VOTKP v3.2 results as summarised in `paper/votkp_v3_2/code/atlas_map/ATLAS_REPORT_1.md` (trace 2 − 4 sinh⁴(r/2)). The VOTKP v3.2 paper itself was not reread for this map.
- The Zenodo record could not be opened (proxy refusal). Edition 3 was confirmed as the Zenodo version through the Lean repo's `PROVENANCE.md` checksums.
- Not rerun: WTK's own verifier (`verify.py` in the code zip) and the Lean builds of either repo. Their outputs were not needed for these maps.

## 7. Check scripts

All are in `/home/claude/connections/checks_transport/`. Each has `# SCRIPT: NAME` at the top and its output file beside it.

| Script | Sections |
|---|---|
| `check_loop_selection_v1.py` (WTK-LOOPWALL-LOOP-SELECTION-01) | 4.1, 4.2 |
| `check_loop_petermann_stress_v1.py` (WTK-LOOPWALL-PETERMANN-STRESS-01) | 4.3, 4.4 |
| `check_schottky_words_v1.py` (WTK-LOOPWALL-SCHOTTKY-WORDS-01) | 4.5 |
| `check_rail_reflection_v1.py` (WTK-LOOPWALL-RAIL-REFLECTION-01) | 4.6, 4.7, 4.8 |
| `check_localization_metric_v1.py` (WTK-LOOPWALL-LOCALIZATION-METRIC-01) | 4.9, 4.10, 4.12 |
| `check_peel_line_distance_v1.py` (WTK-LOOPWALL-PEEL-LINE-DISTANCE-01) | 4.11 |
| `check_readout_bound_v1.py` (WTK-LOOPWALL-READOUT-BOUND-01) | 4.13, 4.14 |
| `check_three_mode_schur_curvature_v1.py` (WTK-LOOPWALL-THREE-MODE-SCHUR-CURVATURE-01) | 4.16, 4.17 |
| `check_pairing_area_v1.py` (WTK-LOOPWALL-PAIRING-AREA-01) | 4.18 |

## 8. Sources read

**What Transport Keeps**

| Source | Version | How read |
|---|---|---|
| `What_Transport_Keeps(2).pdf`, Drive id 18VqfJ9tSpzY4M6L9o0CAPemp5p5uDdyt (current-papers folder) | research edition 3, 6 September 2026, 22 pages | **in full** |
| `What_Transport_Keeps (3).html`, Drive id 11MDPc_yDpflB3V7M4MjYF5ULHeB8rqkC | edition 3 | headings and theorem list compared with the PDF; same text |
| `What_Transport_Keeps_Proofs_and_Code (3).zip`, Drive id 18XD-mk-r7yI9CiTctus9ML5m7vC2ZBGq | edition 3 code package | unpacked and file list read; not rerun |
| `dicipler-pixel/what-transport-keeps-lean`, commit 4754fda (7 October 2026) | — | `README.md`, `PROVENANCE.md`, start of `LIMITATIONS.md` read |

**The Loop Wall** (`/home/claude/votkp-lean`, branch element-paper/loop-wall, folder `research/2026-11-20-element-paper-loop-wall/`)

| Source | How read |
|---|---|
| `README.md` | in full |
| `QUANTUM_CHEMISTRY_LINKS.md` | in full |
| `CLAUDE_REVIEW.md` | in full |
| `VOTKP_Element_Paper_Loop_Wall_v8_20261121.html` | text extracted and read in full |
| `lean/LoopWall.lean` | skimmed: definitions and theorem names to line 218, plus the silicon and silver anion and window theorems |
| `spinor_recovery/README.md` | in full |
| `checks/check_hardness_electrophilicity_v1.py` | header and table read |
| `batch12/chemistry/anion_chemistry_h_nd.csv` | silver row only, for the electron-affinity uncertainty |

**Other context files**

| Source | How read |
|---|---|
| `paper/votkp_v3_2/code/atlas_map/ATLAS_REPORT_1.md` | Job 3 (results 1 to 6) and opening section read |
| `paper/votkp_v3_2/code/atlas_map/ATLAS_REPORT_2_all_cards.md` | the lines naming What Transport Keeps (B48, B134 to B136, B148) and the cards on obliqueness read |
| `research/2026-11-13-space-step/T14_dirac_time/NOTES.md` | the lines naming What Transport Keeps read |
| `data/element_thresholds_20261011.json.gz` (repo root) | used by the scripts |

**Web** (two searches, results not opened)

- [arXiv 1907.00347, Geometric conditions for matrix domination in two dimensions](https://arxiv.org/html/1907.00347v2): found as prior art for dominated 2×2 products; not read.
- A search for the Catalan integral in Γ form was inconclusive; nearest hits included [ProofWiki, Definite Integral from 0 to 1 of Arctangent of x over x](https://www.proofwiki.org/wiki/Definite_Integral_from_0_to_1_of_Arctangent_of_x_over_x) and [arXiv 1203.4618](https://arxiv.org/pdf/1203.4618).
