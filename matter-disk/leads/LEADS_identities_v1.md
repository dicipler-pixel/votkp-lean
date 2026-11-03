# Leads v1: exact identities that join Jeromie Beasley's papers

Lead-finder output, 3 Nov 2026. Read-only on the corpus; nothing in his files was edited. Check scripts: `identity_checks_01.py`, `identity_checks_02.py` in this folder (numpy/scipy, a few seconds). All numbers below are from those runs.

Grades: **[A]** proven by algebra (I wrote the steps out; a script also agrees), **[N]** numerically checked only, **[C]** conjectured (the check is named but not passed or not run).

## Coverage, stated plainly

The corpus-notes folder is 1.35 MB. I read these in full: README, CLAIMS, `offset_speed_limit.md`, `offset_speed_limit_v1_1.md`, `cone.md`, `upg.md`, `twotrees.md`, `nonnormality.md`, `ladder.md`, and `weight_between.md` through section 3.5, `light.md` and `gravity.md` for their abstracts and the sections quoted below, and `bh.md` sections 4 and 5. The rest (`atlas_v7`, `votkp_v29`, `v21`, `iqgt`, `koide`, `neutrinos`, `matter_at_a_scale`, `dirac_gigantefermion`, `present_keeps`, `what_transport_keeps`, and the small ones) I searched by keyword but did not read line by line. Every lead below rests on his notes of the papers, not on the PDFs. Where an identity needs a paper equation I did not see, it is marked.

## The one dictionary behind most leads

Five of his papers carry the same two-number object under five names. For an edge with positive end values (d_i, d_j), ratio z = d_i/d_j = e^r:

| paper | name for it |
| :-- | :-- |
| VOTKP / Two Trees | peel step: Γ(z) = (z−1)/(z+1) = tanh(r/2), length r = ln z |
| Non-Normality (§4, eq. 15, 17) | scalar edge: Γ_e = (d_i−d_j)/(d_i+d_j); E₋/E₊ = Γ_e²; E₊−E₋ = 4 d_i d_j; duality P² + V² + L² = 1 with L = 0 |
| Rails paper (§1–3, 5) | the two rails (λ₊, λ₋), λ₊λ₋ = D |
| Offset Speed Limit (App. B) | balance map (m−p)/(m+p) = tanh(½ ln m/p); census 1−2ν = tanh(τ_ν/2) |
| Light / Black Hole | Schur–Cayley S_b = (Z_b−1)(Z_b+1)⁻¹; Smith reflection (z−1)/(z+1) |

The leads below are mostly consequences of one reading: put the paper's own two numbers into the Non-Normality edge.

---

## L1. The Petermann factor is a ratio of Non-Normality's Hermitian and skew halves **[A][N]**

**(a) Sides.**
- Matter-disk §6 and Light §8.5: K = ½(1 + |d|²/|E|²) for h = d·σ, E² = d·d. In SSH: K = 1 + u²/E² (matter-disk §5).
- Non-Normality §9, eq. (35)–(36): q(T) = ½Tr T² = ½(‖Herm T‖² − ‖Skew T‖²); "the wall" is q = 0 with T ≠ 0 (nilpotent); ‖[T,T*]‖² = 32 h²r².

**(b) Algebra.** Write d = a + ib with a·b = 0 (this is exactly "E² real", the PT-unbroken class: SSH has a = (Re q, Im q, 0), b = (0, 0, u)). Then:
- ‖Herm h‖² = 2|a|², ‖Skew h‖² = 2|b|², q = |a|² − |b|² = E², ‖[h,h*]‖² = 32|a|²|b|².
- K = ½(1 + (|a|²+|b|²)/(|a|²−|b|²)) = |a|²/(|a|²−|b|²) = ‖Herm‖²/(‖Herm‖² − ‖Skew‖²).
- Put ρ := ‖Skew‖/‖Herm‖. Then K = 1/(1 − ρ²), and ρ² = cos²φ, where φ is the angle between the two eigenvectors (for two levels K = 1/sin²φ, because |L₊| = 1/sin φ when |R| = 1).
- At the wall q = 0: ρ = 1, φ = 0, K = ∞. The exceptional point is his "wall".

**(c) Check.** 2000 random real-E d: three forms of K agree to 7e−14; ρ² = cos²φ to 1e−15; q = |a|²−|b|² to 4e−15; ‖[h,h*]‖² = 32|a|²|b|² to 1e−12. Done in `identity_checks_01.py`.

**(d) Borrow.**
- Matter-disk gets a name and a Lean-checked source for "band-averaged K": K is the Hermitian share over the trace form. Non-Normality's wall theorem is the K → ∞ limit.
- The exit law ⟨K⟩ = 2 reads: on average the skew half carries ρ² = ½ of the Hermitian half's energy. See L3 for why this number is the Schottky line.
- Non-Normality gets a physical measurement of ρ: it is the Petermann factor, which is measurable (laser linewidth excess).
- Caveat: this uses h itself split into Herm/Skew; Non-Normality's E₋, E₊ are halves of the product DA. Two different splittings. For the SSH-type h, iH = D + A with D = −uσ_z and A = i·offdiag, scalar edge weight w = |q|², so E₊ = 0 (H² is scalar, "mirror/anti-parallel") and E₋ per k = 4|q|²u². That is the Non-Normality "scalar shore" (§6) in one k-sector, and it is a clean second reading of the same K.

---

## L2. The rails paper's two rails are a Non-Normality scalar edge; the discriminant T²−4D is the connection energy **[A][N]**

**(a) Sides.**
- Rails §1–3: transfer trace T, det D, rails λ± with λ₊λ₋ = D; for D = 1, T = 2 sec ψ, λ± = sec ψ ± tan ψ; band edge |T| = 2 is "an exceptional point"; log λ₊ = gd⁻¹(ψ). Table 1 and Prop. 4: ũ = tan(ψ/2).
- Non-Normality §4 eq. (15), (17): edge (d_i, d_j): E₋ = (d_i−d_j)², E₊ = (d_i+d_j)², E₊−E₋ = 4d_id_j.

**(b) Algebra.** Take (d_i, d_j) = (λ₊, λ₋):
- E₊ = (λ₊+λ₋)² = T², E₋ = (λ₊−λ₋)² = T² − 4D (the discriminant), E₊ − E₋ = 4D (the "transmitted flux" is the determinant).
- Band edge T² = 4D ⇔ E₋ = 0 ⇔ matched edge (his sentence in §4: "a matched edge has no connection energy"). Elliptic band |T| < 2 ⇔ E₋ < 0 (complex end values).
- D = 1: Γ_e = (λ₊−λ₋)/(λ₊+λ₋) = tanh(log λ₊) = sin ψ, so E₋/E₊ = sin²ψ = 1/K_rails (see L3 for why this edge, with ends the two rails, is the natural peel step).
- Petermann factor of the companion matrix [[T, −D],[1, 0]]: K = (T² + (D−1)²)/(T² − 4D) (his eq. (1) algebra, rails §1), so at D = 1, K = E₊/E₋ = csc²ψ.
- Second edge, ends (λ₊, 1): Γ_e = tanh(r/2) = tan(ψ/2) = ũ, so the Rice–Mele modulus ũ is the Non-Normality reflection coefficient of the edge (λ₊, 1), and 1/ξ = 2 artanh ũ = ln λ₊ = ln(d_i/d_j) is the offset τ of that edge.

**(c) Check.** T = 2.2, 2√2, 4, 34: E₋ = T²−4, E₊ = T², K = E₊/E₋ = csc²ψ, E₋/E₊ = sin²ψ, Γ(λ₊) = tan(ψ/2), tanh(ln λ₊) = sin ψ, all to 1e−13 (the T = 34 rows lose digits to cancellation only). `identity_checks_01.py`.

**(d) Borrow.**
- The rails paper's regime table (band, gap, edge) is the sign of the Non-Normality connection energy. Its open item 1 (why T = 34 twice) can be asked as: which edge has E₊ = 34², E₋ = 34² − 4 = 1152 (that is the printed 1152 in Table 1)? See L4.
- Non-Normality's budget E₋ + E₊ = 2(λ₊² + λ₋²) = 2(T² − 2D) gives the rails paper a conserved quantity for free.
- Rails' "ψ is not Φ" (open item 2) has a place to live: ψ is the edge angle; Φ is a product over edges.

---

## L3. One number, five faces: Γ² = ½ (Schottky) = ⟨K⟩ = 2 (exit) = ψ = 45° = cosh τ = 3 = census λ = ⅛ **[A][N]**

**(a) Sides.**
- Two Trees Thm 5.3: Schottky group iff z > 3 + 2√2 iff Γ² > ½; Γ(3+2√2) = 1/√2; commutator trace −2 there (sinh(r/2) = 1); cosh d(O,p) = 3 at ratio 5.
- Matter-disk §5, §6 and CLAIMS: exit when band-average Petermann factor is 2.
- Rails Table 1: π+e sits at ψ = 45° exactly.
- Census / Offset Speed Limit: 1 − Γ² = 4ν(1−ν) = 4λ, where λ is the X_A eigenvalue (matter-disk §7).

**(b) Algebra.** Let the step be the ratio of the two rails (the natural peel step for a rail pair): z = λ₊/λ₋ = λ₊². Then by L2:
- Γ(z) = sin ψ, and K = 1/sin²ψ = 1/Γ(z)². So K = 2 ⇔ Γ(z)² = ½ ⇔ z = 3+2√2 ⇔ ψ = 45°.
- Same Γ as a census level: Γ = tanh(τ/2) with τ = ln z: cosh τ = (1+Γ²)/(1−Γ²) = 3, i.e. cosh²(τ/2) = 2; occupation ν = (1−1/√2)/2 = sin²(π/8) = 0.14645; 4λ = 1 − Γ² = ½, λ = ⅛ (half the maximum ¼).
- τ = 2 ln(1+√2) = arccosh 3 = 1.76275 = Two Trees' ρ = 1.7627471740.
- Per-level inverse census S_ν = 1/λ = 4cosh²(τ/2) = 4/(1−Γ²); at the line S_ν = 8.

**(c) Check.** ν = 0.146446609406726 = sin²(π/8) to 1e−16; cosh τ = 3.0000000; z = 5.828427; sech(ln z) = 1/3; λ = 0.125. `identity_checks_01.py`.

**(d) Borrow.**
- Matter-disk: the exit law has the same constant as the Schottky line, so Two Trees' proof (planes touch at infinity at equality, boundary circles of angular radius π/4) is the geometric picture of "K = 2": eigenvectors at 45°. Two Trees' v2 report gives cap radius α with cos α = Γ; here cos φ = ρ, the same role.
- Caution, stated once: the matter-disk exit is a statement about a band average ⟨K⟩, the Schottky line is a statement about one step. The per-k identity K(k) = 2 ⇔ Γ_k² = ½ is exact; whether ⟨K⟩ = 2 is also a Schottky statement for some ping-pong action is **[C]**.
- Fermion record (BH §7): Γ = tanh(ħω/2kT) = 1/√2 at ħω/kT = 2 ln(1+√2) = 1.7627. A thermal fermion mode at that temperature sits on the Schottky line. Gas §8 (ideal helium): the same value for the stage ratio n_q/n_{q+1}.

---

## L4. The same transcendental number 4 ln(1+√2) = 3.5254943481 appears in the rails paper and in Two Trees **[A][N]**

**(a) Sides.**
- Rails §3: Apéry rate log(17 + 12√2) = 3.52549434808; sec ψ = 17, tan ψ = 12√2; Catalan contains it (T = 34, Pell 17² − 2·12² = 1).
- Two Trees App. B (q1_orbit_accum, q1_commutator): d(O, cⁿO) ≤ 2ρ = 3.5254943481, with cosh ρ = 3 (cosh d(O,p) = 3), ρ = arccosh 3 = 1.7627471740.

**(b) Algebra.** cosh ρ = 3 ⇒ sinh ρ = 2√2, cosh 2ρ = 17, sinh 2ρ = 12√2. So λ₊ = e^{2ρ} = 17+12√2 = (1+√2)⁴ and the Apéry rate is exactly 2ρ, with ρ = r_c = 2 ln(1+√2) the Schottky rapidity of L3. The Pell pair (17, 12) is (cosh 2ρ, sinh 2ρ/√2). Likewise π+e: λ₊ = 1+√2, rate ln(1+√2) = ρ/2 (rails §3 prints 0.88137358702).

**(c) Check.** arccosh 3 = 1.762747174039086; 2 ln(1+√2) = 1.7627471740390859; Apéry rate 3.525494348078172 = 2ρ exactly; π+e rate 0.8813735870195429 = ρ/2; cosh 2ρ = 17.0, sinh 2ρ = 16.970562748 = 12√2. `identity_checks_01.py`.

**(d) Borrow and open.**
- Rails open item 1 ("why T = 34 twice") can be restated: both Ramanujan objects have rail rapidity at an even multiple of the Schottky rapidity (Apéry 2ρ, π+e ρ/2). The coincidence of the number is proved; that it explains T = 34 in two derivations is **[C]**.
- Two Trees' 3.5255 "never lands more than 3.5255 from the centre" is therefore also "the Apéry Lyapunov exponent". A test: the rails paper's three Ramanujan transfer matrices as Two Trees boosts: T = 2 cosh x (the meridian trace, Two Trees Thm 6.1), so Apéry is a boost of length 2x with x = 2ρ.
- To check next: do the other challenge transfer matrices (Questions 1–8, `challenge-calibration`) have T = 2 cosh(kρ/2) for integers k? Untested.

---

## L5. Thomas rotation tan(θ/2) = Γ² is the Non-Normality ratio E₋/E₊, and a quarter turn of its complexification is the disk exit **[A] for the first part, [A]+[C] for the second**

**(a) Sides.**
- Two Trees Thm 4.7 (Lean thomas_half_angle_t): two perpendicular peel steps of equal rapidity r = ln z leave a Thomas turn with tan(θ/2) = Γ², Γ = (z−1)/(z+1); z = 5: tan(θ/2) = 4/9, cos θ = 65/97; z = 7: 9/16, 175/337.
- Non-Normality eq. (15): E₋,e/E₊,e = Γ_e².
- Matter-disk §4: |Γ| < 1 iff |Im W| < π/2; exit at a quarter turn.

**(b) Algebra.** For the scalar edge with d_i/d_j = z: E₋/E₊ = ((z−1)/(z+1))² = Γ² = tan(θ/2). So the Thomas half-angle tangent is the ratio of the connection energy to its opposite on the edge whose ends are in the peel ratio. Consequences: cos θ = (E₊² − E₋²)/(E₊² + E₋²), sin θ = 2E₊E₋/(E₊² + E₋²). The Schottky condition Γ² = ½ is E₊ = 2E₋, i.e. E₊ − E₋ = E₋ i.e. 4d_id_j = (d_i−d_j)²: the Lorentz norm of the edge equals its connection energy, z + 1/z = 6.

For complex Γ define θ = 2 arctan(Γ²). If |Γ| = 1, Γ² has modulus 1 and Re arctan(Γ²) = ±π/4 exactly, so Re θ = π/2: a quarter turn. For |Γ| < 1, |Re θ| < π/2.

**(c) Check.** z = 5, 7, 3+2√2: tan(θ/2), Γ², E₋/E₊ agree to 1e−16. Complex: |Γ| = 1.0: Re θ/(π/2) = 1.0000000000000002; 0.9 gives 0.742, 1.1 gives 1.127 (principal branch; a branch jump appears at |Γ| = 1.5 and at 0.5 when Re Γ² < 0). `identity_checks_02.py`.

**(d) Borrow.**
- Matter-disk: "a quarter turn marks the exit line; a half turn marks the critical point" becomes a statement about a complexified Thomas angle. Two Trees' sentence "order matters only through a phase" (VOTKP §15.2) gets its angle for opened levels.
- The identification of θ_c with the physical phase of an opened level is **[C]**. A decisive test: for the opened SSH chain at the exit, compute the Thomas phase from two perpendicular steps built from the level's complex Γ with the complex boost matrices, and see whether it is π/2 + i·(something). Not run.
- Two Trees open item "Thomas phase around a knot relator loop untested" could use the opened-matter ladder as a second test bed.

---

## L6. The Offset Speed Limit is the Bloch-sphere Cauchy–Schwarz inequality in Mercator coordinates; the rails paper's Gudermannian is its time dependence **[A][N]**

**(a) Sides.**
- Offset Speed Limit Thm 1: τ̇² ≤ 4gS, g = ½‖Ṗ‖²_F, S = Tr[(C(1−C))⁻¹]; equality iff Ṗ = λT; Thm 2 (one accessible mode) exact gap 4(Im b̄ḃ)²/(c(1−c))²; saturating trajectory eq. (4): τ_σ = 2σm artanh(sin 2Ωt), per mode 1−2C = σ sin 2Ωt = tanh(τ/2m).
- IQGT / UPG §6: intrinsic metric g = ½Tr V², Q = g − (i/2)Ω; BH: Σ₄ is the state space of a real qutrit, Bures metric.
- Rails Thm 2: log λ₊ = gd⁻¹(ψ).

**(b) Algebra.** One mode: P = ½(1 + n·σ), n = (sinϑ cosφ, sinϑ sinφ, cosϑ), c = (1+cosϑ)/2. Then:
- g = ¼(ϑ̇² + sin²ϑ φ̇²): the round sphere of radius ½ (UPG's g; BH's "Kendall sphere radius ½").
- Γ = 1 − 2c = −cosϑ, so τ = ln((1−c)/c) = 2 artanh Γ with dτ = ∓2 dϑ/sinϑ: τ is (twice) the Mercator coordinate of latitude π/2 − ϑ, i.e. τ/2 = gd⁻¹(π/2 − ϑ).
- S = 1/(c(1−c)) = 4/sin²ϑ.
- Hence 4gS − τ̇² = (ϑ̇² + sin²ϑ φ̇²)(4/sin²ϑ) − 4ϑ̇²/sin²ϑ = 4φ̇². (The script checks the same thing as 4gS − τ̇² = S sin²ϑ φ̇², since S sin²ϑ = 4.) So τ̇² ≤ 4gS is "the Mercator velocity cannot exceed the arclength velocity times 1/sin ϑ"; equality iff φ̇ = 0, motion along a meridian.
- His saturating trajectory (m = 1) is a meridian with latitude 2Ωt: τ = 2 artanh(sin 2Ωt) = 2 gd⁻¹(2Ωt). Compare rails Thm 2 with ψ = 2Ωt: τ/2 = log(sec ψ + tan ψ) = log λ₊ of a transfer matrix with T = 2 sec(2Ωt).

**(c) Check.** 2000 random Bloch paths: g formula to 1e−6, and 4gS − τ̇² = S sin²ϑ φ̇² holds (so the bound holds with gap ≥ 0 and zero on meridians); saturating trajectory τ = 2 gd⁻¹(2Ωt) to 4e−16 at Ω = 2π·10³ s⁻¹. `identity_checks_01.py`.

**(d) Borrow.**
- The offset paper gets a one-line proof of Thm 2 and a geometric reading of Corollary 3 (τ̇ ≤ 2√(E_B S)) as a speed limit on a sphere; the equality case becomes "move along a meridian".
- Rails paper: the Lyapunov exponent at rail angle ψ is the offset of the saturating clock at time t = ψ/2Ω. Pell time: sec 2Ωt = 17 at 2Ωt = 86.63° (Apéry). The saturating trajectory is the one whose offset passes through every rail ratio.
- Open: the many-mode version (m > 1) is a product of such meridians; the cross terms that make the general bound strict are the Mercator metric's conformal factor per mode. Untested.

---

## L7. The cone paper's round-trip form, Gravity's trace form and Non-Normality's q(V) are one object; supra-unity persistence is Gravity Cor. 9 **[A][N]**

**(a) Sides.**
- Cone eq. (1): Q(θ) = M₊₋M₋₊/(E₊−E₋)², M_mn = ⟨L_m|V(θ)|R_n⟩; Re Q is the biorthogonal metric; C(Δ,θ) = Tr[Π(k)Π(k+Δu)] = 1 − QΔ² + …; supra-unity Re C = 1.00000314 at θ = 37°, Δ = 0.05.
- Gravity Thm 8 / Cor 9: overlap Re Tr(P(0)P(t)) = k − ½Re Tr(D²)t² + o(t²); negative trace form forces overlap above k.
- Non-Normality eq. (20): q(V) = ½Re Tr V²; "q < 0 forces overlap above one".

**(b) Algebra.** For a rank-one Riesz projector Π = |R⟩⟨L| the derivative along u is Π′ = [(1−Π)VΠ + ΠV(1−Π)]/ΔE-type terms, and Tr Π′² = 2 Tr(Π₊VΠ₋V)/(E₊−E₋)² = 2Q. So Re Q = ½Re Tr Π′² = q(Π′): the cone's metric is Gravity's trace form on the tangent of the Riesz projector, and the cone paper's C = 1 − QΔ² is Gravity's (and Non-Normality's) overlap expansion. Supra-unity ⇔ Re Q < 0 ⇔ Cor 9.
For two bands with n = d/E (n·n = 1): Tr(Π₊VΠ₋V) = v·v − (n·v)², so Q = (v·v − (n·v)²)/(E₊−E₋)². Drive in the xy plane gives Lorentzian directions only if Re n_z² < 0 can be arranged, i.e. through the mass-gain axis — the cone paper's "indefiniteness, not openness per se".
Cauchy–Schwarz bound: |M₊₋M₋₊| ≤ √K₊√K₋‖V‖², so |Q| ≤ K‖V‖²/|E₊−E₋|² (two bands: K₊ = K₋ = K). At a Hermitian point K = 1 and Q ≥ 0 (Thm 1).

**(c) Check.** d = (1.6, 1.2, 0.4+0.6i), four θ: Q from the formula equals ½Tr Π′² (finite-difference Π′) to 1e−11; at θ = 0.65, Re Q = −0.001264 and Re C = 1.000000126 > 1 with 1 − Re Q Δ² = 1.000000126 (Δ = 0.01); |Q| ≤ K/|ΔE|² in all four. `identity_checks_01.py`.

**(d) Borrow.**
- The cone paper's graded assembly (§5: "Restricted dynamics generates a cone [H]"; printed sign "+" in QΠ = gΠ + (i/2)ΩΠ against IQGT's g − (i/2)Ω) can cite Gravity Thm 8 for the overlap statement and the Lean-checked Non-Normality identity (20).
- Gravity gets a measurement: the cone gate (Re C = 1.00000314) is a measured instance of Cor 9, which Gravity itself lists as a local expansion only.
- The Petermann bound |Q| ≤ K/|ΔE|² says how large the cone can be near the cone wall: it grows like K, the same K that diverges at the wall (L1).

---

## L8. The self-commutator of the Riesz projector is 2K(K−1); the exit law is ‖C‖²_F = 2·rank; the band average is 1 + √((K₀−1)(K_π−1)) **[A][N]**

**(a) Sides.**
- Matter-disk §5: K(k) = 1 + u²/E(k)², ⟨K⟩ = 1 + u²/(E(0)E(π)), exit line E(0)E(π) = u²; §7: the biorthogonal C is idempotent (10⁻¹⁴).
- Non-Normality §1: (1/8)‖[H,H*]‖² is the standard non-normality measure.
- UPG Thm 8.1: non-normal Riesz projectors are oblique.

**(b) Algebra.** For rank one, Π = |R⟩⟨L|, ⟨L|R⟩ = 1, K = ‖R‖²‖L‖² = ‖Π‖²_F.
- ΠΠ† = ‖L‖²|R⟩⟨R|, Π†Π = ‖R‖²|L⟩⟨L|, so ‖[Π,Π†]‖²_F = 2K² − 2K = 2K(K−1). Exit (K = 2) gives 4.
- For a translation-invariant chain C = ⊕_k Π(k): ‖C‖²_F/rank C = ⟨K⟩. The exit law is ‖C‖²_F = 2 rank C: the biorthogonal correlation matrix has twice the Frobenius weight of an orthogonal projector (which has exactly its rank). Equivalently ½‖1−2C‖²_F per band-site = 2⟨K⟩ − 1 = 3.
- With K₀ = K(0) = 1 + u²/E₀², K_π = 1 + u²/E_π²: ⟨K⟩ = 1 + √((K₀−1)(K_π−1)). The exit law is (K₀−1)(K_π−1) = 1. (I first wrote the reciprocal; the check caught it.)

**(c) Check.** ‖[Π,Π†]‖² = 2K(K−1) to 1e−13 on 2000 cases. SSH (v,w,u) = (0.5,1,0.3): ⟨K⟩ = 1.1530931089 both ways, with the corrected product form; exit at u = 0.5, w = 1: v = 0.46821319246, ⟨K⟩ = 1.9999999999999987. `identity_checks_01.py`.

**(d) Borrow.**
- Matter-disk's open item "a proof that the block levels leave the disk exactly when ⟨K⟩ = 2" can now be attacked on the Frobenius side: the exit is ‖C‖²_F = 2 rank, a statement about a matrix norm, not an average over k. For the infinite chain the block of C shares this norm only in the limit; the P3 counterexample (w = 0) has ⟨K⟩ = 2 but no exit, so the missing condition is how ‖C‖² splits between the block and its complement. Open.
- Non-Normality: ‖[Π,Π†]‖² = 2K(K−1) puts Petermann growth on the same scale as connection energy.

---

## L9. Opened Rice–Mele: the rails modulus ũ continues to E(π)/E(0), and at the disk exit it equals K₀ − 1 **[A] for the identities, [C] for the ladder prediction**

**(a) Sides.**
- Rails Prop 4: ũ² = [(t₂−t₁)² + v²]/[(t₁+t₂)² + v²], 1/ξ = 2 artanh ũ, ladder spacing Δ = 4πK(ũ)/K′(ũ), Δ·log(8ξ) → 2π².
- Matter-disk §3: h(k) = [[iu, q̄],[q, −iu]], q = v + we^{ik}; E² = |q|² − u²; critical |v−w| = u.

**(b) Algebra.** Rice–Mele has a real staggered potential; the opened chain has an imaginary one. Substituting v_RM → iu (hoppings t₁ = v, t₂ = w): ρ = (t₁²+t₂²−u²)/(2t₁t₂), ũ² = [(w−v)² − u²]/[(w+v)² − u²] = E(π)²/E(0)². So ũ = E(π)/E(0), the ratio of the two band-edge energies. Also ũ = |Γ(ζ)| for the complex impedance ratio ζ = (t₂ + iv_RM)/t₁, a Smith-chart modulus.
- ũ → 0 exactly at the critical point E(π) → 0 (ξ diverges there).
- At the exit E₀E_π = u²: ũ = E_π/E₀ = u²/E₀² = K₀ − 1 = 1/(K_π − 1).

**(c) Check.** Three (v,w,u): ũ²_continued = E_π²/E₀² to 1e−16. Exit at u = 0.5, w = 1: ũ = 0.1311888346852546, K₀−1 = 0.1311888346852544, 1/(K_π−1) = 0.13118883468525477. `identity_checks_01.py`.

**(d) Borrow and open.**
- Prediction **[C]**: the opened chain's boundary-level spacing (real part of ln z_j) is 4πK(ũ)/K′(ũ) with ũ = E(π)/E(0) on the gapped side; at the exit ũ = K₀ − 1. Check: compute the real-part spacing from `s03*`/`s05*` at three (u, v) and compare. Not run here (needs the ring scripts). Kill: spacing differs from the closed form by more than the ladder's own uniformity error (CLAIMS §2: 0.022 → 0.006).
- Rails paper's census derivation A = 2c/π² would then extend to opened matter with ξ from E(π)/E(0).
- Convention note: matter-disk §2 uses Γ_{j+1} = Γ_j ⊕ tanh ε₀ with Γ = tanh(ε/2), so the level spacing in ε is 2ε₀. Rails' Δ is a spacing in ε. Check that convention first.

---

## L10. The census eigenvalue is a quarter of Non-Normality's flux term: X_A = ¼(E₊−E₋) of the occupation edge (1−ν, ν) **[A][N]**

**(a) Sides.**
- Matter-disk §7, Weight Between: X_A = C_AB C_BA with eigenvalue λ = ν(1−ν) = (1−Γ²)/4.
- Non-Normality eq. (15), (S5 in the first-edition table): occupation edge Γ = 1 − 2ν; v15 §11 (93) fermion Γ = 1 − 2C.

**(b) Algebra.** Take (d_i, d_j) = (1−ν, ν), d_i + d_j = 1: E₊ = 1, E₋ = Γ² = (1−2ν)², E₊ − E₋ = 4ν(1−ν) = 4λ. So the census eigenvalue is ¼ of the Lorentz mass² of the edge, and 4λ = E₊ − E₋ is boost-invariant (Non-Normality (S4)). The offset τ_ν = ln(d_i/d_j). The Offset Speed Limit's S = Σ_ν 1/λ_ν = Σ_ν 4/(E₊−E₋)_ν.

**(c) Check.** ν = 0.1, 0.3, 0.45: E₋ = Γ², E₊ − E₋ = 4λ, S_ν = 1/λ = 4cosh²(τ/2), all to 1e−15. `identity_checks_01.py`.

**(d) Borrow.**
- The statement "the census loses the sign; the offset keeps it" (Offset Speed Limit §1) is the statement that E₊ − E₋ is even under d_i ↔ d_j while τ is odd: the census sees the flux, the offset sees the log-ratio. Non-Normality's end-reversal rows (S1) have the parities.
- A boost d_i → e^φ d_i, d_j → e^{−φ}d_j is a VOTKP ⊕ step on the census level: τ → τ + 2φ, 4λ fixed: a census level can be slid along the ladder without changing X_A. This is the matter-disk §2 peel ladder with its fixed quantity named.
- Matter-disk's disk exit then reads: the edge (d_i, d_j) leaves the positive quadrant (d_j < 0 in effect, z < 0) and E₊ − E₋ = 4d_id_j changes sign: the census eigenvalue of that level goes negative. Check on the opened chain: X_A eigenvalue real part at the exit. Not run.

---

## L11. The charged-lepton generator is a d·σ with a ⊥ b; its Petermann factor is 1.5×10⁵ **[A][N]**

**(a) Sides.**
- Non-Normality §9, eq. (39)–(41): x = (√m_e, √m_μ, √m_τ), s, h₁, h₂, Z = h₁σ_z + h₂σ_x + sJ, Z² = (h² − s²)I; Koide ⇔ h = s ⇔ Z² = 0 with Z ≠ 0; ζ² = 3Q − 1.
- Matter-disk §6 / Light §8.5: Petermann factor of d·σ.

**(b) Algebra.** J = iσ_y, so Z = d·σ with d = (h₂, i s, h₁): a = (h₂, 0, h₁), b = (0, s, 0), a ⊥ b, |a| = h, |b| = s. By L1: K = max(h², s²)/|h² − s²| = max(ζ², 1)/|ζ² − 1|. Koide (ζ = 1) is K = ∞, the exceptional point. K = 2 happens at ζ² = 2 ⇔ Q = 1 (one mass dominant), the other end of the Q range.

**(c) Check.** PDG 2024 masses in his §9: Q = 0.6666644634026, ζ² = 0.99999339021, K = 151,290.7; eigenvector-based K of Z = 151,290.7 (agree to 1e−8 relative). `identity_checks_01.py`.

**(d) Borrow.**
- The measured leptons sit within 6.6×10⁻⁶ of an exceptional point of their own generator, with Petermann factor 1.5×10⁵. Non-Normality §9 gives the distance in Q (0.43σ); this gives it in the cone paper's currency.
- The cone paper's Thm 1 (no cone at a Hermitian point) and this lead: Z has K ≫ 1 yet E² < 0 slightly (Q < 2/3), so the generator is on the PT-broken side of its wall; the cone/indefiniteness question for Z is **[C]** and untested.

---

## L12. Gravity/Light's two registers map onto E₋ and E₊ through constant-blindness **[A] for the invariances, [C] for the dictionary**

**(a) Sides.**
- Light: "two registers/rails": metric (matter, projector geometry) and ledger (light, contour trace-log Z_C). Light §1: Z_C = Tr log; abstract: fixed symmetric-plus-skew family has even scalar ledger.
- Gravity Prop 30: P_{αC}(αK) = P_C(K), g unchanged, Z_{αC}(αK) = Z_C(K) + k log α.
- Offset Speed Limit §1 and join note: projector blind to sH + cI; Z_C(K + cI) = Z_C(K) + Σ log(1 + c/λ).
- Non-Normality eq. (22): [H+c, (H+c)*] = [H, H*]; (H+c)² − (H+c)*² = H² − H*² + 4cA.

**(b) Algebra.** Under H → H + cI (c real): P_C, g, and E₋ do not move; Z_C and E₊ do. So metric ↔ E₋ (both constant-blind), ledger ↔ E₊ (both constant-sensitive). Bipartite sign flip σ swaps E₋ ↔ E₊ (Non-Normality (12)), the same exchange as the parity statement for the two registers: the metric even, the ledger odd under particle–hole (Offset Speed Limit: "the offset's sign is a record of which side of the cut is filled").

**(c) Check.** Random graph H = D + A (4 vertices, 2×2 blocks): E₋ = 142.3134, E₊ = 138.7584; at H + 0.7I: E₋ = 142.3134 (unchanged), E₊ = 182.1249 (changes by the 4cA term); budget E₋ + E₊ = 2‖DA‖² and E₋ − E₊ = 2Re Tr(DA)² both hold (281.0718, 3.5551). `identity_checks_02.py`.

**(d) Borrow / what is not shown.**
- The invariance table is exact. The dictionary "metric = E₋, ledger = E₊" is a reading: the registers are defined on a Riesz projector and a contour integral, the books on a graph H = D + A. I have not found an operator that carries both at once. Building one (a graph H whose Riesz projector metric equals E₋'s weight and whose contour log equals E₊'s) is the test. Untested, **[C]**.
- If it holds, Light's "ledger and clock are its two readers" (his own wording, Offset Speed Limit join note) becomes: the clock difference reads E₋-type content, the ledger reads E₊-type content. Offer to him as a reading only.

---

## L13. Passivity and the disk: |Γ| < 1 ⇔ Re z > 0, and 1 − |Γ|² = 4 Re z/|1+z|² is Light 8.6, BH Prop 13 and matter-disk §4 **[A][N]**

**(a) Sides.**
- Light §8.6, BH §5.2 Prop 13: I − S_b*S_b = 4(WV_b)*(Herm L)(WV_b), S_b = (Z_b−I)(Z_b+I)⁻¹, Herm Z_b ≥ 0 ⇒ contractive.
- Light §8.7: thin sheet z_b = 1/(1+ζ), r = −ζ/(2+ζ), R + T + A = 1, A ≤ ½ (passive, "one-half bound").
- Matter-disk §4: Γ = tanh(W/2), |Γ| < 1 iff |Im W| < π/2; z = −28 gives Γ = 1.0741 (⁵He, VOTKP §15.4).

**(b) Algebra.** Scalar case: 1 − |(z−1)/(z+1)|² = 4 Re z/|z+1|². So |Γ| < 1 ⇔ Re z > 0 ⇔ |Im W| < π/2 (z = e^W). The matter-disk disk is the passive half-plane; "leaving the disk" is losing passivity of that level. Sheet: with z_b = 1/(1+ζ), 4 Re z_b/|1+z_b|² = 4(1+Re ζ)/|2+ζ|² = T + A, consistent with Light's R + T + A = 1.

**(c) Check.** Random complex z: 1 − |Γ|² = 4Re z/|1+z|² to 1e−16 (including values with |Γ| > 1, where both sides are negative: −298.06). `identity_checks_02.py`.

**(d) Borrow.**
- Matter-disk's unbound nuclei (⁵He, ⁵Li, ⁸Be, outside the disk) are non-passive loads in Light's language, with the quantity 4 Re z/|1+z|² = 1−|Γ|² negative: they emit.
- The exit law E(0)E(π) = u² becomes a passivity margin: the exit is where the first level's 4Re z/|1+z|² reaches zero. Check on the opened chain: min over levels of 4 Re z/|1+z|² at the exit. Not run.
- Light's one-half absorption bound (A ≤ ½, equality at ζ = 2, r = −½, t = ½): the same ½ as L3 appears in a different quantity (Γ = ½ here, Γ² = ½ there). I do not see a link; noted as a curiosity, not a lead.

---

## L14. UPG/IQGT's curvature bound and Non-Normality's Gram duality are the same Cauchy–Schwarz; equality is the two-level/scalar-edge case **[A] for the two-level case, [C] in general**

**(a) Sides.**
- UPG Thm 6.1 / IQGT / Weight Between eq. (2): |Ω| ≤ 2√(g_VV g_WW − g_VW²), equality for rank one (two-level).
- Non-Normality eq. (17): P_e² + V_e² + L_e² = 1, L_e² = 4(‖a‖²‖b‖² − ⟨a,b⟩²)/s² ≥ 0, L = 0 exactly for scalar edges.

**(b) Algebra.** Both are Cauchy–Schwarz for a Frobenius form. In UPG the form is Q(V,W) = Tr(X_V†X_W) on off-diagonal blocks, complex, giving g_VW² + Ω²/4 ≤ g_VV g_WW. In Non-Normality it is the real trace form on edge blocks a = D_i, b = U(D_j). Two-level check on the Bloch sphere: g = ¼(dϑ² + sin²ϑ dφ²), Ω_ϑφ = ½ sinϑ, so 4 det g = ¼ sin²ϑ = Ω²: equality. The scalar-edge circle P² + V² = 1 (his Fig. 5) is the rank-one equality. Rails: sec² − tan² = 1 is the same circle (L2).

**(c) Check.** Bloch: 4 det g = Ω² = 0.1534003 at ϑ = 0.9 on both sides (by hand, script prints both). General statement not run.

**(d) Borrow.**
- A single "two-books" notation for IQGT and Non-Normality: the curvature Ω² is the part of L_e² that the complex phase supplies; for rank-one fields Ω² = 4 det g and L = 0.
- General multi-level equality case: UPG says equality for rank one only; Non-Normality's matrix edges "fill the disc" (L² > 0). The claim "UPG's slack ⇔ Non-Normality's L²" is **[C]**: the check is slack = (s²/4)L² on random two-parameter projector families. Not run.

---

## L15. Garrett's norm ladder is the Fermi–Dirac occupation ladder: Γ_L = 1 − 2n_FD(L ln 5) **[A][N], use is [C]**

**(a) Sides.** Two Trees Thm 2.5: Γ_L = (5^L − 1)/(5^L + 1), length L ln 5. Matter-disk §1: Γ = 1 − 2ν = tanh(ε/2). VOTKP §15: bound steps inside the disk; gas §8: Γ_pop = tanh(½ ln n_q/n_{q+1}).

**(b) Algebra.** ν_L = 1/(1+5^L) is the Fermi–Dirac occupation at ε = L ln 5 (units kT = 1). So Garrett's tree levels are an equally spaced fermion ladder with spacing ln 5 = 1.609, below the Schottky spacing 2 ln(1+√2) = 1.763 of L3; the ln 7 drawing has spacing 1.946, above it. The ladder is "free but not discrete" (ln 5) vs "Schottky" (ln 7): free groups on both sides, discrete only above 1.7627.

**(c) Check.** L = 1, 2, 3: Γ_L = 0.666667, 0.923077, 0.984127 equals 1 − 2n_FD to 1e−16. `identity_checks_02.py`.

**(d) Borrow.**
- Matter-disk: a physical ladder with spacing exactly ln 5 (or ln 7) would be a lab realisation of Two Trees' groups. Which entanglement ladders have uniform spacing Δ = ln 5? Rails Δ = 4πK(ũ)/K′(ũ) = ln 5 fixes ũ; that ũ is the Rice–Mele chain whose census ladder is Garrett's norm tree. Solving this is a one-line root find; not run.
- Whether the free-group property (Two Trees Thm 5.1, residue mod 5) has any meaning for the census (a statement that no non-backtracking sequence of ⊕ steps returns to 0) is **[C]**: it would say the ladder never closes. Untested.

---

## Ranking (my read, for the next step)

1. **L2** (rails = edge; T²−4D = E₋): strongest, exact, joins three papers, answers the rails paper's regime table in Non-Normality's own words.
2. **L3** (five faces of Γ² = ½): exact, and gives matter-disk's exit constant a geometric proof partner. Caveat on ⟨K⟩ vs per-k is stated.
3. **L6** (offset limit = Mercator Cauchy–Schwarz; saturating trajectory = rails gd⁻¹): exact, new one-line proof of his Thm 2, ties to IQGT's g.
4. **L7** (cone Re Q = Gravity trace form = Non-Normality q): exact, checked on his own cone gate point.
5. **L4** (4 ln(1+√2) in rails and Two Trees): the number identity is proved; the explanation of T = 34 is open and is the interesting part.

Others of interest: L1 (prerequisite for L3, L11), L8 (Frobenius form of the exit law), L9 (ladder-spacing prediction, the only one here with a prediction not yet run).

## Prior-art and honesty notes

- L1: K = 1/sin²φ for two levels and K = ‖Π‖²_F are textbook (Petermann factor, Siegman); Non-Normality's q is his. The join is his two papers, not new to the literature.
- L5: tan(θ/2) = tanh(r₁/2)tanh(r₂/2) is Rhodes–Semon (his own citation in Two Trees). Identification with E₋/E₊ is the new step.
- L6: Mercator/Gudermannian form of the Bloch sphere is classical; the Offset Speed Limit's Mandelstam–Tamm lineage is stated in the paper.
- I did no web search (instruction was to read; and he limits web requests). Prior-art for L2, L3, L4, L8 was not checked and should be before any of these goes into a paper.
- No identity here uses Dark Energy language, a spacetime metric substitution, or a mixer. L12 is the only one that borrows his "registers" vocabulary and is marked as a reading.
- Provenance tags for the matter-disk README sections are unchanged by this file; these leads are not findings until a numbered section with scripts and a kill condition exists.
