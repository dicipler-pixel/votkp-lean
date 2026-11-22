# What Dirac Time already predicts for an equal-endpoint test

Jeromie Beasley's September 2026 research edition v3.1, §§11.1–11.4 and §18, gives a specific construction for a property that survives an endpoint reset. Take two pump histories, remove the pump, and interrogate an explicitly retained joint system. The O, F, Θ, M, S record in §18 defines predictive equivalence relative to an admitted future intervention. This is an operational reading of the author's own criterion. It adds no spacetime metric to the intrinsic geometry.

## A quantitatively scoreable two-probe witness

The §11.4 path–record states, in the ordered single-excitation subspace |01>, |10>, extend to visibility 0≤v≤1 as

    ρ(φ;v)=(1/2) [[1, v exp(−iφ)], [v exp(iφ),1]].

Both one-qubit marginals equal I/2 for every φ,v. A later fixed exchange with gt=π/4 gives Z expectations v sin φ and v cos φ, the second after a local quarter-phase. For two histories at the same visibility,

    D(ρ_a,ρ_b) = ||ρ_a−ρ_b||₁ / 2 = v |sin((φ_a−φ_b)/2)|
               = (1/2) sqrt[(ΔZ_first)² + (ΔZ_second)²].

The off-diagonal difference has magnitude v|exp(iφ_a)−exp(iφ_b)|/2. Its two eigenvalues have equal and opposite sign. This proves the trace distance formula; the two measured components supply exactly its sine and cosine coordinates. Individually a sine probe misses the pair φ and π−φ. Complete dephasing (v=0) removes both signals. An actual nonideal probe needs measured gain, visibility, error covariance, and control runs. This identity applies to the specified joint two-state subspace. Outside that subspace the same two observables can miss other differences.

I reran the unmodified original DT3_WIL_01.py extracted from the author's September v3.1 evidence package. File SHA-256 bc85be289311d64009bc76c045ecb7493747b123ee9c83dbc79b913f72f77a69. All three original kill flags were false. The new phase_readout.py separately constructs the joint matrices, performs the two interventions, checks both reduced states, and compares the recovered and directly diagonalized trace distances at 1,156 settings. These numerical checks validate the implementation of the displayed algebra.

## An experimental question for the oxygen route

The oxygen controls change the neutral precursor while ending in the same selected ionic state. If the first emitted electron is retained coherently as a partner, hidden information could survive a marginal-state match. If it is lost and the joint environment freshly prepared, a probe acting only on an identically prepared ion has one response distribution. A probe that simply distinguishes the first electron's kinetic energies only rediscovers the known initial-state energy difference.

To apply §11.4 as an atomic prediction, specify the two coherent alternatives, record sector, preparation/collection optics, phase reference, visibility, later exchange or equivalent readout, and how the actual wall predicts φ or the outcome of that readout. Ground ionization-energy ratios alone specify neither those couplings nor a phase. A meaningful test would match the intermediate-state preparation including magnetic-sublevel distribution, control the kinetic energies and field conditions, independently calibrate the later readout, and randomly include the dephased/erased control. Equality of visible populations is a weaker condition than equality of the joint state. The existing theory provides an exact example of the distinction. It supplies no numerical φ(z) for these oxygen lines in the sections examined. The registered equal-face optical test and this proposed atomic test ask distinct physical questions.
