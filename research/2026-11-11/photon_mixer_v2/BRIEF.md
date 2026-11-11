# Ballad of a Dead Photon — 3D mixer v2: scene brief

Owner: Jeromie Beasley (independent researcher). This page is the visual mixer for his song
"Ballad of a Dead Photon": the life of one photon from the Sun's core to its absorption.
Each of the eight song sections gets one 3D scene ("eye"). You are improving specific scenes.

## What he asked for (his words, paraphrased)
- "Good 3D modelling" at the quality of his own films. Frames from them: /home/claude/refs/mono.png,
  /home/claude/refs/p1.png, /home/claude/refs/h.png. LOOK AT THESE FIRST (Read tool shows images).
  They are inspiration for quality, not a template: the song decides what is in each scene.
- NO bar graphs. NO cartoon or generated art (no drawn suns with faces, no cars, no props).
- It is a live web page, not a download.

## The look (from his films)
- Pure black background. Dense additive point clouds (tens of thousands of points) whose positions are
  sampled from a computed field's density, so the shape IS the physics. Depth, volume, slow camera drift.
- Colour means something: phase (hue wheel `hue(phase)`), wavelength (`lamRGB(nm)`), or temperature.
  Say which in the readout.
- Restraint: one hero object per scene, well framed and filling the view, centred, not tiny, not off-screen.
- Thin glowing guide lines (M.line) are fine; small white or cyan text labels (M.label) sparingly.

## Story beat per section (what each scene must show)
1. core — "Born in the core": photon created in the Sun's core, random-walks out for tens of thousands of years.
2. flight — "Eight minutes": free flight Sun to Earth, 499 s on Earth's clock, zero proper time for the photon.
3. snell — "Bent at the glass": refraction, and past the critical angle total internal reflection with an evanescent field.
4. slits — "Both ways": one photon at a time through two slits; the interference field exists before detection; dots build fringes.
5. redshift — "The long commute": wave stretched by cosmic expansion; arrives redder, with less energy.
6. photoelectric — "Paid in full": absorbed by a metal, all its energy to one electron; electron leaves only above threshold.
7. resonance — "Laid to rest": absorption needs resonance; exact hydrogen 1s/2p orbitals, Rabi transfer.
8. sky — "Into the sunset": the low Sun's colour computed from Planck x Rayleigh extinction along the airmass.

## Code layout (photon_mixer = /home/claude/work/photon_mixer)
- mixer3d_parts_v1.js: the shared 3D parts kit (read it for the API: M.points, M.setPt, M.flush, M.line,
  M.setLine, M.trail, M.pushTrail, M.clearTrail, M.label, M.colour.*, M.grid, M.surface, M.orb, M.shell ...).
  DO NOT EDIT IT.
- photon_core.js: window.PHO physics core, tested 14/14 (energyEV, freq, flight, walk, snell, critical,
  evanescentDepth, fresnelR, slitI, fringe, redshift, photoelectric, planck, tauRayleigh, airmass, sunSpectrum,
  T_SUN). DO NOT EDIT IT; compute extras locally in your scene.
- v2/common.js: shared helpers exported as window.PHX (hue, lamRGB, cloud, fill (rejection sampler), LE
  Lane–Emden n=3 solution, MIXER with the feed params). Do not edit; if you need a helper, put it in your scene file.
- v2/scenes/<id>.js: ONE FILE PER SCENE. Edit ONLY the scene files you are assigned.
  Eye fields: id, section, grade, title, eq, text, uses (feed param ids), view [azimuth, elevation, distance, targetY],
  make(G, st), enter(), step(dt, S) returns readout rows [[label, value], ...]. S = feed.build(params) (see common.js).
  Use PHX.S3 for the stage (scene, camera, world) and call PHX.base() in enter().
- Build: `cd /home/claude/work/photon_mixer && python3 v2/build_v2.py <YOUR_OUT>.html`
  Use YOUR OWN output file name (e.g. test_agentA.html), never Ballad_of_a_Dead_Photon_Mixer_3D_v2.html.
- Test: `timeout 400 python3 shot_test_v2.py <YOUR_OUT>.html <eye1,eye2> <yourprefix_>` writes shots/<prefix><eye>.png
  (1280x760, headless swiftshader), prints readouts and page errors. View the PNGs with Read and iterate until
  the frame looks like it belongs in his films. `node --check` your file first.

## Rules
- All on-screen text in plain, correct scientific English (no slang; slang is for the song only).
  Keep `text` to one short paragraph that explains what the viewer sees.
- Every visual is computed from real physics; no decoration that is not a field or a data point.
  Readout numbers must be correct (check them by hand or with a quick node/python calc).
- Never a pass/fail judge.
- Performance: must run smoothly in a browser. Heavy resampling (fill over 50k+ points) at most a few times
  per second or on parameter change (compare S.key), not every frame; animate cheaply in between
  (e.g. phase rotation via colour update, small position updates, world rotation).
- The page has a left control panel ~420 px wide; the hero object should sit in the right ~2/3 of the frame
  (the stage already offsets; just check the screenshot) and fill it well.

## Report back
For each scene: what it now shows, what is computed, numbers you checked, and the final screenshot path.
Note anything you could not get right.
