# READ_A4: VOTKP / Elemental Peeling, four Drive versions

## Coverage (final)
- v0.6 html (VOTKP_ELEMENTAL_PEELING_PAPER_v0_6_20260924.html, Drive 1d8J0iL19ZP2vxOk5jvc9F73QdtgqXXEU, 3,318,802 bytes): 112,171 characters of text after stripping script, style, tags and data URIs; 3,657 lines. Read in full: yes.
- v0.7 html (VOTKP_ELEMENTAL_PEELING_PAPER_v0_7_20260924.html, Drive 1J-2438vIFi9oEZWSmVtHNv1-DNQnthmD, 3,834,382 bytes): 123,850 characters; 3,928 lines. Read in full: yes.
- v0.7.1 research revision pdf (VOTKP_Elemental_Peeling_Research_Revision_0_7_1.pdf, 51 pages, 2,767,386 bytes, Drive 1334aUZ2UrluN508oJyW0Cs34YAaqyz2H): 151,724 characters via pdftotext -layout; 2,426 lines. Read in full: yes.
- v0.8 pdf (VOTKP_ELEMENTAL_PEELING_PAPER_v0_8_20260924.pdf, 59 pages, 3,437,387 bytes, Drive 1s6lrLttv44SRrNlDyLTKb9RGoK3y5vKn): 175,931 characters via pdftotext -layout; 2,678 lines. Read in full: yes (lines 1-1440 in earlier pass; 1441-2678 in the final pass).
- Read-tool note: a 980-line chunk of v0.7.1 was refused as too large; read in 500-line chunks instead.
- Error log: the first page count for v0.7.1 was recorded as 29; corrected to 51 (pdfinfo). The Be correlation hole was first described as same-spin in v0.6; v0.7 onward states it is the spin-integrated exchange-correlation hole.

## Element-specific results (all four versions)
| Element (Z) | Quantity | Number | Version and section |
|---|---|---|---|
| Be (4) | exchange-correlation hole | about 2 Å; 4-5 Å at 21 eV plasmon | v0.6 Sec 4; v0.8 Sec 15.1 |
| Cu (29) | IE1; step; R450/550/650 | 7.726380 eV; 101.67 eV (k=11); 0.538/0.624/0.935 | v0.6 Sec 7, Table 2 |
| Ag (47) | IE1; step; R | 7.576234 eV; 83.46 (k=11); 0.980/0.983/0.990 | v0.6 Sec 7 |
| Au (79) | IE1; step; R | 9.225554 eV; 79.80 (k=11); 0.408/0.792/0.957 | v0.6 Sec 7 |
| Pt (78) | IE1; step; R | 8.95883 eV; 75.5 (k=10); 0.588/0.641/0.678 | v0.6 Sec 7 |
| Ne, Ar, Kr, Xe, Rn | noble-band first step τ1 | 0.642, 0.561, 0.554, 0.548, 0.569 | v0.8 Sec 15.9 |
| Og (118) | predicted IP1, IP2; τ1; polarizability | 8.888, 16.195 eV; 0.600; about 58 a.u. (Rn 35) | v0.8 Sec 15.9 |
| E119 | predicted IP1; column-line value | 4.784 eV; 3.23 eV line (1.55 eV above) | v0.8 Sec 15.9 |
| E120 | relativistic IP1; column-line value | 5.851 eV; 3.71 eV line (2.14 eV above) | v0.8 Sec 15.9 |
| Lr (103) | measured IP1 | 4.96 eV (lowest actinide) | v0.8 Sec 15.9 |
| Hf, Ta | depth-law misses | at K = 11-12 | v0.6 Sec 8.3; v0.8 App D |
| Re, Os, Ir, Pt, Au, Hg | depth-ladder misses | K=5-6; Os, Ir, Pt, Au at K=7 | v0.6 Sec 8.3 |
| Actinides (f-block, series not named) | cross-series recovery from lanthanides | 2-3 of 14 | v0.8 Sec 15.9 (killed) |
| H⁻ (1), D⁻, Ps⁻ | τ; Γ | 2.89134 / 0.89483; 2.89180(10) / 0.89488; 3.0355(4) / 0.9083 | v0.8 Sec 15.3 |
| He | τ | 0.7945 | v0.8 Sec 15.3 |
| Li | τ1 | ln(75.64/5.39) = 2.641 | v0.8 Sec 15.3 |
| Na | ten steps IE1 to IE11 | Γ = 0.9938; distance 5.77 | v0.8 Sec 15.2 |
| Ca, Ar, K | N=28 closure | 0.40-0.42 | v0.8 Sec 15.4 |
| Cr | N=28 closure | 0.19 | v0.8 Sec 15.4 |
| Mg | N=20 closure | gone at Mg | v0.8 Sec 15.4 |
| Ca | N=34 closure | present only in Ca | v0.8 Sec 15.4 |
| Al, Mo, Ta, Zn, Mg, Pb | film echo weights | 0.57-0.87 (overlap bump range) | v0.8 Sec 15.2 |
| Au (gold film) | rise at 450 nm | 15 of 15 local datasets | v0.8 App D |
| Au/TiO2 swap | reflectance at 550 nm | 0.509 to 0.433; peak 0.16 | v0.8 Sec 15.2 |
| (Knot, not an element) 13a3542 vs mirror 13a4018 | longitude angle at α = 0.11247 | θ/2π = -0.0145346 vs -0.0171689 | v0.8 Sec 13.7 |

Other elements named without per-element numbers in the text (listed for completeness): Rb, Cs, Fr, Ba, Ra, Ni, Pd, Rh, Ti, V, W, Zn, Nb, Ru, Gd, Nd, Sc, Co, Fe, Cr, Ir (v0.6 Sec 8.3-8.4 ridge census and calibration context). Numbers for these appear only in the v0.6 ridge census: Electrons-left 28 (Ni-like) prominence 0.284/0.487/0.478 (grows); 46 (Pd-like) 0.266/0.358/0.149 (peaks mid); 54 (Xe-like) 0.338/-0.028/-0.004 (vanishes deep).

## v0.8 notes lines 1441-2678 (read in full)
- Sec 13.3 end: on five blind pairs of Table 7, |J3| separates all five in order of volume.
- Sec 13.4 colour ladder: 21 pairs identical on J2 and J3; 4-coloured Jones separates all 21 [Exact].
- Sec 13.5 A-polynomial volume: figure-eight Mahler measure matches Vol(4_1) to 2.0298832128193074 [Exact]; 5_2 matches 2.82812208843 vs 2.82812208833. Torus control: omega = 0 identically. Factorizations at L=1: A31 ∝ (u+1)Δ31; A41 ∝ (u+1)²Δ41; A52 ∝ u(u+1)³Δ52.
- Sec 13.6 loop expansion: P1(4_1) = 0; P1(3_1) = −t⁻² (t²+1)(t−1)².
- Sec 13.7 representation windows: torus knots 3_1, 5_1, 8_19 counts equal |σω|/2 at 135 of 135 grid points. 13-crossing window walls at α = 0.10971 and 0.11522. Longitude angles at α = 0.11247: θ/2π = −0.0145345761398 (13a3542), −0.0171688847270 (13a4018). Rice-Mele pump Chern number 1.000000 on FHS grid, 1.0001 in real time.
- Sec 13.7 clock: η = 1 − 2{α}; cycle of duration T carries current e/T; flux ramp gives (e²/h)V.
- Sec 14 realization layer: polystyrene [η]knot/[η]lin = 0.48, [η]cyc/[η]lin = 0.66, Tg = 93.0, 99.3, 101.5 °C (Du et al., Nature Chemistry 2026). Leigh molecular knot loses six nitrogens (C117H136N9O6 to C117H130N3O6).
- Sec 15.1: each step X^{q+} → X^{(q+1)+} + e⁻ costs IE_{q+1}; τ_q = ln(IE_{q+1}/IE_q); Γ_q = tanh(τ_q/2). Pauli exchange hole imaged (Yao et al. 2025); Be hole ~2 Å.
- Sec 15.2 Theorem 15.1 (peel steps add like velocities): Γ_{k→l} = Γ_k ⊕ … ⊕ Γ_{l−1}. Corollary 15.2: d(0,w) = 2 artanh|w|; for w = Γ_{k→l}, equals ln(IE_l/IE_k). Sodium Γ = 0.9938 at distance 5.77. Corollary 15.3: film reflection r(d) = Γ ⊕ x; ∂(Γ⊕x)/∂x at 0 = 1 − Γ² = sech²(τ/2) = 1/γ². Radar reading: β = (z−1)/(z+1) = Γ; Bondi factor = √z. Prior art: Vigoureux 1992; Monzón & Sánchez-Soto 1999; Yonte et al. 2002; Allen & Healy 2004. "We found no use of this law for successive ionization energies."
- Test H-01 (killed): |1−Γ²| 0.778 vs |Γ| 0.994 in sample; held-out |Γ| 0.959-0.977 (171 cases; 57 distinct Γ values).
- Order of peeling: ⊕ associative and commutative for real or complex arguments. Ladders 1,2,6 and 1,3,6 share tanh(½ ln 6) but differ in steps. Associator identity: (x⋆y)⋆z − x⋆(y⋆z) = P[x(I−P)(yz) − (I−P)(xy)z], checked to 1e-15. Film stack zero phase telescopes to tanh(½ ln(N0/Nn)).
- Matter waves: r = −tanh(τ/2), τ = ln(k2/k1); closed form vs transfer matrix 3.5e-16.
- Sec 15.3 Theorem 15.4 (scale blindness): multiplying all masses by λ scales every energy by λ; ratios unchanged. Mass-ratio table: H⁻ infinite-mass τ = 2.89134; D⁻ 2.89180(10); H⁻ measured 2.89206(2); Ps⁻ theory 3.0361; Ps⁻ measured 3.0355(4). Deuteron shift −2.6(1.0)×10⁻⁴; normal mass shift 1.66 cm⁻¹ leaves residual 1.55(62) cm⁻¹. Statistics: He τ = 0.7945; Li τ1 = ln(75.64/5.39) = 2.641 because 1s3 is forbidden. Quantum dots: "the whole 'ladder' of electrochemical potentials can be moved up or down" (Hanson et al. 2007); peel coordinate does not apply. Antihydrogen 1S-2S agrees with hydrogen to about 2×10⁻¹².
- Sec 15.4 nuclear onion: τ_N = ln(S2n(N)/S2n(N+2)); magic-number ridge prominence 8: 0.188; 20: 0.110; 28: 0.141; 50: 0.209; 82: 0.244; 126: 0.221; non-magic 90th percentile 0.000. N=40 and 70 carry no ridge (−0.021, −0.002). NUC-01 (434 even-even nuclei, FRDM2012 β2 label): peel shape 0.65 vs Np·Nn 0.83 (killed).
- Sec 15.5 knots as particles: tight-knot model, Λ = 65.16 ± 0.61 MeV. P-01 (pre-registered, extension to pure-gauge lattice): ratios 2nd/1st lattice 1.390(37); tight knots uncorrected 1.303 (−2.4σ); curvature-corrected 1.275 (−3.1σ). 3rd/1st lattice 1.504(43); uncorrected 1.592 (+2.1σ); corrected 1.557 (+1.2σ). Corrected fails 3σ on first ratio; combined deviation 2.8σ.
- Sec 15.6-15.7: anyons at filling 1/3 (Ghosh et al. 2025); fractional charge e/3 in bilayer graphene (Di Luca et al. 2026); hopfions with H = −1 in FeGe (Chen et al. 2026); vortex-knot fusion conserves Hopf index (Hall et al. 2026). Electroweak sphaleron barrier 9.1 TeV (Matchev & Verner 2025).
- Sec 15.8 electron not a knot: LEP eeee contact Λ ≳ 8-10 TeV; excited electrons excluded to 5.6 TeV (PDG 2025). Requirements list for a topological electron given; "No such model is established, and none is proposed here."
- Sec 15.9 new elements: Og τ1 = 0.600 in noble band; "expected to be a semiconductor rather than a noble gas" (Mewes 2019). Element 119 IP1 4.784 eV on alkali level; column-line forecasts 3.23 eV (119) and 3.71 eV (120). Row-swing candidate of §8.9 forecasts row-7 main-group height 155 kJ/mol [Open]. Superheavy families 4 of 7 for Rf-Ds (T16 killed). Lr measured IP1 4.96 eV. f-block transfer killed (2-3 of 14).
- Sec 16 common pattern: five findings. Sec 17 open problems (measured-only deep peel; Og second IE; clusters; continuum glueball spectrum; Khovanov maps; film measurement with 0.92 threshold frozen; post-gold metamer; complete counts for the 13-crossing pair; drive for meridian phase; general L = 1 statement; row-swing tests; elemental-knot bridge).
- Sec 18 negative controls 1-32 (listed in text). Items 18, 21, 22 relevant to walls: "An Alexander root need not change the signature: 513 roots of even multiplicity do not." "Meeting L = 1 on the A-polynomial curve is not a wall (u = −1 in 3_1, 4_1, 5_2)."
- App A proofs: A.8 Theorem 6.1 expansion; A.9 Theorem 8.1: (z−1)/(z+1) = (e^τ−1)/(e^τ+1) = tanh(τ/2); A.10 torus control; A.11 Theorem 6.2 completing the square, circle |x−x_c| > |x_c|; A.12 Proposition 11.1 parity at a simple root: det H changes sign and σ changes by ±2 (theorem, checked 16,656 of 16,656). A.13 surviving matches (Ker C equivalence).
- App B Lean 4 checkpoint: 49 declarations (30 foundations, 14 force recovery, 5 boundary ledger); finite algebra only.
- App C ideas held: spinor cascade and Clifford layers; Kelvin vortex atoms; the row as one impedance step.
- App D test ledger (pre-registered kill conditions, with results): WALL-01 0 of 17,360 (reproduction); parity at a wall simple roots 16,656/16,656; TIME-01a 135/135; TIME-01b Chern 1.000000, real-time 0.99895 (missed registered 1e-3 by 1.05e-3, traced to sampling); H-01 killed; P-01 corrected 3.1σ, uncorrected 2.4σ; NUM-01 killed (0.392 vs 0.267); DATA-01 measured-only arm not possible with present data; RUSSELL-2 S3 passed; RHYTHM T16 superheavy killed.
- App E literature read at source; remaining listed as title-and-venue only or knowledge-only. Includes Hughes et al. arXiv:2502.18575 and Lyu, Keitel, Harman arXiv:2504.11237.
- App F scripts list. Draft v0.8. Written by Claude from Jeromie Beasley's research programme and his collaborators' reviews.

## Bold mathematical moves (across versions)
- Theorem 6.2 (v0.6, carried to v0.8): the exact boundary circle |x − x_c| > |x_c| with x_c = −C̄/A, A = 1−|a|⁴, C = ā(1−a²). Dropped threshold: the 0.92 radius remains the calibration threshold; no Γ²=½ wall.
- Theorem 15.1 (v0.8): peel steps add like rapidities; ⊕ associative and commutative (order of peeling).
- Corollary 15.3 (v0.8): 1 − Γ² = 1/γ² is the echo derivative; killed as separator in H-01.
- Theorem 8.1 (v0.6 Sec 8.1; v0.8 A.9): (z−1)/(z+1) = tanh(τ/2); the ratio z appears as a radar/Bondi factor √z (v0.8 Sec 15.2).
- Theorem 8.2 (v0.8, split of the peel step): Pythagorean shell wall Γ_sh = (2n−1)/(n²+(n−1)²); pre-registered verification of 5,714 steps to 4e-16.
- Proposition 11.1 / A.12 (v0.8): parity at a simple root, σ changes by ±2; checked on 16,656 of 16,656.
- Thin-knot argument (Lee; Ozsváth–Szabó): cited by title and venue only in v0.8 App E.
- 13a_3542 window (v0.8 Sec 13.7): signed representation count equals |σω|/2; the longitude branches differ in sign and rate; not interval-certified.
- Pumped Chern number (v0.8 Sec 13.7): η = 1 − 2{α}; one eigenvalue crosses zero per period.

## Connections to today's frame (quoted)
- Γ = tanh(½ ln z), length ln z: v0.8 Sec 15.1 "Γq = tanh(τq /2)"; v0.8 Sec 15.2 "β = (zk − 1)/(zk + 1) = Γk".
- Half-line wall Γ² = ½ and z = 3+2√2: no occurrence in any of the four versions. Nearest: v0.6 "|Gamma| ~ 0.92" threshold; v0.8 "0.918-0.926" band.
- √2: appears in v0.6 Sec 5.8 cumulant "(6+√6)/10" and Sec 5.9 "T(0)=T(√2)=1/2"; the √2 there is a polynomial root, not the wall.
- 1/√2: no occurrence found.
- Phase at a wall: v0.8 Sec 13.7 "a second arc is born from L = 1"; Prop 11.1 "σ changes by ±2". Negative control 22 ("Meeting L = 1 ... is not a wall").
- Cancel/lock/convert: v0.8 Sec 15.2 "the phase that appears in compound stacks is a Thomas rotation".
- Two books: v0.8 Sec 15.2 "the two halves of Part II obey one composition law"; v0.8 Sec 16 "Two geometries of a boundary."
- Tree/ball: not found.
- Lorentz/rapidity: v0.8 Sec 15.2 "rapidities φ add"; Cor 15.3 "the Lorentz factor of the equivalent rapidity."
- Neutrinos, Koide, spin: no occurrence in v0.6, v0.7, v0.7.1 or v0.8. v0.8 Sec 15.8 "spin 1/2 and Fermi statistics" is in a required-properties list, not a result.
- Statistics: v0.8 Sec 15.3 "bosons and fermions give the same helium-like peel (τ = 0.7945 for He)."

## Contradictions with today's frame
- The frame's Γ²=½ wall and z=3+2√2 do not appear in any version. v0.6 and v0.7 place the threshold at |Γ| ≈ 0.92.
- v0.8 H-01 killed |1−Γ²| as a separator: "The echo weight is the worse separator" (0.743 vs 0.96-0.98). The frame's amplitude-dies-at-wall reading is not used by the paper.
- v0.8 Sec 15.2: "We found no use of this law for successive ionization energies." This is the paper's own statement; the frame's peel-as-boost reading is claimed by the paper only as an identity.
- P-01 tight-knot extension fails at 2.8σ combined (v0.8 Sec 15.5); the paper calls it moderate evidence against the extension.
- Row-swing identity as printed in v0.8 Sec 8.9 fails for a = 2, b = 1 (left side 1, right side 7/3); flagged as possible typesetting omission (parentheses lost in pdftotext). Not checked against page image.

## Final report (under 300 words)
Coverage: all four versions read in full (v0.6 3,657 lines; v0.7 3,928 lines; v0.7.1 51 pp; v0.8 59 pp, 2,678 lines).
Strongest element results: (1) Li τ1 = ln(75.64/5.39) = 2.641 (v0.8 Sec 15.3); (2) Na Γ = 0.9938 over ten steps, distance 5.77 (v0.8 Sec 15.2); (3) Og τ1 = 0.600 in the noble band (v0.8 Sec 15.9); (4) H⁻/D⁻/Ps⁻ mass-ratio table, Ps⁻ measured 3.0355(4) (v0.8 Sec 15.3); (5) Cu/Ag/Au/Pt calibration table (v0.6 Sec 7).
Boldest moves: Theorem 6.2 exact boundary circle (v0.6, v0.8 A.11); Theorem 15.1 rapidity addition with associativity (v0.8); Proposition 11.1 parity at a simple root (v0.8 A.12).
Wall connection: none of the four versions contains Γ² = ½ or z = 3+2√2. The nearest wall-like items are Prop 11.1 (sign change at a root, σ ±2) and the 0.92 Smith threshold, which the paper treats as a calibration number. Neutrinos, Koide and spin are absent except as a list of required electron properties.
Status: READ_A4.md is finalized in place (coverage and element table in the header). The row-swing identity flag remains unchecked against the page image.

## Working notes from v0.6, v0.7, v0.7.1 (kept below as read)

## v0.6 notes (lines 1-450 of extracted text)
- Title: "VOTKP: A Multi-Layer Knot Potential for Elemental Peeling", Draft v0.6, 24 Sep 2026.
- Abstract grades: [Exact], [Theorem], [Cited], [Reproduction], [Open].
- Peel coordinate: Gamma_k = tanh(1/2 ln(IE_{k+1}/IE_k)) (abstract, item 2). Exact change of coordinates.
- Thin film: Gamma = (1-N)/(1+N); echo x = r12 e^{4 pi i N d/lambda}; single Smith radius |Gamma| ~ 0.92 separates regimes (99.4% in sample, 170 of 171).
- Peel steps compose by Einstein velocity addition: Gamma_{k->l} = Gamma_k (+) ... (+) Gamma_{l-1}; peel coordinate is hyperbolic length on Smith disk (Abstract item 4, section 4 claims).
- Atom results (abstract): period-6 elements; ten peel steps classify all 18 on NIST values, median 17 of 18.
- Polarizability alpha propto IE_1^{-3.04} (R^2 = 0.91).
- Shape ln(IE_{k+1}/IE_k) recovers periodic group, held-out accuracy 0.95.
- Section 6 (two-sided surface), 6.4 thinning peel echo; 8 ionization onion as reflection atlas; 9 refraction (Snell) test FAILED.
- Section 11.5 signature function: 13a_3542 vs mirror of 13a_4018 separated.
- Section 15.9 "Where new elements fit"; Section 15.1 "The electron is the unit removed".
- Elements named so far (with numbers): H, He-like via H^-, D^-, Ps^- (charges/mass ratio extension only), period-6 elements (Cs, Ba, La family ranges; 18 classified), Li, Na, K, Rb, Cs first steps (per today's frame, not yet confirmed in this file's text).

Next: continue reading v0.6 from line 451.

## v0.6 notes lines 451-1150 (read in full)
- Sec 4 correlation hole n2 (Be ~2 A base, 4-5 A near 21 eV plasmon, Cited arXiv 2601.20814); quantum metric g_ij; allowed spacing Delta_allowed(O). Two-level sheet metric 1/4 (Exact).
- Thm 4.1: mu_eff(r) = mu_b + (c^2/delta)(1-2r); chi = 2c^2/delta = 8 delta g_aa(0); r_c = (1/2)(1+mu_b delta/c^2). Response is a curvature.
- Sec 5.9 two-site impossibility: T_s(x) = (x-s)^2/(x^4 - 2 s x^3 + 2); T(0)=T(sqrt2)=1/2 for both signs; Delta = 79,600,000/400,039,601 ~ 0.19898. Records (1/2, 1/5). Level spacing g_s = sqrt(s^2+4) (sqrt5 for s=+-1, same).
- Sec 5.8 cumulant sets {1/5,1/2,4/5} vs {3/10,(6+sqrt6)/10,(6-sqrt6)/10}; sqrt6 appears; c3=0 vs 3/50.
- Sec 6.3-6.4 thinning peel: Gamma = (1-N)/(1+N); echo x = r12 p^2; Thm 6.2 exact boundary circle |x - x_c| > |x_c|, x_c = -conj(C)/A, A = 1-|a|^4, C = conj(a)(1-a^2). Calibration threshold |Gamma| 0.856 (frozen); the 0.92 radius (band 0.918-0.926, 99.4% in sample). Gamma radius ~0.926-0.935 for bumps vs non-bumps. Thm 6.1: 1-Gamma^2 = t01 t10 (round trip).
- Gamma = (1-N)/(1+N) and 1-Gamma^2 is a unit-disk identity; no sqrt2 wall stated here.
- Sec 7 calibration table (Table 2): Cu (Z=29) 3d10 4s1, IE1 7.726380 eV, step 101.67 eV (k=11), R450 0.538, R550 0.624, R650 0.935. Ag (Z=47) 4d10 5s1, IE1 7.576234, step 83.46 (k=11), R 0.980/0.983/0.990. Au (Z=79) 5d10 6s1, IE1 9.225554, step 79.80 (k=11), R 0.408/0.792/0.957. Pt (Z=78) 5d9 6s1, IE1 8.95883, step 75.5 (k=10), R 0.588/0.641/0.678.
- Sec 8.1 Thm 8.1: tau_k = ln(IE_{k+1}/IE_k) = 2 artanh(Gamma_k); Gamma_k = tanh(tau_k/2). Alkali first step Gamma ~0.5 to 0.87 (high reflection). "Most steps have Gamma < 0.4."
- Sec 8.2 Run 01 (Table 3): held-out group accuracy K=10: static S2 0.51, peel T1 0.95; peel shuffled 0.04. T1 beats S2 35/36 variants (best 0.984). Under uncertainty K=10 median 0.92, 5th pct 0.89.
- Sec 8.3 depth ladder (Z<=54 trained, period-6 test): accuracy K=1..12: .22 .33 .39 .50 .67 .67 .78 1 1 1 .94 .89. Misses at K=5,6: Re, Os, Ir, Pt, Au, Hg; K=7: Os, Ir, Pt, Au; beyond K=10 Hf, Ta. Pooled 62 of 65 misses explained. 198 stages: 43 measured, 46 semi-empirical, 109 theoretical. Hf stages 6-11 uncertainty 5-10 eV. Period-6 K=10 median 17/18, 5th pct 15/18; 18/18 in 14% of draws. Kill condition (median<16 or 5th<14) did not trigger.
- Sec 8.4 ridge census (prominence): Electrons-left 10: 1.011/0.905/0.772; 18: 0.533/0.191/0.052 (Ar-like shrinks); 28 (Ni-like): 0.284/0.487/0.478 grows; 36 (Kr-like) 0.571/0.244/0.086; 46 (Pd-like) 0.266/0.358/0.149 peaks mid; 54 (Xe-like) 0.338/-0.028/-0.004 vanishes deep; 68: 0.252/0.268/0.149. Predicted closure at 60 (Kr 4d10 4f14) appears only weakly, Z>=88 only, NIST-estimated stages. Cited: Lyu, Keitel, Harman, Phys Rev Research 2025 (Coulomb filling order).
- Sec 8.5 Run 02 polarizability: peel loses to static 9/9. ln alpha held-out error: S2 0.202, 0.186, 0.150 (K=3,6,10); T1 0.729, 0.636, 0.503. Run 03: polarizability, covalent radius, atomic radius: peel beats static 0/9.
- Element-specific: Be (Z=4) correlation hole (Cited). Alkali first step (Li, Na, K, Rb, Cs) Gamma up to 0.87 (text says "alkali first step", values not per element here).
- Contradiction-check: v0.6 uses Gamma ~0.92 as threshold, not 1/sqrt2 or z=3+2sqrt2. Not yet seen the wall in this section.

Next: continue v0.6 from line 1151.

## v0.6 notes lines 1151-1850 (read in full)
- Sec 8.5 level carries response: ln alpha = 10.28 - 3.04 ln IE1, R^2 = 0.906 over 86 elements (Exact). Morton 2000/2003 lines for 80 elements (Ca absent); 66 with tabulated alpha outside f-block. Held-out ln alpha error: level 0.282; strongest-line denominator 0.267; numerator-added 0.392/0.374 (NUM-01 kill triggered). Listed lines carry median 49% of alpha: Zr 2% (one line), Sc 121%. Slope 0.54 not 1.
- Sec 8.6 noble-gas resets (Table 4): polarizability minimum 6/6, IE1 maximum 6/6, no bound anion 6/6. tau_1 at next element largest values: Li 2.641, Na 2.219, K 1.986, Rb 1.877, Cs 1.783, Fr 1.705. Covalent radius minimum only 4/6 (fails Ne, Kr) "not a reset quantity".
- Sec 9 refraction (Snell) test FAILED: turning set 1 hit, 9 false, 5 missed vs rule 6 hits; confusion labels 0 of 6 (p=1); Slater geometry flat in deep ions cannot order 28 above 18; step size vs Gamma_k correlation 0.61-0.68 but 0.02-0.03 after detrending. Fixed-rank active space {(n-1)d, ns, np}.
- Sec 11.1 HOMFLY convention v^-1 P(L+) - v P(L-) = z P(L0); P(4_1), P(3_1), P(8_19) given (Exact).
- Sec 11.2: 19 pairs of 13-crossing knots (equal Alexander and Jones, different HOMFLY); 18 knots involved; 12 pairs have Alexander = 1; figure 13n_3871 / 13n_65. 15-crossing census cited Dlotko, Gurnari, Sazdanovic 2025 (53.7% vs 53.4%).
- Sec 11.4 categorified rung: 354 blind pairs through 12 crossings; 253 volume-differing; registered claim killed (233 of 253 stay blind). Thin knots: all 11,283 thin through 13 satisfy delta = -sigma/2 and m-a = sigma/2 (Exact). 2,525 thin same-signature blind pairs; none separated. 84 signature-difference pairs all separated. HFK separates 185 equal-volume pairs, through thick knots.
- Sec 11.5 Levine-Tristram signature: walls are Alexander roots on unit circle; 17,360 entries; Table 5: root multiplicity 1: 16,656 entries, no change 0 / change +-2 16,656; mult 2: 575 entries, 494 no-change, 81 change +-4; mult 3: 98, all change +-2; mult 4: 23 (19 no change, 4 change); mult 5: 8 all change. Prop 11.1 (parity at a wall): half the change has parity of m; simple root change exactly +-2 (Theorem, elementary). "Every root of odd multiplicity is a wall."
- Torus knots carry max |sigma|; 12 crossings: 34 knots tie at 8.
- 13a_3542 vs mirror 13a_4018: window t in (0.4388, 0.4609); volumes 22.6445 vs 22.6783; exact arithmetic at rational points omega_s = ((1-s^2)+2is)/(1+s^2); sigma=0 at s=4/5 (t=0.4296) and s=9/10 (t=0.4665); at s=6/7 (t=0.4511) |sigma|=2 same sign. Of 85 blind pairs sigma_omega separates, 30 are pure chirality flips.
- Sec 12 field loading: W = z^alpha w^beta/(z^p + w^q) on |z|^2+|w|^2=1; Hopf charge Q = alpha q + beta p; T(3,4) charges 7,10,11,13,15 from (1,1),(1,2),(2,1),(1,3),(3,1); T(2,3): 5 and 8; T(2,5): 7. Sutcliffe 2007 relaxed energies T(3,4): 7.857, 8.272, 8.761 at Q=12,13,14; survives relaxation only from Q=12.
- Sec 13 volume: Torus knots Seifert-fibred, SnapPy 0 for 3_1, 5_1, 8_19. Table 6 volume pairs: 5_1/10_132 (0 vs 4.056860224); 8_8/10_129 (7.801341224 vs 8.901516637); 8_16/10_156 (10.579021917 vs 11.163390642); 10_25/10_56 (11.875779604 vs 12.398802156); 10_40/10_103 (12.888740330 vs 13.874789570). Perko 10_161/10_162 is one knot.
- Sec 13.3 Hughes et al. arXiv 2502.18575: Vol ~ 3.25 ln(|J3(e^{8 pi i/15})| + 36.97) - 1.72; 1.21% error over 177,316 knots. Offset-free line Vol = 2.979 ln|J3| - 0.658 (205 knots; mean err 4.9%); phase window 1.46-2.42 rad; 8 pi/15 best.
- Sec 13.4 colour ladder: 21 pairs identical on J2 and J3; separated by J4. Named: K11a196/K11a216 (17.2855, 17.2795), K11n4/K11n21 (12.5531, 12.4680).
- Sec 13.5 A-polynomial: figure-eight 2 int log|L| dtheta = 2.0298832128193074 vs SnapPy 2.029883212819307; 5_2 pi m = 2.82812208843 vs vol 2.82812208833.
- Element-specific results in this chunk: none for elements. Atomic: noble gases (He, Ne, Ar, Kr, Xe, Rn implied by 6 noble gases); alkali tau_1 values above; Zr, Sc (Morton lines); Ca absent from Morton table.
- Possible contradiction-check: nothing yet on wall (no Gamma^2 = 1/2 yet). The sqrt2 in Sec 5.9 is the abscissa x = sqrt2, not a wall.

Next: continue v0.6 from line 1851.

## v0.6 notes lines 1851-2750 (read in full)
- Sec 13.5 A-polynomial on L=1: A_{3_1}(1,M) ~ (u+1) Delta_{3_1}(u); A_{4_1}(1,M) ~ (u+1)^2 Delta_{4_1}(u); A_{5_2}(1,M) ~ u (u+1)^3 Delta_{5_2}(u). Meets L=1 at u=-1 with Delta(-1) != 0, "not by itself a wall".
- Sec 13.6 loop expansion: P_1(4_1)=0; P_1(3_1) = -t^-2 (t^2+1)(t-1)^2 (Rozansky integers).
- Sec 13.7 representation windows: trefoil arc 1/12 < alpha < 5/12; 8_19 steps 0-1-2-3-2-1-0 at six walls. 13-crossing pair walls alpha = 0.10971 and 0.11522; longitude theta/2pi = -0.0145345761398 (13a_3542), -0.0171688847270 (13a_4018); mid-window d(theta/2pi)/d alpha ~ -4.6 vs -6.3. Not interval-certified. Rice-Mele pump Chern number 1.000000 (FHS), 1.0001 real-time. Clock: flux ramp cycle h/(eV), current (e^2/h) V (Cited Laughlin 1981). "No Hamiltonian here makes a knot's meridian phase the driven parameter; that bridge is open (§17)."
- Sec 14 realization: polystyrene knot/cyclic/linear eta ratio 0.48, 0.66; Tg 93.0, 99.3, 101.5 C (Cited Du et al., Nat Chem 2026). Leigh/Couto JACS 2025 molecular knot C117H136N9O6 -> C117H130N3O6.
- Sec 15.1: IE_{q+1} = E(X^{(q+1)+}) - E(X^{q+}); "The electron is the unit of the peel". Be exchange-correlation hole ~2 A, 4-5 A at 21 eV plasmon (Cited Bista et al 2026).
- Thm 15.1 (peel steps add like velocities): Gamma_{k->l} = Gamma_k (+) ... ; rapidity addition; tau_k/2 = rapidity. Corollary 15.2: hyperbolic distance d(0,w) = ln((1+|w|)/(1-|w|)); "An atom's peel is a walk along one diameter, which is a geodesic." SODIUM: ten steps IE1 to IE11 reach Gamma = 0.9938 at hyperbolic distance ln(IE11/IE1) = 5.77.
- Cor 15.3 film: r(d) = Gamma (+) x; d/dx at 0 = 1 - Gamma^2 = sech^2(tau/2) = 1/gamma^2, gamma = cosh(tau/2) "the Lorentz factor of the equivalent rapidity" (LORENTZ/RAPIDITY CONNECTION). Complex Gamma: not a hyperbolic isometry.
- Radar reading: beta = (z-1)/(z+1) = Gamma_k; Bondi factor k = e^{tau/2} = sqrt(z_k). Cited Einstein 1905, Bondi 1964.
- Prior art: Vigoureux 1992; SU(1,1) ~ SO(2,1); Thomas rotation Monzon & Sanchez-Soto 1999; Allen & Healy 2004.
- Test H-01 (KILLED): |1 - Gamma^2| as separator scores 0.778 in sample (0.743 held-out) vs |Gamma| 0.994 (0.959-0.977).
- Order of peeling: Gamma_1 (+) Gamma_2 = Gamma_2 (+) Gamma_1; ladders proportional to 1,2,6 and 1,3,6 share tanh(1/2 ln 6). Associator for reduction P: nonzero for generic projection (Exact to 1e-15).
- Film stack: Au 20 nm + titania 60 nm at 550 nm: reflectance 0.509 vs 0.433 (swap); peak difference 0.16.
- Matter wave potential step: r = -tanh(tau/2), tau = ln(k2/k1).
- Thm 15.4 (scale blindness): mass scaling lambda leaves IE ratios unchanged (Theorem, elementary).
- ELEMENT TABLE (Sec 15.3, two-step peels, tau = ln(IE/EA)): H- (theory, inf mass) tau 2.89134, Gamma 0.89483; D- (m_e/M = 1/3670.5) tau 2.89180(10), Gamma 0.89488; H- (1/1836.2) tau 2.89206(2), Gamma 0.89491; Ps- theory tau 3.0361, Gamma 0.9084 (table has 0.9084); Ps- measured tau 3.0355(4), Gamma 0.9083. Replacing proton by deuteron: delta tau = -2.6(1.0)e-4; isotope shift 3.21(62) cm^-1 measured, normal mass shift 1.66 cm^-1, residual 1.55(62).
- Helium-like tau = 0.7945 for He. Lithium tau_1 = ln(75.64/5.39) = 2.641 ("exclusion forbids 1s^3").
- Quantum dots (shells 2,6,12) not on peel coordinate. Antihydrogen 1S-2S agrees to ~2e-12 (Ahmadi 2018).
- Sec 15.4 nucleus (NUBASE2020): magic numbers N = 8, 20, 28, 50, 82, 126 as six strongest ridges; mean ridge prominence 0.188 (N=8), 0.110 (N=20), 0.141 (N=28), 0.209 (50), 0.244 (82), 0.221 (126), non-magic 90th pct 0.000. N=20 gone at Mg; N=34 present only in Ca; N=28 falls from 0.40-0.42 (Ar, K, Ca) to 0.19 at Cr. NUC-01 (434 even-even nuclei): peel shape balanced accuracy 0.65 vs Casten N_p N_n 0.83 (failed).
- Sec 15.5 knots: Kelvin 1867, Tait 1877. Tight-knot P-01 (pre-registered, Buniy/Cantarella/Kephart/Rawdon): Hopf link minimal ropelength 8 pi; trefoil 32.7436; 4_1 40.0122. Lattice r0 m ratios: 2nd/1st 5.85/4.21 = 1.390(37); tight uncorrected 1.303 (-2.4 sigma); corrected (BCKR) 1.275 (-3.1 sigma). 3rd/1st lattice 1.504(43); uncorrected 1.592 (+2.1); corrected 1.557 (+1.2). Fitted Lambda = 65.16 +- 0.61 MeV. Glueball lattice states 0-+, 1+-, 2-+ unmatched. (Element-related? none; but the knot-length ordering is a kill condition hit at 2.4-3.1 sigma).
- Sec 15.9 new elements: Oganesson (Z=118) IP1 = 8.888 eV, IP2 = 16.195 eV (Cited Guo, Pasteka, Eliav, Borschevsky 2021); tau_1 = 0.600; noble band: Ne 0.642, Ar 0.561, Kr 0.554, Xe 0.548, Rn 0.569. Og polarizability ~58 a.u. vs Rn 35; semiconductor (Mewes 2019). Element 119: IP1 4.784 eV (arXiv 2509.05509), first peel step not predicted. Lawrencium IP1 4.96 eV (Sato 2015). f-block does not transfer: killed (2-3 of 14 recovered).
- Sec 16 common pattern (v0.6 pre-conclusion): "6 peel steps fail where 10 succeed"; "colour 3 fails where colour 4 succeeds"; HOMFLY classifies at 13 crossings.
- Frame check: "Refraction (subspace turning) did not predict either target." Lorentz/rapidity connections ARE present (rapidity addition, sech^2 = 1/gamma^2, radar/boost reading). No Gamma^2 = 1/2 or z = 3+2sqrt2 so far. Gamma for Li-Cs first steps: alkali first step GAMMA ~0.5-0.87 (text). Na 0.9938 at ten steps.

Next: continue v0.6 from line 2751 to end (~3657).

## v0.6 notes lines 2751-3657 (read in full) -- v0.6 COMPLETE
- Sec 16 common pattern and Sec 17 open problems (measured-only deep peel; Og second IE; clusters; complete oscillator strengths; Khovanov maps; refraction with relativistic orbitals; "The elemental-knot bridge itself" open). Sec 17 explicitly: "A drive for the meridian phase ... None is given here."
- Sec 18 negative controls: "A fixed knot does not fix the field charge"; "Covalent radius is not a noble-gas reset quantity"; "An Alexander root need not change the signature: 513 roots of even multiplicity do not."
- Appendix A.8 check: t01 t10 = (2/(1+N))(2N/(1+N)) = 1 - Gamma^2 (verified algebra).
- Appendix A.12: det H(omega) = (1-bar omega)^{2g} det(V - omega V^T); Prop 11.1 sign-change argument (Rellich, Kato). Simple root => exactly +-2.
- Appendix B: Lean 4 checkpoint: 49 declarations across three modules (30 foundations, 14 force recovery, 5 boundary ledger), Lean 4.33.0; covers finite algebra only.
- Appendix C ideas held: "Spinor cascade and Clifford layers"; "Kelvin's vortex atoms ... no physical map"; "Pressure, volume and principal angles as the modern elemental angle"; "dual layered Smith volume" per-layer records.
- Appendix D test ledger: all kills/passes listed (see sec 8-16 notes). Verdict notes: "Alkali first step < 6/6 ... 6/6 passed"; "Out-of-period K=6 killed, K=10 passed"; "Depth law killed as universal; holds K<=10"; "Refraction vs reflection passed as registered; trend only"; "H-01 killed"; "P-01 extension killed with corrected lengths; survives with uncorrected"; "NUM-01 killed"; "NUC-01 killed"; "f-block killed"; "SIG-01 survives, thinly"; "TIME-01b real-time run missed by 1.05e-3 as registered, traced to sampling". Ledger item "Nuclear magic ridges 6/6 (measured), 5/6 (with extrapolated) passed; reproduction".
- Appendix E cites Lyu, Keitel, Harman arXiv:2504.11237; Sato et al. Nature 2015 (Lr); Guo et al. arXiv:2107.02164 (Og), 2509.05509 (E119); Mewes 2019; Pershina 2008; Cakirli & Casten PRL 96 (2006) 132501 (delta V_pn; N_pN_n Casten).
- Element-specific results recorded in v0.6 (summary for table): Cu, Ag, Au, Pt (Sec 7); alkalis Li, Na, K, Rb, Cs, Fr (tau_1 from sec 8.6; Na Gamma 0.9938 at ten steps); noble gases He, Ne, Ar, Kr, Xe, Rn; H, D (H-, D-); Ps-; Be (correlation hole); Zr, Sc (line tables); Ca (absent from Morton); Hf, Ta (depth misses); Re, Os, Ir, Pt, Au, Hg (K=5,6 depth misses); Og (Z=118); element 119; Lr (Z=103); Cr, Mg, Ca, K, Ar (nuclear N=28/N=20/N=34 entries); oganesson and element 119 new-elements entries.
- Non-element but wall-relevant: sqrt(2)-abscissa x=sqrt2 (Sec 5.9); the Lorentz factor gamma = cosh(tau/2) (Cor. 15.3); radar ratio k = sqrt(z_k) (Sec 15.2). No Gamma^2 = 1/2 wall, no z = 3+2sqrt2 (= 5.828) appears in v0.6 text read so far. Check later: search for "5.83", "3+2", "Gamma^2", "1/2" in v0.7 / v0.8 with grep.

## v0.6 SUMMARY
- Sections 1-18, Appendices A-F; 3,657 lines extracted, ~112K characters read in full.
- Strongest element results: (1) alkali/noble shape and polarizability split (Run 01 0.95 vs 0.51 K=10; Run 02 0/9; ln alpha = 10.28 - 3.04 ln IE1); (2) Period-6 K=10 17/18 median under NIST uncertainty; (3) Og tau_1 = 0.600 with noble band numbers; (4) H-/D-/Ps- tau 2.892 / 3.036 with specific mass shift 1.55(62) cm^-1 residual; (5) Li tau_1 = 2.641 from exclusion.

Next: v0.7 html (3928 lines) from line 1.

## v0.7 html notes, lines 1-950 (read in full; file lines = extracted text)
- Header: "Draft v0.7 -- 24 September 2026". Same section structure as v0.6 (Parts I-IV, Appendices A-F).
- CHANGES vs v0.6 in this chunk:
  - Abstract adds: "all 15 experiment-based gold datasets ... rise before they fall at 450 nm and none does at 650 nm (two show rises below 1e-3 at 550 nm)"; real films 4-117 nm; "both registered expectations of that test failed" (THIN-01).
  - Abstract adds CIE metamer: same gold separates two spectra the CIE observer matches exactly, Delta E*_ab = 8.6 after reflection; top singular vector of CMP separates 3.5 times the four-band difference.
  - Sec 4 (Be): v0.7 says the 2 Angstrom / 4-5 Angstrom hole is the spin-INTEGRATED solid exchange-correlation hole, "not the isolated same-spin hole written above" (correction vs v0.6).
  - Sec 6.2 rewritten: Grassmann's laws (Cited Grassmann 1853); surviving-match theorem with four equivalences (ker C subset ker CM; CMP=0; CM = TC); proof in Appendix A.13 (new).
  - Gold metamer: four Gaussian bands at 430, 510, 580, 650 nm (width 12 nm), amplitudes 0.5 +- null direction, max 0.95. CIELAB delta E*_ab = 8.60 (delta E00 = 8.27) after gold, vs 1e-13 before. Across 14 experiment-based gold datasets 7.4-9.2; EELS-derived 3.0 [post-hoc].
  - Choosing strongest pair: sigma_max(CMP) = 5.38e-3; sigma_2 = 1.19e-3 per unit 2-norm; published four-band pair reaches 43% of sigma_max; on flat 0.5 baseline singular-vector pair gives Delta E*_ab = 18.4 (delta E00 15.6) vs 5.3 for four-band, about 3.5x; XYZ 0.040 vs 0.0116. Neutral filter M=cI negative control. Cited Bujack et al 2022 (colour distance not Riemannian).
  - Sec 6.4 calibration: "6 of 12 bump: Cu 450 and 550, Au 450, Pt at all three" (same as v0.6). Generalization 171 cases; threshold 0.918-0.926 at 99.4% (Zn at 650 nm on ns=2 the miss; bump at 0.935). Gamma radius bumps 0.926-0.935 band.
  - THIN-01 real films (NEW, Sec 6.4 after Fig 2): registered set of gold films 3.96-117 nm from Lemarchand; Yakubovsky 2017, 2019; Rosenblatt 2020; two 35 nm films from Ciesielski 2018 reported post-run. Continuous films 21-117 nm: model median miss 0.010; same side of bulk 11 of 15, registered kill (13 of 15) TRIGGERED. Percolation range 3.96-9 nm: median miss 0.014 (1.3 times thick-film miss; registered expectation of more than twice FAILED). Films 11 and 11.7 nm: median 0.014, same side 6 of 6. Two 35 nm films: misses 0.02-0.07; same side 5 of 6.
  - Labels survive (post-hoc): 15 gold datasets rise before they fall at 450 nm by 0.0185-0.035 (EELS by 0.001); none at 650 nm; at 550 nm two rises 2e-5 and 2e-4.
  - Every rise-before-fall maximum among 171 cases lies between 25 and 108 nm.
  - Cautions: thin-film constants extracted with homogeneous-layer model (circular); Hovel, Gompf & Dressel 2010 (percolation), Kossoy 2015 (interface layers).
  - Gold bulk reflectance at 550 nm spans 0.79-0.85 across seven datasets, "three times the 0.0185 rise of gold at 450 nm".
- ELEMENTS in this chunk: Au (gold, Z=79) most; Cu (Z=29), Ag (47), Pt (78), Be (4), Al, Cr, Co, Fe, Ir, Mo, Nb, Ni, Os, Pd, Rh, Ta, Ti, V, W, Zn, Mg, Pb (film set), Au film thickness set; Ag with |Gamma| > 0.99 never bumps.
- No wall at Gamma^2 = 1/2 yet. Sec 6.4: "1-Gamma^2 = t01 t10 is the round trip" unchanged.
- Sec 6.4 claim (v0.7): Au at 450 nm leaves the circle at 41 nm, re-enters at 124 nm (as in v0.6).

Next: v0.7 lines 951-1900.

## v0.7 lines 951-1900 (read in full)
- Content is substantively identical to v0.6 Sec 7-13.2, with figures renumbered (Fig 2 = thinning circle, Fig 3 = film vs gold data, Fig 4 = onion disk, Fig 5 = resolution ladders, Fig 6 = period-6 stages, Fig 7-8 = onion/ridges, Fig 9-10 = polarizability, Fig 11 = 13n pair HOMFLY, Fig 12 = blind pairs split, Fig 13 = signature walls, Fig 14 = witnesses).
- Same numbers as v0.6: Table 2 calibration; Table 3 Run 01 (0.95 vs 0.51 at K=10); depth ladder accuracies; ridge census; NUM-01 0.392 vs 0.267; ln alpha = 10.28 - 3.04 ln IE1, R^2 = 0.906; noble resets; Snell kills; 354 blind pairs; 253 volume-different; 233 of 253 stay blind; 11,283 thin knots; 2,525 thin same-signature pairs; 84 signature-difference pairs; 17,360 walls; 16,656 simple roots; 513 even roots change nothing; 13a_3542 vs mirror 13a_4018 with window t in (0.4388, 0.4609), volumes 22.6445 vs 22.6783; sigma=0 at s=4/5 (t=0.4296), 9/10 (t=0.4665); s=6/7 (t=0.4511) |sigma|=2; 85 signature-separated blind pairs, 30 chirality flips.
- One small wording change in v0.7 sec 8.2 Table 3 caption: "The kill condition was passed; the peel-minus-static intervals exclude zero at K = 6 and 10; the result holds to Z <= 103." (same as v0.6).
- Sec 11.5 v0.7 adds "Every root of odd multiplicity is a wall; a root of even multiplicity may or may not be, and 513 of them change nothing (Figure 13, left)."
- Sec 12 field-loading: same charges; relaxed energies 7.857, 8.272, 8.761 at Q=12,13,14.
- Sec 13.2 same volume pairs as v0.6.
- ELEMENTS in this span: none new beyond v0.6 (Hf, Ta, Re, Os, Ir, Pt, Au, Hg mentioned in depth ladder; alkali tau_1 values; noble gases).
- No Gamma^2=1/2 or 3+2sqrt2 wall in this span.

Next: v0.7 lines 1901-2850.

## v0.7 lines 1901-2900 (read in full)
- Essentially identical to v0.6 Sec 13.2-16 (same numbers: colour J3 Vol fit 3.25 ln(...+36.97) - 1.72; offset-free 2.979 ln|J3| - 0.658 (205 knots, 4.9%); 60 unseen 11-crossing 2.85%, 40 unseen 12-crossing 2.94%; K11a196/K11a216 17.2855/17.2795; K11n4/K11n21 12.5531/12.4680; A-polynomial figure-eight 2.0298832128193074; 5_2 2.82812208843 vs 2.82812208833; P1(3_1) = -t^-2 (t^2+1)(t-1)^2; 13a window walls alpha = 0.10971, 0.11522; theta/2pi = -0.0145345761398 (13a_3542), -0.0171688847270 (13a_4018), mirror +0.0171688847270; rates -4.6 vs -6.3).
- Sec 14: Du et al. (Nature Chemistry 2026) polystyrene eta ratios 0.48, 0.66; Tg 93.0, 99.3, 101.5 C; Couto et al JACS 2025 C117H136N9O6 -> C117H130N3O6.
- Sec 15.2: radar reading, Bondi k = sqrt(z_k); sodium ten steps Gamma = 0.9938, hyperbolic distance 5.77 (same as v0.6). Cor 15.3: 1 - Gamma^2 = sech^2(tau/2) = 1/gamma^2 (RAPIDITY/LORENTZ CONNECTION, unchanged).
- Test H-01 killed again: |Gamma| 0.994 (0.959-0.977) vs |1-Gamma^2| 0.778 (0.743). Al, Mo, Ta, Zn, Mg, Pb echo weights 0.57-0.87 overlap bump range 0.54-0.865.
- Sec 15.2 order of peeling; ladders 1,2,6 and 1,3,6 share tanh(1/2 ln 6) (same).
- Sec 15.3 ELEMENTS (same as v0.6): H- tau 2.89134 (inf), D- 2.89180(10), H- 2.89206(2), Ps- 3.0361 theory, 3.0355(4) measured; deuteron shift -2.6(1.0)e-4; isotope shift 3.21(62) cm^-1 with normal mass shift 1.66 and residual 1.55(62); He tau 0.7945; Li tau_1 = ln(75.64/5.39) = 2.641.
- Sec 15.4 (same): magic-number mean prominence values; N=20 gone at Mg; N=34 only in Ca; N=28 0.40-0.42 (Ar, K, Ca) to 0.19 at Cr; NUC-01 0.65 vs Casten 0.83 (434 nuclei; FRDM2012 beta_2).
- Sec 15.5 (same): Hopf link 8 pi; trefoil 32.7436; 4_1 40.0122; ratio table identical; uncorrected 2.4 sigma; corrected 3.1 sigma; "With every quoted error combined, the deviation is 2.8σ" (corrected).
- Sec 15.6-15.8 (same). Sec 15.9 same: Og IP1 8.888, IP2 16.195, tau_1 0.600; Ne 0.642, Ar 0.561, Kr 0.554, Xe 0.548, Rn 0.569; Og polarizability ~58 au vs Rn 35; E119 IP1 4.784 eV; Lr IP1 4.96 eV; f-block killed 2-3 of 14.
- Sec 16 common pattern (same wording as v0.6).
- NEW? "Sec 16 Five findings hold on both sides. Records are vectors... On polymers, one topology change moves viscosity but not absorption." Same as v0.6.
- No wall at Gamma^2 = 1/2 or 3+2sqrt2 in this span.

Next: v0.7 lines 2901-3928 (end).

## v0.7 lines 2901-3928 (read in full) -- v0.7 COMPLETE
- Changes vs v0.6 in this span:
  - Sec 16 same. Sec 17 "Measured film curves" expanded: needs continuous films 20-200 nm with independent thickness/constants; 5-10 nm films need continuity checks (sheet resistance, imaging); ellipsometric phase test of front-surface circle.
  - Sec 17 NEW item: "The post-gold metamer, measured." Published pair vs singular-vector pair measured after characterized gold, neutral-filter control; blinded observer trial stated as separate.
  - Sec 18 adds: "No colour distance on a first record can restore what that record discarded."; "Gold samples differ in bulk reflectance by more than a film's rise above bulk."
  - Appendix A.13 (NEW): surviving matches proof. (1)<=>(2): CM(rho1-rho2)=0; (2)<=>(3) P maps onto ker C; (3)=>(4) with C^+ = C^T (CC^T)^-1, CM = (CMC^+) C, T = CMC^+; (4)=>(2) trivially.
  - Appendix D ledger adds: THIN-01 registered 12:16Z; Gold metamer CIELAB (model target); singular-vector test pair (design tool); THIN-01 continuous films "same side of bulk < 13/15 ... 11/15 ... killed"; THIN-01 percolation "1.3x (relative 12% vs 1.6%, post-hoc) killed"; "Gold labels, all local datasets (post-hoc) rise at 450 nm in 15 of 15; none at 650; two rises below 1e-3 at 550".
  - Appendix E adds: Grassmann 1853 (Ann Phys 165, 69), Bujack et al PNAS 2022 (non-Riemannian perceptual color), Hovel/Gompf/Dressel 2010, Kossoy 2015 (arXiv:1409.7338), gold optical constant sources: Olmon 2012, McPeak 2015, Babar & Weaver 2015, Werner 2009, Yakubovsky 2017/2019, Rosenblatt 2020, Lemarchand, Ciesielski 2018, Hagemann 1975, Magnozzi 2019.
  - Appendix F adds "Running the scripts ... relocation_test_output.txt" and colour/real-film scripts: metamer_check.py, bump_location.py, thin01.py (with PREREG_THIN_01.md), thin01_descriptive.py, thin01_complete.py, fig_metamer_design.py, fig_thin01.py.
- ELEMENTS in this span: Au (ledger), Be, Ni, Ti... none new numeric; He, Li, H-/D-/Ps- (Sec 15.3 table repeated), Mg (N=20 gone at Mg), Ca (N=34 only in Ca; K, Ar, Cr for N=28), Og, E119, Lr; noble gases; "Ps-"; Rn 35 a.u.
- Lorentz/rapidity: unchanged (Cor 15.3 sech^2(tau/2) = 1/gamma^2; radar/Bondi sqrt(z_k)). Contradiction-check: nothing here contradicts the frame; v0.7 still has no wall at Gamma^2=1/2 or z=3+2sqrt2.
- v0.7 SUMMARY: same five headline results as v0.6 plus the gold metamer (sigma_max 5.38e-3; 3.5x), THIN-01 real-film test (the "rise-before-fall" label not validated on real films: continuous-film side-of-bulk 11/15 vs registered 13/15 killed), and the H-01 kill (0.743 vs 0.96-0.98).

Next: v0.7.1 research revision PDF (pdftotext, 151,724 chars, 29 pages): /home/claude/sm/votkp_reads/src/A4/v071.txt

## v0.7.1 research revision PDF (pdftotext -layout; 51 pages; 2,426 lines) -- lines 1-700 read in full
- Title block: "Research revision v0.7.1 -- 24 September 2026 -- editorial corrections to Claude's v0.7, written from Jeromie Beasley's research programme". Revision note (p.1-2 abstract area): "This edition corrects how the existing uncertainty simulation, model-derived film labels, and oscillator-strength comparison are described. It introduces no new experiment, data, result, or claim of experimental validation. The v0.7 source and all recorded failed checks remain available in the supplement; this edition requires the author's review before public release."
- CORRECTIONS vs v0.7 (wording changed, numbers unchanged):
  - Abstract item 2, film bullet: the 0.92 radius "was selected after seeing the results" for the 171 computed homogeneous-film cases (v0.7 presented it as a threshold); "96-98% in a subsequent leave-one-metal-out threshold exercise"; "these are model labels, not measured reflectance curves".
  - Abstract: "models using each of 15 experiment-based gold optical-constant datasets predict a rise before a fall at 450 nm and none at 650 nm ... these datasets do not contain 15 directly measured reflectance-versus-thickness curves." (v0.7: "all 15 experiment-based gold datasets ... rise before they fall").
  - Abstract item 3, atoms: "of the 198 ionization stages used, 109 are theoretical, 46 semi-empirical and 43 measured" (v0.7 gave measured/semi/theor in other order). "In 500 independent Gaussian perturbations at the quoted standard deviations, with 14 unstated uncertainties fixed, the median is 17 of 18; correlations and systematic errors were not modelled."
  - Sec 4 Be: unchanged from v0.7 (spin-integrated).
  - Sec 5.8: fractions shown as sigma-ish; same numbers.
  - Sec 6.4 "Tests": the first-order echo statement; "consistent with the first-order term reproducing all 171 labels, a result found after the run" retained; the calibration "6 of 12 bump" retained.
  - Sec 6.4 "One radius cannot decide": "With a=1/2, the echo x=1/5 gives R=49/121 > 1/4 and x=-1/5 gives R=1/9 < 1/4" (same).
  - Sec 6.4 real films: "Continuous films (21-117 nm) ... the registered kill (13 of 15) triggered"; "a reading made after the run explains them" (retained).
  - Sec 6.4 labels: "Optical constants in all 15 gold datasets ... rise before they fall" (renamed from "The labels survive (post-hoc)" to "The model labels survive (post-hoc)"). Figure 3 caption: "Model calculations using optical constants measured on real gold films; points are computed reflectances, not direct reflectance-versus-thickness measurements." (v0.7: "Points: each measured film computed...").
  - Sec 7 Calibration table reformatted.
  - Sec 8.1: Figure 4 caption: "The dashed circle |Gamma| ~ 0.92 is a threshold selected after the model run" (v0.7: "marks the threshold").
  - Sec 8.2 Robustness: "In 500 sensitivity draws, each tabulated energy with a quoted uncertainty was independently perturbed by a Gaussian ... These draws do not account for correlated theoretical errors or establish coverage of a joint confidence region." NEW sentence: "The atomic-number-only 0.00 baseline is weak for this group split: adjacent numbers typically occupy different groups; static features remain the more relevant control." (NEW).
  - Sec 8.3 depth ladder: same numbers. Figure 5 caption same.
- CONTENT UNCHANGED in Sec 1-8.3 vs v0.7.
- ELEMENTS (this span): Cu, Ag, Au, Pt calibration; Be; Re, Os, Ir, Pt, Au, Hg (K=5,6 misses); Os, Ir, Pt, Au (K=7); Hf, Ta (beyond K=10); period-6 (18 elements); alkali first step.
- Lorentz/rapidity, wall, Gamma^2 = 1/2: not yet seen in this span.

Next: v0.7.1 lines 701-1400.

## v0.7.1 lines 701-1450 (read in full)
- CORRECTIONS vs v0.7 in this span (important):
  - Sec 8.5 NUM-01 (v0.7 said "The level is the denominator"): v0.7.1 REWRITES this: "Energy scales and oscillator strengths (NUM-01, pre-registered). ... with actual excitation energies Delta E_n in the denominators and oscillator strengths f_n in the numerators. First ionization energy IE1 is a separate predictive feature, not a denominator in this sum." The v0.6/v0.7 claim that IE1 IS the denominator is withdrawn.
  - Sec 8.5 new limitation bullets: "A complete sum also requires states and continuum contributions beyond a resonance-line list." and "The observed relation between IE1 and polarizability is consistent with shared atomic energy and size scales; this incomplete line list does not establish that IE1 tracks a dominant transition, or that oscillator strengths are unimportant (Figure 10)." (v0.7: "The level carries the response because it tracks the dominant excitation energy" -- WITHDRAWN.)
  - Sec 8.3 DATA-01 perturbation wording changed to "Under 500 independent Gaussian per-stage perturbations ... (14 unquoted uncertainties held fixed)"; "This independent-draw sensitivity check does not include correlated or systematic errors in the estimated stages."
  - Sec 8.2 Robustness: "These draws do not account for correlated theoretical errors or establish coverage of a joint confidence region."
  - Sec 8.2: NEW sentence "The atomic-number-only 0.00 baseline is weak for this group split: adjacent numbers typically occupy different groups; static features remain the more relevant control."
  - Sec 8.4 ridge census: same numbers; closure-60 sentence unchanged.
  - Sec 8.4 Figure 8 caption: unchanged.
  - Sec 13.1 "Torus knots... SnapPy returns 0 for 3_1, 5_1, 8_19" unchanged.
  - Sec 13.4: "(Figure 5, right)" retained though v0.7.1 numbering.
  - Sec 14: unchanged; Du et al; Couto et al.
  - Sec 13.5: 3 knot factorizations unchanged; "Meeting L=1 is therefore not by itself a wall."
  - Sec 11.5 Torus maxima: "At 12 crossings, which has none, 34 knots tie at 8." unchanged.
- ELEMENT results in this span: Re, Os, Ir, Pt, Au, Hg; Os, Ir, Pt, Au; Hf, Ta; Li 2.641, Na 2.219, K 1.986, Rb 1.877, Cs 1.783, Fr 1.705 (tau_1 values); Zr (2% line), Sc (121%); Ca absent from Morton; Ne, Kr (covalent radius fails); Be 2 A.
- Lorentz/rapidity: unchanged (Thm 15.1 Gamma as velocity; tau/2 rapidity; Cor 15.3 sech^2 = 1/gamma^2, gamma = cosh(tau/2)).
- No wall at Gamma^2 = 1/2 / z = 3+2sqrt2 in this span.

Next: v0.7.1 lines 1451-2426 (end).

## v0.7.1 lines 1451-1950 (read in full)
- Sec 15.2-15.9 identical in substance to v0.7 (radar reading; H-01 kill; order of peeling; film stack 0.509 vs 0.433, peak 0.16; matter wave r = -tanh(tau/2)).
- Sec 15.3 table identical to v0.6/v0.7 (H- 2.89134/2.89180(10)/2.89206(2); Ps- 3.0361 theory, 3.0355(4) measured; deuteron -2.6(1.0)e-4; isotope shift 3.21(62); normal mass shift 1.66; residual 1.55(62); He 0.7945; Li 2.641).
- Sec 15.4 magic-number table identical; NUC-01 0.65 vs 0.83.
- Sec 15.5 identical (Lambda = 65.16 +- 0.61 MeV; ratio table 1.390(37) / 1.303 (-2.4 sigma) / 1.275 (-3.1 sigma); 1.504(43) / 1.592 (+2.1) / 1.557 (+1.2)). Text: "With every quoted error combined, the deviation is 2.8σ."
- Sec 15.9 identical (Og 8.888/16.195; tau_1 0.600; noble band Ne 0.642, Ar 0.561, Kr 0.554, Xe 0.548, Rn 0.569; Og polarizability ~58 a.u. vs Rn 35; E119 IP1 4.784; Lr 4.96 eV; f-block killed 2-3 of 14).
- Sec 16 "Five findings" identical in substance.
- Sec 17 open problems: "Measured film curves" bullet now says "with the 0.92 threshold and the bump definition frozen beforehand" (v0.7.1 retains v0.7 expanded version). Post-gold metamer test retained.
- Sec 18 negative controls: 26 items (same as v0.7 incl. colour distance and gold samples; numbered).
- Lorentz/rapidity connections retained: "Each peel ratio is the frequency ratio of a radar echo from a mirror moving at Gamma_k c"; "Bondi's factor is k = e^{tau/2} = sqrt(z_k)"; "1 - Gamma^2 = sech^2(tau/2) = 1/gamma^2".
- No Gamma^2 = 1/2 wall; no 3+2sqrt2 in this span.

Next: v0.7.1 lines 1951-2426 (Appendix A-F).

## v0.7.1 lines 1951-2426 (read in full) -- v0.7.1 COMPLETE
- Page count correction: pdfinfo reports 51 pages for v0.7.1 (the earlier "29" was a wrong header read). v0.8 pdfinfo: 59 pages.
- Appendix A.1-A.13 identical to v0.7 (A.13 surviving matches present).
- Appendix B Lean checkpoint identical (49 declarations; 30/14/5; Lean 4.33.0).
- Appendix C identical (spinor cascade; Kelvin; elemental angle; d/f rank; boundary offset; nonlinear response; refraction with relativistic orbitals; dual layered Smith volume).
- Appendix D ledger identical to v0.7 in substance (THIN-01 registered 12:16Z; kill outcomes). One change: NUM-01 "killed" row now reads "0.392 vs 0.267 (final parse; two parser corrections, same verdict, in NUM_01_RESULTS)". Same as v0.7.
- Appendix E identical to v0.7 (literature list including Grassmann, Bujack, Hovel, Kossoy, gold constants).
- Appendix F identical to v0.7 plus "Running the scripts ... relocation_test_output.txt".
- Closing line (v0.7.1): "Research revision v0.7.1, editorially corrected from Claude's v0.7 ... No new experiment or verification is claimed for this revision."

### v0.7.1 SUMMARY
- Versus v0.7 the substantive edits are: (a) NUM-01 denominator claim WITHDRAWN (IE1 is now "a separate predictive feature, not a denominator"); (b) the 0.92 Smith radius is labelled as selected after seeing the results (model labels, not measured); (c) the "15 gold datasets rise before they fall" is recast as model predictions from 15 optical-constant datasets, not 15 measured curves; (d) the DATA-01 sensitivity draws are described as independent-Gaussian only (no correlations/systematics); (e) new sentence that the atomic-number-only 0.00 baseline is weak; (f) explicit "requires the author's review before public release" revision note.
- Numbers, theorems, ledger and element table otherwise unchanged from v0.7.
- Headline element results (v0.7.1): Au/Cu/Ag/Pt calibration (R450/550/650); Li (2.641), Na (ten steps to IE11, Gamma 0.9938, distance 5.77), H-/D-/Ps- tau 2.892 / 3.036; Og tau_1 0.600; period-6 17/18 median; Re/Os/Ir/Pt/Au/Hg depth misses.

Next: v0.8 PDF (59 pages; 2,678 lines of text, 175,931 chars) at /home/claude/sm/votkp_reads/src/A4/v08.txt.

## v0.8 PDF (59 pages) lines 1-480 (read in full)
- Title: "Draft v0.8 -- 24 September 2026 -- Claude's version". NOTE: v0.8 DROPS the "Research revision" / editorial-correction framing and the revision note of v0.7.1.
- ABSTRACT now says "Six results organize the answer" (v0.7/v0.7.1: five). NEW item 6 "Rows and columns."
- Abstract item 2 (film bullets): v0.8 REVERTS to the v0.7 wording: "all 15 experiment-based gold datasets available rise before they fall at 450 nm and none does at 650 nm (two show rises below 1e-3 at 550 nm), although gold samples differ in bulk reflectance by more than the rise itself; computing real films ... both registered expectations of that test failed." The v0.7.1 correction ("these datasets do not contain 15 measured curves"; "selected after seeing the results") is GONE in v0.8 abstract. Also v0.8 abstract: "across those cases a single Smith radius near |Gamma| ~ 0.92 separates the two regimes ... 99.4% in sample ... 96-98% when each metal's threshold is set without that metal". (v0.7.1 had 'selected after seeing the results'.)
- Abstract item 3: v0.8 restores "most of which are theoretical or semi-empirical for these ions; within the stated uncertainties the median is 17 of 18." (v0.7.1's 500-draw/correlation caveat is GONE from abstract.)
- NEW ITEM 6 (Abstract, "Rows and columns"), claims:
  - "Each peel step splits exactly into a screening part and a shell part. At a shell wall the shell part depends on the principal quantum number alone, Gamma_sh = (2n-1)/(n^2 + (n-1)^2): 3/5, 5/13, 7/25, ... The shell part alone accounts for 75% of the variance of the step to Z = 86 (exploratory) and 85% in NIST's mostly theoretical values for Z = 87-110 (registered). The screening step is not one quantum."
    - Derived check (my arithmetic): n=2 -> 3/5; n=3 -> 5/13; n=4 -> 7/25. These are the (2n-1)/(n^2+(n-1)^2) values; the denominators n^2+(n-1)^2 = 5, 13, 25 and numerators 3, 5, 7 (the odd numbers). Note that the numerators and denominators form the Pythagorean triples (3,4,5), (5,12,13), (7,24,25), so Gamma_sh = (2n-1)/hyp. This is a NEW "wall-like" constant in the Smith coordinate, not present in v0.6-v0.7.1.
  - "Down a column, a line in ln IE against period predicts the measured period-6 stages to a median 7.5%. It misses Ir, Au, Os and Hg by 18-21% and francium and radium by 0.55 and 0.99 eV, and it falls 1.6-2.1 eV below relativistic calculations for elements 119 and 120."
  - "A fixed octave of eight (Newlands 1865) fails beyond calcium; Russell's octaves (1926) are the rows of the table relabelled."
  - "In the atomization enthalpy of a long row, one wave per row has 2.2 times the median error of a main-group octave plus a transition-metal insert (130 against 59 kJ/mol). The octave-plus-insert model in turn loses to interpolation between neighbours. The two heights move in opposite directions down the table."
  - "After the fact, the octave's fitted height is about a third of the free atom's swing from alkali metal to noble gas in every row (3% spread). This is a candidate relation between a row's two ends and its interior. Carried to melting point and stiffness it fails, and it has not been tested independently."
- Sec 1-3: identical to v0.7.1 in content. Sec 3 Table 1 unchanged (later transmission T(1) "0 against 4/5").
- Sec 4: identical to v0.7 / v0.7.1 (spin-integrated Be hole; quantum metric; Theorem 4.1 same).
- Sec 5: identical; 5.9 unchanged (T_s(0)=T_s(sqrt2)=1/2; records (1/2, 1/5); Delta/2 = 0.0995; 2/5 for second record).
- Sec 6.1-6.2 identical to v0.7.1 (gold metamer; surviving-matches theorem; singular-vector pair).
- Sec 6.4 identical to v0.7 (Theorem 6.1; calibration; generalization; threshold 0.918-0.926; 99.4%). NOTE: the v0.7.1 wording "selected after the model run" is absent in v0.8.
- Element/number results in this span: Be (2 A, 4-5 A); Cu, Ag, Au, Pt; Al, Be, Cr, Co, Fe, Ir, Mo, Nb, Ni, Os, Pd, Rh, Ta, Ti, V, W, Zn, Mg, Pb (film metals); Zn at 650 nm miss.
- NEW elements named in v0.8 Sec 6 abstract "Rows and columns": Ir, Au, Os, Hg (period-6 stage misses 18-21%); francium and radium (0.55 and 0.99 eV); elements 119 and 120 (1.6-2.1 eV below relativistic calcs); calcium (octave fails beyond Ca).

Next: v0.8 lines 481-1100.

## v0.8 lines 481-960 (read in full)
- Sec 6.4 tail: v0.8 film text = v0.7 wording ("a reading made after the run explains them"; "(post-hoc)"). Figure 3 caption: v0.8 = v0.7 wording ("Points: each measured film computed with its own constants"). v0.7.1 "model labels" wording GONE.
- Sec 7 calibration table identical numbers (Cu 7.726380, 101.67 k=11, R 0.538/0.624/0.935; Ag 7.576234, 83.46 k=11, 0.980/0.983/0.990; Au 9.225554, 79.80 k=11, 0.408/0.792/0.957; Pt 8.95883, 75.5 k=10, 0.588/0.641/0.678).
- Sec 8.1 identical; Sec 8.2 robustness: v0.8 drops the v0.7.1 "independent Gaussian / correlations not modelled" caveats (text back to v0.7 "Drawing every energy within NIST's stated uncertainty (500 draws ...)").
- Sec 8.3 identical numbers; Sec 8.4 ridge census identical PLUS NEW paragraph: "Janet's closures carry no ridge [Exact, RHYTHM-20 T06; killed for Janet]. Janet's left-step table ends its periods at the alkaline earths. At those electron counts (4, 12, 20, 38, 56) the mean of the per-closure median ridges is 0.004, against 0.477 at the noble-gas counts 2, 10, 18, 36 and 54."
- Sec 8.5 NUM-01 REVERTED: v0.8 says AGAIN "The level is the denominator (NUM-01, pre-registered) [Exact]. ... with the excitation energy Delta E_n as denominator" and "The level carries the response because it tracks the dominant excitation energy (Figure 10)." (v0.7.1 correction WITHDRAWN in v0.8; this is a regression to the v0.7 framing.)
- Sec 8.5 NEW subsection "In the solid [Exact, RHYTHM-20, pre-registered]": data pymatgen 2024.8.9 element table, mendeleev 1.3.0 radii; Resistivity: shape 0.970 vs level 0.709 (T11 killed; family average 0.423 best); Molar volume: shape 0.231 vs level 0.414 (T12 passed; family average 0.220); Bond size: Apline in ln IE1 predicts metallic/covalent radii 0.087 and 0.104 vs hydrogen-like rh = n Ry/IE1 0.164 and 0.220 (T13 killed); Stiffness: nine group 1-2 metals, slope 1.31 in ln B vs ln(valence electrons/molar volume) (registered 1.2-2.2; free electron 5/3; T14 passed); Surface: |Gamma(550 nm)| of 34 elemental metals (23 of Figure 4 + 11) from refractiveindex.info: solid valence density median error 0.0855 vs atom level 0.0993 (T15 passed); without Werner files 0.0807 vs 0.0871 (post-hoc); One key (n, Zeff) beats level and family only on metallic radius (T20 killed, 1 of 4). Family average reported without pass/kill condition "and the exploratory look had anticipated it" (admission).
- Sec 8.6 resets table identical.
- Sec 8.7 NEW SECTION "The step splits into a shell wall and a screening step":
  - Hydrogen-like form: IE_k = Ry Zeff,k^2 / n_k^2; Zeff,k = n_k sqrt(IE_k / Ry) read from data.
  - Theorem 8.2: tau_k = 2 Delta ln Zeff - 2 Delta ln n; Gamma_k = Gamma^scr_k (+) Gamma^sh_k with Gamma^scr = tanh(Delta ln Zeff), Gamma^sh = tanh(-Delta ln n). Inside a shell Gamma^sh = 0.
  - At a shell wall: Gamma^sh = (n^2 - (n-1)^2)/(n^2 + (n-1)^2) = (2n-1)/(n^2 + (n-1)^2) = 3/5, 5/13, 7/25, 9/41, 11/61, 13/85 for n = 2..7. Text: "These are the odd leg over the hypotenuse of the Pythagorean triples 2n-1, 2n(n-1), n^2+(n-1)^2. ... Euclid's: tanh ln(p/q) = (p^2-q^2)/(p^2+q^2) ... So the triples carry no physics beyond the hydrogen-like ratio (n/(n-1))^2." Proof: at a wall z = (n/(n-1))^2 and Gamma^sh = (z-1)/(z+1).
  - Checked "on all 5,714 NIST steps to Z = 110. It holds to 4e-16 ... [Exact, split_theorem_check.py]. In one step (gadolinium, stage 14) n changes by other than 0 or -1."
  - Lithium first step: "the wall Gamma_1 = 0.867 is 3/5 (+) 0.556" (v0.8 text: "35 ⊕ 0.556"). (Note: 0.867 for Li is the alkali first step value.)
  - Shell-share: 75% variance of tau over 3,655 steps Z<=86 (exploratory, before registration); 85% over 2,059 steps Z=87-110 (T01 passed); for Z>=87 96% of stage values theoretical.
  - Screening not one quantum: median within-shell step in Zeff over first three removals by period 0.85, 0.92, 1.22, 1.33, 1.62 (T02 killed at max/min 1.90); Zeff/n step falls 0.46 -> 0.30 (post-hoc); Slater same-shell constant comparison: median 1.16 vs 0.70 registered (T09 killed).
  - Madelung anomalies (Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, Pt, Au): mean tau1 0.854 vs 0.713 for other d-block periods 4-6 (T17 passed); La normal group; with Lu 0.726 still passes.
  - Half-filled p-shell dip (N above O): holds periods 2-4, not 5-6 (T19 killed, 3 of 5); post-hoc IE1(p3) - IE1(p4) = 0.916, 0.127, 0.036, -0.401, -1.133 eV.
- Sec 8.8 (partial, to line 960): column rhythm: line in ln IE vs period fitted on periods 3-5 predicts 32 measured period-6 stages (k=1-3) median 7.5% (T03 passed). Breaks: 5d metals: at first stage misses Ir, Au, Os, Hg by 18-21%; registered trio Pt 1.5%, Au 19.5%, Hg 17.5% mean 2.28x median miss of others (T04 killed). Francium misses 0.55 eV; radium 0.99 eV (fitted on periods 2-6, T05 killed). Group 1 falls Li 5.392 -> Cs 3.894 eV, rises to Fr 4.073. Group 2 falls to Ba 5.212, rises to Ra 5.278 (post-hoc). Elements 119 (line 3.23 eV vs relativistic 4.784 [arXiv 2509.05509], 1.55 eV below) and 120 (line 3.71 eV vs 5.851 [Borschevsky 2013], 2.14 eV below). "The usual explanation, relativistic contraction of the outer s shell, was not tested here."
- Superheavy families: NN classifier trained on Z<=86 places Rf, Db, Sg, Bh in groups; Hs in group 10 instead of 8; Mt and Ds lack the stages.

### WALL-RELEVANT FINDING (v0.8 sec 8.7) -- important for today's frame
- v0.8 for the first time writes a shell wall as a Pythagorean-type ratio: Gamma_sh(n) = (2n-1)/(n^2+(n-1)^2). Quote: "These are the odd leg over the hypotenuse of the Pythagorean triples 2n - 1, 2n(n-1), n^2 + (n-1)^2."
- Today's frame wall (Gamma^2 = 1/2, z = 3+2sqrt2 = 5.828, Gamma = (z-1)/(z+1) = 0.707 = 1/sqrt2) is NOT among these values: the nearest is n=2 (3/5 = 0.600, z = 4) and n=3 (5/13 = 0.385). No v0.8 value equals 1/sqrt2. Must state: no direct hit. Check later sections.

Next: v0.8 lines 961-1440.

## v0.8 lines 961-1440 (read in full)
- Sec 8.8 end: superheavy NN classifier places Rf, Db, Sg, Bh in groups; Hs in group 10 instead of 8; Mt, Ds lack stages (T16 killed, 4 of 7).
- NEW Sec 8.9 "Octaves: the row as a wave, and two cuts of the onion":
  - Russell's The Universal One (1926): ten octaves of seven tones, master-tone; Table 5 compares: "octave 5 is He-F, octave 6 is Ne-Cl"; hydron (400=) and luminon (403-) do not exist; "unknown element (1001+) preceding radium" = francium (87), identified by Perey in 1939; "fails: molar volume is smallest at the third tone (T2)"; master-tone record "Not supported as registered (T8 killed, 3 of 4)"; "the crest recurs in every row, but the two waves' heights move in opposite directions (T5)". Table 5 basis: first 42% of the text. Meyer 1870 atomic-volume curve; Newlands 1865.
  - Fixed octave of eight places main-group Li..Ca correctly and none after (T07 killed). Nine equal octaves/octaves of eight: ln IE1 errors 0.125 and 0.157 vs 0.052 (T18 killed). Alkali-to-noble IE1 swing falls to about 0.81 of prior row; ratios 0.657, 0.909, 0.823, 0.862 (T08 passed).
  - Atomization enthalpy: crest mid-octave rows 2-3 (C, Si) and first half of TM series rows 4-6 (V, Nb, W) (T1 passed; partly seen before registration; test weak: crest zone holds 13 of 17 elements in rows 4-5). N, O, F, Cl by half bond energy.
  - One wave per row: 130 vs 59 kJ/mol (T4 killed; 2.2x). Friedel 1969 d-band picture.
  - Two heights move opposite: main-group octave falls 521 -> 208 kJ/mol; insert rises 505 -> 865 (T5 passed).
  - Fitted parabola loses to interpolation (T3, T7 killed). Post-hoc: atomization main group 27.5 vs 47.5; insert 91.5 vs 47.7; melting point 244.6 vs 223.3 K and 288.7 vs 180.5 K.
  - Molar volume smallest at third tone (B, Al, Ga, In, Tl); row 2 graphite for C (T2 killed 0 of 5; diamond 1 of 5).
  - CANDIDATE (post-hoc): H_p ~ c (IE1noble - IE1alkali), c = 32.19 kJ mol^-1 eV^-1 (0.334 with H_p in eV per atom). Ratios rows 2-6: 32.2, 32.6, 31.6, 33.3, 30.3; CV 3%; one constant 25.9 vs 27.5 kJ/mol (S3); family average 43.8.
  - Reflection-coordinate rewrite of the swing (v0.8 p.26): "IE1noble - IE1alkali = IE1noble + IE1alkali Gamma_row, Gamma_row = tanh(1/2 ln(IE1noble/IE1alkali))". "This is an identity for any two positive numbers, so it adds no evidence."
    - ARITHMETIC CHECK (done in sandbox): as extracted, the right-hand side IE1noble + IE1alkali*Gamma_row is NOT equal to the left side (test a=2, b=1: LHS 1, RHS 7/3). The correct identity is (IE1noble + IE1alkali)*Gamma_row (test gives 1 = 1). The PDF text layer shows no parentheses; likely a dropped bracket in the typesetting, but as printed the displayed formula is wrong. FLAG to main session: check page image of v0.8 p.26.
  - Other properties: melting point and bulk modulus fail (S1, S2 killed; CV 0.163 and 0.475). Insert ratios 178, 264, 178 vs IE1(group 12) - IE1(group 3) (does not carry). Hydrogen 354 kJ/mol predicted vs 218 tabulated (post-hoc).
  - Row 7: with Og IE1 (Guo et al 2021) forecast main-group height 155 kJ/mol; radium forecast 116 vs tabulated 159 (27% below; registered tolerance 36%; R7). Francium no tabulated value.
  - Prior art: Harrison's tight-binding theory (Harrison 1980) "may already contain the relation. It was not checked."
- NEW "Two cuts of one onion": row's neutral atoms take first steps along diagonal edge; noble gas peeled runs along horizontal; columns = isoelectronic. Second differences of ln IE agree in sign at 3 of 4 all-measured points (T8 killed; 80% needed); post-hoc 18 of 24; misses 4 at O-like position (half-filled dip), 1 at iodine position (+0.001). Helium cannot reach Li to F.
- Sec 9 (Snell): identical to v0.7.1 (turning set 1 hit, 9 false, 5 missed vs 6; 0 of 6; flat deep ridges; 0.61-0.68 vs 0.31-0.46; detrended 0.02-0.03).
- Sec 10: identical; Sec 11.1-11.2: identical numbers (HOMFLY convention; 19 pairs at 13; 12 with Alexander 1; 13n_3871 / 13n_65 figure).
- Sec 11.4: identical numbers (354 blind; 253/20/1,960/183; 101/11/1,125/185; 233 of 253 killed; 11,283 thin; 2,525; 84; 185 HFK). Table numbering shifted (Table 7 = pairs identical through 10).
- Sec 11.5: identical (Table 6 multiplicity; 513 even roots change nothing; torus maxima; 13a_3542 window (0.4388,0.4609), volumes 22.6445/22.6783; s=4/5 t=0.4296; s=9/10 t=0.4665; s=6/7 t=0.4511; 85 blind pairs; 30 flips; 29 with nonzero sigma).
- Sec 12: identical (T(3,4) charges; Sutcliffe 7.857, 8.272, 8.761).
- Sec 13.1-13.3: identical numbers (SnapPy 0 for 3_1, 5_1, 8_19; Table 7 pairs; 285 blind at 11-12; 101 mutants; 124 computable; Hughes 3.25 ln(|J3|+36.97) - 1.72; 1.21% over 177,316 knots; offset-free 2.979 ln|J3| - 0.658, 205 knots, 4.9%; 2.85%, 2.94%).

Next: v0.8 lines 1441-2678 (end).
