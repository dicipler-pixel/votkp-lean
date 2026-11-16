# Read record 08 — VOTKP v2.0 (6 October 2026), read in full
Jeromie Beasley's corpus. Record made 10 November 2026. Source: Drive file VOTKP_ELEMENTAL_PEELING_PAPER_v2_0_20261006 (markdown with equations, 210 k characters; sections 1-18, Appendices A-F; all nine parts read). Its title block says "Claude's version, written from Jeromie Beasley's research programme".
NOT in this version: sections 19-22 of v2.9 (peel metric against the Grassmannian metric, friction bound, hidden channel, xenon). v2.9 exists for me only as an 18 MB PDF I cannot pull; those sections are still unread.

## Statements that the knot / disk / tree work leans on (numbers as printed)
- Thm 3.1 predictive quotient: N = ker(R, RL, ..., RL^(n-1)); futures agree iff v - w in N; the present closes iff ker R is L-invariant.
- 5.3 Schur boundary memory: S(z) = z - A - B(z - D)^-1 C; hidden layer survives as Sigma(z) = B(z - D)^-1 C. 5.4 memory kernel B e^((t-u)D) C. 5.5 transfer silence iff B D^j C = 0 for j < q, sharp.
- 5.9 one hidden level: Sigma_s(x) = 1/(x - s); T_s(x) = (x - s)^2/(x^4 - 2s x^3 + 2). The two signs s = +-1 share T(0) = T(sqrt 2) = 1/2 and differ at x = 1 (0 against 4/5). Only the SIGN of the hidden level separates them.
- 5.10 Sigma_lambda(0) = -c for every lambda; the slope -c/lambda differs.
- 6.2 surviving matches: M preserves every match of C iff C M P = 0 iff CM = TC. Gold metamer Delta E = 8.60.
- 6.4 film: r(d) = (Gamma + x)/(1 + Gamma x), x = r12 e^(4 pi i N d/lambda). Thm 6.2: the film reflects more than its bulk exactly when the echo x lies OUTSIDE a circle through the origin fixed by the front surface. Thm 6.3: the thin end is a shunt admittance.
- Thm 8.1 Gamma_k = tanh(tau_k/2), tau_k = ln(IE_(k+1)/IE_k). Real positive: "the atomic reflection chart has no phase."
- Thm 8.2 split: Gamma = Gamma_scr (+) Gamma_sh; at a shell wall Gamma_sh = (2n-1)/(n^2 + (n-1)^2) = 3/5, 5/13, 7/25, 9/41, ...: odd leg over hypotenuse of a Pythagorean triple; Euclid's form tanh ln(p/q) = (p^2 - q^2)/(p^2 + q^2).
- 11.5 Levine-Tristram: H(omega) = (1 - omega)V + (1 - omega-bar)V^T; all 17,360 walls are Alexander roots; Prop 11.1 half the jump has the parity of the root multiplicity; simple root = exactly +-2; 513 even-multiplicity roots are silent. Torus knots are the unique maximisers of |sigma|. One window separates 13a_3542 from the mirror of 13a_4018.
- 13.5 A-polynomial form omega = log|L| d arg M - log|M| d arg L. TORUS CONTROL (A.10): on a branch L = eps M^-k the form vanishes identically — "the potential vanishes while topology and loading do not." The curve meets L = 1 at the Alexander roots and at M^2 = -1; the second is not a wall.
- 13.7 windows of the meridian phase: meridian -> cos 2 pi alpha + sin 2 pi alpha u; omega = e^(4 pi i alpha); signed count = sigma_omega/2. Trefoil: ONE arc, 1/12 < alpha < 5/12, on which L = -M^-6 meets L = 1 at both ends. 8_19 steps 0,1,2,3,2,1,0 at six walls. "No Hamiltonian here makes a knot's meridian phase the driven parameter; that bridge is open."
- Thm 15.1 block reflection = (+)-sum of the steps; Cor 15.2 peel coordinate = hyperbolic length; Cor 15.3 the film is Gamma (+) x with complex arguments — same algebra, but NOT a hyperbolic isometry for complex Gamma.
- 15.2 order: (+) is commutative and associative, so the composite carries no order. A stack at zero phase telescopes exactly like the ladder; only the phase between additions makes order visible, and in multilayers that phase is a Thomas rotation. A reduction that discards has an associator: (x*y)*z - x*(y*z) = P[x(I-P)(yz) - (I-P)(xy)z].
- 15.4 the mass-5 and mass-8 gaps leave the disk: |Gamma| = 1.074, 1.220, 1.025.
- Section 16 closes: "The paper claims no correspondence between elements and knots." Section 17 lists "the elemental-knot bridge itself" as open.
- H-01: the relativistic reading "unifies the two halves but predicts nothing new" (killed as a separator).

## Carried item 2, examined against the text
"Tetrahedron shape z(a) = kappa - g/(a - d) is VOTKP 5.3 with one hidden level."
- 5.3 with a scalar hidden level D = d gives the retained quantity A + BC/(a - d). The form matches with kappa = A and g = -BC.
- What the text adds: for a Hermitian coupling C = B*, BC = |B|^2 > 0, so g must be NEGATIVE REAL. This is a test the fitted g can fail. If g on the knot data is positive or complex, the hidden level is not Hermitian-coupled, and the tetrahedron is an open (non-normal) channel, not a closed one. UNTESTED: I do not have the fitted kappa, g, d.
- 5.9 says the sign of the hidden level is exactly what a shared record cannot see. On the disk the mirror solution sits outside the rim. Whether d -> its mirror is the same sign flip: UNTESTED.
"Edge equations = Thm 15.1 closing to zero."
- Gamma(A) (+) Gamma(B) = Gamma(AB) is algebraic, so it holds for complex shapes: product of shapes = 1 is the same as the (+)-sum of their Smith points = 0. That part is an identity and predicts nothing.
- The content is what (+) cannot see: the edge equation in logarithms closes to 2 pi i, not to 0. By 15.2 the composite carries no order and no phase; the phase between additions is where order lives. That is the paper's own reason the twist sits in Neumann's winding integers and not in the shapes.

## Joins found on this read
1. VOTKP 13.7 gives the trefoil arc as 1/12 < alpha < 5/12. Dirac Time 13.1 gives ends k/(2pq) = k/12: k = 1 and k = 5. Direction -k^2/6 mod 1 = 5/6 at BOTH ends (1 and 25 are equal mod 6). Agrees with the vacuum-disk value 5/6. CHECKED by arithmetic on the printed numbers.
2. VOTKP A.10 is the corpus's own proof that a torus branch has zero volume form. With Two Trees 8.7 (ab a pure finite rotation) and the vacuum disk (zero decay) that is three statements of one fact.
3. Thm 6.2 (film): "more than bulk iff the echo lies outside a circle through the origin." Vacuum disk: geometric solution inside, mirror outside, flat on the rim. Both are inside/outside tests on one disk decided by one circle. Structural; UNTESTED as an identification.
4. Shell walls and the line Gamma^2 = 1/2 (CHECKED from the printed tau values): every pure shell part is below the line (largest 9/25 at n = 2). The alkali first steps are above it for Li, Na, K, Rb, Cs (Gamma^2 = 0.75, 0.65, 0.58, 0.55, 0.51) and Fr falls just below (0.48). Fr is also where the column line breaks (8.8). A fifth appearance of the line; low weight until something is predicted with it.
5. Pythagorean triples appear twice: the shell wall (2n-1, 2n(n-1), n^2+(n-1)^2) and the Thomas turn of Two Trees (1 - t^2, 2t, 1 + t^2) with t = Gamma^2. Both are Euclid's tanh ln(p/q). The shell wall is a STEP of ratio (n/(n-1))^2; the Thomas triple is a TURN with parameter Gamma^2. Same family of numbers, different roles; no identification made.
