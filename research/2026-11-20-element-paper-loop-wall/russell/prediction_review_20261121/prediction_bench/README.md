# Prediction Bench v1

Jeromie Beasley’s element-paper loop-wall geometry, compared with three fitted alternatives. Open [Prediction_Bench_v1.html](Prediction_Bench_v1.html) in a browser. Download the HTML from GitHub to run it locally. It contains both plots, data and controls and works offline.

The central forward-rung archive through astatine leaves the raw-ratio calibration gap from the Ag anion at 5.80790206 to the Si anion at 5.86653878. Every rule displayed here matches all 3,637 historical single-face binary calls. Each rival uses the raw-ratio midpoint 5.83722042 for its equal-face cutoff. The geometric cutoff is 5.82842712. Use the equal-face slice to inspect the narrow interval of disagreement. The two-face plot shows how choosing a different rule away from the diagonal changes the critical partner at each face setting. Hover or use arrow keys to inspect a setting, then click, tap or press Enter to apply it. Both plots have selectable zoom.

| Setting | Geometry | Shifted sum | Shifted product | Piecewise warp | Geometric return trace |
| --- | --- | --- | --- | --- | ---: |
| Equal faces 35/6 | Open | Closed | Closed | Closed | −2.009529 |
| 3 and 13.99 | Open | Closed | Open | Open | −2.020493 |
| Be and Rb helium-core openings | Open | Closed | Closed | Open | −2.006465 |
| Si and Ag anion rungs | Open | Closed | Closed | Open | −2.016894 |
| 9 and 4 | Ideal | Closed | Closed | Ideal | −2.000000 |

“Ideal” marks the exact boundary. Experimentally resolving a return requires an independently calibrated observable and uncertainty budget. The return trace shown here is calculated from the ideal four-stage transfer matrix. The competing rules specify boundary calls only. The highly charged Rb thresholds are theoretical reference values. This bench supplies dimensionless settings for testing, with no claim of an observed joint atomic response.

## Model definitions

For each positive forward ratio let \(g(z)=(z-1)/(z+1)\), \(q(z)=g(z)^2\), and \(u(z)=(z-1)/(2\sqrt z)\). Define the archive endpoints \(L=7.576234/1.30447\), \(H=8.15168/1.3895212\), and the fitted cutoff \(c=(L+H)/2\).

- Geometry opens when \(q(A)+q(B)>1\). Its ideal predicted return trace is \(2-4u(A)^2u(B)^2\).
- The shifted sum opens when \(q(A)+q(B)>2q(c)\).
- The shifted product opens when \(u(A)u(B)>u(c)^2\).
- The piecewise warp opens when \(f(q(A))+f(q(B))>1\). The function \(f\) fixes each point outside the open interval \((q(L),q(H))\). Within that interval its graph joins \((q(L),q(L))\), \((q(c),1/2)\), and \((q(H),q(H))\) with straight segments. This rule preserves the geometry on all archived pairs whose two inputs were observed while moving the diagonal cutoff to \(c\).

The HTML loads zero external dependencies. The optional Playwright test runs with a locally installed Chromium or a Chrome headless shell.

```sh
CHROMIUM=/path/to/chrome-headless-shell node test_bench.cjs
```

The test replays five presets across all three rivals, checks five frozen trace values, exercises the two charts with pointer and keyboard input and verifies mobile tap, mobile layouts and zero runtime network requests. [Pinned source ledger and certificates](https://github.com/dicipler-pixel/votkp-lean/tree/893bd1018b22fcc575194196975fc9650d2006fb/research/2026-11-20-element-paper-loop-wall)
