# The Offset Speed Limit ("rate is weight") and The Loop Wall: connection map

Jeromie Beasley · mapping prepared 21 November 2026 · local working file, not delivered to GitHub or Drive

## 0. What was mapped

- **The "rate is weight" paper** is *The Offset Speed Limit. Rate is weight: a record moves only as fast as the weight between allows*, Version 1 (v1.1 files), 26 October 2026. Drive file `The_Offset_Speed_Limit_v1_1_2026-10-26.pdf`, id `1uq6DnlOhFSse4tpxMGJ-mXdD93w_RSmf`. A Drive search on the titles "Offset Speed Limit", "speed limit" and "Rate Is Weight" found no later version. GitHub code search returned nothing for either title. This session can only reach the votkp-lean repository on GitHub; offset-lean and dirac-time-lean were refused.
- **No separate paper titled "Rate Is Weight" exists.** That title belongs to three other things:
  - a working note, "Rate Is Weight: proposed Amendment B to The Dirac Time of the Gigantefermion" (24 October 2026), which I read;
  - a song from the paper (the mp3 and the 27 October "cosmic rap" page);
  - a video.
- **The companion paper** is *The Weight Between*, Version 1 (v1.1), 26 October 2026. It defines the coupling energy E_B = ‖PH(1−P)‖²_F.
- **The element paper** is *The Loop Wall: Peeling the Elements from Hydrogen to Astatine*, page v8, from votkp-lean branch `element-paper/loop-wall` at commit e3fae77. I read the folder `research/2026-11-20-element-paper-loop-wall/`.

### Notation used below

The two papers use these symbols. Every formula in this report uses them.

From the speed-limit paper:
- C is the accessible block of a projector P.
- ν is one eigenvalue of C.
- The signed offset is τ = Tr[log(I−C) − log C], so one eigenvalue contributes τ_ν = log((1−ν)/ν).
- S = Tr[(C(I−C))⁻¹] measures how sharp the cut is.
- g = ½‖Ṗ‖²_F is the speed of the projector. For Hamiltonian motion g = E_B (Proposition 5).
- Theorem 1 is the speed limit τ̇² ≤ 4gS. Corollary 3 is |τ̇| ≤ 2√(E_B S).

From the element paper:
- z = b/a is the peel ratio of an ordered pair of thresholds (a first, then b).
- Γ = (z−1)/(z+1) = tanh h, with h = ½ ln z.
- The wall is Γ² = ½, that is z = 3 + 2√2.

## 1. Prior art inside the corpus (read before calling anything new)

Several of these connections are already recorded in Jeromie's own work. The table says where. I read the atlas through the 12 November atlas map on the votkp-lean branch: `paper/votkp_v3_2/code/atlas_map/` (ATLAS_REPORT_1, ATLAS_REPORT_2_all_cards and the CARD_INDEX of all 222 cards). I did **not** read every atlas card in full myself.

| Already in the corpus | Where |
|---|---|
| "The offset is a rapidity: τ = 2 artanh a", with the link "same form as B98: the atom and the film share an addition law" | atlas card B153 |
| "A threshold ratio is a Smith coordinate: Γ = (I′ − I)/(I′ + I) = tanh(τ/2)" | atlas card B97 |
| "The offset is the log-odds of empty against full" | atlas card B151 |
| On one scalar edge the two books are (d_i − d_j)² and (d_i + d_j)², and their ratio is Γ² | atlas card B189 |
| The speed limit τ̇² ≤ 4gS, with a trajectory that meets it at every instant | atlas card B211 |
| "The elementary Cayley dictionary for z = 3 gives Γ = 0.5 and a formal occupation-like number 1/(1+z) = 0.25. This algebra alone neither measures an atomic occupation nor embeds an ionization ladder into this correlation model." | Elemental Peeling paper v3.3 (12 November) |
| The Γ form of B211, (dΓ/dt)² ≤ 4g(1 − Γ²), written as a reader's substitution and not on any card; also the wall as trace −2 of the commutator of two perpendicular boosts | 12 November atlas read, ATLAS_REPORT_2, verdict 4 and its own check |
| The speed-limit scripts (weight_between_core_checks.py, c4_richardson.py) carried into the element line | Elemental Peeling v3.3 source list |

So the shared map between the offset and the peel step is **already in the atlas as a same-form link**, and the occupation reading is **already flagged as formal**.

What this report adds:
- the checks themselves;
- the wall written in the speed-limit paper's variables;
- the wall as the saturation point of the derived rate bound on Γ²;
- the angle form of the loop-closing test;
- the junction sum rule and the localization second moment identified as the paper's census and coupling energy;
- an explicit projector that realises the peel step as an offset.

## 2. Every connection, graded

The grades are:
- **EXACT**: the same formula, by algebra.
- **STRUCTURAL**: the same shape on different objects (flagged).
- **LEAD**: untested, or tested only in part.

### EXACT

**E1. One balance map.**
- The speed-limit paper (eq. (10), Appendix B) has (m−p)/(m+p) = tanh(½ log(m/p)). It names this "the Smith-chart reflection (z−1)/(z+1)" and "the asymmetry 1 − 2ν of an occupation ν against its log-odds".
- The element paper's Γ is the same function, with the same Lean `smith_identity` (votkp-lean `VOTKP/Smith.lean`).
- Put ν = a/(a+b), the lower threshold's share of the pair. Then:
  - τ_ν = log((1−ν)/ν) = ln z = 2h, so the peel rapidity is the per-mode offset;
  - 1 − 2ν = Γ.
- The formula is EXACT. Calling ν an occupation is only STRUCTURAL (see L1).
- Check 01: six symbolic residuals, all 0.

**E2. The census is the returned power, and the complement is reversal.**
- ν(1−ν) = (1 − Γ²)/4. So the speed-limit paper's census C − C² is an even function of Γ, exactly like the element paper's returned power Γ².
- Speed-limit paper: "the census C − C² alone loses the sign". Element paper: "a ledger of Γ² alone cannot tell the two orders apart" (`power_even`). These are one fact.
- The complement ν → 1 − ν is z → 1/z, which gives Γ → −Γ. In the speed-limit paper "taking the complement flips the sign"; in the element paper this is `gam_reverse`.
- Check 01.

**E3. The wall in the speed-limit paper's variables.** At Γ² = ½, all of these hold at once:
- the per-mode census is ν(1−ν) = 1/8, exactly half of the half-filling maximum 1/4;
- the per-mode sharpness is S = 4 cosh² h = 8;
- the offset is τ = ln(3 + 2√2) = 2 asinh 1 = 1.762747;
- ν = (1 − 1/√2)/2 = 0.146447;
- four times the census equals the squared asymmetry: 4ν(1−ν) = (1 − 2ν)².

On the archive (check 01):
- Every one of the 3,570 ordinary steps from hydrogen to astatine gets the same call from S > 8 (or census < 1/8) as from z > 3 + 2√2. There are 0 disagreements.
- The eight outside steps are reproduced: lithium, beryllium, boron, carbon, sodium, potassium, rubidium and caesium.
- At the anion rung, S₀ = (IE + EA)²/(IE·EA) = 4χ²/(χ² − η²) = 4/(1 − Γ₀²). So S₀ = 8 is exactly electrophilicity = hardness.
- All 44 bound anions from hydrogen to caesium agree. Silver has S₀ = 7.9801 (inside) and silicon 8.0370 (outside).

**E4. The angle form of the one-mode speed limit, and the loop-closing test.** Put θ = arcsin Γ.
- Then θ = gd(h), the Gudermannian, since sin gd h = tanh h. Also sinh h = tan θ.
- For one accessible mode, (dθ/dt)² = τ̇²/S exactly. So Theorem 1 (with Theorem 2, its one-mode case) is exactly |dθ/dt| ≤ 2√g. With Proposition 5 this is |dθ/dt| ≤ 2√(E_B).
- The element paper's loop-closing test sinh h_a sinh h_b < 1 is tan θ_a tan θ_b < 1, which is θ_a + θ_b < π/2. The equal-face wall is θ = π/4.

What the checks found (check 02):
- 3,301 random idempotent one-mode paths: the largest (dθ/dt)²/(4g) is 0.999999995 and the smallest is 0.0000. The bound holds and is not trivially met.
- The angle form of the five first-opening mixed pairs gives the same calls as the Γ₁² + Γ₂² test:

| Pair | Γ₁² + Γ₂² − 1 | θ₁ + θ₂ − 90° | Result |
|---|---|---|---|
| carbon with nitrogen | +0.003093 | +0.18° | open |
| sodium with magnesium | +0.114273 | +6.67° | open |
| potassium with calcium | −0.037822 | −2.21° | closes |
| rubidium with strontium | −0.111437 | −6.52° | closes |
| caesium with barium | −0.175248 | −10.29° | closes |

Prior art: the 12 November read wrote the Γ form, (dΓ/dt)² ≤ 4g(1 − Γ²), as a substitution. The θ form and the angle-budget reading of the loop test are not in the texts I read. The angle-budget reading is a short and standard step (sinh h = tan gd h), so I would not claim it as a result.

**E5. The wall is where the speed limit lets the returned power move fastest.** This answers the brief's question directly.
- d(Γ²)/dt = sin 2θ · dθ/dt. So |d(Γ²)/dt| ≤ 2√g sin 2θ ≤ 2√g.
- The outer bound can be reached only at θ = π/4, that is at Γ² = ½. The census 4ν(1−ν) = 1 − Γ² behaves the same way.
- On the paper's saturating trajectory (eq. (4), m = 1): 1 − 2C = sin 2Ωt, so θ = 2Ωt exactly.
- On that trajectory the wall is crossed at t = π/(8Ω). That is the instant when Γ² changes fastest.

Check 02, with Ω = 1.3:
- |θ − 2Ωt| ≤ 1.6 × 10⁻¹³;
- E_B = 1.690000 = Ω²;
- the peak of |d(Γ²)/dt| is 2.600000 = 2√(E_B), at Γ² = 0.50000 and t = 0.302076 = π/(8Ω).

So **Γ² = ½ is a saturation point of a bound derived from the paper**: the bound on how fast the even half of the ledger can move. It is not the equality case of Theorem 1 itself. Theorem 1 is met all along trajectory (4), and its equality condition (ḃ a real multiple of b) does not single out the wall.

**E6. The junction sum rule is the census identity.**
- Element paper, section 7: Σ_{j≠i} ‖P_ij‖² = Tr(C_i − C_i²).
- Speed-limit paper: C − C² = P₁₂P₁₂† (light-ledger-lean `Census.lean`, `projector_block_coupling`). Take the accessible block to be the orbitals of site i and take the trace: the two are the same identity.
- Check 03: worst relative residual 6.4 × 10⁻¹⁴ over 300 random projectors in random site partitions.
- Control: a non-projector breaks the identity by at least 1.3 × 10⁻². My first run's control was too weak (perturbation 0.05, smallest break 5 × 10⁻⁴, so the kill condition fired). The rerun uses 0.3. Both outputs are kept.
- The half-filled ring gives census 1/4 and a nearest share of 0.8106 = 8/π², as in the page.

**E7. The localization second moment is the coupling energy of position.**
- Element paper: Var(X) = Tr(PX(1−P)X) = ½ Σ_ij ‖P_ij‖² (x_i − x_j)².
- This is E_B = ‖PX(1−P)‖²_F of The Weight Between with the position operator X in place of H.
- By Proposition 5 it equals g = ½‖[X, P]‖²_F, which is the speed at which the twist P(s) = e^{−isX} P e^{isX} moves the occupied projector.
- Check 03: worst relative residual 2.2 × 10⁻¹⁴.

What follows from Theorem 1:
- Under the twist, the offset of **any** accessible block E obeys |dτ_E/ds| ≤ 2√(Var(X) · S_E). In random cases the largest ratio was 0.573.
- A block made of whole sites is frozen, because the twist acts on it as a phase. Its offset changed by at most 2.4 × 10⁻¹⁴ under a finite twist.

The algebra is EXACT. Its physical use (the element paper's open "boundary twist" transport reading) is LEAD L3.

**E8. The film (⊕) law.**
- The Weight Between, eq. (13): film reflections compose by u ⊕ v = (u + v)/(1 + uv), so tanh a ⊕ tanh b = tanh(a + b). This is votkp-lean `VOTKP/Film.lean` (`film_is_oplus`, `stack_telescopes`). The element paper cites the same `smith_identity`.
- Successive peel steps compose the same way. The two-step reflection Γ(IE_{k+2}/IE_k) equals Γ_k ⊕ Γ_{k+1}.
- Check 04: worst residual 2.2 × 10⁻¹⁶ on 3,486 archive pairs.

**E9. Peel ratios are blind to H → sH + cI.**
- The speed-limit paper says projector geometry is blind to the affine change sH + cI, and that a constant is read only as a difference.
- Each removal energy is a difference of charge-state energies, so a common shift c cancels in it. The ratio z then cancels a common scale s.
- Check 04: applying E → sE + c to every ladder from hydrogen to astatine changes no z or Γ by more than 1.6 × 10⁻¹⁴.
- The invariance is EXACT. Reading the peel ratio as a two-clock ratio is S2.

**E10. The scalar-edge books.**
- On one scalar edge carrying the two thresholds, The Weight Between's own matrix definitions give E⁻ = (d_i − d_j)² and E⁺ = (d_i + d_j)². Here E⁻ = (1/8)‖[H, H†]‖² is the connection book and E⁺ = (1/8)‖H² − H†²‖² the opposite book. This is card B189.
- So E⁻/E⁺ = Γ², and (E⁺ − E⁻)/E⁺ = 4ν(1−ν), the census of E2.
- The wall is E⁺ = 2E⁻: the reflected share equals the transmitted share.
- Check 07: residuals 6.8 × 10⁻¹⁶ on random edges and 2.8 × 10⁻¹⁶ on all 3,570 archive steps. A non-unitary edge block breaks the identity, as it must.
- The ordinary steps closest to half reflected are: caesium step 1 (0.50710 reflected), nitrogen step 5 (0.48829) and carbon step 4 (0.51480).

### STRUCTURAL (same shape, different objects; flagged)

**S1. Englert's two books.**
- With D := Γ = tanh h and V := sech h, V² + D² = 1, and the wall is V = D (check 04).
- The phase readout ⟨Z_P⟩(θ) = sin 2θ sin Φ of `EqualEndpointWitness` (The Weight Between, section 3) is largest at θ = π/4.
- **Name clash:** these are not the books of E10. With those books, "equal books" means Γ² = 1, as card B189 says, and B199 warns that "equal books on a graph are not the wall". Calling Γ a which-way distinguishability is a substitution of objects.

**S2. The two-clock ratio.**
- In the speed-limit paper the thorium-to-strontium clock ratio cancels the universal (common-scale) part. A peel ratio is likewise a ratio of two removal frequencies of one atom, and cancels any common scale.
- The element work's own review ledger (CLAUDE_REVIEW.md, Codex at 11:18) records the counterpart: a common positive rescaling of both energy ladders keeps every Γ, but can erase the holmium-163 and dysprosium-163 charge-bracket sign reversal with the neutral Q fixed. So absolute energy scales matter.
- That is the speed-limit paper's split exactly: the ratio forgets the scale, and the difference (a mass, a weight) keeps it.

**S3. The same open calibration step.**
- Speed-limit paper: "Turning the offset, a pure number, into a weight needs a clock to supply the units; that step is open."
- Element paper, section 9: "Each peel ratio is a dimensionless clock. Turning one into a distance in ångströms needs a calibration fixed before the comparison."
- Both name the same missing step for the same kind of object. Rate Is Weight Amendment B names the Bisognano–Wichmann test as the decisive calibration.

**S4. The sign as direction.**
- Speed-limit paper: the offset's sign flips under the complement and under H → −H. It is "a record of which side of the cut is filled, not of the clock's direction", and true (antiunitary) time reversal leaves it unchanged.
- Element paper: the sign of Γ is odd under reversing the peel order, and the screw sign χ is odd under a mirror and even under time reversal.
- These are compatible. Reversing the peel order is the complement swap, not a time reversal. The element page's wording "the sign carries the direction" should be read as the order of the pair.

**S5. A protected zero and a matched junction.**
- Speed-limit paper: a spectral pairing forces τ = 0 (offset-lean `protected_zero_of_pairing`).
- Element paper: equal clocks at a junction give Γ = 0 (`matched_junction`).
- Both are the balance point ν = ½ of the same map. The causes differ (a symmetry in one, equal neighbours in the other).

**S6. The Gibbs reading.**
- Speed-limit paper, eq. (7): the two-level population gap is tanh(βΔ/2), the same map.
- Reading z as a Boltzmann ratio puts the wall at βΔ = 2 asinh 1 = 1.762747, with populations 0.853553 and 0.146447 (check 04). This is numbers only.

**S7. Memory under elimination.**
- The Weight Between: "same present, different future" (votkp-lean `Peel.lean` `shared_records`, `later_outcomes`, `schur_memory`) and the memory kernel B e^{Dτ} C.
- Element paper: the spinor-peel recovery. Deleting a mode loses its phase; eliminating it properly keeps it. Re W is even (like Γ²) and Im W is odd (like the sign of Γ).
- Same shape, different objects.

### LEADS (untested, or tested only in part)

**L1. The log-odds offset and the peel log-ratio as one object.**
- E1 makes the formulas identical for any positive pair. The algebra alone does not make ν an occupation of anything; v3.3 already said so.
- One explicit projector does carry the peel step as an offset. It is my own construction and is in neither paper:
  - Take v = (√a, √b) and H = vvᵀ, a two-site dimer with site energies a and b and hopping √(ab), their geometric mean.
  - Its zero-mode projector has site occupations b/(a+b) and a/(a+b).
  - The site-2 offset is exactly ln(b/a) = 2h, and the site imbalance is Γ.
  - The census identity holds, and the wall is |Δ| = 2t (on-site imbalance Δ = b − a equal to twice the hopping t).
  - Check 06: every residual is 0.
- Separately, I noted from memory (not reopened) that Δ/√(Δ² + 4t²) resembles the Coulson–Phillips ionicity of a two-centre bond. Phillips's critical ionicity is about 0.785, not ½, so this does not place the wall.
- **Decisive test:** take a projector that is fixed physically before the comparison, not built to fit. Candidates are the element paper's own hydrogen-cell projector (checks/hsb) or a minimal-basis atomic or ionic calculation of the outgoing-electron block. Compute its census ν at each peel and ask whether ln((1−ν)/ν) reproduces ln z across the archive.
  - Kill condition, written before any run: the wall calls differ beyond the near-wall cases (silver, silicon, caesium step 1, carbon step 4, nitrogen step 5), or the rank correlation of ln((1−ν)/ν) with ln z falls below 0.9.
  - This was not run here.

**L2. The speed limit along a parameter of the element side.** The speed limit needs a projector family moving in some parameter. The element side has no time. Candidates are Z along an opening sequence, pressure (compressed xenon) and the twist (L3).
- Check 05 tried the weakest version: does the angle along an opening sequence advance uniformly, as on the saturating trajectory? If so, the largest change of Γ² would sit on the wall-crossing step.
- The kill condition did not fire (4 of 5 sequences peak at the wall step), but the test is **confounded**. For the neon, argon, krypton and xenon cores the wall-crossing step is also the first step. In the helium sequence, the only one where the two differ, the peak is at lithium to beryllium, not at carbon to nitrogen.
- In every sequence the angle steps shrink fast (helium: 8.07°, 3.89°, 2.30°, 1.52°, ...). So the uniform-rate reading is **not supported**. The speed limit itself, an upper bound, is untested on the element side.
- **Decisive test:** fix a projector family P(Z) (for example the L1 dimer, or a screened-orbital projector from the 11 November screening note) and compare |Δθ|/ΔZ with 2√(g_Z) along each sequence. This only means something if the family is chosen before the comparison.

**L3. The twist transport reading.**
- By E7, under a boundary twist the occupied projector moves with speed Var(X), the localization second moment.
- Theorem 1 then bounds the offset response of any non-site cut by 2√(Var(X) · S_E).
- The rubidium second moment grows with the mesh (5.684 to 12.622 Å²) while krypton's stays at about 0.067 Å². So this bound grows for the metal and saturates for the insulator. That fits the element paper's open item "a transport response (a boundary twist with size scaling)".
- **Decisive test:** from the rubidium and krypton wavefunction data (the supplied weight files hold ‖P_ij‖² only, which is not enough), compute the offset of a band-energy block under a finite twist, and compare its speed with 2√(Var(X) S) at each mesh.
- Untested.

**L4. The gap-power ladder on the element side.**
- In The Weight Between, rung 0 is the coupling energy (here Var(X), by E7) and rung −1 is light's static response. The ladder is log-convex: S₋₁² ≤ S₋₂S₀.
- The element page cites the Souza–Wilkens–Martin sum rule: the localization tensor is the first negative moment of the optical conductivity. Together they may give an inequality joining measured optical data, the projector metric and Var(X) for rubidium and krypton.
- Untested. The rungs must be put in the same variables first.

**L5. The Petermann-type factor from the 12 November work.**
- That read lists K = 1/(1 − 2Γ²) as a result on no card. In the angle of E4, K = sec 2θ: it diverges at θ = π/4, the same point where d(Γ²)/dθ = sin 2θ peaks (E5).
- I did not read the source of that result, so this tie is untested.

### Searched for and not found

- The term "level rapidity" and the symbol ε = ln((1−ν)/ν) do not appear in The Offset Speed Limit v1.1, The Weight Between v1.1, or the element folder. The quantity is the speed-limit paper's τ_ν. The Weight Between uses "rapidity" once, for films.
- Neither speed-limit paper is cited in the element page v8, its README, the quantum-chemistry notes or the review ledger.
- The friction section (ζ = c tanh(βΔ/2) α₀, Corollary 4) has no element-side counterpart in the texts read.
- The Rice–Mele offset 0.881157 gives Γ = 0.414124, close to √2 − 1 = 0.414214 but different by 9 × 10⁻⁵. It is set by the chosen hopping values and is not a connection.

## 3. The strongest connections

1. **E3 with E5: the wall in the speed-limit paper's own variables, as a saturation point.**
   - Γ² = ½ is census 1/8 (half the half-filling maximum), sharpness S = 8 per mode, and offset 2 asinh 1.
   - It is exactly where the bound derived from the speed limit lets the returned power Γ² (and the census) move fastest. On the paper's saturating trajectory it is crossed at t = π/(8Ω), at the peak rate 2√(E_B).
   - At the anion rung the same S = 8 is electrophilicity = hardness, with all 44 anions agreeing.
   - Grade: EXACT as algebra. That the element steps are modes of such a projector is L1.
2. **E7 with E6: the localization second moment is the coupling energy of position, and the junction sum rule is the census identity.**
   - These are the element paper's two projector readings and the two central objects of The Weight Between and The Offset Speed Limit.
   - Through Theorem 1 they bound the twist response of any cut (L3).
   - Grade: EXACT.
3. **E1, E2 and E4: one balance map, the census as the even half, and the loop test as an angle budget.**
   - The peel rapidity is the per-mode offset, the census is the returned power, and the complement is reversal.
   - The loop closes iff θ_a + θ_b < π/2, and the one-mode speed limit is |dθ/dt| ≤ 2√(E_B).
   - Grade: EXACT. The same-form link itself was already in the atlas (B153, B97, B189) and the occupation reading is already flagged as formal in v3.3.

Decisive test for the main lead (L1): a projector fixed in advance whose outgoing-electron census reproduces ln z with the same wall calls; kill condition as stated under L1.

## 4. Scripts and outputs

Each script is in `/home/claude/connections/checks_rate/`, starts with `# SCRIPT: NAME`, and states why it proves its claim and its kill conditions before the code. Outputs sit beside each script.

| Script | What it checks | Result |
|---|---|---|
| `check_rate_01_logodds_peel.py` (RATE-WEIGHT-LOGODDS-PEEL-01) | E1, E2, E3; archive and 44 anions | all residuals 0; 0 disagreements; 8 outside steps |
| `check_rate_02_angle_speed.py` (RATE-WEIGHT-ANGLE-SPEED-02) | E4, E5, five mixed pairs | no kill fired |
| `check_rate_03_census_localization_EB.py` (RATE-WEIGHT-CENSUS-LOCALIZATION-03) | E6, E7, twist bound | no kill fired on the rerun; first run's weak control kept in `check_rate_03_output_run1_weak_control.txt` |
| `check_rate_04_books_clocks_films.py` (RATE-WEIGHT-BOOKS-CLOCKS-FILMS-04) | S1, E9, E8, S6, Rice–Mele | no kill fired |
| `check_rate_05_sequence_rate_lead.py` (RATE-WEIGHT-SEQUENCE-RATE-05) | L2, first test | kill not fired, but confounded (see L2) |
| `check_rate_06_dimer_realization.py` (RATE-WEIGHT-DIMER-06) | L1 construction | all residuals 0 |
| `check_rate_07_scalar_edge_books.py` (RATE-WEIGHT-EDGE-BOOKS-07) | E10 | no kill fired |

Run each archive script as `python3 -I <script> /home/claude/votkp-lean/data/element_thresholds_20261011.json.gz`.

## 5. Sources read

| Source | Version and location | Read |
|---|---|---|
| The Offset Speed Limit | v1.1, 26 Oct 2026, Drive id 1uq6DnlOhFSse4tpxMGJ-mXdD93w_RSmf (7 pp) | in full |
| The Offset Speed Limit, journal edition | v1.1, Drive id 1BUtaeSfGhObp_c9ZHkj5SncdQYzozT73 | compared in part (same text without grade tags, by search) |
| The Offset Speed Limit code and figures | v1.1 zip, Drive id 17KesT5CwAYBRf3DiPYKn5P0UjZzxFf58 | file list only; outputs read as printed in the paper; scripts not rerun |
| The Weight Between | v1.1, 26 Oct 2026, Drive id 1X5mXIfmVNfHl2amxbp88R70oGEtgK8u4 (8 pp) | in full |
| Rate Is Weight, proposed Amendment B to Dirac Time | Google Doc, 24 Oct 2026, id 1WA6h67x1bpE3vWkABYR-QAPJ8aavfdnK8synxAmajl8 | in full (summary doc; the linked artifact page not opened) |
| The Loop Wall page | v8, votkp-lean `element-paper/loop-wall` at e3fae77 | in full (text extracted) |
| README.md, QUANTUM_CHEMISTRY_LINKS.md, CLAUDE_REVIEW.md | same folder | in full |
| lean/LoopWall.lean | same folder | theorem list skimmed (first about 220 lines) |
| Elemental Peeling paper v3.3 | same branch | searched for the speed-limit and offset passages only |
| Atlas map of 12 Nov (ATLAS_REPORT_1, ATLAS_REPORT_2_all_cards, CARD_INDEX) | `paper/votkp_v3_2/code/atlas_map/` | report 2 in full; report 1 in part (cards B97, B153, B189, B204 in full); index in full. The full card set was not read |
| Element archive | `data/element_thresholds_20261011.json.gz` | used by every check |

Not read: The Weight Between and the Exit Line v4 (5 Nov, a later paper in the Weight Between line); The Weight Between draft v2.3 (24 Oct, a different paper on memory, light, time, colour and music); the 1 November note joining The Weight Between and The Offset Speed Limit to the ledger papers; The Offset Belongs to the Boundary v31 (cited only); SECOND_HOUR and REVIEW_GUIDE in the element folder; the offset-lean and dirac-time-lean repositories (no GitHub access from this session).
