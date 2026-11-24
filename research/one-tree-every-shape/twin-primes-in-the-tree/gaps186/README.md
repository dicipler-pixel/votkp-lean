# Checking OpenAI's 186 bound (24 Nov 2026)

Jeromie Beasley · notes

**Source.** github.com/openai/PrimeGaps186 (read only; none of its code was run here).

**The claim.** DHL[40,2] gives liminf (p_{n+1} − p_n) ≤ 186. It uses Maynard–Tao sieve weights with three new pieces:
- triple dense divisibility;
- Stadlmann's prime minorant;
- Dickman-type fragment measures.

The level of distribution is 0.5253 at order three and 0.504 to 0.5062 at order two. The numerical certificate is a 77-coefficient trial in 40 variables, and its normalized margin is just over 1/50000.

**The three Lean axioms.**
- **Axiom 1.** |Kl3(c;p)| ≤ 3. This is Deligne's bound (Katz, GKM Thm 4.1.1).
- **Axiom 2.** |Σ_{t≠0,−1} K2(A/t) K2(B/(t+1))| ≤ 8 p√p for every prime p and every pair of nonzero A, B, including A = B (Fouvry–Kowalski–Michel, Prop. 2).
- **Axiom 3.** 104 outer and 45 inner physical-integral bounds, plus 3 cap bounds. These come from their Python certificate and have not been proved in Lean.

## Our checks
- **The 40-tuple** {0, 2, 6, …, 186}: admissible, size 40, width 186. **Pass.**
- **Axiom 1**, exhaustive over all p ≤ 160 and all c (GAPS186-AXIOM-CHECK-01): max |Kl3| = 2.665 at p = 107, against the bound 3. **Pass.**
- **Axiom 2**, exhaustive over all p ≤ 160 and all A, B: max ratio 4.06 at p = 137, against the bound 8. **Pass.**
- **Axiom 2, split by case** (GAPS186-AXIOM2-DIAGONAL-01, p ≤ 400): the largest ratio is 3.30 when A = B and 4.50 when A ≠ B. The case A = B shows no main term and behaves like A ≠ B.
  - The kill condition as written was "the fitted exponent is above 0". Fitted exponents came out 0.14 and 0.12, so it fired.
  - That condition was badly chosen. The maximum taken over p² pairs grows slowly as an extreme value, so a small positive exponent is expected even when the bound holds. The test is inconclusive, not a refutation.
  - Whether the cited Proposition 2 allows A = B is not yet confirmed. The note itself could not be fetched.
- **Next tuples down.** Dropping the end at 186 gives a 39-tuple of width 182. The known narrowest widths (standard table, OEIS A008407, not re-fetched) are H(39) = 182, H(38) = 176 and H(37) = 168.

## What it would take to go lower
DHL[39,2] would give 182. Their margin at k = 40 is about 2×10⁻⁵, while the criterion changes by roughly 1% from k = 40 to k = 39 (a rough estimate from how M_k grows). So k = 39 needs at least one of these:
- a better trial than 77 coefficients;
- better distribution exponents;
- a new sieve idea.

Axiom 3 can be pinned down independently only by reimplementing their certificate in interval arithmetic. That is also the tool needed to search a k = 39 trial.
