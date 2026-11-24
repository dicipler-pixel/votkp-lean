# Independent reader's notes and what changed because of them (24 Nov 2026)

Author of the record: Jeromie Beasley. The reader was a separate agent that had not seen the work being made.
It re-ran the saved scripts, wrote its own, and was told not to soften anything.

## Held as stated
- Flat maximum 3/2, 7/4, 15/8 (sizes 2, 3, 4); the reader added size 5: 31/16.
- Star ratio exactly 5/3 (rank-1 mean 81/72, rank-2 mean 90/48).
- Hyperbolic star: 1.500005 at leg 0.01, 1.662399 at leg 40, 1.665814 at leg 200; end to end = 2 x leg - ln(4/3).
- Poincare numbers 0.5000, 1.7071, 3.4397, 4.9886 for sizes 2 to 5 by the reader's own build; sizes 6, 7 by re-running the script.
- The loop identities and the weak-value identity.

## New from the reader
- Exhaustive over all 4^9 placements of the nine rank-1 matrices on a three-leg star: maximum 5/3, reached by exactly
  12 labelings (column-space or row-space grouping, times leg relabelings). Other groupings: 9/13, 15/13, 4/3, 25/21.
- Search over all tree metrics on 16 points (about 200 restarts): best 1.66666667, always the equal three-leg star. A search, not a proof.
- General metric spaces: the cap is 4, reached by distance = rank.
- Averaging the star over the symmetry group gives a uniform placement (every rank-1 pair one distance, every rank-2
  pair another) with ratio 5/3 inside a product of trees. A product with squared distances added can never beat its best factor.

## Corrections taken
1. "Search products of trees for a placement above 5/3" is withdrawn as a next step: such a product cannot beat its best factor.
   The live question at size 2 is whether squared distance = rank (ratio 2) fits in any nonpositively curved space.
2. "Uniform target above 3/2 not found" is superseded: it exists at 5/3 (the averaged star).
3. Flat space below 2 "at every size" is enumerated for sizes 2 to 5. The rank-1 character gives 2 - 2^(1-mu) at every size
   by a hand count; that it is the maximum at every size is not proved here.
4. The flat Poincare constant is an ordinary spectral gap. For odd primes the literature gives a gap of order 1/n
   (Stong 1995, as quoted by Coppersmith and Pak 2000), which makes this constant bounded. For the two-element field
   that citation was not confirmed here.
5. "All found the same star" applies to the three-dimensional run only; the other runs were not analysed for structure.
6. Size 3: only equal-leg stars were searched. No general tree search at size 3 has been run.
7. Cheshire script 01 left out the factor i of the published pre-selection and printed a modulus. Script 02
   (`cheshire_gamma_v2.py`) uses the published states and prints complex values: cat (1, 0), grin (0, 1).
8. One convention now: z = right-arm over left-arm amplitude, right arm reads (1 + Gamma)/2. The first mapping script
   used the inverse ratio, so its Gamma has the opposite sign.
9. The flux reading Gamma = -i tan(Phi/2) is inside the disc only up to a quarter flux quantum, on the rim at a quarter,
   and outside beyond it (script 02, line C2).
10. Which twists land on the rim depends on the grin observable: for the circular grin a linear filter is on the rim and a
    handed one is real; for the diagonal observable it is the other way round; for horizontal/vertical the twist is zero.
11. Lines that cannot fail (true by definition, the dictionary): the arm shares (1 -/+ Gamma)/2, the addition law joining
    cat and grin, flux moving both together, the ring walk determinant, card B158 (Cauchy-Schwarz). The torus check compared
    two closed formulas and built no operator. None of this is new physics: it is standard weak-value algebra written in the Smith-disc coordinate.

## Not checked by anyone yet
- Whether 5/3 is the true maximum over trees (search only), and over all nonpositively curved spaces.
- A general tree search at size 3.

## Second independent check (CHECK-16MATRIX-01, later on 24 Nov)

New code: matrices as integers, rank by bitmask elimination.
- Counts: 9 rank-1 and 6 rank-2 matrices. Each rank-2 matrix splits 6 ways and each rank-1 matrix has 4 partners. **Held.**
- Flat maximum over all characters: 3/2, 7/4 and 15/8 at μ = 2, 3, 4. **Held.**
- The star by column space gives 5/3. The exhaustive search over all 4^9 placements has maximum 5/3, reached by 12 placements. **Held.**
- The hyperbolic star: 1.500005 at leg 0.01, 1.662399 at leg 40, 1.665814 at leg 200. **Held.**
- At μ = 5 the rank-1 character gives exactly 31/16. Closed count: a random invertible matrix has its corner entry equal to 1 with probability 2^(μ−1)/(2^μ−1), so the ratio is 2 − 2^(1−μ) at every μ.
- Characters of rank 2 to 5 at μ = 5 were sampled (200,000 invertible matrices) and come out at 1.25 or less. So 31/16 is the μ = 5 maximum up to sampling. Rank class determines the value, by GL × GL invariance.
- Not rechecked here: the Poincaré numbers, and the Stong 1995 spectral-gap citation.
