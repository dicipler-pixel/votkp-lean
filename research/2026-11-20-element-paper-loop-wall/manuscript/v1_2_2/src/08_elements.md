## The element test from hydrogen to astatine

The atom is the first place in this programme where the ordered object can be specified without a geometric drawing. For an atom with proton number $Z$, let $I_k$ be the positive energy needed for removal $k$, starting from the isolated neutral ground state; on the ground-state ladder the starting ion has charge $k-1$. Where a usable ground-anion electron affinity exists, I set $I_0 = A$. Removing the electron from the negative ion and ionising the neutral atom are different experiments; their energy ratio supplies the extra zeroth rung, the anion rung. The sign is relative to the order of the two positive costs. There is no ratio after $I_Z$.

**DERIVED.** For neighbouring thresholds $a, b>0$, put $r = \ln(b/a)$, $\Gamma = (b-a)/(b+a)$ and $u = \tanh(r/4)$. Given $\Gamma$, $b/a = (1+\Gamma)/(1-\Gamma)$. A ladder records every adjacent relative change, including which threshold was larger. Its sum of clock differences is fixed by its endpoints, $\sum r_k = \ln(I_Z/I_1)$ for the ordinary ladder, while the interior shape is free. Multiplying all energies by one positive constant leaves the whole relative record intact. The first energy anchors the inverse,
$$I_k = I_1\prod_{j=1}^{k-1}\frac{1+\Gamma_j}{1-\Gamma_j},$$
which is why a prediction involving an absolute isotope mass needs a mass and energy anchor.

**DERIVED.** The two faces of the auxiliary loop meet in the interior when $\Gamma_a^2+\Gamma_b^2<1$, meet at an ideal point at equality, and give an open loop above one. With identical faces, outside means $2\Gamma^2>1$, the exact integer-or-rational test $2(b-a)^2>(b+a)^2$; for positive ratios that is $z<3-2\sqrt2$ or $z>3+2\sqrt2$. Reversal keeps the side and flips the signed reflection: $z = 6$ gives $\Gamma = 5/7$ and $z = 1/6$ gives $\Gamma = -5/7$, both with $\Gamma^2 = 25/49>\tfrac12$. $\Gamma = 2/3$ exactly at $z = 5$, and the hydrogenic one-electron ratio 4 gives $\Gamma = 3/5$ (Lean: `two_thirds_iff`, `hydrogenic_limit`).

**MEASURED INPUTS, DERIVED CALLS.** I reconstructed all 85 vectors from the October threshold archive. The 3,655 positive-index energies are 290 experimental, 847 semiempirical and 2,518 theoretical entries in the archive's grade system; an energy's grade does not fix the leading configuration of either state. Pairing successive removals within each of the 85 atoms gives $3{,}655 - 85 = 3{,}570$ ordinary steps. The full archive adds 2,144 adjacent pairs from radon to oganesson, giving 5,714; both counts exclude anion rungs and excited channels, and heavy-element coverage is incomplete. There are 65 anion rungs in the adopted ledger, and 67 numeric anion rungs when the estimate-grade affinities of dysprosium (0.015 eV) and thulium (0.032 eV, disputed) are added; the samarium lower bound and the preliminary polonium value are scored separately. **Eight ordinary steps and 53 of the 65 adopted anion rungs lie outside the wall** (55 of 67 with the two estimates). Of 3,637 numeric comparisons, 3,614 have two quoted energy widths. If both inputs lie in their quoted ranges and stay positive, the admitted ratios run from $(b-\delta b)/(a+\delta a)$ to $(b+\delta b)/(a-\delta a)$, and all 3,614 keep their wall side across the whole rectangle. Where a rectangle crosses $z = 1$ the minimum squared reflection is zero. The width calculation expresses sensitivity to assumptions on the inputs: quoted error bars provide neither simultaneous confidence nor a known joint correlation model.

![All 3,570 ordinary steps from hydrogen to astatine, as $\Gamma^2$ against atomic number. Eight cross the wall, and every one is the first opening of a closed noble-gas core.](../figs/fig02_steps.png)

### Three boundaries in every element

I read each element at its anion rung ($z_0 = IE_1/EA$, where a bound anion exists) and at each closed-core opening: the last removal above the core, then the first removal from it.

- **K opening** — the opening of the helium-like $1s^2$ core ($2s\to1s$).
- **L opening** — the opening of the neon-like core ($3s\to2p$).
- **Argon-core opening** (the M opening) — $4s\to3p$ for potassium and calcium, and from scandium onward the last $3d$ removal to $3p$. That last kind keeps the principal shell (both are $n = 3$), so its bare hydrogenic ratio is 1, not $16/9$.
- **Krypton-core opening** — the $4s^24p^6$ core, from rubidium on.
- **Xenon-core opening** — the $5s^25p^6$ core, from caesium on.

The full 85-row table of these six boundaries, each cell with $z$ and $\Gamma$, is in the appendix *The element table*. Reading it down the columns (**RECOGNISED**):

- **K opening:** outside from lithium to carbon, crosses inward between carbon (6.08) and nitrogen (5.64), and stays inside from then on.
- **L opening:** outside only at sodium (9.20).
- **Argon-core opening:** outside only at potassium (7.29).
- **Krypton-core opening:** outside only at rubidium (6.53).
- **Xenon-core opening:** outside only at caesium (5.95), the smallest outside ordinary value in the catalogue.

The eight ordinary outside steps from hydrogen to astatine — none new after caesium — are all first core openings: lithium, beryllium, boron and carbon at the helium core, and sodium, potassium, rubidium and caesium at the neon, argon, krypton and xenon cores. A change of shell alone always lands inside: the bare hydrogenic floors $4, 9/4, 16/9, 25/16, 36/25, 49/36$ are all inside. An opening can stand outside only through a departure from the bare shell, which screening provides at low $Z$, and that departure shrinks shell by shell.

**Anion rung:** outside for most bound anions, but inside for fluorine, sulfur, chlorine, selenium, bromine, silver, tellurium, iodine, iridium, platinum, gold and astatine — the strong electron attachers. Across gallium to bromine it runs outside, outside, outside, inside, inside; arsenic stands above germanium because its first removal energy is higher and its affinity lower at the same time. Two elements make the boundaries visible. **Oxygen stands on both sides at once:** its anion rung is outside and its core opening inside (Lean: `oxygen_two_sides`). **Silver and silicon are the closest calls:** silver's anion rung sits just inside ($\Gamma_0 = 0.70622$) and silicon's just outside ($\Gamma_0 = 0.70873$), against the wall at 0.70711, each on its side across its quoted uncertainties (Lean: `rung0_Si_low`, `rung0_Si_high`). Neon's helium-core ratio is strictly greater than five, just above $\Gamma = 2/3$.

**Conduction does not need an outside step.** Magnesium and calcium are metals with every ordinary step inside (Lean: `mg_all_inside`, `ca_all_ordinary_inside`), and so are scandium to zinc, gallium, strontium, yttrium to silver, indium and tin. The wall reads the atom's own ladder. Conduction is a property of the connections between atoms, and I take it up with the junctions. Conductivity or not is still, to me, the key in every element — set by the electron, with light as its twin guiding it — and the record of that is in the junction section, not in the single-atom ladder.

The strongest ordinary step changes rank in the third and fourth periods: from the L opening to the K opening between magnesium and aluminium, and from the argon-core opening to the K opening between potassium and calcium (Lean: `rank_swap_Mg_Al`, `rank_swap_K_Ca`). The filled $3d^{10}$ and $4d^{10}$ openings decline across their rows; palladium's anion rung is its own filled $4d^{10}$ opening, and no filled $4d^{10}$ ordinary opening exists from niobium to rhodium.

### The opening map across the whole table

The same opening can be followed along its whole isoelectronic sequence: every ion with one electron above a given noble core, from the first element that has it to the end of the data. The archive holds 433 such ratios.

| Core | Ratios | First element | Outside the wall |
|---|---|---|---|
| helium core | 101 | lithium 14.029 | lithium, beryllium, boron, carbon |
| neon core | 100 | sodium 9.201 | sodium |
| argon core | 92 | potassium 7.286 | potassium |
| krypton core | 74 | rubidium 6.533 | rubidium |
| xenon core | 49 | caesium 5.947 | caesium |
| radon core | 17 | francium 5.500 | none (francium straddles) |

**DERIVED.** Counted from the first element that has it, each sequence crosses inward after 4, 1, 1, 1 and 1 steps for the helium, neon, argon, krypton and xenon cores. The first ratio falls core by core: 14.03, 9.20, 7.29, 6.53, 5.95. Each sequence crosses inward once and never comes back out: for the neon, argon, krypton and xenon cores right after the first element, and for the helium core after carbon. Francium's radon-core value, 5.50, is centrally inside, but its semiempirical second energy gives a range of 5.03 to 5.97, which straddles the wall (Lean: `francium_straddles`). The neutral nobelium or lawrencium first ionisation energy alone cannot decide an ordinary two-energy wall class. All 433 openings are certified in `OpeningMap.lean`.

![Core openings computed from successive thresholds at fixed electron count. Each core sequence starts outside the wall and crosses inward once and stays inside: carbon to nitrogen, sodium to magnesium, potassium to calcium, rubidium to strontium, caesium to barium.](../figs/fig09_openings.png)

Before the numbers for rubidium and strontium were opened in this element run, the call was written down in the batch record: rubidium outside, strontium inside. Both held, rubidium at 6.533 and strontium at 3.888 (Lean: `frozen_prediction_Rb_Sr`). Rubidium and caesium already appear in my dated November VOTKP paper, whose Figure 35 places the non-helium core-line crossings after their alkali metals, so this frozen call tests the pipeline against concealed rows; it does not date the first statement of the bracket.

**HYPOTHESIS.** Element 119 would start the next core sequence. My written call is that its opening ratio lies inside the wall, $1<IE_2/IE_1<3+2\sqrt2$. A reliable measured ratio above 5.8284 would defeat it.

### The two screening readouts and the 5/8

The last two electrons of every element give two readings of the same pair. In hartrees, with $h$ the hydrogen-like and $b$ the helium-like removal energy,
$$S = \frac{h-b}{Z},\qquad \sigma = Z - \sqrt{2b}.$$
**DERIVED.** An exact identity links them:
$$Z(S-\sigma) = \big(h - Z^2/2\big) - \sigma^2/2 .$$
If the hydrogen-like energy were the bare $Z^2/2$, $S$ could never exceed $\sigma$ for any element (Lean: `readouts_identity`; the false control `bare_S_above_sigma` is rejected). So the two readings can pass each other only through the hydrogen-like ion's binding beyond $Z^2/2$: the Dirac term, less the nuclear-mass and Lamb terms. They do pass, between aluminium and silicon, near 0.617. The full table is in the appendix. The events are distinct, and the round numbers are not where the readings meet:

- $\sigma$ crosses $5/8$ between neon and sodium on measured energies, which include nuclear recoil; without recoil this event moves to between fluorine and neon;
- $S$ crosses $\sigma$ between aluminium and silicon;
- $S$ crosses $5/8$ between argon and potassium;
- $\sigma$ falls through $\tfrac12$ between nickel and copper;
- $\sigma$ turns negative between palladium and silver, where the helium-like energy exceeds $Z^2/2$.

**DERIVED.** Every one of these events needs the electron's spinor (Dirac) structure. With a scalar wave alone and an infinitely heavy nucleus, the $1/Z$ expansion gives $S = 5/8 - 0.157666/Z$ and $\sigma = 5/8 + 0.037646/Z$, so $S$ stays below $5/8$ and $\sigma$ above it for every element. The leading spinor term $\alpha^2Z^4/8$ that the Dirac equation adds to the hydrogen-like energy predicts where $S$ meets $\sigma$:
$$Z^* = \big(4\sigma^2/\alpha^2\big)^{1/4} = 13.0\quad\text{for }\sigma = 0.617,$$
exactly between aluminium and silicon. (This 5/8 is the helium-like screening constant; the 5/8 in the screened core-opening series below has a different origin, and I keep the two apart.)

### The screened core series and the carbon–nitrogen crossing

The helium-like and lithium-like effective series give a sharper local test than the bare-shell floor:
$$z_{\text{core}}(Z)\simeq\frac{Z^2/2-5Z/8+0.157666}{Z^2/8-(290/729)Z+0.250500}.$$
It reaches the wall at $Z^* = 6.538$, between carbon and nitrogen; replacing the helium-like numerator by the bare $Z^2/2$ moves the crossing to about 9.47, between fluorine and neon (removing only the $5Z/8$ term gives 9.55). Screened at $Z = 6$ the series is outside and at $Z = 7$ inside (Lean: `screened_six_outside`, `screened_seven_inside`; the false control `screened_seven_outside` is rejected). The screened ratios match the archive to 0.08–0.26 percent: carbon 6.09547 against 6.07953, nitrogen 5.64841 against 5.63967, oxygen 5.35859 against 5.35283, fluorine 5.15546 against 5.15101, neon 5.00518 against 5.00135. The $5Z/8$ term — the Coulomb repulsion of the two $1s$ electrons — is what places the crossing.

Between carbon and nitrogen nothing about the core changes; the absolute jump even grows. The loop for the helium-core opening goes from open to closed because the relative mismatch between its faces fell below the rim-touching point.

### The jump as a loop: closing and opening

**DERIVED.** The wall can be read without the sinh formula. Put the corner of a ball at the centre of the disc, with one face along each of two perpendicular directions. Each face sits at its half-step distance $h = \tfrac12\ln z$ from the corner. At each face draw the line perpendicular to its direction; in the disc that line is a circle meeting the rim at right angles, with radius $1/\sinh h$. The two circles cross exactly when $\sinh h_a\sinh h_b<1$. When they cross, the loop around the step closes; when they miss, it is open. The border case is the classical quadrilateral with three right angles and its fourth corner on the rim — the Lambert quadrilateral. For equal faces the border is $z = 3+2\sqrt2$, the loop wall. Closed, $\cos\phi = \sinh a\sinh b$; open, $\cosh d = \sinh a\sinh b$. With one face fixed at $a$, the tangent partner is $b^*(a) = \big((\sqrt a+1)/(\sqrt a-1)\big)^2$; $a = 9$, $b = 4$ is an exact tangent pair ($\Gamma = 4/5$ and $3/5$).

| Faces of the loop | Result |
|---|---|
| carbon's helium-core opening ratio (6.0795) on both faces | open |
| nitrogen's helium-core opening ratio (5.6397) on both faces | closes |
| carbon's on one face, nitrogen's on the other | open, barely (margin $\Gamma_a^2+\Gamma_b^2-1 = +0.00309$) |
| carbon's held on one face, the other face swept | opens at $z = 5.591156$ |
| rubidium's krypton-core opening ratio (6.5331) held, the other face swept | opens at $z = 5.222848$ |
| rubidium's on one face, strontium's krypton-core opening ratio (3.8878) on the other | closes |

### Which cutoffs the data allow

**DERIVED.** For a forward rule "outside if $z>c$", each inside datum puts $c$ at or above its value and each outside datum puts $c$ strictly below its value. The eight ordinary positives alone allow any $c$ in $[5.6396654003, 5.9471008342)$, from nitrogen's helium-core opening up to caesium's xenon-core opening (Lean: `ordinary_window_nitrogen_caesium`); caesium is the first ordinary step that a cutoff of 6 gets wrong. Including the anion rungs narrows the window to
$$[5.8079020598,\ 5.8665387761),$$
from silver's anion rung (inside) up to silicon's (outside) (Lean: `window_silver_silicon`). Using complete input rectangles narrows it to $[5.8080102725, 5.8665142305)$; with silicon's 2024 isotope-resolved affinity the upper edge is 5.866513048. The window is 0.059 wide, and the derived $3+2\sqrt2 = 5.8284$ sits inside it. The silver and silicon electron affinities are the two measurements that test the wall hardest.

Across all 5,714 central ratios, no ratio separates the geometric wall from the registered arithmetic-midpoint rival; of the 5,691 pairs with both widths recorded, one interval overlaps the test window (francium), and 23 lack a complete width. The geometry selects an exact number before any fit; the census gives a range with identical classifications. So the data cannot by themselves pick $3+2\sqrt2$ out of the window, and the uniqueness has to come from the geometry — which is exactly what the two-face agreement theorem supplies. A physical test that could tell the wall from its neighbours would need an independently measured observable that changes characteristically across the window, with its threshold and error budget fixed in advance. The carbon and nitrogen K-resonance areas show why such an observable is needed: their reported areas overlap within quoted uncertainties, so they do not separate the two sides.

![The data window and the points inside it. Every cutoff between silver's anion rung and silicon's sorts all 3,637 steps identically; the geometry picks $3+2\sqrt2$, and the oxygen triplet, the scandium–tin pair and the 35/6 bench are the settings that could separate it from the midpoint rivals.](../figs/fig04_window.png)

### The anion rung: the stone and the wanting

**DERIVED.** At the anion rung the reflection is
$$\Gamma_0 = \frac{IE-EA}{IE+EA} = \frac{\eta}{\chi},$$
where $\eta = (IE-EA)/2$ is the absolute hardness — how much an atom resists having its electron count changed, the stone — and $\chi = (IE+EA)/2$ is the Mulliken electronegativity — how strongly it pulls, the wanting. In the half-hardness convention, with electrophilicity $\omega = \chi^2/(2\eta)$,
$$\frac{\omega}{\eta} = \frac{1}{2\Gamma_0^2},$$
so the loop wall $\Gamma_0^2 = \tfrac12$ is exactly **electrophilicity equal to hardness** (Lean: `gam_anion_rung`, `omega_eta_wall`). Inside the wall the wanting wins ($\omega>\eta$); outside, the stone wins. At the wall $\chi/\eta = \sqrt2$. The same identity in my own variables: $(I+A)^2-2(I-A)^2 = -(I^2-6IA+A^2)$, so the wall is the root of $I^2-6IA+A^2 = 0$, that is $I/A = 3+2\sqrt2$, and for a given first ionisation energy the critical affinity is $I(3-2\sqrt2)$. In the gravity ledger the anion rung's metric determinant is $IE\times EA$. Switching to the full-hardness convention $\eta = IE-EA$ changes the numerical comparison and must be declared.

**How much charge an atom takes.** The quadratic that matches both thresholds, $E(x)-E(0) = -\chi x+\eta x^2$, has its minimum at
$$x^* = \frac{\chi}{2\eta} = \frac{1}{2\Gamma_0},$$
which is $1/\sqrt2$ at the wall, with energy drop $\chi^2/(4\eta)$. In the same convention the familiar maximum uptake $\Delta N_{\max} = \chi/\eta = 1/\Gamma_0$ equals $\sqrt2$ at the wall; it is twice the threshold-matched value because it uses the half hardness in a formula built for the full curvature. The two numbers are different quantities and both are stated. Actual charge uptake needs a reservoir and a measured response.

**RECOGNISED.** The inside set is not the metals against the non-metals, not the metalloid line, and not hard against soft. Silver ($\omega/\eta = 1.0025$) and silicon ($0.9954$) bracket the wall. The quantities $\eta$, $\chi$ and $\omega$ are standard (Parr and Pearson 1983; Parr, von Szentpály and Liu 1999), but I found no published use of $\omega = \eta$, $\eta/\chi = 1/\sqrt2$ or $IE/EA = 3+2\sqrt2$ as a boundary. The full 65-row table of $IE/EA$, $\eta/\chi$ and $\omega/\eta$ is in the appendix. Calcium, strontium and barium do bind an extra electron (affinities 0.02455, 0.05206 and 0.14462 eV): their anion rungs are far outside, at 249.0, 109.4 and 36.0. Among the alkaline earths through barium, only beryllium and magnesium have no stable anion.

![The anion rung read as $\omega/\eta = 1/(2\Gamma_0^2)$. Below the line (red) the stone wins and the rung is outside the wall; above it (blue) the wanting wins. Silver sits just above the line and silicon just below.](../figs/fig03_anion.png)

**PREDICTION TESTED.** Written at 09:24 on 21 November 2026, before the adopted values were opened, as informed calls from remembered chemistry (correlated with one another, not independent tests): gold, platinum, iridium and astatine inside, with iridium close to the wall; osmium, bismuth, polonium and lead outside. Result: gold 3.996, platinum 4.216, iridium 5.733 and astatine 3.857 are inside; osmium 7.830, bismuth 7.731 and lead 20.79 are outside. All seven cases with adopted experimental point values agree (Lean: `heavy_anion_prediction`). The eighth call, polonium outside, **failed this way, provisionally**: three preliminary laser photodetachment fits from one campaign put it inside — the JyvIS value $11{,}905.631(9)\ \mathrm{cm^{-1}}$ gives $A = 1.4761101164$ eV and $z = 5.702874$ — and the wall would need $A<1.444312474$ eV for outside. The team explicitly excludes unfinalised systematics from the reported uncertainty, and the fits are not independent experiments. With the same provisional affinity the barium-donor, polonium-acceptor pair gives about $5.2117/1.476110 = 3.531$, also inside. Gold and platinum are known to form monatomic anions in real compounds. These seven heavy calls do not, by themselves, single out $3+2\sqrt2$ among cutoffs between 5.8 and 6. A separate holdout rule that predicted anion side from the ordinary call and the position of the strongest opening, trained on hydrogen to xenon, called every caesium-to-astatine case outside: 20 of 20 outside correct, 0 of 4 inside, balanced accuracy 0.50, missing iridium, platinum, gold and astatine. That rule failed this way. The strongest opening still gives a useful address: it occurs deeper than the first eligible core for 70 of 83 elements, and adding its ordinal to the anion and ordinary address reduces the number of indistinguishable element pairs from 1,304 to 366.

### The element address

Each element's address is where its two strongest boundaries fall: the anion rung (inside, outside or none) and the first opening of its noble-gas core (inside, outside or none). From hydrogen to astatine this gives seven occupied classes:

| Anion rung | First core opening | Elements | Count |
|---|---|---|---|
| outside | outside | lithium, boron, carbon, sodium, potassium, rubidium, caesium | 7 |
| none | outside | beryllium | 1 |
| outside | inside | 45 elements, including oxygen, aluminium, silicon, phosphorus, calcium, strontium, barium and most transition metals | 45 |
| inside | inside | fluorine, sulfur, chlorine, selenium, bromine, silver, tellurium, iodine, iridium, platinum, gold, astatine | 12 |
| none | inside | 18 elements, including the noble gases from neon on, magnesium, nitrogen, zinc, mercury | 18 |
| outside | none | hydrogen | 1 |
| none | none | helium | 1 |

**DERIVED** from measured inputs. The out-and-out class — lithium, boron, carbon, sodium, potassium, rubidium and caesium — is the set of atoms where both the extra electron and the first core electron are held past the wall. This address is the backbone of my *Periodic Table of Elemental Peels*.

### Francium: a registered prediction

**OPEN, registered.** Francium's radon-core opening is inside the wall if and only if $IE_2(\mathrm{Fr})<23.738$ eV, at the adopted $IE_1 = 4.0727411$ eV. Only a measured $IE_2$ in $[23.654, 23.893)$ eV — the image of the silver–silicon window — would bear on where inside the window the true cutoff lies, separating the wall from the cutoffs on the far side of the measured value; to separate it from the raw-ratio midpoint alone, a new uncertainty interval would have to lie wholly inside $(23.73768111, 23.77348109)$ eV at the reported $IE_1$ width. The NIST semiempirical value is $[22.4]\pm1.9$ eV; $IE_2$ is unmeasured. A separate frozen extrapolation down the alkali column, $z_{\text{next}} = 2z_{\text{last}}-z_{\text{previous}}$, gives $z = 5.361114977$ and $IE_2 = 21.834433307$ eV for francium; applied to the earlier alkalis it predicted potassium, rubidium and caesium inside, and all three are outside. That extrapolation failed this way, 0 of 3, and it stays on record. A verified ground-channel threshold would score both statements wherever it falls; an excited Fr²⁺ residual channel has a different threshold.

### The gold–mercury bracket

**DERIVED / HOLDOUT.** The one-electron shell ratio 4 plays two roles. In the unscreened Schrödinger (scalar-wave) $2s\to1s$ comparison it gives $\Gamma = 3/5$. The actual lithium-like to helium-like pair includes state-dependent electronic binding and follows a different sequence. All 82 consecutive uncertainty-box comparisons from lithium to astatine descend strictly. The ratio first falls below four between gold, 4.00189784, and mercury, 3.99780412; both heavy inputs in each pair are theory-grade. A straight secant based on terbium and ytterbium, and a point-Coulomb Dirac ratio with a fitted $1/Z$ correction, both predicted this bracket from truncated inputs (intervals $[4.001832223, 4.001963460]$ and $[3.997740439, 3.997867804]$). Only two of 15 held-out point predictions for the secant enter the tabulated intervals, and zero of 15 for the corrected spinor formula. The comparison grades the specified many-electron extrapolation; no one-electron spinor equation was falsified. A preregistered successful bracket can coexist with a poor pointwise error model, and gold–mercury shows both.

### A transfer that failed this way

**DERIVED / FAILED TRANSFER.** For four log-steps $r_i$ spanning a core, divide each by $\sum_ir_i$. The resulting shape says where an endpoint-fixed ratio accumulates. The frozen first-two contrast gave 72 of 72 positions in the lighter neon-, argon- and krypton-count families. On the 24 xenon-count positions it gave 14 of 24; the ordered four-component classifier gave 15 of 24. Eleven primary responses remain correct and three remain wrong across complete input boxes; ten are ambiguous within those boxes. In Ce²⁺ the primary contrast is positive, about 0.018854, while the required class lies below $-0.163945$. A ratio can be reliably measured and still be a poor predictor of a transferred label. The subshell bookkeeping supplies an independent control: across the 605 removals from barium to terbium it counts 595 with zero required reassignment, nine with one, and one gadolinium step with two, under the ASD leading configurations; an alternative sequence of configurations removes the apparent gadolinium 1, 2, 1 episode. Writing occupations $a_\ell$ before a peel and $b_\ell$ after it, $K = \sum\min(a_\ell,b_\ell)$ counts slots matchable within each subshell and $R = \sum(b_\ell-a_\ell)_+$ counts the remaining target slots; $N_{\text{after}} = K+R$ and $\|a-b\|_1 = 2R+1$ for a one-particle loss. None identifies an individual electron.

### Three physical checks on what an elemental ladder keeps

**DERIVED / MEASURED INPUTS.** Electron removal leaves the proton and neutron counts of a chosen isotope unchanged; nuclear transmutation is a second process. For two isobars at equal ionic charge the missing-electron rest energies cancel. Defining $Q(q) = [M_{\mathrm{Ho}}(q)-M_{\mathrm{Dy}}(q)]c^2$ gives $\Delta Q = I_{\mathrm{Ho},q+1}-I_{\mathrm{Dy},q+1}$, which is $(I_{\mathrm{Ho}}+I_{\mathrm{Dy}})\,\Gamma_{\mathrm{Ho,Dy}}$ with the signed interspecies reflection taken at equal charge. Observed neutral holmium-163 decays toward dysprosium; bare dysprosium-163 was observed to decay the other way, to hydrogen-like holmium. The independent neutral mass anchor and the archive predict only one ground-mass-ordering reversal, from $Q(56) = +1.9514$ keV to $Q(57) = -4.5186$ keV. Separate restarts from the published 38+, 39+ and 40+ trap frequency ratios keep the bracket. At 56+ the two species have eleven and ten electrons, so the next removal opens dysprosium's neon-like core while holmium still loses its last $3s$ electron, which drives a $-6.470$ keV increment. No intermediate-charge decay rate was measured. Multiplying both energy ladders by 0.01 while holding neutral $Q(0)$ fixed erases the ordering change and keeps every adjacent and interspecies reflection — an explicit identifiability control on a dimensionless-only model. The full calculation is in *Where the vector reaches nuclear decay*.

**DERIVED / CONTROL.** In the lead-205 and thallium-205 system the signed mass gap crosses between 79+ and 80+. Subtracting the 2.329 keV daughter nuclear excitation from the bare-endpoint calculation gives 31.0715 keV for the dominant bound-electron channel; the published 31.1(5) keV shares the neutral mass baseline, and the directly observed stored-ion decay is independent evidence that the channel opens. Rhenium gives a different control: the same elemental electronic ladder applied to rhenium-185 and rhenium-187 gives opposite outcomes because of their different nuclear mass anchors. For rhenium-187 a directly measured rhenium–osmium 29+ mass difference removes the need to accumulate both sets of outer-shell uncertainties; the bare parent then has about 63.005 keV available to the osmium-187 excited state at 9.756 keV via the daughter K shell, while the neutral endpoint falls short by about 7.285 keV. The proposed $2s$ channel to that excited state straddles zero within the stated interval, so its status stays open.

**MEASURED INPUT / RECOGNISED.** Structure and photons can change independently of any free-atom peel ratio. The two crystallographic sites of double-hcp neodymium agree in their first twelve distances and second moments yet differ in their angular environment. In coexisting ytterbium refinements some shortest contacts lengthen as the molar volume falls. For elemental polonium the alpha-to-beta refinements give six closest neighbours in both cases, with the shortest distance increasing while the volume per atom declines. Osmium gives direction-resolved optics in one crystal: at 650 nm the two principal-polarisation reflectances from the measured complex indices are 0.4846 and 0.5285. Both belong to the same isotope-averaged electronic ladder. For astatine-197 one nuclear-state change at fixed $Z$, $N$ shifts the 216 nm line up by 4,215 MHz and the 795 nm line down by 1,868 MHz. These examples ask the theory to say which distance, state, direction and optical transition it aims to predict. Neither a signed crystal path nor a nuclear-state label supplies an atomic HOMFLY or Jones invariant without a chosen embedding and closure.

### Reproducibility and retained discrepancies

All 3,655 positive-index energy cells in the corrected historical tables match the pinned archive exactly. I rebuilt 3,740 indexed rows (3,655 removal energies plus 85 anion slots). The early magnesium $k = 4$ table displays 0.12800 for $\Gamma$, which recomputes as 0.127953665550. The scandium affinity display 0.179380 eV differs from the adopted 0.179378 eV, so the zero-rung ratio is 36.579123. Selenium has a conversion-rounding discrepancy below $10^{-27}$ eV. Every typed energy in the seventeen batch tables was compared with the archive; the corrections — vanadium $k = 11$, chromium $k = 9$ and $k = 20$, nickel $k = 21$, copper $k = 5$ and the magnesium $k = 4$ display — change no wall classification. In the independent 21 November ASD snapshot for barium to astatine, 2,114 of 2,115 records agree in value, uncertainty, grade and references with the older pin; neutral neodymium changed from 5.5250(6) to 5.52475(5) eV. The repository folder carries the full threshold table, a one-row-per-element index, the field-level discrepancy file and a standalone reconstruction script.
