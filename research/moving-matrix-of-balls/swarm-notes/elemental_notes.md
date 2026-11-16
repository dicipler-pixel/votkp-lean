# Reader notes: VOTKP: Elemental Structure and Response

Source: Google Drive file 1-upIjHRVCgb97WixiTIXIx0zTfVZqkxH, read via read_file_content on 2026-11-15.
Local text copy: /tmp/claude-0/-home-claude/f86429e3-e32f-50e6-b1fd-fcadab5264af/scratchpad/work/elem.txt (49,909 characters, 735 lines).

## 0. How much was read, and what is missing

- The text extraction was NOT cut short. It runs from the title through page footer "Elements manuscript 21" (the References), 21 printed pages. Every prose section, Appendix A (all 118 rows) and the reference list were read.
- BUT: every display equation and almost every inline mathematical symbol is absent from the extraction (they are evidently not text in the PDF). Sentences read like "Let  be the atomic number and  the initial nonnegative charge". So NO equation in this paper was read as printed, except a few inline ones in Section 3 that survived as plain characters (listed in section 3 below).
- The paper has NO printed equation numbers in the extracted text. Equations below are listed in order of appearance with my own labels (Q1, Q2, ...), not his.
- Figures 1, 2, 3: only captions read. Images NOT READ.
- Table of superheavy CIPT thresholds: partly scrambled by extraction; the rows for Ds, Rg, Cn were recovered. Any other rows of that table (if there are any) NOT READ. Column headers recovered: Element / Initial charge range / Thresholds in cm^-1, ordered by charge / First [peel coordinate, symbol missing] / Added charge keys absent from ASD and earlier structured theory records.
- The "electronic supplement attached to this PDF" (data, code, SHA-256 manifest) NOT READ (not reachable through text extraction; file not downloaded per instruction).

Marking used below:
- READ = present in the extracted text verbatim.
- REBUILT (checked) = symbol/equation missing; rebuilt from surrounding prose AND confirmed by reproducing a number printed in the paper.
- REBUILT (unchecked) = rebuilt from surrounding prose only; no printed number available to confirm it. Treat as my reading, not his print.
- NOT READ = missing, not rebuilt.

## 1. What the paper is

- Title (printed): "VOTKP: Elemental Structure and Response"
- Subtitle: "Ionization Ladders, Boundary Conditions, and Retained Information across 118 Elements"
- Author: Jeromie Beasley
- Date line: "11 November 2026 Research manuscript · 11 November 2026"
- Version: no version number is printed. Running footer: "VOTKP: Elemental Structure and Response · Elements manuscript <page>". It calls itself a "Research manuscript". No AI-assistance disclaimer line appears in the extracted text. No DOI for this paper itself is printed.
- Length: 21 pages. Sections: Abstract; 1 Introduction; 2 Elemental ionization methods and results; 3 Operator records beyond the threshold ladder; 4 Environment, pressure and the state needed for response; 5 Optical response, perception and internal colour; 6 Discussion: what the elemental record determines; 7 Conclusion; Data, code and provenance; Appendix A Coverage of all 118 elements; References (main; Environment and matter sources E1-E9; Colour and tree source editions C1-C7).
- Self-description (abstract, last sentence): "The result is an elemental record and a mathematically specified response framework, rather than a derivation of all atomic properties or the Standard Model from one scalar coordinate."
- What it builds on (his words, Intro): "VOTKP begins with a deliberately modest object: the ordered energies required to remove successive electrons. Their dimensionless adjacent ratios expose shape independently of an overall energy scale." "Dirac Time complements this approach by asking which differences remain distinguishable under a declared family of subsequent observations. IQGT supplies geometry only after a state or projector family has been specified. The three roles are compatible, but they are not interchangeable definitions of an atom."
- Reference object: "a family of records: element, charge and state; the source-resolved threshold ladder; specified excitation and coupling data; preparation and environment; and the chosen observable. A reduction is an optional map from that record, with its lost information stated explicitly. There is no claim that a single quotient, metric or tree endpoint retains every physically relevant distinction."
- Four kinds of result, as he grades them (Intro): (1) "reproducible data transformations and bounded statistical comparisons"; (2) "exact algebraic identities and counterexamples"; (3) "mathematical models with explicit physical assumptions, such as ideal Saha equilibrium"; (4) "proposed identifications tested against their own failure criteria. A failed identification remains part of the scientific record".
- Principal additions (Intro): "the full charge-slot census, a coherent superheavy supplement, repaired uncertainty enclosure and charge adjacency, and explicit tests linking retained information to boundary and dynamical response." Explicit disclaimer: "Standard Schur elimination, moment reconstruction and observability arguments are not presented as newly invented mathematics."

## 2. Objects and definitions (his names)

Section 2.
- Atomic number and initial charge: "Let [symbol missing] be the atomic number and [symbol missing] the initial nonnegative charge of the atom or ion." (Symbols NOT READ; Appendix A uses Z for nuclear charge.)
- Threshold: "the energy required to remove one electron from the relaxed ground state of that charge sector, with the free electron referenced to zero kinetic energy." The neutral threshold is the charge-0 one (symbol NOT READ). "A complete ladder contains [range missing]" - Appendix A fixes this: "For nuclear charge Z there are Z possible successive-removal slots."
- Purpose of the definition: "keeps charge-sector energy differences distinct from transitions between bound states at fixed charge. It also fixes the charge index when ladders are compared at equal remaining electron number."
- Charge slot / charge key: one (element, initial charge) position. 7,021 possible slots in all (= sum of Z for Z=1..118; I checked: 118*119/2 = 7,021).
- Two snapshots: (a) "the threshold archive bundled with The Vector of Traits Kept under Peeling v2.9 (Beasley, 2026b)"; (b) "a NIST Atomic Spectra Database (ASD) v5.12 export retrieved on 11 November 2026".
- Evidence class per row: "E for an unmarked evaluated value, S for a square-bracketed semi-empirical value and T for a parenthesized theoretical or otherwise non-experimentally evaluated value. Blank energies and omitted rows are recorded separately."
- Edge: "An edge joins only consecutive charges with numeric energies in the same source."
- Source identity: "A theoretical series from the literature is given its own source and method identity, including where it overlaps ASD."
- Peel coordinate / adjacent peel: defined on an edge from two successive positive thresholds (display missing; see Q1). The abstract and tables call these "adjacent peel coordinates", "adjacent peels".
- Cayley coordinate: "It is the real Smith-coordinate representation of the threshold ratio introduced in the earlier VOTKP study (Beasley, 2026a)." (See Q1.)
- Composite: the composition of consecutive edges; "the composite preserves the endpoint ratio and discards the interior thresholds."
- Energy anchor: "The ordered coordinates with one absolute energy anchor reconstruct every threshold of the connected component. Across a missing threshold, the two neighboring components require separate anchors."
- Connected component: a run of consecutive charges with numeric energies in one source.
- Remaining electronic binding: sum of a complete suffix of thresholds (from a given charge up to the last); "With the bare nucleus and free electrons at rest defining the electronic zero, the relaxed sector energy is [minus that sum - REBUILT (unchecked)]. For a specified isotope and consistent mass convention, [it] is the electronic binding contribution to the mass deficit."
- Conditional endpoint box / conditional range: the exact extrema of the peel coordinate over the rectangle of the two source margins; "decimal bounds rounded outward. They carry no coverage probability. We leave bounds unspecified when either margin is unavailable."
- Three-threshold window: a contiguous run of three thresholds (two edges), used for composition checks.
- Original diagnostics: the ten elements Li, Be, B, C, N, O, Cr, Cu, Xe, Au (Beasley 2026b, section 21.1 and Appendix G).
- Run 01: "the original Run 01 leave-one-out one-nearest-neighbor group classification with feature scaling fitted within each training fold."
- Thomas-Fermi envelope: "a linearly interpolated finite-[Z, symbol missing] Thomas-Fermi envelope in log-ratio space", subtracted to form the residual (test name TF-RESID-01).
- Declared shell assignment / shell contribution / screening term: under a declared assignment the threshold ratio "factorizes" into (shell factor)(screening factor) [symbols NOT READ]; "the screening term is inferred from the thresholds under the declared shell assignment."
- Proposed (universal) shell marker / half-line test: a stronger proposed marker on the peel coordinate (see Q6), tested against a "specified count set" of closed-shell electron counts (set NOT READ).
- CIPT: "configuration-interaction plus perturbation theory" series from Lackenby et al. FS-CCSDT: a separate method series for Cn.

Section 3.
- Operator completeness vs threshold completeness: "Extending the table to all 118 element identities ... does not turn threshold completeness into operator completeness."
- Dirac Time roles (v3.0.1 section 3): "distinguishes what survives transport, what remains distinguishable and what responds to a chosen probe. Its predictive quotient in section 2 is relative to a declared evolution and reading. Neither that quotient nor a selected projector is a privileged physical core. Full relational transport remains the reference".
- Lift / declared lift P(eta): a choice of projector path over a scalar record; "A declared lift P(eta) supplies a pullback metric; a positive lower bound on that metric is an additional hypothesis."
- Channel: "Fix an element, charge, preparation and configuration split." Retained block A, hidden block(s), coupling B (and C for a nonreciprocal split), hidden generator E.
- Positive matrix measure dM: "retains both hidden energies and their channel coupling."
- Retained resolvent: [zI - A - Sigma(z)]^-1 (READ), from Schur elimination.
- Feedback kernel K; hidden preparation term (separate terms). General nonreciprocal kernel "B e^{Et} C" (READ); reciprocal selfadjoint zero-lag identity "K(0)=BB†" (READ).
- Scalar channel measure with r distinct real support energies and positive weights; moments m_j = sum_a w_a E_a^j (READ); Hankel matrix H_r = (m_{i+j})_{0<=i,j<r} (READ); Jacobi realization J (real symmetric tridiagonal).
- Projector metric: from differentiating P^2 = P (display missing, see Q14).
- Hermitian transport generator G with P' = -i[G,P] (READ).
- Connection energy identity: Hermitian vertex operators D_i, anti-Hermitian edge transport A with unitary edge blocks, H = D + A (READ). "This connection-energy identity measures mismatch under declared transport, not an elemental mass or a universal dynamical clock."
- Weighted-gap readings: for fixed nonnegative coupling weights and positive active gaps, three quantities with inverse-square, inverse, and squared gap weights (see Q16).
- Boundary record: covariance 0<C<I on an interior B plus one boundary site x; tau = logdet(I-C) - logdet C (READ); residuals s0, s1 (definitions missing, see Q17); protected interior: det C_B = det(I - C_B) (Atlas B204).
- Principal cosines of two rank-k subspaces; three readings (mean overlap, fidelity, determinant - names from the prose; displays missing).
- Bargmann invariant (Atlas B206): the oriented three-ray loop quantity.

Section 4.
- Finite Saha model for a single nuclear species (from Matter, Then On Down, edition 4, section 6 [E1]).
- Number density of nuclei; number density in each charge sector; Saha coefficients (positive, "including the specified internal partition ratios and ionization energies", held fixed); material pressure; equilibrium mean charge. Symbols NOT READ.
- "Synthetic one-rung control": a one-rung model whose coefficient depends on density.
- Density-compensated endpoint ratio: the inverse-Saha quantity that "gives the binding sum".
- "A declared state, its evolution and a specified readout" = the transferable construction.

Section 5.
- Frozen elemental classifier: predicts a visible ground-state electric-dipole line from first ionization energy (inequality NOT READ).
- Receiver matrix, filter, projector onto [a subspace - missing] : metamer-survival condition (display NOT READ).
- Mixin positive-channel metric: separates into a brightness coordinate and a chromatic metric (display NOT READ).
- Ledger model vs logarithmic model vs sine model: competing perceptual response fits (Colour Selects the Leader v1.2).
- "The Ball": its "three spatial boosts generate the six-dimensional Lorentz algebra"; "Ball coordinates"; "arm labels"; "path mixers"; "pair mixer"; "internal three-port triangle"; "Lorentz boost tree" / "rational tree"; "democratic axis"; "45-degree cone" (Koide cone).
- Internal colour: "a proposed three-state gauge interpretation" (The Standard Model in the Ball).

## 3. Equations in order of appearance (no printed numbers; labels Q* are mine)

Q1. Peel coordinate definition (Section 2, "Peel coordinate, composition and energy anchor"). Display missing. Prose: "For successive positive thresholds, define [..]. The Cayley coordinate lies in [..]. It is the real Smith-coordinate representation of the threshold ratio ... Inverting gives [..]. Reversing an edge sends [..] to [..] and [..] to [..]. For two consecutive edges, the addition law for [..] gives [..]."
   REBUILT (checked): with thresholds I_q, I_{q+1} (my symbols), ratio z = I_{q+1}/I_q, log step r = ln z, Cayley coordinate
     Gamma = (I_{q+1} - I_q)/(I_{q+1} + I_q) = (z-1)/(z+1) = tanh(r/2), lying in (-1, 1).
   Check: the printed "First" coordinates in the superheavy table are reproduced exactly from the printed wavenumbers: Ds (141,108-81,933)/(141,108+81,933) = 0.265310; Rg 0.312287; Cn 0.305762. So the Cayley form is confirmed. The symbol names (his letters for threshold, ratio, log step, Cayley coordinate) are NOT READ. The identification of the "peel coordinate" name with the log step vs the Cayley coordinate: the abstract says "adjacent peel coordinates"; the table column of Cayley values is headed "First ..." with the symbol missing. Which of the two he calls "the peel" in this paper is NOT READ.
   Inversion REBUILT (unchecked): z = (1+Gamma)/(1-Gamma), r = 2 artanh(Gamma).
   Reversal REBUILT (unchecked): r -> -r and Gamma -> -Gamma.
   Addition law REBUILT (unchecked): the hyperbolic-tangent addition law, Gamma_13 = (Gamma_12 + Gamma_23)/(1 + Gamma_12 Gamma_23); log steps add.

Q2. Iterated composition. Prose: "Iterating gives [..]. The second equality follows by cancellation of the intervening logarithms. Consequently the composite preserves the endpoint ratio and discards the interior thresholds."
   REBUILT (unchecked): sum of the adjacent log steps from charge a to charge b = ln(I_b/I_a); composite Cayley coordinate = tanh( (1/2) * sum of r ) = (I_b - I_a)/(I_b + I_a).

Q3. Remaining electronic binding. Prose: "A complete suffix from [..] to [..] gives the remaining electronic binding [..]. ... the relaxed sector energy is [..]."
   REBUILT (unchecked): binding of charge sector q = sum of thresholds from q to Z-1; relaxed sector energy = minus that sum (zero = bare nucleus plus free electrons at rest).

Q4. Endpoint uncertainty. Prose: "For [..] and [..], the derivatives of [..] are [..] and [..], respectively. Where a joint covariance is available, these give the first-order variance [..]." Display NOT READ. Text facts: "Consecutive peels share one threshold. Their propagated errors can therefore be correlated even if threshold errors are independent."
   (If the coordinate is Gamma = (b-a)/(b+a) the derivatives are -2b/(a+b)^2 and 2a/(a+b)^2 - REBUILT (unchecked); which coordinate he differentiates is NOT READ.)

Q5. Conditional range: "When only source margins [..] and [..] are given and [positivity condition missing], we report the conditional range from [..] to [..]. These are the exact extrema on the stated endpoint rectangle". Display NOT READ. (Monotonicity implies the extrema are at opposite corners of the rectangle - my remark.)

Q6. Shell factorization (Section 2, "Shell boundaries and the half-line test"). Prose: "For a declared assignment [..], the ratio factorizes into [..]. The corresponding Cayley coordinates compose under [..]. For [..], the shell contribution is [..], with maximum [..] at [..]." All displays NOT READ. Then: "the stronger proposed marker [..], equivalent to positive [..] and [..]. Use [..] and the specified count set [..]." NOT READ. The heading "half-line test" and the phrase "equivalent to positive ... and ..." are consistent with a marker of the form Cayley coordinate > 1/2 (i.e. ratio > 3) but this is NOT confirmed by any printed number - do not quote it as his.

Q7. Proposition 1 matrices (Section 3). Prose: "Let [display missing]. For every real x, P is an orthogonal rank-one projector and H has spectrum {0,2}. Direct differentiation gives [display missing]. The constant projector P0 = diag(1,0) gives the same spectrum through H0 = 2(I - P0), but has zero speed." READ: P0 = diag(1,0); H0 = 2(I - P0); spectrum {0,2}; "explicit rational parametrization". The explicit P(x), H(x) and the speed formula are NOT READ.

Q8. Channel block form and measure. "For a finite selfadjoint Hamiltonian write [display missing]. The positive matrix measure dM retains both hidden energies and their channel coupling. VOTKP section 20.3.3 expresses this same record as [display missing]." NOT READ.

Q9. Retained resolvent: [zI - A - Sigma(z)]^-1 "wherever the required inverses exist" (READ).

Q10. Time-domain retained equation: "With hbar=1, eliminating the hidden Schrodinger amplitude yields [display missing]. The hidden preparation and feedback kernel are separate terms." NOT READ. READ facts: nonreciprocal kernel is B e^{Et} C, "its vanishing need not force B=0"; reciprocal selfadjoint case K(0) = BB†.

Q11. Proposition 2 proof. READ: m_j = sum_a w_a E_a^j; H_r = (m_{i+j})_{0<=i,j<r} = V diag(w) V^T with V an invertible Vandermonde matrix, hence positive definite. "Solve [display missing]" - the linear system for the coefficients c_j, NOT READ. READ: monic p(E) = E^r + sum_{j<r} c_j E^j obeys sum_a w_a E_a^i p(E_a) = 0 for i<r; invertibility forces p(E_a)=0; roots recover energies; second Vandermonde solve recovers weights; orthogonalizing 1, E, ..., E^{r-1} in L^2(mu) makes multiplication by E a real symmetric tridiagonal Jacobi matrix J. "Consequently [display missing]" - NOT READ. READ: "The cyclic dimension and infinite Hankel rank equal r."

Q12. Moment counterexample. "The positive measures [display missing] share moments m0...m3 = (1,2,5,14), but have m4 = 41 and 44." READ numbers. For p(E) = (E-1)(E-3) (READ), integral of p^2 d mu is 0 and 3 respectively (READ). The two measures themselves are NOT READ. (My check: equal weights 1/2 at E=1 and E=3 give moments 1,2,5,14,41 and integral 0, consistent with the first being that two-atom measure; the three-atom measure is NOT READ.)

Q13. Projector metric. "For a differentiable orthogonal projector, differentiating P^2=P gives [display missing]." NOT READ. READ: "If P' = -i[G,P] for a Hermitian transport generator G, this metric equals ||P G (I-P)||^2; for rank one it also equals Var_psi G." Any normalisation factor in the metric is NOT READ.

Q14. Connection-energy identity. "For H = D + A, [display missing]." READ: "[H,H†] = -2[D,A]; opposite edge blocks contribute equal norms, and right multiplication by a unitary preserves the norm. Without unitarity the correct edge term remains ||D_i A_ij - A_ij D_j||^2." The displayed identity (constant, sum over edges) is NOT READ.

Q15. Weighted-gap quantities. "For fixed nonnegative coupling weights and positive active gaps, define [display missing]. Cauchy-Schwarz gives [inequality missing]." NOT READ. READ: "inverse-square gap weights enter projector geometry, inverse-gap weights enter ground-state static response, and squared-gap weights enter the commutator norm." "Equality requires the relevant powers of the active gaps to be proportional on the positive-weight support. A single active gap is sufficient, while signed weights invalidate the general inequality."

Q16. Boundary Schur identity. "For a covariance 0<C<I on an interior B plus one boundary site x, define [display missing]." READ: tau_{B+x} = tau_B + log(s0/s1), where tau = logdet(I-C) - logdet C.
   REBUILT (checked): s1 = C_xx - c^T C_B^-1 c and s0 = (1 - C_xx) - c^T (I - C_B)^-1 c, with c the interior-to-boundary coupling column. Check against his printed example: C_B = diag(1/4,3/4), C_xx = 1/2, c = (1/8,0) gives s1 = 7/16, s0 = 23/48, s0/s1 = 23/21, and tau_B = 0, so e^tau = 23/21 as printed; c = (0,1/8) gives 21/23 as printed.

Q17. Principal-cosine readings. "For two rank-k subspaces, their squared principal cosines give three further readings: [display missing]. The arithmetic-geometric mean inequality and nonnegative variance imply [inequality missing], with [equality condition missing]." NOT READ. READ: "The first k power sums recover the principal-cosine multiset by Newton identities. A mean overlap alone does not: the lists (1,0) and (1/2,1/2) have the same mean but different fidelity and determinant."

Q18. Bargmann invariant. READ: rays (1,0), (1,1)/sqrt2 and (1, +-i)/sqrt2 have every pairwise projector overlap 1/2, "while [display missing]". The value is NOT READ. (My computation: the cyclic triple product is (1 +- i)/4 up to conjugation convention; not his print.)

Q19. Saha equilibrium and neutrality. "With [..], the equilibrium and neutrality equations are [display missing]. Write [..], [..], and [..]." NOT READ.

Q20. Pressure proposition display: "the equilibrium mean charge satisfies [display missing]". NOT READ. Proof skeleton READ in words only: weights from adjacent ratios; differentiating the weights; "The neutrality equation has a unique positive root" (function "increases strictly, is negative as [..], and is positive at [..]"); implicit differentiation; "The pressure counts one neutral or ionic particle per nucleus and each free electron"; chain rule; "All charge fractions are positive".
   What can safely be said: sign only - at fixed temperature and fixed Saha coefficients, mean charge decreases as material pressure increases (confirmed in Discussion: "Fixed-coefficient ideal equilibrium predicts a decrease in mean ionization with increasing material pressure").

Q21. One-rung example: "a one-rung model with [..] and [..] in common density units has [..], [..], and derivative [..]." All numbers NOT READ.

Q22. Inverse Saha: "Under the Saha equations, [combination missing] eliminates the common electron density and leaves a partition term and an adjacent threshold difference divided by [kT, symbol missing]." NOT READ as display. "For a synthetic helium partition [..], omitting its temperature dependence biases the reconstructed first peel by about [value missing]." NOT READ.

Q23. Visible-line classifier inequality: "when the first ionization energy satisfies [missing]"; oscillator/strength condition "with [missing]". NOT READ.

Q24. Metamer survival condition: "For receiver matrix [..], filter [..], and projector [..] onto [..], every initial metameric match survives precisely when [display missing]". NOT READ.

Q25. Mixin metric separation: "Its positive-channel metric separates as [display missing] with zero symbolic residual." NOT READ.

Q26. Arm coherent states and matrix-unit commutators: "assigns coherent states [missing] to arm labels. Matrix units satisfy [display missing]. Exact computation checks all 81 such commutators." NOT READ (81 = 9 x 9 matrix units).

Q27. Koide cone equation: "No nonzero [rational triple - symbol missing] satisfies [display missing]. After clearing denominators to a primitive integer triple, expansion gives [display missing]. Reduction modulo 4 forces all three coordinates even, contradicting primitivity. This is the 45-degree cone about the fixed democratic axis." Displays NOT READ.

## 4. Results with the status the paper gives

A. Data transformations and bounded statistical comparisons (his kind 1)
1. Census: both snapshots contain 5,847 numeric thresholds among 7,021 possible charge slots; 5,714 adjacent peels each. Status: reproducible data result. (I re-summed Appendix A: 5,847 / 7,021; E/S/T 311/919/4,617; 156 E/E pairs in 60 elements; 56 theory entries; 103 complete, 7 partial, 8 empty - all match the body.)
2. "Exact reconstruction and composition are verified on both snapshots." Detail: "All adjacent inversions and three-threshold compositions were checked with exact rational arithmetic on the reported decimal energies." Status: verified, exact.
3. "No numerically complete ladder has grade E at every rung." (Discussion: "none of the 103 complete baseline ladders consists entirely of evaluated E entries.")
4. Run 01 group classification repeated: "Archived and current energies yield identical aggregate scores." Shape beats uncentered log energies and shuffled shape (numbers in section 5). Scope stated: "These results apply to the original finite sample with mixed evidence grades."
5. Thomas-Fermi comparison (registered, TF-RESID-01): residual and original shape both 0.951, envelope alone 0.000 at the main setting. His reading: "supports a distinction between the broad ionization envelope and the finer structure used by this classifier, within the specified sample and fitting rule." Abstract: "Registered K=10 group-classification results survive Thomas-Fermi envelope removal and the four neutral-threshold revisions."
6. Li through O shell/screening total decreases from 0.8669235 to 0.6851797 (thresholds whose initial ions have three and two electrons). Caveat he gives: "Each pair contains a theoretical endpoint."
7. Superheavy supplement: 56 source/model rows over 53 charge keys, 40 outside numeric ASD, 41 within-source adjacent peels, 11 keys absent from both ASD and the earlier structured theory tables. Status: "source-supported theoretical values"; "These low-charge calculations leave the deeper gaps and the experimental status unchanged."
8. Gold interior perturbation: varying the disputed interior threshold through 30.0, 34.0, 36.6 eV changes the two neighbouring coordinates but "All three compose to [same value, NOT READ]. Thus a reproducible change in the neighboring coordinates can coexist with exact agreement of the composite. Discrimination among the physical threshold estimates requires the ordered record and independent evidence about the intermediate ion."

B. Exact identities and counterexamples (his kind 2)
9. Proposition 1 (nonunique spectral lift): "Even a complete prescribed spectrum does not determine the path of a spectral projector or its intrinsic length." Proved by explicit example. "the scalar record cannot choose between the two lifts." It is "the constructive obstruction of VOTKP section 19.4 in an explicit rational parametrization."
10. Proposition 2 (finite scalar channel realization): a scalar channel measure with exactly r distinct real support energies and positive weights is determined within this class by moments m_0..m_{2r-1} and admits an exact r-dimensional Jacobi realization. Proved. Graded by him as standard: "These are standard finite moment and spectral-realization constructions, applied here to the channel record of VOTKP. The known-r assumption matters."
11. Moment counterexample: two positive measures share m0..m3 = (1,2,5,14) but m4 = 41 vs 44. "four moments recover a known two-atom measure without excluding a three-atom alternative." "Positivity turns exact vanishing into a support certificate; noisy smallness requires a separate conditioned inference. Multiple channels likewise require matrix cross-moments, since independent scalar fits can lose interference."
12. Projector metric identities: metric = ||PG(I-P)||^2 under P' = -i[G,P]; rank one = Var_psi G. Attributed to The Weight Between v1.1, Proposition 5. Warning: "In Proposition 1 the moving projector commutes with its instantaneous H; identifying projector motion with physical time evolution would therefore be incorrect."
13. Connection-energy identity for H = D + A (exact, [H,H†] = -2[D,A]). Its relation to gap-weighted geometry "requires the couplings and gaps used in The Weight Between, Proposition 6, rather than an identification from scalar resemblance."
14. Cauchy-Schwarz inequality linking the three gap-weighted readings (exact, with equality conditions; fails for signed weights).
15. Boundary Schur identity tau_{B+x} = tau_B + log(s0/s1), and the counterexample that a protected interior "does not cancel the interior dependence inside the residuals": e^tau = 23/21 vs 21/23.
16. Principal-cosine readings: mean overlap alone does not determine the multiset; first k power sums do.
17. Bargmann (Atlas B206) phase obstruction: "Pairwise magnitudes therefore do not determine the oriented loop."
18. Summary sentence of Section 3: "They establish compatible exact maps without asserting that an unmeasured operator record has already been recovered for every element."
19. Internal gauge algebra: "The Ball's three spatial boosts generate the six-dimensional Lorentz algebra, not eight-dimensional [su(3) - symbol missing; Discussion says 'internal SU(3)']." Constructive internal extension: two path mixers close into a three-dimensional algebra; adding the independent third pair mixer yields eight traceless anti-Hermitian directions. "Coherence and independent controls are additional structure. An internal three-port triangle is not a spacetime plaquette."
20. Koide rational obstruction (exact): no nonzero rational point on the 45-degree cone about the fixed democratic axis; "Exact direct alignment is therefore excluded under those hypotheses. Arbitrarily close alignment, irrational axes and separately specified real mass maps remain outside the exclusion." ([C7]: "distinct from the centered-book Koide construction of atlas B200".)

C. Models with explicit physical assumptions (his kind 3)
21. Pressure Proposition (unnumbered): "At fixed [temperature] and [Saha coefficients], the material pressure increases strictly with [nuclear density], and the equilibrium mean charge satisfies [display NOT READ]." Proved within "a dilute, nondegenerate, ideal mixture in local thermodynamic equilibrium", single nuclear species, "no other species or reservoirs of free electrons." Conclusion in words: mean ionization decreases with increasing material pressure.
22. Synthetic one-rung control with density-dependent coefficient: mean charge increases with density. "This control establishes sensitivity to the coefficient dependence. It does not supply a dense-plasma model."
23. Inverse Saha: "Known partitions and two temperatures then recover the ladder within the model." "This is an inversion of modeled populations under declared equilibrium, with the isolated ladder as an input to the forward calculation."
24. Free-streaming control (Matter, Gases and VOTKP [E7, section 8]): "positive velocity distributions with equal initial density, flow and stress that acquire different later density under free streaming".
25. Finite angular neutrino example ([E8, section 9]): "higher Legendre moments can likewise leave the initial stress unchanged and alter its future." Two-mode preparation gives 36.27% greater integrated-output norm than the pure mode at the same guaranteed minimum intensity 0.75. Limits: "The mixture falls outside the conservative weighted coefficient budget in [E8] ... It supplies no collapse threshold or atomic collision law."
26. Standard Model representation attached to the tree: "109 generator checks, standard charge assignments, anomaly cancellation and Higgs breaking pass. The construction imports matter representations, generations, couplings and Yukawa matrices." "These results establish compatible mathematical attachments, not a derivation of Standard Model dynamics from threshold or Ball geometry."

D. Proposed identifications tested against their own failure criteria (his kind 4)
27. FAILED - proposed universal shell marker: "Only eight of the 675 true adjacent steps in the set cross, or 1.19%, below the proposed minimum of one half." "In this sample crossing is selective, and its converse fails." Abstract: "a proposed universal shell marker fails after correction of missing-charge indexing."
28. FAILED - THIN-01 real-film predictions: "Both registered criteria fail. This failure does not invalidate the Airy identity; it rejects those predictive readings of the archived real-film comparisons."
29. FAILED - "the tested universal shell-ridge interpretation fails, including negative prominence for Xe-like Ce 4+."
30. FAILED - "The Lorentz boost tree does not generate internal SU(3) merely because a projection resembles its weights."
31. PASSED within scope - frozen visible-line classifier (accuracy 0.83077, AUC 0.94595). Limit: "This calculation reuses saved spectral labels: the original raw line-query exports are unavailable." "The restricted association therefore neither reconstructs line strengths nor determines condensed-phase colour."
32. Gold metamer witness: computed failure of the survival condition (receiver calculation). "These are receiver calculations, not measured perceptual differences."
33. Film sweep: exact enhancement-circle criterion matches 171/171 "with the same detection threshold as the labels".
34. Mixin: "passes 18 declared algebraic checks"; identifies "a brightness coordinate and a chromatic metric within the specified representation. It does not provide material optical constants or wavelength-dependent retardance."
35. Perception v1.2 rerun: 150/150 fits converged. Grey: logarithmic model better. Green/pink: ledger beats log, sine best. Blue/orange: small ledger advantage. "Results distinguish the stimulus families rather than declaring one universal perceptual ruler." "The corrected grey ranking reverses the older protocol's ranking while retaining every grey response."
36. Finite gauge / ordered-monodromy branch (Discussion): "Fresh local window and two-square certificates, rational allocation witnesses, and direct positive-semidefinite comparisons survive their stated tests. Electric-cutoff retention fails at weak coupling, and torus harmonic zero modes cannot all be classified as gauge directions. ... They establish neither a continuum Yang-Mills mass gap nor an elemental mass law."

Headline sentences (Discussion/Conclusion):
- "An anchored, connected ionization ladder is recovered exactly from its directed peel coordinates."
- "These are explicit transformations of supplied records. Their validity does not fill in missing physical inputs."
- "The response extension requires more than a threshold coordinate. Channel weights, projector lifts, preparation, environment and readout determine which histories are distinguishable."
- "Mechanical compression, an electron reservoir, screening, optical termination and collision history cannot be substituted for one another by calling each an outside pressure."

## 5. Numbers (with units and source)

Census (Section 2 table, per snapshot; both snapshots identical in keys):
- Possible charge slots: 7,021. Numeric thresholds: 5,847. ASD blank energies: 172. Charge slots with no row: 1,002. (5,847+172+1,002 = 7,021.)
- Complete ASD ladders, H-Lr: 103. Partial ASD ladders, Rf-Ds: 7. Elements without numeric ASD thresholds, Rg-Og: 8.
- Numeric thresholds by grade E / S / T: 311 / 919 / 4,617.
- Adjacent peels: 5,714. Contiguous three-threshold windows: 5,584.
- Peels with conditional endpoint boxes: 5,691.
- Evaluated-to-evaluated (E/E) pairs: 156, in 60 elements.
- 51 elements outside the original ten diagnostics have at least one E/E edge. Hg has six; V, Fe, As, Br each have five.
- Snapshots differ numerically only at neutral S, Ca, Nd, Np; newer ASD reference keys: Civis et al. (2024), Pak et al. (2022), Miyabe et al. (2024), Kaja et al. (2024) respectively.
- Derived by me from Appendix A: if no gaps, peels would be 5,737; printed 5,714 implies 23 interior gaps, matching his "23 nonadjacent pairs".

Classification (Run 01, leave-one-out 1-nearest-neighbour, group label; 61 eligible elements; K values' symbols missing - abstract names "K=10"):
- At the main adjacent-step setting: log-ratio shape accuracy 0.951; uncentered log energies 0.508; shuffled shape 0.039.
- Shape scores at two other settings [values of the setting NOT READ]: 0.515 and 0.738.
- Thomas-Fermi: at [main setting] residual 0.951, original 0.951, envelope alone 0.000. At [other setting] residual 0.723 vs original shape 0.738.

Shell / half-line:
- Li through O total (shell x screening Cayley total, three-electron vs two-electron initial ions): decreases from 0.8669235 to 0.6851797 (dimensionless).
- Marker test: eight crossings in both snapshots, all at a count in the specified set; 8 of 675 true adjacent steps = 1.19%; proposed minimum one half. Compressing rows across gaps admits 23 nonadjacent pairs and changes denominator 675 -> 694.

Superheavy CIPT (Lackenby, Dzuba, Flambaum 2020, Table VIII; wavenumbers cm^-1, successive one-electron removals; eV conversion "divides by [constant NOT READ]"):
- Ds, initial charge 0-3: 81,933; 141,108; 240,185; 328,830. First coordinate 0.265310. Added keys 1-3.
- Rg, initial charge 0-4: 90,132; 171,989; 250,503; 338,736; 439,861. First coordinate 0.312287. Added keys 1-4.
- Cn, initial charge 0-5: 97,956; 184,241; 260,665; 351,903; 451,630; 566,242. First coordinate 0.305762. Added keys 2-5.
- (Added keys: 3 + 4 + 4 = 11, matching "Eleven keys".)
- My computed Cayley coordinates for the later edges (not printed in the extraction): Ds 0.259845, 0.155787; Rg 0.185835, 0.149741, 0.129881; Cn 0.171776, 0.148943, 0.124111, 0.112600.
- Consolidated literature record: 56 source/model rows; 53 charge keys; 40 outside numeric ASD; 41 within-source adjacent peels; 11 new keys.
- FS-CCSDT series for Cn "gives first [value NOT READ]" (Kaygorodov et al. 2022).

Gold: two outer thresholds [values NOT READ] eV held; disputed interior threshold 30.0, 34.0, 36.6 eV (scenarios from Beasley 2026b section 21.1.10); resulting coordinate pairs and composite NOT READ.

Section 3 worked numbers: spectrum {0,2}; moments (1,2,5,14), m4 = 41 and 44; integral p^2 = 0 and 3; C_B = diag(1/4,3/4), C_xx = 1/2, c = (1/8,0) or (0,1/8), e^tau = 23/21 and 21/23; cosine lists (1,0) vs (1/2,1/2); pairwise overlaps 1/2.

Section 4: SmS discontinuous reflectivity change "near [..]-[..] GPa" (pressure values NOT READ), golden metallic phase (Kirk et al. 1972; Mizuno et al.). Neutrino two-mode: 36.27% greater integrated-output norm; guaranteed minimum intensity 0.75. Helium partition bias value NOT READ.

Section 5:
- Visible-line classifier: target = allowed neutral-gas E1 transition in 380-780 nm. 65 classifiable held-out elements; 37 positive labels; 54 correct. Confusion: 27 TN, 1 FP, 10 FN, 27 TP. Accuracy 0.83077; majority baseline 0.56923. AUC 0.94595 (exact historical and comparison-snapshot energies); 0.94546 with workbook rounding.
- Gold metamer: archived four-band pair matches initially "to numerical precision" and separates after reflection by [value NOT READ], using tabulated gold optical constants, D65, CIE 1931 observer. Neutral 50% filter preserves the match to an XYZ residual of [value NOT READ]. Consistent-quadrature version: strongest singular-vector pair has initial [value NOT READ], post-gold separation 18.35 (units/colour-difference metric NOT READ).
- Film sweep: 171 metal-wavelength-substrate cases, 57 distinct front reflections. First-order phase-sensitive predictor matches 171/171 bump labels. Fitted scalar threshold 170/171; previously frozen threshold accuracy 0.871. Holding out metals: 0.977 or 0.959 by threshold convention. Exact enhancement-circle criterion 171/171.
- THIN-01: 15 thick-film cases, median absolute reflectance mismatch 0.0104, 11/15 agreement on the side of bulk reflection. 18 ultrathin cases, median mismatch 0.0138 = 1.3 times thick-film value; registered factor was "exceeding 2".
- Mixin: 18 declared algebraic checks pass.
- Perception v1.2: 150/150 fits converged; 91,896 grey and 45,060 chromatic responses; 742 repeated chromatic export rows removed. Ledger minus logarithmic held-out NLL per response: grey response folds +0.0008055; grey whole-triad folds +0.0007753; green/pink record folds -0.0004009; blue/orange record folds -0.0001803. Grey response-fold conditional bootstrap interval [0.0002727, 0.0013558]; 320 clusters are stimulus keys, not participants.
- Gauge: 81 commutators checked; 3-dimensional algebra from two path mixers; 8 traceless anti-Hermitian directions with the third; Lorentz algebra 6-dimensional. Koide: 45-degree cone; reduction modulo 4. Standard Model attachment: 109 generator checks.

Appendix A (per element: numeric/possible, E/S/T, adjacent E/E, theory entries): full table is in the local text copy, lines 391-649. Notable rows:
- H 1/1, 0/0/1, 0, 0. He 2/2, 1/0/1. Li 3/3, 1/0/2. C 6/6, 4/0/2, EE 3. O 8/8, 4/2/2, EE 2. Ne 10/10, 6/2/2, EE 4. Fe 26/26, 9/14/3, EE 5. Au 79/79, 3/3/73, EE 1. Hg 80/80, 7/3/70, EE 6. U 92/92, 4/2/86, EE 3. Lr 103/103, 1/1/101.
- W is printed "74/74, 2 / 69 / 3" (S=69, T=3), unlike its neighbours (Ta 2/4/67, Re 2/4/69). Row sum is still 74 and the grand totals only close with it as printed; whether S and T are transposed for W cannot be decided from the text.
- Partial ladders: Rf 69/104 (0/0/69); Db 70/105 (0/0/70); Sg 71/106 (0/6/65), theory 3; Bh 72/107 (0/7/65), theory 4; Hs 73/108 (0/8/65), theory 5; Mt 68/109 (0/0/68), theory 5; Ds 68/110 (0/0/68), theory 4.
- No numeric ASD: Rg theory 6; Cn 8; Nh 3; Fl 4; Mc 1; Lv 5; Ts 6; Og 2.
- Elements with zero E entries among complete ladders: H (0/0/1), Pa, Fm, Md.
- Appendix rule: "Supplement entries may overlap baseline keys or represent competing models and must not be added to the baseline count as independent measurements."

References carrying identifiers: Beasley 2026a = VOTKP original public edition v1.1, doi 10.5281/zenodo.23011140. Beasley 2026b = VOTKP v2.9, 13 October 2026, doi 10.5281/zenodo.23340757. Dirac Time research edition v3.0.1, 25 September 2026. The Weight Between v1.1, 26 October 2026 (Propositions 5-6). Matter, Then On Down, edition 4, 4 November 2026 [E1]. Elemental / Periodic Table Branch Handoff, 23 September 2026 [E2]. VOTKP and the colours of the elements, project report, 1 November 2026 [E3]. Matter, Gases and VOTKP, formal research edition, 3 November 2026 [E7]. What the Neutrino State Must Keep, research manuscript v6.0, 11 November 2026 [E8]. Colour Selects the Leader v1.2 [C4]. The Standard Model in the Ball, "recovered latestBall v3" [C6]. Atlas cards cited: B200, B204, B206. NIST ASD v5.12 doi 10.18434/T4W30F. Lackenby et al. PRA 99, 042509 (2019); PRA 101, 012514 (2020). Crowley, HEDP 13, 84-102 (2014) [E6]. Kirk et al. PRB 6, 3023 (1972). Mizuno et al. arXiv 0809.1306.

## 6. Limits, failures and open items (as the paper states them)

- "There is no claim that a single quotient, metric or tree endpoint retains every physically relevant distinction."
- Threshold ladder "does not specify the transition amplitudes, phase relations or preparation needed for a response experiment."
- "Actual ionization thresholds compare different electron-number sectors, so identifying them with gaps of one fixed-space Hamiltonian requires an additional construction. Even after that construction, the nonuniqueness remains."
- A positive lower bound on the pullback metric "is an additional hypothesis"; VOTKP sections 19.5-19.6 "further requires preparation, bath weights and a slow-driving regime before projector length implies a dissipation bound."
- Numerical completeness is not experimental completeness; no complete ladder is all-E; superheavy additions are theoretical.
- Endpoint boxes "carry no coverage probability"; "Interval enclosure is geometric enclosure of declared endpoint ranges, not a newly assigned statistical confidence level."
- Across a missing threshold separate anchors are needed; missing measurements are preserved "rather than interpolating them into apparent completeness."
- Classification results are limited to "the original finite sample with mixed evidence grades."
- Failed: universal shell marker (1.19% vs one half); THIN-01 both registered criteria; universal shell-ridge (negative prominence for Xe-like Ce 4+); boost tree generating internal SU(3); direct rational-tree Koide alignment; electric-cutoff retention at weak coupling; torus harmonic zero modes as gauge directions.
- "Neither those thresholds nor a neutral-gas line screen determine a macroscopic specimen's colour."
- "sums of electronic removal energies contribute electronic binding under specified conventions; they do not determine nuclear masses or isotope structure."
- Pressure proposition "applies within the dilute equilibrium model"; the density-dependent control "is a changed assumption, not a dense-plasma equation of state."
- "an equilibrium ionization free-energy difference and a fast spectroscopic threshold refer to different protocols and can differ [E6]."
- Neutrino control "supplies no collapse threshold or atomic collision law."
- Classifier reuses saved labels; raw line-query exports unavailable.
- Grey perception clusters are stimulus keys; "grey participant identifiers are unavailable."
- Tree: "Tree edges alone have no independent Wilson loops; curvature requires further cycles or a spacetime connection. Neutrinos carry no colour charge and require their own weak and coherent flavour description."
- No "continuum Yang-Mills mass gap nor an elemental mass law."
- Provenance limits: "Some replay scripts refer to the previously delivered source/repository package; those dependencies are named rather than silently represented as newly bundled originals." "Numerical examples do not substitute for a fresh Lean build, a missing optical measurement, an unavailable exhaustive search or a nonlinear collapse calculation." [C5]: "the bounded knot replay certified only its first pair before stopping."
- Open, in his words: "unresolved physical maps all kept visible"; an "unmeasured operator record" has not "been recovered for every element."

## 7. Bearing on the four team questions

(a) The peel coordinate and the step r = ln z.
- This paper is the direct source. On an edge of two successive positive thresholds the threshold ratio z gives the log step r = ln z and the Cayley coordinate Gamma = (z-1)/(z+1) = tanh(r/2), which he calls "the real Smith-coordinate representation of the threshold ratio". (Displays missing; Cayley form numerically confirmed against Ds/Rg/Cn; the letters r, z, Gamma are mine/the team's - his printed symbols NOT READ.)
- Structure he states: reversal flips sign; consecutive edges compose by the tanh addition law (log steps add); "cancellation of the intervening logarithms" makes the composite depend only on endpoints: it "preserves the endpoint ratio and discards the interior thresholds."
- Coordinates plus ONE absolute energy anchor per connected component reconstruct every threshold. Missing rung => separate anchors.
- Shell assignment: the ratio "factorizes" into a shell part and a screening part, and "The corresponding Cayley coordinates compose under [the same addition law]".
- Gold shows the lesson: three different interior values give different neighbouring coordinates but the same composite.
- Errors: consecutive peels share a threshold, so their errors are correlated.

(b) Several equal balls on a hyperbolic field with light/energy passing from one to the next.
- The paper has NO construction of several equal balls on a hyperbolic field and no ball-to-ball light or energy transfer. Do not cite it for that.
- What it does contain that is adjacent: (i) the tanh addition law for composing peel steps (adding log steps along a chain - the same rule as composing collinear boosts, though he does not say this about balls here); (ii) "The Ball" of The Standard Model in the Ball: "The Ball's three spatial boosts generate the six-dimensional Lorentz algebra"; "Finite words of rational boosts, including axis boosts of rapidity [value NOT READ], have rational Ball coordinates; their uniquely defined canonical rotation axes also have rational representatives"; the "Lorentz boost tree" whose "Tree edges alone have no independent Wilson loops; curvature requires further cycles or a spacetime connection"; (iii) the connection-energy identity for a graph with Hermitian vertex operators D_i and anti-Hermitian edge transport A_ij with unitary edge blocks: edge mismatch ||D_i A_ij - A_ij D_j||^2 - the stated measure of "mismatch under declared transport" between neighbouring vertices; (iv) the chain-with-hidden-part machinery: Schur elimination, retained resolvent [zI - A - Sigma(z)]^-1, feedback kernel K with K(0) = BB† in the reciprocal case, and the warning that a nonreciprocal kernel B e^{Et} C can vanish without B = 0.
- Warning from Proposition 1 relevant to any matrix-of-balls build: a spectrum (or ladder of ratios) does not fix projector motion; a lift must be declared.

(c) Boundary conditions at walls.
- Exact boundary identity: adding one boundary site x to interior B, tau_{B+x} = tau_B + log(s0/s1), tau = logdet(I-C) - logdet C. A protected interior (det C_B = det(I-C_B), Atlas B204) cancels tau_B but NOT the interior dependence inside s0, s1 (23/21 vs 21/23 example).
- Pressure as a boundary: "The imposed hydrostatic pressure can be identified with this material pressure when it balances the mixture at the boundary and any additional stress contributions are negligible."
- Optical interface: "VOTKP v2.9 already includes the outside medium, substrate and propagation phase in its interface model"; metamer survival condition (display NOT READ); gold reflection breaks a metameric match; film sweep exact "enhancement-circle criterion" 171/171; "exact phase-sensitive boundary identity remains valid" (the Airy identity) while THIN-01 predictive readings fail.
- "Shell-wall criterion" (Discussion's name for the shell marker) fails as a universal marker: 8/675.
- General rule: "retain the mechanism by which the surroundings enter the state equations."
- The paper cites the neutrino manuscript [E8] only for the angular-moment history control; there is no wall construction here.

(d) The Sun and planets.
- Nothing. The words Sun, solar, planet do not occur. The only astrophysically flavoured content is the ideal Saha ionization equilibrium (single species, dilute, nondegenerate, LTE) and the remark on dense plasma (screening, degeneracy, dissolution of bound states), both stated without reference to any star. "sol" appears only as a directory name in archive paths (research/sol/...).
