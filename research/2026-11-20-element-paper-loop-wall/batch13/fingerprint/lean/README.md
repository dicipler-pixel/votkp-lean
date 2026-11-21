# Three held-out misses survive exact threshold arithmetic

The earlier scalar fingerprint classified 72/72 windows from the neon, argon and krypton families. Its frozen xenon-family test found three doubly-above-core starts that it misses throughout their quoted input boxes. The test below asks whether the exact arithmetic behind these three misses could be an artifact of numerical logarithms. A permitted class-2 contrast in any of these three boxes would falsify that conclusion.

Write the five ordered positive energies as $a,b,c,d,e$. The contrast is

$$D=\frac{\ln(b^2/(ac))}{V},\qquad V=|\ln(b/a)|+|\ln(c/b)|+|\ln(d/c)|+|\ln(e/d)|.$$

The input boxes place $e>a>0$. The triangle inequality and telescoping give $V\geq \ln(e/a)>0$. Thus the fourth energy can be arbitrary positive in the following lower-bound calculation.

For cerium²⁺ the smallest possible $b^2-ac$ equals

$$(36.906-0.009)^2-(20.1974+0.0025)(65.55+0.25)=32.235189\;\mathrm{eV}^2>0.$$

Consequently every admitted cerium²⁺ contrast is **positive**, whereas class 2 requires a negative contrast. Neodymium⁴⁺ gives the same conclusion with a lower bound of 128.8 eV². Praseodymium³⁺ permits either numerator sign; its lower bound is −50.5656 eV². A positive-numerator claim for all three would fail.

There is a common exact test with more margin than needed. Lean proves for all three input rectangles, at every rational realization,

$$(ac)^8 a < (b^2)^8 e.$$

Over positive real inputs the same corner inequality follows by monotonicity of multiplication and of the eighth power. Taking real logarithms gives $8\ln(b^2/(ac))+\ln(e/a)>0$. Replacing $\ln(e/a)$ by its upper bound $V$ preserves positivity. Dividing by $8V$ yields **$D>-1/8$**. This derivation does not assume that the intermediate steps are monotone.

The checker reruns the frozen training feature on the same 72 original windows. It checks the exact binary64 representations of the class-zero and class-two centres used by the scorer. Their midpoint is exactly $-2953376414123437/18014398509481984$, below $-1/8$. Strictly above that midpoint the class-zero centre is closer than class two, regardless of where class one sits. This rules out class two at every admissible input for all three cases; the finite test still scores 14/24 on the central xenon-family values.

The kernel checks rational inequalities, the two stored trained centres and distance comparison. The real logarithm and total-variation argument above is an analytic implication in prose. The source uses exact rational endpoints from the pinned spectroscopy archive, including its theoretical estimates and quoted widths. It leaves the original predictor and its training set unchanged.

```sh
python3 check.py --lean /path/to/lean
```

[Original 72-window test](../../../batch9/fingerprint/FINGERPRINT.md) · [Frozen transfer test and full scores](../README.md)
