# Leads, matter then on down (v1)

Prepared for Jeromie Beasley, 3 November 2026. A lead-finding note, not a result. Nothing here is a finding until a kill condition has been written, run and recorded in `CLAIMS.md`. No file of his was edited. Made with AI assistance (see `AI_USE.md`).

## How to read this

- Notation is his: `Gamma = (z - 1)/(z + 1) = tanh(W/2)`, `W = ln z`; occupation `nu`, odds `z = (1 - nu)/nu`, `Gamma = 1 - 2 nu`; offset `tau`; census `X_A = C_AB C_BA`; `tau_nu = Log((1 - nu)/nu)`.
- Papers: **MS** Matter at a Scale v5; **OFF** The Offset Belongs to the Boundary v31; **OSL** The Offset Speed Limit v1.1; **WB** The Weight Between v2.3; **VOTKP** v2.9; **CONE** the cone paper v8; **MD** matter-disk README, CLAIMS, PROVENANCE (sections 1 to 9); **KOIDE** Koide, Connection Energy, and the Prime-by-Prime Record; **NEUT** When the Neutrinos Leave.
- Ranking is by how much of the lead rests on his own text. Leads 1 to 5 use only his equations and his own numbers. Leads 6 to 10 need a published data table (NUBASE and similar) but no outside theory beyond what is flagged. Leads 11 to 17 need outside physics and are flagged **OUTSIDE** in the heading.
- Grades as he uses them: theorem [T], measured against published data [V]lit, verified with controls [V], conjecture [C], reading [H].
- Prior art has NOT been checked for any lead (his rule: check before investing). Likely-crowded leads are marked.

## Coverage, stated plainly

Read in full: MD README, CLAIMS, PROVENANCE, AI_USE; notes for MS, OSL (both versions), CONE, VOTKP (all of it, including the appended full read), band_edge, screen_prog_03 and 04, nonnormal_lattice, spectral_stability, theta_21.
Read for the sections the theme needs, not line by line: OFF (sections 1 to 7, 12, 13), WB (sections 1 to 6), NEUT (sections 1 to 4), KOIDE (sections 1 to 4), twotrees (abstract, sections 1 to 3), BH, LIGHT, GRAVITY, ladder (openings and keyword searches for Petermann, exceptional point, Cayley, resonance).
Not read this pass: atlas_v7 beyond keyword hits, v21, dirac_gigantefermion, directional_transport, colour_selects_leader, projector_calibration, iqgt, nonnormality, present_keeps, what_transport_keeps, what_russell_saw, paper_XI, paper_v7, suns, upg, three_body, four_body, filament, foft_v2, earth_moon, obs, price_of_a_direction, kakeya notes. Leads may exist there that I did not see. The "about 40 full reads" instruction was not met for these.

Small computations run while writing (milliseconds, scratch only, not kept as scripts): the nuclear numbers in leads 6 and 7, the continued-offset check in leads 1 and 2, the damped-oscillator algebra in lead 14. Each is marked where used. They are lead-finding checks, not registered runs, and any number from them that was looked at after the fact is graded post hoc.

---

## TIER A. Rests directly on his text

### Lead 1. The disk-exit law is a quarter turn of the continued offset: `<K> = sec^2( (1/2) Im tau_inf )`

(a) Statement, PT-symmetric class (MD section 5). Rice-Mele with staggering `v -> i u` is the opened SSH chain (`E^2 = |q|^2 - u^2`, `E_min = E(pi)`, `E_max = E(0)`). OFF section 5 gives the large-block offset `tau_inf = 2 artanh( v/sqrt(E_min E_max) )`. Continued to `v = i u`:

`Im tau_inf = 2 arctan( u / sqrt(E(0) E(pi)) )`, and with MD section 5's band average `<K> = 1 + u^2/(E(0)E(pi))`:

`<K> = 1 + tan^2( Im tau_inf / 2 ) = sec^2( Im tau_inf / 2 )`.

So `<K> = 2` is exactly `Im tau_inf = pi/2` (a quarter turn of the signed offset), the exit line `E(0)E(pi) = u^2` is that quarter turn, and the critical point `E(pi) -> 0` is `Im tau_inf = pi` (half turn). This is the sentence MD's README already uses ("a quarter turn marks the exit line; a half turn marks the critical point"), made into an identity.
Joins: OFF section 5 (endpoint constant), OFF section 7.8 (central rung is the odd-block offset), MD section 4 (Im W), MD section 5, OSL section 1 (`1 - 2 nu = tanh(tau_nu/2)`).

(b) Why. The odd-block ladder pairs `(eps, -eps)` and leaves one central rung whose value is the total offset, so the central level's `Im W` is `Im tau_inf`. `tan(Im tau/2) = x` where `x = u/sqrt(E_min E_max)`, and `<K> - 1 = x^2`. Both sides are algebra once the closed form continues to complex `v`. Checked while writing: massless `(t1, w) = (0.5, 1)`, the continued formula gives `Im tau/pi = 0.500000` at `gamma = 0.4743416` (the measured exit), and `sec^2` of half of it matches `<K>` at `gamma = 0.4` (1.3686 against 1.3689, rounding of my hand arithmetic; run properly it should be exact).

(c) Kill condition, written before the run: on the opened chain at three unseen `u` (say 0.15, 0.35, 0.55) with `t1 != w`, the lowest block level's `Im W/pi` at the measured exit differs from 0.5 by more than 1e-3, or `<K>` differs from `sec^2(Im tau/2)` by more than 1e-6 on the closed form, at any of the three. Opposite also run: with the sign of `u` reversed, and with the odd block replaced by an even block (where OFF says the protected offset is zero), to see what the identity then predicts.

(d) Needs: existing MD scripts (`s05*`, `nhssh_lib`), block sizes 40 to 160 already used. Laptop-scale, minutes. The continuation of OFF's endpoint theorem to complex `v` needs its domain checked (strict positivity `0 < C_A < I` fails when the covariance is non-Hermitian); that is the open step, stated visibly.

(e) Grade: [T] for the algebra given the continuation; [V] for the identity on the chain. It closes the MD README open item 1 for the PT class only.

NOT claimed: it does not say what sets the massive-band exit. Tried while writing: with a mass term `sec^2(Im tau_inf/2)` is 1.0245, 1.0182, 1.0162 at the three massive exits against `<K>` = 1.0224, 1.0188, 1.0150. Near misses of 1e-3 to 2e-3 in both directions, not an identity. See lead 2.

### Lead 2. The massive-band exit is a tower, one exit per ladder rung, and the endpoint filter selects the rung

(a) Statement (MD sections 6 and 9). The block ladder is `eps_j = tau_inf + j Delta*`, with `Delta* = 4 pi K(m)/K(1 - m)`, `m = E_min^2/E_max^2` (OFF equations 92 and 101). For a real band `m` is real and `Delta*` is real, so `Im eps_j` is the same for every rung, and one exit line serves all rungs: this is the PT (massless) class, MD section 6's `<K> = 2` law. For complex mass `mu = m + i gamma`, `m` is complex, `Delta*` is complex, and `Im eps_j = Im tau_inf + j Im Delta*` grows with `j`. Rung `j` leaves the disk when `Im eps_j = pi/2`, at `gamma_j`, and `gamma_j` falls as `j` grows. With every rung counted the exit tends to `gamma = 0+`; the endpoint filter `nu > delta` admits rungs up to the one with `nu_j > delta`, so the measured exit is `gamma_j` of the deepest admitted rung. The "exit" in MD section 6 is then not a band property; MD section 9's filter table is this tower seen through a window.

Predicted rung exits from the ideal ladder (computed while writing, 30 digits, post hoc):

| `(t1, m)` | rung 1 | rung 2 | rung 3 | rung 4 | rung 5 |
| :-- | :-: | :-: | :-: | :-: | :-: |
| (0.5, 0.4) | 0.2794 | 0.1722 | 0.1244 | 0.0973 | 0.0799 |
| (1.5, 0.4) | 0.3817 | 0.2391 | 0.1745 | 0.1373 | 0.1131 |
| (1.5, 0.8) | 0.3941 | 0.2269 | 0.1594 | 0.1229 | 0.0999 |

Level `|nu|` at the rung-j exit, `(0.5, 0.4)`: 6.6e-5, 9.4e-9, 1.3e-12, 1.8e-16. Against MD section 9's measured plateaus at `(0.5, 0.4)`: 0.271637 (filters 1e-6, 1e-8), 0.169170 (1e-9, 1e-10), 0.122722 (1e-12). The three plateaus sit within 2.9%, 1.8%, 1.4% of rungs 1, 2, 3, the error shrinking with depth as an asymptotic ladder should, and the filter boundaries fall where the rung `|nu|` values cross 1e-8, 1e-9 and 1e-12.

Where it does NOT match, stated plainly: at `(1.5, 0.4)` and `(1.5, 0.8)` the single 1e-9 filter admits rungs up to 2, predicting 0.2391 and 0.2269, against measured 0.1957 and 0.2519 (22% and 11% off, and the second is on the wrong side). The ideal ladder (101) is an asymptotic statement and was matched in OFF only for real parameters. So the lead is a strong post-hoc reading at one parameter set and a failure at two. It is repaired, not dropped: the next step is the exact finite-block ladder (not the ideal one) and the intercept `q` (OFF equation 95) in place of `tau_inf`.
Joins: OFF sections 7.3 to 7.8, MD sections 3, 5, 6, 9, GPT P3 (the w = 0 counterexample, where `m` degenerates).

(b) Why. Opening makes the single ladder spacing complex. Each rung then has its own rotation, and a window that includes more rungs sees an earlier exit. The massless class is exactly `Im Delta* = 0`.

(c) Kill condition, written before the run. Pre-register the predicted rung exits above for two unseen parameter sets `(t1, m) = (1.0, 0.4)` and `(0.7, 0.6)`, computed from `Delta*` and `tau_inf` only. Run the block exit with mp precision at filters 1e-6, 1e-9, 1e-12, 1e-15, 1e-18. Kill: any measured plateau differs from the nearest predicted rung by more than 5% at both sets; or the measured exit does not decrease as the filter deepens; or the plateau count is not the predicted rung count. Opposite tried: also test the negative side `eps = tau - j Delta*` (levels near `nu = 1`); my table shows its exits arrive at nearly the same `gamma`.

(d) Needs: MD scripts `s04b`, `s06` with arbitrary precision (levels at `nu` 1e-16 and below need mpmath, not float64). Laptop-scale, tens of minutes. No new data.

(e) Grade if it passes: [V] with the PT class as control (`Im Delta* = 0`, one plateau). If it only holds at one set: reading.

### Lead 3. Census sign at the opened critical point: census reads `|c|`, the offset and entropy read the sign

(a) Statement. MD section 3 measures the Renyi-2 central charge at the opened critical point as `c_eff = -1.79 -> -1.96` on `v < w` (literature: -2). OSL section 1: "The census C - C^2 alone loses the sign... The offset is the clock face; the census is the gauge without its sign." MS section 3.3: `A = 2c/pi^2` per two-endpoint interval, from the ladder count, which is a count of rungs inside `nu in [eps, 1 - eps]`. Prediction: at the opened critical point the radial boundary census (MD section 9: count by `|1 - 4 lambda|^(1/2)`) grows as

`N_eps ~ (2 |c_eff| / pi^2) ell_eps ln L = (4/pi^2) ell_eps ln L` (coefficient 0.405),

positive, while the entropy route carries `c_eff = -2` with its sign. That is the same structure as OSL's `diag(0.2, 0.8)` against `diag(0.2, 0.2)`: same census, opposite offsets.
Joins: MS eq. (2), OFF section 7.8, OSL section 1, MD sections 3, 7, 9.

(b) Why. A count cannot be negative; the ladder count uses `|eps|` windows. Whether it picks up `|c|` or something else depends on whether the opened ladder keeps equal spacing in `|Re eps|`. Lead 2 says the spacing is complex, so this is a real question, not a formality.

(c) Kill conditions (three, written before the run, each separate). K1: slope is `4/pi^2` within 10%. K2: slope is `2/pi^2` (the unopened critical coefficient at `c = 1`): the census is blind to opening. K3: no logarithmic growth. Also run the Hermitian critical control (`c = 1`, expect 0.2027) and the gapped control (saturates) at the same sizes, and the `v > w` side, whose Renyi-2 value has not converged (MD open list).

(d) Needs: MD scripts `s03b` and `s07`, block sizes to a few thousand. Laptop-scale. Prior art for the central charge is crowded (non-unitary critical chains); the census-sign framing is his.

(e) Grade: [V] on this chain, one model only (MD tag: MINE ON A TEST BED).

### Lead 4. A speed limit for the complex offset of opened matter

(a) Statement. OSL Theorem 1: `tau_dot^2 <= 4 g S`, `g = (1/2)||P_dot||_F^2`, `S = Tr[(C(I - C))^-1]`. MD section 4 flags "a speed limit for the complex offset of opened matter is untested". For a biorthogonal (oblique) idempotent `P` the proof steps `tau_dot = Tr(W C_dot)`, `P_dot` off-diagonal, and `Tr(F P_dot) = Tr(T P_dot)` with `T = [P,[P,F]]` all survive (they use only `P^2 = P` and that `C`, `I - C` commute). What fails is `||T||^2 = 2S`: for an oblique `P` the Frobenius norm of `T` has a cross term. Candidate: `|tau_dot|^2 <= 4 g S (1 + delta)` with `delta` set by the Petermann factor `K` of the block. Untested whether `delta = 0`.
Joins: OSL Theorem 1 and Appendix A (tangent is off-diagonal), WB Theorem 7 and Corollary 9, MD sections 4, 5, CONE Theorem 1 (Hermitian point is positive).

(b) Why. The Hermitian proof closes with orthogonality of the two off-diagonal blocks of `T`; biorthogonality replaces that by a K-weighted inner product.

(c) Kill condition. Draw 1e5 random oblique idempotents (rank 1 to 3, near and far from exceptional points) and random smooth paths; compute `|tau_dot|^2/(4 g S)` with the same `g` and `S`. If the ratio ever exceeds 1, the Hermitian form fails and the correction `delta(K)` becomes the object. If it never exceeds 1 even when maximised by optimisation over `P_dot` (the opposite, his rule), the Hermitian form may extend and a proof is the next step. Equality case: does the saturating trajectory (OSL equation 4) survive opening?

(d) Needs: ten lines of numpy. Laptop-scale, minutes.

(e) Grade: [T] if proved either way; [V] otherwise.

### Lead 5. The rim and the pole of the peel disk are one-nucleon and two-nucleon thresholds; unbound nuclei are small negative occupations

(a) Statement. With his orientation (z = next separation energy over the first, the first being the outer step), his three gap nuclei have `z = -28.0, -10.08, -80.25` (his script output, `s10`). Exact consequences of `Gamma = 1 - 2 nu`, `nu = 1/(1 + z)`:

- `nu = S_first/(S_first + S_next)`, the first step's share of the two-step total. Bound steps have `nu in (0, 1)` (the MD section 1 window). Unbound: `nu = -0.0370, -0.1102, -0.0126` for 5He, 5Li, 8Be.
- `|Gamma| - 1 = -2 nu = 2|S_first| / (S_next - |S_first|)`. VOTKP 15.4 says the distance outside the rim is "close to twice the decay energy over the neighbouring step" and calls the ordering an observation. It is an identity: 0.07406, 0.22032, 0.02524, agreeing with the printed |Gamma| 1.074, 1.220, 1.025.
- The rim (`|Gamma| = 1`, `Re z = 0`) is a one-step threshold, `S = 0`. The Cayley pole `z = -1` is `S_first + S_next = 0`, which for two consecutive neutron removals is `S_2n = 0`: the two-neutron drip line. VOTKP's onion uses `S_2n` ratios, which is the pole-free chart.
- Across the pole the two outside sheets differ: `Gamma > 1` is `z < -1`, `Gamma < -1` is `-1 < z < 0`. A Borromean nucleus (bound, but removing one neutron leaves an unbound core+n) has outer step bound, inner unbound, and `S_2n > 0`, so it sits on the `-1 < z < 0` sheet with `|Gamma| > 1`.
Joins: VOTKP Theorem 8.1, 15.2 and 15.4 (pages 71 to 72), MD sections 1, 4, `s10_nuclear_gaps_his_script.txt`.

(b) Why. Algebra of `(z - 1)/(z + 1)` and `1 + z = (S_first + S_next)/S_first`.

(c) Kill condition. (i) Identity fails on any NUBASE2020 step by more than 1e-12. (ii) The claim "Borromean nuclei sit on the -1 < z < 0 sheet" fails for any established Borromean nucleus (6He, 11Li, 14Be and so on) when `z` is computed from NUBASE masses. Both are checks, not risks; the value of the lead is the reading and the data scan.

(d) Needs: NUBASE2020 (public, already used by his `mass_gaps_smith.py`). Laptop-scale, seconds.

(e) Grade: [T] for (i); [V]lit for (ii); the negative-occupation reading is [H]. Prior art: only for Borromean definitions (standard, flagged OUTSIDE for that word only).

---

## TIER B. His coordinate plus a published data table

### Lead 6. Resonances as rotations: `Im W = pi - theta`, `theta = arctan(Gamma_w / 2 E_r)`, computed from his own printed half-lives

(a) Statement. A resonance has complex separation energy `S = -E_r + i Gamma_w/2`. Then `z = S_next/S`, `Im W = -(pi - theta)`, `theta = arctan(Gamma_w/(2 E_r))`, and `|Gamma| < 1` iff `Re z > 0` iff `Re S > 0`: the exit is the pole's real part crossing threshold. Using only the half-lives he prints in VOTKP 15.4 (width `Gamma_w = hbar ln2 / t_half`), computed while writing:

| nucleus | `Gamma_w` (keV) | `theta` | `|Im W|/pi` | complex `Gamma` |
| :-- | :-: | :-: | :-: | :-: |
| 5He | 758 | 27.28 deg | 0.8484 | 1.0733 - 0.0396 i |
| 5Li | 1233 | 17.41 deg | 0.9033 | 1.2177 - 0.0766 i |
| 8Be | 0.0056 | 0.0017 deg | 0.99999 | 1.0252 - 0.0000 i |

This is the particle-side step in MD's open list ("nuclear resonances placed by rotation from published energies and widths"), done with his own numbers. MD section 4 finds levels at exactly `Im W = pi` at opened critical points; the nuclei sit at `Im W = pi - theta`, and the opened chain reaches `Im W/pi` = 0.5 at its exit, 1.0 at its critical point.
Joins: VOTKP 15.4 (the resonance caution: "leakage rates require channel couplings and barriers"), MD sections 4, 5.

(b) Why. A complex pole is a complex `z`; the disk does the rest.

(c) Kill condition. The pair `(rho, theta)` with `rho = ln|z|` is only a change of variables for `(E_r, Gamma_w)`, so on its own it predicts nothing. The testable content: for neutron resonances at fixed orbital angular momentum, points `(rho, theta)` lie on one curve and no point lies beyond the single-particle (Wigner) limit curve. Kill: a published narrow-or-broad light resonance at that `l` outside the curve by more than its quoted errors. The widths in NUBASE and in a TUNL/ENSDF evaluation differ by evaluation (5He especially); use both and report the spread. Not yet tested.

(d) Needs: NUBASE2020 plus a width table. **OUTSIDE**: the Wigner limit and the barrier penetrability are outside physics, flagged; VOTKP says the escape barrier is not in the coordinate. Laptop-scale.

(e) Grade: [V]lit if the limit curve holds; otherwise a restatement.

### Lead 7. Registered test of VOTKP open item 11: does the peel ratio add anything beyond the decay energy?

(a) Statement. VOTKP 15.4 ordered three post-hoc points (half-life against `|Gamma| - 1`) and called it an observation. Scan every NUBASE nuclide that is one nucleon (or an alpha) beyond a bound neighbour. Prediction to test: at fixed emitted particle and `l`, `ln Gamma_w` depends on `|Gamma| - 1 = 2|S|/(S_next - |S|)` only through `|S|`; the neighbouring step `S_next` adds nothing. This is likely, since NUC-01 found peel shape restating `delta_2n`. It is stated as the straw man to be killed, per his rule: the strongest form is that `S_next` matters.
Joins: VOTKP 15.4, 17 (open 11), NUC-01, lead 5.

(b) Why. The barrier carries the width; the neighbouring step is the other end of the ratio.

(c) Kill condition, before the run: partial rank correlation of `ln Gamma_w` with `|Gamma| - 1` controlling for `|S|` is not greater than 0.3 in each of three classes (neutron, proton, alpha). Opposite: control for `S_next` and ask whether `|S|` adds.

(d) Needs: NUBASE2020 only (half-lives, uncertain and limit values need the declared handling; the registration must say how limits count, the lesson of T16). **OUTSIDE** for the barrier model, flagged; none is needed for the test itself. Laptop-scale.

(e) Grade: [V]lit; most likely outcome is the straw man surviving, which is itself a clean negative control.

### Lead 8. Integer record along a chain: sign alternation, winding, and why `S_2n` removes it

(a) Statement. Along an isotopic chain, `z_k = S_(k+1)/S_k` is negative whenever the single-nucleon separation energy changes sign between neighbours. With odd-even staggering, a loosely bound chain such as the helium isotopes beyond 4He alternates in sign (untested: to be read from NUBASE), so every single-neutron rung is outside the disk with `Im W = pi`, and the rapidity winds by `pi` per rung. Pairing the steps (VOTKP's `S_2n`) removes the alternation. Algebraically `(+)` is a Mobius law and holds off the disk (the proof of Theorem 15.1 is `2(AB - 1)/2(AB + 1)`), so the composite `(E_m - E_0)/(E_m + E_0)` survives, but `Gamma` cannot see an even number of crossings: two unbound steps in a row give `z > 0` and a deceptively inside-the-disk point. The winding number of `Im W` along the chain, in units of `pi`, is an integer record in the sense of MS section 4.2 ("windings, signatures, channel counts").
Joins: VOTKP 15.2, 15.4, 19.2 (cancellation defect), MS section 4.2.

(b) Why. `Gamma(W)` has period `2 i pi` in `W`.

(c) Kill condition. Count, over all NUBASE chains, the sign changes of `S_n` and compare with the sign changes of `S_2n`. Kill the staggering explanation if the alternation count of `S_n` beyond the first bound nucleus is not larger than that of `S_2n` in at least 80% of chains with at least four unbound rungs. List every unbound-to-unbound step: each is a place where the chart is misleading, which belongs in VOTKP's negative controls.

(d) Needs: NUBASE2020. Laptop-scale, seconds. **OUTSIDE** only for the word "pairing", already implicit in his choice of `S_2n`.

(e) Grade: [T] for the periodicity and the composite; [V]lit for the chain counts.

### Lead 9. Rung exits for the gas generator (MD open item, with the neutrino chain as a ready example)

(a) Statement. MD open list: "Gas as opened matter: the kinetic generator `L = -nu Q - i k M` is non-normal; place its modes on the disk." NEUT section 2 already has the two-moment truncation, eigenvalues `lambda = -kappa/2 +- sqrt(kappa^2/4 - k^2/3)`, exceptional point at `kappa = 2k/sqrt(3)`. Place the root ratio `z = lambda_+/lambda_-` on his disk (checked while writing, simple algebra): at `kappa = 0`, `z = -1` (the Cayley pole, pure oscillation); at `kappa = sqrt(2/3) k` the roots are at 45 degrees and `Re z = 0` (disk exit, damping ratio `1/sqrt 2`); at `kappa = 2k/sqrt 3`, `z = 1` (the centre, the exceptional point); beyond it `z` is real positive and `Gamma` runs to the rim as `kappa -> infinity`. So pole, exit, centre, rim are four named positions of one damped mode. NEUT says the exceptional point belongs to the truncation and that with 200 moments the least-damped mode turns real near `kappa = 0.646 k`: the prediction is where, in that 200-moment chain, the first mode leaves the disk and whether the exit tracks `kappa/k` near `sqrt(2/3)` or elsewhere.
Joins: NEUT sections 2 and 4, WB Corollary 9, MD sections 4, 5, MS section 4.1 (gas is wall-free; non-modal).

(b) Why. A damped mode's root ratio is a Smith point; its quarter turn is the 45-degree root.

(c) Kill condition. For the 200-moment chain, define the exit as the first mode whose root-ratio has `Re z = 0` against the first mode that turns real; kill the pairing "exit near `sqrt(2/3) k`" if the 200-moment exit lies outside 0.8 to 1.0 times that value. Opposite: use the density-flux ratio (not the root ratio) as the disk point.

(d) Needs: NEUT scripts. Laptop-scale. No outside physics.

(e) Grade: [V] on one operator (the NEUT relaxation model); not a general law.

### Lead 10. Gas with excited-state weights: how far does `Gamma_0` read back move (MD section 8, the opposite test)

(a) Statement. MD section 8 returns `Gamma_0 = D/B = 29.830/79.005 = 0.377575066984` for ground-state weights `U = (1, 2, 1)`. With `U(T)` summed over NIST levels, `D(T) = D - kT^2 d ln(U_0 U_2/U_1^2)/dT` and the slope reading drifts. A back-of-envelope size, untested: He I first excited level at 19.82 eV (g = 3) gives a relative `D` shift of order `3 e^(-19.82/kT)(19.82/29.83)`, about 2e-5 at 20 kK and about 6e-3 at 40 kK. The prediction is the curve of read-back `Gamma_0` against `T`, which tells at what temperature the ground-state model stops being a measurement of the peel step.
Joins: MD section 8, VOTKP section 20.3.2 (anchored ladder).

(b) Why. Excited states add `T`-dependent terms to the two log combinations.

(c) Kill condition. If the shift at 20 kK exceeds 1e-6 in `Gamma_0` the section 8 claim "to 2e-16" is a ground-state-model statement only (it already says so); if the shift is below 1e-9 up to 30 kK the ground-state model is safe in the review's range.

(d) Needs: NIST ASD levels for He I and He II (IMPORTED, not his; MD tags section 8 IMPORTED), Saha solver already in `s08`. **OUTSIDE**: ideal Saha gas is textbook. Laptop-scale.

(e) Grade: [T] in the model; stays a reproduction note (PROVENANCE rule 4).

---

## TIER C. Needs outside physics, flagged

### Lead 11. **OUTSIDE.** Natural-orbital occupations of helium-like ions against the last peel step `5/(8Z)`

(a) Statement. VOTKP 15.10: `Gamma_last -> 5/(8Z)`. MD section 1 and OSL: `Gamma = 1 - 2 nu` for an occupation `nu`. For a helium-like ion, first-order perturbation theory gives a correlated (non-1s) natural-orbital occupation `nu_2 ~ kappa/Z^2`. Reading to test: is `nu_2 Z^2 / (Gamma_last Z)^2` tending to a constant, i.e. is the one-electron occupation defect the square of the last peel step? Not an identity: the two `Gamma`s are defined on different objects (an IE ratio against an occupation), so the comparison is flagged STRUCTURAL.
Joins: VOTKP 15.10, MD section 7 (census of a pure state).

(b) Why. First-order correlation amplitude scales as `1/Z`; the peel step scales as `5/(8Z)`; occupation is an amplitude squared.

(c) Kill condition. Ratio not approaching a constant (within 5%) over `Z = 10 to 80`.

(d) Needs: two-electron CI or Hylleraas to modest accuracy. **OUTSIDE** (quantum chemistry). Laptop-scale, an afternoon. Grade: [H] at best.

### Lead 12. **OUTSIDE.** Monolayer end of the thin-film peel

(a) Statement. VOTKP Theorem 6.3: the thin end is a shunt admittance, error falling as `d^2`, whole-sheet form missing 12 to 16% at the substrate face. For an atomically thin film in vacuum the sheet admittance is `y = Z_0 sigma`. For graphene with universal `sigma = e^2/(4 hbar)`, `y = pi alpha = 0.02293` (computed), first-order absorbance `pi alpha`, reflectance `(y/(2 + y))^2 = 1.28e-4`. A zero-parameter number at the atomic end of the film peel, with his `Gamma_film = -y/2` to first order.
Joins: VOTKP 6.4, Theorem 6.3, 17 (open 16).

(b) Why. Theorem 6.3 needs only the film's optical sheet response, which is known for a monolayer.

(c) Kill condition. A published suspended-monolayer absorbance (Nair et al., Science 2008, to be read at source) outside the first-order value by more than its quoted error. 

(d) Needs: published sheet conductance. **OUTSIDE**; this is textbook and would be a reproduction note, not a finding (PROVENANCE tag IMPORTED). Laptop-scale, minutes. Grade: [V]lit as a reproduction.

### Lead 13. **OUTSIDE.** Ladder classes: exponential, power, affine, and where each scale sits

(a) Statement. With hyperbolic length `ln(IE_l/IE_1)` (VOTKP Corollary 15.2), three ladders have three growth forms: the matter ladder `eps_j = q + j Delta` has linear length in rung count (MD section 2: constant peel step); the atom's Thomas-Fermi middle has `IE_m ~ m^(4/3)`, length `(4/3) ln l` (VOTKP 15.11); a nuclear chain in the liquid-drop middle is affine, `S ~ a - bN`, length `ln(S_0/S_N)` saturating at the drip line. Reading: the number of rungs reachable within hyperbolic distance `ell` of the anchor is linear in `ell` for matter, exponential for the atom's middle (`l_max = e^(3 ell/4)`), and finite for a nucleus. VOTKP 15.4 found no nuclear analogue of the 4 to 9% in-shell TF agreement and NUC-01 failed; the class statement says why: nuclear saturation is not a power law in the removed number.
Joins: MD section 2, VOTKP 8.1, 15.11, 15.4, NUC-01.

(b) Why. Pure bookkeeping on the three functional forms; the content is which form each scale obeys.

(c) Kill condition. On NUBASE chains with `N` well away from magic numbers, an affine fit of `S_2n(N)` beats a power-law fit in median residual by at least a factor 2 at `Z` = 20 to 82. Opposite: whether the Thomas-Fermi step form `tanh((2/3) ln((k+1)/k))` is beaten at fixed `Z` by the nuclear affine form (it should lose for atoms and win for nuclei if the class statement is right).

(d) Needs: NUBASE and the VOTKP archive (`element_thresholds_20261011.json.gz`). **OUTSIDE**: liquid-drop saturation. Laptop-scale. Grade: [H].

### Lead 14. **OUTSIDE.** Koide `Q` on the Smith disk: the charged leptons sit near the centre

(a) Statement. KOIDE Theorem 4.1: minimally passive oscillator with `omega = s`, `zeta = h/s`, `zeta^2 = 3Q - 1`; `Q = 2/3` iff critically damped. Taking the root ratio `z = lambda_+/lambda_-` as in lead 9: the centre `Gamma = 0` is critical damping, `Q = 2/3`; the disk exit (`|Gamma| = 1`) is `zeta^2 = 1/2`, `Q = 1/2`; the pole `z = -1` is `zeta = 0`, `Q = 1/3` (the lower limit for positive roots). For `Q < 2/3`, `|Gamma| = sqrt(2 - 3Q)/sqrt(3Q - 1)`. With the PDG values quoted in KOIDE (`Q = 0.6666644634`, `sigma_Q ~ 5.1e-6` from the tau mass), `|Gamma| = 0.0026`, and the tau-mass uncertainty alone moves `1 - zeta^2` by about 1.5e-5, so the measured point is consistent with the centre. This restates Q in his coordinate; KOIDE already says the optimisation is "a conditional variational characterization, not a mass-generation mechanism", and I keep that caveat.
Joins: KOIDE sections 1, 3.1, 4, lead 9.

(b) Why. The two roots of the damped oscillator merge at critical damping.

(c) Kill condition. With a fresh PDG lookup (his rule: research it again each time, masses change), `|Gamma(Q)| > 3 sigma` from zero. Opposite: compute `Gamma(Q)` for other triples (the up-type quarks, neutrino mass triples if a published one is available) and see which sheet each falls on; no claim in advance.

(d) Needs: current lepton masses. **OUTSIDE**: Koide's relation is empirical, not in his corpus as a derived law. Laptop-scale, minutes. Grade: [V]lit if it passes; a reading regardless.

### Lead 15. **OUTSIDE.** Pairing: the BCS occupation is a Smith point, and the window count is not logarithmic

(a) Statement. For a paired level `nu_k = v_k^2 = (1/2)(1 - eps_k/E_k)`, `E_k = sqrt(eps_k^2 + Delta^2)`: `Gamma_k = 1 - 2 nu_k = eps_k/E_k = tanh(s_k)`, `s_k = arsinh(eps_k/Delta)` (checked), so the peel rapidity is `tau = 2 arsinh(eps/Delta)` and the census eigenvalue is `nu(1 - nu) = Delta^2/(4 E_k^2)`. The counting window `nu in [delta, 1 - delta]` is `|eps| <= Delta sinh(ell_delta/2)`, so the window count is `N = 2 rho Delta sinh(ell_delta/2)` for a flat level density `rho`: linear in the gap, with no `ln L`. That is a third census class beside the gapless `L log L` and the gapped logarithmic (MS section 4.1). Nuclear pairing gaps (odd-even staggering) would put a nucleus in this class.
Joins: MD section 1 (bridge), MS section 4.1, VOTKP 15.4 (odd-even staggering enters through `S_2n`).

(b) Why. Algebra of `eps/E`.

(c) Kill condition. For a nucleus with published single-particle levels and a `Delta` from the odd-even mass difference, the window count disagrees with `2 rho Delta sinh(ell/2)` by more than a factor 1.5. Prior art is crowded (the BCS algebra is textbook), which is why this is graded as a reading and flagged.

(d) Needs: single-particle levels and `Delta`. **OUTSIDE**. Laptop-scale. Grade: [H].

### Lead 16. **OUTSIDE.** The anchored sum as a thermal offset: `B_el/kT`

(a) Statement. The offset is `tau = ln[P(empty)/P(full)]` (OFF equation 11). For an atom in an ideal Saha gas the all-empty to all-full odds are `n_bare/n_neutral`, and MD section 8's second combination is `ln(n_0/(n_2 n_e^2 lambda^6)) = (I_0 + I_1)/kT - ln 4`. For element `Z`, `ln(n_0/n_Z)` has slope `B_el = sum_q I_q` in `1/kT`, and VOTKP 20.3.2 reconstructs `B_el` from an anchor plus the peel vector. Reading: the atom's signed offset in a thermal gas is its anchored total binding over `kT` (up to the `n_e`, `lambda` terms, which play the part of the zero), so an anchored peel vector is the offset's slope. Checked against his table: O has `B_el = 2.04384 keV`.
Joins: OFF section 2 (Theorem 2), VOTKP 20.1.3, 20.3.2, MD sections 1, 8.

(b) Why. Ground-state Saha is exact in the model.

(c) Kill condition. In the model, `B_el` read from the slope differs from the anchored sum by more than 1e-9. A trivial pass; the lead is the reading and the extension to the ten ladders (Li to Au) in one table.

(d) Needs: the VOTKP ten ladders (Appendix G) and `s08`. **OUTSIDE** (Saha, IMPORTED). Laptop-scale. Grade: [T] in the model; stays a reproduction note.

### Lead 17. **OUTSIDE.** Band-edge rectifier: the normalised response is flat when `M` is proportional to `L`

(a) Statement. The band_edge note proves `|dR/d omega| <= 2|e^dag (M - R L) u| sqrt(g_omega)/(e^dag L e)` and that `M = cL` gives `R` flat. Read against matter then down: the projector speed `g_omega` of the photonic layer is the intrinsic metric on its projector bundle (not a spacetime metric), and it enters through the same off-diagonal weight as WB's `E_B`. Prediction already registered there (forward calculation frozen 13 Oct 2026): the film-averaged `R` inside the gap is about 0.05 lower for gyromorph than random packings. What belongs in this note: whether the same inequality bounds the rectified output of a *non-Hermitian* (lossy) layer, where `P` is oblique. That is lead 4 applied to a device, so it is the same kill test on an optical model.
Joins: band_edge, WB Proposition 5, lead 4.

(c), (d), (e). Kill condition and data are those of lead 4; laptop-scale; grade [V]. **OUTSIDE** for the optics.

---

## Not pursued, and why

- Redshift test of `Gamma_last` through `alpha` (MS Theorem 1, `alpha` fixed): the closed dictionary predicts exactly zero variation, which agrees with a null, so there is nothing new to check.
- Harmonic-oscillator walls `Gamma = 1/(2N + 4)`: his own result (VOTKP 15.4) is that the oscillator closures carry no ridge, so I left it as a note and did not build on it.
- A lead from OSL's `E_B = k^2/3 = c_s^2 k^2` (NEUT) joining `E_B` to the speed of sound for other gases: this stays in the neutrino strand.

## What would change the ranking

Lead 2 moves to the top if a registered run at unseen parameters reproduces the tower. Lead 4 moves up if a single counterexample is found in minutes. Lead 5 is the safest start because it is mostly bookkeeping on data he already has.
