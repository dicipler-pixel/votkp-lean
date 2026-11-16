# SCRIPT: TB-BUILD-V2 — assembles the two Three Balls on the Field v2 pages (one light carried through three balls).
# Each takes a finished Light at the Hypersurface page as it stands, adds one line to its app that hands its ball, its light objects
# and its trace to the field layer, and appends TB-LAYER-V2. The original pages are not changed.
lay = open('tb_layer_v2.js', encoding='utf-8').read(); add = '\n<script>' + lay + '</script>\n'
def one(src, old, new, title_old, title_new, out):
    s = open(src, encoding='utf-8').read(); assert s.count(old) == 1, (src, s.count(old)); s = s.replace(old, new)
    assert s.count(title_old) >= 1, title_old; s = s.replace(title_old, title_new, 1)
    i = s.rfind('</body>'); s = s[:i] + add + s[i:]; open(out, 'w', encoding='utf-8').write(s); print(out, len(s))
one('../lh_build/Light_at_the_Hypersurface_Mixer_v2_20261115.html', 'window.__S3 = S3; }',
    "window.__S3 = S3; window.__TBHOST = { S3, WORLD, tau:() => CLOCK.tau, S:() => S, kind:'mixer', light:[RAYL, RAYP, HITP, STKP, PRSP, RIMP, HYPX, HYPY] }; }",
    '<title>Light at the Hypersurface</title>', '<title>Three Balls on the Field</title>', 'Three_Balls_on_the_Field_Mixer_v2_20261115.html')
one('../surprise/Light_at_the_Hypersurface_Surprise_v1.html', 'window.__LHS={CLOCK,P,UI,S3,',
    "window.__TBHOST={S3,WORLD,tau:()=>CLOCK.tau,S:()=>S,kind:'surprise',tr:()=>TR,light:[rayLines.mesh,rayPts.mesh,sparkPts.mesh,axisPts.mesh,rec]};window.__LHS={CLOCK,P,UI,S3,",
    '<title>Light at the Hypersurface, Surprise v1', '<title>Three Balls on the Field, Surprise', 'Three_Balls_on_the_Field_Surprise_v2_20261115.html')
