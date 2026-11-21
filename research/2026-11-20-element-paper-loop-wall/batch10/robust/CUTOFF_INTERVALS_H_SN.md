# Which forward cutoffs reproduce hydrogen through tin?

**DERIVED.** The forward decision is “outside if z>c.” Across 1,225 ordinary steps and 40 anion inputs (one, technetium, estimated), the central labels at c=3+2√2 are also obtained at every c in **[5.807902059840…, 5.866538776091…)**. Silver’s anion supplies the lower endpoint and silicon’s anion the upper. Including reported input uncertainties narrows the interval to **[5.808010272529…, 5.866514230542…)** on the 1,247 steps having complete boxes, using the element-paper silicon affinity 1.3895212(7) eV. There are 18 other steps. Their central labels agree throughout that interval, and the archive supplies insufficient uncertainty information for an unconditional box calculation for them.

| Inputs | Highest value that must be inside | Least value that must be outside |
|---|---|---|
| Ordinary, central | Nitrogen k=5, 5.639665400281… | Carbon k=4, 6.079534191962… |
| Ordinary, complete boxes | Nitrogen k=5 upper bound, 5.639689262507… | Carbon k=4 lower bound, 6.079515661295… |
| Ordinary + anion, central | Silver k=0, 5.807902059840… | Silicon k=0, 5.866538776091… |
| Ordinary + anion, complete boxes | Silver k=0 upper bound, **7576259/1304450** | Silicon k=0 lower bound, **6270500/1068863** |

**DERIVED.** Given A±u and B±v, independent positive input boxes bound z=B/A between (B−v)/(A+u) and (B+v)/(A−u). For every inside row the new cutoff must be at least its upper bound. For every outside row the cutoff must be lower than its lower bound. Taking the two extrema gives the necessary and sufficient interval [L,U). The exact wall decision was evaluated using 2(B−A)²>(B+A)². A second rational check recomputed every central decision in Γ coordinates and the reference wall on both endpoints of every complete box. Even where a ratio's low endpoint departs from the central value, every checked low endpoint exceeds 1/2, well above the reverse wall.

For silver, L=(7.576234+0.000025)/(1.30447−0.00002). For the encoded silicon threshold, U=(8.15168−0.00003)/(1.3895212+0.0000007). Accepting a cutoff at L preserves the foremost inside row under strict >. At U an outside row can fall exactly on the cutoff. The stated boxes propagate the published error extents. They specify neither a joint uncertainty probability nor guaranteed physical truth.

## Silicon isotope sensitivity

**MEASURED.** The 2024 DESIREE study measured three stable silicon isotopes separately. Table 1 assigns 1.38952201(17) eV to silicon-28, 1.38952172(12) eV to silicon-29, and 1.38952078(12) eV to silicon-30. The table resolves a repeated isotope label in the preprint abstract. [DESIREE Table 1](https://arxiv.org/abs/2404.06226)

**DERIVED.** Replacing only the affinity input and retaining the archive’s elemental IE₁±0.00003 eV gives exclusive upper cutoffs 5.866513048392…, 5.866514483860… and 5.866518452511…, respectively. The lower silver cutoff is unchanged. The intersection under all three substitutions uses **5.866513048392…** as the upper endpoint. These substitutions do not establish isotope-matched IE₁ values. The original central/bracket results remain reproducible from the original silicon input, with a separate newer-isotope sensitivity calculation.

## Negative controls and the earlier fixed point

**DERIVED.** Cutoffs 5.82, 5.83 and 5.85 all reproduce the 1,265 central labels. Cutoff 5.8 disagrees only at the silver anion. Cutoffs 5.9 and 6 disagree only at the silicon anion. Thus silver and silicon tighten identifiability markedly compared with comparing noble-core openings alone. They still admit a continuum of cutoffs. A binary label here is generated from a ratio; an independent physical observable would be needed to give special empirical status to one cutoff within that interval.

**DERIVED.** At c=5, equivalent to Γ=2/3, seven central rows move outside relative to c=3+2√2. The five ordinary rows are the helium-core openings in nitrogen, oxygen, fluorine and neon, and the neon-core opening in magnesium. The other two are the fluorine and silver anions. The nearest central ratios on opposing sides of 5 are the sulfur anion at 4.987717997… and the neon helium-core opening at 5.001351753…. The latter has a complete box [5.001310336…, 5.001393169…], so its small nonzero offset from five exceeds the propagated input uncertainties. Its central Γ is 0.666741747….

## What is unknown

The accompanying small CSV lists every row lacking one or more quoted input uncertainties. Seventeen ordinary rows depend on missing archive uncertainties. The eighteenth is the technetium anion, whose EA is a calculated estimate without a measured uncertainty. Ten elements lack a bound atomic ground-state anion in the adopted reference and have no k=0 ratio.

**HYPOTHESIS / DERIVED conditional bound.** Suppose the unknown true consecutive energies in each affected ordinary block increase, and the block's immediate measured ends lie within their listed boxes. Every ratio within the block is then at most (upper energy at the right end)/(lower energy at the left end). This extra premise bounds 11 of the 17 ordinary rungs below even the silver limiting ratio: bromine (2), zirconium (2), niobium (3), ruthenium (2), palladium (2). It cannot bound the three technetium steps or the three rhodium steps below the loop wall, since their outer ratios can reach 5.99774 and 5.85881, respectively. No missing error bars have been filled in by this conditional argument.

## Sources and reproduction

The standard-library script checks the archived SHA-256 before reading energies. Meaning of the accompanying affinity source codes: EA22 is Ning and Lu Table 3, H91 is the historical measured hydrogen value, ScY23 the scandium/yttrium measurement, As25 the arsenic measurement, Se26 the selenium revision in cm⁻¹ (converted using exact defining SI constants), Zr17 the zirconium measurement, Tc02 the technetium estimate, and Rh26 the revised rhodium measurement. The frozen affinity inputs allow repetition of the cutoff test; the silicon isotope rows are explicit alternate inputs. [Archive](https://github.com/dicipler-pixel/votkp-lean/blob/bcedbd9bba0de5a75fd2a860a912ebc4882f4e8a/data/element_thresholds_20261011.json.gz) · [EA22](https://doi.org/10.1063/5.0080243) · [H91](https://doi.org/10.1103/PhysRevA.43.6104) · [ScY23](https://doi.org/10.1063/5.0124882) · [As25](https://doi.org/10.1103/PhysRevLett.134.043001) · [Se26](https://pubmed.ncbi.nlm.nih.gov/41626821/) · [Zr17](https://doi.org/10.1063/1.4986547) · [Tc02](https://doi.org/10.1103/PhysRevA.65.064502) · [Rh26](https://doi.org/10.1088/1674-1056/ae5173)

```sh
python3 cutoff_intervals.py /path/to/element_thresholds_20261011.json.gz
```
