# A lower bound on rubidium's long-range reading from the occupied pocket

**DERIVED · question and failure conditions.** Can the first-shell weights say how much of the longer-range signal comes from occupied electronic states being carried into empty states? Fix a uniform Bloch mesh with binary occupations and one translation-compatible wavevector. Reject the quantitative bound if the mesh cannot be reconstructed, the band and filling are ambiguous beyond the stated enclosure, or the phase operator fails to map one Bloch fibre unitarily to the translated fibre. Compare finite-mesh lower bounds, continuum slopes of specified interpolated dispersions and orbit-based constraints separately.

## A bound independent of the orbital texture

**DERIVED.** In a fixed periodic supercell, the full-position phase $U_q=e^{iq\cdot x}$ maps the single-particle fibre at $k$ unitarily onto the fibre at $k+q$. So does the Wigner–Seitz cell-centre phase $U_{q,c}$ when the whole partition translates with the lattice. Write $P_k$ for the occupied projection and $r_k$ for its rank. For either phase its leakage on that fibre is
$$
 \ell_k=\|(1-P_{k+q})U_qP_k\|_{\mathrm{HS}}^2
       =r_k-\|P_{k+q}U_qP_k\|_{\mathrm{HS}}^2
       \ge (r_k-r_{k+q})_+.
$$
The product of contractions has singular values at most one and rank at most $\min(r_k,r_{k+q})$. Consequently the directional readout per electron satisfies
$$
 L_q\ge L_q^{\rm rank}:=\frac{\sum_k(r_k-r_{k+q})_+}{|q|^2\sum_k r_k}.
$$
For rubidium's selected outer subspace $r_k$ is zero or one per spin. Each occupied state shifted into an empty fibre contributes exactly one to the numerator. The remaining leakage is nonnegative and measures occupied-to-occupied orbital mismatch. Spin degeneracy cancels in the quotient. For krypton's constant-rank filled manifold this lower bound vanishes. The material's actual leakage can be positive.

**DERIVED · finite-mesh result.** The direct calculation uses archived **eigenvalues**, with no orbital interpolation. The original PAW files reconstruct all cubic symmetry images and supply their integration multiplicities. Verified below every half-filling cut are four semicore bands; the sixth band is above every cut. The unshifted meshes can put a degenerate shell at the Fermi energy. We treat all states within $10^{-7}$ eV of the centre of the last-occupied/first-empty pair as ambiguous. A guaranteed crossing has a certainly occupied source and a certainly empty target. The upper count allows all possible assignments of the ambiguity and bounds the rank term only. These are conditional bounds over Bloch-diagonal, spin-symmetric choices at fixed half filling.

| Crystal input | Reciprocal mesh | Directional step | Guaranteed crossings / occupied per spin | Minimum full-position $L_q$ (Å²/electron) |
|---|---:|---|---:|---:|
| 297 K geometry | 48³ | (110), 0.03247721 Å⁻¹ | 1,935 / 55,296 | 33.17643 |
| 297 K geometry | 48³ | (200), 0.04592972 Å⁻¹ | 2,769 / 55,296 | 23.73787 |
| 297 K geometry | 48³ | (222), 0.07955260 Å⁻¹ | 4,843 / 55,296 | 13.83923 |
| 5 K geometry | 40³ | (110), 0.03977514 Å⁻¹ | 1,339 / 32,000 | 26.44887 |

**DERIVED · read the table.** At 48³ along [110] the outer-band rank term is enclosed between 33.17643 and 33.99942 Å². Only the lower endpoint applies to both the full-position and cell-centre total. The 297 K and 5 K labels refer to the underlying crystallographic inputs. Both projector occupations are taken at zero temperature. All three directions and all ten meshes appear in [rank_flow.csv](rank_flow.csv). [Archived input hashes](../../batch8/material_transport/band_inputs.sha256)

## Why this term grows in a metal with a regular Fermi pocket

**DERIVED · continuum hypotheses.** Take the continuum Brillouin-zone measure before $q\to0$. For a bounded single occupied pocket $\Omega$ with piecewise smooth boundary, a translation $q=t u$, $|u|=1$, gives
$$
 t L_{tu}^{\rm rank}
 =\frac{|\Omega\setminus(\Omega-tu)|}{t|\Omega|}
 \longrightarrow
 C(u):=\frac{1}{|\Omega|}\int_{\partial\Omega} (u\cdot n)_+\,dS.
$$
A boundary patch loses a slab of thickness $t(u\cdot n)_+$ to first order. Equivalently, integrate outgoing crossings over lines parallel to $u$. The same derivative is expressed by the directional variation of the set's covariogram. The expression also applies per period on a reciprocal torus with regular boundary. A strictly positive $C(u)$ forces growth at least as $C(u)/t$ for the stated projector reading. For a spherical pocket one obtains $tL_{tu}^{\rm rank}=3/(4k_F)-t^2/(16k_F^3)$ for $0<t<2k_F$ from the intersection volume of two spheres. A gapped, constant-rank Bloch projector has no such term. The material's remaining orbital texture enters the full reading. [Galerne (2011), Eq. (3) and Theorem 13](https://www.ias-iss.org/ojs/IAS/article/view/22)

**DERIVED · model evaluation.** On each periodic tetrahedron linearly interpolate the original band energies. Fix the chemical potential by the half-filled volume, keeping the crystal symmetry and primitive lattice. For an area facet on $\epsilon=\mu$ its outgoing projected area can be integrated using $\delta(\mu-\epsilon)(u\cdot\nabla_k\epsilon)_+$. The script reuses the repository's isoenergy slice formula, retaining incoming and outgoing flux independently. Uniform energy units cancel. Four primitive-cube diagonals probe triangulation sensitivity. A deliberately unbounded slab on the reciprocal torus with $\epsilon=-\cos(2\pi k_x)$ tests the general flux formula along three directions; its exact normalized outgoing area is $2|u_x|$ in a unit reciprocal cell.

| 297 K geometry, 48³ underlying eigenvalues | Minimum $C$ across the four triangulations, Å | Maximum $C$, Å |
|---|---:|---:|
| [100] | 1.102471 | 1.103745 |
| [110] | 1.092883 | 1.093825 |
| [111] | 1.107806 | 1.108972 |

**DERIVED · scope of the limit.** A positive limiting coefficient for a specified interpolant is a conditional consequence of its regular Fermi surface. In the finite 48³ calculation along [110] the rank-only $|q|L_q$ interval is 1.07748–1.10421 Å; it contains all four continuum estimates. Limits along an arbitrary discrete twist sequence require their own sampling control. [Tetrahedron calculations](rank_slope.csv) · [Archived independent Fermi-surface method](../../batch8/material_transport/README.md)

## What the oscillation experiment can constrain

**MEASURED · inputs.** Shoenberg and Stiles measured rubidium's de Haas–van Alphen oscillations. Table III in Lee gives the corresponding fractional extremal area excesses in units of $10^{-4}$ along [100], [110], [111] as $+38.4,-27.9,+56.5$, each with quoted uncertainty 2.2. The independent cold crystallographic input is $a=5.585$ Å. [Shoenberg and Stiles (1964)](https://doi.org/10.1098/rspa.1964.0169) · [Lee (1969), Table III](https://doi.org/10.1103/PhysRev.178.953) · [5 K structure](https://www.crystallography.net/cod/9011008.html)

**DERIVED · condition.** Take one bounded regular quasiparticle pocket with one conduction electron per body-centred-cubic primitive cell including both spin copies. A plane section perpendicular to $u$ projects into the pocket's footprint; each intersected line has at least one exit. Therefore $C(u)\ge A_{\rm section}(u)/|\Omega|$. The equality can fail for pockets with overhangs or multiple intersections. An open tube winding around the reciprocal torus would invalidate the bounded-pocket argument. This comparison concerns an idempotent quasiparticle projector constructed from the pocket; the observed frequency is not a many-body localization measurement.

**DERIVED · numerical lower estimates.** With $k_0=(3\pi^2/(a^3/2))^{1/3}=0.6979010$ Å⁻¹, $A_0/|\Omega|=3/(4k_0)$. Multiplying by each measured $A/A_0$ gives lower-side readings $1.078778,1.071653,1.080723$ Å, respectively. Each has a propagated area-input uncertainty of $0.000236$ Å at fixed lattice parameter and filling. The orbit constrains one side; its uncertainty does not give a two-sided interval on $C$. The cold PBE bands are independent inputs, with their own limitations.

**DERIVED · independent cold-surface test.** To check the sensitivity of the tetrahedron result, fit a periodic cubic spline to the same cold eigenvalues. Use the earlier volume-matched chemical potential. Along rays from the pocket centre solve for the Fermi radius, triangulate the resulting surface, and add the positive projected triangle areas. This allows overhangs in the line-of-sight projection. Orient each angular mesh around the tested direction and retain its equatorial section independently. A sphere with the same mesh has a known polygon-area error. The 96×192 and 192×384 angular meshes on the 40³ cold band give $C_{[110]}=1.0696133$ and $1.0697569$ Å. The latter sphere-control discretization error is $-0.0000480$ Å. Both values fall below the experimental orbit-derived lower estimate even at its low end, 1.0714163 Å. The 40³ linear-tetrahedron answers span 1.0703019–1.0716613 Å. That range overlaps the experimental comparison at its upper end. Thus the smooth PBE estimate undershoots this directional area constraint; the conclusion at the narrow experimental uncertainty depends on numerical representation. All variants retain a positive outgoing area. [Independent triangulated pocket](orbit_slope.csv) · [Source cold bands and orbit controls](../../batch8/material_transport/Rb_cold_orbits.csv)

## Reproduce the bounds

From this directory run the following. NumPy and SciPy are required; the scripts reuse the branch's checked band-grid and isoenergy routines. Input hashes are recorded in the earlier material folder. Results are reported to more digits in the CSV for replay.


    OPENBLAS_NUM_THREADS=1 python3 rank_flow.py > rank_flow.csv
    OPENBLAS_NUM_THREADS=1 python3 rank_slope.py > rank_slope.csv
    OPENBLAS_NUM_THREADS=1 python3 orbit_slope.py > orbit_slope.csv
