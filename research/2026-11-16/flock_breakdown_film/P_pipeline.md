# P_pipeline — film pipeline proof (hand P, 16 Nov 2026)

Result: a 15.0 s clip, 1920x1080, 30 fps, H.264 (libx264 -preset veryfast, crf 20) plus AAC, 7.5 MB:
`/home/claude/balls/film/work/p/proof_clip_p.mp4`. I extracted frames at 0.6, 2.4, 3.9, 5.4, 6.5, 8.0, 11.7, 12.9 and 14.5 s and looked at them
(sheets: `film/work/p/look/sheetA.png`, `sheetB.png`). What I saw is listed under "What I looked at". Everything below was run on this machine (2 cores, 7.8 GB).

## (a) Voice: works, nothing needed installing
- `kokoro-onnx 0.6.1`, `onnxruntime 1.29.0`, `soundfile` were already installed; model files were already in `/home/claude/balls/film/models/`
  (`kokoro-v1.0.onnx` 325,532,387 bytes, `voices-v1.0.bin` 28,214,398 bytes). I did not need pip or the proxy.
- Voice am_michael, speed 0.92, lang en-us. Script: `film/work/p/voice_p.py` (copy of `tools/make_voice.py`, also writes per-sentence start/end to `times_p.json` so cues sit on spoken words).
- Command: `python3 -I voice_p.py lines_p.txt narration_p.wav times_p.json`. Time: 15.8 s for 3 sentences (about 2 to 7 s of synthesis per sentence, CPU only); output 13.8 s of audio (0.8 s lead, 0.38 s between lines, 1.2 s tail).
- Lines used (no lives/winds/read-past; "light" and "close" avoided too): "Four balls sit on one field." / "Kick the centre ball, and light sets out across the gaps." / "The light in the balls plus the light in the gaps is always exactly one."
  Sentence times: 0.80-2.89, 3.27-6.90, 7.28-12.21 s. Loudness: mean -21.0 dB, peak -1.1 dB.
- Not heard by me (I cannot listen); only the waveform levels and timings were checked.

## (b) Deterministic capture of the Flock page
- Tool: `film/work/p/capture_p.py` = copy of `film/tools/mixer_capture.py`, changed only to write lossless PNG frames (and an md5 per frame into the clock csv) instead of piping into ffmpeg.
  It replaces `performance.now`, `Date.now` and `requestAnimationFrame` with a virtual clock, steps it by exactly 1/30 s per frame, runs cues (`window.__FL.kick(0)` at 3.4 s), screenshots the page (mode "page", drawer/strip hidden, `MIXER_API.clean`), logs `__FL.books()` each frame.
- Determinism test: the same 1 s spec (30 frames) captured twice: all 30 frame md5s identical between the runs, and all 30 differ from each other (the page really moves). Not tested: determinism of the whole 12.8 s run or across machines.
- Real run: 384 frames, viewport 1220x834 (the kit's panel box), 4 balls, view goTo(-1). Capture 309 s = 0.81 s/frame = 24 min of work per minute of film. PNG frames 108 MB. Log: `page_p_clock.csv`.
  Books check read from the page each frame: total = balls + gaps, max |total - 1| = 4.9e-14 over 384 frames (consistent with fl_check_01 K2, tolerance 1e-12).
- WHAT FAILED, and a bug in the page (not edited; found in the built Mixer page):
  the first full run crashed at frame 294 (film 9.8 s, host_tau exactly 10.0 = 2 x T_LOOP) with
  `TypeError: Cannot read properties of undefined (reading '0')` at `partialSquare` (`Flock_of_Balls_on_the_Field_Mixer_v1_20261116.html:416`), called from `updateLoop` (:669).
  Cause: at tau a hair below a multiple of 5, `f = tau/T_LOOP - floor(tau/T_LOOP + 1e-12)` is a tiny negative number, `q = Math.min(3.999999, f*4)` is negative, `i = floor(q) = -1`, and `st[-1]` is undefined.
  The function is defined in the host source `lh_math_v1.js:185` (clamp on the next line). Smallest repair: `const q = Math.min(3.999999, Math.max(0, f*4))`.
  For the proof I used a patched COPY, `film/work/p/page_patched_copy.html` (one `sed`, 4 diff lines, original untouched). Any film that runs the page past tau = 10 needs this repair in the page or the copy. The coordinator/L-hands should decide whether the repair goes into the source.
- Earlier artefact, unexplained: `film/work/test_canvas.mp4` and `test_page.mp4` have the same md5 although their PNG frames differ. I did not chase it.

## (c) Narrator overlay and clip
- Tool: `film/work/p/compose_p.py`. It imports the kit from the copy `film/work/kit/code` (identical to `gh/narrator-animation-kit/code` apart from `__pycache__`), overwrites the cue lists in memory and uses its own functions (figure, arm, ripple, arc, screen blend). The kit is not edited.
  Command: `python3 compose_p.py narration_p.wav times_p.json pageframes proof_clip_p.mp4` (12.8 s main + 2.2 s credits).
- Cues: arc (eyes shine, strike on ball A) 3.0 s; kick 3.4 s; mirror turn 4.6 s (one); gestures 1.0-3.6 s and 8.8-12.0 s; cane TAP at 11.5 s on "exactly one" (the books-sum result is the one check that holds to 1e-12; taps are for proved/checked results only).
- Layout: page in the kit panel box (50,104)-(1270,938); narrator at the kit position; lower band (50,950)-(1270,1034) with the spoken sentence, dark translucent, light text, auto-shrunk to fit so no word is cropped; screen blend means the figure has no background rectangle.
- Credits card (test): dissolves in over 0.4 s from 12.8 s, holds to 15.0 s. Title, byline "Jeromie Beasley", "AI-assisted" line, DOI line with a PLACEHOLDER (`10.5281/zenodo.XXXXXXX (set at upload)`; I did not invent a DOI). Smallest ink margin to any edge: 326 px (script asserts every line fits in width minus 120 px).
- Timing: compose 166.5 s for 450 frames = 0.37 s/frame (2 cores, numpy/cv2, ffmpeg in a pipe). Total proof effort: voice 16 s + capture 309 s + compose 167 s, about 8.2 min for 15 s of film, so about 33 min of machine time per minute of film at 1220x834 page size. A 5-minute film is about 2.7 hours of machine time. Background jobs here need `nohup ... &` and polling; a foreground call is limited to 10 min.
- Encode: `libx264 -preset veryfast -crf 20 -pix_fmt yuv420p`, AAC 128k, `+faststart`. File 7,476,937 bytes (about 4 Mbit/s). ffprobe: h264 1920x1080 30 fps, duration 15.000 s.
- Measured on all 450 frames: max mean brightness 46/255 (dark ground); max share of pixels above 204/255 in any frame 7.0%. These are the arc/eye flare and the ball glare, not a background; the extracted frames show a black ground everywhere. The white-ball page (`..._White_v1_...html`) was not used.

## What I looked at (frames from the final mp4)
- 0.6 s: hologram being drawn from the feet up (scan line), page panel with 4 balls, no band yet.
- 2.4 s: whole figure, caption "Four balls sit on one field." fully inside the band.
- 3.9 s: eyes flared, lightning arc from the figure strikes ball A on the page, impact ring; caption 2 fits.
- 5.4 s and 8.0 s: mirror turn (figure thin mid-turn, then seen from the back with a bright sheen). The sheen at 8.0 s has a ragged glow edge on the right; that is the kit's own mirror effect, I did not alter it.
- 6.5 s: page after kick, links lit; 11.7 s: cane tap, ring on the floor, hand lowered; caption 3 fits.
- 12.9 s: mid-dissolve not shown; 14.5 s: credits card, centred, nothing cropped, dark ground.
- Not checked: lip/mouth sync by eye (mouth follows loudness in the kit code); the exact frame of the cane strike against the audio.

## Problems and advice for the film
1. The page content is small in the panel (balls fill about a third of its width). For the film, set zoom in the setup (`window.__FL.setZoom(160)` or `goTo(...)`) and capture each shot at the kit's panel size 1220x834. I did not test setZoom in this run.
2. Fix the `partialSquare` clamp (above) before rendering any shot past tau = 10 (about 10 s after start, any "host_tau" multiple of 5).
3. Cost: 0.8 s/frame capture is the bottleneck. Shots can be captured once and reused; compose is independent of capture.
4. The kit's mirror turn lasts 3.8 s and drops the arm gesture; place it in a pause.
5. Captions in the lower band repeat the spoken sentence; if the film should have no text, set `CAPS = []`.

## Files (all under /home/claude/balls/film/work/p/)
`voice_p.py`, `lines_p.txt`, `narration_p.wav`, `times_p.json`, `capture_p.py`, `shot_p.json`, `shot_det.json`, `shot_det2.json`, `page_patched_copy.html`, `pageframes/` (384 PNG, 108 MB, can be deleted), `page_p_clock.csv`, `compose_p.py`, `proof_clip_p.mp4`, `look/`.
