# Atlas card set: where it lives, every card, and today's six results mapped onto it

Prepared 2026-11-12 for Jeromie Beasley. Nothing from the repos or Drive was run; only text was extracted. Drive read-only, no web, no agents. Companion files in this folder: CARD_INDEX.md (one line for every card), CARDS_FULL_MATCHED.md (171 cards in full: every card whose text contains a requested term, plus the named ones), cards_v4.json and cards_W.json (extracted text), matched_keywords.json (which card hit which term).

# JOB 1: THE FULL CARD SET AND WHERE EACH VERSION LIVES

## The latest and complete set: continuous edition v4 / card set v7, B1 to B207
- Drive file "operator_first_atlas_continuous_v4 (1).html", id 1gYiS0FTilWj_pLgj0Ol7wTnox_q23Hwm, 3,101,901 bytes, folder 1pKLkygVcPhJWy7jId7aNV6zUgdUCcqTG, 2026-10-25.
- On disk: /home/claude/in/VOTKP_Full_Table_Research_20261111/VOTKP_Full_Table_Research_20261111/research/atlas_continuous_v4.html. Its md5 (08954c4d723300e31de0e63384576158) equals the md5 recorded for operator_first_atlas_continuous_v4.html in relational-atlas-lean/atlas/coverage/coverage.json (Zenodo record 10.5281/zenodo.23590925, concept 10.5281/zenodo.23590924, title "Continuous edition v4 · card set v7 (B1-B207)").
- It holds all 207 cards as `<article class="card" id="B1">` to `id="B207"`. Every number 1 to 207 is present (B91-B93 included). Grade tally from the cards: theorem 149, measured 34, derived 6, conjecture 10, reading 8 (matches the Zenodo description). Card titles equal the titles in coverage.json.
- Same file also carries extension notes under cards (not separate B numbers): I01-I08, X01, X02, X04, X05, X06, X08.
- Companions of the same release on Drive (folder 1pKLkygVcPhJWy7jId7aNV6zUgdUCcqTG): atlas_cards_v7_html (1).zip (one HTML per bridge), atlas_cards_v7_png_part1-4, atlas_new_cards_B183-B207_v7 (1).zip, The_Operator_First_Atlas_v7 (1).pdf (and part1/part2), atlas_paper_inventory_v2.xlsx; earlier continuous v1, v2, v3 and cards v3, v5, v6 zips (all 2026-10-21 to 25). Not downloaded; v4 already contains every card.
- Per-card text files B97.txt to B207.txt: /home/claude/in/VOTKP_Full_Table_Research_20261111/.../research/atlas_cards/.
- Earlier reads of this set exist in the repo: votkp-lean branch claude/sm-ball-20261111, research/2026-11-11-standard-model-ball/atlas/ATLAS_B97_B207_READ_20261111_v1.md (a coverage table for B97-B207).

## Earlier, partial versions
- Card edition 2026-09-07 / public edition 2026-10-14: B1-B90 and B94-B96 only (93 cards; B91-B93 absent from that edition). Files: /home/claude/repos/relational-atlas-lean/atlas/cards/html/B*.html, png/, manifest.json, README.md; same cards in operator-first under tools/compound-eye/preserved/original_modular_release/preserved/atlas-cards/cards/. The v4 text for B91-B93 and B97+ is not in these.
- The one-volume Atlas, 27 Aug 2026 (B1-B84, plates I-XXI): text at operator-first branch claude/gallant-bardeen-0pgpae research/acc/atlas_drive/THE_OPERATOR_FIRST_ATLAS_20260827.txt (per the audit file relational-atlas-lean/atlas/ATLAS_VERSION_AUDIT_2026-10-14.md; that branch is not cloned here); Drive THE_OPERATOR_FIRST_ATLAS.pdf (2026-10-11) and reading texts under /home/claude/check_v29/pkg/.../atlas_cauchy_reading/.
- Drafts: Drive VOTKP_Atlas_Drafts_B97-B108.pdf and IQGT_Atlas_Drafts_B109-B120.html (2026-10-14).
- The repository "reusable-results" atlas (operator-first atlas/cards.json, 18 cards on main) is a different object (ALG-, UPG-, DIO- ids), not the B series.

## Cards after B207
- B208-B213: two sources. (a) Drive "2026-10-26 Atlas new cards B208-B213 - README v1.md" (hero line, route, grade of each; card bodies are in atlas-source_v8draft_2026-10-26.zip sent in chat, not on Drive, not found). (b) The rebuilt versions in "Atlas Cards in 3D.html" (/home/claude/nov/knots/raw/, Drive id 1D7rZ3b4U_g--UcIg_7E-1_56Dd343_u6, 30 Oct), extracted in /home/claude/nov/knots/atlas_cards_B204_B213.json. The 3D record says these were rebuilt from the papers, keeping number, route, grade and hero line.
- B204-B207: the v7 bodies are in atlas_continuous_v4.html (used here). The 3D record says they were "not readable from Drive", so the 3D page rebuilt them; hero lines, routes and grades agree with v4. Wording of equations and witnesses differs (for example B207 uses lambda in v4 and r in the 3D rebuild).
- B214, B215, B216 (L2 to L0 theorem; L0 to L5 reading; L1 to L5 theorem): named only in the Drive record "2026-10-30 The Weight Between - music video v2 and atlas cards B214-B216" (a "map: stretch, hold, s = -1 flip", "two clocks", "same face"). Bodies are in Atlas_Cards_3D_B204-B216_v2.html sent in chat; not on Drive. NOT FOUND.

## Second set W1-W9, "Atlas II: Past the Wall"
- Drive "Atlas_II_Past_the_Wall_ed1_2026-11-03.html", id 1YMHuQziMZCaRsU3BaJFEvz_aXhg5l7y1, 47,860 bytes, 3 Nov 2026 (edition I, 3 theorem, 4 measured, 2 reading). Read through the Drive text reader and saved as /home/claude/closure/atlas/atlasII_ed1.html (markdown escapes removed), parsed to cards_W.json. All nine cards present. No other edition found.

## Other card sets that are not B or W
- P1-P4 "When the Neutrinos Leave" cards: /home/claude/repos/neutrinos-leave-lean/cards/ (videos, README, source). W5 cites P1.
- Connections records: Drive docs "Atlas v7 connections record" rounds 1-6 (2-3 Nov), and a 99-connection final record (C1-C99).

## Which is the latest
Complete text for B1-B207: continuous v4 (25 Oct). Newest cards: B208-B213 (26-30 Oct, README plus 3D rebuild), B214-B216 (30 Oct, bodies not found). Atlas II W1-W9 (3 Nov) is the newest set.

# JOB 2: EVERY CARD

CARD_INDEX.md lists all 222 cards (B1-B213, W1-W9) with route, grade and the card's own one-line statement, and B214-B216 as not found. The keyword scan (full text of every card; terms: Smith, tanh, rapidity, Cayley, ratio, wall, rim, 1/sqrt2, 2 sqrt2, loop, commutator, Thomas, Petermann, Jordan, exceptional point, Koide, Schottky, Garrett or ratio-5, light/radiation pressure, radiation, speed limit, Kakeya, direction, memory kernel, weight between, exit line) hit 171 cards, which are all given in full in CARDS_FULL_MATCHED.md (each headed by the terms that hit). The named cards are given in full below.

Term hits across B1-B207 + B208-B213 + W (card lists, from matched_keywords.json):
- Smith: B63, B97, B98, B102, B175, B189, B198, W1.
- tanh / artanh: B30, B40, B97, B98, B151, B153, B165, B166, B176, B189, B198, B203, B204, B207.
- rapidity: B98, B151, B153, B176, B189, B198, B204.
- Cayley (coordinate): B97, B99, B102, B104, B161, B175, B191, B199, B208, W5.
- rim: W1, W2, W3, W4, W5 only (no B card uses the word).
- Petermann: B73 only. Koide: B191, B197, B199, B200. radiation: B14 only. memory kernel: B161, B209. weight between: B210, B211.
- Jordan / exceptional point: B13, B26, B35, B36, B41, B44, B73, B121, B122, B145, B167, B171, B173, B177, B178, B179, B196, B199 (and more, see file).
- loop / commutator: B9, B13, B67, B128, B137, B159, B178, B187, B193, B194, B201 and others.
- NO card contains: Thomas, Schottky, Garrett or ratio-5 tree, light pressure, speed limit (as a phrase; B211 is the offset speed limit by content), Kakeya (B16 "A direction costs one channel" and B133, B103 carry the directional-capacity idea in the census language), exit line, 1/sqrt 2, a Poincare-radius or centre of a turn.
- "wall" (L3 stratum and many others): 62 cards, all in the file. "direction": 64 cards, all in the file.


# JOB 2 (continued): THE NAMED CARDS IN FULL

Text as extracted from the source file (figure text omitted). B204 is given as it stands in the v7 continuous edition; the rebuilt 3D version of B204 is in /home/claude/nov/knots/EXTRACT_cards.md.


## B97 | L7 → L6 | theorem
 A threshold ratio is a Smith coordinate.
 Γ = (I′ − I)/(I′ + I) = tanh(τ/2)
τ = ln(I′/I) · I′/I = (1 + Γ)/(1 − Γ)
an exact, reversible change of variables
 Move a pair of positive ionization thresholds into the same Cayley coordinate used for impedance mismatch. The coordinate is reversible: it retains the ratio, while a separate anchor retains the energy scale. Its value is a reusable interface between an atomic ladder and a familiar geometric chart.
 1CarryTwo ordered thresholds I, I′ with their units, charge labels and source grades.
 2CheckBoth thresholds positive. Γ may be negative; reciprocal ratios give opposite Γ.
 3ArriveA point on the real Smith diameter that composes with every other rung.
 Closed whenA point on the chart is not a measured electromagnetic reflection coefficient.
 LinksfeedsB98The atom and the film share an addition law.feedsB102Ratios need an anchor to recover binding.contrastsB63A rescaling can only be seen as a running.
 Linked fromsame form asB175A boundary that returns nothing is a matched load; the horizon is one.same form asB189One scalar edge is one reflecting step.same form asB198At a good prime the Frobenius edge keeps ap² and erases its sign; the twist count keeps it.
 Why it holdsPut r = I′/I = eτ. Then Γ = (r − 1)/(r + 1) = (eτ − 1)/(eτ + 1) = tanh(τ/2), and solving back gives r = (1 + Γ)/(1 − Γ). The map is one-to-one, so nothing in the ratio is lost; the absolute scale was never in it.
 Witnessr = 2 → Γ = ⅓; r = ½ → Γ = −⅓; r = 4 → Γ = 0.6.
 ReferenceVOTKP v2.9 · §8.1, Theorem 8.1 · elementary algebra


## B109 | L1 → L0 | theorem
 The moving subspace has a Fisher speed.
 ρ = P/k · L = 2Ṗ · FQ = 4g/k
g = ½ Tr(Ṗ²) · Bures speed² = g/k
normalization sets the rank factor
 Normalize the rank-k projector into a density operator. The tangent identity supplies its symmetric logarithmic derivative, and the Fisher information becomes the Grassmannian speed with the correct rank factor. Moving the subspace can therefore be read as distinguishability without identifying distinguishability with dissipated work.
 1CarryRank k, orthogonal projector P, tangent Ṗ, normalization, the metric convention, physical time when used.
 2CheckP² = P = P†, fixed finite k, differentiable motion.
 3ArriveThe quantum Fisher information of the moving subspace, FQ = 4g/k.
 Closed whenThe state stays uniform on its support, so its entropy stays ln k; a bath is needed to assign a cost.
 Linksbuilds onB22Leakage out of a channel is the capacity.extendsB28It does not need pure states.feedsB111The bath reads a response at its own rate.
 Linked frombuilt on byB112The kernel decides whether the SLD exists.built on byB180Fisher information is eight times the shape kinetic energy.pairs withB129Which-path knowledge and visibility are two entries of one Gram.pairs withB27Turning costs, and the geometry says how much.
 Why it holdsFor ρ = P/k, the SLD equation ρ̇ = ½(Lρ + ρL) is solved by L = 2Ṗ, because ṖP + PṖ = Ṗ on the tangent space. Then FQ = Tr(ρL²) = (4/k) Tr(PṖ²) = (4/k)·½ Tr(Ṗ²) = 4g/k.
 WitnessAt subspace speed g = 1: FQ = 4, 2, 1.33, 1, 0.8, 0.67 for rank 1 to 6.
 ReferenceIQGT v7.3.1 · §5.1, Lemma 5.1 · Lean: sld_two_tangent, two_trace_PVV


## B153 | L5 → L7 | theorem
 The offset is a rapidity: τ = 2 artanh a.
 τ = log(m/p) = 2 artanh a, a = (m − p)/(m + p)
|τL| → 2 artanh γ · γ = |v|/√(EminEmax) < 1 · Emin/max = √((t₁ ∓ t₂)² + v²)
an asymmetry between two positive numbers, added like velocities
 For an odd interval the offset reduces to the log-ratio of one positive boundary prediction error and its reflected partner. Any such ratio is 2 artanh of a normalized asymmetry a in (−1, 1), so offsets compose like rapidities. In the gapped Rice–Mele chain the asymmetry tends to γ = |v|/√(EminEmax), which is always below one, and the offset to the finite value 2 artanh γ.
 1CarryTwo positive numbers p, m (the boundary errors for v and −v); for the limit, a connected gapped Rice–Mele chain.
 2Checkp, m > 0; Emin > 0 with a nonzero hopping, so (EminEmax)² − v⁴ = (t₁² − t₂²)² + 2v²(t₁² + t₂²) > 0.
 3ArriveA bounded offset whose limit is fixed by the band edges alone.
 Closed whenThe endpoint is a large-size limit, not a finite-L identity; the sign alternates with (−1)n and is a separate statement from the magnitude.
 Linkssame form asB98The atom and the film share an addition law.builds onB151The offset is the log-odds of empty against full.
 Linked frompairs withB176The outside half of a Hawking pair is thermal and blind to the pair; its offset is ω/TH.same form asB198At a good prime the Frobenius edge keeps ap² and erases its sign; the twist count keeps it.pairs withB204The boundary sets the sign of the offset: it flips when the two residuals trade places.
 Why it holdsWith d = (m + p)/2 and a = (m − p)/(m + p), m = d(1 + a), p = d(1 − a), so log(m/p) = log((1 + a)/(1 − a)) = 2 artanh a; since m + p > |m − p|, |a| < 1. The odd-block offset is τ = log m − log p by an exact Schur reduction; the limit |a| → γ comes from a determinant transfer and an equal-hopping Hankel asymptotic (Szegő-type), and continuity of artanh on (−1, 1) carries it to τ.
 WitnessReference point (0.6, 1, 0.4): γ = 0.414123876567, 2 artanh γ = 0.881157076037. The 17-site interval gives τ = 0.881157076037163155, below the endpoint by 6.6e-15; the odd-L errors fall geometrically, with signs +−+−+−+−+.
 ReferenceOffset v31 · Offset v31 Theorems 9, 11, Proposition 10, Eq. (89) · 40-digit covariance; identity symbolic


## B175 | L3 → L7 | theorem
 A boundary that returns nothing is a matched load; the horizon is one.
 I − Sb*Sb = 4(WVb)* Herm L (WVb)
Zb = Lbb − LbiLii⁻¹Lib = W*LW · Sb = (Zb − I)(Zb + I)⁻¹
the power not returned is interior dissipation, pulled back
 Eliminate the interior of any passive operator and the boundary impedance inherits passivity, with no normality assumed. Its Cayley map is a contraction, and the deficit is exactly the interior’s dissipation pulled back to the boundary. Zero reflection is the matched load Zb = I. The membrane horizon carries a surface resistivity equal to the impedance of empty space, so in this calculus it returns nothing.
 1CarryA passive L (Herm L ⪰ 0) split into boundary and interior blocks, and a reference impedance to normalise by.
 2CheckLii and Zb + I invertible. For the horizon: the membrane description, RH = 4π/c with BH = EH × n.
 3Arrive‖Sb‖ ≤ 1, with Sb = 0 exactly at the matched load.
 Closed whenNo reflection is not full absorption, and an impedance says nothing about causality; the horizon reading is structural.
 Linkssame form asB97A threshold ratio is a Smith coordinate.builds onB48The seam is a Schur complement.pairs withB101The thin end is a shunt with a reference plane.contrastsB182Delay is not trapping: a slow return and no return differ only in the limit.
 Linked frompairs withB179A horizon’s static base and the coplanar wall share one fold normal form; only κ differs.fed byB90The clock exponent says whether a system is open.same form asB189One scalar edge is one reflecting step.contrastsB207The doubled Schwarzschild slice reads as the two books of one scalar edge.
 Why it holdsPut W = (I; −Lii⁻¹Lib). The interior row of LW vanishes, so LW = (Zb; 0) and W*LW = Zb, hence Herm Zb = W*(Herm L)W ⪰ 0. Then (Z + I)*(Z + I) − (Z − I)*(Z − I) = 2(Z + Z*); multiplying on both sides by V = (Z + I)⁻¹ gives I − S*S = 4V*(Herm Z)V = 4(WV)*(Herm L)(WV).
 WitnessOn 200 random passive samples the identity holds to 6e-15, with largest ‖Sb‖ = 0.950. The membrane value 4π/c converts to 376.7303 Ω = μ₀c; normalised, Zb = 1 gives Sb = 0, while Zb = ½ and 2 give Sb = ∓⅓.
 ReferenceBlack Hole v8.4 · §4.2, Proposition 13 · membrane resistivity from Damour; Thorne, Price and Macdonald · BH-SPINE-09, BH-MATCHED-12


## B176 | L5 → L7 | theorem
 The outside half of a Hawking pair is thermal and blind to the pair; its offset is ω/TH.
 τ = log P(empty)/P(full) = ħω/kBTH
|ψ⟩ = Σ tanhⁿr/cosh r |n⟩|n⟩ · tanh r = e−ω/2TH · CHSH = 2√(1 + tanh²2r)
a complete record, blind to the phase that decides the future
 Trace the inside partner out of a Hawking pair and the outside mode is exactly thermal, whatever phase sits on the pair. The pair itself beats the CHSH bound at every frequency, so no locally carried record could reproduce it. For a fermion pair the outside record has an exact zero point: its log-odds of empty against full is ω/TH for every pair phase.
 1CarryOne Hawking mode of frequency ω at temperature TH, and the two-mode pair (bosonic, or the Dirac pair cos r|00⟩ + eiφ sin r|11⟩).
 2CheckA pure two-mode pair; for the offset, a fermion mode with 0 < C < 1.
 3ArriveA thermal one-mode record, CHSH > 2, and τ = ω/TH independent of φ.
 Closed whenThe offset fixes only the ratio ω/TH, never an absolute scale; a bosonic mode has no “full” state.
 Linkssame form asB108The same local record can lead to opposite futures.builds onB151The offset is the log-odds of empty against full.pairs withB153The offset is a rapidity: τ = 2 artanh a.
 Why it holdsEach |n⟩out is paired with its own |n⟩in, so tracing the partner removes every off-diagonal term and a phase einφ cancels in |cₙ|². The parity pseudospin operators obey the spin-½ algebra; the two largest singular values of their correlation matrix are 1 and tanh 2r, so the Horodecki maximum is 2√(1 + tanh²2r) > 2. For the Dirac pair the outside occupation is C = sin²r = e−ω/T/(1 + e−ω/T), so log[(1 − C)/C] = ω/TH.
 WitnessCHSH = 2.785688 at ω/TH = ½, 2.383254 at 2 and 2.000182 at 10. By partial trace of the Dirac pair, τ = ω/TH to 10⁻¹⁵ at ω/TH = 0.3, 1.7 and 5 for pair phases 0, π/3 and π.
 ReferenceBlack Hole v8.4 · §5, Proposition 14 and eq. (offset) · CHSH value from Chen et al. 2002 · BH-BELL-11, BH-OFFSET-15


## B184 | L2 → L6 | theorem
 The two books are the halves of one product: a fixed budget and a signed trace form.
 E⁻ + E⁺ = 2Σi deg(i)‖Di‖² = 2‖DA‖² · E⁻ − E⁺ = 2 Re Tr (DA)²
E⁻ = 2‖Herm(DA)‖², E⁺ = 2‖Skew(DA)‖² · normal and H² Hermitian ⇒ Di = 0 at every vertex with an edge
the transport only decides how a fixed amount is shared
 Put X = DA. Its Hermitian half is ½[D, A] and its skew half is ½{D, A}, so the connection energy and its opposite are twice the squared norms of the two halves. They add to a budget that does not depend on the transport at all. Their difference is the indefinite trace form Re Tr X², the same split as the gravity ledger’s positive and negative books, and its sign says which half wins.
 1CarryThe operator H = D + A of B183 on a fixed graph with a fixed field.
 2CheckUnitary edge blocks, so ‖DiAij‖ = ‖Di‖.
 3ArriveOne budget, one signed difference, and the corollary that H normal with H² Hermitian forces the field to vanish.
 Closed whenThe budget is an identity of a fixed field, not a conservation law: when the field itself changes, the budget changes with it.
 Linksbuilds onB183Non-normality has an opposite: the energy of the anti-parallel field.same form asB125The trace-log of the imported form-space operator starts with the Einstein term.pairs withB123Leave the orthogonal projectors and the overlap can exceed the rank.
 Linked frombuilt on byB186The sector flip is a quarter turn, and it swaps the two halves.built on byB201Along the relaxation flow both books fall, and the total drained is the departure from normality.
 Why it holdsX* = A*D = −AD, so Herm X = ½(DA − AD) and Skew X = ½(DA + AD). The two halves are orthogonal in the Frobenius inner product, so their squared norms add to ‖X‖², and ‖DA‖² = Σi,j‖DiAij‖² = Σ deg(i)‖Di‖². Re Tr X² = ‖Herm X‖² − ‖Skew X‖² for every square matrix. If both books are zero, the budget is zero.
 Witness300 random graphs: the budget holds to 9e-16 and the difference to 2e-16, each side computed separately from the full matrices. The trace form came out positive 158 times and negative 142 times: neither half is favoured.
 ReferenceConnection Energy v16 · §2 eqs. (budget), (diff); Gravity Ledger ed. 6 Proposition 15 · random graphs, full-matrix comparison


## B186 | L2 → L2 | theorem
 The sector flip is a quarter turn, and it swaps the two halves.
 ΓA = i UAU*, U = e−iπΓ/4 · Tr X² + Tr(ΓX)² = 2Tr B²
Γ² = I · A crosses the sectors (ΓAΓ = −A), B stays inside (ΓBΓ = B) · (ΓA)² = −A²
a change of frame followed by multiplication by i
 Let a sign Γ be +1 on one sector and −1 on the other. On coupling that crosses the sectors, multiplying by Γ exchanges the Hermitian and skew halves exactly, keeps the self-commutator as a matrix, and reverses the trace form. It is not a reflection: it is a unitary change of frame followed by a right-angle turn of the spectrum. What it cannot move is the coupling inside a sector, and 2Tr B² is exactly the shortfall.
 1CarryA grading Γ = Γ*, Γ² = I, and any square X split into its crossing part A and its inside part B.
 2CheckThe grading must anticommute with the crossing part of the whole family it is applied to.
 3ArriveAn exact exchange of the two books for crossing coupling, and an exact measure of what spoils it.
 Closed whenNo single sign need exist for a family: σz, σx and J have no common anticommuting sign.
 Linkssame form asB68Paired spectrum is where the integers come from.builds onB184The two books are the halves of one product: a fixed budget and a signed trace form.pairs withB172The cover keeps a sign the Gram observer cannot see.
 Why it holdsΓA anticommutes with Γ. U = e−iπΓ/4 acts as e∓iπ/4 on the two sectors, so UAU* multiplies the crossing blocks by e−iπ/2 and e+iπ/2, which is −iΓA; hence ΓA = iUAU*. Then Herm(ΓA) = Γ Skew A and Skew(ΓA) = Γ Herm A, and AA* stays inside the sectors so [ΓA, (ΓA)*] = [A, A*]. Tr(AB) = 0 because a crossing block times an inside block is crossing, hence traceless.
 WitnessRandom 4×4 with Γ = diag(1, 1, −1, −1): ΓA = iUAU*, (ΓA)² = −A², the swap of the halves, the equality of self-commutators and the defect identity all hold to 2e-15. The figure is that matrix: every eigenvalue of ΓA is i times one of A.
 ReferenceConnection Energy v16 · §2 “The sector flip”, eqs. (defect), (quarter) · random matrices


## B189 | L3 → L7 | theorem
 One scalar edge is one reflecting step.
 E⁻/E⁺ = Γ², Γ = (di − dj)/(di + dj) = tanh(½ ln di/dj)
E⁺ − E⁻ = 4didj · boost di ↦ eφdi, dj ↦ e−φdj: Γ ↦ (Γ + tanh φ)/(1 + Γ tanh φ)
the ratio of the two books is the squared reflection coefficient
 On a scalar edge the two books are (di − dj)² and (di + dj)². Their ratio is the square of the coefficient of a wave meeting a step between impedances di and dj, and their difference is the transmitted part of the flux balance. A matched edge has no connection energy; a positive semidefinite field can never have more connection energy than opposite on any edge.
 1CarryTwo positive end values, or two positive semidefinite blocks and a unitary transport.
 2CheckPositive values for the tanh form; positive semidefinite blocks for |Γ| ≤ 1.
 3ArriveThe Smith coordinate of the edge, its rapidity ln(di/dj), and composition by the velocity law.
 Closed whenExchanging the ends negates Γ and leaves both books unchanged: the books do not say which end is larger.
 Linkssame form asB97A threshold ratio is a Smith coordinate.same form asB175A boundary that returns nothing is a matched load; the horizon is one.extendsB98The atom and the film share an addition law.
 Linked frombuilt on byB198At a good prime the Frobenius edge keeps ap² and erases its sign; the twist count keeps it.built on byB203The book ratios fix the route; the signs fix the endpoint.same form asB207The doubled Schwarzschild slice reads as the two books of one scalar edge.
 Why it holds(di − dj)² + 4didj = (di + dj)². With s = di/(di + dj), Γ = 2s − 1 = tanh(½ log(s/(1 − s))). A boost multiplies the ratio di/dj by e2φ, so it adds 2φ to the rapidity and composes tanh by the addition law. For positive semidefinite blocks Tr(DiUDjU*) ≥ 0, so E⁻ ≤ E⁺.
 Witness2000 random edges: the ratio, the tanh form and the flux balance hold to 3e-14, and the boost law to 4e-16. 3000 random positive semidefinite 3×3 edges: E⁻ − E⁺ never exceeded 0e+00.
 ReferenceConnection Energy v16 · §4 eqs. (gamma), (boost), (passive) · random edges


## B200 | L3 → L7 | derived
 Koide’s relation is the balance of the centered books on one plane.
 Q = Σm/(Σ√m)² · h²/s² = 3Q − 1 · (E⁻W, E⁺W) = (2(1 − ρK), 2ρK) = (1, 1) at Q = ⅔
Z = h₁σz + h₂σx + sJ, Z² = (h² − s²)I · minimally passive shift: ζ = h/s, ζ² = 3Q − 1 · e₃ = √(memμmτ) free
a declared encoding fixes a cone and leaves one number free
 Write the square-root masses as a democratic part s and a spread h. Koide’s Q = ⅔ is exactly h = s: a null cone, a nonzero nilpotent Z, a damped oscillator at critical damping, and a pair of centered books (1, 1) on the plane of √m and (1, 1, 1). The measured pole masses sit on it within the τ-mass uncertainty. The balance fixes the cone, not the point: the cubic invariant e₃, the triangle’s C₃, stays free.
 1CarryThree positive masses, their square roots, and the declared encoding: one coherent positive phase, pole masses.
 2CheckUnequal roots, so the plane is two-dimensional; the weight reading needs coherent positive amplitudes.
 3ArriveKoide as equal books, as critical damping, and the one number a selection principle would still have to fix.
 Closed whenThis is a conditional reformulation, not a derivation: generator, shift, resource and objective are all assumptions. Full dephasing gives ρ = ⅓ for every triple, and running masses are a different object.
 Linksbuilds onB199One wall where the trace form vanishes: the spinning key, critical damping, the ISCO.pairs withB197The triangle’s first prime keeps the cubic record that both books erase.builds onB191A constant is invisible to the connection energy; the opposite records it.
 Why it holds|x|² = s² + h² and (Σx)² = 3s², so Q = (s² + h²)/3s². The weight of the democratic ray is ρK = 1/3Q. Compress P = ψψᵀ and R = eeᵀ to their plane and center by ½I: the books are ‖P − R‖² = 2(1 − ρ) and ‖(P − ½I) + (R − ½I)‖² = 2ρ, equal at ρ = ½. Shifting Z by hI makes its top Hermitian eigenvalue zero and gives [[0, 1], [−1, −2h/s]] up to rotation.
 Witnessme = 0.51099895069, mμ = 105.6583755, mτ = 1776.93 ± 0.09 MeV: Q = 0.6666644634, ρK = 0.5000016525, centered books (0.999997, 1.000003), ζ = 0.9999967. The τ error gives σQ = 5.08e-06, so Q sits 0.43 standard deviations from ⅔.
 ReferenceConnection Energy v16 · §10 eqs. (koideq), (koidebooks), (koideosc), (e3); Koide 1982–83, Foot, Brannen; PDG masses · exact algebra; measured masses


## B202 | L1 → L7 | theorem
 Both books are blind to which way an edge runs; the resolvent is not.
 E∓(Hᵀ) = E∓(H)
[Hᵀ, (Hᵀ)*] = −[H, H*]ᵀ · (Hᵀ)² − (Hᵀ)*² = (H² − H*²)ᵀ · L = [[−1, 0], [0.3, −2]]: |R₂₁(0.5i)| = 0.130158, |R₁₂| = 0
a one-way coupling and its reverse have the same two books
 Transposing an operator reverses the direction every coupling carries signal, and changes neither book: both self-commutator and opposite are transposed, so their norms are equal. The resolvent sees the difference at once: a one-way block transfers from site 1 to 2 and not back, and its transpose does the opposite. Direction is a record the books do not keep.
 1CarryAny square operator H, and for the contrast a frequency at which to read the resolvent.
 2CheckThe Frobenius norm is transpose-invariant.
 3ArriveA limit on what the books can say: nothing about which way an edge runs.
 Closed whenThe books are not a transfer measurement; reciprocity and its breaking are read from the resolvent or the response.
 LinkscontrastsB89Reciprocity breaks at first order; conductance can only see it at second.pairs withB65Two diagnostics, not two views.builds onB183Non-normality has an opposite: the energy of the anti-parallel field.
 Why it holds(Hᵀ)* = (H*)ᵀ, so [Hᵀ, (H*)ᵀ] = (H*H − HH*)ᵀ and (Hᵀ)² − ((H*)ᵀ)² = (H² − H*²)ᵀ. Transposition preserves the Frobenius norm. For lower triangular L the resolvent is lower triangular, so its (1, 2) entry is zero; Lᵀ is upper triangular.
 WitnessL and Lᵀ both have books (0.024525, 0.202500); |R₂₁| = 0.130158 at z = 0.5i for L, with |R₁₂| = 0, and the entries swap for Lᵀ. 100 random complex 5×5 matrices: books of H and Hᵀ agree to 10⁻¹⁰.
 ReferenceConnection Energy v16 · §11 eq. (transpose) · exact; random matrices


## B204 | L4 → L5 | theorem
 The boundary sets the sign of the offset: it flips when the two residuals trade places.
 eτB+x = eτB s₀/s₁ · protected interior: τB+x = log(s₀/s₁)
s₁ = Cxx − c*CB−1c, s₀ = 1 − Cxx − c*(I − CB)−1c · det CB = det(I − CB)
the numerator becomes the denominator
 Add one site to a block. The offset changes by the log of two Schur residuals of that site, the empty-side one over the full-side one. When the interior is protected, so its full and empty determinants are equal, the whole offset is that one ratio: the interior has no say, and the sign flips exactly when the two residuals trade places. In the Rice–Mele chain this happens every time the block grows by two sites.
 1CarryA Gaussian regional covariance C on a block B plus one site x, with coupling column c.
 2Check0 < C < I; for the reduced form, a protected interior, det CB = det(I − CB).
 3ArriveThe sign of the offset located at one boundary site.
 Closed whenWithout protection the interior offset τB carries over; the identity still holds but the sign is shared.
 Linksbuilds onB151The offset is the log-odds of empty against full.pairs withB153The offset is a rapidity: τ = 2 artanh a.same form asB48The seam is a Schur complement.
 Linked frombuilt on byB205Rice–Mele and Kitaev are opposite chains for the self-dual mode.
 Why it holdsThe Schur complement gives det CB+x = det CB · s₁ and det(I − CB+x) = det(I − CB) · s₀. τ is the log of the second over the first, so τB+x = τB + log(s₀/s₁). A protected interior has τB = 0.
 WitnessRice–Mele (0.6, 1, 0.2) on a 60-site ring at 50 digits: eτ matches eτBs₀/s₁ to 9e-40 for every block up to 15 sites. Every even block has τ below 10⁻³⁹, and the odd blocks give τ = -0.4787, +0.4800, -0.4801, +0.4801, … , alternating with each two sites.
 ReferenceConnection Energy v16 · §11 eq. (boundaryflip); Offset v31 Theorem 8 · 50-digit covariance


## W1 | L2 → L3 | theorem
The kept edge is the rim; every other edge is the centre.
Γ₀ = (d₀ − d₁)/(d₀ + d₁) = −1 · Γ_l = 0 for l ≥ 1
D = −σ(I − P₀): d₀ = 0, d_l = −σ · E⁻₀ = E⁺₀ = σ², E⁻_l = 0, E⁺_l = 4σ²
one reflecting step, then a matched line
Put the neutrino chain's erasure operator on the atlas's scalar edges. The edge between the kept moment and the first erased one has one end at zero, so its reflection coefficient is minus one: the rim, with equal books. Every edge deeper in the chain joins two equal ends: matched, no connection energy, all of its budget in the opposite book. σ and k cancel; the placement is the same at every rate.
[figure] 
CARRYThe chain operator L = −ikM − σ(I − P₀) read as H = D + A with D = −σ(I − P₀), and the edge rule of B189.
CHECKScalar edges; d₀ = 0 exactly (the kept sector is not erased).
ARRIVEThe chain on the Smith disc: one edge at the rim, the rest at the centre.
CLOSED WHEN A chain that erases the kept moment too (d₀ ≠ 0) moves the first edge off the rim; a non-unitary edge map leaves B189.
WHY IT HOLDS Γ = (d_i − d_j)/(d_i + d_j) with d₀ = 0 gives Γ₀ = −d₁/d₁ = −1; equal ends give Γ = 0. The books are (d_i ∓ d_j)².
WITNESS E14-RIM-CENTRE RD1: Γ = (−1, 0, 0, 0, 0) and (E⁻, E⁺)/σ² = (1, 1), (0, 4), (0, 4), … for σ = 10⁻³, 1, 10⁴ and k = 0.3, 2.5, 8, to 10⁻¹².
REFERENCE Connection Energy v16 §4 (B189) · When the Neutrinos Leave v3.1 §2 (the chain) · E14-RIM-CENTRE  ·  LINKS carried from B189, B175; pairs with W5
W1 · L2-L3 · ATLAS II, PAST THE WALL · Jeromie Beasley


## W2 | L5 → L3 | measured
The state leaves the rim at k(τ − τ₀) = 2.30614, every mode.
s = E⁻/(E⁻ + E⁺) felt by the state · s = ½ at k(τ_rim − τ₀) = 2.30614
s(e₀) = 4/5 · free streaming depends on k(τ − τ₀) only · 36 modes, spread 0.00000
a constant of the chain, read on the right clock
Read the two books through the state instead of the operator: the share the state feels starts at four fifths on the kept moment, above the rim, and falls as the chain fills. In free streaming the fall is one curve in k(τ − τ₀) for every mode, and it crosses the rim at one number. Read on the wrong clock, k·τ, the crossings scatter by thirty percent; the preregistered kill line caught that and the clock origin, not the physics, was the error.
[figure] 
CARRYThe state-felt books K₂ = ‖[L, L*]v‖², K₃ = ‖(L² − L*²)v‖² (σ² and k² cancel in the share), and the chain's start τ₀.
CHECKFree streaming (σ = 0 after τ₀) from v = e₀; the crossing found by interpolation in log τ.
ARRIVEOne universal crossing, x* = 2.30614, and the share curve s(k(τ − τ₀)).
CLOSED WHEN Under erasure the crossing moves (τ_rim = 1.69 … 7.81 across the nine histories); 2.30614 is not identified with any named constant (ln 10 = 2.30259 is 0.15 % away).
WHY IT HOLDS With σ = 0 the chain is da/dτ = −ikMa from e₀ at τ₀, so a(τ) is a function of k(τ − τ₀) alone and every state-built ratio shares its clock.
WITNESS E14B-RIM-ORIGIN: k·(τ_rim − τ₀) mean 2.30614, min 2.30614, max 2.30614 over 36 profile modes; k·τ_rim 2.33–3.21 (spread 0.315). E14 RD2 as preregistered: FAIL; corrected origin: universal.
REFERENCE E14-RIM-CENTRE, E14B-RIM-ORIGIN · preregistration file RD2  ·  LINKS builds on W1; contrasts B160 (one rate cannot set the seconds); feeds W3
W2 · L5-L3 · ATLAS II, PAST THE WALL · Jeromie Beasley


## W4 | L2 → L2 | theorem
Two players split the budget exactly in half; the full chain gives the rim almost nothing.
s_op = c₀² / (2c₀² + 4 Σ_{l≥1} c_l²) · s_op(L_max = 1) = ½
c_l = (l+1)/√((2l+1)(2l+3)) · s_op = 0.1923, 0.0696, 0.0340, 0.00557 at L_max = 2, 5, 10, 60
the ½ lives on the density–flux pair, not on the chain
Take the operator's own books, with no state in them. [M, D] lives on the single edge joining the kept moment to the first erased one; {M, D} lives on every edge. So the share of the budget in the connection energy is a pure number set by how many moments are kept, independent of k, σ and time. With density and flux alone it is exactly one half; with sixty moments it is half a percent. The about-half of the ledger and this half are different objects: one is a ratio of integrated histories, the other a ratio of operator norms.
[figure] 
CARRYThe chain couplings c_l and the erasure D = −σ(I − P₀).
CHECKFrobenius norms; D scalar on each moment.
ARRIVEThe operator share as a function of the truncation, and its exact value ½ at L_max = 1.
CLOSED WHEN Truncation-dependent by construction: an infinite chain sends s_op to zero; the physical content is the single edge, not the number.
WHY IT HOLDS ‖[M, D]‖² = 2c₀²σ² (one edge), ‖MD + DM‖² = 2σ²(c₀² + 4Σ_{l≥1}c_l²); E∓ = ½k²‖·‖² and the common factors cancel.
WITNESS E13-TWOCLOCK-TWOBOOKS TB1: 0.5, 0.1923, 0.06962, 0.03398, 0.005571 at L_max = 1, 2, 5, 10, 60.
REFERENCE Connection Energy v16 §2 (budget, B184) · E13 TB1  ·  LINKS builds on B184, B186; contrasts W2 (the state's share is not the operator's)
W4 · L2-L2 · ATLAS II, PAST THE WALL · Jeromie Beasley


## W6 | L5 → L5 | theorem
Every rung is a quarter turn from its neighbour, so the chain has no reactive book.
a_l(τ) = (−i)^l r_l(τ), r_l real · Re(a_l* a_{l+1}) ≡ 0
from a(τ₀) = e₀ and da/dτ = −(ikM + σ(I − P₀))a with M real symmetric tridiagonal
the phase locks; only the active part of the traffic exists
The chain's generator couples each moment to the next through ik times a real number and damps each moment by a real rate. Starting from a real density, every rung picks up exactly one factor of −i from the one below it and nothing else can turn it. So neighbouring moments are always a quarter turn apart and the real part of their product vanishes identically. The density–flux traffic has an active part and no reactive part: there is nothing stored and sloshing to book.
[figure] 
CARRYThe chain in the form above with real c_l and real σ(τ).
CHECKA real initial moment vector; no complex coupling anywhere in the generator.
ARRIVEExact phase locking and the vanishing of every Re(a_l* a_{l+1}).
CLOSED WHEN A complex initial condition or a complex damping breaks the lock; so does any non-tridiagonal coupling.
WHY IT HOLDS Write a_l = (−i)^l r_l; the equation for r_l has only real coefficients (the i from the coupling cancels the (−i) of the step), so r_l stays real.
WITNESS E10 X check and E15-CARDSDATA: max |Re(a_l* a_{l+1})| over all rungs and times for k = 4.81 is 0.00e+0; arg a_l / (π/2) = 0, 1, 0, −1, 0, … at τ = 3.
REFERENCE When the Neutrinos Leave v3.1 §2 · E10 (X_reactive), E15  ·  LINKS pairs with B186 (the sector flip is a quarter turn); feeds W4
W6 · L5-L5 · ATLAS II, PAST THE WALL · Jeromie Beasley


## W9 | L3 → L5 | reading
What survives a wall is the even half; the odd half is the orientation, and it lives only in the split of a pair.
even: volume, det g, fidelity, both books, route length, Tr Π_blk · odd: signature, Ω, sign det X, the resolvent, Bargmann, the signs along the route
B174, B71, B180, B202, B206, B203, B172, B35
six cards, one sentence
Across the black-hole paper, the connection-energy paper and the neutrino ledger the same split appears: readings even under the wall's involution survive it, readings odd under it sum to zero there. The books, the metric determinant, fidelity and the contour count are even; the signature, the curvature's sign, the orientation on the cover, the direction an edge runs and the third-order Bargmann invariant are odd. The ledger's about-half is, on this reading, an even quantity read on one clock. The sentence is a map of the land; none of the four tests of this atlas proves the link between the two halves.
[figure] 
CARRYA wall with an involution (mirror, sector flip, transpose, the cover's sheet exchange) and a reading of the state.
CHECKClassify the reading as even or odd under that involution before asking whether it survives.
ARRIVEA rule for which records cross and where the ones that do not can still be found.
CLOSED WHEN A reading, gathering theorems and measurements from the old atlas; the claim that the ledger's half is the even half of the two-book budget is untested (W2–W4 are the first steps toward it).
WHY IT HOLDS Each listed card proves its own even/odd statement on its own object; the reading is that the objects are instances of one involution.
WITNESS None beyond the cited cards; the only new numbers in this land are W1–W4.
REFERENCE Beyond the Event Horizon v10 §4.2, §6 · Connection Energy v16 §11 · the old atlas  ·  LINKS carried from B174, B71, B172, B180, B202, B203, B206, B35; feeds W5
W9 · L3-L5 · ATLAS II, PAST THE WALL · Jeromie Beasley


# JOB 3: TODAY'S SIX RESULTS ON THE CARDS

Rule used: "holds" means the card's own statement contains the result; "partly" means a card holds an ingredient or the same form for a special case; "not on a card" means no card statement, equation or witness contains it. Card formulas are quoted from the text above.

## Result 1. Loop of two perpendicular steps of ratio z: trace 2 - 4 sinh^4(r/2), r = ln z; turn for Gamma^2 < 1/2, one Jordan block at Gamma^2 = 1/2, a run beyond.
- The step and its coordinate: HELD WHOLLY. B97: "Gamma = (I' - I)/(I' + I) = tanh(tau/2), tau = ln(I'/I)". B189: "Gamma = (di - dj)/(di + dj) = tanh(1/2 ln di/dj)" with composition "Gamma -> (Gamma + tanh phi)/(1 + Gamma tanh phi)" along one line. B98: "u (+) v = (u + v)/(1 + uv)". B153: "tau = 2 artanh a".
- The three regimes turn / one Jordan block / run: HELD PARTLY, for a 2x2 generator. B199: "T^2 = q(T) I ... q = 0, T != 0 <=> a nonzero nilpotent"; positive q grows and decays, negative turns, zero with T != 0 is a Jordan block (real traceless 2x2). B122: Jordan block "grows before it decays exactly when kappa = |mu|/b > 2". B177: "oscillation outside, growth inside, a nilpotent at r = 6M".
- A loop of two steps at right angles built from steps of ratio z, its trace 2 - 4 sinh^4(r/2), and the threshold Gamma^2 = 1/2: NOT ON A CARD. The nearest loop cards use other loops: B13/B178 (loops around exceptional points: "(1/2pi) Delta arg (l1 - l2)^2 = +1 per loop"), B67 (a closed loop of shapes lifts to an open path, "the gap in SO(d)"), B128 (commutator of two unitaries "R = U V U+ V+, delta + g^2 <= 4"), B159 (loop ledgers). No card has "Thomas", "boost" beyond the collinear law in B189, or a product of two perpendicular boosts.

## Result 2. Centre of turn at Poincare radius rho, rho^2 = (1-s)/(1+s), s = sqrt(1 - 2 Gamma^2); at z = 5 the point (3,2,2,0), radius 1/sqrt 2, distance ln(3 + 2 sqrt 2).
- NOT ON A CARD. Cards with a disc: B98 ("The real atomic walk carries a hyperbolic distance... a film map needs a conjugate in the denominator before it is a disk isometry"), B175 and W5 (the Smith disc for a boundary, "one disc holds the horizon's load and the neutrino boundary"), B190 (the duality disc P^2 + V^2 <= 1). None carries a fixed centre of a loop, a Poincare radius, the point (3,2,2,0), 1/sqrt 2 or ln(3 + 2 sqrt 2). Ingredient held: the hyperbolic length of a rung is the rapidity (B98, B189, B203: "Lrec = 2 Sum |rj| = 2 Sum artanh sqrt(E-j/E+j)").

## Result 3. Obliqueness (Petermann factor) of the loop K = 1/(1 - 2 Gamma^2) = cosh^2 of the centre's distance; K = 2 at z = 3.
- HELD PARTLY. B73: "<L|R> ~ gap => K ~ gap^-2" ("the Petermann factor diverges as the inverse square of the gap" at a square-root collision); B167/B26: "kappa sqrt(delta) -> const". Obliqueness as a notion: B57 ("Pi^2 = Pi, Pi != Pi+"), B123, B124 (oblique rank-one idempotents). The closed form K = 1/(1 - 2 Gamma^2), its link to the distance cosh^2, and the value 2 at z = 3: NOT ON A CARD.

## Result 4. Two-level signal c = [1 + sin(n theta) sin(phi)]/2 driven by the loop; Gamma = 1 - 2c; bound (dGamma/dt)^2 <= 4 g (1 - Gamma^2).
- The bound: HELD (as the scalar-cut case). B211: "P = [[C, B],[B+, D]], tau = Tr[log(I - C) - log C], g = 1/2 ||P-dot||^2, S = Tr[(C(I - C))^-1], tau-dot^2 <= 4 g S", with "scalar cut: 4gS - tau-dot^2 = 4(Im b-bar b-dot)^2/(c(1 - c))^2, b = P12". With c a 1x1 block, tau = 2 artanh(1 - 2c) (B153: "tau = 2 artanh a"; B151: offset = log P(empty)/P(full)) and S = 1/(c(1 - c)) = 4/(1 - Gamma^2), which turns tau-dot^2 <= 4gS into (Gamma-dot)^2 <= 4 g (1 - Gamma^2). The substitution is the reader's step; B211 does not print the Gamma form. Equality "along the meridian of the Bloch sphere" is on the card; "moving around a latitude changes only a phase and leaves the record still".
- The particular signal c = [1 + sin(n theta) sin(phi)]/2 and its driving by the loop: NOT ON A CARD.
- Offset-as-record cards: B204 (sign flip), B176 (tau = omega/T_H).

## Result 5. One lossless layer with R = Gamma^2, T = 1 - R: wall is R = T; push P = 2R; K = 1/(1 - P).
- R = Gamma^2 and T = 1 - R: HELD. B189: "E-/E+ = Gamma^2" ("the ratio of the two books is the squared reflection coefficient"; "E+ - E- = 4 di dj", "the transmitted part of the flux balance", so (E+ - E-)/E+ = 1 - Gamma^2). B175: "I - Sb*Sb = 4(W Vb)* Herm L (W Vb)", "Sb = (Zb - I)(Zb + I)^-1", matched load Sb = 0.
- A wall at R = T (Gamma^2 = 1/2): NOT ON A CARD. The cards' walls: B199, "one wall where the trace form vanishes" (equal books, q = 0, T != 0 nilpotent); B200 centred books (1, 1); W1 "the kept edge is the rim; ... Gamma0 = -1 ... equal books". On the scalar edge of B189, equal books mean Gamma^2 = 1 (the rim), not Gamma^2 = 1/2. B199 also says "Equal books on a graph are not the wall".
- Push P = 2R and K = 1/(1 - P): NOT ON A CARD. (B190 has a different "P", predictability, with "P^2 + V^2 + L^2 = 1".) No card has light pressure or radiation pressure; B14's only "radiation" is the photon gas entropy.

## Result 6. Exit line <K> = 1 + u^2/(E(0)E(pi)) = 2 of the gain-and-loss chain.
- NOT ON A CARD. No card has an exit line, an average K, or a gain-and-loss chain. Nearest on cards: W1/W6 (the erasure chain, one rim edge then matched edges, "a_l(tau) = (-i)^l r_l"), B195/B196 (chains and zeta), B201 (relaxation flow). The "gain" word appears only in B72 and B201 in unrelated senses.

# END OF REPORT

## Cards read in full (every line printed and read, this session)
B13, B35, B36, B63, B66, B73, B78, B92, B97, B98, B99, B102, B109, B122, B137, B151, B153, B159, B160, B161, B167, B171, B172, B173, B175, B176, B177, B178, B179, B183, B184, B185, B186, B187, B188, B189, B190, B191, B193, B194, B195, B196, B199, B200, B201, B202, B203, B204, B205, B206, B207 and B208-B211 (B205, B206, B208-B211 from /home/claude/nov/knots/EXTRACT_cards.md), W1-W9. B212 and B213 read only as far as their hero line, equation band and the start of the json entry plus the README summary (not the Why/Witness lines).
Read in compact form (headline, equation band, prose, closed-when, links; "how to cross", why-it-holds, witness and reference lines not read): B2, B3, B5, B9, B14, B15, B16, B17, B19, B22, B26, B27, B30, B31, B34, B39, B40, B41, B42, B44, B46, B54, B55, B57, B67, B68, B72, B74, B79, B81, B82, B84, B87, B89, B94, B96, B101, B103, B104, B110, B111, B112, B116, B117, B121, B123, B124, B127, B128, B129, B130, B131, B132, B133, B143, B144, B145, B148, B150, B155, B156, B165, B166, B168, B170, B174, B180, B181, B192, B197, B198.
Index line only (title, route, grade): every other card in CARD_INDEX.md (about 100 cards, including B1, B4, B6-B8, B10-B12, B18, B20-B21, B23-B25, B28-B29, B32-B33, B37-B38, B43, B45, B47-B53, B56, B58-B62, B64-B65, B69-B71, B75-B77, B80, B83, B85-B86, B88, B90-B91, B93, B95, B100, B105-B108, B113-B115, B118-B120, B125-B126, B134-B136, B138-B142, B146-B147, B149, B152, B154, B157-B158, B162-B164, B169, B182). The standing rule (every card read in full before a path is called new) is therefore NOT yet met for these; their full text is in cards_v4.json and, where a keyword hit, in CARDS_FULL_MATCHED.md.

## Cards not found
B214, B215, B216 (bodies); B208-B213 original markdown bodies (only the 3D rebuild and the README hero lines); the one-volume Atlas of 27 Aug as text on this machine (branch claude/gallant-bardeen-0pgpae not cloned); the chat-only files Atlas_Cards_3D_B204-B216_v2.html and atlas-source_v8draft_2026-10-26.zip.

## Which of results 1 to 5 are already on a card
1. Only the ingredients (Gamma = tanh(r/2) on B97/B189, the turn/Jordan/run split for a 2x2 generator on B199/B122); the loop trace, Gamma^2 = 1/2 and the loop itself are on no card.
2. On no card; 3. only the divergence of the Petermann factor at a Jordan point (B73), not K = 1/(1 - 2 Gamma^2); 4. the bound is B211's scalar cut (with B153's tau = 2 artanh Gamma), the specific signal is on no card.
5. R = Gamma^2, T = 1 - R are on B189/B175; the wall R = T, the push P = 2R and K = 1/(1 - P) are on no card (result 6 is also on no card).
