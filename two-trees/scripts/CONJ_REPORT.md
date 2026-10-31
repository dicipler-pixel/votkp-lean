# Are the LPS group and the boost group conjugate in PGL2(Q_5)?

Scripts (same folder): inv.py (exact invariants, sympy), padic.py (5-adic Hensel i_5 mod 5^24, tree check).

## Verdict
NOT conjugate. PROVED (exact rational invariant, plus computed checks). Not conjugate in PGL2(Q_5), GL2(Q_5), PGL2(Q(i)), or PGL2(C), under any relabelling of generators, and in fact not even setwise under any isomorphism of the groups.

## The separating invariant
For g in GL2 over any field, t(g) = tr(g)^2 / det(g) is unchanged by scaling g and by conjugation.

| generator (any u, either sign) | trace | det | tr^2/det |
|---|---|---|---|
| LPS: 1 +/- 2u as 2x2 matrix | 2 | 5 | 4/5 |
| Boost: 3I +/- 2 sigma_u (sqrt5 x boost) | 6 | 5 | 36/5 |

All six generators of each group have the same value, so every relabelling (permutation, sign swap) compares 4/5 with 36/5. These are rational numbers, so the comparison is the same under every embedding Q(i) -> Q_5 (i_5 = +/-2 mod 5) and in C. A conjugating g would force 4/5 = 36/5 in Q_5; instead v_5(36/5 - 4/5) = -1.

Equivalent eigenvalue form: with rho = ratio of eigenvalues, tr^2/det = (1+rho)^2/rho, so conjugacy up to scalar needs rho_A in {rho_B, 1/rho_B}. Boost: rho = 5 (eigenvalues 5, 1 of 3I+2sigma_u). LPS: rho = (1+2i_5)/(1-2i_5) = (-3+4i_5)/5. Computed 5-adically: rho_LPS = 5 and rho_LPS = 1/5 both fail (they agree only mod 5; the differences have valuations 1 and 0). Exact reason: i_5 = 7 would be needed, but 7^2 = 49 is not -1 in Q_5.

## Table of further invariants (exact, sympy; u != v, all sign choices give the same value)
| word | LPS tr^2/det | Boost tr^2/det |
|---|---|---|
| g_u | 4/5 | 36/5 |
| g_u^2 | 36/25 | 676/25 |
| g_u g_v and g_u g_v^-1 (u != v) | 4/25 | 324/25 |
| commutator [g_u, g_v] | 196/625 | 196/625 |

Every single-generator, square and product invariant differs. The commutator value happens to agree (196/625); an agreeing invariant does not imply conjugacy, and the disagreeing ones decide the question. So no linear system g X = Y g needs solving: an intertwiner g that is invertible cannot exist (invertible g X g^-1 = lambda Y forces equal tr^2/det).

## Over R / C: where it breaks
LPS elements are images of quaternions q = a+bi+cj+dk, so t = 4a^2/N(q) <= 4 (Cauchy-Schwarz a^2 <= N). For the generator, q/sqrt5 = cos(theta) + sin(theta)u with tan(theta) = 2: an elliptic element (compact, SU(2)), rotation of S^3-action angle arccos(-3/5) = 126.87 degrees about axis u; eigenvalue ratio has modulus 1. Boosts have t = 36/5 > 4: loxodromic, real eigenvalue ratio 5 = e^r (r = ln 5), modulus != 1. Elliptic and hyperbolic classes in PGL2(C) are disjoint, so not conjugate over C (hence not over Q(i) either). Setwise strengthening: every element of the LPS group has t <= 4, so no boost generator (t = 36/5) is conjugate to ANY element of the LPS group, whatever isomorphism is used.

Over Q_5 the distinction is subtler, because both generators are split hyperbolic with translation length 1 on the tree (det valuation 1, primitive). The tree sees them as alike; the multiplier rho (a cross-ratio type quantity) separates them.

## The "v2 working report" observation: checked and TRUE
With i_5 = 2 mod 5 (Hensel to 5^24):
- Each 3I +/- 2 sigma_u and each LPS generator is primitive of determinant valuation 1, so moves the base vertex to a neighbour.
- Image lines mod 5 in P^1(F_5): Boost: i+ -> 4, i- -> 1, j+ -> 3, j- -> 2, k+ -> inf, k- -> 0 (six distinct = all of P^1(F_5)). LPS: i+ -> inf, i- -> 0, j+ -> 3, j- -> 2, k+ -> 4, k- -> 1 (also all six distinct).
- Proof of simple transitivity (no freeness assumption needed): let F be the abstract free group on three letters, rho: F -> group the generator map. The orbit map from the 6-regular Cayley tree of F to the Bruhat-Tits tree, f -> rho(f) v0, is equivariant and bijective on neighbours of every vertex (because the six neighbour images of v0 are distinct), hence a covering of trees, hence an isomorphism. So both groups are free of rank 3 and act simply transitively on the vertices. Computed check: all reduced words to length 4 (1+6+30+150+750 = 937 words) give 937 distinct vertices, at distance equal to word length, for both groups.

## Consequence (precise statement of what is and is not true)
Both groups are free on matched generators and both act simply transitively on the same tree T. The vertex map gamma_A v0 -> gamma_B v0 (matching words) is therefore an automorphism of T conjugating one group to the other, so they ARE conjugate in Aut(T) (the first-neighbour labelling matches after relabelling i <-> k, j fixed, but that is not needed). That automorphism is NOT in PGL2(Q_5): Aut(T) is far larger than PGL2(Q_5), and the algebraic invariant t separates the groups there. "Same tree action" does not give "same matrices".

## Status
- Not conjugate in PGL2(Q_5)/GL2(Q_5)/C, any relabelling, even setwise: PROVED (one exact rational invariant; 4/5 vs 36/5).
- Simple transitivity of the boost group: PROVED (covering argument) and COMPUTED (depth 4).
- Conjugate in Aut(T): PROVED (same argument), not algebraic.
- Open: none for the stated question. Possibly interesting follow-up (not tested): whether a different pair of lattices/other Lorentz-type groups with t <= 4 could match; the boost group with t = 36/5 cannot.
