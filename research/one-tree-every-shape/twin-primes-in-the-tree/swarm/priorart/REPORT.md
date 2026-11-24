# Swarm 5 — prior art and framework fit (twin-chain frame turn)

Jeromie Beasley · swarm notes · 24 November 2026
Script: ce_turn.py (TWIN-TURN-CONNECTION-ENERGY-01). Grades: cited (opened), search-only, standard, derived, checked, hypothesis.

## Novelty
- Not found anywhere: the twin chain walked as boosts with rapidity ln(a_{n+1}/a_n), the law d − L/√3 → 0.109, the frame turn near 12.27°, or any holonomy constant built from the primes.
- Closest work: Sahoo arXiv:2111.09053 (cited). Twin primes by residue class; consecutive pairs prefer to switch class mod 4; plain counts, no gap weighting, no geometry.
- End-digit avoidance is the twin version of Lemke Oliver–Soundararajan, PNAS 2016, arXiv:1603.03720 (search-only). Holt arXiv:2405.03540 (cited): such biases are transient but outlast computable range.
- Prime walks: Fraile et al. arXiv:2105.12547 and arXiv:2506.15357 (cited). Last digit sets the direction on a flat unit-step grid: no curvature, no frame.
- Thomas–Wigner rotation as holonomy: Palge–Pfeifer arXiv:2310.08121 (cited); Rhodes–Semon gr-qc/0501070. Decreasing deterministic rapidities with a converging frame: not found.
- Benaïm 1999, Sém. Prob. XXXIII (search-only), covers the heading flow on the sphere (Step 3). The frame integral (Step 5) goes beyond it.

## Residues and what is proved
- Exact (derived): twin starts above 5 are ≡ 11, 17, 29 (mod 30), one class per end digit 1, 7, 9. The three arms are exactly these classes.
- Unconditional:
  - Sieve upper bounds per class only (standard).
  - No lower bound in any class.
  - No Bombieri–Vinogradov theorem for twin primes.
  - Banks–Freiberg–Turnage-Butterbaugh, Acta Arith. 167 (2015), cover bounded-gap runs of ordinary primes in one class, not twins.
- Σ r_n² is not known to converge unconditionally (derived). It would follow if twin gaps were O(a^θ) with θ < 1, which is unproved.

## Flag on H3 (derived, untested)
- Under Hardy–Littlewood the gap-weighted tilt is about c/L². Its tail is then about 1/L, the borderline, so H3 with fixed weights fails at exactly that edge.
- Repair (H3'): split ξ_n = r_n δ(L_n) + η_n with ∫|δ| dL < ∞.
  - The drift part enters the frame sum absolutely convergently.
  - Only the fluctuation η needs the O(L^{−1−δ}) tail.
- The line "turn does not converge ⇒ infinitely many twins" is true but carries no leverage: non-convergence of any sequence implies it is infinite.

## Framework map
- **The turn is curvature (derived).** One-step Wigner angle r sin θ tanh(d/2) = area of the thin triangle (origin, walker, next walker) on rapidity space H³ (curvature −1). The total turn is the holonomy of the loop: origin → chain → geodesic back. Rapidity space bends; the twin primes choose the loop.
- **Projector bundle, option 8 (derived).**
  - L = P U.
  - ρ = LL*/tr = ½(I + tanh d · n·σ), the Klein-model point.
  - The heading is the spectral projector ½(I + n·σ); "locks onto the diagonal" means the projector converges.
  - The steps are not Uhlmann-parallel. Frame versus Uhlmann holonomy is open.
- **Connection energy (checked).**
  - [L, L*] = P² − U*P²U, one edge of the identity in *Non-Normality Is Connection Energy*.
  - ‖[L, L*]‖_F = √2 sinh d · 2 sin(φ/2) sin β (φ = frame turn, β = turn axis to heading).
  - Worst relative error 2.7×10⁻¹² over 200 random products.
  - The chain operator is normal exactly when the turn is a pure twist about the heading.

| twin start | L | d − L/√3 | φ | β | 𝒩 = √2 tanh d sin(φ/2) sin β |
|---|---|---|---|---|---|
| 1,019 | 4.529 | 0.146 | 15.20° | 69.2° | 0.1734 |
| 10,007 | 6.813 | 0.1123 | 7.00° | 20.9° | 0.0308 |
| 100,151 | 9.117 | 0.1091 | 9.87° | 46.8° | 0.0886 |
| 1,000,037 | 11.418 | 0.1085 | 11.62° | 54.9° | 0.1171 |
| 10,000,139 | 13.720 | 0.1085 | 12.07° | 56.7° | 0.1243 |

**Hypothesis H-CE.** 𝒩 converges, to about 0.125–0.13 under Hardy–Littlewood.
- Kill condition (written before any run): fails if |𝒩(10⁹) − 𝒩(10⁸)| > |𝒩(10⁸) − 𝒩(10⁷)|.
- Sub-question, untested: does β → arccos(1/√3) = 54.74°?

## Sources
Opened:
- arxiv.org/pdf/2111.09053
- arxiv.org/html/2506.15357v1
- arxiv.org/html/2405.03540v1
- ar5iv.labs.arxiv.org/html/2310.08121
- arxiv.org/abs/1311.7003v2

Search-only:
- arxiv.org/abs/1603.03720
- arxiv.org/abs/2105.12547
- arxiv.org/pdf/2108.07712
- arxiv.org/pdf/gr-qc/0501070
- numdam.org/item/SPS_1999__33__1_0
- arxiv.org/pdf/2101.08222
- arxiv.org/pdf/2504.15658
