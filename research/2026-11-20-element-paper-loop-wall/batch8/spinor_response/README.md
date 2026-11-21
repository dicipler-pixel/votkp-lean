# What the spinor peel keeps at an elemental junction

**DERIVED.** Jeromie’s recovered compression identity gives the element paper’s junction budget as a special case. Let the space split orthogonally into sites, let ιᵢ include site i, and write P for the **occupied orthogonal projector**. In the recovered identity set A=P, take Qᵢ=I−ιᵢιᵢ†, and let Cᵢ=ιᵢ†Pιᵢ. Using P²=P gives the operator equality on site i

\[
 C_i-C_i^2=(Q_iP\iota_i)^\dagger(Q_iP\iota_i)
          =\sum_{j\ne i}P_{ij}P_{ji},\qquad P_{ij}=\iota_i^\dagger P\iota_j .
\]

Tracing gives \(B_i=\sum_{j\ne i}X_{ij}\), with \(X_{ij}=\|P_{ij}\|_F^2\). Thus \(B_i\) measures exactly the failure of compressing P to preserve its square, and each junction contributes a positive term. This argument assumes finite-dimensional sites and a complete orthogonal decomposition (or appropriate convergence in an infinite model). Replacing P by a finite-temperature density matrix generally adds the local block of \(P-P^2\). [Claude’s recovered spinor identity at dda2d97](https://github.com/dicipler-pixel/votkp-lean/tree/dda2d97/research/2026-11-20-element-paper-loop-wall/spinor_recovery)

**Rejection tests.** If every projector triangle were real, a signed loop could add nothing to its norm ledger. Conversely, if any nonzero imaginary projector triangle implied directional transfer, every Hamiltonian with this occupied projector would have to exhibit a corresponding imbalance. The following control tests both statements.

## A signed observable with an edgewise constraint

Define \(W^P_{ijk}=\mathrm{Tr}(P_{ij}P_{jk}P_{ki})\). Under independent unitary basis changes at each site, intermediate basis changes cancel and the trace is invariant. Reversing the walk conjugates the trace by Hermiticity. Its imaginary part is therefore traversal-odd. Each link norm is identical for a walk and its reverse.

Idempotency places a strong constraint on this signed readout. For each fixed oriented edge,

\[
 \sum_k W^P_{ijk}
 =\mathrm{Tr}\!\left(P_{ij}(P^2)_{ji}\right)
 =\mathrm{Tr}(P_{ij}P_{ji})=X_{ij}.
\]

The terms k=i and k=j are real: each is the trace of a product of two Hermitian matrices, one being an on-site block. Consequently, if the whole projector has **only three sites**, the single distinct-site triangle has zero imaginary part. This holds even for several orbitals per site. For a projector on a larger crystal a triangle can be complex, but its signed weight cancels against other triangles sharing that oriented edge in the complete sum. Omitting sites or shell truncation can hide that cancellation.

**Exact control.** Take four scalar sites and let V have rows (1,0), (0,1), (1,1), (1,i). The occupied projector is \(P=V(V^\dagger V)^{-1}V^\dagger\). The included script checks its Hermiticity, idempotency and rank using integers. Each site gives \(B_i=12/49\). At edge 0→1 the two distinct-site loops are
\[
 W^P_{012}=1/343-i/49,\qquad W^P_{013}=1/343+i/49 .
\]
Every link weight agrees between P and its entrywise complex conjugate. The imaginary loop values have opposite signs. Thus a phase survives the path ledger even when all absolute weights and shell concentration fractions agree.

**Direction control.** Claude’s three-mode hopping Hamiltonian allows a complex Hamiltonian loop \(W^H_{ijk}\) and a directional short-time signal. A spectral projector obeys an additional identity, \(P^2=P\). For the flat-band Hamiltonian \(H=I-2P\), P projects onto the occupied lower band, and
\[
 e^{-itH}=e^{-it}(I-P)+e^{it}P.
\]
Between different sites its transition block is \(2i\sin(t)P_{ji}\). Summing transition probabilities over the local initial and final channels gives \(4\sin^2(t)X_{ij}\), identical in both directions. The displayed four-site projector therefore has a nonzero imaginary triangle **and zero directed population imbalance for all times** in a Hamiltonian with precisely that occupied projector. Energies and matrix elements of the actual generator enter a transport prediction.

## Keep three operations identifiable

| Change to the record | Peel reflection Γ | Signed projector loop Im W | Three-displacement screw χ |
|---|---|---|---|
| Reverse the two threshold energies | Flips | Separate input | Separate input |
| Traverse the same path backward | Separate input | Flips | Stays, because the displacement sequence becomes −d₂, −d₁, −d₀ |
| Apply a spatial mirror to the crystal | Scalar energies stay for equivalent mirrored physics | Requires the action of the mirror on orbitals and on the labelled path | Flips, by the determinant of the spatial transformation |

Complex conjugating P in this control is an algebraic operation. For spinless time reversal represented by conjugation, it also gives the time-reversed projector. More generally a site-preserving antiunitary time-reversal symmetry of the occupied subspace maps the **full traced** loop to its conjugate, so its imaginary part vanishes. Exchanging sites or selecting one sector instead of the full time-reversal pair changes this conclusion. A spatial mirror is ordinarily represented by a unitary action on the orbital and spin spaces; the image loop may preserve or reverse the chosen traversal depending on how it is labelled. Chirality of a crystal alone does not impose a signed imaginary projector loop.

**Geometry control.** On the ideal bcc nearest-neighbour graph the eight displacements are (±1,±1,±1) in half-cell units. Two such steps have all-even coordinates; a third nearest-neighbour edge requires all-odd coordinates. No all-nearest-neighbour triangle exists. A meaningful loop for that graph can use four nearest edges, or a triangle with a verified longer-range projector block. A nearest-neighbour hopping Hamiltonian and its occupied spectral projector may have different edge supports.

Run `python3 check_projector_loops.py` for the exact controls. The four-site example is a finite projector witness. An elemental assignment would require its occupied projector, a labelled path and a specified time-reversal convention. A transport claim would also require its dynamical generator and a measured directional observable.
