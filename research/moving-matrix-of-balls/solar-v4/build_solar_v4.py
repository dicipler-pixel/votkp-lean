# SCRIPT: SF-BUILD-V4 — assembles Solar_Field_v4_20261116.html: the Light at the Hypersurface Surprise v1 page as it stands, one added line in its
# app handing its ball to the layer, then the raw data block, SF-HELIO-V4 and SF-LAYER-V4. The source page is not changed.
import json
s = open('../surprise/Light_at_the_Hypersurface_Surprise_v1.html', encoding='utf-8').read()
old = 'window.__LHS={CLOCK,P,UI,S3,'; assert s.count(old) == 1
s = s.replace(old, "window.__TBHOST={S3,WORLD,tau:()=>CLOCK.tau,S:()=>S,P,CLOCK};" + old)
t = '<title>Light at the Hypersurface, Surprise v1'; assert t in s; s = s.replace(t, '<title>Solar Field v4: the heliosphere', 1)
raw = open('sf_raw_data_v4.json', encoding='utf-8').read(); json.loads(raw); assert '</' not in raw
add = '\n<script type="application/json" id="sf_raw_data">' + raw + '</script>\n<script>' + open('sf_helio_v4.js', encoding='utf-8').read() + '</script>\n<script>' + open('sf_layer_v4.js', encoding='utf-8').read() + '</script>\n'
i = s.rfind('</body>'); s = s[:i] + add + s[i:]; open('Solar_Field_v4_20261116.html', 'w', encoding='utf-8').write(s); print('Solar_Field_v4_20261116.html', len(s))
