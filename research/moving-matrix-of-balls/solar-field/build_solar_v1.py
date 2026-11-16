# SCRIPT: SF-BUILD-V1 — assembles Solar_Field_v1_20261115.html: the Light at the Hypersurface Surprise v1 page as it stands,
# one added line in its app handing its ball, light objects, parameters and clock to the field layer, then SF-MATH-V1 and SF-LAYER-V1.
s = open('../surprise/Light_at_the_Hypersurface_Surprise_v1.html', encoding='utf-8').read()
old = 'window.__LHS={CLOCK,P,UI,S3,'; assert s.count(old) == 1
s = s.replace(old, "window.__TBHOST={S3,WORLD,tau:()=>CLOCK.tau,S:()=>S,P,CLOCK,light:[rayLines.mesh,rayPts.mesh,sparkPts.mesh,axisPts.mesh,rec]};" + old)
t = '<title>Light at the Hypersurface, Surprise v1'; assert t in s; s = s.replace(t, '<title>Solar Field', 1)
add = '\n<script>' + open('sf_math_v1.js', encoding='utf-8').read() + '</script>\n<script>' + open('sf_layer_v1.js', encoding='utf-8').read() + '</script>\n'
i = s.rfind('</body>'); s = s[:i] + add + s[i:]; open('Solar_Field_v1_20261115.html', 'w', encoding='utf-8').write(s); print('Solar_Field_v1_20261115.html', len(s))
