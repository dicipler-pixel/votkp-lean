# How far do the same projector weights reach?

**DERIVED · question.** The nearest-shell share counts the fraction of the off-site projector weight reaching the first neighbours. The second moment weights those same links by squared distance. We can test the difference with two systems whose exact occupied states and electrical phases are independently known. We can also bound how much replacing a continuous position by its cell centre affects a periodic position reading.

**DERIVED · scope.** The earlier rubidium and krypton wavefunctions were cut into **geometric Wigner–Seitz regions of real space**. Each region consists of the positions closest to its lattice site. These data support both a weight between spatial regions and, given the wavefunctions themselves, an additional phase-sensitive readout using positions inside each region. A projection onto atomic orbitals or a zero-flux electron-density basin would require a different partition. [Original material implementation](../../batch8/ws_control/README.md)

## What was fixed before reading the material weights

* **DERIVED · normalization control.** For a translationally invariant idempotent occupied projector on a finite torus, let ν be electrons per primitive cell, including precisely the spin channels included in the weights. The complete spatial block weights obey Σ_R X(R)=ν. The site-centre second-moment tensor per electron uses Σ_R X(R)R⊗R/(2ν). Repeating a spin channel doubles its weight and ν and leaves the per-electron answer unchanged. A failed sum rule, asymmetry X(R)≠X(−R), or negative weight beyond numerical tolerance invalidates the check.
* **DERIVED · geometry control.** For a periodic mesh, choose the shortest Cartesian representative of each translation. Average the dyads of all tied representatives. Tie choices preserve length and can alter off-diagonal components. A primitive parallelepiped can be skew, so wrapping each primitive coordinate individually is insufficient to find a shortest Cartesian representative. The checker exhausts an image cube with provably sufficient extent using the smallest singular value of the primitive lattice matrix.
* **DERIVED · phase control.** A second distance on a ring is its chord. A common twist, a finite sampling mesh, and a chosen site partition pertain to the same projector when comparing estimators. Reject reconstruction if a direct occupied-to-empty phase overlap and its weight sum disagree for the soluble models. Check the clustering versus extended behavior separately from the value of the shell share.

## Two exact chains

**DERIVED.** Both chains use a lattice spacing $a$, one spin copy, and a ring of $N=4m+2$ sites. For one origin define $B=\sum_{r\ne0}X_r$, $S_1=(X_1+X_{N-1})/B$ and
$$
 L(d)=\frac{1}{2\nu}\sum_r X_r d_r^2.
$$
Use either the shortest length $d_r=a\min(r,N-r)$ or the chord $d_r=Na|\sin(\pi r/N)|/\pi$. Lengths squared in the table are in $a^2$.

| Model | Shell share as N grows | Shortest-image second moment | Periodic chord second moment |
|---|---:|---:|---:|
| Half-filled nearest-neighbour hopping chain | $8/\pi^2\approx0.81057$ | $L/N\to a^2\ln(2)/\pi^2$ | $Na^2/(2\pi^2)$ exactly |
| Filled bonding band of isolated dimers across cells | $1$ exactly | $a^2/4$ exactly | $\frac{a^2}{4}[N\sin(\pi/N)/\pi]^2\to a^2/4$ |

**DERIVED · hopping chain.** Fill the modes $k_j=2\pi j/(Na)$, $j=-m,\ldots,m$, of $E(k)=-2t\cos(ka)$, $t>0$. The thermodynamic dispersion crosses its Fermi energy with nonzero velocity. There are $N/2$ electrons. The finite Fourier sum gives $P_{00}=1/2$ and
$$
 X_r=|P_{0r}|^2=\frac{\sin^2(\pi r/2)}{N^2\sin^2(\pi r/N)}\quad (r\ne0).
$$
Thus $B=1/4$ and $S_1=8/[N\sin(\pi/N)]^2$. Each odd $r$ contributes $a^2/\pi^2$ to the chord sum and exactly $N/2$ residues are odd. With shortest images, the corresponding Riemann sum gives $L/(Na^2)\to\int_0^{1/2}x^2\csc^2(\pi x)\,dx=\ln 2/\pi^2$, by integration by parts and $\int_0^{\pi/2}\ln(\sin x)dx=-(\pi/2)\ln2$.

**DERIVED · gapped dimer band.** Put two local orbitals in each cell, with hopping only from $A_j$ to $B_{j+1}$ and its adjoint. The levels are $\pm t$ for all momenta. Filling one bonding state per cell gives $P_{00}=I_2/2$, $X_0=1/2$, and $X_{\pm1}=1/4$. Every other $X_r$ vanishes. Substitution yields the second row. Both systems pass the shell-share test $S_1>1/3$; only the metallic model's second moment grows without bound here.

## Exact bound for replacing positions with cell centres

**DERIVED · hypotheses.** Use the *same* finite-rank orthogonal one-electron projector $P$ with $N_e=\operatorname{Tr}P>0$, a fixed partition with $c(x)$ the centre of the cell containing $x$, and $|x-c(x)|\le\rho$ for the local representative. On a torus require that $q\ne0$ be compatible with its periods. Define $U(x)=e^{iq\cdot x}$, $U_c(x)=e^{iq\cdot c(x)}$, and the directional readout
$$
 L_q(U)=\frac{\|(1-P)UP\|_{\rm HS}^2}{N_e|q|^2}.
$$
For a cell-constant phase, $\|[P,U_c]\|_{\rm HS}^2=2\|(1-P)U_cP\|_{\rm HS}^2$ by unitarity and cyclicity of the trace. The commutator in spatial blocks has entries $P_{ij}(U_{c,j}-U_{c,i})$. Therefore $L_q(U_c)$ is exactly the link-weight sum with squared chord $4\sin^2[q\cdot(c_i-c_j)/2]/|q|^2$ and $1/(2N_e)$ normalization in the sum over all ordered site pairs.

**DERIVED · inequality.** The reverse triangle inequality for the Hilbert–Schmidt norm gives
$$
 \left|\sqrt{L_q(U)}-\sqrt{L_q(U_c)}\right|
 \le\frac{\|(1-P)(U-U_c)P\|_{\rm HS}}{|q|\sqrt{N_e}}
 \le\frac{\|U-U_c\|_{\rm op}}{|q|}
 \le\rho .
$$
The final bound uses $|e^{is}-e^{it}|\le|s-t|$. The radius can be replaced by the maximum **directional** intracell displacement. Consequently a uniformly bounded cell radius preserves boundedness or divergence of these matched directional square-root readings along any sequence of meshes. Numerical finite values can differ appreciably. A nonidempotent occupation matrix or changing occupied span between the two calculations breaks the hypotheses. With a pair of local point orbitals at $c_j\pm\rho$, occupy only their equal bonding combination. The centre result vanishes while $L_q(U)=\sin^2(|q|\rho)/|q|^2\to\rho^2$. This limiting control attains the bound and preserves a real intra-cell spread that cannot be inferred from the off-site shell share.

**DERIVED · shortest-image bridge.** For fixed primitive lattice matrix $A$ with primitive vectors as rows, let $\kappa=s_{\max}(A)/s_{\min}(A)$. On an $M^3$ torus use the three primitive reciprocal covectors $q_i=(2\pi/M)A^{-T}_{i,:}$. Let $D$ be the shortest Cartesian length for a displacement, and $d_i=2|\sin(q_i\cdot R/2)|/|q_i|$. Then
$$
 \frac{4}{\pi^2\kappa^2}D^2
 \ \le\ \sum_{i=1}^3 d_i^2
 \ \le\ \kappa^2 D^2.
$$
Indeed write the wrapped fractional-supercell displacement as $u\in[-1/2,1/2]^3$. Then $Ms_{\min}|u|\le D\le Ms_{\max}|u|$, because $u$ is coordinatewise nearest to zero in Euclidean fractional coordinates. Each reciprocal row norm of $A^{-T}$ lies between $1/s_{\max}$ and $1/s_{\min}$; apply $2|u_i|\le|\sin(\pi u_i)|\le\pi|u_i|$. Multiply by $X(R)/(2\nu)\ge0$ and sum. The *trace* of the shortest-image tensor is uniformly comparable to the sum of the three matched cell-centre directional chords. Combined with the bounded-radius result this gives the same boundedness criterion as the sum of the three full-position phase readings along fixed-shape meshes. The constants do not identify the two finite values, a divergence rate, a dc conductivity, or an experimental phase transition.

## Independent material check and experimental scope

**DERIVED · reproducibility.** The second script independently reconstructs all tensor components, the first-shell share, and the three primitive reciprocal chord readings from the full spatial-weight cubes in the sibling calculation. Each real-space weight cube is the shared input; its quantum-chemistry wavefunctions were generated by the material calculation. These two scripts can be rerun from this directory.

```sh
OPENBLAS_NUM_THREADS=1 python3 localization_controls.py > finite_controls.csv
OPENBLAS_NUM_THREADS=1 python3 verify_material_weights.py > material_check.csv
```

**DERIVED · values.** For the 75 Ry norm-conserving outer-subspace calculation, rubidium's shortest-image trace divided by three rises from 5.7043606170 to 7.9951856988 Å² per electron from $4^3$ to $6^3$; krypton's changes from 0.0732240204 to 0.0732704240 Å². Their nearest-shell shares at $6^3$ are 0.4775584435 and 0.9909584083. The measurements used here are the lattice parameters supplied to the electronic models. A trend on these meshes is a finite-size result. The analytic implications above apply if a bounded or divergent sequence is subsequently established. [Numerical rows](material_check.csv) · [Model rows](finite_controls.csv) · [Original spatial partition](../../batch8/nc_control/README.md)

**RECOGNISED · physical comparison and falsifier.** In the zero-temperature thermodynamic treatment of Souza, Wilkens and Martin, their Equation 49 relates the position cumulant to the inverse-frequency moment of the optical conductivity. A quantitative experimental comparison would require the physical position operator, the corresponding electron count and full optical spectral weight, polarization, low-frequency limits and a treatment of the Drude contribution. Band-limited optical data, a smooth pseudo-wavefunction subspace or a pair of finite-mesh cell-centre values alone do not provide that comparison. Likewise the finite-$q$ projector leakage here measures a sum of squared overlaps. Resta–Sorella's many-electron polarization uses a logarithm of an overlap; on the partially filled translation-invariant ring a reciprocal step shifts one electron across the occupied boundary, so the determinant vanishes even for a finite mesh while the leakage estimator is finite. [Souza, Wilkens and Martin (2000), §§IV–V](https://arxiv.org/pdf/cond-mat/9911007) · [Resta and Sorella (1999)](https://doi.org/10.1103/PhysRevLett.82.370)

**DERIVED · independent extension.** On the room-geometry 48³ rubidium band mesh, the [110] phase step forces a directional second moment of at least 33.58792 Å²/electron even before orbital overlaps are supplied. The discrete rank term has 1,959 exits for every filling of the ambiguous Fermi-level sites. The proof counts the occupied fibres carried into empty ones and handles all assignments of the Fermi-level tie. [Rank-flow calculation and comparison with quantum oscillations](RANK_FLOW.md)

**DERIVED · mainstream-blend watch.** In three-dimensional Coulomb matter the screened static charge weight and transverse optical weight use different integrands. Smith's 24 measured rubidium index pairs let us compute both and apply the directed wall to their frequency-by-frequency ratio, with three distinct crossing brackets. [Screened and optical tests](SCREENED_OPTICS.md)
