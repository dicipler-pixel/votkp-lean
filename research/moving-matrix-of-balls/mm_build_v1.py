# SCRIPT: MM-BUILD-V1 — assembles Moving_Matrix_of_Balls_Mixer_v1_20261115.html:
# three.js + mixer3d_parts_v1 verbatim from Balls in One Ball Mixer v2, then MM-MATH-V1 (+MM-REST), the rest states, then MM-MIXER-V1.
import json
ref = open('../lh_build/balls_v2_ref.html', encoding='utf-8').read()
three = ref[201:651869]; kit = ref[651870:670915]
assert three.startswith('<script>') and three.endswith('</script>') and 'SCRIPT: mixer3d_parts_v1' in kit and kit.endswith('</script>')
math = open('mm_math_v1.js', encoding='utf-8').read(); app = open('mm_app_v1.js', encoding='utf-8').read()
rest = json.dumps(json.load(open('rest_states_v1.json')), separators=(',', ':'))
head = ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Moving Matrix of Balls</title></head><body>\n')
out = head + three + '\n' + kit + '\n<script>' + math + '</script>\n<script>window.MM_REST=' + rest + ';</script>\n<script>' + app + '</script>\n</body></html>\n'
name = 'Moving_Matrix_of_Balls_Mixer_v1_20261115.html'
open(name, 'w', encoding='utf-8').write(out); print(name, len(out))
