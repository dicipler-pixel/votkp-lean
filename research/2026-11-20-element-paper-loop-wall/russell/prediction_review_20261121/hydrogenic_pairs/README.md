# Two real one-electron ground thresholds between the registered cutoffs

Jeromie Beasley's element table uses adjacent thresholds of a fixed atom. This extension compares the ground binding energies of the last electron in **two different hydrogenlike ions**. The family, orientation, two cutoffs, treatment of missing inputs and error boxes were recorded before the scan in PROTOCOL.md (SHA-256 3e0c3c84eefca371e0136507cb6a11d3cfc561bcb16c53ab34b64af78148084b). The prior scans of adjacent peels and excited-state channels had already been seen. No number of hits or winning ion was forecast.

## Archive result

Of 118 elements, 110 have a last 1s removal with both energy and width. All 110 carry archive grade T. Rg, Cn, Nh, Fl, Mc, Lv, Ts and Og lack a last removal. This gives 5,995 oriented comparisons with both endpoints and 908 unavailable comparisons from the full set of 6,903. The lower cutoff is w=3+2√2=5.8284271247. The fixed competing cutoff is the arithmetic Ag–Si midpoint c=5.8372204180.

**One pair out of 5,995** has its entire source rectangle in the open interval (w,c). It is also the only central hit and the only rectangle intersecting the interval. The numerator is the ground removal of H-like tin, Sn L (Sn⁴⁹⁺ → bare Sn⁵⁰⁺), B=35,192.501(11) eV. The denominator is the ground removal of H-like scandium, Sc XXI (Sc²⁰⁺ → bare Sc²¹⁺), B=6,033.75643(9) eV. B(Sn)/B(Sc)=5.832602195379, with rectangle [5.832600285303,5.832604105455]. Parentheses in these quoted precision values give the estimated final-digit widths. Both are theoretical inputs from NIST ASD reference L19200. A rectangle is an endpoint arithmetic envelope, independent of an assumed covariance. Treating those source uncertainties as rigorous physical bounds would exceed the tabulation.

For the same 5,995 candidate pairs, infinite-mass Schrödinger scaling yields one different hit, niobium/einsteinium. Infinite-mass, point-nucleus Dirac 1s binding B=mc²[1−sqrt(1−(Zα)²)] gives argon/technetium, scandium/tin, and bromine/thallium. For stability the script uses the rationalized positive form mc²(Zα)²/[1+sqrt(1−(Zα)²)]. Only scandium/tin remains in the full compilation. The script compares the unrounded numbers, retaining exact rational arithmetic for the archive and nonrelativistic cases.

## Published nuclear-size and mass controls

The original theoretical component table uses ⁴⁵Sc (R=3.5459(25) fm, nuclear mass 81928.648 electron masses) and ¹²⁰Sn (R=4.6519(21) fm, mass 218518.671 electron masses). In Table III, MASS is the authors' principal relativistic finite-mass correction. Smaller recoil and recoil-QED terms reside in LAMB. In Table II, FNS is the leading finite nuclear charge distribution shift, separate from radiative finite-size terms and nuclear polarization. The following ground-level corrections raise the signed levels (therefore reduce the binding magnitudes).

| Theory component | ⁴⁵Sc²⁰⁺ (eV) | ¹²⁰Sn⁴⁹⁺ (eV) |
|---|---:|---:|
| Infinite-mass point Dirac binding magnitude | 6035.756887 | 35228.572212 |
| MASS shift | +0.073235 | +0.155649 |
| FNS shift, included in total LAMB | +0.018664 | +1.955568 |
| Total LAMB | +1.927215 | +35.915764 |

Ratio at successive choices: nonrelativistic 5.668934240, point Dirac 5.836645324, adding MASS 5.836690357, adding FNS to MASS 5.836384403, adding the entire LAMB to MASS 5.832602156. Reconstructing from the publication's rounded component table differs by 0.000000039 from the archived central ratio. It is the same theoretical source. The printed component ratios use Table III Dirac rows; the all-pair screen uses the explicit Dirac expression and modern α. The resulting 4×10⁻⁹ difference in the point ratio is below the displayed physical input budget. [Yerokhin and Shabaev (2015), Tables II–III](https://arxiv.org/pdf/1506.01885) · [NIST Sn table](https://physics.nist.gov/cgi-bin/ASD/ie.pl?at_num_out=on&biblio=on&e_out=0&el_name_out=on&format=1&level_out=on&seq_out=on&shells_out=on&spectra=Sn&unc_out=on&units=1)

## Test an independent energy determination

At the archived Sc central value, the allowable tin threshold is (35167.30964, 35220.36623) eV, leaving 25.19136 eV to the lower edge and 27.86523 eV to the upper edge. With tin held fixed, scandium must lie in (6028.98271,6038.07858) eV. For new symmetric widths ΔSn and ΔSc centred at the current predictions, sufficient and necessary rectangle conditions are

    ΔSn + w ΔSc < 25.19136 eV,     ΔSn + c ΔSc < 27.86523 eV.

For new measured means recompute both margins from those means. Isotopes and transition endpoints have to match. An independently measured total ratio strictly below w or above c would refute this particular forecast of disagreement. A measurement wholly inside confirms where two classified inputs lie. Selecting a *physical* wall still needs an additional independently observable effect that the rival laws predict differently.

The 1989 PLT measurements by Beiersdorfer et al. actually observed hydrogenic Sc Ly-α₁, Ly-α₂ and Ly-β₁ while calibrating heliumlike transitions. They used theoretically known hydrogenic wavelengths as standards. The report therefore supplies spectral identification, rather than an absolute Sc XXI ground threshold. This is an important qualification to the A&A 2012 review's statement that Sc XXI had not been observed. Even an independently calibrated Lyman-α photon measures the 1s–2p gap. Adding an upper-state theoretical binding produces a hybrid limit; in Sc the 2p correction alone is about 1.50 keV. [Beiersdorfer et al. (1989), pp. 4–6](https://www.osti.gov/servlets/purl/6321058) · [A&A scandium review (2012)](https://doi.org/10.1051/0004-6361/201117758)

In hydrogenlike ¹¹⁸Sn⁴⁹⁺, the 2023 ALPHATRAP study measured a bound-electron g factor and ionic mass. In its methods the authors actually use 35192.501(11) eV as an input. That precision therefore cannot be cited as a new measurement of the last binding energy. Their measured ionic mass is for ¹¹⁸Sn, whereas the 2015 component row above uses ¹²⁰Sn. Morgner's 2024 Heidelberg dissertation, Fig. 6.1, displays an observed ≈92-keV radiative-recombination X-ray peak group during hydrogenlike and bare tin production. The photon energy is the beam electron kinetic energy plus binding. The figure supports charge assignment and gives no separate ground-threshold interval of the requisite width. These primary sources did not yield an independent two-threshold ratio. [Tin study (2023)](https://doi.org/10.1038/s41586-023-06453-2) · [Heidelberg dissertation, Fig. 6.1](https://archiv.ub.uni-heidelberg.de/volltextserver/35537/1/JMThesisHeiDoc.pdf)

## A separate mathematical spinor overlap

An ion pair in the archive is not a single physical quench between nuclear charges 21 and 50. For comparison define an ideal central-field sudden map between point-Coulomb Hamiltonians of two prescribed charges, at the same centre with common mass, spin projection and origin. For each 1s Dirac spinor let γᵢ=sqrt(1−(Zᵢα_fs)²), λᵢ=Zᵢ/a₀, bᵢ=Zᵢα_fs/(1+γᵢ). In a consistent angular phase convention the usual reduced large radial component is Gᵢ=Nᵢ R^γᵢ exp(−λᵢR), the small component Fᵢ=−bᵢGᵢ. Normalization ∫(Gᵢ²+Fᵢ²)dR=1 gives

    Nᵢ=(2λᵢ)^(γᵢ+1/2) / sqrt[(1+bᵢ²) Γ(2γᵢ+1)].

The angular spinors are orthonormal for identical κ and m; their radial integrals sum. Here Γ in the following expression is Euler's gamma function.

    <a|b> = NₐNᵦ (1+bₐbᵦ) Γ(γₐ+γᵦ+1) / (λₐ+λᵦ)^(γₐ+γᵦ+1).

For scandium/tin the integrated large-component overlap is 0.731720599 and the small-component overlap is +0.010656439, yielding fidelity 0.551123666. Direct quadrature agrees on 24 tests including identical states, reordered charges and the exact α→0 limit. In that limit F=[4ZₐZᵦ/(Zₐ+Zᵦ)²]³, giving 0.578359374 here. Merely substituting the archived energy ratio into the nonrelativistic face formula produces 0.568289555, a different conditional model. Finite mass, extended nuclei and radiative corrections can affect spinors; a list of corrected energies is insufficient to infer their exact overlaps. No joint atomic transition, scattering probability, or measurement of these overlaps is asserted.

## Reproduction

Supply the pinned archive to pair_scan.py. The script verifies its SHA-256 before parsing its declared decimals, writes both candidate tables and prints coverage. The Dirac program uses SciPy quadrature; the pair scan uses Python's standard library. The spectral tables and flags are from the calculations, without retyping energy inputs into the scan.

    python pair_scan.py /path/to/element_thresholds_20261011.json.gz
    python dirac_check.py
