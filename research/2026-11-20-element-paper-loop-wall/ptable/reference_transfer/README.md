# Reading a period with only other periods on the shelf

The rule was committed at `e3367e4` before this run. The archived elements and their periodic assignments had already been examined in previous work. This is a transfer test on existing data. The reference elements never include the query or another member of its excluded period in the first panel. In the second panel the reference library ends at astatine. Both panels exclude the detached f rows.

| Full-precision archive comparison | Eligible | Simplex | Plain Euclidean log ratios | Simplex-only / plain-only | Two-sided sign p |
|---|---:|---:|---:|---:|---:|
| Exclude the query's whole period, F–At | 62 | 58 | 56 | 4 / 2 | 0.6875 |
| Rn–Og queries against the frozen F–At collection | 8 | 5 | 8 | 0 / 3 | 0.25 |
| Exclusively experimental, nine consecutive energies | 0 | — | — | — | — |

The simplex did not clear the predeclared transfer hurdle on either panel. The eight heavy examples favour ordinary log ratios by three hits, with substantial uncertainty. The archive's 72 heavy query thresholds carry four experimental, 24 semiempirical and 44 theoretical grades. No nine-threshold ladder in the historical reference collection consists entirely of experimental entries either. The sign tests count discordances between methods. Chemical relationships within this small set limit their statistical interpretation.

## Every heavy query

| Query | Grades in removal order | Simplex nearest | Log-ratio nearest | Long-column outcome |
|---|---|---|---|---|
| Rn | ETSTTTTTT | Xe | Xe | both |
| Fr | ESSTTTTTT | Cs | Cs | both |
| Ra | EETTTTTTT | Ba | Ba | both |
| Rf | TTTTTTTTT | Ge | Hf | plain logs |
| Db | TTTTTTTTT | As | Nb | plain logs |
| Sg | SSSSSSTTT | Se | W | plain logs |
| Bh | SSSSSSSTT | Re | Re | both |
| Hs | SSSSSSSST | Ru | Ru | both |

On the historical split the simplex gains Co, Rh, Ir and Au and loses Hf and Ta. On the heavy split it places Rf, Db and Sg beside groups 14, 15 and 16 instead of 4, 5 and 6. All three are the corresponding A/B partners. That observation was made after the primary long-column test. The change of grouping cannot convert those three misses into primary hits. The inputs for Rf and Db are wholly theoretical in the archive.

Run `python3 replay.py` from any directory. The script writes [per-element predictions](predictions.csv) and the [counts and element-by-element exclusions](results.json). It checks the archive fingerprint and uses Python's standard library. The per-query CSV gives the grades of each nominated neighbour, pool size, ties and whether the correct group was represented. All scored queries had an attainable label and a unique nearest neighbour. H through O have fewer than nine electrons to remove; the missing charges for those elements are physically unavailable. The archive has gaps at Mt through Og. Ac–Lr and La–Lu were excluded by the protocol. Grade E denotes experimental, S semiempirical and T theoretical. No part of either distance uses the wall value.
