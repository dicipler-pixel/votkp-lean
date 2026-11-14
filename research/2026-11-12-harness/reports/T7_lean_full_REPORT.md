# T7_lean_full REPORT (13 Nov 2026)

## Results first
- Full Mathlib built from source (no cache): `lake build Mathlib` = 8,923 jobs, EXIT 0, about 4 h compute across two cut-offs (a session restart stopped it at 7,708 and again at 7,778; each resume continued from built files, no module failed, no memory kills).
- The project builds: `lake build VOTKP Showcase` = 8,942 jobs, "Build completed successfully", 0 errors. Warnings only (style linters, deprecated `if_neg`, e.g. VOTKP/Energy.lean:97:2, VOTKP/Memory.lean:261:10); log project.log.
- His own gate `scripts/verify.py` (run unmodified in the copy) printed: `OK: 140 theorems, axioms used: ['Classical.choice', 'Quot.sound', 'propext'], 15 false controls rejected`. That matches config.json (expected_theorems 140, expected_false_controls 15). Each of the 140 carries only those three axioms; the 15 FalseControls fail to compile for mathematical reasons as intended; Showcase statement file matches the proved Showcase.main_theorem (his script checks this).
- grep for `sorry` in VOTKP, FalseControls, Showcase*.lean: none (the only hits are the words "no sorry" in two-trees header comments). No `axiom` declarations anywhere.
- two-trees/ is not a lake project (core Lean, no Mathlib). Built in place with `lake env lean` per file: PeelTrees, PeelTrees2, PeelTrees3, PeelTrees4, PingPong7 all compile, 0 errors, 0 output. Theorem counts 74 + 49 + 7 + 12 + 17 = 159, equal to the README badge. `#print axioms` on every one of the 159: none uses sorryAx or a project axiom; sets seen are [propext], [propext, Quot.sound], [propext, Classical.choice, Quot.sound], or "does not depend on any axioms". No native_decide in the files.
- two-trees/lean/controls/Controls1.lean and Controls4.lean fail by design (decide proves `1 + 1 = 3` false; ring disequality), as controls should.
- Earlier T6 file NewProps.lean (narrow imports) was not recompiled against the full build; its T6 result stands.

## Errors
None.

## Headline theorems
verify.py audits every named theorem (all 140), so the headline ones are covered; I did not separately list them.

## Method
- Built in place inside T6_lean/proj (its .lake), as allowed. Scripts: build.sh, proj_build.sh here. Logs: mathlib.log, project.log, verify.log. verify.py wrote its output to T6_lean/proj/verification/.
- Not pushed anywhere. Nothing in his Lean files was changed.

## Untested
- Lean files in the repo outside VOTKP, FalseControls, Showcase, two-trees/lean (peel-atlas, research, data, docs) were not built.
- Whether the repo's GitHub CI matches this local result is not checked.
