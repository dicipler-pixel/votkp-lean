# L4 — The new maths of the Flock: prior art, the locking hunt, the retarded push

Hand L4, 16 Nov 2026. Everything run lives in `/home/claude/balls/breakdown/scratch/L4/` (each script carries its `// SCRIPT:` or `# SCRIPT:` line, its kill line is in its header, and each run left an `.out` file). The original `/home/claude/balls/w/fl/fl_math_v1.js` was never edited. All edits went into the scratch copy `fl_math_scratch.js` (diff against the original: 23 lines, listed in section 2.1).

Grades used: CHECKED · tolerance (a run, command given), READING (a source read this session), FROM MEMORY (not read this session, check before it goes in the film), HYPOTHESIS and MODEL CHOICE as the plan uses them. Nothing is upgraded.

## 0. Summary in plain words

1. **Prior art.** The Flock sits on four known pieces of physics: Kuramoto oscillators with a delay (Yeung–Strogatz), Huygens clocks sharing a beam, collision models, and input–output theory with delay in waveguide QED. I was allowed three web requests and used three searches. They returned titles and links only, no page text. So what I say about the content of those works is FROM MEMORY, and only the titles and links are READING. The Flock step is exactly a collision model (section 1.3), and its continuum limit is the standard input–output equation (CHECKED, `l4_limit_01.js`).
2. **Locking.** I looked for clocks locking together in the Flock, with and without loss, with an absorbing end, with both signs on the arm–arm faces, with the torque reversed and made stronger, and with the field coupling κ raised to 4. Result: **no locking was found.** Of 1,920 ball pairs with different free rates in 192 z-clock cells, none had measured rates that agreed within 0.02 in both of the last two windows. One equal-clock cell met the kill line; it did not survive four nearby variants, so it is not a lock. The balls do share spectral lines, but those lines are there with the torque off as well, so they are the normal modes of a linear coupled system and not a Kuramoto-type pull. The instrument was checked on a Kuramoto-with-delay system where locking is known; it says LOCKED there and NO LOCK at zero coupling.
3. **The retarded push (K6b).** The rest state is unstable under the retarded push because the push arrives late and nothing carries or books its energy. For two balls the growth rate is the real part of a root of λ = −i a (1 + e^(−λτ)); to first order it is 2a²τ, positive for any delay. The scratch two-ball integrator reproduces that root to 0.2 percent at every delay tried (CHECKED), and the real code's growth rate falls to zero as the delay is cut and stays flat for the two controls (static push, no push). The unstable growth rate of N = 7 at the shipped delays, 0.27 per unit time, matches the original K6b line.
4. A new fact the film should carry: even with no stored history, the field update uses the neighbour's value from the start of the step, so the effective delay is one step longer than the stored one. That is an exact, small effect (section 3.3).

## 1. Prior art for the Flock model

### 1.1 What the three web searches returned (READING of titles only)

| Query (one request each) | Titles and links seen |
|---|---|
| Yeung Strogatz 1999 time delay Kuramoto | "Time Delay in the Kuramoto Model of Coupled Oscillators", arXiv chao-dyn/9807030 (https://arxiv.org/abs/chao-dyn/9807030), Phys. Rev. Lett. 82, 648 (https://www.doi.org/10.1103/PHYSREVLETT.82.648) |
| Huygens clocks, common beam | "Synchronizing Huygens's clocks" arXiv 0802.1024 (https://arxiv.org/pdf/0802.1024); "The rhythm of coupled metronomes" arXiv 1210.3175 (https://arxiv.org/pdf/1210.3175); a Wiesenfeld 2011 PDF at https://schatzlab.gatech.edu/Library/Wiesenfeld2011.pdf |
| time-delayed feedback, waveguide QED, collision models, input–output | "Time-delayed collective dynamics in waveguide QED and bosonic quantum networks", arXiv 2505.02642 (https://arxiv.org/html/2505.02642v2); also arXiv 2110.09362 (no title in the result; I do not name it); Phys. Rev. A 112, 063702 (1 Dec 2025) PDF on dml.riken.jp |

No page was fetched, so no sentence below is READING of content. Each content statement is FROM MEMORY and should be checked against the paper before it goes in the film. Static redshift against Doppler was not searched; it is textbook (section 1.5) and the numbers come from runs.

### 1.2 Kuramoto with delay (Yeung–Strogatz) — FROM MEMORY

- Model: θ̇ᵢ = ωᵢ + (K/N) Σⱼ sin(θⱼ(t − τ) − θᵢ). Delay enters only inside the sine.
- Known result (memory): for identical oscillators the in-phase state runs at a common Ω that solves Ω = ω − K sin(Ωτ); there can be several Ω for one K and τ, some stable and some not; delay can make the incoherent state lose stability at a different K than without delay.
- Control run in this session (CHECKED, `node l4_kura_ctrl_01.js`, output `l4_kura_ctrl_01.out`): three oscillators, ω = (1.0, 1.1, 1.3), K = 3, τ = 0.3, all-to-all. The common rate is 0.5985. The memory formula with ω replaced by the mean 1.1333 gives 0.597; the difference is 0.3 percent. At τ = 1 the common rate is 0.2867. With K = 0 the rates stay at 1.0, 1.1, 1.3. This is a reproduction of a known result and a check of the instrument, not a result of his.
- How the Flock differs: there is no sin(θⱼ − θᵢ) term. A Flock ball's clock is a two-level splitting of fixed size, |dᵢ| = ω·rateᵢ/2 (`fl_math_v1.js:57`, kept by the rotation at `:94-95`, comment "a rotation, so |d_i| is kept"). Coupling is a **linear** exchange of light amplitude through a link of travel time d (`:74-83`). The only nonlinearity is the field turning under the light's spin (step c, `:89-95`). The delay is a travel time of an amplitude, not a delay inside a phase coupling.
- Consequence for locking (derived, then tested in section 2): Kuramoto locking pulls frequencies. Here the ball's own frequency never changes; only the direction of its field changes. The torque does make a ball's spin turn faster in proportion to the light it holds (see 2.5), which is the one amplitude-dependent rate in the model.

### 1.3 Collision models — the Flock step is one — FROM MEMORY, with the structure CHECKED

- A collision model drives an open system by letting it interact in turn with a stream of fresh small pieces of environment, each for a short time. The standard review is Ciccarello, Lorenzo, Giovannetti and Palma (Physics Reports, 2022); I did not read it.
- The Flock port at `fl_math_v1.js:79-80` is that: each step the ball amplitude p and the arriving sample inc are mixed by the rotation [[cos θ, sin θ], [−sin θ, cos θ]] with θ = √(γh); out = sth·p + cth·inc, p ← cth·p − sth·inc. The faces (`:81-82`) are beam-splitters with reflection ρ and transmission τ = √(1 − ρ²).
- CHECKED · 1e-12 (`node l4_unitary_01.js`, `l4_unitary_01.out`): one whole step, built column by column as a matrix from `FL.step`, has max |MᵀM − I| of 6.7e-16 (N = 3, γ = 0.6), 8.9e-16 (N = 3, γ = 2), 2.2e-14 (N = 4), 8.9e-15 (N = 7), and is complex-linear to 0. This is why the books close exactly (the books error over all 384 sweep cells was at most 1.4e-11, including light lost to the absorbing ports).
- CHECKED (`node l4_limit_01.js`, `l4_limit_01.out`): against the closed form of the input–output equation dψ/dt = −i(d·σ)ψ − (γ/2)(ports)ψ − √γ·b_in, the error at t = 0.8 and 1.5 halves every time h halves (ratios 2.014 → 2.001). So the step is **first order in h**, and converges to the continuum equation. The port decay rate is γ/2 + γ²h/12 per amplitude (0.30015 at γ = 0.6, h = 0.005, checked against γ²/12 = 0.0300 to three figures). Note for the film and the page: results at h = 0.005 are correct to about 1 part in a thousand, not better (D at t = 6 changes by 3e-4 to 1e-3 between h = 0.005 and 0.00125 because link lengths are rounded to whole steps).

### 1.4 Input–output theory and waveguide QED with delay — FROM MEMORY

- Input–output theory (Gardiner–Collett 1985) writes a system coupled to a line as dψ/dt = (system) − (γ/2)ψ − √γ b_in, b_out = b_in + √γ ψ. That is the limit equation tested above. It is the standard tool.
- With a round-trip delay the line feeds the output back as input after a travel time, giving delay-differential equations. Papers on this (Pichler–Zoller, Grimsmo, Whalen–Carmichael, atom-in-front-of-a-mirror work; and the 2025 review title seen above, "Time-delayed collective dynamics in waveguide QED and bosonic quantum networks") treat the same structure: emitters separated by a line of length d see each other after time d, with a phase and with collective decay.
- The Flock links are such lines, with the new feature that the line has faces (mirrors of strength Γ = tanh(r/2)) on it and a curved set of lengths from the hyperbolic geometry. The faces on a link make each ball a half-cavity with a mirror at distance r/2: the echo term −ρ·γ·(t − r)·E(t − r) in `l4_limit_01.js` is the standard "atom in front of a mirror" echo. I have not compared numbers with any of these papers. **Prior-art claim not made: that the Flock matches any published waveguide-QED result in numbers.**

### 1.5 Huygens clocks on a common beam — FROM MEMORY

- Two pendulum clocks hung on one beam synchronise (Huygens 1665). The modern account is Bennett, Schatz, Rockwood and Wiesenfeld (Proc. R. Soc. A 458, 563, 2002), with the beam's motion as the coupling; the usual result is anti-phase locking, in-phase for some parameters. The titles listed in 1.1 are of this family. In the Huygens case the beam couples the clocks nearly instantly; there is no travel time on it.
- Why this is the right picture for him and where it stops: a flock of clocks on a beam needs the clocks to **pull each other's rate**, which a pendulum escapement does (the swing amplitude sets a small rate shift). In the Flock, the rate is pulled only through the spin torque (2.5), and the sweep shows it does not pull far enough to merge rates (section 2).

### 1.6 Static redshift against Doppler for the clock ratios

Statement: the Flock gives ball i the rate 1/zᵢ with zᵢ = e^rᵢ (`fl_math_v1.js:39`, `rate:opts.clocks === 'z' ? Math.exp(-rr) : 1`), marked HYPOTHESIS at `:11`.

- Doppler ratio (textbook): light exchanged between two frames with relative rapidity r changes frequency by e^(±r). This is the radar ratio z of the step.
- Time dilation of a clock moving with rapidity r (textbook): its rate against the frame is 1/cosh r. Run: `node -e` with cosh r = (z + 1/z)/2 gives **1.6667, 2.6000, 3.5714** for z = 3, 5, 7 (CHECKED; same numbers as L2 item G12). So the hypothesis picks the signal ratio z, not the dilation ratio cosh r.
- Static (potential) redshift (textbook): clocks that stay at rest at different places in a static field differ by a fixed factor √(g₀₀ ratio), independent of any signal. Round-trip product is 1. A Doppler factor from real recession is not a round-trip-consistent assignment: out and back give e^(2r).
- What the Flock's structure is: a rate is a number attached to each ball (`rate` field, `:39`), so the ratio between two balls is a ratio of two per-ball numbers and any closed loop of ratios multiplies to 1 by construction. That is the structure of a potential, i.e. of the static redshift. The **number** chosen, z = e^r, is the Doppler number. This is a mix, and it is the item REQUIREMENTS lists as not stated by him. The arm–arm ratio the code uses is z_b/z_a (`fl_layer_v1.js:142`, per L2), 5/3 = 1.6667 for B–C at z = (3, 5), whereas the radar ratio of the B–C link itself is e^d with cosh d = cosh r_B · cosh r_C = 4.3333, d = 2.1459, e^d = **8.5497** (CHECKED, same `node -e`). Which of these the clocks should follow is a choice for him; I did not pick.
- Not claimed: that either choice is physically correct for the electron picture.

## 2. The hunt for locking in the Flock

### 2.1 Set-up

- Scratch copy: `scratch/L4/fl_math_scratch.js`. `diff /home/claude/balls/w/fl/fl_math_v1.js scratch/L4/fl_math_scratch.js` shows the only changes: (a) the `require` path; (b) `opts.delayScale` scales the stored delay in the retarded push (`nTot`, line 45 of the original); (c) `opts.gloss`, an extra absorbing port on every ball: ψ ← cos(√(gloss·h))·ψ, the removed light booked in `S.lost`; (d) `opts.sinkBall`, `opts.sinkRate`: the same absorbing port on one ball only (the "absorbing end"); (e) `opts.signSwap`, which flips the sign of the two arm–arm face marks.
- The sign issue (L2 section 4, `fl_math_v1.js:50-51`): as written, the first face on an arm–arm link has ρ = +tanh(r_a/2) and the second −tanh(r_b/2). "Swap" makes them −tanh(r_a/2) and +tanh(r_b/2). Both are run everywhere below. Books close in both (≤ 1.4e-11).
- Scripts: `l4_sync_02.js` (one run per call; measures); `run_sweep2.py` with `jobs2.txt` (384 cells, `sweep2.jsonl`); `l4_read_02.py` (applies the kill lines). The earlier `l4_sync_01.js` sweep (`sweep.jsonl`, 108 cells, sign as written) is reproduced exactly: all 108 rows match `sweep2.jsonl`, largest |r difference| 0.0 (`python3 l4_tag_summary_02.py`).

### 2.2 What is measured and why it decides

- **Rate test.** Each ball's clock phase is the angle of its light spin about its own field (`FL.clockPhase`, `fl_math_v1.js:110-112`). Its slope over a window is the ball's measured clock rate. Why this decides the point: locked clocks run at one common rate (or a fixed whole-number ratio) that differs from their free rates, window after window; unlocked clocks keep their own rates or wander. The kura control (1.2) shows the test saying LOCKED where a lock exists and NO LOCK at K = 0.
- **Weights.** A ball that holds almost no light has no meaningful phase, so the second kill line demands weight > 0.02 for half the samples.
- **r and its control.** The Kuramoto order parameter r (`FL.order`, `:114`) is weighted by how much each ball swings. When one ball holds almost all the light, r is near 1 for no reason. So r is compared with 300 surrogates in which each ball's phase series is shifted in time by its own random amount.
- **A frame-free second eye.** `FL.clockPhase` is measured in a frame tied to the ball field, which turns when the torque is on. `l4_iso_01.js` shows the effect: with torque 1, ball D's spin turns about its conserved axis at 1.039969 (the predicted |J| = 1.040016, CHECKED) but the slope of `FL.clockPhase` is −0.013435; the frame of the readout hid the turning. So in torque-on cells the rate test is weakened. The torque-0 cells (field fixed) are clean. For that reason the spectrum of each ball's amplitude along the up and down states of its **rest** field was added as a frame-free eye (peak frequency ν_up, ν_dn over the last half).
- **Kill lines**, written before the runs (verbatim in the headers of `l4_sync_01.js` and `l4_sync_02.js`):
  - Line 1: a pair is LOCKED only if its measured rates agree within 0.01·ω = 0.02 in both of the last two windows AND (z clocks) their free rates differ by more than 0.02, or (equal clocks) the phase-difference s.d. is < 0.5 rad with torque on while > 0.5 rad in the matching torque-off run.
  - Line 2 (written after the first sweep showed weights near 1e-4 in some balls): AND both balls weight > 0.02 for at least half the samples AND r exceeds the surrogate mean by more than 3 surrogate s.d.

### 2.3 The sweep (384 cells, T = 400, h = 0.005, kick in ball A)

Command: `python3 run_sweep2.py` (reads `jobs2.txt`), then `python3 l4_read_02.py` (`l4_read_02.out`).

Cells: N = 3, 4, 7; clocks z and equal; torque 0 and 1; γ = 0.1, 0.3, 0.6, 1, 2 with loss gloss = 0, 0.05, 0.3 at selected γ (the 108-row grid from `jobs.txt`); both signs (216 cells). Then the opposite runs, both signs, N = 3, 4, 7, both clock types, γ = 0.3 and 1: torque −1 (24 cells); κ = 1 and κ = 4 (48 cells); the absorbing end with sink rate 0.5 and 2 on ball A and on the last ball (96 cells).

Results (CHECKED · reproduction to 0.0 on the 108 old rows; every number from `l4_read_02.out`, `l4_tag_summary_02.out`, `l4_zagree_02.out`):
- z-clock cells: 192. Pairs with different free rates: 1,920. **Pairs whose measured rates agree within 0.02 in both windows: 0.** (`python3` one-liner saved in `l4_zagree_02.out`.) This includes torque 0, where the readout frame is clean.
- Cells that meet kill line 1 on some pair: 1 of 384. Cells called LOCKED by kill line 2: 1 of 384. That cell is N = 7, clocks equal, torque 1, γ = 0.1, **sign swap**, pair (2, 5) = balls C and F, the +J and −J arm balls. They are mirror images of each other, which already suggests symmetry as the reason. Not the sign as written.
- Follow-up, kill line written first (`python3 l4_lock_followup_01.py`, `l4_lock_followup_01.out`): the call stands only if the pair meets the line in at least 3 of 4 variants (T = 800; γ = 0.08; γ = 0.12; kick in ball D). Result: **0 of 4** for the swapped sign and 0 of 4 for the sign as written. In the original cell the phase difference of C and F has s.d. 0.244 rad with torque on and 5.559 with torque off; at γ = 0.08 it is 8.2, at γ = 0.12 it is 2.2, with the kick in D it is 6.6. So that is one cell, not a lock. Not killed as a possibility: a lock of the mirror pair at some narrow setting I did not scan; I report only that this cell did not hold under neighbours.
- Loss and absorbing end: in the 96 gloss cells and the 96 sink cells the light left at t = 400 is between 0.019 and 0.859 (median 0.117); the survivors are not locked by the rate test. A loss that drains the faster-decaying modes leaves the slowest-decaying one, which would show as one common line; see 2.4 for what the spectrum says.
- Opposite runs (reverse torque, κ up to 4, sinks, big torque): no cell is locked.
- **r.** Cells with at least two heavy balls: with sign as written, r exceeds surrogate + 3 s.d. in 3 of 59 cells (0 of 19 at torque 0); with the swapped sign, in 12 of 51 (4 of 16 at torque 0) (`l4_rexcess_02.out`). Median excess is 1.3 to 2.7 surrogate s.d. in every group. So r is not 1 in a meaningful way anywhere; the weighted r of 0.9 or more seen in many cells is one ball holding the light (the surrogate gives 0.96 there). The swap raises r above the shuffled value more often than the sign as written, even at torque 0 (linear), which is a sign-dependent mixing of phases, not locking. **The surrogate shifts weights with phases and so breaks the time correlation of weights across balls; the excess it shows is therefore a loose upper bound on phase ties.** In 133 of 384 cells r is above the surrogate by 3 s.d., but in 71 of those no ball is heavy, so the excess there carries nothing.

### 2.4 The opposite of "no lock": do the balls share lines?

Kill line written first (headers of each script): see `l4_spec_02.py`, `l4_spec_03.py`, `l4_spec_04.py`.
- `python3 l4_spec_02.py`: among heavy unequal-free-rate pairs in z cells, the peaks of ν_up and ν_dn coincide within 0.03 (about the window resolution) in 59 of 216 comparisons (27.3 percent) against 2.75 percent for random pairing across cells (ratio 9.9). Under the written kill line: shared lines exist.
- `python3 l4_spec_03.py`: of the 59, 57 are more than 0.1 from both balls' own free lines (±free/2). So the shared lines are real shared frequencies that neither ball has alone.
- `python3 l4_spec_04.py`: the same count split by torque: 39.1 percent at torque 0 (18 of 46), 25.0 percent at torque 1 (33 of 132), 21.1 percent at torque −1. Kill line: "linear mixing if the torque-0 fraction is at least half the torque-1 fraction" — it is 1.6 times larger. So the shared lines are present with the field fixed: they are the normal modes of the flock as a linear unitary system (the eigenmodes of the coupled balls and links), which appear in every ball that takes part. This is a **reproduction** of ordinary coupled-mode physics, not a rate pull. The rate test says the rates do not merge because several modes are populated at once and their beating moves the phase of each ball.
- Reading of the two eyes together: the Flock shows shared mode lines (hybridisation) and no clock locking. If the film wants to say "the balls hum together", the honest sentence is "they share modes". Whether a single mode can be made to dominate (all balls on one line) is the case I did not hunt for by design of the kick; it is the natural next test, and it would be a mode selection, not a Kuramoto lock.

### 2.5 The opposite of weak coupling: strong torque

`python3 l4_torque_big_01.py` (`l4_torque_big_01.out`). `l4_iso_01.js` shows why this is the place a lock could come from: a ball holding all the light turns its spin at |J| = √((ω·rate)² + torque²) (CHECKED · 1e-3 against the measured turning rate: A 2.236045 against 2.236068; B 1.201844 against 1.201850; C 1.077024 against 1.077033; D 1.039969 against 1.040016). The rates of the four balls move from 2, 0.667, 0.4, 0.286 at torque 0 to 2.236, 1.202, 1.077, 1.040 at torque 1: the spread shrinks from about 7 to 1 down to about 2 to 1. At large torque all balls would approach one rate, so this is the one place a rate-merging mechanism exists, and it is a self-pull by the light a ball holds, not a coupling between balls. Runs at torque 3 and 10, γ = 0, 0.3, 1, both signs (12 runs): no pair has gaps below 0.02 in both windows; the smallest in a pair of heavy balls is 0.015 in a single window (swap, torque 3, γ = 1, balls B–C), not in both. So strong torque narrows the spread of a ball's spin rate when it holds the light, but the Flock's balls do not hold the same amount of light at the same time, so they do not merge. With the links closed (γ = 0) one ball holds all the light and the other readouts are not defined.

### 2.6 What this does and does not say

- It says: in the model as built (z or equal clocks, N up to 7, γ 0.1–2, κ 0.25–4, torque −1 to 10, loss and sinks, both face signs, kick in A), no pair of clocks locked in rate. Within 3 s.d. of shuffled phases there is no order beyond what one dominant ball gives.
- It does not say: that no locking exists anywhere in the model. Not scanned: kicks in other balls except one variant, a driven flock (a source feeding a link continuously), N > 7, and a spectral lock with a single dominating mode. Nothing here has been tried with the retarded push, which is unstable (section 3), or with the push at `static` replaced by any other.
- **Repair route, not run:** if he wants a locking flock, the Kuramoto structure says a rate pull needs an amplitude-dependent frequency in the ball (the torque gives one) and enough shared light between balls at the same time. A driven flock, where a source holds light in all balls at once, is the setting with that property. HYPOTHESIS, untested.

## 3. Why the retarded face push is unstable (K6b)

### 3.1 What the code does and what the check saw

- `fl_math_v1.js:93`: with push `retarded` the face push uses `hist` = ball j's field as it was `nTot` steps ago (the link travel time, rounded, `:45`). Header lines 15-17: "No field carries that push, so its energy is not booked, and FL-CHECK-01 finds the rest state unstable under it (delay instability). Kept for exploring only."
- `fl_check_01.js:44` and `fl_check_01.out:13`: N = 7, no light, largest field turn: 2.5e-7 at t = 25, 2.3e-4 at t = 50, 2.2e-1 at t = 75, 2.3 at t = 100. The turn grows by a factor of 920 from t = 25 to 50 and of 957 from t = 50 to 75, i.e. ln(920)/25 = 0.273 and ln(957)/25 = 0.274 per unit time: clean exponential growth at about 0.27 per unit time (arithmetic on the four printed values).

### 3.2 The explanation, derived by hand

Setting: two balls with equal fields |d| = D along z, R = identity, no light. Write a small transverse tilt of ball i as the complex number δᵢ = x + i y. Step (c) rotates d about G = 2κ(dᵢ − dⱼ(t − τ)) (`:93-95`, k2 = 2κ). To first order:
δᵢ′ = −i a (δᵢ − δⱼ(t − τ)),  a = 2κD.
- Both tilt together (δ₁ = δ₂ = δ): δ′ = −i a (δ(t) − δ(t − τ)). λ = 0 is a root: the pair turns rigidly, nothing grows.
- Opposite tilts (δ₁ = −δ₂ = δ): δ′ = −i a (δ(t) + δ(t − τ)); characteristic equation λ = −i a (1 + e^(−λτ)).
  - τ = 0: λ = −2 i a. Pure precession at frequency 2a, no growth. That is the static push: the pair is a stable (neutral) precessing system.
  - Small τ: set λ = −2ia + ε. Then ε ≈ −i a (e^(2iaτ) − 1) ≈ 2a²τ. **The real part of λ is positive for any positive delay.**
- Plain words: the push on ball i is toward where ball j was a moment ago. A precessing pair is always being pushed by a partner that is slightly behind in its turn, so each pushes the other along its own direction of motion and gives it energy. Nothing pays for that energy because the push is not carried by a field. For large τ the growth saturates (Re λ = 0.2715 at τ = 2 for a = 0.5, `l4_k6b_01.out`).

### 3.3 Tests (kill lines written before each run, in the script headers)

`node l4_k6b_01.js` (`l4_k6b_01.out`), then `node l4_k6b_02.js` (`l4_k6b_02.out`).
- **Part A, the formula against a standalone two-ball integrator** with the same rotation update as `:94-95` and the same read-before-write ring buffer as `:93, 96`. Kill line A: rate within 5 percent of the root of the characteristic equation (found by Newton iteration), and zero growth at no delay. Result: **killed at n = 0 and n = 10** (measured 2.5e-3 at τ = 0 where 0 was predicted; 2.741e-2 at τ = 0.05 where 2.493e-2 was predicted), agreeing at n = 20 to 200. This is not hidden: it is what the run said.
- **Repair of A, derived then tested** (`l4_k6b_02.js`): the field update builds all new fields from the old ones (`:92-95`, `nd` from `S.d`, then `S.d = nd`), so even with no stored history the neighbour's value is one step old. Effective delay is (n + 1)·h. Prediction made before the run: rate = Re λ at τ = (n + 1)h; at n = 0 about 2a²h, so halving h halves the rate. Kill line A′: within 3 percent. Result (CHECKED · 0.2 percent): n = 0, h = 0.005: predicted 2.4999e-3, measured 2.5000e-3; n = 10: 2.7403e-2 against 2.7406e-2; n = 40: 9.7816e-2 against 9.7894e-2; n = 200: 0.26772 against 0.26821; n = 0, h = 0.01: 4.9994e-3 against 4.9997e-3; n = 0, h = 0.0025: 1.2500e-3 against 1.2500e-3.
- **Part B, the cause inside the real code** (scratch copy, delay scaled by `delayScale`, tilt of 1e-6 on every field, no light, kill line B: delay explanation killed if the rate at delayScale 0.05 exceeds half the rate at 1, or if the rate is not non-decreasing over 0.05 to 0.5). Growth rates per unit time (N = 3 / N = 7): delayScale 0.05: 0.0173 / 0.0328; 0.1: 0.0332 / 0.0594; 0.25: 0.0756 / 0.1295; 0.5: 0.1248 / 0.2104; 1: 0.1601 / 0.2718; 2: 0.1451 / 0.2447. At 0.02 (delays 0.02–0.06) no growth window was reached in the run. Kill line B not met (0.0173 < 0.0800; 0.0328 < 0.1359; monotone on 0.05 to 0.5). The shipped delays (delayScale 1) give 0.2718 for N = 7, the same as the 0.27 in the original K6b line.
- **Controls under the same tilt:** push `static`: largest tilt over t = 200 is 9.2e-7 (N = 3), 2.2e-6 (N = 7); push `off`: 8.1e-7. No growth, as required. The delay is the cause; the static push is the repair already in the code.
- Not tested: whether a retarded push carried by a field on the link (so that its energy is booked, which the header says is missing) would be stable. HYPOTHESIS, untested. That is the smallest honest repair if he wants the push retarded; the present default (`static`) is a MODEL CHOICE already labelled as such.

## 4. Where source and code do not match, or what to carry

1. The arm–arm face sign (L2 section 4, `fl_math_v1.js:50-51`) is open until he chooses. This hunt shows the choice does not change the answer to the locking question (no lock either way) but does change r above its shuffled value (3 of 59 against 12 of 51 cells) and the shares, as L2 found.
2. The clock readout `FL.clockPhase` (`:110-112`) measures in a frame tied to the field. With the torque on it can hide the true turning (ball D: slope −0.013 against turning 1.04, `l4_iso_01.out`). The page that shows "clock phases" for torque-on cells should say so or use the frame-free line.
3. The hypothesis "ratio z" uses the Doppler number inside a structure that is a potential (1.6). Open, his choice.
4. The step is first order in h (1.3). The page's quoted numbers are right to about 1e-3 at h = 0.005.
5. With the retarded push the real delay is the link time rounded to whole steps plus one step (3.3).

## 5. Open or not claimed

- Prior art: no content of any paper was read this session; every content statement in section 1 is FROM MEMORY. No claim that the Flock reproduces a published delay result.
- Locking: not scanned are a driven flock, N > 7, kicks in other balls (one variant only), unequal z per arm in N = 7, and single-mode selection. The one cell that met the kill line is a mirror pair that did not survive variants.
- The shared mode lines are a reproduction of linear coupled-mode physics. They are not a result of his and not a lock.
- No physical claim that the clock ratio z is right (HYPOTHESIS stands).

## 6. Picture ideas for the film

1. **Two clocks on a beam, a slider for the delay.** Two clocks tick at different speeds. Draw a travelling wave between them. A slider for τ moves the common rate (the Kuramoto control: 1.1333 → 0.5985 at τ = 0.3 → 0.2867 at τ = 1). Then the Flock's balls on the same slider: the readout shows each ball's own rate stays put. Number on screen: "pairs locked: 0 of 1920".
2. **Three bars that refuse to meet.** Bars for the free rates 2, 0.667, 0.4 and a dot on each showing the measured rate over time. In the Kuramoto control the dots slide into one bar; in the Flock they wander near their own. Switch the two arm–arm face signs and show the same result both ways.
3. **The comb of shared lines.** Each ball's spectrum as a row of peaks; shared peaks are joined by a thin line. Turn the torque off and the same lines stay. Number: 27 percent of heavy pairs share a line, against 2.75 percent by chance. Caption: the balls share modes, they do not lock.
4. **The push that listens to old news.** Two field arrows precess; a ghost arrow shows where the partner was τ ago. A slider for τ makes the pair's tilt grow like a spiral: growth 2a²τ; the static push beside it stays still. Numbers: 0.27 per unit time at the shipped delays; none for the static push.
5. **A stream of small collisions.** The ball sits at a bank of beam splitters; one small amplitude θ = √(γh) = 0.0548 leaves per tick. Show the light count falling at γ/2 per port in the limit, and the books staying at 1 in the balls plus the links (error 1e-11).
6. **A ruler of three clock numbers.** For z = 3, 5, 7 mark z (3, 5, 7), cosh r (1.667, 2.6, 3.571) and for the B–C link e^d = 8.55 against the Flock's 5/3 = 1.667. A loop of two balls shows that a per-ball rate always closes the loop (round trip 1) while a Doppler recession does not (e^(2r)).

## 7. Commands, in one place

All from `/home/claude/balls/breakdown/scratch/L4/`:
`node l4_unitary_01.js` · `node l4_limit_01.js` · `node l4_iso_01.js` · `node l4_kura_ctrl_01.js` · `python3 run_sweep2.py` (reads `jobs2.txt`) · `python3 l4_read_02.py` · `python3 l4_tag_summary_02.py` · `python3 l4_rexcess_02.py` was a heredoc, saved in `l4_rexcess_02.out` with its header · `python3 l4_lock_followup_01.py` · `python3 l4_spec_02.py` · `python3 l4_spec_03.py` · `python3 l4_spec_04.py` · `python3 l4_torque_big_01.py` · `node l4_k6b_01.js` · `node l4_k6b_02.js`. Earlier SYNC-01 sweep: `sweep.jsonl` from `jobs.txt`. A sweep cell: `node l4_sync_02.js '{"N":3,"clocks":"z","torque":1,"gamma":0.3,"gloss":0,"sign":"asis","T":400,"h":0.005}'`.
