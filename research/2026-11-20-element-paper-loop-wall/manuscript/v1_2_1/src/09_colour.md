## Colour and the half-power line

*This section is written with Elizabeth Johnson, whose Mixin colour system my colour work builds on. Her readings are credited to her by name; the algebra that maps them onto the peel is marked.*

### The colour line

The complex optical coordinate of my Volume paper is $(1-N)/(1+N)$, where $N = n+i\kappa$ is the complex refractive index: the same Smith form as the peel, with the index in place of the clock ratio. At normal incidence from vacuum on a homogeneous non-magnetic half-space its squared modulus is the reflectance,
$$R = |\Gamma_{\text{opt}}|^2 = \frac{(n-1)^2+\kappa^2}{(n+1)^2+\kappa^2},$$
and $R-\tfrac12$ has the sign of $(n-3)^2+\kappa^2-8$ (Lean: `circle_identity` in `OpticalWall.lean`). The half-power circle $|\Gamma|^2 = \tfrac12$ is the same circle as the loop wall on my Smith disc.

**MEASURED INPUTS, DERIVED CALL.** Averaged over the visible band, **all 35 metals with optical data reflect above $|\Gamma|^2 = \tfrac12$, and none of the 6 non-metals do.** Niobium is the closest metal (0.5026) and tellurium the closest non-metal (0.4940). The data are the refractive-index sets used in my vacuum-disk paper (v6). The source also reports that phase gaps predict thin-film colour differences among 39 pairs similar in bulk, with rank correlation 0.64, and in a finite-film closure test a frozen reflection threshold $|\Gamma| = 0.856$ scored 87% on 171 film cases. The same number one half appears for the isolated atom's ladder and for the bulk metal's mirror, but they are different inputs and different detectors; the colour line is a classification of metals by their optical response, not a consequence of the atomic peel. The osmium control makes this concrete: at 650 nm the two principal polarisations of one osmium crystal give 0.48460 and 0.52845, straddling the half-power line while the isolated-atom ladder is unchanged.

![Left: visible-average reflectance $|\Gamma|^2$ for the 41 elements with optical data; all 35 metals (gold) sit above one half and all 6 non-metals (blue) below. Right: Elizabeth Johnson's gap ladder read as peel steps; the wall falls between her 4:1 and 6:1 rungs.](../figs/fig06_colour.png)

### Mixin and the wall circle

In my polarisation encoding of Elizabeth's Mixin labels (the mixin-colors repository), the secondary colours come out at a degree of polarisation $1/\sqrt2$. That is a circle of radius $1/\sqrt2$ on the polarisation sphere — a different disc from my Smith disc, so this is a match of numbers, not of objects. Whether colour perception reads that circle as a boundary is **OPEN**.

### Elizabeth's reading of the step

Elizabeth's notebook pages describe how a reaction chain lights and runs. I record her model in her terms and mark where it meets the peel.

**Matter and memory.** She writes matter as positive, giving shell and sections, and memory as negative, the recipe; matter and memory together make the firework. I write the same split in my two books: the positive book $E^+ = (\Sigma IE)^2$ is the shell, and the negative book $E^- = (\Delta IE)^2$ is the record of the step.

**The drum.** Her page reads: to go from 3 : 7 to 10 requires a 4 drum to get 3 to activate 7. For the pair 3 and 7, the 4 is the difference and the 10 is the sum, so
$$\Gamma = \frac{7-3}{7+3} = \frac{4}{10},\qquad \frac{E^-}{E^+} = \frac{16}{100}.$$
Her drum is the difference face and her ten is the sum face: this is my reflection written in her own terms. **DERIVED.**

**The monad at the midpoint.** I place the monad — the still point of a step — at the midpoint of the pair. For 3 and 7 the midpoint is 5 and half the gap is 2, so $\Gamma = 2/5$: the reflection is half the gap measured against the midpoint, and the stillness sits exactly in the middle, as Russell's fulcrum does.

**The pilot hole.** In her drawing a memory photon runs ahead from A to B, finds the best path, and returns to A before matter makes the run. A wave that goes out and comes back is a reflection, and $\Gamma$ is a reflection coefficient. Her picture reads $\Gamma$ as the returning echo that sets the path. **RECOGNISED** as a structural reading.

**Her gap ladder.** She writes ratios by gap, 2 : 1, 4 : 1, 6 : 1, 8 : 1, with the gap as the oxygen amount, running from "easier" at 2 to "harder" at 10, and 1 : 1 as "furthest away from itself". Read as peel steps $z$:

| Her ratio | $\Gamma^2$ | Side of the wall |
|---|---|---|
| 1 : 1 | 0 | matched, nothing reflected |
| 2 : 1 | 0.111 | inside |
| 4 : 1 | 0.360 | inside |
| 6 : 1 | 0.510 | outside |
| 8 : 1 | 0.605 | outside |

The wall at 5.83 falls between her 4 and her 6; her page marks 2 as easier and 10 as harder. **DERIVED** as a structural match, not a test. Her page calls kindling a twin segment with many gaps and firewood segments with few, and her grid runs in columns headed 3, 7 and 9. I read this, as my interpretation, through her prime work: those are last digits of primes above 5, and a twin segment would be a twin-prime gap of 2, her tinder. Her even ladder is not ordinary fuel chemistry: alkanes take $(3n+1)/2$ oxygen molecules per fuel molecule (2, 3.5, 5, 6.5, 8 from methane to pentane), so the two ladders meet only at methane's 2 : 1 and pentane's 8 : 1.

**Fastest or maximum energy.** She writes that efficiency is fastest or maximum energy, and cannot be both. For steady-running heat engines this is a known trade-off: power and efficiency cannot both be maximised (Shiraishi, Saito and Tasaki 2016; Pietzonka and Seifert 2018), and a recent Pareto-front result bounds the efficiency at maximum power by one half of the maximum efficiency, with zero power at maximum efficiency. Whether that one half and my half-power wall are the same line is **OPEN**, untested.

**Questions she asked me in our conversation, answered.** Layered: yes — the shells are layered, and each peel step goes from one layer to the next. Moving in parallel like conveyor belts: nothing in the data shows it yet; it is a picture to test. An inserted charge: yes — each removal leaves the ion one charge more positive, which pulls every remaining electron in and restructures the whole at every step. "Too close to the ceiling": a step that jumps too far; past a ratio of 5.83 the loop cannot close, and the steps that do this are the breaks into a closed inner core. The speed of light and the charge: not the same thing, but they meet in one number, the fine-structure constant $\alpha\approx1/137$ — the charge squared over the speed of light and Planck's constant — which enters this paper as the $(Z\alpha)^2$ spinor correction of the heavy hydrogen-like ions. The squaring in my formulas turns a strength into an energy, which is why one half is the line.

**OPEN.** The preregistered blind colour test — Elizabeth's colour readings scored against the wall circle before either of us sees the other's calls — still needs her readings.
