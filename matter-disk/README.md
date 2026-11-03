# Matter on the Smith disk: where closed matter ends and opened matter begins

Jeromie Beasley. Working record, started 3 November 2026. Made with AI assistance (see [`AI_USE.md`](AI_USE.md)).

**Read [`PROVENANCE.md`](PROVENANCE.md) first.** Every section is tagged there as MINE, MINE ON A TEST BED or IMPORTED, and only MINE sections count as findings.

This folder is the growing home of one line of work. It joins three of my papers:

- *Matter at a Scale* (August 2026): matter has no absolute size; the only place scale returns is a logarithmic boundary count with coefficient `A = 2c/π²`, where `c` is the central charge.
- *VOTKP: The Vector of Traits Kept under Peeling* (v2.9, 13 October 2026, [10.5281/zenodo.23340757](https://doi.org/10.5281/zenodo.23340757)): each peel step becomes the Smith coordinate `Γ = (z − 1)/(z + 1)`; bound steps sit inside the unit disk, steps add like velocities, and the unbound nuclei ⁵He, ⁵Li, ⁸Be sit outside it (§15.4).
- *A Measured Lorentzian Cone in Non-Hermitian Quantum Geometry* (August 2026): opening a system (non-Hermitian generator) can turn the geometry of its states Lorentzian; at a Hermitian point it never does.

It is a working record, not a finished paper. Every claim carries a grade, and every number comes from a script in [`scripts/`](scripts/) whose output is kept in [`outputs/`](outputs/). It is not part of the Lean build.

## Sections

| § | What it does | Grade | Scripts |
| :-: | :--- | :-: | :--- |
| 1 | **The bridge.** A boundary-count level with occupation `ν` has odds `z = (1 − ν)/ν`, and its Smith coordinate is `Γ = tanh(ε/2) = 1 − 2ν`, where `ε = ln z`. The counting window `ν ∈ [δ, 1 − δ]` is the Smith disk `\|Γ\| ≤ 1 − 2δ`. The binary entropy integrated over the peel rapidity is `π²/3`. | [T] (identity standard; reading new) | `s01_bridge.py` |
| 2 | **Matter's ladder is a peel ladder.** On the transverse-field Ising chain (c = ½), consecutive levels differ by one constant peel step under `⊕` (VOTKP Theorem 15.1); the rapidity spacing error falls 0.022, 0.011, 0.006 as ξ grows. | [V] | `s02_ladder.py` |
| 3 | **Opened matter.** Non-Hermitian SSH chain `h(k) = [[iu, q̄],[q, −iu]]`, `q = v + w e^{ik}`. Closed: Γ real. Opened and gapped: Γ complex, inside the disk. At the critical point `\|v − w\| = u`: Γ leaves the disk (`\|Γ\|` ≈ 3). Rényi-2 central charge: −1.79 → −1.96 on the `v < w` side (literature: −2); −0.88 → −1.09 on `v > w`, not converged. Band metric: Lorentzian over 93% of the opened plane, `(−,−)` in the PT-broken zone, signature change exactly at the critical points; the closed plane is degenerate. | [V] / open | `s03*` |
| 4 | **Across the Cayley pole.** With `Γ = tanh(W/2)`, `W = ln z`: `\|Γ\| < 1` iff `\|Im W\| < π/2`; a negative ratio has `Im W = π`. At every opened critical point tested (u = 0.2 … 0.7) a level sits at exactly `Im W = π`, the signature of the unbound nuclei in VOTKP §15.4. | [T] + [V] | `s04*` |
| 5 | **The disk-exit law.** The levels leave the disk where the band-averaged Petermann factor equals 2. For this chain the Petermann factor is `K(k) = 1 + u²/E(k)²` and its band average is `1 + u²/(E(0)E(π))`, so the exit line is `E(0)·E(π) = u²`. Predicted at three unseen `u` and measured to within 4 × 10⁻⁸. | [T] for the average; [V] for exit ⇔ average = 2 | `s05*` |
| 6 | **Is the exit law universal?** Second band: the cone paper's family in one dimension, `d = (t₁ + cos k, sin k, m + iγ)`. The general Petermann factor is `K = ½(1 + \|d\|²/\|E\|²)` (exact). With no mass (`m = 0`, the SSH class) the exit is again at `⟨K⟩ = 2.000000`. With a mass term the census leaves the disk much earlier, at `⟨K⟩` ≈ 1.015–1.022, and the exit does not move under a fourfold larger block. So `E(0)E(π) = u²` is the law of the PT-symmetric class, not of all opened bands; what sets the massive exit is open. | [T] for K; [V]; open | `s06_second_model_exit_law.py` |
| 7 | **The boundary census on the disk.** Split a one-body correlation matrix at a cut: `C_A − C_A² = (C − C²)_A + X_A`, `X_A = C_AB C_BA`. In a pure state the eigenvalues of `X_A` are `ν(1 − ν) = (1 − Γ²)/4`, so the boundary coordinate `Γ_b = √(1 − 4λ)` is the same disk point as `\|Γ\|` and the count is the §1 window. Heat pulls raw levels to the centre with nothing crossing the cut; `Γ_b` sends them back to the rim. Disconnected sites: raw count 32, boundary 0. The 128-site ring table of the 3 Nov gas review is reproduced to every printed digit. On the opened chain the biorthogonal `C` is still idempotent (10⁻¹⁴), so §§4–6 carry over to the boundary census unchanged. | [T] identity; [V] | `s07_boundary_census_disk.py` |
| 8 | **A gas carries the peel.** Helium in an ideal Saha gas, with the VOTKP v2.9 ladder (24.587389011, 54.4177655282 eV). Each adjacent charge pair is a disk point `Γ_pop = tanh(½ ln n_q/n_{q+1})` that sweeps the whole diameter as temperature and density change. Two combinations lose density exactly: `ln(n₀n₂/n₁²) = −(I₁ − I₀)/kT − ln 4` and `ln(n₀/(n₂ n_e² λ⁶)) = (I₀ + I₁)/kT − ln 4`. Their temperature slopes return `Γ₀ = 0.377575066984` to 2 × 10⁻¹⁶ while the neutral fraction runs from 10⁻⁵ % to 82 %. The review's population table is reproduced. Model statement (ideal gas, ground-state weights only), not a new measurement. | [T] in the model; [V] | `s08_gas_carries_the_peel.py`, `fig02_boundary_and_gas.py` |
| 9 | **GPT formal edition, checked.** The 3 Nov *Matter, Gases and VOTKP* formal edition (prepared with OpenAI tools, 58 pp, 34 Lean theorems) is kept in [`external/gpt_formal_20261103/`](external/gpt_formal_20261103/). I reran its new claims independently. **The §6 massive-band exit depends on the endpoint filter**: γ = 0.27164 at filters 10⁻⁶ and 10⁻⁸, 0.16917 at 10⁻⁹ and 10⁻¹⁰, and 0.12272 at 10⁻¹². The massless exit (0.47434) is stable through 10⁻⁸ and moves to 0.47412 at 10⁻¹². So the §6 number 0.1691699 belongs to the 10⁻⁹ filter, not to the band. Its counterexample P3 also checks: with w = 0 and v² = 2u², ⟨K⟩ = 2 but no level leaves {0, 1}. So ⟨K⟩ = 2 alone cannot be the exit law. The idempotent D5, the information bound 4 Tr X_A ≤ I_G (200 random cases) and the partition-bias number of G9 all reproduce. The package's gas verifier passes 18/18. The 34 Lean theorems were **not** rebuilt here, because there is no toolchain. | IMPORTED; [V] reruns | `s09_check_gpt_formal.py` |
| 10 | **His nuclear script, rerun.** VOTKP's `mass_gaps_smith.py` was rerun on NUBASE2020 (via pynucastro). ⁵He 1.074, ⁵Li 1.220, ⁸Be 1.025; ⁷Li 0.123 and ⁴He 0.579 inside. Every printed digit matches §15.4. | [V] (his script) | `s10_nuclear_gaps_his_script.py` |
| 11 | **Is the exit the quarter-turn of the offset?** (lead-finder lead 1) Continuing the offset closed form gives Im τ = 2 arctan(u/√(E(0)E(π))), and ⟨K⟩ = sec²(Im τ/2) exactly, so ⟨K⟩ = 2 is the same statement as Im τ = π/2. **Killed as a description of the census rotation away from the exit.** The measured rotation sits 4×10⁻⁶ to 3.4×10⁻² above the formula, and the gap does not change with block size. The top-rotation level is often a near-endpoint level (\|Re W\| ≈ 15–19, ν ≈ 10⁻⁷–10⁻⁸), the same levels the §9 filter result exposed. What survives: the formula and the census both cross a quarter-turn at E(0)E(π) = u² (§5). | killed as stated; [T] for the identity ⟨K⟩ = sec² | `s11_exit_quarter_turn.py` |
| 12 | **The rim distance is exact.** For an unbound step, \|Γ\| − 1 = 2s/(S_next − s), where s = −S_first. VOTKP's "close to twice the decay energy over the neighbouring step" is its small-s form, 2s/S_next. The Cayley pole z = −1 is S_first + S_next = 0. | [T]; [V] on the three gap nuclei | `s12_nuclear_rim_identity.py` |

Grades: [T] proved, [V] verified numerically with controls, [C] conjecture, [H] reading.

## What is killed, and what replaced it

Kill conditions are written before each run. These are recorded in [`CLAIMS.md`](CLAIMS.md):

- "The negative-`c` region is the Lorentzian region." Killed: the opened gapped chain is Lorentzian with `c = 0`. Rebuilt: negative `c` sits on the wall where the cone closes.
- "The levels leave the disk at the critical point." Killed: they leave earlier, inside the gapped phase, with no change under a fourfold larger block. Rebuilt: a quarter turn marks the exit line `E(0)E(π) = u²`; a half turn marks the critical point.
- "The exit is set by the peak Petermann factor." Killed: 81 down to 2.4 along the line. Rebuilt: the band average, exactly 2.
- "`⟨K⟩ = 2` is the exit law for every opened two-band chain." Killed on the massive band (§6). Rebuilt: it is the law of the PT-symmetric (massless) class.

## Open

- Why the census crosses a quarter-turn at E(0)E(π) = u² while its rotation away from the exit is not the offset closed form (§11); the near-endpoint levels need conditioned (high-precision) eigenvalues.

- A proof that the block levels leave the disk exactly when the band-averaged Petermann factor reaches 2.
- The exit law for bands with a mass term (§6): what is constant at their exit? Since §9 the question needs a filter-independent definition of the exit first (endpoint filter, ring and block sizes, and the order of limits).
- §5's law needs its coupling and partition assumptions stated (§9, counterexample P3 at w = 0).
- A second non-unitary model of a different kind (Yang–Lee) for every section.
- Convergence on the `v > w` side of the critical point (§3).
- §8 with excited-state partition functions `U(T)`: how far does the read-back `Γ₀` move? (The opposite test of §8.)
- Gas as opened matter: the kinetic generator `L = −νQ − ikM` is non-normal; place its modes on the disk and test the §5 exit law there.
- Xe 4d channel pair (Zhong et al., Nat. Commun. 11, 5042, 2020): the two-channel amplitude ratio is a complex `z`, so its rotation is a phase. Needs the publisher source data locally.
- Nuclear resonances placed by rotation from published energies and widths (the particle-side step).
- Matter v5: the 3 Nov review reports an extra leading minus in the §5 derivative `dΔ/dlog₁₀C`, and a factor-two open question in the doubled (BdG) versus physical Majorana census counting. Both are noted here and still need checking against the paper's own text.

## Adding a section

Each new piece of work gets the next number `§n`: scripts named `sNN*_*.py`, each carrying `# SCRIPT: NAME` and its kill condition in the header; the verbatim output in `outputs/`; one row in the table above; one entry in `CLAIMS.md`; and its provenance tag in `PROVENANCE.md`. Nothing earlier is rewritten. A section that changes an earlier one says so in its own row.

## Run

```bash
cd scripts
python3 s01_bridge.py      # and so on; numpy, scipy, matplotlib
```

`s03d` writes the signature map that `fig01_signature_and_disk.py` draws.
