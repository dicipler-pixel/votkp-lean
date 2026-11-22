# From Beasley's face apex to an atomic projector overlap
**Jeromie Beasley's element paper · worked microscopic comparison.**

The ball notes assign the dimensionless face apex a=tanh(r/4) to a step r=ln z. In a particular atomic model this quantity has a direct operational meaning. Consider a same-mass, nonrelativistic, one-electron Coulomb Hamiltonian before and after a sudden scale change α→β. Compare like hydrogenic levels (same n,l,m). Their binding energies scale as α² and β², hence z=(β/α)² and **a=(β−α)/(β+α)**. Measure the probability of finding the same orbital label in the new Hamiltonian. For pure states this is the trace of the product of the two rank-one projectors. The old and new orbitals must share a centre and orientation. The observable depends on which orbital was occupied.

| Prepared orbital | Same-orbital survival probability, t=1−a² | z=4 |
|---|---:|---:|
| 1s | t³ | 512/729 = 0.702332 |
| 2s | t³(1−3a²)² | 2048/6561 = 0.312148 |
| 2p, same m | t⁵ | 32768/59049 = 0.554929 |
| any circular n,l=n−1 | t^(2n+1) | (8/9)^(2n+1) |

**How to derive the powers.** The 1s overlap integral is 8(αβ)^(3/2)/(α+β)³, so the squared overlap is t³=sech⁶(r/4). For a circular orbital its radial function is a normalized constant times R^(n−1) exp(−αR/n). The radial measure adds R². Integration of R^(2n) exp[−(α+β)R/n] gives (2n)! [n/(α+β)]^(2n+1); divide by the two individual norm factors to get overlap [2√(αβ)/(α+β)]^(2n+1) and square it. For 2s the radial polynomial is 2−αR. Expanding the product of the two polynomials uses the second, third and fourth moments of the exponential. Its signed overlap becomes t^(3/2)(1−3a²). The node of this overlap occurs at β/α=2+√3 or its reciprocal. The 2p overlap has no such zero for finite positive scales. This is a concrete example of the information held by the orbital beyond the scalar face coordinate.

**At the exact geometric wall,** β/α=1+√2, a=√2−1. The 1s survival probability is 8(5√2−7)=0.568542495, while the 2s and 2p results are 0.133890627 and 0.390185882. At z=4 the two n=2 orbitals have exactly the same binding energies in each ideal Coulomb Hamiltonian and hence the very same pair of clocks. Their probabilities already straddle 1/2. This refutes a universal interpretation of the peel wall as the half-survival boundary for an arbitrary atomic orbital.

**A microscopic check on the intrinsic distance parameter.** For circular n, the expansion of t^(2n+1)=sech^(4n+2)(r/4) is 1−(2n+1)r²/16+O(r⁴). The coefficient of the local projector fidelity is specific to this chosen family and energy coordinate. No assertion about the ambient IQGT, nor a replacement spacetime geometry, follows. The low-order coefficient is directly testable against the projector overlap for the specified scale family.

The 1s→1s probability at z=4 is the familiar ideal tritium sudden-charge example. Source: [Tong, Applications of Quantum Mechanics](https://www.damtp.cam.ac.uk/user/tong/aqm/aqm.pdf). The contribution here connects Jeromie's exact **face apex** to a familiar atomic projector observable and uses the nodal and circular states to determine the connection's scope. Experimental charge fractions sum over several states; they do not themselves measure this orbital-resolved probability. Ground-state ionization ladders of a fixed many-electron nucleus represent another operation. If applying this microscopic formula there, a reader would need the actual projection and change of Hamiltonian.

The orbital_check.py program evaluates the normalized general Laguerre radial functions and integrates them independently at 70 settings, including reversed scales and the 2s node. FaceFidelity.lean certifies the rational algebra after performing the 1s radial integral. The integral derivation and the physical assumptions are supplied here. [Jeromie's branch description of the face apex](https://github.com/dicipler-pixel/votkp-lean/blob/893bd1018b22fcc575194196975fc9650d2006fb/research/2026-11-20-element-paper-loop-wall/gpt_batches/batch4_S_to_Ca.md)
