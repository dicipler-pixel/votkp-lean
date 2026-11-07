# Path notes: Dirac Time, then VOTKP (working notes, not a deliverable)

Jeromie Beasley · started 7 November 2026

Rule for this pass: read in full first, log what needs changing, fix nothing until the whole picture is in.

## Yardstick: IQGT v7.3.1 (GitHub iqgt-grassmannian-lean, paper/iqgt_grassmannian_v7_3_1.html)
- Projector first. Geometry lives on Gr(k,H); parameter spaces only pull it back.
- Q = g − (i/2)Ω, Ω = +i Tr(Π[V,W]), g = ½ Tr(VW), F_Q = (4/k) g.
- Tangents are block off-diagonal; "silent" means first-order silent (Prop 4.3, Prop 8.6).
- The intrinsic metric is not a spacetime metric. A degenerate metric needs a connection supplied.
- Dissipation only with a declared bath (friction law, §5.3).

## Paper 1: Dirac Time long form v3.1 (6 Nov 2026), read in full
State: v3.0.1 fully preserved (0 lines deleted, 6 declared swaps, 9 paragraphs with insertions only; checked independently). DT31-NOLOSS-01 and DT31-CHK-01 rerun here: all pass, same numbers as stored.
Conventions agree with the IQGT throughout (§6, App D.1, §12.6 = IQGT §5.3).

Changes needed (to make later, not now):
1. Abstract, last sentence: states Claude's F reading as fact. §18 labels it "proposed" and the ledger says it waits for his own F and Θ. Abstract must not carry Claude's version as his.
2. App A.2 cites the August IQGT (Zenodo 21804717). Cite the current IQGT ("Intrinsic QGT on the Grassmannian and Spectral Lower Bounds on Dissipation", v7.3.x). The two papers share the friction law; each should cite the other.
3. G.1: monopole paper listed "with GPT (OpenAI) and Claude (Anthropic)". Check against the monopole paper's own title page and the name-only byline rule.
4. "Measured" used for numerics: §17.1 ("measured on finite blocks", "the location measured"), Fig 11 caption, G.2 DT31-FIGS row. Should say computed.
5. §10.5: "√E_B = k/√3, the radiation sound speed". It is the sound frequency (sound speed 1/√3 times k).
6. §5.2 addition reads the −1 through a gauge potential A_N. Correct, but IQGT Example 6.5 gets it gauge-free from curvature over the cap; consider the projector-first phrasing.

His calls (from the v3.1 ledger): his own F and Θ for §18; 13a_4018 naming convention; θ on the mirror diagram (one computation, not run); VOTKP 19 blind pairs vs Dirac 2,525 thin pairs (different filters, not reconciled).

Where Dirac touches VOTKP v2.9: §6.2 (VOTKP §4), §11.3 (VOTKP §5.6, 5.9, 5.10), §15.6 gate 11 (VOTKP §15.8), §17.1 (VOTKP §15.4), §13.5 census (VOTKP ADM-01 SIG-01).

## Paper 2: VOTKP v2.9 (13 Oct 2026, Zenodo 10.5281/zenodo.23340757), read
Access: PDF (165 pp) and zip uploaded 7 Nov. Zip holds scripts, data, Lean, checks; no paper source. Prose read in full from the PDF text, §§1–22 and App A–C; App D–G (test ledger, literature, scripts, data ladders) searched rather than read line by line. The PDF stores equations as images, so the math was checked by rendering pages where it decides something (p46, p53, p61 so far).
Title page says "developed with AI assistance"; App F: "Written by Claude from Jeromie Beasley's research programme and his collaborators' reviews".

Against the IQGT yardstick: holds.
- §9 Snell test uses g∥ (turns where g∥ < C²), not λ_min. Same index as IQGT §8.
- §19.4 keeps the Poincaré (peel) metric and the intrinsic Grassmannian metric apart: "Neither is the other without a declared map". Exactly the don't-mix-models rule.
- §19.5 friction bound uses IQGT §5.3 with the bath declared; §19.7 reproduces IQGT §8.4 polar stratum, notes folds differ (IQGT §8.5).
- §15.2 Einstein addition / radar reading fenced: "a representation: nothing in the atom moves". §19.6 Penrose comparison labelled structural, "not a spacetime metric".
- §20.2/20.5: adding cI leaves projectors fixed; energy origin needs calibration (same as Dirac §9.4).

Every place Dirac v3.1 leans on VOTKP checks out against the text:
- Dirac §6.2 ← VOTKP §4 "Spacing is not enough" ✓
- Dirac §11.3 ← VOTKP §5.6 (side condition, real symmetric in Lean), §5.9 (miss one by at least half the gap) ✓
- Dirac §15.6 gate 11 ← VOTKP §15.8 (PDG 5.6 TeV) ✓
- Dirac §17.1 ← VOTKP §15.4 (5He 1.074, 5Li 1.220, 8Be 1.025, 4He 0.579) ✓
- Dirac §13.5 ← VOTKP §11.4–11.5, §13.7: window t ∈ (0.4388, 0.4609) = α ∈ (0.10971, 0.11522); 60-digit longitudes match, including signs (13a_4018 −0.01717, its mirror +0.01717) ✓

Resolves one open item in the Dirac v3.1 ledger:
- "VOTKP 19 blind pairs vs Dirac 2,525, not reconciled" is a misreading. Both numbers are in VOTKP and answer different questions: 19 = pairs at 13 crossings with equal Alexander+Jones but different HOMFLY (§11.2); 2,525 = thin, same-signature HOMFLY-blind pairs through 13 crossings (§11.4), of which the signature function separates one (§11.5). Nothing to reconcile; Dirac's ledger line should be corrected.

Changes needed in VOTKP (later):
1. Cites IQGT v6 (Zenodo 23250681). Current is v7.3.x; section numbers it uses (§§2–5, 8, 10; §5.3, §8.4, §8.5, §§10.3–10.4) still line up — verify against the newest cut before swapping.
2. Cites "Dirac Time, v3.0.1" with no DOI. v3.0.1 DOI is 10.5281/zenodo.22978631 (or cite v3.1 when it is deposited).
3. §13.7 checks torus-knot counts numerically (TIME-01a, 135/135, "under orientation and genericity conditions [Lin, Herald]"). Dirac v3.1 Theorem 13.2 now PROVES arc count = |σ|/2 = |ρ|/2 for every torus knot (and all arcs carry one sign). VOTKP §13.7 should cite it.
4. §13.7 "No Hamiltonian makes a knot's meridian phase the driven parameter; open" and Dirac T7/§25.2 are the same open problem; cross-reference both ways.
5. §21.2 xenon: numerical files not retrieved (access gap, stated). Still open.

Where the two papers meet, for the big picture:
- Same predictive quotient (VOTKP Thm 3.1 = Dirac §2), same Schur/memory kernel (VOTKP 5.3–5.4, §20.3.3 = Dirac §10), same correlation-phase witness (VOTKP §20.5.2 = Dirac P5a / §11.4), same signed offset with sign flip under C → I − C (VOTKP §20.5.5 = Dirac §9.4 offset).
- Same 13-crossing window; VOTKP found it (ADM-01/TIME-01), Dirac proved the torus-family law around it.
- Dirac's feedback/stability model (§23) is cited by VOTKP §20.4.2.

Next on his path: VOTKP's Nov scope (colour of the elements, Two Trees in One Ball v4, matter-disk, Smith/Snell charts, The Weight Between, monopole paper) per notes; confirm order with him.

## Oct–Nov reads (full-read helpers; their notes in notes/reads/)
### When the Neutrinos Leave v5.1 (5 Nov, 72 pp)
- Matches Dirac §10.5 item for item. Qualifier: the 7–10% return holds for planting at/after decoupling only (0.074–0.098); deep in the coupled era ≤ 8.6e-3. Dirac already says this.
- Changes: cite IQGT v7.3.x (it cites v7.2); DOI of Non-Normality Is Connection Energy (paper 22804072 vs notes 22803572) — check; cite Dirac v3.1 and VOTKP v2.9 (its Smith/rapidity link coordinate is the VOTKP peel coordinate, uncited); "measured" used for simulation output (§§3, 7); abstract overbroad on "equals the sound speed" and "no closure can carry this memory". Lean: public main is v3 (84 thm); paper's commit c372d3f (100 thm) not on public main.
- Coverage: main text, App A, B.1–B.7, C in full; B.8–B.18 run logs sampled.
### Monopole paper v5.0 (5 Nov, 15 pp; Drive zip; repo main still v4, v5 on branch v5-seam d02b612)
- Byline on the title page: "Jeromie Beasley · GPT (OpenAI) · Claude (Anthropic)" as three authors. Conflicts with the name-only byline rule — his call; Dirac G.1 copies it.
- Dirac §5.2 checks: curvature ½ sinθ, flux 1, a_N=(1−cosθ)/2, a_N−a_S=1 all Lean-checked. The equatorial holonomy π / half-flux reading is NOT stated in the monopole paper; it is Dirac's own (correct) inference from a_N(π/2)=½ — Dirac should say so rather than attribute it.
### Two Trees in One Ball v4 (30 Oct, 101 pp, Zenodo 23847114; Lean in votkp-lean/two-trees, 159 thm, core Lean)
- Results: ln 5 boosts generate a free group (all lengths, Lean); every whole ratio z ≥ 2 free (odd divisors Lean; even ratios written ping-pong only); Schottky line Γ² = 1/2; at ln 5 commutator is infinite-order rotation (cos φ = −527/625): free, not discrete; Thomas rotation tan(θ/2) = Γ² (Lean); not conjugate to LPS group; ln 7 constants optimal; knot commutator band criterion (Lean), T(2,3), T(2,5), T(2,7) never turn; 26-knot census 19 turn / 7 never.
- Links: built on VOTKP Thm 8.1, 15.1, §15.2; knot family shared with Dirac §13. No IQGT content.
- Changes: §8.3 count is first-letter-fixed (full is 2,929,686, not 488,281); §6 "|M|≠1 ⇒ conjugate into SL(2,R)" not general; §8.2 simple transitivity graded proved but not proved; §5.3 extrapolation stated as fact; add one line that the Lorentz language is structural (no spacetime metric); cite VOTKP v2.9 (23340757), not 23011140; §3 typo ±5r → ±5^r; abstract should say even ratios are not in Lean.
- Coverage: body full; Lean source and scripts not line by line.
### "VOTKP colours of the elements" (1 Nov, 11 pp) — NOT his paper: an AI-compiled report for him from nine "colour bots"
- Findings: gold metamer ΔE 8.6022; gold edge 2.46 eV; registered test: a visible ground-state line follows IE₁ (AUC 0.946, 65 of 105 elements); Γ₁ tracks colour only weakly (|ρ| 0.352 vs 0.897 for the level); colour comes from molecules, d–d, f–f, charge transfer, oxidation state.
- Changes if it is ever used: misspells his name "Jeremy"; "peel shape" overbroad (only Γ₁ tested); "passed on Z 14–118" should be 65 of 105; "matches what people see" compared to described swatches only; §5.2 heading/table mismatch.
### Colour Selects the Leader v1.2 (2 Nov, ~70 pp, Zenodo 23876186)
- Results: Schrödinger colour metric splits exactly into brightness line + chromatic sphere; waveplate between polarizers gives two complementary ports ("two books"); Perron-leader selection (Schrödinger distance stretches in 955/20,000 passes, Hilbert distance 0); bend of log-brightness = squared Fisher speed; uses offset speed limit and predictive quotient; perception reanalysis favours log on grey; Rule 30 colour result corrected as a duplicate-row artefact.
- Changes: cites IQGT v7.2 (→ v7.3.x) and Dirac v3.0.1 as Zenodo 22979186 — CONFLICT with notes (22978631); one of the two DOIs is wrong, check on Zenodo before touching any citation. Missing citations: Exner, Englert, Mandelstam–Tamm, Bisognano–Wichmann, Fox, clock-sensitivity inputs. §12 frames Λ as time-conjugate in unimodular gravity — his call against his rule that Λ is a term in the field equations (unimodular is not dark energy, but it reframes Λ). "Measured" in script comments for simulations. §9 refractive index and √k in Davis–Kahan unreadable in text — check on rendered pages.
### θ census: "The θ invariant as a chirality detector" (2 Nov, ~80 pp build read)
- Counts confirmed: 12,965 knots, 12,887 nonzero, 78 zero; grid certificate 78 rows, 66,728 cells; Alexander gate 249/249 and 12,716/12,716; published table: 208 identical, 21 equal up to sign, 20 joint zeros; Conjecture 21 stated as conjecture.
- The window-pair θ values Dirac §13.5 quotes are NOT in this build (App C per-knot data empty in extraction). They must come from the later 223-page version the 1 Nov review addendum covers — locate it.
- Changes (in this build): abstract and §9 say 3 of 78 certified while §5.4 says all 78; 21 sign cases still "unresolved" (the addendum resolves them 21/21); "nine" representatives but eight named; §1.2 overstates what Conjecture 21 forces; §7 cites §2.4 for a gate in §2.3.
### "The 21 sign cases now reproduce exactly" (1 Nov, 2 pp) — external review addendum prepared for him, not his paper
- 21/21 sign-opposite knots now match the published θ table using original KnotTheory diagrams; 63/63 Alexander gate comparisons; asks five edits to the 223-page manuscript. Dirac G.1 cites it.
### The Offset Speed Limit v1.1 (26 Oct, 7 pp; title page still says "Version 1"; no own DOI)
- Theorem 1 τ̇² ≤ 4gS with equality iff Ṗ ∝ [P,[P,F]] — re-derived correct; Theorem 2 exact gap; Prop 5 g = E_B = Var H; Corollary 4 τ̇² ≤ 4Sζ/w_min (model-dependent). "Rate is weight" and Th/Sr clock test open. Matches Dirac §9.4, §12.6.
- Its speed-bound Lean files are local, not public → Dirac must not grade the speed bound as Lean-checked (Dirac currently says "[T]" only — OK; keep it that way).
- Changes: "measured from the evolving projector" (computation); stale C5 label "(12)"; c1,c2 missing; two-branch check is mod 2π; cite the 10⁻⁸ limit; state Anandan–Aharonov normalisation; version label.
### The Weight Between v1.1 (26 Oct, 8 pp)
- Predictive quotient + finite closure (Lean); E_B as speed, variance, zero-lag memory; connection-energy identity; the two books; log-convex gap-power ladder; light at rung −1; three-port ring G₁₂−G₂₁.
- YARDSTICK CONFLICT: writes Ω = 2 Im Q; IQGT gives Ω = −2 Im Q (from Q = g − (i/2)Ω). Sign flip.
- Changes: polariser ports look swapped; cites IQGT v7.2 and Dirac v3.0.1 as 22979186; "Born note v4" missing from references; App A lists checks belonging to the companion paper; two garbled passages (§3 survival, §4 trefoil) — read on rendered pages before judging.
### The Weight Between and the Exit Line v4 (4 Nov, 22 pp; + review ledger)
- Cross-block bounds (Thm 3.1), 4 Tr X_A ≤ I_G (Thm 3.7); Prop 4.2 ⟨K⟩ = 2 iff E(0)E(π) = u² [T][L] (re-derived); [C_R,T_R] = 0; elliptic ladder [V] only; conditional exit theorem; analytic derivation open.
- DIRAC §17.1 MUST CHANGE: it says the HALF-chain correlation matrix is a biorthogonal idempotent — wrong; the WHOLE-chain matrix is, the half-chain block is not (Thm 4.1). Also: the exit line is verified numerically [V] (theorem only conditional on the ladder form), and it fails on the second, massive model (s06 killed) — Dirac should not read as universal.
- Changes in the paper: abstract bounds (8.37e-12, 4.21e-7, not "8e-12, 4e-7"); "measured" for finite-block computations; name the Lean library/commit for [L]; missing citations (PT-SSH, Petermann factor, his own Offset Speed Limit); "weight between" here means X_A, not E_B — say so; Zenodo description for v4 not written.

### DOI to settle (cross-paper)
- Dirac v3.0.1: notes say 10.5281/zenodo.22978631; Colour Selects the Leader and The Weight Between both print 22979186. One is probably the concept DOI and the other the version DOI. Check on Zenodo (blocked here) before editing any citation.
### Matter, Then On Down, Edition 4 (4 Nov, 86 pp; Lean in votkp-lean/matter-disk; no DOI)
- Census A = 2c/π²; weight between 0 ≤ X ≤ F ≤ 1/4; one chart Γ = tanh(½ ln z) where peel steps add; Saha ladder inversion (helium Γ₀ = 0.37757507); 5He/5Li/8Be outside the nuclear disk; opened matter: Petermann factor and exit line E(0)E(π) = u².
- Changes: abstract "four times" bound is I_G/4; curvature sign differs from IQGT; 8Be ordering text vs scripts; "measured" for computations; [L] tags don't say what Lean covers; §9.4 conflates the exit with the exceptional point; Thm 9.2 metric degenerates with no connection supplied (IQGT fold rule); filter table vs script s09; IQGT DOI unversioned; does not cite Dirac despite overlap.
### Matter, Gases and VOTKP: Formal Research Edition (3 Nov, ~53 pp; Lean 34 declarations, 5 false controls; prepared with OpenAI tools)
- Formal source for Matter Then On Down: B1–B13 (incl. 4 Tr X ≤ I_G), D1–D7, G1–G9 Saha/gas inverses, M1/M2, K1–K4, P1–P3 (P3 counterexample).
- Coverage: Drive text stops mid-§16.6; rest of §16.6, §17 and Lean inventory unread — needs the file uploaded.
- Changes: 11.3/11.4 order; dispute narration in §1, §16; Dirac not cited.
### What the Present Must Keep v1.2 (prints 3 Nov, 16 pp; five Lean repos; HANDOFF (1),(2) are its review handoffs, branch joint-paper-edits, unpushed)
- Memory kernel Tr K(0) = E_B; speed limit nearly saturated by free streaming (0.99996); gap ladder with optical bound α₀ ≤ 2(g²F)^(1/3); neutral-signature wall at y = 0; neutrino ledger K1–K5 with K2 failing (worst miss 0.101).
- Changes: §7.4 and §9 contradict abstract/§7.5 on a factor of two; 0.511 vs 0.513; Ω sign differs from IQGT; IQGT cited v7.2; "measured" for simulations; version mismatches refs [1],[4],[5],[6]; Prop 14 degenerate metric with no connection; Sr/Th-229 estimate has no script; test B missed by ~17σ yet counted inside the kill line; abstract says four results, lists five; restates Dirac v3.1 material without citing it.

## THE FULL PICTURE (7 Nov, after all reads)
Patterns across the Oct–Nov papers:
1. Ω sign. The Weight Between, Matter Then On Down and What the Present Must Keep all use the opposite curvature sign to the IQGT (Ω = +i Tr(Π[V,W]), Ω = −2 Im Q). Check each: a paper may define its own sign consistently, but the corpus should use one.
2. Citation drift. IQGT cited at v6 or v7.2 almost everywhere (current v7.3.x). Dirac v3.0.1 DOI conflict (22978631 vs 22979186). The Nov papers that restate Dirac (Matter, Present Must Keep, Neutrinos, Formal Edition) do not cite it; Neutrinos does not cite VOTKP.
3. "Measured" for computations: Dirac, Neutrinos, Offset, Exit Line, Matter, Present Must Keep, Colour (scripts).
4. Degenerate metric with no connection supplied (IQGT fold rule): Matter Thm 9.2, Present Must Keep Prop 14.
5. Lean status claimed but not public: Offset speed bound (local), Neutrinos commit c372d3f, monopole v5 (branch v5-seam), matter-disk branch.
6. Byline: monopole paper lists three authors; Dirac G.1 copies it.
7. Not his papers, kept as background: "VOTKP colours of the elements" (AI report), "21 sign cases" (review addendum).

Dirac v3.1 change list, complete so far:
D1 Abstract last sentence states Claude's F reading as fact (§18 says proposed).
D2 Cite current IQGT (v7.3.x); settle the v3.0.1 DOI.
D3 Monopole byline in G.1 (his call).
D4 "Measured" for numerics: §17.1, Fig 11, G.2.
D5 §10.5 "sound speed" → sound frequency (Neutrinos paper has the same overreach in its abstract).
D6 §5.2: the half-flux holonomy is Dirac's own inference (monopole paper does not state it); present it so, optionally gauge-free as IQGT Ex 6.5.
D7 §17.1: WHOLE-chain correlation matrix is the biorthogonal idempotent, not the half-chain block; exit line is numerical with a conditional theorem, and fails on the massive model — not universal.
D8 v3.1 ledger line "19 vs 2,525 not reconciled" is a misreading (both in VOTKP, different questions).
D9 §13.5 θ window values: source is the 223-page θ census, not the 80-page build on Drive — locate it.
D10 Speed bound stays [T]; do not claim Lean-checked (files local).
Still unread: Formal Edition §16.6–end; the 223-page θ census; Roots_Rings_Branches_and_Clay (4 Nov) not yet identified.

## VOTKP research, 7 Nov — the branch cut (exploring; nothing graded yet)
The line of thought:
- Peeling moves the occupied subspace through the Grassmannian; the energy ladder is only its shadow on one line (VOTKP §19.4). Straight steps add and leave nothing but endpoints; turning steps enclose area, kept only in the phase (VOTKP §15.2 Thomas rotation, Two Trees tan(θ/2)=Γ², IQGT Ex 6.5). Turning is what can make "space".
- Hypersurfaces are where the motion changes character: subspace stops (wall, reflect), sheets meet (fold), gap narrows (channel) — IQGT §8.
- A cut at a fold splits into TWO branches that are mirror images: equal in every even record, opposite in every odd one (three-body triangle/mirror, IQGT Ex 8.8; Dirac ΓP₊Γ = P₋). The metric alone cannot pick the branch; a direction (time) must.
- Parallel vs opposed: curvature only from the crossing part, |Ω| ≤ 2√(g_VV g_WW)|sin θ|; parallel and antiparallel make none; the sign is the hand. Structural likeness to Maxwell stress only.
- Light the path, electron the ground (Smith disk: centre open, rim −1 conductor). Closing a space needs both; closed → discrete modes → a gap → the gap holds the subspace. Dirac Prop 15.3: magnetic closing alone cannot hold itself; it needs the electric side too.
- Question to him (open): when both are cut, does one closed space form between the two mirror branches, or does each close on its own?

## The physical counterpart: Hall, Tai, Kauffman, Smalyukh, "Fusion and fission of particle-like chiral nematic vortex knots", Nature Physics 22, 103–111 (online 15 Dec 2025), doi:10.1038/s41567-025-03107-0; arXiv:2508.05841
- Fusion: vortex-line segments with OPPOSITE twists cancel and form new composite knots; reversing the voltage splits them; subsecond.
- Reconnections can BUILD new long-lived structures (composite knots, multi-loop links), not only simplify.
- A topological invariant is conserved through fusion and fission (summed Hopf index).
- Cores of the vortex lines are achiral: molecular twist cannot be defined there — the hypersurface where orientation collapses.
- Made by light (laser tweezers melt a spot), set by cooling (relaxes into heliknotons), switched by electric pulses (fuse or split): light makes, cold keeps, electric chooses the direction.
- Knot-theory moves realized physically: connected sum (fusion), band surgery (fission) = VOTKP §11.3 band peels; VOTKP §17 open item "the maps of band peels" has a physical system that performs them. VOTKP §12/§15.6 cite it only as field loading.

### BRANCH-CUT-01 (exploratory, 7 Nov; scripts in /home/claude/votkp_research/branch_cut_01*.py)
Construction: fusion = connected sum = block sum of Seifert matrices; parallel K#K, opposed K#mirror(K) (mirror Seifert = −Vᵀ); Levine–Tristram form H(ω) = (1−ω)V + (1−ω̄)Vᵀ. Knots 3_1, 5_1, 7_1, control 4_1 (amphichiral). Seifert matrices checked by their Alexander polynomials.
- Even records survive either way: Alexander polynomial equal (up to sign), determinant equal (9, 25, 49; 25 for 4_1), projector metric speed exactly 2× K's for BOTH fusions at every phase read (spread 0).
- Odd record: parallel fusion signature = 2× K's at all 400 phases; opposed fusion signature = 0 at every phase.
- Opposed fusion's spectrum is exactly ±-paired (|λ_i + λ_{n−i}| ≤ 4e-15): the mirror block is −H̄, so opposed fusion builds a chirally paired operator — exactly the Dirac §5.3 negative control, made by fusing opposites.
- The hand is not destroyed: the block-odd probe Tr(P₊ Z), Z = +1 on K, −1 on the mirror, returns K's signature at 400 of 400 phases. The scalar spectrum forgets the hand; the projector keeps it (Dirac §5.3 "the only place the orientation can live").
- Control 4_1 behaves as it must (both fusions identical, signature 0).
Reading: opposed branches cancel in every odd SCALAR record, keep every even record, and store the hand only in the subspace. Parallel branches double it. Matches the vortex-knot fusion (opposite twists cancel, an invariant conserved).
Grade: the algebra is elementary (signature additivity under connected sum is classical; K # −K̄ is ribbon/slice, i.e. cancels in the concordance group — prior art to cite). What is new here is the reading: opposed fusion produces Dirac's chiral pairing exactly, and the hand moves from the spectrum into the projector. Untested on the physical vortex knots.
Next to explore: fission (band surgery) — what a band move does to H(ω), the walls and the projector; and the Dirac-time windows of K#K vs K#mirror(K).

## Paths carried forward (from the atlas map, cards B1–B207), 7 Nov
- P1 Metal reflection as a Smith track: Γ = (1−N)/(1+N) across the visible (VOTKP §6.3). Cards B97, B98, B189 (coordinate, ⊕), B175 (passivity: inside the disk; absorption = 1−|Γ|²), B100/B101 (film circle; complex-index shunt). Gap: "two books" (B189) proved only for positive real ratios; for a metal the books are |Γ|² (seen) and arg Γ (phase, thrown away in bulk). Idea: a thin oxide film turns the hidden phase back into colour — metals matched in bulk colour but with different phase tracks should separate under the same film.
- P2 Colour perception as a declared reduction: the eye keeps 3 numbers; metamers are hidden distinctions; [W, Π] ≠ 0 is exactly when they come back (B31, B22, B65); associator (B105); certificate (B161); test design (B110, B132, B108). Per-metal "key strength" (commutator size): Cs, Bi, Au, Cu strongest, Hg nearly dead. Prior art: metamer mismatching (Logvinenko, Funt, Godau). VOTKP §6.2 surviving-matches theorem vs Dirac §2.4 (RL = AR) — same statement? not yet checked line for line.
- P3 Two Trees in optics: film stacks compose like the boosts (VOTKP Cor 15.3, Vigoureux); metal Γ complex → loxodromic words in SL(2,C). Bi tarnish, anodised Ta are real multilayer words. Lead seen in data: Schottky line |Γ|² = ½ sits near the metal/non-metal split (most metals above; B, C, Si, Ge, Se, Te below; Zr, W also below).
- P4 Knots and seen colour: no bridge on any card (B53 name clash, B106, B59). B174/B172: Gram-type readings can't see handedness; the CIE eye is Gram-type, so hue can't carry knot chirality.
- X02 (on B22/B25): absorption reads the quantum metric, g = (1/π)∫ Im α / x² dx — each element's optical spectrum gives its own g, gap-weighted: the "space between" on the periodic table.
- His question (connection-energy foundation): "the pattern is close but not quite right; we must be missing a small key in the foundation. In my connection energy work I saw a key flipping in the NASA video; as it switched axis I also noticed its climb, due to what I called the angular momentum of the switching." (Connection Energy v15: tumbling rate √ab = |Ω|·√((I₃−I₂)(I₂−I₁)/(I₁I₃)), trace form q decides climb (q>0) or turn (q<0).)

### FLIP-KEY-01/02 (exploratory, 7 Nov) — the small key in the foundation
Prior art: intermediate-axis (tennis racket / Dzhanibekov) instability; Montgomery 1991 phase (Δθ = 2ET/|L| − solid angle); rigid body as Lie–Poisson / double-bracket structure (Bloch, Brockett, Ratiu; Bloch–Krishnaprasad–Marsden–Ratiu, Commun. Math. Phys. 175, 1 (1996)); Van Damme et al. tennis-racket papers (arXiv:1606.08237, PRL 125, 064301).
Findings (body I = 1,2,3 unless stated):
- Climb rate at the intermediate axis = 0.577350 = Connection Energy's √((I₃−I₂)(I₂−I₁)/(I₁I₃))·Ω exactly; zero at the outer axes.
- The small key: an axis climbs exactly when its two neighbouring gaps have opposite sign, (I_k−I_a)(I_k−I_b) < 0 — i.e. it is the sandwiched level. Extremal levels turn. (Same as Brockett's flow, IQGT §4.4: only top/bottom eigenprojectors are stable; middle ones are saddles.)
- The switching's memory is IQGT curvature: n = L/|L| is a point of Gr(1,ℂ²); the gauge-free overlap phase of P(t) = (1+n·σ)/2 around one period = −½ × enclosed solid angle (2.094391884 vs 2.094391880). Montgomery's rotation reproduced to 1e-8 (−0.562448297 vs −0.562448306).
- Near the flip, the enclosed area is a LUNE between the separatrix planes L₃ = ±k L₁, k = √(I₃(I₂−I₁)/(I₁(I₃−I₂))): area 4 arctan k or its complement — which lune is the branch the motion takes. Checked on six bodies.
- 45° again: k = 1 exactly when 1/I₂ sits midway between 1/I₁ and 1/I₃ (the energy operator I⁻¹ has equal gaps either side of its middle level). Then the separatrix planes are at 45°, all four lunes are π, and both branches carry the same area. Unbalanced bodies: the two branches carry different areas.
- Connection to BRANCH-CUT-02: paired/equal-gap spectrum ⇒ 45° in both places (opposed knot fusion: projector at 45° to the cut; balanced key: separatrix at 45°). In both, the sandwiched/shared part is where the branch is chosen, and the hand is stored in which side.
- Structural echo (not identified): tan(α/2)-type laws — lune half-angle tan = k (ratio of gaps), Two Trees Thomas rotation tan(θ/2) = Γ².
Grades: the rigid-body facts and Montgomery's formula are known (reproductions in this coordinate). The lune limit formula is derived here and likely known in the tennis-racket literature — check before claiming. New: the reading that the climb is the sandwiched-level saddle of the same projector geometry, its memory is IQGT curvature, and the balanced case reproduces the 45° of the mirror fusion.

### SILENT-WALLS-01 (lead A, exploratory) — VOTKP Table 6 double walls
- Reproduces VOTKP Table 6 exactly from KnotInfo: 575 double unit-circle Alexander roots, 494 silent, 81 jump ±4. Every double root sits on a squared factor f² (forced: distinct irreducible factors share no roots).
- Where KnotInfo records algebraic concordance order: finite order (1, 2, 4) → 65 of 65 double walls silent; infinite order → 61 silent, 21 jump ±4. By topological 4-genus: g4 = 0 or 1 → 113 of 113 silent; ±4 only at g4 ≥ 2 (g4 = 4: 6 of 6 jump).
- Known theory forces most of this: the Levine–Tristram signature is a concordance homomorphism (finite order ⇒ σ_ω = 0 generically ⇒ every wall silent), and |σ_ω| ≤ 2 g4 bounds the jumps. So "finite order ⇒ silent" is a theorem, not a finding.
- What it supports: the silent double walls are exactly the opposed-fusion pattern — a squared factor whose two copies carry opposite hands. Algebraically slice examples (the form has the cut L): 8_20 (Δ = (t²−t+1)², the trefoil's square — same as 3_1 # mirror 3_1), 10_87, 10_123, 10_140, 11a_28, 11a_58, 11a_165, 11n_73, 11n_74, 12a_169, 12a_189, 12a_377. Not forced and still open: the 61 silent double walls in infinite-order knots — hands cancelling at that wall without the whole knot cancelling.
### TILT-01 (lead B, exploratory)
- Exact mirrors: projector locked at 45° to the shared half at every phase. Deform the mirror slightly (V ⊕ −(V+εD)): the form on the shared half grows linearly in ε (0.039 at ε = 0.01, 3.86 at ε = 1), and ±2 signature windows reappear (the hand leaks back out).
- Where the lock breaks (ε = 0.03): median deviation 0.57° far from walls, ~2° near walls, with full 45° swings near the walls (near-zero eigenvalue: the tip is free at a tie). The 45° is a rigidity of exact mirrors; mismatch is felt at the walls first.
- Unlike pair 3_1 # reversed-mirror 5_1: signature values {0, 2} — windows survive; hands do not fully cancel.

## OPTICS-01 (P3, X02), 41 elements, refractiveindex.info widest set covering 0.38-0.78 um (exploratory)
- P3, Schottky line |Gamma|^2 = 1/2 (visible mean): metals 35/35 above, non-metals 0/6 above. Closest to the line: Nb 0.506, Te 0.486. Lead holds on this set; the line is clean but thin near Nb/Te.
- X02, IR slope of the running integral of eps2 (the quantum-metric/localization integral, Souza-Wilkens-Martin/Resta): metals are clearly nonzero (-0.2 to -1.05); C and Si are ~0. Direction matches "metal = divergent localization, insulator = finite."
  Caveats: the slopes are shallower than Drude's -2 because most datasets stop above the Drude regime (cuts at 0.16-0.3 eV); Bi, Hg and Li give 0 only because their data doesn't go deep enough into the IR. A clean X02 needs far-IR sets.

## FILM-PHASE-01 (P1), film_phase_01.py
- 39 metal pairs the eye matches in bulk (CIEDE2000 < 2, D65), each put under the same n=1.5 film, 10-300 nm.
- The mean Smith-phase gap (arg Gamma) between the pair predicts how far apart their film colours go: Spearman rho = 0.64 (p < 0.001).
- Biggest: Rb-Ta (phase gap 58.5 deg) -> film dE up to 16; Fe-Mo, Lu-Mo (13-14 deg) -> 11-12. Smallest: Lu-Mn (0.8 deg) -> 0.84.
- Outliers: the alkali pairs (Ag-Na, K-Na, Mg-Na, K-Mg) have large phase gaps but small film shifts. Likely the Gamma magnitude near 1 (|r12| ~ 1), so the film interference reads the phase only weakly. Worth a look: phase that is present but not "loaded."
- Reading: the Smith phase is a hidden record that bulk colour throws away and a film writes back out. This is P1's claim, seen on real data.

## PRESSURE-LINE-01, the 2/3 vacuum line under squeeze (pressure_line_01.py)
- Squeezing shrinks the room and leaves the atom alone, so an element crosses E = 2/3 at V/V0 = 3(1 - E0). Measured metallization pressures: Wikipedia table, experimental rows (B 160, Si 12, P 4.8, S 83, Ge 11, Se 23, Br 25, Te 4, I 16 GPa).
- Two families appear.
  - Molecular/chain solids (Te, P, I, Se, Br, S) have open, vacuum-like room. The squeeze needed to reach 2/3 ranks their metallization pressure, Spearman 0.89 (p = 0.02, n = 6). Order: Te 0.07 -> 4 GPa, P 0.10 -> 4.8, Se 0.28 -> 23, I 0.31 -> 16, S 0.46 -> 83, Br 0.57 -> 25.
  - Network solids (Si, Ge, B) already sit on the line (0.665-0.673) and still need 11-160 GPa. Their room is filled with bond charge, not vacuum: they sit on the wall and need a rearrangement (a coordination change, diamond -> beta-tin) rather than a squeeze. That is the same shape as the saddle in FLIP-KEY: on the wall, the change is a flip. Structural reading, untested.
- Absolute pressures from the Murnaghan EOS (B0' = 4, pymatgen B0) come out 2-4x low; the bulk-modulus data is rough. Rank only.
- Next: add gases (O 96, Xe 130 GPa; Cl) with low-temperature solid densities; Br is the one molecular out-of-order point.

## GEO-PHASE-01, the two books of the Smith track (geo_phase_01.py)
- Climb = hyperbolic length of Gamma(lambda) on the Smith/Poincare disk. Turn = signed hyperbolic area enclosed with the closing geodesic (the Bargmann/Berry term, the same object as Montgomery's solid angle). Area routine checked on a geodesic triangle: 0.76682 vs pi minus angle sum 0.76647.
- Every element turns the same way: the area is negative for 38/41, and the other three (C, Be, Nb) are ~0. One handedness across the whole table. Possible cause: causality (Kramers-Kronig) fixing the direction the track runs. Untested.
- Free-electron metals ride the rim, the ground at Gamma = -1: K -32.7, Na -31.4, Rb, Ag, Ti, Mg ~ -10 to -12. Bonded transition metals and non-metals sit at ~0. The turn does not split metal/non-metal cleanly (Te, Ge overlap Zr, Cr, Fe).
- Near the rim, turn and climb merge (rho = -0.99 among metals). That is hyperbolic geometry near the ideal boundary, where enclosed area tracks perimeter.
- Among metals, more space between -> more turn (rho -0.43), the same direction as the earlier space-between vs arg N result.

## FILM-GEO-LINK-01 (film_geo_link_01.py)
- The film writes back the phase gap as colour gap ~ (phase gap)^0.34. Pairs that under-read are pairs where both elements ride the rim: residual vs pair min|turn|, rho = -0.52, p = 0.0007. (Mg-Na, K-Mg, K-Na, Ag-Na; Lu-Mn is a tiny-gap pair.)
- Reading: near the ground the phase is present but pinned. |Gamma| ~ 1 makes the film reflection all-phase, and the two rim tracks move together, so the film can't pull them apart. "Present but not loaded."

## VOTKP first meaning: volume of the knot potential (Jeromie's hypothesis, held as his stance)
Hypothesis as he said it: the old VOTKP tried to map the volume from a HOMFLY / coloured Jones mix; the vectors now used may be what creates space and volume as we follow light. A space made by light strings would hold a vacuum.

## KNOT-VOLUME-01/02/03, the Jones string as light (knot_volume_01..03.py), 2970 hyperbolic knots, 3-12 crossings
- Setup: t = e^{i theta} runs once around the circle, the way colour runs violet to red; the Jones polynomial V(t) traces a closed string that leaves V(1) = 1 and comes back.
- Climb book = Mahler measure (mean log|V|). It carries volume: rho 0.854 overall and 0.66-0.84 within each crossing number. After log det (Dunfield's baseline, rho 0.925) is taken out, the climb still carries the rest: rho 0.50.
  - Fits: log det alone R^2 0.708; Jones climb alone 0.734; together 0.810; adding the Alexander climb 0.826.
- Turn book, counted as roots inside the circle (vacuum enclosed): nothing for volume (rho -0.02) and nothing for signature.
- Opposite count, turn = signed area swept / size: nothing for volume (-0.07), but it carries the handedness, |signature| rho 0.83.
- So the two books split cleanly: climb = volume (space made), turn = handedness. This is the same split as Q = g - (i/2) Omega in the IQGT (real part metric / size, imaginary part curvature / turn). Structural match, flagged; not a mapping of one onto the other.
- Torus knots (the Dirac paper's knots) have zero hyperbolic volume: they make no space in this sense. Worth keeping in mind for the Dirac-to-VOTKP bridge.
- Prior art to check before leaning on this: Mahler measure of the Jones polynomial vs volume (Champanerkar-Kofman line); determinant density (Champanerkar-Kofman-Purcell).

## HANDEDNESS-01 (handedness_01.py)
- Drude metals (9 cases) and single Lorentz oscillators (6 cases, including a line inside the visible band) all wind the same way as frequency rises, the same sense as the element tracks.
- So the one-way winding is not just normal dispersion: it holds through absorption lines. Likely cause: causality plus passivity (the family of Foster's reactance theorem), which is prior art.
- The exceptions (As2Se3 etc.) would need overlapping oscillators. Open.

## Pending
- Gases (O 96, Xe 130 GPa, Cl) in PRESSURE-LINE: need low-temperature solid densities. Br out of order.

## KNOT-CS-01/02, does the turn book carry Chern-Simons? (knot_cs_01.py, knot_cs_02.py)
Background: Friedl-Jackson 2011 left open whether the arguments of Alexander zeros relate to CS. KnotInfo 'volume_imaginary_part' is defined mod pi^2.
- The whole-string turn (swept area) vs CS: nothing. Signed rho 0.04; |turn| vs |CS| 0.09; as an angle r 0.01 (shuffled null 0.02).
- Alexander zero angles vs CS: r 0.07. Jones zero angles: r 0.08. Faint at most.
- Opposite, the turn read at single points t = e^{2 pi i/N}, N = 3..10: CS-angle r 0.16 at N=3 (V(e^{2pi i/3}) is a special mod-3 value), ~0.03 elsewhere. arg V vs signature runs -0.1 to -0.3, +0.33 at N=3.
- Reading: in the uncoloured Jones, the turn holds handedness (signature), not the Chern-Simons half. CS comes from the knot's geometric (holonomy) data, so a polynomial that carries both halves of complex volume needs the holonomy route (Mobius / Smith moves around the knot's loops), not the diagram alone.

## RIFE deep dive (agent report, 7 Nov). Kept for the light work only; medical claims are history, not results.
- Solid: the prism microscopes (Science Museum London holds No. 5, 1938, plus a beam ray tube); Kendall-Rife 1931; Rosenow in Science 1932; Smithsonian report 1944.
- Rife's illumination modes (monochromatic, polarized, dark-field, slit-ultra) can make particles below the Abbe limit visible as bright points (Zsigmondy). That is detection, not resolution.
- Kendall's filterable-forms claim failed replication 1932-33 (Craig & Johns; Swingle & Kiser).
- 1934 clinic: no records seen. "14/16 cured" traces to later recollection and Lynes 1987. The AMA plot story is undocumented. The lawsuit (1939), the FDA seizure (1960) and the Crane trial (1961) are real.
- Modern "Rife machines" are not his RF plasma-tube design. His own configuration has never been tested in any published study.
- Link to our work: "coordinative colour" = staining by light = dispersion staining (Christiansen). At the matched wavelength the index matches, the reflection crosses the Smith centre (vacuum, Gamma = 0) and its phase flips. Rife's colour is the wavelength where a thing's track passes through the vacuum point.

## CIRCUIT-POLY-01/02, first attempt at our own knot polynomial (circuit_poly_01.py, circuit_poly_02.py)
- The diagram as a circuit. Nodes = shaded regions; branches = crossings; right-handed crossing = admittance z, left-handed = 1. Q(z) = sum over spanning trees of z^(right-handed branches). Light leads: z = e^{i phi}.
- Kirchhoff check: Q(1) = det on 1846/1846 alternating knots.
- Redrawn diagrams in general: Q changes (3/50 unchanged), so for non-reduced diagrams it is a diagram quantity.
- Repair: on reduced alternating diagrams, 180/180 comparisons equal (up to the shading flip, Q -> reversed).
  - Reason (sketch, not a proof yet): by Tait's flyping theorem (Menasco-Thistlethwaite) reduced alternating diagrams differ by flypes. A flype acts on the Tait graph as a Whitney twist, which keeps the cycle matroid, so it keeps every spanning tree with its branches. A flype is rigid on the tangle, so it keeps each crossing's handedness. So Q is an invariant of alternating knots.
  - Caveat: some of the 180 may be the same diagram; the argument carries the weight.
- What it carries: it is coarse. Knots with all crossings one hand (3_1, 5_2) give a constant = det.
  - Climb vs volume rho 0.34, but it adds to log det: residual rho 0.44, R^2 0.708 -> 0.773 (Jones climb gave 0.810).
  - |turn| vs |signature| rho -0.51.
- Reading: on the diagram alone, the weights that survive every Reidemeister move are the Kauffman bracket ones (the Jones polynomial through the Tutte/Potts route). So "circuit + light, made fully invariant" leads back to Jones. Something better has to bring in what the diagram lacks: the holonomy (Smith/Mobius moves around the loops), which is also where Chern-Simons lives.
- Prior-art check pending: tree enumerators by crossing sign (Kauffman's clock states, Crowell), whether Q is already known.

## Carolina Figueiredo's work (with Arkani-Hamed, Cao, Dong, He, Backus; surfaceology with Frost, Salvatori)
Papers: Hidden zeros 2312.16282 (JHEP 10 (2024) 231); Scalar-scaffolded gluons 2401.00041; NLSM in Tr(phi^3) 2401.05483; Circles and Triangles 2403.04826; All-order splits 2405.09608; Tropical amplitudes 2402.06719; Backus-Figueiredo surface gauge invariance 2505.17179; Strings 2024 talk.
- The "numerator vs denominator" point: combinatorial geometry (associahedron, surfaces) gave the denominators (poles) of amplitudes, but real theories need numerators. Her clue was the hidden zeros: loci where the whole amplitude vanishes though no Feynman term does, with splits into products of smaller amplitudes near them. The one kinematic shift that keeps the zeros (even-even X up by delta, odd-odd X down) turns the denominator-only scalar theory into pions (and, from the stringy form, gluons). Numerators come out of shifted denominators.
- u-variables: one per curve on the surface, binary relations u_C + prod u_D = 1; curve words are products of 2x2 matrices (Mobius moves along the curve).

## SURFACEOLOGY-01, reproduction (surfaceology_01.py)
- Hidden zero, n=6: the 14 Feynman terms sum to exactly 0 on c_13 = c_14 = c_15 = 0.
- Delta shift: the leading term is -(X13+X24) at n=4, and exactly NLSM_6 at n=6 (ratio 1 at three random points). The numerator appears from shifted denominators.
- u-equations as Mobius cross-ratios: |u_C + prod u_D - 1| <= 4e-16 for n=5..8; Mobius change in u ~1e-15. The u's are Smith-chart invariants.

## Mapping onto VOTKP (structural, untested)
- Our circuit polynomial (Kirchhoff tree sum) is a denominator-only object, like Tr(phi^3): positive counts of trees. Jones carries signs, numerator-like. Her move suggests a parity shift on the checkerboard (shaded vs unshaded = even/odd) or on handedness, to find which shift keeps the polynomial's zeros and what appears at leading order.
- Zeros first: her shift was found from the zeros. Next we look for universal zeros and fixed values of our polynomials.
- Hyperbolic knots are glued from ideal tetrahedra whose shapes are cross-ratios (u-like, Mobius-invariant). Complex volume Vol + i CS is a sum of dilogarithms of those shapes. So both books (volume and the Chern-Simons twist) come from u-type variables. This is the holonomy route.
- Prior art: the A-polynomial (Cooper-Culler-Gillet-Long-Shalen) is built from holonomy; Boyd / Rodriguez-Villegas relate its Mahler measure to volume. Check where ours differs.

## SHAPE-DISK-01/02, what VOTKP seeks: volume as distance from the vacuum point (shape_disk_01.py, shape_disk_02.py)
- Setup: each ideal tetrahedron of a hyperbolic knot complement has shape z (a cross-ratio). Put it on a Smith disk centred on the regular tetrahedron w = e^{i pi/3}: G = (z - w)/(z - conj w).
- Racket check: the three axis labels z, 1/(1-z), 1-1/z sit at the same radius, exactly 120 deg apart, with identical volume (0.9832288623). The axis switches; the volume stays.
- Vacuum and rim: the regular tetrahedron (D = 1.014942, the maximum) is exactly the centre G = 0; flat tetrahedra are the rim.
- Per piece (2777 tetrahedra, 243 knots with 4-10 crossings): distance from the vacuum point vs volume, rho -0.998.
- The vacuum well (numerical, matches to 4 digits; derivation pending): near the centre D = V0 - (3 sqrt3/4)|G|^2 + (3-fold term). Measured (V0-D)/|G|^2 = 1.2990 vs 3 sqrt3/4 = 1.29904.
- Knot level, no fitting: Vol ~ sum over pieces [V0 - (3 sqrt3/4)|G|^2]. Median error 0.27%, 90th percentile 0.96%, worst 13% (10_1). Counting pieces at full volume alone: 10.9%.
- Reading: a knot's volume is its pieces at full volume, minus a squared penalty for how far each sits from the vacuum. Real knots keep most pieces near the vacuum (1391 of 2777 within distance 0.5).
- What is recognised: volume = sum of Bloch-Wigner D(z) is standard (Thurston, Milnor). The disk centred on the regular tetrahedron, the racket rotations and the well law are this session's reading; check prior art on expansions about the regular ideal tetrahedron.
- The turn half (Chern-Simons): the summed 3-fold angle of G gives nothing (rho 0.02). Expected: CS is not a sum of local shape terms; it needs the branch/winding data of log z (flattenings, Neumann's extended Bloch group). The turn book should live in those winding integers. Next.
