# SCRIPT: PHOTON-MIXER-BUILD-V2
# usage: python3 v2/build_v2.py OUT.html  (run from photon_mixer/). Concatenates parts kit, PHO core, v2 common, scenes in film order, run.
import sys, os
D=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(D)
ORDER=['core','flight','snell','slits','redshift','photoelectric','resonance','sky']
rd=lambda p: open(p).read()
head='''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ballad of a Dead Photon — 3D mixer</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600&family=Inter+Tight:wght@400;500&family=JetBrains+Mono:wght@400&display=swap">
</head><body>
<script src="https://cdn.jsdelivr.net/npm/three@0.158.0/build/three.min.js"></script>
'''
js=[rd(R+'/mixer3d_parts_v1.js'), rd(R+'/photon_core.js'), rd(D+'/common.js')]+[rd(f'{D}/scenes/{e}.js') for e in ORDER]+[rd(D+'/run.js')]
out=head+''.join('<script>\n'+j+'\n</script>\n' for j in js)+'</body></html>\n'
open(sys.argv[1],'w').write(out); print(len(out))
