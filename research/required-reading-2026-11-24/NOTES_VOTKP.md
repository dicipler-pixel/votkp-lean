# Required reading, notes 2 of 2: VOTKP

Reader: Session A, alone, no agents. 24 November 2026.
Text read: `VOTKP_ELEMENTAL_PEELING_PAPER_v3_3_20261112.html` (branch `claude/sm-ball-20261111`, folder `paper/votkp_v3_3/`), built 12 November on the whole v2.9 that Jeromie supplied. Not an Open Math build. 454,000 characters of text, equations in the source.
Notes keep to the periodic table and the tensors. Coverage record at the end says exactly what was read.

## Front matter, Sections 1 to 6

- **The record is a vector, not a number.** VOTKP = vector of traits kept under peeling. The one question: "when a layer is peeled away, which records change and which survive?"
- **The peel coordinate.** z_k = IE_{k+1}/IE_k read as an impedance; Γ_k = tanh(½ ln z_k). "An exact change of coordinates, not a mechanism." Steps compose by the velocity-addition law, so a peel is a hyperbolic length on the Smith disc.
- **Shape and level are separate records.** Shape, ln(IE_{k+1}/IE_k), recovers the periodic group at held-out accuracy 0.95. Level, ln IE_1, carries response: polarizability ∝ IE_1^(−3.04), R² = 0.91, with radius and hardness.
- **Shell part of a step at a wall:** Γ^sh = (2n−1)/(n²+(n−1)²): 3/5, 5/13, 7/25. It depends on the principal quantum number alone. The rest is the screening part.
- **Inside a subshell:** the largest step sits at the half-filled step in lightly charged ions and at the spin-orbit edge in highly charged ones (84% of 316 p subshells, 70% of 158 d).
- **Ends and middle:** last step → 5/(8Z) (two 1s electrons, the 5/8 is their Coulomb repulsion); middle follows Thomas–Fermi, Γ_k ≈ tanh((2/3) ln((k+1)/k)) ≈ 2/(3k). The envelope "carries none of the family".
- **Result 9 (the bridge to the tensor):** for two positive numbers on one edge, E₋ = (d_i−d_j)², E₊ = (d_i+d_j)², and E₋/E₊ = Γ². "The half line Γ² = ½ is the edge on which the first book holds one third of the budget; the rim is the edge on which the books are equal."
- **Result 10:** eight of 5,714 steps lie past the half line: first steps of Li, Na, K, Rb, Cs and the K-shell openings of Be, B, C. Each core-opening line crosses it once.
- **Octaves (summary item 6):** a fixed octave of eight fails beyond calcium; "Russell's octaves (1926) are the rows of the table relabelled". One wave per row loses to octave plus transition-metal insert (130 against 59 kJ/mol), which loses to neighbour interpolation.
- **Separations the paper keeps (Section 1):** chemical identity ≠ isolated-ion record ≠ surface record ≠ response; subspace refraction ≠ boundary reflection.
- **State labels (Section 2):** (Z, state, environment, T, P, charge) replace Z alone. Data: NIST ASD 5.12 through mendeleev 1.3.0; deep stages are mostly theoretical.
- **Theorem 3.1:** predictive quotient. Two states have the same futures iff their difference is in the unobservable subspace N; rank(O) − rank(R) extra coordinates are needed beyond the present reading.
- **Section 4, where the tensor enters by name:** the quantum metric g_ij = Σ_occ Σ_unocc Re[⟨n|∂_iH|m⟩⟨m|∂_jH|n⟩]/(E_m−E_n)² "needs both a gap and a coupling". Allowed spacing Δ_allowed(O) = smallest gap with a nonzero coupling. Theorem 4.1: occupation sets a response curvature, χ = 2c²/δ = 8δ g_aa(0). "Static polarizability is such a curvature, α = 2Σ|⟨m|d|0⟩|²/(E_m−E_0)."
  - This is the IQGT pair sum with weight 1/Δ per pair in the dipole coupling, which in the IQGT table (Section 7.2 there, written with the velocity-type coupling) sits one gap power from the metric.
- **Section 5:** finite peel theorems. 5.3 Schur boundary memory: the hidden layer survives as the self-energy Σ(z) = B(zI−D)⁻¹C. 5.9: two states with the same spacing and the same two transmissions differ later (0 against 4/5). 5.10: Σ_λ(0) = −c for every λ, but Σ′_λ(0) = −c/λ.
- **Section 6:** surface reflection Γ = (1−N)/(1+N) on the same disc; film echo theorems 6.1 to 6.3; the gold metamer through the map CMP.

## Sections 6.4 to 8.9 (the ionization onion): the heart of the periodic-table material

- **Theorem 8.1.** Γ_k = (z_k−1)/(z_k+1) = tanh(τ_k/2), τ_k = ln(IE_{k+1}/IE_k). Every z_k > 1, so "the atomic reflection chart has no phase". The paper's own limit on it: "Any increasing ladder has such a chart ... so the chart alone constrains no atomic dynamics. Its content is in the tabulated ratios."
- **Run 01 (registered).** Held-out group accuracy from the peel shape: 0.51, 0.74, 0.95 at 3, 6, 10 steps; static record 0.41, 0.42, 0.51; shuffled 0.04.
- **Depth ladder (8.3).** Period-6 groups from a model trained on Z ≤ 54: accuracy 1.00 at 8 to 10 steps. Misses at shorter windows "are exactly the elements whose outer shell the window has not reached". Of the 198 stages used, 43 measured, 46 semi-empirical, 109 theoretical.
- **Ridge census (8.4).** Ridges at closed counts 10, 18, 28, 36, 46, 54, 68. Ar-like and Kr-like shrink tenfold with charge; Xe-like vanishes in deep ions; Ni-like (28) grows. **Janet's left-step closures (4, 12, 20, 38, 56) carry no ridge: 0.004 against 0.477 at the noble-gas counts.** This bears directly on yesterday's table-wave work, which anchored pair ends at Z = 4, 20, 56, 120.
- **Level carries response (8.5).** ln α = 10.28 − 3.04 ln IE_1, R² = 0.906, 86 elements. Adding tabulated oscillator strengths makes the prediction worse (registered kill fired): "the level tracks the denominator". IE_1 is a median 1.6 times the energy of the strongest ground line.
- **Resets (8.6).** τ_1 after each noble gas: Li 2.641, Na 2.219, K 1.986, Rb 1.877, Cs 1.783, Fr 1.705: the six largest in the table.
- **Theorem 8.2, the split.** With IE_k = Ry·Z_eff²/n², τ_k = 2Δln Z_eff − 2Δln n, so Γ_k = Γ^scr ⊕ Γ^sh. At a wall Γ^sh = (2n−1)/(n²+(n−1)²) = 3/5, 5/13, 7/25, 9/41, 11/61, 13/85: "the odd leg over the hypotenuse of the Pythagorean triples". "The triples carry no physics beyond the hydrogen-like ratio (n/(n−1))²." Lithium: 0.867 = 3/5 ⊕ 0.556. Checked on all 5,714 steps to 4×10⁻¹⁶.
- **Two kinds of wall.** Same shell part, two screening parts: onto a closed p core the Z_eff jump is 1 to 3 and grows down the table (1.10, 1.88, 2.31, 2.89, 3.31 at the alkali metals); onto a filled d shell it is under 1 and shrinks along the row. Onto the filled 4f shell it is negative in all twelve row-6 elements (−4.2 to −6.7): "The f shell is not a third kind" (registered, failed that way).
- **Stagger inside a subshell.** Largest interior step sits at the half-filled step (Hund) or the spin-orbit edge: p 264/316, d 110/158. Changeover with charge: 2p at Z = 29, 3p at 46, 4p at 47. f shells: 0 of 36 (failed that way, open).
- **Down the column (8.8).** ln IE_k is near linear in period (median miss 7.5% into period 6). Under-prediction happens where "the step has slipped a filled inner shell of a new kind, d or f, under the outer electron" (20 of 22 signs).
- **Octaves (8.9). Already tested here; yesterday's table-wave run repeated part of this without my having read it.**
  - Fixed octave of eight: correct from Li to Ca, none after (T07). My run: 16 of 16 for Z = 3 to 20, failing beyond. Same result, his was first.
  - "Ten octaves of seven tones, each headed by an inert master-tone" = "the rows of the periodic table, relabelled".
  - Contraction to the fourth tone fails: molar volume is smallest at the third tone (B, Al, Ga, In, Tl).
  - One wave per row loses to main-group octave plus transition insert (130 against 59 kJ/mol). The two heights move in opposite directions down the table (521→208 and 505→865).
  - What survives: the swing. Alkali-to-noble swing in IE_1 falls to about 0.81 of the row before.
  - **The one-third constant (post-hoc, open):** main-group atomization height H_p ≈ c·(IE_noble − IE_alkali) with c = 0.3336 in matching units, "within 0.1% of one third; no reason for a third is known here". Held out a row at a time it predicts each row within 6.5%. Written with Γ_row = tanh(½ ln(IE_noble/IE_alkali)).
  - Lead noted while reading, untested: on the half line Γ² = ½ the first book holds exactly one third of the budget (Result 9). The row constant is also one third. Whether these are the same third is a question, not a finding.
  - Two cuts of one onion: a row's neutral first steps (diagonal) against its noble gas peeled (horizontal) agree in sign of second difference at 18 of 24 points; they share shell structure, not the half-filled dip.

## Sections 9 to 15.4

- **Section 9, the Snell test that failed (registered).** An orbital-subspace geometry (principal angles between neighbouring ions, built from Slater orbitals, no ionization energies) does not reproduce the short-window misses or the deep ridges. After smooth trends are removed its step size correlates with the tabulated Γ_k at only 0.02 to 0.03. "Refraction and reflection are distinct layers. They share a global trend, not step-by-step structure." Left open for relativistic self-consistent orbitals, and for two places: the column misses of 8.8 and the nuclear gaps of 15.4.
  - For the tensor: this is the one place the paper put the IQGT metric (principal angles, g_∥) directly on the table of elements, and in that setup it failed. The tensor entered the elements successfully only later, through the two-books edge of Section 22, not through refraction.
- **Section 10.** VOTKP(K,Ψ) = (topology, field loading, geometry, realization). "The layers are not collapsed into one scalar." Permanent distinctions: crossing number ≠ atomic number ≠ colour N.
- **Sections 11 to 14 (knots).** HOMFLY first separates beyond Alexander and Jones at 13 crossings (19 pairs). 354 blind pairs through 12 crossings; categorified invariants separate only through signature or thickness. Levine–Tristram signature: walls are Alexander roots on the unit circle; one window separates 13a3542 from the mirror of 13a4018. Hopf charge Q = αq + βp varies on a fixed knot (7, 10, 11, 13, 15 on T(3,4)). Colour ladder: 21 pairs blind at colours 2 and 3, all separated at colour 4. "The colour ladder on knots and the depth ladder on atoms are the same pattern."
- **15.1.** "The electron is the unit of the peel; the layering belongs to the interacting state." IE is a difference of two many-electron total energies.
- **Theorem 15.1 and Corollary 15.2.** Γ_{k→l} = Γ_k ⊕ … ⊕ Γ_{l−1}; hyperbolic distance from the centre is ln(IE_l/IE_k). "An atom's peel is a walk along one diameter, which is a geodesic." Sodium's ten steps reach Γ = 0.9938.
- **Corollary 15.3.** The film is r = Γ ⊕ x with complex arguments; the hyperbolic reading holds only for real Γ. Derivative at x = 0 is 1 − Γ².
- **Order.** ⊕ is commutative and associative, so the composite "carries no information about the order or grouping of its steps; the resolved ladder does". A projected product x⋆y = P(xy) is not associative: "what one reduction discards can reappear in the next". Order in a film comes only from the phase between additions (Thomas rotation).
- **Theorem 15.4, scale blindness.** Multiplying every mass by λ scales every energy by λ and leaves every ratio unchanged. The coordinate sees a change of particle only through charges, mass ratios and statistics: H⁻ 2.892, D⁻ 2.8918, Ps⁻ 3.036.
- **Statistics makes the ridges.** Two particles give the same helium-like peel for bosons and fermions (τ = 0.7945). "The first ridge needs a third fermion. Lithium's τ₁ = 2.641 exists because exclusion forbids 1s³."
- **The coordinate needs an absolute zero.** Quantum dots and clusters have shells but no continuum reference, so no peel ratio.
- **15.4 nuclei.** Neutron-pair peel: the six magic numbers are the six strongest ridges; oscillator closures 40 and 70 carry none. Mass-5 and mass-8 gaps leave the disc: |Γ| = 1.074 (⁵He), 1.220 (⁵Li), 1.025 (⁸Be); z = −1 is the Cayley pole. "The mass-5 gap is the nuclear form of the exclusion wall."

## Sections 15.5 to 20.2

- **15.5 to 15.8.** Knots as particles: Kelvin's vortex atoms were the first "periodic table" of knots; "This paper keeps Tait's tables and claims no correspondence between elements and knots." Tight-knot glueball extension: registered tests failed that way. "The electron is not modelled as a knot." Loop states of SU(2) lattice gauge theory map into hydrogen's state space (n = 2j+1) but "a shared state space is not a shared spectrum".
- **15.9 new elements.** Oganesson: τ₁ = 0.600, inside the noble band by shape; polarizability 58 against radon's 35, so "noble by peel shape, less noble by level response". Elements 119 and 120 sit 1.55 and 2.14 eV above the column line. The f-block does not transfer between lanthanides and actinides (2 to 3 of 14).
- **15.10 last step.** IE_last = Z² − (5/4)Z Rydberg at first order; the 5/8 is ⟨1s1s|1/r₁₂|1s1s⟩ = 5Z/8 Hartree, "the screening of one 1s electron by the other, to first order, and that is all it is". Γ_last → 5/(8Z). Helium reproduced to 1 meV with the 1/Z series; residual grows as Z^4.3 (relativity).
- **15.11 middle.** Cost of the first m rungs → a_TF·m^(7/3), a_TF = 1.2875 eV (cited external machine-checked claim), q_TF = 5.2211. Limiting step Γ_k → tanh((2/3)ln((k+1)/k)). "Both are Euclid's form applied to a ratio of neighbouring integers, one at full power and one at power 2/3." TF-RESID-01 (registered, passed): the envelope classifies 0.000 of the groups; the residual classifies 0.951. "The envelope carries the scale of the middle of the peel, and the residual carries the family."
- **Section 16, five common findings:** records are vectors; resets fade away from home; resolution ladders; two geometries of a boundary (reflection organises the onion, refraction did not); one composition law.
- **Section 17, open problems that touch the tensor and the table:**
  - "The elemental angle in projector form. The principal angles of §9 were taken between model orbital subspaces; the same angles between the retained projectors of §22.1 have not been computed."
  - "A map between the disks. No map is stated from a point of the Smith disk to a point of the tetrahedron-shape disk."
  - The wall of the f shell (negative screening part; stagger fails).
  - A measured IE of Fr⁺: 23.74 eV decides whether francium is past the half line.
  - The alkali charge ratio: why Z_c/Z_v is one number from Na to Cs.
  - The row-swing one-third.
- **Section 19, directed peels: the exact statement of what the scalar ladder does and does not give the tensor.**
  - Proposition 19.1: G_j = tanh(½ ln(E_{j+1}/E_j)) for any positive record; reversal negates; ⊕ is a group law on (−1,1); the record telescopes to (E_m−E_0)/(E_m+E_0).
  - Proposition 19.2: traversed length minus endpoint distance = 4·min(R₊,R₋). "Adding the inverse deletes the endpoint displacement but does not delete the record of travel."
  - **Proposition 19.3: a positive ladder does not determine the path length of a retained projector.** Families with the same eigenvalues move the ground projector at metric b² for any b. "The intrinsic Grassmannian metric measures projector displacement; the Poincaré metric here measures a directed logarithmic energy record. Neither is the other without a declared map and its differential. This is the precise missing hypothesis."
  - Also: "actual atomic ionization thresholds are differences of ground energies in different electron-number sectors, rather than adjacent eigenvalues in one fixed sector."
  - Proposition 19.4 (conditional): with a declared lift, a metric floor a² and positive bath weights, excess work ≥ w*·L²/T ≥ (w*a²/4T)·L_rec².
  - 19.6: two distinct gaps d, e carry the same friction weight exactly when d·e = 1/τ² (1 and 4 at τ = ½).
- **Section 20.1 to 20.2.** Anchored ledger: B_q = Σ_{j≥q} I_j (remaining binding), E_{q,0} = −B_q. "The full coordinate vector plus one absolute threshold reconstructs a connected block." Each charge sector has its own Hamiltonian H_q, state ρ_q and "an explicitly selected retained projector P_q"; "Different charge Hamiltonians need not share nested projectors." Channel measure dF_q(Δ) = Σ Δ·Re(d d†)δ(Δ−Δ_a): "not populated by ionization energies alone". Normalisation: g = ∫Δ⁻³dF, α(x) = 2∫(Δ²−x²)⁻¹dF. Metric from a rate spectrum: g_aa = (2/πA²)∫R(ω)/ω² dω. Bath weight w(ω) = 2ħτω/(1+(τω)²), maximum ħ at ωτ = 1. Ferranti: V_r/V_s = sec(βℓ).

## Sections 20.3 to 21

- **20.3.2.** I_q = I_0·Π(1+Γ_j)/(1−Γ_j): the anchor and the full peel vector rebuild the whole ladder and the electronic binding; M_atom = M_nucleus + Z·m_e − B_el/c². 103 elements have complete ladders.
- **20.3.3.** One positive matrix measure dM(E) = B·dE_D(E)·B† gives three readings: self-energy Σ(z) = ∫dM/(z−E), kernel K(t) = ∫e^(−iEt)dM, and contour moments. K(0) = BB† is only "a coupling footprint". **"Choosing a spectral projector of the same self-adjoint H makes B = 0."** A nontrivial peel needs a projector that selects "a different physical configuration, channel, region, or readout".
- **20.3.4.** For a fixed-charge atom with dipole couplings: g_ij = ΣRe(a*a)/Δ², α_ij(x) = Σ2Δ·Re(a*a)/(Δ²−x²). "Both weight the same dipole channels differently." g_e = (1/π)∫Im α_e(x)/x² dx. "Ratios of removal energies cannot determine its numerators." "An optical tune-out can cancel a reading while channels remain coupled."
- **20.3.5.** Moving-channel order: a cumulative upward shift of oscillator strength in the matrix order gives positive metric loss. Counter-example kept: four gaps with the same sum rule and two equal polarizabilities, metric up by 1/48.
- **20.4.2, the table of what each representation keeps and loses** (threshold vector, net peel, K(0), Σ(z), trace, Riesz projector, optical measure). A trace-log second variation "differs from inverse-square cross-gap metric weights". The relaxation flow K̇ = −2[[K,K†],K] "vanishes identically for Hermitian K and cannot supply a new closed-atom binding force".
- **20.5 witnesses.** Same K(0) = 0.58, different later kernels. Two states with equal local entropy and energy read ±0.531186 later. Signed offset ϑ = log det(I−C) − log det C = log(s₀/s₁) keeps a sign that entropy loses. log J = (log 2)I + N/2 keeps the nilpotent part that the trace drops.
- **Section 21, ten ladders.** Li 0.8669, Be 0.3228, B 0.5039, C 0.3682, N 0.3414, O 0.4412, Cr 0.4180, Cu 0.4485, Xe 0.2672, Au 0.3730 (first steps). The helium-core boundary moves one rung per element: k = Z − 2, Γ falling 0.8669 → 0.6852 from Li to O. Neutral-neighbour comparisons are signed: Be→B −0.058, N→O −0.033. Coinage metals: thresholds order Au > Cu > Ag, peel sizes order Ag > Cu > Au. Gold's third threshold is disputed (30.0 against 34 or 36.6 eV). Xenon 4d channel delays are the one identified measured phase record; the data were located, not retrieved.

## Section 22: the peel inside the projector geometry (the join of the two papers)

- **Proposition 22.1, one number, three readings.** With H in blocks (A, B; B†, D) for retained and peeled parts: E_B = ‖PH(1−P)‖² = ‖B‖² = ½‖[H,P]‖² = Tr K(0). "The first is the weight between a subspace and its complement; the second is the squared speed of the projector when H generates its motion; the third is the zero-lag value of the memory kernel." **"What a peel keeps is therefore stated without reference to a coordinate: the retained block A, the projector P, and the coupling B through which the peeled part still acts. The traits of the title are the readings of that triple that survive when D is no longer observed."**
- **Proposition 22.2, the edge.** For positive d_i, d_j: E₋ = (d_i−d_j)², E₊ = (d_i+d_j)², budget 2(d_i²+d_j²), difference 4d_id_j. (d_i−d_j)/(d_i+d_j) = Γ; E₋/E₊ = Γ²; E₋/(E₋+E₊) = Γ²/(1+Γ²); (E₊−E₋)/E₊ = 1−Γ², the echo weight. Half line Γ² = ½ at z = 3+2√2: first book holds one third. Rim |Γ| = 1: books tend to equal. "These are different circles."
- **Proposition 22.3, the gap-power ladder.** "The metric by Δ⁻², the static response by Δ⁻¹, the commutator norm by Δ²." Γ(z^k) = Γ ⊕ Γ ⊕ … ⊕ Γ (k times). "The static response reads the gap step once and the metric reads it composed with itself." Half power: Γ(z^½) = tanh(¼ ln z), a matter wave at a step. On charges: Γ^scr = r ⊕ r with r = (Z_c−Z_v)/(Z_c+Z_v).
- **22.4, priority.** "The geometry of the retained subspace comes first, and the threshold ladder is the real diameter of its chart. Order, phase and turning are carried by the parts of the triple (A, P, B) that the diameter cannot hold."
- **22.5.** 0 ≤ X_A ≤ F_A ≤ ¼I with X_A = C_AB·C_BA (weight between) and F_A = C_AA − C_AA² (defect); Tr X_A = ‖B‖²; 4Tr X_A ≤ Gaussian mutual information. General books: E₋ = ⅛‖[H,H*]‖², E₊ = ⅛‖H²−H*²‖², the two ends u = ±1 of the pencil K(u) = I − uA + u²(Deg − I). On a holonomy eigenvalue λ: |1−λ|² and |1+λ|², sum 4. "Both are blind to the sign of the transport ... they hold the square of a trace and not the trace. The sign, the direction, the constant and the order of a route are carried by the odd record." Friction weight in the same coordinate: w = (1/χ)(1−Γ_u²)/(1+Γ_u²).

## Section 23: the half line on the ionization chart

- Half line: Γ = 1/√2, z = 3+2√2 = 5.828. "Where a loop of two equal perpendicular steps stops closing as a pure turn."
- **Eight of 5,714 steps lie past it:** first steps of Li, Na, K, Rb, Cs; helium-core openings of Be⁺, B²⁺, C³⁺. Of 675 closed-shell openings only these eight cross. "The line is selective, and it is not a marker of shell openings."
- **One crossing per core line.** He core: C³⁺ 6.080 past, N⁴⁺ 5.640 inside. Ne: Na 9.201 / Mg⁺ 5.330. Ar: K 7.286 / Ca⁺ 4.289. Kr: Rb 6.533 / Sr⁺ 3.888. Xe: Cs 5.947 / Ba⁺ 3.583. Rn: none, Fr starts at 5.50. High-charge limits (n/(n−1))²: 4, 2.25, 1.78, 1.56, 1.44, 1.36.
- **Alkali charge ratio.** Z_c/Z_v: Li 1.873, Na 2.022, K 2.024, Rb 2.045, Cs 2.032, Fr 2.010. From Na to Cs it is one number (spread 1.1%). In charges the half line is Z_c/Z_v = (1+√2)(n−1)/n, rising toward the silver ratio. Γ^scr is constant at 0.607 to 0.614, so "the whole descent of the alkali metals toward the half line is carried by the shell part" 5/13, 7/25, 9/41, 11/61. Caesium is the last element past the line (Γ² = 0.507).
- **The 5/8 places the carbon–nitrogen crossing.** Z* = 6.538 with the 5/8, 9.55 without it.
- **Optical phase finds the same five atoms.** At 1.5, 2.0, 2.5 eV the five alkali metals hold five of the six largest reflection phases (p = 2.7×10⁻⁶); reflected power does not separate them (p ≈ 0.09). "The odd reading finds them where the even reading is blind."
- **Three discs are not one disc:** Smith coordinate, tetrahedron shape, chiral grading. A radius 1/√2 on each is a separate statement.

## Section 24 (knots) and 25.1

- A wall is "a nonzero nilpotent: an operator that is not zero and whose square is". Of 575 double Alexander roots on the circle: 81 jump by four, 376 touch (one Jordan block), 118 opposed crossings. Split decided by the second Alexander polynomial in every case.
- Commutator number k = 2 − tr[a,b] = |λ−1|² is the relator defect δ of the projector geometry, δ + g² = 4.
- 24.4: "An ionization ladder is collinear and open: it climbs and keeps no order. A film with phase is not collinear ... A torus knot closes as a pure turn ... The wall and the half line are the places where turning becomes possible."
- **25.1 the loop.** A step is the positive matrix B = exp((r/2)·â·σ), r = ln z. Loop of two perpendicular steps W = B_iB_jB_i⁻¹B_j⁻¹: tr W = 2 − 4 sinh⁴(r/2) = 2 − 4(R/T)², R = Γ², T = 1−R. Turn below Γ² = ½, one Jordan block at it, run beyond. Obliqueness K = 1/(1−2Γ²). z = 3: Γ² = ¼, K = 2. z = 5: Γ² = 4/9, K = 9, centre of turn at ρ² = ½. z = 7: Γ² = 9/16, K = 9, runs. "Two steps whose coordinates multiply to one half are paired across the wall": 2/3 · 3/4 = ½.

## Sections 25.2 to 29 and the appendices

- **25.2 light on the peel disc.** A two-level share c(t) = ½[1 + sin(2κt) sin φ] has peel coordinate Γ = 1 − 2c, metric g = κ² sin²φ, and Γ̇² ≤ 4g(1 − Γ²). "The stored phase sets the reach of the signal: max Γ² = sin²φ." This is the scalar case of the offset speed limit τ̇² ≤ 4gS with g = ½‖Ṗ‖². Here the IQGT metric bounds the speed of a peel coordinate directly.
- **25.3.** Third-axis light: sin φ = Γ/Γ_w with Γ_w = 1/√2, "the form of the law of refraction"; the half line read as the critical angle of the hypersurface (hypothesis, open). "It is a different place from §9, where a refraction rule for the order of filling was tested and failed." Γ(1/z) = −Γ(z): "what changes sign under exchange vanishes on equal entries" (exclusion reading, open). A direction buys a bounded number of distinguishable channels: N ≤ ⌊π/arcsin(√(ε/2)/sin φ)⌋.
- **25.3 also carries the twin-prime word:** frame turn 9.87°, 11.62°, 12.07°, 12.08° to 2×10⁷ and 12.27° at 10⁹; shuffled arms give 23° to 29°; "whether the angle converges is Open".
- **25.4.** Push on a lossless layer P = 2R = 2Γ², K = 1/(1 − P). The wall is P = 1. "That P is the pressure of light on the layers of an atom is a reading and is not tested."
- **25.5.** Atlas placement of every part (B97, B189, B100, B101, B148, B211, B153, W1, W6) and what is on no card: the loop of two perpendicular steps, K = 1/(1 − 2Γ²), the push, the line ⟨K⟩ = 2.
- **Section 26.** Exit line of the gain-and-loss chain: ⟨K⟩ = 1 + u²/(E(0)E(π)) = 2. In peel coordinates of the two band ends: ⟨K⟩ = 2 ⟺ G₀² + G₁² = ½. "The exit line of the chain is the half line shared between the two ends of the band." Three places on the chart: shell wall, half line, rim (table in 26.3).
- **Section 27, colour.** Visible ground line sorted by IE₁ at 6.82 eV (area 0.946); correlation with ln IE₁ 0.897, with Γ₁ only 0.352. "The level carries the response, the shape carries the family", again. Coinage metals: peel order Ag, Cu, Au; absorption-edge order Ag 3.8, Au 2.5, Cu 2.1 eV. "No statement about the half line is made for colour."
- **Section 28.** Tetrahedron shape coordinate G = (z − w)/(z − w̄); volume series D = V₀ − (3√3/4)|G|² + …; a different disc from the Smith disc.
- **Section 29.1 open questions that are about the table:** is P = 2Γ² the pressure of light on a layer of an atom; "A tree on a prime p has p+1 arms at every node, six, eight and twelve for 5, 7 and 11: are these the angles of the lattices of six, eight and twelve neighbours?"; Fr⁺ above or below 23.74 eV; is the alkali optical phase a function of the margin from the half line.
- **Appendix C, ideas held for later (his older coordinates, kept, not used):** spinor cascade and Clifford layers; Kelvin's vortex atoms; "Pressure, volume and principal angles as the modern elemental angle"; d/f response rank; "The historical V_H element numbers, crossing-number element frequencies and element gaps are heuristic coordinates, not measured constants"; the row as one impedance step; **the dual layered Smith volume: per-layer records {Γ_s, |Γ_s|, arg Γ_s, θ_s} stacked over peel depth. "The atomic chart here is its real-axis case."**
- **Appendix D.** The whole test ledger with each kill line and verdict, including every Russell test (T1 to T8, S1 to S3, R7) and the twenty rhythm tests.
- **Appendix G.** The helium-core opening read down the ten ladders: Γ = 0.867 (Li), 0.788, 0.745, 0.717, 0.699, 0.685 (O), 0.626 (Cr), 0.621 (Cu), 0.608 (Xe), 0.600 (Au): falling onto the shell part 3/5 exactly as the charge grows.

## Coverage record

Read line by line: title page to Section 29.1; Appendices A, B, C, D, E, E.1, E.2, F; Appendix G ladders for Li, Be, B, C, N, O, Cr and the first 24 rungs of Cu. Read by parse only (rows tabulated by script, not eye): the rest of Cu, and the Xe and Au ladders, 212 rows. Figures: captions read; images not viewed. Nothing skipped otherwise.
