# SCRIPT: BUILD-ELEMENT-MIXER-V3
# Assembles the self-contained film mixer: three.js r158, the shared 3D parts, the element data,
# the ladder block data (ladder_data_v2.py), the mixer itself and the song, embedded so the film
# plays in sync offline.  Usage: python3 build_mixer_v2.py THREE_JS SONG_MP3 OUT_HTML
import base64, json, sys
three, mp3, out = sys.argv[1], sys.argv[2], sys.argv[3]
lad = json.load(open('ladder_data_v2.json'))
ladder_js = 'window.LADDER_DATA=' + json.dumps({'ref': lad['ref']}, separators=(',', ':')) + ';'
parts = open('mixer3d_parts_v1.js').read(); data = open('element_data_v1.js').read(); mixer = open('element_mixer_v3.js').read()
audio = base64.b64encode(open(mp3, 'rb').read()).decode()
html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Loop Wall — Element Paper Mixer v3 — Jeromie Beasley</title></head>
<body>
<audio id="song" preload="auto" src="data:audio/mpeg;base64,{audio}"></audio>
<script>{open(three).read()}</script>
<script>{parts}</script>
<script>{data}</script>
<script>{ladder_js}</script>
<script>{mixer}</script>
</body></html>'''
open(out, 'w').write(html); print(out, len(html), 'bytes')
