# SCRIPT: MIXER-BUILD-01  (inline three.js r158, the 3D Mixer Parts v1 and the data into one standalone HTML)
s=open('votkp_mixer.js').read()
h='<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VOTKP Mixer v1 — Jeromie Beasley</title></head><body>\n'
h+='<script>'+open('three.min.js').read()+'</script>\n<script>'+open('mixer3d_parts_v1.js').read()+'</script>\n'
h+='<script>window.VOTKP_DATA='+open('votkp_data.json').read()+';</script>\n<script>'+s+'</script>\n</body></html>'
open('VOTKP_Mixer_v1.html','w').write(h); print('built',len(h))
