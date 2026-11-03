# Gas and response formal extension — final result record

3 November 2026. Run `python gas/verify_formal_gas.py` from the package root, or run that file by absolute path. It requires Python 3, NumPy and SciPy. The script has no network operations and accepts no runtime arguments. It regenerates `gas/formal_gas_results.json`; stdout may be captured separately.

## Proof documents

- `formal_gas_response.md`: G1–G7 cover anchored threshold coordinates, finite Saha neutrality, uniqueness, density and parameter response, temperature response and complete scaling covariance. R1–R4 cover retained/hidden dynamics, positive channel measures, an equal-spectrum counterexample and the independent hidden-source omission.
- `gas_peel_inverse.md`: G8–G9 retain and extend incoming matter-disk §8, proving full-ladder reconstruction, partition corrections, excited-state slope biases and deterministic error bounds.
- The labels M1–M4 in the original prospective protocol were changed administratively to R1–R4 to avoid a manuscript numbering collision. The predictions, controls and tolerances were not changed.

These are analytic proofs. Machine-checked coverage is only what the final Lean manifest says; neither an exact-arithmetic assertion nor a floating-point check is represented as a Lean proof.

## Execution result

All **18 check flags passed**. They include implementation checks, algebraic identities and false-control demonstrations; they are not 18 independent empirical findings.

| Check | Maximum recorded error or outcome |
|---|---:|
| 100 rational positive-ladder reconstructions/scalings | Exact equality |
| 8 rational manufactured neutrality polynomials | Exact zero |
| Numerical manufactured roots | 1.066e-14 |
| Charge neutrality, 64 systems | 4.397e-14 |
| Density-response finite differences | 1.439e-11 |
| Single-coefficient-response finite differences | 1.824e-11 |
| Fixed-partition temperature-response differences | 2.014e-10 |
| Coefficient/density scaling populations | 3.886e-16 |
| Physical scaling dictionaries | 1.666e-15 |
| General 2–8 stage inverse ladder, 16 cases | 6.662e-15 |
| Equal-spectrum witness survival at pi/4 | 0 versus 1/32 (within 2.1e-17) |
| Same-kernel, different hidden-source witness | 1 versus 0 (within 4.5e-16) |

## The incoming gas-peel construction and its opposite

The actual threshold inputs remain 24.587389011 eV (E) and 54.4177655282 eV (T), with Gamma = 0.37757506698375054. The original matter-disk §8 fixed-partition identity was already supplied; its rerun is retrospective. The separately declared excited-partition control was specified before this implementation ran.

At temperatures 30,000 K and 32,000 K and each nucleus density 1e18, 1e20, 1e22, 1e24 and 1e26 per cubic metre:

| Inverse model | Recovered Gamma |
|---|---:|
| Fixed U=(1,2,1), uncorrected slopes | 0.37757506698375 |
| Synthetic U1(T)=2+4 exp(-10 eV/kT), ignoring its variation | 0.36614943350748 |
| Same synthetic partition, correcting its known variation | 0.37757506698375 |

Ignoring the synthetic excitation partition biases Gamma by -0.0114256334763. Correcting the known partition terms restores it within 1.433e-14; the original fixed-partition recovery is within 4.108e-15. This closes the mathematical partition-dependence question inside the declared model. It does not validate a real helium excitation spectrum, non-LTE closure, or laboratory inversion.

The population triple ratio cancels density without further state measurements. The full-ladder sum combination requires the pointwise electron-density/thermal-wavelength correction. Those two observables should not both be described as population-only or experimentally density-free.

`formal_gas_results.json` preserves every Boolean outcome, protocol hashes, exact rational coefficients, numerical Hamiltonian evaluations, each density's inverse results and all maximum errors. `gas_peel_inverse_results.csv` is a readable subset of its inverse results. The CSV is a convenience export; the JSON and executable are authoritative.
