# Two predictions from twin_chain_v1 Section 12, run now (2026-11-25T03:13:00Z). Kill conditions as printed in v1.

TWIN-SPLIT-79-01 (v1 Prediction 6). The 0.07 offset in the 7/9 split beyond 1e9 comes from the walk's
step weighting, not from the tooth form. KILL if a direct gap-weighted count on twin starts in
(1e9, 1e10] reproduces the walk's split (+0.72, +0.20) rather than the prediction (+0.81, +0.14).
Operational: kill if the direct count's digits 7 and 9 are both closer to the walk values than to the
prediction. Real-data definition (same as v1): dev_j = gap-weighted share of class j minus count share,
gap = distance back to the previous twin start; times G = mean gap.
Method check first: the same code on (1e8, 1e9] must give (-0.924, +0.839, +0.085) to 0.002.

COUSIN-THREAD-01 (v1 Prediction 7). Same full-product construction with pattern {0, -4, h, h-4} and
cousin classes 7, 13, 19 mod 30. KILL if classes 7 or 13 miss the real cousin values at 1e8-1e9 by more
than 2 se (se from 30 equal blocks).
