# VOTKP mixer and film, v1 (sources)

Jeromie Beasley, 7 November 2026. Companion to *The Volume of the Knot Potential: Decay and Direction on the Vacuum Disk* (v1).

AI-assisted: built with Claude (Anthropic) from the author's ideas, papers, mixer parts kit and narrator.

## mixer/

`VOTKP_Mixer_v1.html` is published as its own file. These are its sources.

- `votkp_mixer.js`: the eleven eyes. Each computes its picture live, from the Bloch–Wigner dilogarithm, the vacuum-disk map, the film reflection formula and the paper's data.
- `mixer3d_parts_v1.js`: the shared 3D Mixer Parts v1 (27 Oct 2026), unchanged.
- `votkp_data.json`: the real data the eyes use. It is exported by `mixer_data_01.py`, from SnapPy, KnotInfo and refractiveindex.info, together with the drawing spectra and torus directions from the research scripts.
- `build.py`: inlines three.js r158, the parts and the data into one standalone HTML.
- `shot.py`: the headless check that opens every eye and takes a screenshot.

## film/

- `narration.py`: the full narration text, one segment per eye.
- `make_voice.py`: Kokoro am_michael at speed 0.92, int8 model.
- `record.py`: live recording of each eye in clean view, with its title and equation shown.
- `compose.py`: the recordings, the narrator (taken from the Two Trees films and screen-blended at bottom right) and the voice, with fades, joined into one MP4.
