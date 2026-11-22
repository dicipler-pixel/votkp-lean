# SCRIPT: SEA-BUILD-V3 — assembles Balls_in_the_Sea_v3_20261117.html: the Flock of Balls on the Field Mixer v2 page with ONE change (its layer exposes the
# balls' positions and labels, so the sea can move the balls), then the stored rest seas, SEA-MATH-V3 and SEA-LAYER-V3.
import json
s = open('../flock_zip/Flock_of_Balls_on_the_Field_Mixer_v2_20261116.html', encoding='utf-8').read()
t = '<title>Flock of Balls on the Field</title>'; assert s.count(t) == 1; s = s.replace(t, '<title>The Balls in the Sea</title>')
a = 'arrive:() => arrive };'; assert s.count(a) == 1; s = s.replace(a, 'arrive:() => arrive, get pos(){ return pos; }, get labels(){ return labels; } };')
R = json.load(open('rest_seas_03.json')); keep = {k: R[k] for k in ('3|z|sealed', '3|equal|sealed', '3|z|container', '4|z|sealed', '4|equal|sealed', '7|z|sealed', '7|equal|sealed')}; raw = json.dumps(keep); assert '</' not in raw
add = '\n<script type="application/json" id="sea_rest">' + raw + '</script>\n<script>' + open('sea_math_v3.js', encoding='utf-8').read() + '</script>\n<script>' + open('sea_layer_v3.js', encoding='utf-8').read() + '</script>\n'
i = s.rfind('</body>'); s = s[:i] + add + s[i:]; open('Balls_in_the_Sea_v3_20261117.html', 'w', encoding='utf-8').write(s); print('Balls_in_the_Sea_v3_20261117.html', len(s))
