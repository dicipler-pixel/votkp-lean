# How much of the comparison can use experimental thresholds alone?

Three consecutive experimental-grade thresholds starting from the neutral atom give two positive peel steps. That is enough for the project's shape comparison to have one independent coordinate. Under the protocol committed before this calculation (`67c1435`), 33 elements from F through At qualify. We found the nearest element in a different period. The triangle-family profile recovers 18 long-form columns, versus 17 with plain Euclidean distance on the two log ratios. The methods agree on success or failure 28 times. The profile gains Ne, As and Kr, and loses Se and Br. The two-sided sign test is 1.00 for three wins and two losses. This experimental-only comparison supplies no advantage under the specified test.

The reference pool contains no member of the correct group in a different period for Ti, V, Cr, Mn, Fe, Ni and Cu. Keeping all seven in the primary denominator limits achievable recall to 26/33. Among those 26 with an available group, the same predictions score 18/26 and 17/26. At K=2 none of the Rn–Og queries outside the detached row has the required three consecutive E-grade thresholds in the archive. Later measured levels at higher charge cannot fill a missing initial rung.

| Log steps K | Historical queries | With available correct column | Simplex / plain logs at K | Two-step scores with same eligible queries and references |
|---|---:|---:|---|---|
| 2 | 33 | 26 | 18 / 17 | 18 / 17 |
| 3 | 22 | 17 | 16 / 14 | 11 / 12 |
| 4 | 12 | 7 | 7 / 6 | 3 / 3 |
| 5 | 4 | 0 | 0 / 0 | 0 / 0 |
| 6 | 1 | 0 | No other-period candidate | No other-period candidate |
| 7 | 0 | 0 | No queries | No queries |
| 8 | 0 | 0 | No queries | No queries |

At three steps, keeping the same 22 queries and reference candidates changes the scores from 11 to 16 for the simplex and from 12 to 14 for plain logs. This is a descriptive contrast on a coverage-selected group. Across different rows of the table, both coverage and the rung count change. At five steps four elements have candidates but none has its true group represented in another period. At six the single element has no candidate at all.

Run `python3 experimental_prefix.py`. [Frozen protocol](EXPERIMENTAL_PREFIX_PROTOCOL.md) · [Counts and paired differences](experimental_prefix_results.json) · [Every nomination and candidate-pool size](experimental_prefix_rows.csv)
