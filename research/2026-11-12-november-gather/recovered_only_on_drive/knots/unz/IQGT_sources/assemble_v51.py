# SCRIPT: assemble_iqgt_mixer_v51
import sys, os
out = sys.argv[1]; bodies = sys.argv[2:]
core = open('core_v2.js').read()
iq = open('iqgt_math_v5.js').read().replace("const IQ = (() => {","window.IQ = (() => {").replace("if (typeof module !== 'undefined') module.exports = IQ;","")
iq = iq.replace("const C = (typeof Core !== 'undefined') ? Core : require('./core_v2.js');","const C = window.Core;")
parts = open('parts_v31.js').read()
b = '\n'.join(open(f).read() for f in bodies if os.path.exists(f))
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>IQGT Mixer 3D</title>
<meta name="description" content="Maps Don't Make the Sky: a 3D explorer of the intrinsic quantum geometric tensor on the Grassmannian. Jeromie Beasley.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=STIX+Two+Text:ital,wght@0,400;1,400&display=swap">
<script type="importmap">{{"imports":{{"three":"https://cdn.jsdelivr.net/npm/three@0.158.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.158.0/examples/jsm/"}}}}</script>
</head><body>
<script>
{core}
window.Core = Core;
{iq}
</script>
<script type="module">
{parts}
{b}
{open('iqgt_v51_main.js').read()}
</script>
</body></html>'''
open(out,'w').write(html); print(out, len(html))
