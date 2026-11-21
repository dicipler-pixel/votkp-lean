# From the recovered spinor peel to the site budget

Claude’s [spinor recovery](https://github.com/dicipler-pixel/votkp-lean/tree/dda2d977fb427dc332525cb4d608d570fea0f39b/research/2026-11-20-element-paper-loop-wall/spinor_recovery) checked the compression identity numerically for an isometric inclusion. The closest existing branch statements I found were NewProps.prop22_1_weight, prop22_1_commutator and prop22_1_trace in the November harness. Those identify a block Frobenius weight and trace. A search of the branch Lean sources found no theorem asserting the following projector compression identity.

Let e be the retained site and P the occupied projection. In the ambient, generally noncommutative, unital ring, the kernel-checked equalities are

    e A² e − (eAe)² = e A (1−e) A e                 if e²=e
    e P e − (ePe)² = e P (1−e) P e                  if also P²=P
    e P e − (ePe)² = L† L,   L=(1−e)Pe              if e†=e and P†=P.

The second line uses both idempotencies. Multiplication preserves order throughout. For the third, the code uses an adjoint with involution, product reversal, subtraction and preservation of the identity. Under the isometric identification e=ιι†, the retained endomorphism is C=ι†Pι. For finite Hilbert sites, taking a trace gives Tr(C−C²)=‖(1−e)Pι‖²_F. The abstract ring theorem certifies the factorization; Hilbert-space positivity and the Frobenius reading use that additional structure. With e=1 and P=2 over the rationals, the putative deficit equals −2 and the leakage equals zero. The source proves the unequal values.

The three-site theorem uses a cyclic additive signed trace that changes sign under the adjoint, e.g. the imaginary part of the ordinary complex matrix trace. Its scalar codomain has no nonzero two-torsion. For e+f+g=1 and P²=P, the edge sum of signed triangles equals the signed trace of ePfP, which vanishes. The two repeated-site summands vanish separately as signed traces of products of self-adjoint elements. This leaves zero for the sole distinct-site triangle. This theorem covers arbitrary orbital multiplicities in three complete sites. With four or more sites several signed contributions may instead cancel. It concerns an occupied projector; Claude’s hopping Hamiltonian in the chiral quantum walk is a different operator.

Run `lean -j1 CompressionDefect.lean` with the repository's Lean 4.34.1. The six public theorem audits appear in lean_run.txt. A false equality at the scalar control was tested in a separate temporary file and rejected. There are no external imports beyond Std.
