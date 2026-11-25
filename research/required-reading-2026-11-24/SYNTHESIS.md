# What the two readings say together

Session A, 24 November 2026. Built only from `NOTES_IQGT.md` and `NOTES_VOTKP.md` in this folder. Nothing here was run except the three one-line identities marked "checked".

## 1. How the tensor was made (one paragraph)

Take an operator with a gap. Keep only the projector P onto what is retained. Differentiating P² = P forces every move of P to be a block B that crosses from the retained part to the rest. The tensor is the one Hermitian form on those blocks, Q(X,Y) = Tr(XY*); its real part is the metric, its imaginary part the curvature. The first edition (12 June) already said the rest: "all geometric features are generated exclusively by the mixing between the occupied and unoccupied subspaces", and the gap is "the fundamental geometric regulator". VOTKP §22.1 then names what a peel keeps in the same terms: the triple (A, P, B), with one number read three ways, ‖B‖² = ½‖[H,P]‖² = Tr K(0).

## 2. Recognising the others

Every tensor functional met this week reads the same cross block B and differs only in what it does with B's singular values σ.

| Object | What it does with the singular values of the cross block | Where |
|---|---|---|
| Flattening rank (the explicit spectral point over every field) | counts the nonzero ones: Σσ⁰ | Anthropic release; Strassen |
| Quantum functional (explicit over the complex numbers) | entropy of the normalised σ², largest over the restriction orbit | Christandl, Vrana, Zuiddam |
| Weight between, E_B | Σσ² | VOTKP 22.1, The Weight Between |
| IQGT metric of the move B generates | Σσ²/Δ², each pair over its own gap squared | IQGT 3.3 |
| Static response, polarizability | Σσ²/Δ per pair | IQGT 7.2, VOTKP 4 and 20.3.4 |
| Zero-lag memory | Tr BB† = Σσ² | VOTKP 20.3.3 |
| Self-energy, memory kernel | the whole positive measure B·dE_D·B†, not a sum | VOTKP 20.3.3 |

Checked: on a wire of dimension q the cross block is a q×q identity, so rank = q and Σσ² = q. The count and the weight agree on wires and both multiply under tensor product. They part company off wires, where the weight is not monotone under restriction and the count is.

So the difference between the IQGT and a spectral point is not the object but the reading. A spectral point is allowed only readings that never rise under restriction and multiply exactly. IQGT reads the same block at power two and then divides by the gap, which no spectral point does. **The gap is what the others do not have.** That is the regulator of the first edition, and it is the thing to look for when asking whether another tensor is his: does it weight each cross pair by its own gap.

Mapping to try, not a result: the release's limiting price is "squared distance = rank". IQGT's squared chordal distance is Σ sin²ϑ, which counts the 90° angles when all angles are 0 or 90° (the equality case of IQGT Proposition 12.3). Placing the 16 matrices as graph projectors and reading both distances is the first test of whether the building cone is the gap-free limit of his metric.

## 3. What the tensor does and does not do on the periodic table (from VOTKP itself)

1. **The ladder is the real diameter only.** "The geometry of the retained subspace comes first, and the threshold ladder is the real diameter of its chart" (22.4). The ladder has no phase (Theorem 8.1) and does not fix a projector path (Proposition 19.3).
2. **The tensor has been put on the elements once directly, and failed that way.** Section 9 used principal angles between Slater-orbital subspaces; registered; failed. Section 17 lists the repair as open: "The elemental angle in projector form ... between the retained projectors of §22.1 have not been computed."
3. **The tensor enters the elements through the edge of two books.** E₋/E₊ = Γ² (22.2). Gap powers compose the step: static response reads Γ once, the metric reads Γ ⊕ Γ (22.3).
4. **The tensor needs numerators the ladder cannot give.** g = ∫Δ⁻³dF, α = 2∫(Δ² − x²)⁻¹dF for the oscillator-strength matrix measure F (20.1.7, 20.3.4). "Ratios of removal energies cannot determine its numerators."
5. **Where a phase exists, it finds what the even reading cannot.** The five alkali atoms past the half line hold five of the six largest optical phases; reflected power is blind (23.5).

## 4. For the formal addition to the periodic table: what the paper has already fixed

- Two records per element, never merged: **level** (ln IE₁: polarizability, radius, hardness, visible ground line at 6.82 eV) and **shape** (the peel vector: group, at 0.95 held out with ten steps).
- **Shell wall fractions** 3/5, 5/13, 7/25, 9/41, 11/61, 13/85, exact at every wall, with a **screening part of two kinds** (p-core, d-shell) and a negative one at 4f.
- **Half line** crossed once on each core line; eight steps past it; caesium the last; the carbon–nitrogen crossing set by the 5/8.
- **Alkali charge ratio** 2.02 to 2.05 from Na to Cs.
- **Stagger**: half-filled step against spin-orbit edge, changing over with charge (2p at Z = 29, 3p at 46, 4p at 47).
- **Ends and middle**: 5/(8Z); Thomas–Fermi envelope carries scale, residual carries family.
- **Octave tests already run** (8.9, Appendix D): fixed octave correct only to calcium; one wave per row loses; Russell's contraction falls at the third tone, not the fourth; what survives is the swing and the one-third constant (open).

## 5. Three things this reading changes in my own work of the last two days

1. **The table-wave run repeated part of Section 8.9 without my having read it.** The octave result (correct for Z = 3 to 20, failing beyond) is VOTKP test T07, his first.
2. **The pair wave I reported is anchored on Janet's double-period ends** (Z = 4, 20, 56, 120). VOTKP test T06 found Janet's closures carry no ionization ridge (0.004 against 0.477 at the noble gases). The two are different observables, a wave in properties against a ridge in the peel, but any addition to the table has to state both and say why they differ. Not reconciled yet.
3. **The one third appears twice.** The row constant H_p ≈ ⅓(IE_noble − IE_alkali) (8.9, open) and the share of the first book on the half line (22.2). Question only; no test run.

## 6. Still owed

- The June IQGT version with the contractive operator (not in the 12 June file; the other June files were not opened).
- Open Math's builds were not used anywhere here.
