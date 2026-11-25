# Record check: elemental-peeling-lean attribution branches (24 November 2026, Session A)

Asked by Jeromie to check the history behind a report on the branches `ej-work`, `ej-results`,
`open-math/ej-claims-attribution` and pull request #5 of `dicipler-pixel/elemental-peeling-lean`.
Read-only: nothing in that repository was changed. All times Central.

## Confirmed from git

| Item | What git shows |
|---|---|
| `ej-work` | 82 commits ahead of `main`, all authored "Elizabeth Johnson", 24 Nov 01:30 to 22:32 |
| `ej-results` | 8 ahead of `main`: 6 "Open Math OS Agent", 1 "Open Math OS", 1 "Jeromie Beasley"; 22 Nov 18:09 to 24 Nov 01:23 |
| `open-math/ej-claims-attribution` | 13 commits, all "Open Math OS Agent", 24 Nov 21:50 to 22:33 |
| Pull request #5 | open, into `main`, opened by `open-math-os[bot]` 24 Nov 21:50, title "The Harmonic Law: Elizabeth Johnson's contributions, and whose claims are whose" |
| `EJ-PROMPT-AUDIT.md` | on `ej-work`; 35 prompts; the stated rule and the count "27 moved work into her column" are in the file as quoted |
| Evidence base | `ATTRIBUTION-LEDGER.md` and `LAW-ATTRIBUTION.md` say commit dates and `git grep` are "withdrawn as evidence"; commit 959f154 is titled "the evidence base rebuilt on the chat, not on commits" |
| The git test | every test line in the two ledgers searches `main` only |
| Commit 82c045a | author and committer "Jeromie Beasley", 23 Nov 04:41, on `ej-results` and two `open-math/` branches, not on `main` |

First commit on any branch that adds each term (`git log --all -S`):

| Term | First commit | Next |
|---|---|---|
| "specific heat" | 82c045a, 23 Nov 04:41 | 24 Nov 01:23 |
| "Dulong" | 82c045a | 24 Nov 01:34 |
| "pore" | 82c045a | 24 Nov 01:23 |
| "Light Bridge" | 82c045a | 23 Nov 05:07 |
| "C_2" | 82c045a | 23 Nov 05:07 |
| "the Col" | 2a303ef, Open Math OS Agent, 24 Nov 01:23 | 24 Nov 01:30 |
| "706r" | 785121b, 24 Nov 02:10 | |

In 82c045a, `results/classical-equations.md` rows E6 to E8: C = 3RN "Dulong-Petit / Kopp", c = C/M
"the specific heat", air = c't^2 - 2 with c' = 1/(2 C_2) = 0.75739.

## Not in the report, and it matters

1. Commit 82c045a itself lists `AUTHORS.md` as "Jeromie Beasley and Elizabeth Johnson" and gives
   `results/light-bridge-paper.md` the author line "Jeromie Beasley and Elizabeth Johnson". Commit
   a596587, 26 minutes later (05:07), is "Revert the authorship line to Jeromie Beasley alone, and cite
   the Johnson paper only", and 55754c3 (05:32) writes the authorship rule down.
2. 82c045a sits between Open Math agent commits (04:43 follows it). It is a session build committed
   under his name, and it "brings in the tree" in one step, so it dates the material no later than
   23 Nov 04:41 and says nothing finer than that.
3. `results/end-digits-and-pores.md` in that commit tests 'the "end digit and pore" reading', in
   quotation marks, and finds no end-digit signal. The file does not say whose reading it is.
4. "706": in 82c045a it appears as data values in the Lean files (706.994, 706.0, 706.7). A theorem
   count of 706 was not found in the files checked.
5. The specific-heat chain is the textbook Dulong-Petit law (1819); 82c045a labels it so.
