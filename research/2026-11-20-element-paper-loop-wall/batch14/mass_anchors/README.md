# Which part of the peel vector fixes an energetic decay direction?

**MEASURED inputs.** For holmium-163 and dysprosium-163, the 2024 PENTATRAP experiment measured the cyclotron-frequency ratio at q=38, 39, and 40. For equal charge, R=ν(Dy)/ν(Ho)=M(Ho)/M(Dy), so the ionic ground-mass energy gap at the measured charge is directly (R−1)M(Dy)c². The published neutral Q also uses electronic binding calculations. Here we restart separately from each of the three raw measured frequency ratios, without using either the neutral Q or the paper’s computed difference of electronic bindings. Their measured values and uncertainties appear in Table 2. The three starts share a mass reference and the subsequent ionization inputs. [Schweiger et al., Table 2](https://repository.gsi.de/record/353513/files/s41567-024-02461-9-1.pdf?subformat=pdfa) · [NIST Dy-163 mass](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=Dy)

**DERIVED.** To make the size of the margin explicit, put the entire ion mass between 162.89 and 162.93 u and the energy per u between 931 and 932 MeV. Both deliberately broad ranges enclose the tabulated estimates. Removing at most 40 electrons of mass <0.00055 u from the neutral atom, with positive binding corrections, preserves the lower bound. Each of those removals costs far below an electron rest energy, so the neutral mass is an upper bound. For each anchor, apply the two archived energy ladders from that anchor upwards and add the endpoint widths for a full input rectangle. No probability for that rectangle is assumed. [CODATA 2022](https://physics.nist.gov/cuu/Constants/) · [All three runs](direct_trap_bounds.csv)

| Direct trap anchor | Q(56) interval, eV | Q(57) interval, eV |
|---|---:|---:|
| q=38 | [1770.43, 2068.88] | [−4709.57, −4391.12] |
| q=39 | [1774.09, 2061.60] | [−4705.91, −4398.40] |
| q=40 | [1782.87, 2054.25] | [−4697.13, −4405.75] |

Each path puts the sign change at the same charge. This calculation predicts an energetic ordering. It supplies no event count, nuclear matrix element, branching fraction or lifetime at 56+ or 57+. The measured reverse decay in bare Dy occurs at 66+. [Original storage-ring observation](https://doi.org/10.1103/PhysRevLett.69.2164)

**DERIVED, scale control.** Holding the neutral mass gap Q(0) fixed, multiply every ionization energy of *both* species by the same positive number c. Every ratio, every signed Γ, every log-shape entry, and every geometric wall label is preserved. The mass ordering becomes Q(q;c)=Q(0)+c[Q(q;1)−Q(0)]. At 57+, the central expression is 2863.2−7381.793561c eV. The signs are opposite for c=1 and c=0.01. At c=0.01 the central ordering in fact stays positive at all 67 charges. With the physical energies and measured neutral gap it reverses. A positive rescaling is an identifiability control on a mathematical input, with Q(0) and the units fixed. It does not correspond to a change of units or describe a new dysprosium atom.

**DERIVED.** Keeping the entire observed central sign sequence requires approximately 0.407469 < c < 2.570674, with the exact constraints coming from q=60 and q=39 respectively. A physical conclusion needs the absolute energy scales and a nuclear mass anchor. Given the first ionization energy I₁ and the directed steps of each species, Iₖ=I₁∏ⱼ₌₁ᵏ⁻¹zⱼ recovers every absolute rung, and the cross-isobar sum recovers the mass change. This specifies what Jeromie’s directed record can encode and what an experiment must supply.

[Source calculation and scale control](check.py) · [Four core Lean theorems](ShapeScale.lean) · [Lean 4.34.1 axiom output](lean_run.txt) · [Full neutral-anchored mass table](../materials/holmium_dysprosium_decay.md)
