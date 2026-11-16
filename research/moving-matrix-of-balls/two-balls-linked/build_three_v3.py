# SCRIPT: TB-BUILD-V3 — assembles the two v3 ball pages and the linked page that holds both.
# Each ball page is a finished Light at the Hypersurface page as it stands plus small hand-over lines in its app and TB-LAYER-V3.
# The linked page embeds both ball pages whole and keeps them on one clock, one camera, the same steps and the same kick.
import json
lay = open('tb_layer_v3.js', encoding='utf-8').read(); add = '\n<script>' + lay + '</script>\n'
def page(src, reps, title_old, title_new, out):
    s = open(src, encoding='utf-8').read()
    for old, new in reps: assert s.count(old) == 1, (out, old[:60], s.count(old)); s = s.replace(old, new)
    assert s.count(title_old) >= 1; s = s.replace(title_old, title_new, 1)
    i = s.rfind('</body>'); s = s[:i] + add + s[i:]; open(out, 'w', encoding='utf-8').write(s); print(out, len(s)); return s
mix = page('../lh_build/Light_at_the_Hypersurface_Mixer_v2_20261115.html', [
  ('window.__S3 = S3; }', "window.__S3 = S3; window.__TBHOST = { S3, WORLD, tau:() => CLOCK.tau, S:() => S, kind:'mixer', light:[RAYL, RAYP, HITP, STKP, PRSP, RIMP, HYPX, HYPY], eyes:[E_A,E_B,E_C,E_D,E_E,E_F,E_G,E_H,E_I,E_J], EMPH, WT, cur:() => CUR.id, TSP }; }"),
  # own timing: the moving markers of rays, layers, rotation and rim each run on their own time, advanced from the one clock at their own speed
  ('const tag = updateRays(CLOCK.tau); updateStack(CLOCK.tau);', 'TLstep(); const tag = updateRays(TLS.rays); updateStack(TLS.stack);'),
  ('const lp = updateLoop(CLOCK.tau), rm = updateRim(CLOCK.tau);', 'const lp = updateLoop(TLS.loop), rm = updateRim(TLS.rim);'),
  ('let made = false;', 'let made = false; const TLS = {rays:0,stack:0,loop:0,rim:0}, TSP = {rays:1,stack:1,loop:1,rim:1}; let TLprev = null; function TLstep(){ const dd = TLprev === null ? 0 : CLOCK.tau - TLprev; TLprev = CLOCK.tau; for(const c in TLS){ if(dd < 0 || Math.abs(dd) > 1) TLS[c] = CLOCK.tau; else TLS[c] += dd*TSP[c]; } }'),
  ], '<title>Light at the Hypersurface</title>', '<title>Three Balls on the Field</title>', 'Three_Balls_on_the_Field_Mixer_v3_20261115.html')
sur = page('../surprise/Light_at_the_Hypersurface_Surprise_v1.html', [
  ('window.__LHS={CLOCK,P,UI,S3,', "window.__TBHOST={S3,WORLD,tau:()=>CLOCK.tau,S:()=>S,kind:'surprise',tr:()=>TR,light:[rayLines.mesh,rayPts.mesh,sparkPts.mesh,axisPts.mesh,rec],layers:{faces:faces.map(f=>f.mesh).concat([faceLines.mesh]),crossings:[crossLines.mesh],tree:[treeLines.mesh,nodePts.mesh],rays:[rayLines.mesh,rayPts.mesh,sparkPts.mesh],arms:[axisPts.mesh],loops:[loopLines.mesh,loopPts.mesh],record:[rec],gaps:[hypLines.mesh]}};window.__LHS={CLOCK,P,UI,S3,"),
  ], '<title>Light at the Hypersurface, Surprise v1', '<title>Three Balls on the Field, Surprise', 'Three_Balls_on_the_Field_Surprise_v3_20261115.html')
shell = open('linked_shell_v1.html', encoding='utf-8').read()
esc = lambda t: json.dumps(t).replace('</', '<\\/')
out = shell.replace('/*MIXER_PAGE*/null', esc(mix)).replace('/*WHITE_PAGE*/null', esc(sur))
open('Two_Balls_Linked_v1_20261115.html', 'w', encoding='utf-8').write(out); print('Two_Balls_Linked_v1_20261115.html', len(out))
