# SCRIPT: LH-BUILD-V1
# Assembles Light_at_the_Hypersurface_Mixer_v1_20261115.html: three.js and mixer3d_parts_v1 copied verbatim
# from Balls in One Ball Mixer v2, then LH-MATH-V1, then LH-MIXER-V1.
import sys, os
ref = open('balls_v2_ref.html', encoding='utf-8').read()
three = ref[201:651869]; kit = ref[651870:670915]
assert three.startswith('<script>') and three.endswith('</script>') and 'SCRIPT: mixer3d_parts_v1' in kit and kit.endswith('</script>')
math = open('lh_math_v1.js', encoding='utf-8').read(); app = open('lh_app_v1.js', encoding='utf-8').read()
head = ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Light at the Hypersurface</title></head><body>\n')
out = head + three + '\n' + kit + '\n<script>' + math + '</script>\n<script>' + app + '</script>\n</body></html>\n'
name = 'Light_at_the_Hypersurface_Mixer_v1_20261115.html'
open(name, 'w', encoding='utf-8').write(out); print(name, len(out))
