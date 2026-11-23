# Finite-profile minimax certificate

For any **nonempty finite set** of indices and any two real profiles `x` and `y` strictly positive on that set, `PeelProfile.finite_profile_minimax` proves that the least possible maximum residual over a common positive multiplier is

```math
\min_{a>0}\max_{i\in s}\left|\ln\frac{x_i}{a y_i}\right|
=\tfrac12\Big(\max_{i\in s}u_i-\min_{i\in s}u_i\Big),
\qquad u_i=\ln(x_i/y_i).
```

Lean expresses the minimum as `IsLeast` of the set of achieved errors and forms each finite maximum with `Finset.sup'`. The minimizing multiplier is unique and equals the exponential of the midpoint of the two extreme log ratios. A singleton gives zero optimal residual. For multiple indices, the optimal residual is zero exactly when the coordinatewise ratios xᵢ/yᵢ are constant. In the element application, `x_i` and `y_i` are the positive **logs of successive energy ratios**. The multipliers act on those logs.

The exact feasibility statement at shift `t` and error bound `r` is `max u − r ≤ t ≤ min u + r`. It follows by inspecting maximum and minimum coordinates. For an arbitrary shift, the larger endpoint error is at least half the range. The two endpoint errors coincide at the midpoint. The proofs infer attainment of each extreme from finite nonemptiness.

| Theorem in namespace `PeelProfile` | Certified statement |
|---|---|
| `worst_le_iff` | Characterizes a feasible shift by the two endpoint inequalities. |
| `radius_le_worst` | Half the range bounds every shift's maximum error from below. |
| `midpoint_attains` | The midpoint has exactly this error. |
| `only_midpoint_attains` | Every optimizing shift equals the midpoint. |
| `worst_eq_radius_add_offset` | At every shift, maximum error equals the half-range plus the absolute displacement from the midpoint. |
| `scaledError_eq_worst` | The positive-scale objective equals the translated log-coordinate objective. |
| `optimal_positive_scale` | Gives a positive multiplier attaining the stated error. |
| `finite_profile_minimax` | The half-range is an attained minimum over all positive real scales. |
| `unique_positive_scale` | Any optimal positive multiplier equals the stated exponential. |
| `positive_scale_tolerance_iff` | Every positive multiplier with at most ε excess error lies in the exact multiplicative tolerance interval, and conversely. |
| `squared_ratios_zero` | Squaring all forward ratios gives exactly zero mismatch against the original when their doubled logs are scaled by one half. |
| `squared_ladder_wall_control` | The exact rational wall statistic is below one half at ratios 2, 3 and 4, and above one half at ratio 9. |

**Reading the tolerance band.** Put `m = (min u + max u)/2`, `R = (max u − min u)/2`, and `a★ = exp(m)`. At scale `a` the worst log error is exactly `R + |log a − m|`. For allowance ε, the feasible scales are precisely `a★ exp(−ε) ≤ a ≤ a★ exp(ε)`. At ε = 0 only the optimizer survives. At positive ε both boundary scales attain the allowed error. A negative allowance makes the interval empty. When the second input is multiplied by a common constant `c > 0`, its log ratios subtract `log c` throughout. The half-range stays the same while the optimal multiplier and both limits divide by `c`. This last observation is a direct algebraic consequence of the displayed formulas. The tolerance here controls approximation error and has no statistical coverage interpretation.

These certificates concern exact mathematics. The numerical nearest-neighbour score, archive provenance, and physical interpretation are independent checks. [Manuscript passage](../profile.md) · [Lean source](ProfileMinimax.lean)

## Reproduction

The executed environment used Lean **4.37.0-rc1**, Linux x86-64, compiler commit `0b77e12952ad39077d80d8bd6b66d601f225c321`, and mathlib commit `31ce06eaadf4a200c0e1407c5f10953cf606b8f8`. In a Lake workspace with that mathlib revision and compiled imports, run:

```sh
lake env lean /absolute/path/to/ProfileMinimax.lean
```

Exit code **0**, with no warnings. For each of the twelve declarations, its embedded `#print axioms` returned precisely `[propext, Classical.choice, Quot.sound]`. The source contained no `sorry`, `admit`, added `axiom` or `native_decide`. Source SHA-256: `8626a09c2b2f251df5b5e4e52b78affd8d4b2b2064f98c6ba0e8fdc4f26a0461`. The parent repository pins Lean 4.34.1. Compatibility with that toolchain remains untested in this pass.
