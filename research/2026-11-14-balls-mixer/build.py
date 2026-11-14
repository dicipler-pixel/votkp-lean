# SCRIPT: BALLS-MIXER-BUILD-01  (inline three.js r158, 3D Mixer Parts v1 and the mixer into one standalone HTML)
import sys
v=sys.argv[1]
h='<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Balls on the Field, Mixer '+v+' — Jeromie Beasley</title></head><body>\n'
h+='<script>'+open('three.min.js').read()+'</script>\n<script>'+open('mixer3d_parts_v1.js').read()+'</script>\n<script>'+open('balls_mixer_'+v+'.js').read()+'</script>\n</body></html>'
open('Balls_on_the_Field_Mixer_'+v+'.html','w').write(h); print('built',len(h))
