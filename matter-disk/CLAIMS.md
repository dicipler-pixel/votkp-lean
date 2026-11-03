# Claims ledger

One entry per section, in the order the work was done. Each entry gives the kill condition as it was written before the run, the outcome, and the grade. Nothing here is rewritten later; a later section that changes an earlier one adds its own entry.

Grades: [T] proved, [V] verified numerically with controls, [C] conjecture, [H] reading.

## §1 The bridge (3 Nov 2026)

- Claim: for occupation `ν`, odds `z = (1 − ν)/ν`, `ε = ln z`: `Γ = (z − 1)/(z + 1) = tanh(ε/2) = 1 − 2ν`. Checked to 1.1 × 10⁻¹⁶. [T]
- Claim: `∫ H(ν(ε)) dε = π²/3` over the peel rapidity. 3.2898681336964595 against 3.289868133696453. [T]
- The identity `1 − 2ν = tanh(ε/2)` is standard in entanglement-spectrum work; what is new is the reading as a VOTKP peel step and the counting window as a Smith disk.

## §2 Matter's ladder is a peel ladder (3 Nov 2026)

- Kill condition: on the transverse-field Ising chain the relation `Γ_{j+1} = Γ_j ⊕ tanh(ε₀)` fails by more than the ladder's own uniformity error.
- Outcome: residual 8.0 × 10⁻⁶, 5.5 × 10⁻⁶, 3.2 × 10⁻⁶ at ξ = 20.5, 50.5, 125.5; rapidity spacing error 0.022, 0.011, 0.0062. PASS. [V]
- Caveat: near `|Γ| = 1` the disk compresses differences, so the informative number is the rapidity spacing error.

## §3 Opened matter, non-Hermitian SSH (3 Nov 2026)

- B1 kill condition: at the critical point the levels stay real and inside the disk. Outcome: `|Γ|` reaches about 3.06 and goes complex; Hermitian and gapped controls stay inside. PASS. [V]
- B2 kill condition: no `c ≈ −2` at the critical point, with controls at `c ≈ 1` (Hermitian critical) and `c ≈ 0` (gapped). Instrument note: the von Neumann entropy crossed a logarithm branch (imaginary part 0.26) and read `+1.32`; rejected. Rényi-2 outcome: controls `+1.007`, `0.000`; `v < w`: −1.79 (N = 1000), −1.96 (N = 2000); `v > w`: −0.88, −1.09. [V] on `v < w`; open on `v > w`.
- B3 kill condition: no indefinite metric region near the critical point, with the Hermitian control positive. Instrument note: the first pass failed its own control (rank-one probe plane, roundoff signs); fixed with a rank pre-check. Outcome: closed plane degenerate everywhere; opened plane (u = 0.5) 93% Lorentzian, `(−,−)` in the PT-broken zone; determinant changes sign exactly at v = 0.5 and 1.5. [V]
- Killed: "negative-`c` region = Lorentzian region" (the opened gapped chain is Lorentzian with `c = 0`). Rebuilt: negative `c` sits on the wall where the cone closes.

## §4 Across the Cayley pole (3 Nov 2026)

- `|tanh(W/2)| < 1` iff `|Im W| < π/2`; 0 mismatches on 4000 random complex `z`. A negative ratio has `Im W = π`; `z = −28` gives `Γ = 1.0741` (the ⁵He value of VOTKP §15.4). [T]
- Kill condition: on approach to the critical point the levels leave the disk inside the gapped phase. Instrument note: the unwindowed first pass read `Im W ≈ π` everywhere (levels with `ν = 0` or `1` have meaningless phase); fixed with the window `10⁻⁹ < ν < 1 − 10⁻⁹`. Outcome: KILL fires; exit at v ≈ 0.468 (u = 0.5), identical to 4 digits at blocks 40, 80, 160 and rings 2000, 4000. [V]
- Survives: at every critical point tested (u = 0.2 … 0.7) a level has `Im W = π` exactly. [V]

## §5 The disk-exit law (3 Nov 2026)

- Kill condition 1: the peak Petermann factor is constant along the exit line. Outcome: 80.9, 31.9, 15.7, 8.6, 4.9, 2.4. KILLED.
- Opposite: the band average is 1.99995, 2.00001, 2.00001, 2.00000, 2.00000, 2.00000 at the six exits.
- Kill condition 2: predicted exits from "band average = 2" miss the measured exits by more than 10⁻⁵ at u = 0.25, 0.45, 0.65. Outcome: +4.0 × 10⁻⁸, −1.5 × 10⁻⁹, −3.7 × 10⁻⁸. PASS. [V]
- `K(k) = |q|²/(|q|² − u²) = 1 + u²/E(k)²`, checked to 3.6 × 10⁻¹⁴ on 500 random points; band average `1 + u²/(E(0)E(π))` from `⟨1/(A + B cos k)⟩ = 1/√(A² − B²)`. Hence exit line `E(0)·E(π) = u²`. [T] for the average; [V] for exit ⇔ average = 2.
- One prior-art search (3 Nov 2026) found no statement of this exit law. Nearest: Chang, You, Wen, Ryu, PRR 2, 033069 (2020); arXiv:2406.15564; arXiv:2509.09587.

## §6 Is the exit law universal? (3 Nov 2026)

- General Petermann factor for `h = d·σ`: `K = ½(1 + |d|²/|E|²)`, `E² = d·d`; worst error 1.5 × 10⁻¹³ on 300 random points. [T]
- Kill condition (written before the run): on the band `d = (t₁ + cos k, sin k, m + iγ)`, `⟨K⟩` at the measured exit differs from 2 by more than 10⁻⁴ at any of (t₁, m) = (0.5, 0.4), (1.5, 0.4), (0.5, 0), (1.5, 0.8).
- Outcome: KILL fires. Exits at γ = 0.1691699, 0.1956728, 0.4743416, 0.2518871 with `⟨K⟩` = 1.022352, 1.018838, 2.000000, 1.015041. The only pass is `m = 0`, which is the SSH chain with v = t₁, w = 1, u = γ. Closed controls (γ = 0): real census inside the disk at every setting. [V]
- Size check at (0.5, 0.4): exit γ = 0.169170 at blocks 40, 80, 160 and rings 2000, 4000. The early exit is real. [V]
- Opposite tried: max and mean of `|arg E|`, `max |Im E|/min Re E`, `min Re E`, `min |E|`, `max arg(d_z/E)` at the three massive exits; none is constant. Open.
- Rebuilt: `⟨K⟩ = 2`, equivalently `E(0)E(π) = u²`, is the exit law of the PT-symmetric class; §5's statement is scoped to that class.

## §7 The boundary census on the disk (3 Nov 2026)

- Source of the idea: the 3 Nov 2026 gas review (`Matter_Gases_VOTKP_Deep_Dive_20261103.pdf`). The block identity is standard; what is new is placing it on the disk.
- Kill conditions (written before the run): (a) identity error > 10⁻¹² on 32 random Hermitian contractions; (b) a nonzero boundary count on disconnected sites `C = 0.3 I`; (c) at T = 0 the boundary count differs from the raw count, or `\|Γ_b\|` differs from `\|Γ\|` by > 10⁻⁸; (d) the review's 128-site ring table is missed by > 10⁻⁵ in Tr X_A or mutual information, or by any integer in a count; (e) on the opened SSH chain, `C² ≠ C` or the identity fails by > 10⁻⁸.
- Outcome: (a) 2.8 × 10⁻¹⁶; (b) raw 32, boundary 0; (c) 4 × 10⁻¹⁵; (d) all six rows match; (e) `\|C² − C\|` 9 × 10⁻¹⁵ and 2.8 × 10⁻¹⁴, `\|X_A − C_A(1 − C_A)\|` ≤ 1.3 × 10⁻¹⁴. PASS on all five. [T] identity, [V] numbers.
- Reading: heat moves raw levels to the centre of the disk (raw count 24, then 64), with no correlation across the cut (boundary count 0; innermost `\|Γ_b\|` 0.82, then 0.97).

## §8 A gas carries the peel (3 Nov 2026)

- Model: ideal Saha helium, ground-state weights U = (1, 2, 1), charge neutrality solved (root finder and an independent cubic).
- Kill conditions (written before the run): (a) the review's populations at 10²² m⁻³ are missed by > 10⁻⁶ % at 10, 20, 50 kK, or the 20 kK density sweep misses 0.5680 % and 87.6482 %; (b) `Γ₀` read back from the gas differs from 0.377575066984 by > 10⁻⁹ at any density from 10¹⁸ to 10²⁶ m⁻³; (c) the two solvers disagree by > 10⁻¹².
- Outcome: (a) all match; (b) worst 2.2 × 10⁻¹⁶, with D = 29.830376517 eV and B = 79.005154539 eV at every density; (c) PASS. [T] in the model, [V].
- Scope: exact only for ground-state weights. Excited-state `U(T)` is the opposite test, and it is open.

## §9 The GPT formal edition, checked (3 Nov 2026)

- Source: *Matter, Gases and VOTKP — Formal Research Edition*, 3 Nov 2026, prepared with OpenAI tools for Open Math OS review. It was handed over by Jeromie and is kept unchanged in `external/gpt_formal_20261103/`. The reproduction zip (51 MB) is not committed; its SHA-256 is recorded there.
- Kill conditions for my independent check (written before the run):
  - (1) its endpoint-filter table for the §6 massive exit fails to reproduce at 10⁻⁶, 10⁻⁸, 10⁻⁹, 10⁻¹⁰, 10⁻¹² to 4 digits;
  - (2) its P3 counterexample shows a level leaving {0, 1}, or a band average other than 2;
  - (3) its D5 matrix is not idempotent;
  - (4) 4 Tr X_A > I_G in any of 200 random Gaussian cases;
  - (5) its G9 biased value 0.36614943350748 fails to reproduce to 10⁻¹⁰.
- Outcome:
  - (1) reproduces: 0.271637, 0.271637, 0.169170, 0.169170, 0.122722 (theirs 0.122791 at 10⁻¹², the same 3 digits);
  - (2) block eigenvalues sit within 10⁻¹⁴ of {0, 1}, with ⟨K⟩ = 2.000000;
  - (3) idempotent, Y_A = −2;
  - (4) minimum margin 2.0 × 10⁻³ ≥ 0;
  - (5) 0.36614943350815.
  - Their gas verifier: 18/18 PASS. Their adversarial, Gaussian-information and moment scripts: status PASS.
  - Lean: not rebuilt (no toolchain here). The sources contain no `sorry`. [V]
- What this changes, as an addition (§5 and §6 stay as written):
  - §6's massive exit value is a property of the 10⁻⁹ endpoint filter, not a filter-free threshold.
  - §5's ⟨K⟩ = 2 exit statement needs its coupling and partition assumptions; P3 shows that the average alone does not force an exit.
- Their framing points that I accept:
  - Γ_b equals |1 − 2ν|, not the signed Γ.
  - A zero boundary count at T > 0 does not mean zero cross-boundary correlation (Tr X_A = 0.170835 in the warm ring).
  - For opened (non-Hermitian) matter, the count must use the radial |1 − 4λ|^½, not a real square root.

## §10 His nuclear script, rerun (3 Nov 2026)

- `mass_gaps_smith.py` from the VOTKP v2.9 package was run unchanged on NUBASE2020 via pynucastro. Its output matches §15.4 to every printed digit. [V]

## §11 Is the exit the quarter-turn of the offset? (3 Nov 2026)

- Source: a lead from the matter-downward lead finder (`leads/LEADS_matter_down_v1.md`, lead 1).
- Identity: ⟨K⟩ = 1 + u²/(E(0)E(π)) = sec²(½ Im τ) with Im τ = 2 arctan(u/√(E(0)E(π))). So ⟨K⟩ = 2 ⇔ Im τ = π/2. [T]
- Kill (written before the run): at u = 0.3, 0.5, 0.7 and v at 60/80/95 % of the exit, the gap between the measured census rotation and 2 arctan(u/√(E0 Eπ))/π is not smaller at block 160 than at block 20, or it exceeds 2 × 10⁻³ at block 160.
- Outcome: KILL fires. The gaps are block-independent: +9.8e-3, +2.1e-2 and +3.4e-2 (u = 0.3); +4.9e-3, +8.0e-3 and +6.3e-3 (u = 0.5); about 1e-5 (u = 0.7). The opposite guess 2 arctan(u/E(π)) fails too, as required.
- Follow-up probe (after the run, post hoc): the maximising level often has |Re W| ≈ 15–19, i.e. ν within 10⁻⁷–10⁻⁸ of an endpoint. These are the same filter-sensitive levels as §9.
- Survives: both curves reach a quarter-turn at E(0)E(π) = u².

## §12 The rim distance is exact (3 Nov 2026)

- Kill (written before the run): the identity |Γ| − 1 = 2s/(S_next − s) misses by more than 1e-12 on ⁵He, ⁵Li or ⁸Be.
- Outcome: exact, at 0.074062, 0.220318 and 0.025238. The author's 2s/S_next is the small-s form: 0.071417, 0.198457, 0.024923. [T][V]
