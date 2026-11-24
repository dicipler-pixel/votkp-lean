# The twin-chain turn: five-way swarm

Jeromie Beasley · 24 November 2026

## The setup
The twin-prime chain is walked in his peel ball:
- Each step is a boost of rapidity ln(a′/a).
- It runs along the arm set by the end digit of the next twin start (1, 7, 9 → x, y, z).

Five independent checks were run:
- **proof**: how far the proof goes;
- **opposite**: other chains and broken chains;
- **shapes**: the measuring shapes;
- **precision**: the walk to 10¹²;
- **priorart**: prior art, and the framework fit.

Each check wrote its kill conditions before running. Each folder holds its REPORT.md, scripts and outputs. The key numbers were re-checked independently.

Grades: proved / derived / measured / cited / open.

## What stands
1. **Exact step (proved; checked to 160 digits, and independently to 7e-14).**
   - tan(ε/2) = Γ₁Γ₂ sin γ / (1 + Γ₁Γ₂ cos γ), with Γ = tanh(r/2), at any arm angle γ.
   - Wall for two arms: tr[A,B] = 2 − 4 sinh²(r₁/2) sinh²(r₂/2) sin²γ. For equal steps the wall sits at Γ² = 1/(1 + sin γ); at 90° that is Γ² = ½.
2. **Endpoint law (proved, conditional on steps → 0 and gap-weighted digit shares settling; Σr² not needed).**
   - d/L → |P|, where P is the gap-weighted mean arm direction.
   - It holds for every chain with shrinking steps and mixed arms: twins by end digit, by mod 9 and by mod 7; cousins; all primes on four arms; random chains.
   - 1/√3 is the shadow of a cube edge on the body diagonal. It is the same in flat space.
3. **The turn is curvature (derived).**
   - Each step's Wigner angle equals the area it sweeps in rapidity space.
   - Every flat reader gives zero turn.
   - On a curvature dial, the turn approaches curvature × flat area as the curvature goes to 0. At the ball's curvature the ratio is 0.114.
4. **Connection energy (checked).**
   - With L = P·U: ‖[L, L*]‖ = √2 sinh d · 2 sin(φ/2) sin β.
   - The chain operator is normal exactly when its turn is a pure twist about the heading.
5. **Frame theorem (proved, conditional).** The old "converges iff Σω converges" step was false and is replaced by a corrector lemma. The conditions are:
   - Σr² < ∞;
   - a weight path of finite total change;
   - Σ r|N| < ∞, where N is the noise around the *local* mean.
6. **Limit (measured to 10¹², conditional on the tilt dying).**
   - Measured turn: 12.2695° (10⁹), 12.2969° (10¹⁰), 12.3197° (10¹¹), 12.3442° (10¹²).
   - "Turn if the tilt dies": 12.46508° at both 10¹¹ and 10¹².
   - Limit: 12.4651° ± 0.0001°. The ± is estimated, not proved.
7. **Constant (measured).** c = 0.1086 to four digits.
   - Its limit is about 0.10866 (derived).
   - It is set by roughly the first 1200 twin starts.
   - It changes with the labelling: mod 9 gives 0.067, mod 7 gives 0.347, cousins give 0.184.

## What died
- **Unconditional convergence.** Frame convergence would force a twin in every interval (x, (1+ε)x], which is open. Σr² < ∞ is not provable unconditionally, even granting infinitely many twins.
- **"Hardy–Littlewood counts ⇒ H3."** A chain with equal digit counts, but the largest gap in each triple given to digit 1, gives d/L = 0.656.
- **H3 with fixed weights (⅓, ⅓, ⅓).** The noise tail falls only like 1/L, which is the borderline case.
- **Exact lock on the diagonal.** At 10⁹ the heading sits 0.47° off it, on the tilted local mean.
- **Frame axis on the diagonal** (57.8° off), and **c from a random-arm model** (0.245 ± 0.128).
- **The simple mod-30 lattice model of the tilt** (wrong sign).
- **"Bounded distance" when |P| = 0.** For the tetrahedron the distance grows like 0.326 ln L.
- **"The turn does not converge ⇒ infinitely many twins" as leverage.** It is true, but any infinite sequence satisfies it. The stronger, proved form: d → ∞ by itself implies infinitely many twins.

## New, measured
- **The tilt.** The gap-weighted digit tilt falls like 1/(mean twin gap). Tilt × gap = 1.15, 1.15, 1.18, 1.17 per decade from 10⁸ to 10¹². The factor 1.17 is not derived (open).
- **All primes.** For all primes the gap-weighted shares carry a steady 1/L tilt: ×L gives +0.080, −0.196, +0.174, −0.058 for digits 1/3/7/9. The cause is that each end digit forbids one class of incoming gap.
  - Sexy primes carry the same tilt.
  - For both, frame convergence is undecided. Twins and cousins are the clean cases.
- **Twin digit order.** Consecutive twin starts repeat their end digit at rate 0.312, not ⅓. Forward steps 1→7→9 come at 0.355.
  - The chirality gives the along-diagonal part of the turn (6.54° of the 12.27°) to 10%, with the right sign.
- **Where the wall shows up.** No single step reaches the wall. The chain as a whole crosses the wall sphere ρ² = ½ between twin starts 197 and 227. Pair readings hit it at 1151, 2027 and 4481, the same range in which c settles.
- **Hypothesis H-CE, untested beyond 10⁷.** The normalised connection energy 𝒩 = √2 tanh d sin(φ/2) sin β converges.
  - Measured: 0.117 (10⁶), 0.124 (10⁷).
  - Kill condition: fails if |𝒩(10⁹) − 𝒩(10⁸)| > |𝒩(10⁸) − 𝒩(10⁷)|.

## Prior art
Nothing found does this: the boost chain from twin primes, the distance law, the frame turn, or a holonomy constant from primes.
- Closest work:
  - Sahoo, arXiv:2111.09053 — twin classes, plain counts.
  - Fraile et al., arXiv:2506.15357 — flat last-digit walks.
  - Lemke Oliver–Soundararajan (2016) — digit bias of consecutive primes.
  - Lu, ICML 2026 poster — counts converge, spacings do not.
- Methods: Benaïm (1996, 1999); Kushner–Clark (1978); Thomas–Wigner rotation as holonomy (Palge–Pfeifer, arXiv:2310.08121).
