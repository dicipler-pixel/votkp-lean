# READ B2: VOTKP v2.9, lines 3001–6053 (Round 2, Full Table package, 11 Nov 2026)

## 1. Coverage

- **File:** /home/claude/sm/fulltable_src/VOTKP_Full_Table_Research_20261111/research/sol/v29.txt
- **Version:** VOTKP v2.9. Line 5516 reads "Version 2.9. Written by Claude from Jeromie Beasley's research programme and his collaborators' reviews." The Zenodo status (v2.9 on Zenodo) comes from the memory note and was not checked against this text.
- **Range read:** lines 3001–6053 (the last line of the file), every line, in 400-line chunks, including all ten Appendix G ladders.
- **Characters of text read:** about 185,900 bytes (3,053 lines, including tables, appendices, bibliography and Appendix G).
- **Read in full:** yes, every line of 3001–6053.
- **Not read:** nothing in the range. Lines 1–3000 belong to the other reader.
- **Extraction caveat:** the text export drops many display formulas, leaving blank runs (for example the Proposition 19.1 formula, the §20.1.3 sums, the §20.3.6 onset formula, the A.15 matrices, and the Ag values in §21.1.11). Where a number is blank in the text, I say "missing in export". Where I reconstructed a number from the printed ladder values, I say so.

## 2. What the version defines and claims (lines 3001–6053)

- **Items 32–46 (lines 3001–3038):** a numbered list of takeaways, including item 42 (equal shell parts do not imply equal walls: the screening residue at a wall differs five- to ten-fold between a p-core and a d-shell wall; line 3027) and item 44 (at the 4f shell of row 6 the screening part is negative; line 3032).
- **§19 Directed peels, cancellation and the geometry of a retained subspace (lines 3039–3324):**
  - §19.1 declares strictly positive energies and a directed record; natural units are used only in the synthetic bath calculations.
  - §19.2, Prop 19.1 (directed real peel): the directed coordinate is defined; the composition is associative and commutative; reversal gives the inverse. Line 3081 reads "A negative step reduces an initially positive signed rapidity." Lines 3081–3083 give when a negative step passes the origin.
  - §19.3, Prop 19.2 (cancellation defect): the concatenated record has a traversed length and an endpoint distance. Equality holds "exactly when all nonzero increments have the same sign" (line 3107). The worked example gives zero endpoint and traversed length 1.6 (line 3111). Line 3113 says the distinction "adds route information to §15.2 without changing its endpoint identity."
  - §19.3 packaged-data check: 5,847 stage values, 5,714 adjoining pairs, 56,191 complete windows of one to ten steps reproduce the endpoint composition (lines 3116–3119).
  - §19.4, Prop 19.3 (non-unique Grassmannian lift): the scalar record does not fix the projector path. A constant and a rotating projector give the same eigenvalues and the same reflection (lines 3129–3131). Line 3154: "the eigenvalues alone leave ... undetermined."
  - §19.5, Prop 19.4 (route-sensitive lifted bound): conditional on a nondegenerate lift, a relaxation bath and positive friction weights. Line 3198: the net scalar coordinate can vanish while the cost stays positive under the added hypotheses.
  - §19.6, equality conditions and tests RP-WEIGHT and RP-RANK. Line 3211: "Equality in the length step requires constant intrinsic speed." Line 3213: "Several distinct gaps can have the same weight and saturate the bound." The synthetic example saturates with gaps 1 and 4 at weights 0.8 and 0.8 (line 3224).
  - §19.7, Test RP-POLAR: refraction in the chosen lift; the Clairaut constant and a polar reflection. Line 3269: "Normal incidence can reach the collapsed projector."
  - §19.8: physical realisations and evidence boundaries (recombination, screening, spectral selection, measured subspaces). Line 3309 states the accepted addition.
  - §19.9 reproducibility: check_reverse_peel.py, 5,725 passed assertions, seed 20261011.
- **§20 Energy, coupling and retained response (lines 3330–3948):**
  - §20.1 anchored ground energies and transformation conditions: the ledger over 103 complete ladders; §20.1.3 ground-energy reconstruction; §20.1.4 VOTKP and energy; §20.1.5 dynamics in a sector; §20.1.6 transformation, feedback and memory; §20.1.7 translation across atoms.
  - §20.2 frequency, memory, entropy, mass and delay as separate readings. Line 3486: "For positive thresholds ... give exactly the same ratios and peels." §20.2.1 bath crossover needs a measured timescale. §20.2.2 boundary phase (the Ferranti connection).
  - §20.3 from the peel coordinate to channel-resolved response: §20.3.1 frequency adds an absolute calibration; §20.3.2 the complete ladder carries an electronic binding contribution to mass (103 elements); §20.3.3 Cauchy contours and the retained/hidden Schur reduction; §20.3.4 optical measure; §20.3.5 moving-channel order (Prop A.16); §20.3.6 backreaction and a wall-link onset.
  - §20.4 projector response, feedback and the representations that lose information (table at lines 3879–3902).
  - §20.5 worked witnesses: §20.5.1 same coupling, different frequencies; §20.5.2 equal local entropy, different futures; §20.5.3 intervention; §20.5.4 reciprocal feedback; §20.5.5 boundary residual and signed offset; §20.5.6 Jordan term; §20.5.7 positive redistribution controls (metric loss 7/8; divided-difference loss 38/15; the four-gap control with a 1/48 metric increase).
  - §20.5.8 "what has been earned".
- **§21 Ten element peels, the xenon bridge and collective phases (lines 3942–4437):**
  - §21.1 ten diagnostic cases; table at lines 4157–4179; subsections §21.1.1–21.1.10; §21.1.11 contrasts.
  - §21.2 bounded xenon bridge: Zhong et al. 2020; the 4d-hole channel at 67.5 eV; the Swedish data deposit; an access gap (numeric files not retrieved).
  - §21.3 collective matter phases as a sourced extension (polariton supersolid, graphene bilayer, liquid-crystal space-time crystal, photonic time-quasicrystal preprint).
- **§22 What the paper establishes; §22.1 open questions (lines 4439–4475).** Line 4440: "The strongest element result is an anchored vector record."
- **Appendix A (proofs, lines 4480–4609):** A.1 Thm 3.1; A.2 Thm 4.1; A.3 positive peel; A.4 Schur and memory; A.5 transfer silence; A.6 phase reference; A.8 Thm 6.1; A.9 Thm 8.1; A.10 torus control; A.11 Thm 6.2; A.12 Prop 11.1 (wall parity); A.13 surviving matches; A.14 four-reading certificate; A.15 Thm 6.3 (thin film, top and substrate face); A.16 moving-channel order.
- **Appendix B (lines 4610–4675):** Lean status: 140 theorems in fifteen modules in dicipler-pixel/votkp-lean, commit bd4d15a. Prop 19.4 takes its excess-work density bound as a hypothesis (line 4657). The exact value at a simple root of Prop 11.1 "uses Rellich's analytic eigenvalue branches" and is not formalized (line 4657).
- **Appendix C (lines 4676–4697):** ideas held for later, including "Kelvin's vortex atoms", "The row as one impedance step" and "The dual layered Smith volume."
- **Appendix D (lines 4701–5144): test ledger.** Kill conditions registered by date (lines 4711–4717); registration file hashes (lines 4722–4761); Table 10 of tests (lines 4767–5143). Lines 4708–4709 say the rank-two and distinct-gap examples are synthetic counterexamples.
- **Appendix E (lines 5153–5415): literature.** E.1 gives the sources for §§20–21 ([S1]–[S17]). Lines 5396–5399 list the author's related work, which §§19–20 restate.
- **Appendix F (lines 5418–5514): scripts.** Section 19 script is v22/check_reverse_peel.py.
- **Appendix G (lines 5522–6043): all ten diagnostic ladders in full.** Values were checked against the §21.1 text and against the Γ formula (§3 below).
- **Archive checks (lines 6048–6053):** 5,847 thresholds, 110 elements, 103 complete ladders, 5,370 state-energy edges, 5,714 peel inversions. Line 6053: the electronic binding "contributes ... to a consistently defined mass defect; nuclear binding requires its own ledger."

## 3. Element-specific results (every element with a number in lines 3001–6053)

Γ here is the peel value printed in Appendix G, Γ = (z−1)/(z+1) with z = E(q+1)/E(q). I checked this against the printed thresholds (Li: z = 75.640097/5.391715 = 14.0289, Γ = 0.8669235, matches). The "3→2" column is my reconstruction: the step from the 3-electron ion to the 2-electron ion, i.e. the 2s→1s (K-shell) opening. The text names only Li–O for this comparison (§21.1.11, lines 4330–4334). The Cr–Au values are my extension and are labelled derived.

| Element (Z) | Neutral config (§21.1 table) | First threshold E0 (eV), grade | First Γ, pair grade | 3→2 Γ (derived) | Γ² vs ½ (derived) | Binding total (keV) | Section |
|---|---|---|---|---|---|---|---|
| Li (3) | [He] 2s¹ | 5.391715, E | 0.8669235, ET | 0.866923 (q=0; 5.39→75.64 eV) | 0.7516, past wall | 0.203486 | §21.1.1; App G |
| Be (4) | [He] 2s² | 9.322699, E | 0.3228191, EE | 0.788375 (q=1; 18.21→153.896 eV) | 0.6215, past | 0.399149 | §21.1.2; App G |
| B (5) | [He] 2s² 2p¹ | 8.298019, E | 0.5038976, EE | 0.744837 (q=2; 37.93→259.374 eV) | 0.5548, past | 0.670984 | §21.1.3; App G |
| C (6) | [He] 2s² 2p² | 11.260288, E | 0.3681704, EE | 0.717496 (q=3; 64.49→392.091 eV) | 0.5148, past (margin 0.0148) | 1.030108 | §21.1.4; App G |
| N (7) | [He] 2s² 2p³ | 14.53413, E | 0.3413842, ES | 0.698780 (q=4; 97.89→552.067 eV) | 0.4883, below | 1.486058 | §21.1.5; App G |
| O (8) | [He] 2s² 2p⁴ | 13.618055, E | 0.4411865, EE | 0.685180 (q=5; 138.12→739.327 eV) | 0.4695, below | 2.043843 | §21.1.6; App G |
| Cr (24) | [Ar] 3d⁵ 4s¹ | 6.76651, E | 0.4180051, EE | 0.625954 (q=21; 1721.18→7481.86 eV) | 0.3918, below | 28.582028 | §21.1.7; App G |
| Cu (29) | [Ar] 3d¹⁰ 4s¹ | 7.72638, E | 0.4484854, EE | 0.620942 (q=26; 2586.95→11062.43 eV) | 0.3856, below | 45.002586 | §21.1.8; App G |
| Xe (54) | [Kr] 4d¹⁰ 5s² 5p⁶ | 12.1298437, E | 0.2671862, ES | 0.608228 (q=51; 9810.37→40271.73 eV) | 0.3699, below | 202.399388 | §21.1.9; App G |
| Au (79) | [Xe] 4f¹⁴ 5d¹⁰ 6s¹ | 9.225554, E | 0.3730202, EE | 0.600152 (q=76; 22868.1→91515.8 eV) | 0.3602, below | 517.177249 | §21.1.10; App G |

Other element results in range:

- **Li:** the derived first peel is E/T, not experimental-only (§21.1.1, lines 4193–4195). The next decisive test is named as an independently traced experimental Li+ ionization limit (lines 4199–4201).
- **Be:** the second step, 153.896205 eV, gives Γ = 0.7883745 and is graded T (lines 4204–4205). Line 4338 gives the neutral signed step Be→B = −0.0581520 (see below).
- **B:** 8.298019 eV is 1.02468 eV below Be's 9.322699 (line 4218). B's first peel 0.5038976 exceeds Be's 0.3228191.
- **C:** four unflagged thresholds, 11.260288, 24.383143, 47.88778 and 64.49352 eV, precede a theoretical He-like endpoint (lines 4229–4230; App G). The research trace cites a 2018 neutral-C revision and a 2022 C II evaluation (lines 4232–4234).
- **N:** neutral threshold 14.53413 eV (E); second threshold 29.60125 eV (S); first peel 0.3413842 (E/S) (line 4241).
- **O:** 13.618055 eV is 0.916075 eV below N (line 4255). The neutral term changes from nitrogen's ⁴S to oxygen's ³P (line 4257). Line 4338 gives the neutral signed step N→O = −0.0325401.
- **Cr:** 6.76651, 16.486305 and 30.959 eV (E; the last "substantially less precise"). Sansonetti and Nave (2014) cited for Cr II (lines 4270–4271). The Cr binding sum 28.582028 keV agrees with my re-sum of Appendix G. A local spike sits at row 13 (n = 11): Γ = 0.449530 (384.163→1011.6 eV), derived and not discussed in the text.
- **Cu:** 7.72638, 20.29239 and 36.841 eV (all E). Cu's first threshold is below Au's, but its first peel is larger (line 4285). The Ag control gives the absolute ordering Au > Cu > Ag and the peel ordering Ag > Cu > Au (lines 4355–4356); the Ag numerical values are missing in export. Cu row 18 (n = 11): Γ = 0.431955, derived.
- **Xe:** 12.1298437 eV (E) and 20.975 eV (S); first peel 0.2671862 (E/S). The 4d-hole threshold used for the matched channel is 67.5 eV (line 4374), with about 2 eV spin-orbit separation (line 4375). The 2020 measured channel delays differ by over 100 attoseconds near threshold (lines 4296–4297). The 2024 pump-probe lifetime is 49 ± 3 fs (lines 4301–4302). Xe row 43 (n = 11): Γ = 0.393513 (3333.8 eV, S), derived.
- **Au:** 9.225554 eV (E), 20.203 eV (E), 30.0 ± 1.6 eV (T); first Γ 0.3730202. The disputed Au²⁺ rung gives Γ(q1→q2) = 0.1951477 at 30 eV, 0.2545431 at 34 eV and 0.2886643 at 36.6 eV (lines 4321–4322). I reproduce all three. Au row 68 (n = 11): Γ = 0.366667, derived.
- **Ne:** the Xe/Ne RABBIT reference uses Ne for the atomic delay (lines 4369–4370). No Ne number is printed in the range.
- **He / helium-like stages:** "helium-like endpoint" for C (line 4230); the Unsöld 5/8 and Hylleraas expansions are cited (lines 5307–5308); the negative electron affinity of helium is noted (line 5358); "helium-like and hydrogen-like stages are theoretical in the archive" (item 43, line 3029).
- **H⁻, D⁻, Ps⁻ (P-02, App D):** constituent axis 2.892, 2.892 and 3.036 (line 4874). Reproduction.
- **Pt, Au, Hg (RHYTHM T04, App D):** ratio 2.28 against a kill condition of ratio > 2; killed (line 4956).
- **Fr and Ra (RHYTHM T05, App D):** misses 0.55 and 0.99 eV against a 0.3 eV limit; gaps 1.55 and 2.14 eV at Z = 119 and 120 (lines 4959–4960). Killed. R7 forecast: Ra −27% against a 36% tolerance; Fr not tabulated (lines 5027–5028).
- **Hf, Ta (depth law, App D):** holds for K ≤ 10; Hf and Ta at 11–12 are the misses (line 4787).
- **Tl–Rn (F-WALL-01, App D):** the 4f jump lies outside the p–d interval in 6 of 6 cases, and is negative in all 12 row-6 elements (lines 5106–5107). Killed as written; recorded as a control.
- **Mt, Ds (RHYTHM T16):** no data; counted as misses (line 4987).
- **Og, Lr, element 119 (App E):** reference items only. Element 119 with 4.7839(56) eV is cited (lines 5200–5201). The element-120 Borschevsky value is a blank in export (line 5332).
- **Mn, V:** named as predicted controls for Cr (line 4275). No numbers.
- **Carbon allotropes, metallic Cr magnetism, Au films:** named as needing their own specimen labels (lines 4360–4361). Gold metamer ΔE*ab 8.60 (line 4893). Gold labels in local datasets: a rise at 450 nm in 15 of 15, none at 650 nm (lines 4914–4915).
- **Binding totals, all ten:** Li 0.203486 keV; Be 0.399149; B 0.670984; C 1.030108; N 1.486058; O 2.043843; Cr 28.582028; Cu 45.002586; Xe 202.399388; Au 517.177249. All as printed in §21.1. The Cr and Cu sums agree with my re-sum of Appendix G.
- **Signed neutral steps (§21.1.11, line 4338):** Be→B −0.0581520 and N→O −0.0325401. I reconstructed both as Γ of the ratio of neutral thresholds (B/Be and O/N), and they match to all printed digits. The defining line itself is blank in export.

Derived observations from the table (my computation, not stated in the text):

- The 3→2 Γ sequence from Li to Au is strictly decreasing in Z across all ten ladders: 0.8669, 0.7884, 0.7448, 0.7175, 0.6988, 0.6852, 0.6260, 0.6209, 0.6082, 0.6002.
- Only Li, Be, B and C sit above the half-line Γ² = ½ (Γ = 1/√2 ≈ 0.707107). N is the first element below it.
- Within these ten ladders the four steps past the wall are the Li first step and the Be, B and C K-shell openings. Those four are the ones the frame places in this sample.
- The n = 11 peels (Cr row 13, Cu row 18, Xe row 43, Au row 68) are local spikes in each ladder. They are not the global maxima; the Cr and Cu maxima are at n = 3.

## 4. Bold moves (the mathematical move, its assumptions, and whether later versions dropped it)

1. **Net versus traversed length (Prop 19.2, lines 3095–3113).** Concatenating a directed edge with its inverse gives zero endpoint but length 1.6. Assumptions: the real diameter with Poincaré normalisation, geodesic edges. Route length is kept as a separate invariant from endpoint.
2. **Scalar record does not fix the projector (Prop 19.3, lines 3129–3159).** Constant and rotating projector families share the adjacent gaps and the same gap-ratio coordinate. Assumption: an adjacent-gap ladder stands in for a positive record. The text flags that actual thresholds come from different electron-number sectors, so the surrogate is marked as one.
3. **Saturation with several distinct gaps (§19.6, lines 3209–3216).** The bound saturates when every active gap has the minimum weight, and different gaps may share that weight. The text calls this "The correct saturation condition," which marks it as a repair of an earlier statement.
4. **Signed log-odds separate from entropy (§20.5.5, lines 4070–4096).** A Schur reduction of a fermionic correlation matrix. The particle–hole partner has the same entropy but a different signed offset, so entropy cannot carry the signed distinction. Assumption: a Gaussian correlation model.
5. **Equal present summaries, different futures (§20.5.2, lines 3986–4018).** Two qubit states with the same local entropy and mean energy differ only in a correlation phase, which a later local readout exposes. Line 4018: the atomic version "has not yet populated this atomic test."
6. **Intervention without marginal change (§20.5.3, lines 4022–4043).** A nonselective phase measurement takes the global entropy from zero to a positive value while the local marginals stay maximally mixed. Assumption: no apparatus or reservoir ledger.
7. **Moving-channel order (§20.3.5, Prop A.16, lines 3719–3740).** A cumulative positive-matrix upshift gives a positive metric loss. Equal oscillator budget and two polarizability readings do not certify it (the four-gap control gives a metric increase of 1/48).
8. **Wall-link onset as a ratio limit (§20.3.6, lines 3746–3761).** Increasing drive raises coupling and detuning together, so an activation threshold can approach a ratio-controlled limit. The text calls this a model-specific proposal, not an atomic claim.
9. **Ridge alignment by remaining electron count (§21.1.11, lines 4330–4334).** The strong comparisons across Li to O are aligned at the step that leaves three electrons. That alignment is what makes the 0.8669 to 0.6852 decline visible. The text says the indexing "is useful for organizing tests, not a newly discovered shell law."
10. **Thin-film reference change (A.15, lines 4583–4589).** Referring the admittance to the substrate face multiplies it by a factor. The whole-sheet correction then differs only in an imaginary term, so reflectance agrees to first order and phase does not.

## 5. Connections to today's frame (quoted)

- **Γ² = ½, z = 3+2√2, √2, 1/√2:** none of these appear in lines 3001–6053 (grep confirmed). The wall is not named in this range. The phrase "shell wall" appears only as a Lean module label in Appendix B (line 4615): "the shell wall and the ladders (§§8.1, 8.7, 15.2–15.4)." Its definition lies in the part the other reader covers.
- **Phase at a wall / phase survives:** line 4010: "The energy and present local entropy do not distinguish the preparations. Their correlation phases do." This is the closest structural match to "phase crosses what amplitude cannot." Line 3551: "A common wavefunction phase leaves the density matrix unchanged, so only relative phases ... can be observed."
- **Cancel:** line 4092: "cancellation of an interior factor does not erase its coupling from the residual." The closest match to CANCELLED (partner on the reversed word) is the cancellation-defect construction (line 3113), where the endpoint cancels but the length does not.
- **Lock / convert:** none found in range.
- **Two books per edge (E⁻/E⁺ = Γ²), Koide, neutrinos, spin as a frame label:** not found. "spin-orbit" appears only as a channel label (lines 4371, 4703, 4375).
- **Lorentz / rapidity:** line 3081: "A negative step reduces an initially positive signed rapidity." Line 3333: "Dimensionless rapidity is not physical time." Line 3108: "The real diameter is a geodesic with length ... on each edge."
- **Tree / ball:** none in range.
- **Edge Γ = tanh(½ ln z):** the same definition as the frame's. Γ = (z−1)/(z+1) is used throughout Appendix G; ratio 5 gives Γ = 2/3 by the same formula.

## 6. Anything that contradicts today's frame

- **Phase at a wall:** the frame says "at a wall the amplitude dies and the phase survives." Lines 4586–4589 (A.15) say that for a thin film "the reflectance agrees to first order and the phase does not." This is a different object (a sheet over a substrate), so I do not call it a contradiction. It is a tension the main session should look at before writing a wall-phase sentence.
- **Scalar records do not fix geometry:** the frame's wall is a scalar condition on Γ. Lines 3129–3131 and 3154 say a scalar record fixes no projector path. So the wall condition cannot by itself say anything about a projector or a phase. This is not a contradiction of the wall, but it limits what the wall can carry.
- **Count:** the frame uses 5,737 ionisation steps. This version gives 5,714 peel inversions and adjoining pairs (lines 3116, 6050–6051). 5,847 − 110 = 5,737 is arithmetic that this range does not state. Reconcile before quoting either number.
- **Provenance:** line 5516 says the version was "Written by Claude from Jeromie Beasley's research programme and his collaborators' reviews." Under the standing rule, a version Claude wrote is labelled as Claude's version and not called his. The main session should check that label on v2.9 before any public use.

## 7. Notes for the main session

- Memory facts used: only the Zenodo status of v2.9 in §1, which I did not check against this text. Nothing else from memory bears on the reading.
- The 3→2 sequence in the §3 table gives an element-indexed version of the frame's wall that this version does not state. It is taken straight from Appendix G, so anyone with the table can check it.
- Items in Appendix D that the version itself records as killed or as reproduction-only are reported as the version records them. I did not build any ledger from them.
