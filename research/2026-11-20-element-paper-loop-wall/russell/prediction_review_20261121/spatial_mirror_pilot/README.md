# A grade-blinded test of one interpretation of Russell's mirror

Twenty-four randomly ordered historical claims were sampled from Jeromie Beasley's September ledger, balanced by the original T/F grades within each of its three source groups. The selection was deterministic from a public hash rule. Two Codex workers started with fresh contexts and received the claim text, a preregistered codebook for *spatial inversion of the entire system*, and no source IDs or grades. These are two runs of an AI system, not independent human historians. Both froze their reasons before the joint score. The protocol was established locally before grading and on the branch before the joint score. The two retrospective datasets are named in PROTOCOL.md.

| Result | Count |
|---|---:|
| All labels agreed between the two raters | 23 of 24 |
| Both rated the principal readout even under spatial inversion | 20 |
| Both withheld a label | 3 |
| Disagreement (withheld versus even, L25) | 1 |
| Both rated a principal readout odd | 0 |
| Original grades among the 20 agreed-even cases | 10 T, 10 F |

Thus a rule that calls a claim true because its readout is even scored **10/20**, with four withheld cases. Each of the ten agreed-even false claims is a counterexample to that rule on this panel. The experiment does not estimate accuracy in Russell's full record, and cannot estimate odd-class performance because neither rater assigned O. Spatial inversion preserves many relations and scalar errors alongside correct scalar laws. A different question about charge conjugation, exchanging clocks, transposing a record or reversing one spatial component needs a named operation and its own blinding.

The source grades were copied from the author's public ledger (version-specific deposit 22986657) as an external answer key; they were not regraded here. This 24-position panel and the 132-ID element-specific crosswalk serve different purposes and may overlap. Counts cannot simply be added. The full 585-position project would need an operation specified for each physically scoreable readout and a policy for abstentions; this pilot does not complete it.

The public scripts, raters' own explanations, token-to-source key and result.txt permit rechecking without redistributing the historical claim texts. Rebuild the masked questions locally with select_pilot.py and the source ZIP if needed, then replay score_pilot.py in this folder. The local questionnaires given to the original raters contained only a token and the source claim.
