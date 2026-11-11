# SCRIPT: PHOTON-MIXER-BUILD
import sys
parts=open('mixer3d_parts_v1.js').read(); core=open('photon_core.js').read(); app=open('photon_app.js').read()
head='''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ballad of a Dead Photon — 3D mixer</title>
<meta name="description" content="3D mixer for the song Ballad of a Dead Photon by Jeromie Beasley: a photon's life from the Sun's core to a leaf, with every number recomputed live, and a closing scene driving out into the sunset.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600&family=Inter+Tight:wght@400;500&family=JetBrains+Mono:wght@400&display=swap">
</head><body>
<script src="https://cdn.jsdelivr.net/npm/three@0.158.0/build/three.min.js"></script>
'''
out=head+'<script>\n'+parts+'\n</script>\n<script>\n'+core+'\n</script>\n<script>\n'+app+'\n</script>\n</body></html>\n'
open(sys.argv[1],'w').write(out); print(len(out))
