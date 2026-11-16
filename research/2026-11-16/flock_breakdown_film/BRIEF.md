# BRIEF — full breakdown of the Flock of Balls on the Field (16 Nov 2026)

Owner: Jeromie Beasley, independent researcher (no lab; a laptop and his own papers). Byline everywhere: "Jeromie Beasley".
He asked for: "a full breakdown of this all — real good understanding of where and why all this math comes from and goes", to be turned
into an explainer film with his Tesla narrator kit. He asked for many helping hands and one agent watching the work.
You are one of the hands. The coordinator (main session) joins your reports into ONE breakdown page and then the film script.

## What "this" is
Three generations of one object, all his:
1. **Light at the Hypersurface** (one ball): the peel step B(u, r), r = ln z, Γ = tanh(r/2); faces at r/2; R = Γ², T = 1 − Γ²;
   refraction a sin²θ; total return and the gap; layers and Smith addition ⊕; pressure 2R; Thomas turn; the rim.
   Plan with every source cited: `/home/claude/balls/in/367c3aed-Light_at_the_Hypersurface_Mixer_v2_Source/PLAN_light_at_the_hypersurface.md`
   (its `GH/` paths are repos; local copies below). Code: `lh_math_v1.js`, `lh_app_v2.js`, ledgers `LEDGER_build_v2.md`, `REVIEW_fable_v1.md` in the same folder.
2. **Three Balls on the Field / Moving Matrix** (15 Nov): `/home/claude/balls/in/81dc35c1-Three_Balls_on_the_Field_v1_Source/`
   (`mm_math_v1.js` = H = D + A matrix, electron sea projector, ball fields, Weight Between readouts; `tb_math_v1.js`; README).
3. **Flock of Balls on the Field v1** (today): `/home/claude/balls/w/fl/` (`fl_math_v1.js`, `fl_check_01.js/.out`, `fl_layer_v1.js`, README.md),
   and the check that motivated it: `/home/claude/balls/w/tb/gap_clock_check_01.js/.out`. Requirements as he stated them:
   `/home/claude/balls/w/REQUIREMENTS_v1.md`. Code map of the pages: `/home/claude/balls/w/CODE_MAP_v1.md`.
   What is new in 3: links are real stretches of field with travel time; faces scatter on the way; a gap layer tunnels (HYPOTHESIS);
   each ball has its own clock, ratio z (HYPOTHESIS); ball fields held by faces (MODEL CHOICE); books = light count, exact.
   His picture for it: "the electron as a swing of chains swinging with the universe keeping it synced, or a flock of birds, or a flock of clocks".

## Where his sources are (all READ-ONLY — never modify, never write inside them)
- `/home/claude/votkp-lean/` (VOTKP Lean: `VOTKP/Smith.lean`, `Film.lean`, `Directed.lean`, `ThinFilm.lean`; `two-trees/lean/PeelTrees*.lean`, `PingPong7.lean`; `paper/`)
- `/home/claude/gh/event-horizon-lean/` (`EventHorizon/Edition10.lean`), `/home/claude/gh/nonnormality-connection-energy-lean/`,
  `/home/claude/gh/iqgt-grassmannian-lean/`, `/home/claude/gh/dirac-time-lean/`, `/home/claude/gh/light-ledger-lean/`, `/home/claude/gh/narrator-animation-kit/`
- Atlas cards (B-numbers): `/home/claude/dicipler-pixel/relational-atlas-lean/atlas/coverage/coverage.json` (or search `/home/claude/atlas_src/`)
- Other repos may be cloned read-only into `/home/claude/gh/` with `git clone --depth 1 https://github.com/dicipler-pixel/<name>.git` (square-case-lean, upg-lean, maxwell-lean, …).
- Paper texts already on disk may be under `/home/claude/corpus`, `/home/claude/text`, `/home/claude/src` (search before fetching anything).

## Rules (his standing rules; breaking them wastes his time)
- **No guessing.** Every statement about a source gives file and line (or card number) and quotes the key line. If you could not find it, say "not found", do not paraphrase from memory.
- **Run it or say "untested".** Any numerical claim you make must come from a run you did (give the command), or be marked untested.
- **Show why a check proves its claim** before the result.
- **Grades, exactly as the plan uses them:** LEAN · name / PROVED · paper, theorem / CHECKED · tolerance / CARD · Bnn (grade) / READING / DRIVE / DRAWING / MODEL CHOICE / HYPOTHESIS. Never upgrade a grade. A textbook result restated in his coordinate is a reproduction; say so.
- **His work is spoken of directly, as the work itself** ("the peel step does X"), never "his idea claims". Repair before calling anything wrong: if something looks wrong, state exactly what, where, and the smallest repair.
- **Plain scientific English**, short sentences, no slang, no hype. He does not read LaTeX: write formulas in plain Unicode (Γ = tanh(r/2)).
- Web: at most 3 web requests each, only if your task says so. Never fetch the same page twice.
- Cosmology: never describe anything as "after the big bang"; dark energy / dark matter are out.
- Write your report to the path given in your task (under `/home/claude/balls/breakdown/`). Scratch scripts go in `/home/claude/balls/breakdown/scratch/<yourname>/` and each carries `# SCRIPT: NAME` (or `// SCRIPT:`) inside.
- Report format: (1) one-paragraph plain summary; (2) the chain, link by link: statement in plain words → source (file:line, quote) → grade → what it rests on → where the Flock code uses it (file:line) → "why it is there" in one sentence a non-specialist can follow; (3) anything that does not match between source and code; (4) open or not-claimed items; (5) three to six picture ideas for the film (what moves, what number shows).
