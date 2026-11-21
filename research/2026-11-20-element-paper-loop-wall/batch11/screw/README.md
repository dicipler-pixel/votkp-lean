# Tellurium's nearest-neighbour screw

**MEASURED INPUT.** Two deposited models of trigonal tellurium supply the lattice and tellurium fractional coordinates. Adenis, Langer and Lindqvist (1989) give space group 152, P3₁21, with a = 4.456 Å, c = 5.921 Å and u = −0.2636. Wyckoff (1963), as transcribed in the Crystallography Open Database, gives space group 154, P3₂21, with a = 4.44693 Å, c = 5.91492 Å and u = 0.269. These are two separate sources. Each computed mirror below uses the coordinates of its own source. [1989 model and original citation](https://www.crystallography.net/cod/2020222.html) · [1963 model and original citation](https://www.crystallography.net/cod/9008580.html)

**DERIVED.** In a right-handed Cartesian frame, take the hexagonal basis (a,0,0), (−a/2,√3 a/2,0), (0,0,c). Start at fractional position (u,0,w) from the CIF. Apply the ascending nearest-neighbour screw three times without wrapping z. Group 152 uses (−y,x−y,z+⅓), a +120° turn per bond. Group 154 uses (−x+y,−x,z+⅓), a −120° turn per bond. The chain points satisfy p₃ = p₀ + (0,0,c) in Cartesian coordinates. The two nearest periodic neighbours are the preceding and following screw sites. The tabulated third-neighbour distances check that the selected path follows the short covalent chain.

**DERIVED.** Write dⱼ = pⱼ₊₁ − pⱼ. In the ordering (d₀,d₁,d₂), χ = d₀·(d₁×d₂) = s (3√3/2)c(au)² with s = +1 or −1 for the ascending ±120° turn, respectively. The bond length obeys d² = 3(au)² + c²/9. The radial coordinate u enters squared, so its printed sign alone cannot assign the hand. A reverse traversal gives (−d₂,−d₁,−d₀), preserving χ. A Cartesian mirror (x,y,z) ↦ (x,−y,z) has determinant −1 and reverses χ. The values are triple products. Geometric tetrahedron volumes would require division by six.

| Deposited model | Shortest bond (Å) | Next contact (Å) | Bond angle | χ (Å³) | Reversed path (Å³) | Same-coordinate mirror (Å³) |
|---|---:|---:|---:|---:|---:|---:|
| Group 152 | 2.834506 | 3.491173 | 103.1352° | +21.224043 | +21.224043 | −21.224043 |
| Group 154 | 2.860109 | 3.463644 | 102.2878° | −21.990034 | −21.990034 | +21.990034 |

**DERIVED — controls.** Within-source mirroring must reproduce an equal magnitude and opposite sign. Reversing the full path must reproduce the original value. A shorter competing contact would invalidate the nearest-neighbour selection. The script checks each condition, the analytic determinant, and a lower bound on all omitted periodic images. Digits above the input precision aid computational replay. Coordinate uncertainties have not been propagated.

**MEASURED — absolute hand.** Tanaka and co-workers (2010) used circularly polarized resonant diffraction to determine the absolute chirality of their tellurium crystal, assigning group 152. This is an independent experiment on a different specimen. The determinants above identify the hand encoded by each coordinate file. Assigning the physical hand to either historical specimen would require evidence tying that specimen to an absolute-hand determination. [Tanaka et al.](https://doi.org/10.1088/0953-8984/22/12/122201) · [Diamond Light Source experimental account](https://www.diamond.ac.uk/default/Science/Research/Highlights/2010/Forbidden-reflections.html)

**SET ASIDE.** Three screw steps return to a lattice translate. An ordinary closed knot in three-dimensional space needs a specified closure and an isotopy test. The present readout measures a local handedness. Its reversal parity differs from the peel reflection Γ. An optical rotation, a knot identifier, and an elemental knot polynomial do not follow from this determinant.

Run `python3 tellurium_screw.py` in this directory. Both input CIFs and the reference stdout accompany the script. It uses the Python standard library.
