# CODE MAP v1 — existing pages behind "the multi balls on the field"

All sources read-only. Line numbers refer to these files (one long line per statement, so a line number is precise):

| Short name | File | Notes |
|---|---|---|
| KIT | `/home/claude/balls/ex_three_1_mixer3d_parts_v1.js` (218 lines) | byte-identical to `ex_surp_1_...` |
| LHM | `/home/claude/balls/ex_three_2_LH-MATH-V1.js` (255) | identical to `in/367c3aed-.../lh_math_v1.js` |
| APP | `/home/claude/balls/ex_three_3_LH-MIXER-V2.js` (381) | = `in/367c3aed-.../lh_app_v2.js` except line 264 (adds `__TBHOST`) |
| MM | `/home/claude/balls/in/81dc35c1-.../mm_math_v1.js` (236) | shipped copy `ex_three_4_MM-MATH-V1.js` = same lines 1–236, then TB-MATH at 238–268 |
| TBM | `/home/claude/balls/in/81dc35c1-.../tb_math_v1.js` (31) | |
| L1 | `/home/claude/balls/ex_three_5_TB-LAYER-V1.js` (99) | identical to `in/81dc35c1-.../tb_layer_v1.js` |
| L3 | `/home/claude/balls/ex_two_TB-LAYER-V3.js` (123) | extracted here; the same text sits in both pages of Two Balls Linked |
| APP3 | `/home/claude/balls/ex_two_LH-MIXER-V2_app.js` | the Mixer app as shipped inside Two Balls Linked; differs from APP at lines 212, 213, 263, 264 only |
| SM / SA | `/home/claude/balls/ex_surp_2_...js` (maths, 129) / `ex_surp_3_...js` (app, 219) | the white "Surprise" ball |
| SHELL | `/home/claude/balls/ex_two_LINKED-SHELL-V1.js` | tail of the Two Balls Linked page |
| pages | `/home/claude/balls/ex_two_mixer.html`, `/home/claude/balls/ex_two_white.html` | the two whole pages decoded from `const PAGES` |
| BUILD | `in/81dc35c1-.../build_three_v1.py`, `in/367c3aed-.../lh_build_v2.py` | |

Two different "between the balls" models exist. **L1** (Three Balls v1) uses the matrix MM/TB: instantaneous links. **L3** (inside Two Balls Linked) uses no MM/TB at all: it carries the single ball's traced rays into each ball's chart. The earlier check `/home/claude/balls/w/tb/gap_clock_check_01.out` was run on the L1 model.

## 1. How one ball is drawn three times, and what blocks N balls

- The ball is one three.js group `WORLD` (APP 69), holding 11 sub-groups `G[c]` for `COMPS` (APP 28, 70). It is added to the stage once (APP 264) and handed to the layer as `window.__TBHOST = { S3, WORLD, tau(), S() }` (APP 264).
- Nothing is cloned. L1 replaces `renderer.render` (L1 49–56). Per frame: `step()`; set the camera; clear once with `autoClear = false`; then `for b in 0..2`: `WORLD.position.copy(pos[b])`, `FIELD.visible = (b === 0)`, `R.toneMappingExposure = 0.28 + 0.85*min(1, share[b])`, call the original render (L1 55). So each copy is the same object in the same state, moved and re-exposed.
- Placement: `layout(S)` (L1 23–24): A at origin, B at `(dI,0,0)`, C at `(0,0,−dJ)` with `d = RB*(1 + tanh(h/2))`, `RB = 2.6`, `h = r/2`; then recentred on the mean. This is a drawing convention (README: "each ball's rim passes through the cap vertex on the shared arm"); the drawn B–C distance is Euclidean, not the hyperbolic `d_BC`.
- Scale: none; every copy has radius RB. Lit by `share[b]` = `MM.lightDensity(St,b)` or the chosen eigenvector's share (L1 32).
- Field objects in `FIELD` (L1 15–21): `lens` (ring where two rims meet), `flowLine`, `arrows` (each ball's field d), `flowPts`, `midPts`, `corePts`, labels.
- L3 does the same render trick (L3 61–76) and in addition rewrites the position buffers of the light objects `H.light` per ball by `carry()` with `chart(S,b) = G_b⁻¹ G_src` (L3 24–26, 51–57, 73–76), then restores them.

What has to change for N balls (e.g. 7) at arbitrary field positions:

| Blocker | Where |
|---|---|
| Ball count fixed at 3: `NAMES`, `COL`, `COLV`, `pos`, `TR`, `share`, `AL`, `AS`, `for(i<3)`, `[0,1,2]`, buffer sizes `3*128`, `3*40`, `3*4`, `3*14` | L1 11, 13, 19–21, 26, 30–32, 44, 55, 80–96 |
| Layout knows only the I and J arms | L1 23; L3 36 |
| World builder fixed at 3 points and 3 pairs: `PAIRS`, `pts(r)`, `nbr` literal, `tris:[[0,1,2]]`, `modes` share over `[0,1,2]`, `loop` on triangle `[0,1,2]`; `relink`/`advance` call `pts(r)` | TBM 11–12, 15–16, 21–23, 25, 28 |
| Kick buttons A/B/C and eigenvector slider `max="5"` (= 2N − 1) are literal HTML | L1 67, 69 |
| Every copy shows the same ball state `S` (same z_I, z_J, z_K, same rays, same τ). A ball with its own clock or own steps needs its own `S = L.feed(PP, τ_i)` and its own `update()` before its render pass; `update()` (APP 206–214) writes into shared buffers, so this is one full update (about 4 ms of script, LEDGER_build_v1 line 75) plus one full scene render per ball per frame | APP 206–214; L1 55 |
| Render cost: N whole-scene passes per frame (RAYL alone is 60000 vertices, APP 90) | L1 55 |
| L3 only: `REL` (letters from the kicked ball to each other ball) and `cells()` are written out for A, B, C | L3 24–28, 45–48 |

Already general in N (no change needed): everything in MM — `applyH`, `denseH`, `eigh` ("n up to ~200", MM 102), `groundProjector`, `initState`, `deriv`, `rk4`, `energies`, `lightCurrents`, `lightDensity`, `ballPowers`, `ballCensus`, `seaSpeed`, `tauDot`, `restState`. `MM.makeWorld(level, opts)` (MM 82–89) with `buildSeries` (MM 62–78) already builds 7 balls at level 1 (centre + six spokes, 6 + 12 links, octahedral triangles) and 49 at level 2, but with ONE step length per level (`opts.steps`), not separate r_I, r_J, r_K. A world is just `{ N, balls:[{p}], links:[{i,j,d,Gam,c,R,U}], tris, nbr, d, opts }` (TBM 16); `TB.linkOf` (TBM 13) makes a link from any two hyperboloid points.

## 2. Where the matrix state is advanced, its readouts, and every use of the instantaneous link

Advance (L1 model):

- Clock: `CLOCK.tau` in the app (APP 21), advanced in `update()` (APP 206) by `d = clamp(dt,0,0.05)*CLOCK.speed`. The layer reads it through `H.tau()`.
- `step()` (L1 29–47), called from inside the render override (L1 52): `dt = min(0.1, tau − lastTau)`; if `tau` went backwards, `build()`.
- `TB.advance(W, St, S.r, dt, 0.01)` (L1 30; TBM 22–23): `n = ceil(dt/0.01)` steps of `MM.rk4(W, St, h)` (MM 165–170, with `purify` MM 174), then `relink(W, r)` to the breathing steps and book the energy change as `St.work`.
- `MM.deriv` (MM 150–161): `i ψ' = Hψ`; `P' = −i[H,P]`; `d_i' = (s_light + s_sea + face gradient) × d_i`. One `h` for every ball: no ball uses its own time.
- `build()` (L1 25): `TB.makeWorld(S.r)` (rest state by descent, TBM 20), `MM.initState` (ground projector = the sea, MM 136). `kick(i)` L1 27; `intoMode()` L1 28.

Readouts produced:

| Readout | Source |
|---|---|
| `EN = MM.energies` → `EL, ES, EF, Eper[k], E` | L1 31; MM 177–180 |
| `CUR = MM.lightCurrents` (one per link, J > 0 = from j into i) | L1 31; MM 182–184 |
| `TR[k]` running sum of abs(CUR)·dt | L1 31 |
| `share[i]` = light in ball i, or eigenvector share | L1 32 |
| `AL[i]`, `AS[i]` first time light > 1e-3 / sea occupation moved 1e-3 | L1 30 |
| rows every 250 ms: link d, link c, light, flow, face energy, loop turn / area / Thomas, books, norm, in − out, arrival times, clock limit τ̇²/(4gS), eigenvalues, eigenvector shares, margin | L1 79–97 |
| `MD = TB.modes` (eigenvalues, vectors, shares, lead, margin) | L1 26, 28, 77, 79; TBM 25–26 |

Every use of the instantaneous link:

| Use | Where |
|---|---|
| Link strength defined from distance only: `c = c0/cosh(d/2)` | TBM 13; MM 85 |
| `applyH`: `y_i += c U x_j`, `y_j += c U† x_i` in the same instant | MM 96–99 |
| `applyH` callers: `denseH` MM 101, `deriv` MM 151 and 157, `energies` MM 177–178 | |
| `lightCurrents` uses `l.c`, `l.U` | MM 182–184 |
| Face energy and gradient use `l.R` across the link instantly | MM 145–147 |
| Drawing: ring colour `gj` from CUR (L1 37); path brightness from TR (L1 41); moving markers `flowPts` — their direction is `sign(CUR[k])`, their speed is the fixed wall-clock `performance.now()/1000*0.45` (L1 42), not a signal speed; `midPts` (L1 43) | |
| Readout rows "link strength" and "flow across each face" | L1 84, 86 |

So the only "light moving between balls" on the L1 page is the row of 14 markers per link at L1 42: decoration whose sense follows the current. Nothing in MM carries a delay, a field in the gap, or the face gap δ (`S.pairs[i].delta`, LHM 173, is computed by the single ball and never read by MM/TB).

L3 model: no link at all. `handover(S)` (L3 39–49) sums `flux × T` of the single ball's own traced rays crossing toward each ball; `X.eps` moves B and C off their place; still one shared `S` and one clock.

## 3. The eyes of LH-MIXER-V2

| id | title | defined at |
|---|---|---|
| A | A · The object: four balls, faces, rim | APP 268 |
| B | B · One face is one reflecting step | APP 273 |
| C | C · Refraction at the face | APP 279 |
| D | D · Total return and the gap | APP 283 |
| E | E · Layers: echoes and Smith addition | APP 296 |
| F | F · Pressure and the kick record | APP 305 |
| G | G · Rotation within and outside the layers | APP 312 |
| H | H · Light on the rim | APP 319 |
| I | I · The hypothesis layer | APP 326 |
| J | J · Everything at once, and the ledger | APP 337 |

- An eye never has its own scene. `eye(o)` (APP 264–265): `enter()` copies `EMPH[id]` into the target weights `WT`; `view:views[id]` is `[yaw, pitch, dist, ty]` (APP 245); `step(dt)` runs the one shared `update(dt)` and returns that eye's `rows()`.
- Emphasis: 11 components `COMPS` (APP 28); `EMPH` table APP 246–256; `applyEmph` (APP 33–34) eases `W[c]` toward `WT[c]` and sets every registered material's opacity to `base*W[c]` (`REG`, APP 30–32). `hyp` is also gated by the strip toggle `HYP.shown`.
- Camera: KIT `show(id)` calls `S3.setView(cur.view)` on every eye change (KIT 191), so yaw, pitch, distance are reset each time; it also rebuilds `#ctl` and calls `enter`.
- Combined: in APP, no. KIT holds one `cur` eye (KIT 178, 185–193). Eye J is the built-in "everything" view (all weights 1).
- L3 already adds combination on the Mixer ball (L3 105–117): a set `ON`; every 80 ms `WT[c] = max over (open eye + ON) of EMPH[id][c]` (L3 114); buttons per eye, "all", "only the open eye"; readouts of the extra eyes appended in `#tb_more` (L3 115–116). It needs `H.eyes, H.EMPH, H.WT, H.cur, H.TSP`, which APP3 line 264 exposes and APP does not. APP3 also gives rays, layers, rotation and rim their own timing (`TLS`, `TSP`, `TLstep`, APP3 263; used at APP3 212–213).
- On the white ball L3 gives each drawing layer a visibility switch (`H.layers`, L3 119–121; adapter in `ex_two_white.html`, after the `S3.onFrame` line of SA): faces, crossings, tree, rays, arms, loops, record, gaps.

To make every eye an independent on/off toggle with a combined "all" view:

1. Keep weights as max (or sum, clamped) over the set of eyes that are on (as L3 114), with no privileged "open eye"; allow the empty set.
2. Stop the camera reset: `S3.setView` in KIT 191 must not fire when an eye is toggled.
3. `#eq`, `#what`, `#tag`, `#ctl`, `#read` are single slots filled for one eye (KIT 189–191, 210). Combined mode needs one block per eye that is on, or a merged readout. `rows()` of any eye can be called at any time because all read the shared `S`, `AUD`, `LIVE`, `ST` (the try/catch at L3 115 is a guard only).
4. Sliders: `controls(e)` (KIT 179–184) builds only the sliders in `e.uses`; a combined view needs the union. Extra buttons come from `e.extra` and `e.bind`.
5. Film mode (KIT 196, 207) steps through single eyes with `show`; decide what it does when several are on.

## 4. The camera

- State: `V = { yaw:0.75, pitch:0.42, dist:7.2, ty:0.4, auto:true, panel:true }` (KIT 91), exposed as `S3.view`.
- Orbit: one pointer drag changes yaw; pitch clamped ±1.3 (KIT 99). Any pointer down sets `auto = false` (KIT 96). Auto-turn 0.08 rad/s (KIT 108).
- Zoom: wheel `V.dist = clamp(V.dist*exp(deltaY*0.001), 3, 20)` (KIT 103); pinch, same clamp (KIT 101). `setView` (KIT 119) is not clamped.
- Position: `D = V.dist*(innerWidth < 640 ? 1.5 : 1)`; camera on a sphere about `(0, V.ty, 0)`, `lookAt(0, V.ty, 0)` (KIT 109–111). Perspective 45°, near 0.05, far 200 (KIT 87).
- Pan / target: none. The target is fixed on the vertical axis; only its height `ty` can be set, and only through `setView`. No keyboard, no right-drag, no double-click.
- Picture shift: while the left panel is shown, `camera.setViewOffset` moves the picture right by `min(180, 0.14 w)` px on desktop, or up by 20% of the height on mobile (KIT 92–93). Clean view clears it (KIT 200).
- The layers override the camera every frame (L1 52–53; L3 70–71): `Dc = V.dist*2.0` (×1.5 on narrow screens), pitch `+0.55` clamped to [−1.3, 1.35], yaw `+0.55`, `lookAt(0,0,0)`; `V.ty` is ignored. Effective distance range is therefore 6 to 40.
- White ball: named views `VIEWS` whole / cell / arm / rim (SA 208–209).

For zoom by percent: define a reference distance (100%) and show `100*ref/dist`; the 3–20 clamp at KIT 101 and 103 limits the range and must widen for a larger field (far plane 200 is the hard limit). For moving across the field: add a target point (x, z, and height) to the view state and use it in both the camera position and `lookAt` (KIT 110–111 and L1 53 / L3 71); add an input for it (drag with a modifier or second button, arrow keys, or click a ball to centre on it). The kit's listeners are anonymous and cannot be removed, so either ship a new kit file (`mixer3d_parts_v2`, new name, original untouched) or do it all in the layer, which already owns the final camera each frame, and intercept wheel/pointer in the capture phase.

## 5. Every DOM panel

Three Balls on the Field, Mixer page (`8ee08d50-Three_Balls_on_the_Field_Mixer_v1_20261115.html`):

| Element | Made at | Position | Shows |
|---|---|---|---|
| `canvas#stage` | KIT 158; CSS KIT 127 | fixed, whole window | the 3D view |
| `div.panel#panel` | KIT 159–171; CSS KIT 128–130 | top LEFT 12 px, width 350, full height; ≤ 640 px wide: bottom, 46% high | title, byline, eye buttons `#eyes`, `#tag`, `#eq`, `#what`, sliders `#ctl`, readout `#read`, Eye / Film / Clean view / Frame PNG, seconds per eye, film bar, hint |
| `button.cleanexit#m_back` | KIT 172; CSS KIT 131 | bottom right, only in clean view | "show panel" |
| `div.strip#strip` | APP 364–367; CSS APP 360–363 | bottom RIGHT 12 px, max-width min(560 px, 100% − 390 px); ≤ 640: top | `#tau`, Play, Step, Speed, Reset τ, hold / breathe / sweep, Hypothesis layer, Admittance |
| `div.tb#tb` | L1 64–69; CSS L1 58–63 | top RIGHT 12 px, width min(340 px, 100% − 400 px), max-height 100% − 110 px, z-index 5; ≤ 900: bottom band 34% high | "Three balls on the field": What this shows; Three balls / One ball / Restart / Sea pushes back; Kick A / B / C; Lit by; Put the light in this eigenvector; Eigenvector slider `#tb_n`; Leading eigenvector; "light in A, B, C" `#tb_sh`; "All the numbers" `#tb_rows` |

"The data control box on the right" is `#tb` (class `.tb`): it is the only box that holds both data and controls, it is the one the three-ball layer added, and it sits over the right-hand balls because the kit shifts the picture to the right to clear the left panel (KIT 93). The control strip `#strip` is the other box on the right (LEDGER_build_v2 line 120: "The control strip has moved to the bottom right"). He did not name which; see REQUIREMENTS C1. All three boxes are hidden by `body.clean` (KIT 130, APP 362, L1 62).

If `#tb` goes, these need a new home or are lost: three/one toggle, Restart, sea toggle, kick, lit-by, into-eigenvector, eigenvector slider, leading, and all rows at L1 83–95. In L3 it also carries the placement slider `#tb_eps`, "Just right", the eyes-on-together buttons `#tb_eyes`, the own-timing sliders, the layer switches `#tb_lay`, and `#tb_more`.

Two Balls Linked (`139f7edd-...html`): shell `#bar` (top, 38 px high, full width: Ball mixer / white / both, Zoom one / three, Kick A / B / C, `#pp`, `#tau`), `iframe#f_mixer`, `iframe#f_white` (below the bar, full size), `#note` (bottom centre). Inside each frame: the same `.panel` (left) and `.tb` (top right, width min(300 px, 100% − 400 px), L3 78), plus `.strip` in the Mixer frame. `body.linked` hides `.tb`, `.panel`, `.strip`, `#back` in the white frame when both are overlaid (L3 82).

White (Surprise) ball page (`ex_two_white.html` head; original `6f0930cc-...html`): static markup, not built by `Mixer3D.run`. `canvas#stage`; `div.panel#panel` top LEFT, width 390: title, text, `#play`, `#reset`, `#o_tau`, `#hypt`, `#sig`, sliders `#speed`, `#amp`, `#rays`, camera buttons `data-view`, `#clean`, legend, `#laws`, `#hypbox` / `#hyp`, "What is not claimed"; `button#back` bottom right in clean view. Nothing on the right until the layer adds `#tb`.

## 6. Global names and build order

| Global | Set at | Holds |
|---|---|---|
| `THREE` | three.js r158 block | |
| `window.Mixer3D` | KIT 217 | `T, colour, tcol, sprite, glow, points, setPt, flush, line, setLine, orb, paintOrb, shell, box, grid, trail, pushTrail, clearTrail, surface, setSurface, label, stage, run` |
| `window.MIXER_API` | KIT 213 | `show, setMode, clean, P, S (getter), set(id,v)` |
| `window.LH` | LHM 254 | maths api (LHM 250–253); on the white page `var LH` is a different, smaller object (SM) with the same name |
| `window.__S3` | APP 264 | the stage `{ T, scene, camera, renderer, world, view, resize, onFrame, setView }` |
| `window.__TBHOST` | APP 264 (three-ball pages) | `{ S3, WORLD, tau(), S() }`; in APP3 also `kind, light[], eyes[], EMPH, WT, cur(), TSP`; white page: `kind:'surprise', tr(), light[], layers{}` |
| `window.__lh` | APP 377–380 | `go, setTau, play, set, hyp, selftest, S, AUD, ST, rows, CLOCK, PP, bench` |
| `window.MM` | MM 225 | matrix maths; `MM.restState` added at MM 230 |
| `TB` (`var`) | TBM 8 | `PAIRS, NAMES, pts, makeWorld, relink, advance, modes, loop` |
| `window.__tb` | L1 98 / L3 122 | L1: `X, build, kick, intoMode, rows, setOn, state, books`; L3: `X, rows, setOn, ON, HO, chart` |
| `window.__LHS` | SA 217 | white ball: `CLOCK, P, UI, S3, state, step(d)` |
| `window.__link` | SHELL last line | `mode, set(m), ready, W, clock, view` |

`CLOCK`, `PP`, `ST`, `S`, `WORLD`, `WT`, `EMPH` are closure variables of the app, reachable only through `__lh` and `__TBHOST`.

Build order:

- `lh_build_v2.py` (lines 5–11): head; three.js block and kit block cut verbatim by character offsets from `balls_v2_ref.html`; `<script>` LH-MATH; `<script>` LH-MIXER app.
- `build_three_v1.py` (lines 4–12): reads `../mm/mm_math_v1.js`, `tb_math_v1.js`, `tb_layer_v1.js`; takes a finished page; one exact string replacement in the app that adds `window.__TBHOST` (asserted to occur once); replaces the title; inserts before `</body>`: `<script>` MM + TB maths `</script><script>` layer `</script>`. Final script order: three.js, kit, LH-MATH, LH-MIXER, MM-MATH + TB-MATH, TB-LAYER. Done for two pages: the Mixer v2 ball and the Surprise v1 ball. Its input paths (`../lh_build/`, `../surprise/`) are relative to a work folder that is not in the zip.
- Two Balls Linked pages: three.js, kit, ball maths, ball app, TB-LAYER-V3. No MM or TB.

LINKED-SHELL-V1 (SHELL): there are no messages. No `postMessage` and no `message` listener anywhere. The two pages are loaded with `iframe.srcdoc` (same origin) and the shell reaches into `contentWindow` directly. `link(from, to)` runs every animation frame from master to follower (`tick`) and copies: clock `tau, playing, speed, anim`; steps (`PP.zI/zJ/zK, A, orient` ↔ `P.zbar[], amp, sigma`; `hold` maps to `amp = 0`; `sweep` is turned into `breathe` when the white ball is master); camera `yaw, pitch, dist, ty` and `auto = false`; `__tb.X.src`, `X.eps`, and `setOn`. Master is the white page only in white mode. "Both as one" stacks the white frame over the Mixer frame with `mix-blend-mode: screen` and no pointer events. Bar buttons write `__tb.setOn` and `__tb.X.src` in both frames; `#pp` flips the master's `CLOCK.playing`.

## 7. Fragile points

1. First frame can report a negative dt: `last = performance.now()` is taken at stage creation and `frame` uses the rAF timestamp with an upper clamp only (KIT 105–107). The app clamps at zero (APP 206, comment there); the white app clamps (SA 216); any new per-frame code must clamp too. The v1 ledger records the fault this caused (clock at −0.057 s, rim eye indexing arm −1; LEDGER_build_v1 lines 77–85).
2. `tEye` is reset in `show` (KIT 187) and passed to `step`, but the LH eyes ignore it. Film mode calls `show` on every change, which resets the camera (KIT 191) and rebuilds `#ctl`.
3. The matrix is stepped inside the render override (L1 52). With "One ball" on, `step()` is not called and the matrix stands still while `CLOCK.tau` runs; on return at most 0.1 is advanced (L1 29). Any other code that calls `renderer.render` on the main scene would step it again.
4. Clock going backwards (Reset τ, `__lh.setTau`, or the shell copying a smaller τ) triggers `build()` (L1 29): world, sea and all books restart.
5. `TB.advance` re-links to the breathing steps each frame and books the energy jump as work (TBM 22–23); the "books" row depends on that order.
6. `ballCensus().tau` is `log((1−ν₀)(1−ν₁)/(ν₀ν₁))` (MM 195): infinite when an occupation is 0 or 1. The earlier check output shows `tau-tau0 -Infinity` on every line of block C4, so the existing per-ball offset clock cannot be used as a ball's time as it stands; only `tauDot` (MM 218–222) is finite there.
7. `TB.makeWorld` `nbr` is a literal that happens to be right for the triangle (TBM 15); `MM.makeWorld` builds it properly (MM 86). `MM.faceGrad` depends on it.
8. `groundProjector`/`chooseCut` pick the sea's filling from the largest gap near half filling (MM 126–129); with a different N or link set the cut can move.
9. Cost that grows with N: `deriv` applies H to every column of P; `purify` is two dense (2N)³ products per rk4 step; up to 10 rk4 steps per frame; `rows()` every 250 ms runs `eigh`, `deriv`, `ballPowers`, `seaSpeed`.
10. Layer sets `R.toneMapping = LinearToneMapping` for the whole page (L1 50) and exposure per pass; L3 does not.
11. L3 `carry` rewrites and restores the light buffers in place each frame (L3 73–76); it assumes ball-local coordinates with RB = 2.6 and treats points with r² ≥ 0.9996 as rim directions (L3 53, 55).
12. Objects rebuilt while running: ball labels every 0.5 s (APP 129–130) and crossing lines every frame (APP 140–145) are removed from `REG` and re-registered; code that caches materials or `REG` indices will go stale.
13. Wheel and drag listeners sit on the canvas only (KIT 96–103); any panel over the canvas swallows them.
14. `build_three_v1.py` and `lh_build_v2.py` cut by exact string / character offsets (asserted); a changed source page breaks the build loudly, not silently.
15. Two globals named `LH` with different contents (Mixer maths vs white-ball maths): they cannot share one page without renaming.
