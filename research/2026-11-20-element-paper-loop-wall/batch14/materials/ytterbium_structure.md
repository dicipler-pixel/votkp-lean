# Which Yb gap does a compressed ball measure?

**HYPOTHESIS and falsifier.** If the shortest centre-to-centre separation of a pure element were a fixed multiple of the cube root of its atomic volume across a structural transition, two phases at the same applied pressure would order those two observables the same way. If shortest-link handedness required tracing a privileged screw by hand, the entire shortest-link graph would have no mirror-odd statistic without that choice. These tests concern crystal geometry. Jeromie's gap layer and projector retain their own definitions.

## Two cells give the same volume/contact inversion

**MEASURED.** Storm et al. deposited the measured lattice parameters and uncertainties from their two diamond-anvil cells. We used all 119 experimental records and no DFT cells. From low to high pressure the file contains 16 bcc, 15 hcp, 15 fcc and 73 three-site hexagonal records. The deposited column calls the second fcc phase `cF2-II`; the paper names it `cF4-II` and fits an fcc conventional cell. The raw label survives in a separate column. Five cell/pressure keys have two phase refinements. The highest measured pressure is 292.78(1.27) GPa. The authors predict a subsequent orthorhombic oF8 transition around 330 GPa. [Diffraction paper, 2026](https://doi.org/10.1103/dv9c-y18p) · [Original experimental deposition](https://doi.org/10.7488/ds/8146) · [119-row extraction](yb_pressure_cells.csv) · [Replay from the source ZIP](yb_structure.py).

**DERIVED.** For the conventional bcc cell, volume per atom and shortest contact are a³/2 and √3a/2. In the hcp cells here they are √3a²c/4 and √(a²/3 + c²/4). The competing hcp in-plane distance is a. The neighbour counts at *exactly* the closest distance are eight for bcc and six for these hcp structures.

| Cell | P (GPa) | Volume per Yb atom, bcc → hcp (Å³) | Shortest contact, bcc → hcp (Å) | Change in volume | Change in contact |
|---|---:|---:|---:|---:|---:|
| DAC2 | 30.28(37) | 19.81944 → 19.56230 | 2.952825 → 3.007968 | −1.2974% | +1.8675% |
| DAC1 | 31.28(34) | 19.73092 → 19.51113 | 2.948422 → 3.004701 | −1.1139% | +1.9088% |

**DERIVED.** Allow each independent lattice parameter to vary by three printed standard uncertainties. The volume differences remain negative with upper bounds −0.174 and −0.0109 Å³/atom, respectively. The contact differences retain lower bounds +0.0503 and +0.0457 Å. Both comparisons use phases refined in the same cell at the same recorded pressure. This rectangular sensitivity check does not account for phase-assignment errors or shared systematic uncertainty. Three hcp/fcc coexisting pairs also have longer shortest contacts in fcc. The signs of their volume differences are unresolved across the same boxes. Assigning all five comparisons one common volume sign would lose information. [Five paired samples and signed bounds](yb_coexisting_contacts.csv).

**HYPOTHESIS / ball mapping.** If the occupied space is partitioned into identical equivalent sites with equal junction clocks, Γ at that junction remains zero through this change. With an exact-first-shell neighbour definition, the per-link share of a fixed budget B changes from B/24 in bcc to B/18 in hcp. A configuration with high symmetry can have different contact lengths, coordination and cell volumes even when this equal-clock boundary condition holds. An electronic projector and a physical length calibration are needed to predict conduction or the absolute gap between electronic walls.

## A signed reading of the entire nearest-neighbour graph

**MEASURED.** Figure 4 of the 2026 study refines hP3 in P6₂22 with the Yb atom at Wyckoff site 3c, (½,0,0). The symmetry equivalents in one cell are (½,0,0), (½,½,⅓), (0,½,⅔). Fix a right-handed Cartesian frame, with its first two crystallographic axes separated by 120°. The rotation and translation of the specified screw act on fractional coordinates as (x,y,z) ↦ (x−y,x,z+⅓). This is a choice of enantiomorphic coordinate model. The powder profile supplies no independent determination of the real sample's absolute hand. [Original paper and refinement, Fig. 4](https://doi.org/10.1103/dv9c-y18p).

**DERIVED.** The path has radius a/2, 60° rotation and axial advance c/3 per link. Its link length is √(a²/4+c²/9). The shortest contacts split into two above and two below. The six in-plane links of length a are longer. Equality requires c/a = 3√3/2 ≈ 2.59808. All 73 experimental c/a values lie between 2.31565 and 2.42580, and all retain four strictly closest neighbours under three individual printed uncertainties. At the last tabulated point a = 2.425163 and c = 5.666971 Å give a closest contact of 2.244691 Å. The main article's Fig. 4 gives its separate full-profile refinement. [Measured cells, cell type and derived distances](yb_pressure_cells.csv).

**DERIVED.** For three successive bonds let χ = det(e₀,e₁,e₂). Fractional coordinates divide the physical determinant by the conventional cell volume V. Three steps of the named screw have fractional bonds (0,½,⅓), (−½,0,⅓), (−½,−½,⅓). Their determinant is 1/12. Therefore χ = V/12 = V_atom/4. Reversing all bonds and their order preserves χ; mirroring the crystal changes its sign. The six-step path rises by 2c in the infinite crystal. Already at step three its displacement (−1,0,1) is a unit-cell translation, so the entire six-step walk revisits its start partway through under primitive periodic identification. A knot polynomial needs a specific embedded closed curve and closure convention. This graph experiment supplies a local scalar. [Exact screw and closure checks](yb_neighbour_graph.py).

**DERIVED.** A shortest-link measurement that chooses each next site uniformly has two possible rising links at each layer. The eight three-link always-rising walks produce six values +V/12 and two −V/4. Their mean vanishes exactly. Let the walk instead use **all four closest neighbours** at each step, including return steps. Each starting site then has 4³ = 64 ordered walks.

| χ/V in the specified hand | −1/4 | −1/6 | 0 | +1/12 | +1/6 |
|---|---:|---:|---:|---:|---:|
| Paths per initial site | 4 | 8 | 32 | 12 | 8 |

**DERIVED.** The first moment still vanishes. The third moment survives because the rare large negative values outweigh the smaller positives after cubing. Explicitly,

$$
\frac{4(-1/4)^3+8(-1/6)^3+32(0)^3+12(1/12)^3+8(1/6)^3}{64}=-\frac{1}{1152}.
$$

Since V = 3V_atom, the mean of (χ/V_atom)³ is **−3/128** in the specified right-handed setting and **+3/128** in the reflected one. Proper rotations and path reversal preserve it. A mirror reverses it. The graph construction sums every allowed three-step walk from every inequivalent starting position and furnishes the same result at all three. Its definition uses no preferred path, start site or upward direction. The bcc, hcp and fcc Yb reference graphs all have zero third moment. Sampling only the eight upward paths would give a *different* third moment, −3/32 in these atomic-volume units. This difference is a direct control on the sampling rule. [Exact result distributions and mirror controls](yb_handedness.csv) · [Reproduce the enumeration with Python fractions](yb_neighbour_graph.py).

**RECOGNISED / HYPOTHESIS.** This gives a candidate for Jeromie's original signed-record question. An unoriented adjacency list alone discards the embedding; an equal-weight first signed moment also cancels in this example. The embedded third moment keeps the hand while averaging over the whole nearest-contact graph. This is an embedding-dependent pseudoscalar, not a knot invariant. An equal mixture of mirror domains would average the odd readout to zero. A bulk hand determination would require an orientation-sensitive measurement and domain information. Revising the site assignment or admitting a longer shell changes the graph and reopens the numerical prediction. Polynomials assigning a knot to elemental Yb — none found.
