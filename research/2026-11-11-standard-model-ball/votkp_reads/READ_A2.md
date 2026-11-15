# READ A2: VOTKP / Elemental Peeling old versions (label A2)

Reader: A2. Date of reading: 11 Nov 2026. Scope: the three assigned Drive files only. Nothing else was edited or pushed. Decoded inputs sit in /home/claude/sm/votkp_reads/src/A2/.

---

## 1. Coverage

| File | Drive id | Version / date (as printed) | Source size | Text read | Read in full |
|---|---|---|---|---|---|
| Elemental_Peeling_Combined.html | 1T_8EQwtFZavtdfGYAV2E8GfGFDir1FAT | "Elemental Peeling: Spacing, Subspace Geometry, and Light-Driven Boundary Memory", dated 8 September 2026, byline "Jeromie N. Beasley" | 2,020,421 bytes | 78,374 characters after stripping script, style, tags and data-URI images (saved as combined.txt, 1,682 lines) | Yes, every line of text (lines 1 to 1682). Embedded raster figures (7 data-URI images) skipped per brief. |
| Elemental_Peeling_Phase_Tests.html | 18jzQdyVw4fPNcPdtC3W7FqU0VDhO9FhK | "Elemental Peeling: Gases, Phases, and Recoverable Measurements", "v3", dated 8 September 2026, no byline printed in the text | 1,076,876 bytes | 55,307 characters after the same stripping (saved as phase.txt, 1,379 lines) | Yes, every line of text. Embedded figures (4 data-URI images) skipped. |
| votkp_drafts_dropped_passages.md | 1bPJ4Y7nlxxmcx1ZJCZP89XWQVFeNBsld | Passages dropped between drafts v0.1 (23 Sep 2026) and v1.0 (25 Sep 2026), absent from Zenodo v1.1; v1.1.1 difference noted | 86,664 bytes | 86,664 characters, 842 lines | Yes, every line. Text from v0.5 onward is PDF-extraction fragments; those fragments are read but flagged as low-reliability below. |

Not read: the embedded images in both HTML files and the figure PNGs named in the dropped-passages file (not in the assigned files). Nothing else.

Byline discrepancy: the brief says the byline is "Jeromie Beasley". The Combined file prints "Jeromie N. Beasley". Flagged for the main session.

Date discrepancy: both HTML files are dated 8 September 2026, earlier than v0.1 (23 Sep) of the dropped-passages file. The two HTML files do not contain the Smith, rapidity or IE-ratio-as-impedance material that the dropped file says was in v0.2 to v0.7. I cannot establish from the files alone whether the HTML files precede or follow that material. Treat the ordering as unresolved.

---

## 2. What each version defines and claims

### 2a. Elemental_Peeling_Combined.html (8 Sep 2026)

Abstract: exclusion-to-boundary chain, with headline results: confined-fermion size law, a fixed-gap Hamiltonian whose subspace rotation changes transition strength, a velocity-memory kernel with "initial strength ζ(0)=2Δg_qq", and a "stricter proposed equality of two light-prepared electronic states" that is not achieved. Also two-nonnegative-spectra metamer separated by gold reflection.

Section by section (headings as printed, no section numbers in this file):

- "The physical question". Organizing principle: exclusion and interactions constrain the arrangement, the arrangement selects subspaces, a physical interface couples them. "Each arrow requires a constitutive or dynamical equation."
- "A spatial consequence of antisymmetry". Eq. (pauli): same-spin pair density n^(2)=n n − |γ|²; vanishes at coincidence; Cauchy–Schwarz gives nonnegativity.
- Proposition 1 (exclusion changes confined size). E_A(L)=cA/L²+PL, L_A³=2cA/P; fermions A_F=5, bosonic pair A_B=2; L_F/L_B=(5/2)^{1/3}.
- "A gas supplies a direct optical benchmark". Structure factor S(x)=3x/4−x³/16 for x≤2; Pauli-suppressed scattering from cited ultracold-atom experiments.
- "From a material operator to moving subspaces". Riesz projector; (Ṗ)_ij=(p_i−p_j)/(λ_i−λ_j)(Ḣ)_ij; g_qq=Σ|⟨j|∂H|i⟩|²/(λ_i−λ_j)²; "Equal gaps can coexist with different matrix elements". Field metric g_E=Σ K_m and polarizability α_s(x)=Σ 2Δ³K/(Δ²−x²). Proposition 2 (silence below the gap): ker α_s=ker g_E for x²<min Δ². Counterexample: tune-out point y=4/3 with g_E=2.
- "The two-sided hypersurface and retained feedback". Schur elimination K_Σ=D−CA^{-1}B−GE^{-1}F, exterior perturbation δK_Σ=GE^{-1}(δE)E^{-1}F. Feedback statement: F=0 iff [H,R]=0 iff B=0 iff K≡0, with ‖F‖²_F=2Tr K(0).
- "The time-domain state that remains". Memory kernel K(t)=Be^{−itD}B†; "The enlarged state evolves without memory in this finite closed model".
- "A complete optical mode includes the outside". Hellmann-type relation ∂β/∂n_o = (k0² n_o/β)∫_outside |u|² dz.
- "One electronic model, optical and electrical probes". Sheet H_θ=a(cosθσ_z+sinθσ_x), gap 2a, dipole d²sin²θ, metric g_θθ=1/4; contacted transmission T(0)=γ²a²sin²θ/(a²+γ²/4)².
- "Light writes a state: a derived geometric memory kernel". Driven H(q,E) with reset-bath Bloch equation, mechanics with ionic potential U(q)=MΩ²q²/2+R(q), energy bookkeeping (optical work, reset heat, mechanical dissipation).
- "The gap and projector metric set the memory amplitude". Proposition 3 (boxed): ζ(t)=2Δg_qq e^{−γt}cos(Δt), g_qq=g²a²/(4R⁴); ζ(0)=2Δg_qq. Real part of the transform nonnegative at every real frequency.
- "Executed pulse and dark-trajectory test". Parameters (a,t0,g,d,M,Ω,κ,γ_e)=(1,0.6,0.35,0.8,12,0.12,0.024,0.55). Bare oscillator error 3.29756e-4; with derived memory 1.37209e-5, factor 24.03.
- "Paired probes and a second interface". Frozen-geometry susceptibility; Airy-type composition of two sheets with return reflections; written state changes reflectance up to 0.007685.
- "Phase transport and the receiving color response". Projector distance ‖P_u−P_v‖²=2sin²ϑ; photon helicity curvature Ω=h sinθ dθ∧dφ; latitude loop phase −2πh cosθ.
- "Color is the response of a specified receiver". Tristimulus map C_j(q); metameric nullspace; example with M=diag(1,1/2,1/4,3/4).
- "A gold surface separates an actual observer equivalence". CIE 1931 2°, D65, four Gaussian bands at 430, 510, 580, 650 nm; Johnson–Christy gold; post-reflection XYZ separation 0.0104183 against threshold 0.001; gray-filter control holds equality.
- "Positive-channel peeling and a four-reading optical test". Proposition 4: β_min L ≼ D ≼ β_max L, ker D = ker L, with β_m=2Δ³/((Δ²−y1)(Δ²−y2)).
- "A scattering subspace and two phase references". S=I−iW†R_E W unitary for real E; K_φ=(2I−e^{−iφ}S−e^{iφ}S†)/4; recovery of A and B from two references; "No absolute phase of an isolated quantum ray is measured by this construction."
- "A present snapshot still requires an evolution law". Side-orbital family with equal Σ(0)=−c but Σ'(0)=−c/λ.
- "Counting cumulants recover a bounded channel family". c1=p1, c2=p1−p2, c3=p1−3p2+2p3; Newton identities; four-channel ambiguity witness z³−1.49z²+0.6451z−0.073549=0.
- "Elemental inputs and experimental response controls". Table of NIST first IE and later jump; R450/R550/R650 for Cu, Ag, Au, Pt.
- "A film peel changes two interfaces". r, t formulas; Au at 450 nm on n_s=1.5: reflectance 0.408191 at 200 nm, peak 0.426742 near 58.2093 nm, 0.163082 at 10 nm.
- "A published phase-sensitive optical-current dataset". Lesko et al. processed data (Floquet TI / light-dressed graphene), held-out interpolation with even/odd phase columns: RMSE 73.2257 to 7.19122, 99.0356% reduction; permutation best 60.5794%. Labelled exploratory, not blind.
- "Execution evidence and formal scope". Compound Eye counts (1,315 requests, 2,448 outputs). Lean: 71 named statements; axioms restricted to propext, Classical.choice, Quot.sound.
- "What the combined construction establishes". "The strongest supported statement is a conditional physical chain."
- "Full guide normalization and mode geometry". Symmetric slab; ∂_{n_o}β=k0²n_o f_o/β; checked β from 1.227328958881 to 1.318814249749.
- "Passivity and a boundary coordinate chart". Schur complement of accretive M is accretive; Cayley S=(Z−I)(Z+I)^{-1}, I−S†S ⪰ 0.
- "Signed changes and retained paths". Finite rational response, pole-count bound; exponential history record τṀ=P−M.
- "Continuum phase, nonlinear response, and failed identifications". Zeta-regularized η(D_a)=1−2a on the circle; raw sign count at a=1/4 is one, eta is one-half; second-harmonic interface response; three controls rejecting overbroad identifications (flatness, neutral Dirac, log|A| at A=0). "No universal element-to-knot table" is used.
- "A gas–metal chart that the controls reject". Rice–Mele gap Δ=2√(v²+(t1−t2)²); census 3,3,2 at v=0.2,0.4,0.8 with r=0.01.
- "Reproducibility and the missing empirical lift". The eight-feature UPG empirical lift and its generator are absent from the recovered material; this blocks one empirical cascade branch.

### 2b. Elemental_Peeling_Phase_Tests.html (8 Sep 2026, "v3")

- "The question to carry forward". Separates changed specimen from retained record; tests whether a pair of records identifies an element, metal or gas.
- "Testing the proposed gas–metal boundary chart". Rice–Mele H(k) with E(k)²=v²+t1²+t2²+2t1t2cos k; offset τ=log det(I−C)−log det C; census N_ε. Predeclared test results in a table (offset agreement passes; census=1 fails at r=0.01 for all three v; resolves at r=0.001 and 0.0001). Endpoint: equal hopping keeps gap 2|v|. Pearson correlations +0.893, +0.946, +0.086 (descriptive only).
- "The authentic angle law survives; census independence does not." Exact relation tanh(τ_{2n+1}(θ)/2)=sinθ·tanh(τ(π/2)/2). Exact one-site witness with f0≥1/√5 gives census 1 and 0 at ε=1/3.
- Proposition (resolution certificate for one dimer mode). If δ=‖P−P0‖, δ²<ε and ε+δ<ν0<1−ε−δ, then N_ε=1. Written proof, no Lean.
- "Endpoint, registration, and limiting order." r=0 vs L≥3 whole dimers; even/odd cut results; at r=1, v=0 census 9, 11, 13, 15 for L=9, 17, 33, 65 at 10⁻⁶.
- "What gases add: density, internal response, and a recovery problem". Four-state dipole model with zero permanent moment, transition-strength rank three, α_ij=2Δd²/(Δ²−ħ²ω²)δ_ij. Dilute susceptibilities at 100 kPa, 300 K from NIST rounded polarizability volumes.
- "Two frequencies recover bound and free weights when the pole is known". χ(y)=B/(p−y)−D/y; inverse formulas (B,D); fixed-pole error bounds |δB|≤4.5η, |δD|≤2.5η.
- "An unknown pole defeats two readings; a third restores this family". Examples with equal χ at y=1 and y=2 and different χ at a third point; three-reading inverse p=(g12 y1−g23 y3)/(g12−g23).
- "A fixed oscillator budget reduces the probe count". Known W=B+D; one-sample and two-sample inverses; two preparations sharing W and χ(1) with different χ(2).
- "A measured gas example: two-color dispersion barometry". Yang, Stone and Egan (2025) table: He, Ne, Ar, N2 values; first-order Δn; "Recovery and its obstruction" with common distortion d; bias −δ/(a2−a1).
- "Quantum geometry and thermopower: the useful continuation". Oh et al. and Oh & Kim references; goldene DFT numbers flagged as failing PF=S²σ check.
- "An exact thermal obstruction: equal conductance, opposite thermopower". Proposition: for every T and every measurable p, ∫p(T+)w_T=∫p(T−)w_T, while S+=−S−<0. Numerical example a=0.2 eV, Γ=0.1 eV, T=300 K: G/G0=0.2209316590271, S=∓63.21177934 µV/K.
- "Electromagnetic records: an obstruction and its recovery". Evanescent TE/TM field pair with equal |E| but opposite normal reactive power; coherency matrix recovered from two intensities plus two complex transverse flux quadratures. Example a=1/√2, b=±i/√2, q=5/3, h=4/3, Re S_y=±10/(3√41).
- "Cold and warm plasma branches". Cold ω_p, warm correction ω²≃ω_p²+3k²v_T².
- "Reproducible status" and "Reproduction, provenance and remaining limits" with a suite table (Rice–Mele 57 groups; gas 741 assertions; budget 211; published gas coefficients; thermal mirror 378 cases; evanescent 29 groups, 1,040 pairs, 600 recoveries, 132 error checks).
- References list (NIST CCCBDB, Yang et al., Oh et al., Kumar et al. goldene, Madsen & Singh BoltzTraP, Ludoph & van Ruitenbeek, Möller et al., Wei et al., Kress, Xu et al., Tonks & Langmuir, Bohm & Gross, Peschel).

### 2c. votkp_drafts_dropped_passages.md (v0.1 to v1.0, 23 to 25 Sep 2026)

Organised below by draft. Each entry: the passage, then its mathematical move.

**v0.1 (23 Sep), passages dropped from the first draft:**

1. VOTKP as a vector, VOTKP(K,Ψ)=(T,L,G,E). Move: a record of four layers with independent variation. Witnesses: Hopf charge and volume splits in Table 1.
2. Peel typology (channel / coordinate / physical) and knot-move classes (Reidemeister, Markov, skein, band, cobordism, Dehn filling). Move: classify peels by what each preserves.
3. Theorem 3.1, finite linear predictive quotient. O v=(Rv,RLv,…,RL^{n−1}v), N=ker O, dim(V/N)=rank O, rank O − rank R extra coordinates. Move: observability quotient as the smallest autonomous summary.
4. Absorption threshold with occupations: n→m absorbs only when ρ_nn>ρ_mm. Move: occupation difference gates the threshold.
5. Conductance as a second-order quantity: A(b)=a1 b+O(b²) with even conductance. Move: parity argument, first-order structure versus even transport.
6. Theorem 4.1 (occupation fixes an effective curvature). U_b=μ_b a²/2+λa⁴/4 with fixed population r; response curvature χ=2c²/δ=8δ g_aa(0); critical occupation r_c where μ_eff=0. Move: occupation as a sign-setting parameter for curvature.
7. Schur boundary memory: Σ(z)=B(zI−D)^{-1}C, bare deletion loses it.
8. Transfer silence: B(zI−D)^{-1}C≡0 iff BD^jC=0 for j<q; sharp by a nilpotent shift (q=5). Move: Cayley–Hamilton reduces the infinite family to q terms.
9. Intensity erases phase: |z+a|²−|z−a|²=4a Re z; worst-case error ε/(√2 a). Move: quadrature recovery from intensity differences.
10. Counting cumulants and Newton identities: three channels recovered; {0.91,0.37,0.08} recovered; {0.2,0.5,0.8} and {0.3,0.845,0.355} share c1 and c2 with c3=0 vs 0.06.
11. Reduced-record impossibility bound, H_s=[[0,1],[1,s]] with a wide-band lead: the record R agrees for s=±1 while later transmissions differ by Δ≈0.19898; minimax error ≥Δ/2≈0.09949. Move: any prediction from R has minimax error at least half the gap.
12. Side-orbital family Σ_λ(E)=cλ/(E−λ): equal Σ(0), unequal Σ'(0)=−c/λ. Move: one-energy snapshots underdetermine derivative.
13. Receiver kernel: ker C ⊆ ker(CM) iff a later linear map preserves equivalences. Move: kernel inclusion as an equivalence criterion. Example with gold.
14. Film thinning is non-monotone: R=0.408191 (200 nm), 0.426742 (58.2093 nm), 0.163082 (10 nm). Move: interference, not monotone decay.
15. Element table of shell steps (Table 2) and IE ratios (Table 3). See Section 3.
16. Peel-shape pilot and Run 01 (see Section 3).
17. Run 02, polarizability: K1 kill condition, K2 six-of-six noble-gas minima.
18. HOMFLY through ten crossings: 250 prime knots and mirrors, no pair equal in Alexander and Jones but different HOMFLY; 24 pairs share Jones and differ in Alexander.
19. Two-variable HOMFLY specialization: Alexander is v=1, z=t^{1/2}−t^{−1/2}; Jones is v=t. Move: one object, two specializations.
20. Torus-link denominator z^p+w^q=0 as T(p,q). Move: Milnor link as the denominator of a rational map.
21. Hopf charge by exact elimination: preimage counts α q+β p (table with T(3,4): 7, 10, 11, 13, 15). Move: degree counted as a resultant degree.
22. Hyperbolic volume separates five pairs with equal HOMFLY, Alexander and Jones (Table 6). 5_1 / 10_132 is the sharpest case.
23. Figure-eight volume two ways: two regular ideal tetrahedra, 2D(e^{iπ/3}); Kashaev limit 2.734, 2.271, 2.106 at N=50, 200, 800.
24. Adjoint Jones (3-colour) at q=e^{8πi/15}: T-A test.
25. CCGLS volume form ω on the A-polynomial curve. Torus control: ω≡0 identically on L=ε M^{−k}. Move: a closed 1-form that vanishes on torus branches.
26. Habiro-type loop expansion: coloured Jones at q=e^{u/N} tends to 1/Δ(e^u)=1.19352357.
27. Polymer topology measurements (Du et al.): viscosity ratios 0.48, 0.66, 0.73; T_g 93.0, 99.3, 101.5 °C. Move: topology moves viscosity but not absorption.
28. Molecular-knot nitrogen deletions (Couto et al.): formula change at fixed knot. Move: composition change with ΔT=0.
29. Field-knot realizations: Hall et al., Chen et al., Kasai et al. Move: loading and topology change together.
30. Physical volume V_phys=∫d³x over the realized field: needs a scale.

**v0.2 (23 Sep):**

31. Peel shape as reflection coordinate. Impedance ratio z_k=IE_{k+1}/IE_k; the peel coordinate is the Smith log-impedance; a first-order echo 2Re[Γ̄(1−Γ²)r12 e^{4πiNd/λ}] predicts reflectance rise in 171 of 171 cases; Smith radius |Γ|≈0.93 separates regimes to 99.4%. Move: identifies IE ratios with a Smith-chart reflection. Theorem 8.1 and Theorem 6.1 (echo expansion).
32. Dimension count: dim V/N=rank O.
33. Colour ladder: 21 pairs blind to ordinary and 3-coloured Jones separated by 4-coloured Jones.
34. A-polynomial returns 4_1 volume to 4×10⁻¹⁶ and 5_2 to 10⁻¹⁰.
35. Coloured Jones via U_q(sl2) R-matrix, framing removed; checks J2,J3,J4(4_1) to 10⁻¹⁴.
36. Census note: HOMFLY unique for 53.7% of knots against 53.4% for Alexander plus Jones through 15 crossings (cited census).

**v0.3 (23 Sep):**

37. Nuclear peel: S_2n(Z,N)=B(Z,N)−B(Z,N−2) with magic-number ridges, pre-registered 6 of 6.
38. Theorem 15.1. A matter wave meeting a potential step reflects with r=(k1−k2)/(k1+k2)=−tanh(τ/2), τ=ln(k2/k1). Light at a metal, an electron leaving an ion and a matter wave at a step share one reflection coordinate.
39. Theorem 15.4 (scale blindness): H_λ unitarily equivalent to λH, so IE ratios are unchanged under all masses scaled by λ. Move: the ratio is a dimensionless invariant.
40. Film stack reflection r_ij=(N_i−N_j)/(N_i+N_j)=tanh(½ ln(N_i/N_j)).
41. H^- / D^- mass-ratio table with infinite-mass energy −0.527751016544 a.u.; glueball tight-knot extension (P-01): 2.4 to 3.1 sigma from lattice on the first ratio.
42. Nuclear shell evolution, N=16, 20, 28, 32, 34 values (Section 3).

**v0.5 to v0.6 (24 Sep):** fragments only (figure labels, a second version of the "dropped" 0.19898 bound, and a Run 01/ Hopf-charge note). No new mathematical move that is not listed above.

**v0.7 (24 Sep), rapidity and Smith passages (strongest for this frame):**

43. Radar reading. Light reflected from a mirror approaching at βc returns at ν(1+β)/(1−β). Setting that ratio to z_k gives β=(z_k−1)/(z_k+1)=Γ_k. Move: IE ratio as a Doppler ratio; Γ_k as the velocity.
44. Rapidity identification. For β=tanh φ, rapidities add. Here τ_k/2 is a rapidity and Γ_k a velocity. The map Γ⊕x=(Γ+x)/(1+Γx) is Einstein velocity addition; Γ_{k→l}=Γ_k⊕…⊕Γ_{l−1}; ∂(Γ⊕x)/∂x at x=0 equals 1−Γ². Move: composition of peel steps as relativistic velocity addition.
45. For real Γ=tanh(τ/2), sech²(τ/2)=1/γ² with γ=cosh(τ/2).
46. Metal's complex Γ: the isometry on the disk needs Γ̄ in the denominator.
47. Disk model: "The disk squeezes the walk toward the rim." Sodium ten steps: Γ=0.9938 at hyperbolic distance ln(IE11/IE1)=5.77.
48. Two transmissions for H_s with s=±1: T_s(0)=T_s(√2)=1/2 for both signs, because 2(x−s)²=x⁴−2sx³+2 at x=√2; T(1)=0 for s=+1 and 4/5 for s=−1. Move: a degenerate-at-√2 pair that differs only at x=1.
49. Signature zeros: both knots of the 13a_3542 / 13a_4018 pair have sigma=0 at s=4/5 (t=0.4296) and s=9/10 (t=0.4665).
50. Smith-based echo kill tests: H-01 echo weight |1−Γ²| as separator fails to beat |Γ| (held-out 0.743 vs 0.96 to 0.98). Move tested and killed.
51. Snell-like turning (§6.2): turning before g∥ vanishes. Killed: 1 hit vs 6 for window rule.
52. Associator of peeling order: 2×10⁻¹⁶ identity; zero-phase stacks telescope.

**v0.7.1:** editorial revision note; "requires the author's review before public release"; no new results.

**v0.8 (24 Sep):** fragments of checks; killed items noted.

**v1.0 (25 Sep):** fragments; includes the rapidity formula tanh(τ_k/2)=(z_k−1)/(z_k+1), and the Lean finite-algebra checkpoint (49 declarations: 30 foundations, 14 force recovery, 5 boundary ledger, Lean 4.33.0).

---

## 3. Element-specific results

Columns: element (symbol, Z), quantity, number, section. Values are as printed in each file. "Γ (computed here)" is my calculation from the version's own ratio, using Γ=(z−1)/(z+1); the version does not state it. "Sec" refers to headings in the file, or to the dropped-passage section numbers.

| Element (symbol, Z) | Quantity | Number as printed | Sec / source |
|---|---|---|---|
| Hydrogen (H, 1), hydride H⁻ | Infinite-mass energy; EA | −0.527751016544 a.u.; EA 6082.99(15) cm⁻¹ | Dropped v0.3 §15 (mass-scaling table, Nakashima & Nakatsuji; Lykke et al.) |
| Deuterium (D⁻) | EA | 6086.2(6) cm⁻¹ | Dropped v0.3 §15 |
| Helium (He, 2) | Rounded polarizability volume | 0.208 Å³ | Phase tests, "What gases add" (NIST CCCBDB) |
| He | Derived static susceptibility, 100 kPa, 300 K | 6.31×10⁻⁵ | Phase tests (illustrative) |
| He | Published A₂ (10⁻⁴ cm³/mol) and first-order Δn | 1.332468(6); Δn 1.47985×10⁻⁷ | Phase tests, two-color barometry table |
| He | Distortion sensitivity for δ=10⁻¹² | −0.6757 Pa | Phase tests, "Recovery and its obstruction" |
| He | Polarizability strict minimum | 6 of 6 noble gases incl. He | Dropped Run 02 (§8.3) |
| Lithium, Sodium, Potassium, Rubidium, Caesium (Li, Na, K, Rb, Cs) | Polarizability: next element after a noble gas | a maximum (6 of 6) | Dropped Run 02 (§8.3) |
| Sodium (Na, 11) | IE₁ to IE₁₁ over ten steps; Γ; hyperbolic distance | Γ=0.9938; ln(IE11/IE1)=5.77 | Dropped v0.7 (disk section) |
| Alkali first step (Li–Cs group) | Γ for largest alkali first step | 0.87 (stated as "0.87 for the alkali first step") | Dropped v0.3 §15 (nuclear comparison) |
| Alkali first step | Reset test, strict minimum | 6 of 6 passed | Dropped v0.8 check table |
| Neon (Ne, 10) | Rounded polarizability volume | 0.381 Å³ | Phase tests |
| Ne | Static susceptibility | 1.16×10⁻⁴ | Phase tests (illustrative) |
| Ne | A₂ and Δn | 2.46000(8); Δn 2.73210×10⁻⁷ | Phase tests, barometry table |
| Ne | Distortion sensitivity (δ=10⁻¹²) | −0.3660 Pa | Phase tests |
| Ne | Nuclear chain N=16 (isotope chain for Ne) | 0.60 | Dropped v0.3 §15 |
| Argon (Ar, 18) | Rounded polarizability volume | 1.664 Å³ | Phase tests |
| Ar | Static susceptibility | 5.05×10⁻⁴ | Phase tests (illustrative) |
| Ar | A₂ and Δn | 24.1320(8); Δn 2.68012×10⁻⁶ | Phase tests, barometry table |
| Ar | Distortion sensitivity | −0.03731 Pa | Phase tests |
| Ar | IE peel step v=8: IE 143.4567 → 422.6 eV; ratio | ratio 2.94584 (Γ computed here 0.4931) | Dropped Table 3 (§8) |
| Ar | Nuclear N=28 ridge | 0.40 to 0.42 | Dropped v0.3 §15 |
| Krypton (Kr, 36) | Rounded polarizability volume | 2.498 Å³ | Phase tests |
| Kr | Static susceptibility | 7.58×10⁻⁴ | Phase tests |
| Kr | IE peel step v=8: 125.802 → 233.0 eV; ratio | 1.85212 (Γ computed here 0.2988) | Dropped Table 3 |
| Xenon (Xe, 54) | Rounded polarizability volume | 4.005 Å³ | Phase tests |
| Xe | Static susceptibility | 1.22×10⁻³ | Phase tests |
| Xe | Peel ridge at 54 electrons left (near / mid / deep) | 0.338 / −0.028 / −0.004 | Dropped v0.3 §15 ridge table |
| Radon (Rn, 86) | Strict minimum of polarizability | 6 of 6 (no number) | Dropped Run 02 |
| Nitrogen (N₂, molecule) | A₂ and Δn | 25.997(5); Δn 2.88725×10⁻⁶ | Phase tests |
| N₂ | Distortion sensitivity | −0.03464 Pa | Phase tests |
| Oxygen (O, 8) | IE peel step v=6: 138.1189 → 739.32697 eV; ratio | ratio 5.35283 (Γ computed here 0.6852; Γ²=0.469, inside ½) | Dropped Table 3 (§8; not marked grade C) |
| Aluminium (Al, 13) | IE step v=3: 28.447642 → 119.9924 eV; ratio | ratio 4.21801 (Γ computed here 0.6167) | Dropped Table 3; Run 01 K=10 miss (groups 3/4/5 with Si, P); "by peel shape, Al resembles Sc" |
| Silicon (Si) and Phosphorus (P) | Run 01 K=10 misses | scored as groups 4 and 5 | Dropped Run 01 |
| Scandium (Sc, 21) | Nuclear N=34 | 0.21 | Dropped v0.3 §15 |
| Argon / Krypton / Xenon closure staircases | Qualitative | closed-shell staircases | Dropped Table 3 notes |
| Calcium (Ca, 20) | Nuclear N=20, N=28, N=32, N=34 | 0.38, 0.40 to 0.42, 0.43, 0.45 | Dropped v0.3 §15 |
| Potassium (K, 19) | Nuclear N=20, N=28, N=32 | 0.34, 0.40 to 0.42, 0.42 | Dropped v0.3 §15 |
| Magnesium (Mg, 12) | Nuclear N=20 closure gone | 0.15 (typical non-magic 0.12) | Dropped v0.3 §15 |
| Chromium (Cr, 24) | Nuclear N=28, N=32 | 0.19, 0.12 | Dropped v0.3 §15 |
| Fluorine (F, 9) | Nuclear N=16 | 1.24 (drip-line contribution mixed in) | Dropped v0.3 §15 |
| Nickel-like (Ni, 28) | Electron-count ridge (Ni-like closure) | ridge at 28 electrons left; grows in census | Dropped Run 01 and v0.7 ridge census |
| Palladium-like (Pd, 46) | Electron-count ridge | ridge at 46 | Dropped Run 01 |
| Gold (Au, 79) | IE₁ | 9.225554 eV | Combined, "Elemental inputs" table |
| Au | Later jump (after 11 removals) | 79.80 eV | Combined; dropped Table 2 |
| Au | Reflectance R450, R550, R650 | 0.408, 0.792, 0.957 | Combined, elemental inputs |
| Au | Film at 450 nm on n_s=1.5: 200 nm / 58.2093 nm / 10 nm | 0.408191 / 0.426742 / 0.163082 | Combined "A film peel changes two interfaces"; dropped §6.4 |
| Au | Gold metamer XYZ separation after reflection | 0.0104183 (threshold 0.001) | Combined "A gold surface separates an actual observer equivalence" |
| Au | Gold/titania swap (v1.1.1 note) | N = 0.4+2.3i, titania N = 2.4; 0.432 vs 0.433 | Dropped preamble (v1.1.1) |
| Au (gold) | Goldene (2D Au) thermopower check | six of seven Table 4 rows fail PF=S²σ by >5%; zero strain: 1.26906×10¹⁴ computed vs 1.27×10¹¹ printed | Phase tests, "The goldene numbers require correction" |
| Au (gold) | Lattice thermal conductivity "17 times bulk" | simulation result for a lattice, not total bulk gold | Phase tests |
| Au (gold) | Equal conductance, opposite thermopower model | G/G0=0.2209316590271; S=±63.21177934 µV/K (a=0.2 eV, Γ=0.1 eV, T=300 K) | Phase tests, thermal mirror (illustrative, not fitted to gold) |
| Copper (Cu, 29) | IE₁ | 7.726380 eV | Combined, elemental inputs |
| Cu | Later jump (after 11 removals) | 101.67 eV | Combined; dropped Table 2 |
| Cu | R450, R550, R650 | 0.538, 0.624, 0.935 | Combined |
| Silver (Ag, 47) | IE₁ | 7.576234 eV | Combined |
| Ag | Later jump (after 11 removals) | 83.46 eV | Combined |
| Ag | R450, R550, R650 | 0.980, 0.983, 0.990 | Combined |
| Platinum (Pt, 78) | IE₁ | 8.95883 eV | Combined |
| Pt | Later jump (after 10 removals) | 75.50 eV | Combined |
| Pt | R450, R550, R650 | 0.588, 0.641, 0.678 | Combined |
| Ruthenium (Ru, 44) | IE step v=8: 110.0 (grade C) → 178.41 eV; ratio | 1.62191 (Γ computed here 0.2372) | Dropped Table 3 |
| Rhodium (Rh, 45) | IE step v=9: 135.0 (grade C) → 207.51 eV; ratio | 1.53711 (Γ computed here 0.2117) | Dropped Table 3 |
| Tellurium (Te, 52) | IE step v=6: 69.1 → 124.2 eV; ratio | 1.79740 (Γ computed here 0.2851) | Dropped Table 3 |
| Hafnium (Hf, 72) | IE step v=4: 33.37 → 68.37 eV; ratio | 2.04885 (Γ computed here 0.3440) | Dropped Table 3; depth-law failure at 11 to 12 |
| Tantalum (Ta, 73) | Depth-law failure at 11 to 12 | named as failing (no number) | Dropped Run table |
| Lead (Pb, 82) | IE step v=4: 42.33256 → 68.8 eV; ratio | 1.62523 (Γ computed here 0.2382) | Dropped Table 3 |
| Polonium (Po, 84) | IE step v=6: 69.1 → 108.0 eV (both grade C); ratio | 1.56295 (Γ computed here 0.2197) | Dropped Table 3 |
| Beryllium (Be, 4) | Electron correlation hole | about 2 Å base; 4 to 5 Å near 21 eV plasmon | Dropped v0.1 §3 (cited arXiv 2601.20814) |
| Black phosphorus (P, 15) | Full quantum metric reconstructed | no number | Dropped v0.1 §3 (cited) |
| Oganesson (Og, 118) | Predicted noble-peel second IE | test proposed (no number) | Dropped v0.3 "still open" list |
| Ce, Zr, Hf (allotropes) | Pressure/volume/angle intuition | no numbers | Dropped §8.5 |
| Tc, Pm, Po, At, Rn, Fr, Ra, Ac, superheavy | Sparse data grade D | no numbers | Dropped §2.4 |
| Nuclear N=8, 20, 28, 50, 82, 126 (magic numbers, element-independent ridges) | Mean ridge prominence | 0.188, 0.110, 0.141, 0.209, 0.244, 0.221 (non-magic 90th percentile 0.000) | Dropped v0.3 §15 |
| Nuclear N=20 with extrapolated masses | Ridge prominence | −0.008 (island of inversion) | Dropped v0.3 §15 |
| Nuclear N=34 | Ca 0.45, Sc 0.21 | closure in calcium only | Dropped v0.3 §15 |

Data grades: several rows are NIST-estimated (grade C). The dropped file says the 0.95 Run 01 result at K=10 rests on NIST-estimated deep stages and that the measured-only redo was not completed (T-C). Those rows are marked.

---

## 4. Bold moves (mathematical, with assumptions)

These are the moves, with the assumption each rests on. Several were dropped after v0.7.

**Move 1. Peel coordinate as Smith log-impedance (dropped v0.2, Theorem 8.1; restated v0.7).** Set z_k=IE_{k+1}/IE_k, τ_k=ln z_k, Γ_k=tanh(τ_k/2)=(z_k−1)/(z_k+1). Assumption: IE ratios are treated as an impedance ratio, so the Smith disk and a first-order echo can be applied to ionization. Consequence: a single peel step is a point on the disk at hyperbolic distance τ_k. This is the frame's identity (Γ=(z−1)/(z+1)=tanh(½ ln z)), stated in the version.

**Move 2. Radar Doppler reading gives Γ as a velocity (dropped v0.7, §6.2).** Light reflected from a mirror receding at speed β returns at ν(1+β)/(1−β); setting this equal to z_k gives β=Γ_k. Assumption: the ionization ratio is a reflected-frequency ratio. Consequence: IE ladders are velocity sequences in units of c.

**Move 3. Peel composition as relativistic velocity addition (dropped v0.7).** Γ⊕x=(Γ+x)/(1+Γx), Γ_{k→l}=Γ_k⊕…⊕Γ_{l−1}, and ∂_x(Γ⊕x)|_{x=0}=1−Γ². Assumption: the disk isometry, valid for real Γ only. For complex metallic Γ the version notes the isometry needs Γ̄ in the denominator. Consequence: the derivative of a peel step with respect to an added small step is 1−Γ², i.e. the same quantity that appears in the frame's wall discussion. The version does not state a wall at 1−Γ²=½.

**Move 4. One reflection coordinate for light, electrons and matter waves (dropped v0.3, Theorem 15.1).** A matter wave meeting a step reflects with r=−tanh(τ/2), τ=ln(k2/k1). Assumption: a step in wavenumber of the same form as the IE step. The version checks a slab with a transfer matrix to 3.5×10⁻¹⁶ and reports 390 of 400 bump cases. Consequence: one reflection law across three physical contexts.

**Move 5. Scale blindness (dropped v0.3, Theorem 15.4).** Multiplying all masses by λ gives H_λ unitarily equivalent to λH; every IE ratio is unchanged. Assumption: pure Coulomb interaction with all masses scaled. Consequence: ratios are dimensionless invariants; absolute energies are not.

**Move 6. Observability quotient (dropped v0.1, Theorem 3.1).** O v=(Rv,RLv,…), N=ker O, V/N is the smallest autonomous state summary, and rank O − rank R extra coordinates are needed beyond the present observation. Assumption: finite-dimensional linear evolution. Consequence: a count for how many hidden coordinates a present reading leaves unresolved.

**Move 7. Occupation sets a curvature sign (dropped v0.1, Theorem 4.1).** With population r held fixed, the response curvature is χ=2c²/δ=8δ g_aa(0), and vanishes at a critical occupation r_c. Assumption: population-preserving probe; bare energy quartic. Consequence: response curvature changes sign as a function of occupation, a wall-like crossing in a parameter that the frame would call a phase.

**Move 8. Transfer silence reduced to q Cayley–Hamilton terms (dropped v0.1 §5.4; surviving as the memory-kernel result in the combined file).** B(zI−D)^{-1}C≡0 iff BD^jC=0 for j<q. Assumption: hidden dimension q. Sharpness by a nilpotent shift. Consequence: a finite list of zero measurements decides whether a hidden layer is dynamically silent.

**Move 9. Quadrature recovery from intensity differences (dropped v0.1 §5.7; surviving in the combined file as the electromagnetic records).** |z+a|²−|z−a|²=4a Re z and |z+ia|²−|z−ia|²=4a Im z; error ε/(√2 a). Assumption: exact real reference a. Consequence: intensities alone discard phase; a second quadrature restores it.

**Move 10. Ratio-invariant thermal mirror (surviving in the phase file).** T_−(E)=T_+(−E) under reflection about the chemical potential, so every moment ∫p(T)w_T is equal, while the Seebeck coefficients S_±=∓. Assumption: elastic single channel, linear response. Consequence: a conductance-only record cannot fix the sign.

**Move 11. Equal conductance is equal under mirrored energy (surviving).** Same move as Move 10 applied to the transmission distribution; the energy-odd probe is named as the restoring record.

**Move 12. Counting cumulants with Newton identities (surviving in combined and dropped v0.1).** c1, c2, c3 as power-sum combinations; three cumulants fix up to three transmissions. Assumption: known channel count bound of three. Counterexample: four channels can match all three moments.

**Move 13. Projector-distance one-mode certificate (surviving in phase file).** δ=‖P−P0‖; if δ²<ε and ε+δ<ν0<1−ε−δ, then N_ε=1. Assumption: block of 2n+1 modes with restricted P0 spectrum as stated. Consequence: resolution-dependent single-mode certificate that is independent of block size.

**Move 14. Gap-weighted derivative of a projector (surviving in combined).** (Ṗ)_ij=(p_i−p_j)/(λ_i−λ_j)(Ḣ)_ij, so equal gaps with different matrix elements of Ḣ give different subspace motion.

**Move 15. Torus control: a form that vanishes identically on torus branches (dropped v0.1 §12.5).** On L=εM^{−k} with |ε|=1, ω=−k log|M| d arg M + k log|M| d arg M = 0. Assumption: branch of the A-polynomial curve. Consequence: the knot potential is zero while topology is nontrivial.

**Move 16. Hopf charge as a preimage count (dropped v0.1 §11.2).** Q equals the number of preimages of a generic value; by exact elimination preimages of (c1,c2) under (z^α w^β, z^p+w^q) are roots of a polynomial of degree αq+βp (T(3,4) gives 7, 10, 11, 13, 15).

**Move 17. Neutron-pair peel for nuclei (dropped v0.3 §15).** S_2n(Z,N)=B(Z,N)−B(Z,N−2) with the same reflection and peel-coordinate machinery as the atoms. Pre-registered magic-number test, 6 of 6 ridges above the 90th percentile.

Each is an assumption-bound move. None was claimed as a general law in the version.

---

## 5. Connections to today's frame

Frame quantities: Γ=(z−1)/(z+1)=tanh(½ ln z); wall at Γ²=½ (z=3+2√2≈5.828); phase at a wall; cancel/lock/convert; two books E⁻/E⁺=Γ²; neutrinos; Koide; spin; tree or ball; Lorentz/rapidity.

**Found in the files (quoted, short):**

- Γ and the peel coordinate (dropped v0.2, Theorem 8.1): "the peel coordinate τ_k=ln(IE_{k+1}/IE_k) is the Smith log-impedance". Identical to the frame's Γ=tanh(½ ln z) with τ=ln z.
- Γ as velocity (dropped v0.7): "Set this ratio equal to z_k=IE_{k+1}/IE_k and solve: β=(z_k−1)/(z_k+1)=Γ_k." Exact frame formula.
- Rapidity (dropped v0.7): "In that language Γ_k is a velocity and τ_k/2 a rapidity." Lorentz/rapidity frame point is here.
- Lorentz factor (dropped v0.7): "sech²(τ/2)=1/γ²" with γ=cosh(τ/2).
- Sodium step (dropped v0.7): "Sodium's ten steps from IE_1 to IE_11 reach Γ=0.9938". This is consistent with the frame's Γ=tanh(½ ln z) (I checked: ln 5.77 gives 0.99378).
- Alkali first step past the wall (dropped v0.3): "against 0.87 for the alkali first step". Frame's "alkali first steps past the wall" is consistent: Γ=0.87 gives Γ²=0.757>½. The version does not state the wall; this is a Γ value only.
- Oxygen and aluminium steps are inside the wall (computed here from the version's ratios): O Γ=0.6852, Γ²=0.469; Al Γ=0.6167, Γ²=0.380. Both below ½. Consistent with the frame's claim that only a small set of steps pass the wall. Frame's Be, B, C K-shell openings are not in these files.
- Wall-type quantity tested and killed (dropped v0.7, H-01): "echo weight as separator fails to beat |Γ|". The quantity |1−Γ²| was tested against |Γ| and lost (0.743 against 0.96 to 0.98). Relevant to any claim that Γ²=½ marks a separator.
- Phase at a wall (combined): "A response can look information-poor because the instrument discarded the quadrature it needed." Frame's "phase survives at a wall" has a direct analogue: intensity loses phase, complex flux keeps it.
- Phase survives, amplitude does not (phase tests): "The two resonances are reflected across the chemical potential." Paired with equal |T| and opposite S. Partial analogue of "amplitude dies, phase survives" (energy-odd record needed).
- Cancel (combined): "The remaining path is released from destructive interference." Frame's CANCELLED case. The side orbital raises transmission from 0.180144 to 1 when coupling g goes to zero.
- Two resonances reflected (phase tests, thermal mirror): T_+(E) and T_−(E)=T_+(−E). Equal G, opposite S. Frame's "two books" equal-sum and opposite-sign is a structural analogue only; the version does not use "books".
- Tree or ball (combined): "preserves the Bloch ball" and (dropped v0.7) "The disk squeezes the walk toward the rim." The version's Smith disk is a hyperbolic disk, which is the frame's tree/ball in a different language. Not identical.
- √2 (dropped v0.7): T_s(0)=T_s(√2)=1/2 for both signs, because 2(x−s)²=x⁴−2sx³+2 at x=√2. Only √2 in the files, not the frame's wall.
- 1/√2 (phase tests): coherency example a=1/√2, b=±i/√2. A state, not a wall.
- Neutrality (combined): "neutrality does not imply a geometric wall". Quoted as a control; see contradictions.
- Spin: appears only as "spin-degenerate" and "spin-polarized" occupations. No CANCEL/LOCK/CONVERT spin move.

**Not found in any of the three files (stated plainly):**

- z=3+2√2 ≈ 5.828, and Γ²=½ (|Γ|=1/√2≈0.707). No string match in any file.
- Lock (resonance on a periodic end): the grep hits are "block" only.
- Neutrinos (m3/m2, m1=0). No match.
- Koide's lepton ½ or balanced books. No match.
- Garrett's ball tree or ratio-5 edge (Γ=2/3). No match.
- Two books E⁻/E⁺ as such. No match.

---

## 6. Anything that contradicts today's frame

1. Different wall. The version's Smith-chart separator is |Γ|≈0.93 for a metal film echo (dropped v0.2: "a single Smith radius near |Γ|≈0.93 separates the two regimes to 99.4%"), and a calibration threshold |Γ|≤0.856 (87%). These are not the frame's Γ²=½ (|Γ|≈0.707). The version gives no evidence that |Γ|=1/√2 marks a boundary. It is a different radius for a different quantity (a film echo, not an ionization step).

2. |1−Γ²| not a separator. The version tested |1−Γ²| (the derivative of velocity addition, which vanishes at |Γ|=1) against |Γ| and killed it (0.743 against 0.96 to 0.98). If the frame's wall is read through 1−Γ², this test cuts against that reading. The frame's Γ²=½ is not the same as |1−Γ²|=½ either; the version does not test Γ²=½.

3. Neutrality. "neutrality does not imply a geometric wall" (combined). A neutral gapped Dirac projector has finite nonzero metric. This is a control against reading neutrality as a wall. It does not contradict Γ²=½, but any frame claim that a neutral or balanced state sits on a wall would need to meet this control.

4. Complex Γ for metals. The version notes that a metal's Γ is complex and the disk isometry then needs Γ̄. The frame's wall is written for real Γ. The frame must say whether it applies to complex Γ.

5. Snell-like turning (dropped §6.2) was tested as a wall-like turning and killed: "1 hit vs 6 killed" (dropped v0.7). A turning set that does not beat the window rule is a negative result against using a turning point as the wall.

6. Ratio-invariance. The version's scale-blindness theorem (dropped v0.3) says IE ratios are unchanged under mass scaling. This supports the frame's use of ratios but also means the wall is a statement about the ratio alone, not about absolute energies. No contradiction; a constraint on how the wall is stated.

7. Ionization count. The version's O and Al steps sit inside the wall (Γ²=0.469 and 0.380). Sodium and the alkali first steps sit past it (Γ=0.87). This is consistent with a small set of past-wall steps. Nothing in the files contradicts the 8-of-5,737 count, but the files do not include that count.

8. Byline and date. The Combined file byline is "Jeromie N. Beasley". The two HTML files are dated before the dropped drafts. Neither changes the physics, but both bear on which version the frame may cite.

---

## Summary of strongest element results (for the main session)

1. Sodium: ten IE steps reach Γ=0.9938 at ln(IE11/IE1)=5.77 (dropped v0.7). Consistent with the frame's Γ=tanh(½ ln z).
2. Noble gases: strict minima of polarizability for He, Ne, Ar, Kr, Xe, Rn (6 of 6), with the next element a maximum (dropped Run 02). Quantity: polarizability; a reset in the outer peel.
3. Oxygen and aluminium IE steps: ratios 5.35283 and 4.21801 (computed Γ 0.685 and 0.617; both inside Γ²=½). Dropped Table 3.
4. Gold: R450 0.408, film 0.408191 / 0.426742 / 0.163082 at 200 / 58.2 / 10 nm, metamer separation 0.0104183 (combined; dropped §6.4).
5. Alkali first step Γ=0.87 (dropped v0.3), past the frame's wall.

Strongest moves: (a) peel coordinate equals the Smith log-impedance and the Doppler reading gives Γ as a velocity (dropped v0.2 and v0.7); (b) peel composition as Einstein velocity addition (dropped v0.7); (c) one reflection law for light, electrons and matter waves (dropped v0.3).

Connection to the wall: the version has the identity Γ=(z−1)/(z+1)=tanh(½ ln z) and the rapidity reading, but no Γ²=½ wall, no 3+2√2, no lock, neutrino, Koide or tree. The version tested and killed |1−Γ²| as a separator.

Coverage caveat: the Combined and Phase Tests files do not contain the Smith, rapidity or IE-ratio material. That material is only in the dropped-passages file (v0.2 to v1.0).
