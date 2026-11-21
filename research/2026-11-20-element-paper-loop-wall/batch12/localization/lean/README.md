# A strict drop in occupied dimension forces a zero twist determinant

**DERIVED, machine checked.** Let M be the occupied overlap operator on the entire finite system. Suppose its restriction to an injectively embedded source sector factors through the occupied target sector, which has smaller dimension. The restriction has a kernel, so the whole overlap is noninjective and its determinant is exactly zero. The factorization records the momentum selection rule. No invertibility of the target embedding is assumed. The result applies to vector spaces over any field, including complex scalars. The independent-spin Slater expectation is the determinant of this occupied overlap (its modulus is the quantity used here).

| Lean declaration in namespace VOTKP.Junction | Conclusion |
|---|---|
| occupiedOverlap_not_injective_of_rank_drop | the full occupied overlap M cannot be injective |
| occupiedOverlap_det_zero_of_rank_drop | its determinant is zero when the full occupied space is finite dimensional |
| occupiedOverlap_kernel_at_least_rank_loss | with finite source and full occupied spaces, the kernel dimension is at least the source dimension minus the target dimension (natural-number subtraction) |

**Checked on the repository pin.** Lean 4.34.1, official commit 5045d0056413266e57c625dcd7c365b10e377c52, and Mathlib v4.34.1 at d13f23b723b8a846827a245b89c10fc7d3f11612. The exact final module compiled, and the independent leanchecker replay of its olean exited successfully. Each declaration reports only propext, Classical.choice and Quot.sound. An independent build of the first two qualitative results on Lean 4.37.0-rc1 with Mathlib 31ce06eaadf4a200c0e1407c5f10953cf606b8f8 gave the same axiom lists for those results. This supplemental result uses the repository's Mathlib dependency; the element threshold certificates use core Lean separately. [Source](SlaterRankDrop.lean) · [pinned axiom output](axioms.txt) · [kernel replay and hashes](kernel_check.txt)

**Application.** The actual phase translation takes k to k+q. In rubidium, one occupied state entering an empty sector supplies the strict drop. The witness table exhibits one such sector and the number of losses for each tested direction. Uniform occupied rank removes this obstruction. Equal dimensions alone do not imply that the overlap is nonsingular; krypton's singular values are a numerical assertion about its wavefunctions. [QE witnesses](../rank_witnesses.csv) · [all directional overlaps](../phase_directions.csv)

To compile and print the axioms, run from the root after installing the pinned dependencies.

~~~sh
lake env lean research/2026-11-20-element-paper-loop-wall/batch12/localization/lean/SlaterRankDrop.lean
~~~
