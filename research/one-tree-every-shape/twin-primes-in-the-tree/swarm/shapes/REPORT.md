# Swarm 3: the twin chain read through the measuring shapes

Jeromie Beasley · swarm notes · 24 November 2026

All runs go to 10⁹ and use all 3,424,504 twin starts from 11, through a spinor walker. A 4×4 walker loses the frame beyond d ≈ 12.

Grades: derived = algebra, checked by a script; measured = from a run; cited = standard result.

## 1. Why 1/√3, and the offset c
**Slope (derived).** Each step is a cube edge. Only its shadow on the body diagonal (cos = 1/√3) moves the chain outward; the rest goes into turning. Measured slope: 0.57729.

**Offset (measured).** c = 0.10857, steady to ±0.0001 from 10⁵ on. It splits exactly (to 1.5e-12) into four parts:

| at twin start | c | first step | curvature gain | arm noise | heading lag |
|---|---|---|---|---|---|
| 1019 | +0.1460 | +0.1840 | +0.5651 | −0.3785 | −0.2246 |
| 10007 | +0.1123 | +0.1840 | +0.5866 | −0.4080 | −0.2503 |
| 9.99×10⁸ | +0.10857 | +0.1840 | +0.5913 | −0.4093 | −0.2575 |

**Predicting c.**
- True step sizes with random arms: 0.245 ± 0.128. Killed.
- Real chain to 10⁴, then the averaged transient theory: 0.1091 against 0.1086. Survives (miss 0.0005).
- The same from 10³ misses by 0.013. Killed.
- So c is set by roughly the first 1200 twin starts. It is a fingerprint of the early chain, not a universal constant.
- The real c ranks 21st of 200 random-arm chains. One step, 29→41, alone drops c from +0.142 to +0.035.

## 2. Thomas turn at any arm angle γ, and the wall
- **Turn (derived; checked to 6e-15):** tan(ε/2) = Γ₁Γ₂ sin γ / (1 + Γ₁Γ₂ cos γ).
- **Wall:** tr[A,B] = 2 − 4 sinh²(r₁/2) sinh²(r₂/2) sin²γ. For equal steps the wall sits at Γ² = 1/(1 + sin γ); at γ = 90° this is the known Γ² = ½. Checked independently to 1.4e-14.

**Platonic arm sets (measured to 10⁹).** The slope law |P| = √((1 + 2 cos γ)/3) and the late turn per step √(1 − |P|²) hold on every shape:

| arms | γ | \|P\| | measured slope | c | turn | late turn per step (predicted) |
|---|---|---|---|---|---|---|
| cube = octahedron | 90° | 0.57735 | 0.57729 | 0.1086 | 12.27° | 0.8164 (0.8165) |
| tetrahedron face normals | 109.47° | 0.33333 | 0.33271 | 0.1567 | 19.62° | 0.9380 (0.9428) |
| icosahedron face vertices | 63.43° | 0.79465 | 0.79465 | 0.0603 | 7.45° | 0.6071 (0.6071) |
| dodecahedron, vertex neighbours | 41.81° | 0.91117 | 0.91117 | 0.0281 | 4.62° | 0.4120 (0.4120) |
| icosahedron face edges (closed loop) | 120° | 0 | d bounded at 0.81 | — | 6.78° | — |

## 3. Where the chain meets the wall
- No single step reaches the wall below 10⁹. The largest is 17→29, with Γ² = 0.068.
- The chain as a whole crosses the wall sphere ρ² = ½ between twin starts 197 and 227. By then 80% of the turn has already happened.
- Read as three books, the pairs hit the wall at twin starts 1151 (x,z), 2027 (y,z) and 4481 (x,y). That is the same 10³–10⁴ range in which c settles.

## 4. Flat readers and what curvature adds
- "Lengths add" gives d = L exactly. Flat Euclidean space still gives slope 1/√3 (0.57840). The tetrahedron's own reading gives 1/3.
- So the 1/√3 is the cube-edge shadow, not curvature. Curvature contributes the turn (zero in every flat reader) and most of the offset (flat value 0.019, falling).

**Curvature dial.**
- The flat loop area grows by about 0.18 per unit of path. That equals the leftover book imbalance S = (−0.265, −0.256, +0.521) crossed with (1,1,1), divided by 6.
- Hyperbolic area saturates, which is why the turn converges.

| √curvature | turn | turn ÷ (curvature × area) | offset above flat |
|---|---|---|---|
| 2 | 30.93° | 0.072 | +0.217 |
| 1 (the ball) | 12.20° | 0.114 | +0.087 |
| 1/16 | 0.40° | 0.966 | +0.0013 |

## 5. Three-fold (3-6-9) reading
- The frame axis is not on the diagonal (57.8° off). Killed. It is still nearer the diagonal than random chains (rank 13 of 200; random median 80.8°).
- The arm walk moves on the 120° turn group. Measured step probabilities: forward 1→7→9 0.355, backward 0.333, repeat 0.312.
- In the mod-9 reading, the step is exactly the gap mod 9 ∈ {0, 3, 6}.
- **Chirality.** The 12.27° splits into 6.54° along the diagonal and 10.38° across it. The chirality sum gives the along-diagonal part to 10%, with the predicted sign. Random arms average to 0.
- Mod-9 arms: same slope, but c = 0.067 and turn 9.22°.
- The book imbalance S lies in the three-fold plane along z. The heading's tilt does not follow it (80–83° apart). Killed.
- One kill line failed as written: the cyclic relabel x→y→z gave 1.3e-7° against a 1e-9° limit. This is floating-point roundoff, not physics.

## Files
twinlib.py, s1_diagonal.py, s1b_noise.py, s2_platonic.py, s3_wall.py, s4_flat.py, s5_369.py, s5b_chirality.py, each with its .out file.
