# Verification brief (read fully)

You are verifying one part of Jeromie Beasley's paper "What the Peel Keeps" v1.2. The goal: ONE correct paper with no hallucinations. Every factual claim and every number must trace to a real source or a recomputation.

Paper source (markdown): /home/claude/paper_v12/build/src/<files named in your task>.
Sources you may use (READ ONLY, never commit, push or branch):
- Repo: /home/claude/votkp-lean (branch element-paper/loop-wall checked out). Element folder: research/2026-11-20-element-paper-loop-wall/ (batches, checks, lean, russell/prediction_review_20261121/**, holdouts, connections, ptable/ptable_data.json, manuscript/What_the_Peel_Keeps_v1_1b.pdf, VOTKP_Element_Paper_Loop_Wall_v8_20261121.html).
- Threshold archive: /home/claude/votkp-lean/data/element_thresholds_20261011.json.gz.
- VOTKP v3.3 and v3.2 text: /tmp/vk/v3_3.txt, /tmp/vk/v3_2.txt (html beside them). Other branches: git -C /home/claude/votkp-lean show origin/<branch>:<path> (branches: claude/sm-ball-20261111, claude/votkp-research-20261110, claude/moving-matrix-of-balls, claude/light-at-the-hypersurface, main). Fetch with git fetch if missing.
- Earlier read reports: /home/claude/paper_v12/reads/R1_versions.md, R2_records.md, R3_batches_lean.md, R4_framework.md (useful pointers, but NOT proof: confirm in the source file itself).
- Lean binary: /opt/lean/lean-4.34.1-linux/bin/lean.
- Web search/fetch allowed only for published literature citations (prior art, journal references).

Method, for EVERY sentence in your files that states a fact, number, theorem name, citation or attribution:
1. Find the source file and line (or recompute it with a short Python script you run; save scripts under /home/claude/paper_v12/verify/scripts/, each with a "# SCRIPT: NAME" line).
2. Verdict: VERIFIED (give path:line or script output), WRONG (give the correct statement and its source), UNTRACEABLE (searched where, found nothing), or OVERSTATED (source says less; give the source's exact scope).
Ignore pure framing sentences with no checkable content, but DO check every attribution of an idea to a paper/section ("§12.6 of Dirac Time says…", "Theorem 5.3…").
Rules: write "crossing number" in full, never "CN"; no slash pairs; say "the electron's spinor (Dirac) structure", never "relativity". Do not edit the paper. Do not guess: if you cannot reach a source, say UNTRACEABLE.

Output: /home/claude/paper_v12/verify/<your group>_report.md — a table: file | quoted claim (short) | verdict | evidence / correction. Put all WRONG, OVERSTATED and UNTRACEABLE rows first. End with counts. Reply with the counts and the non-VERIFIED rows.
