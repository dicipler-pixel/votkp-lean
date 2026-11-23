# SCRIPT: PERIODIC-TABLE-OF-PEELS-HTML-V2
# Assembles the v2 page from the v1.1 page (read only, never written) plus ptable_v2_data.json,
# add_views.js and openel_v2.js. Every replacement is asserted to hit exactly once.
import json, re, sys
SRC = '/mnt/user-data/uploads/0de192e0-Periodic_Table_of_Elemental_Peels_v1_1_Jeromie_Beasley__1__1_.html'
s = open(SRC).read()
data = open('ptable_v2_data.json').read()
add = open('add_views.js').read(); oel = open('openel_v2.js').read()
def rep(old, new, cnt=1):
    global s
    n = s.count(old)
    assert n == cnt, (n, old[:80])
    s = s.replace(old, new)
# head
rep('<title>Periodic Table of Elemental Peels — Codex review v1.1 · Jeromie Beasley</title>', '<title>Periodic Table of Elemental Peels v2 · Jeromie Beasley</title>')
i = s.index('<div class="by">Jeromie Beasley · hydrogen to astatine'); j = s.index('</div>', i) + 6
s = s[:i] + '<div class="by">Jeromie Beasley · hydrogen to darmstadtium · v2, 22 November 2026</div>' + s[j:]
rep('ul{', 'ul{') if 'ul{' in s else None
css = ('.tile.heavy{border-style:dashed}.tile.nodata{opacity:.4;cursor:default}.tile.nodata .s{color:var(--faint)}'
       '#spiral3d{width:100%;height:640px;display:block;border:1px solid var(--edge);border-radius:8px;background:#000;cursor:grab}'
       '.ctl{display:flex;gap:10px;align-items:center;margin:0 0 10px;font-size:13px;color:var(--dim)}.ctl select{background:#0d141d;color:var(--ink);border:1px solid var(--edge);border-radius:6px;padding:5px 8px;font:13px var(--body)}'
       'table.steps td,table.steps th{white-space:nowrap}\n')
rep('@media (max-width:900px)', css + '@media (max-width:900px)')
i = s.index('<p class="by"><a href="https://github.com/dicipler-pixel/votkp-lean/blob/dfff861'); j = s.index('</p>', i) + 4
s = s[:i] + ('<p class="by"><a href="https://github.com/dicipler-pixel/votkp-lean/blob/element-paper/loop-wall/research/2026-11-20-element-paper-loop-wall/manuscript/v1_2_2/What_the_Peel_Keeps_v1_2_2_Jeromie_Beasley.pdf">What the Peel Keeps, v1.2.2</a> · '
             '<a href="https://zenodo.org/records/24432624">table v1.1 on Zenodo</a> · source and data on the <a href="https://github.com/dicipler-pixel/votkp-lean/tree/element-paper/loop-wall/research/2026-11-20-element-paper-loop-wall/ptable/v2">element-paper/loop-wall branch</a></p>') + s[j:]
rep('and every one is the first opening of a core.</p>',
    'and every one is the first opening of a core. The same archive carries the ladders on from radon to darmstadtium; they are drawn here as a separate extension, mostly theoretical, and none of their steps is counted in the 3,570.</p>')
rep('<a href="#tests">Tests and predictions</a>',
    '<a href="#spiral">Spiral</a><a href="#heavy">Radon onward</a><a href="#decay">Decay</a><a href="#window">The window</a><a href="#faces">Two faces</a><a href="#corpus">The work behind it</a><a href="#tests">Tests and predictions</a>')
rep('<div class="rowlabel">lanthanides, cerium to lutetium</div><div class="grid" id="grid-f"></div></section>',
    '<div class="rowlabel">lanthanides, cerium to lutetium</div><div class="grid" id="grid-f"></div><div class="rowlabel">actinides, thorium to lawrencium (archive ladders, dashed: heavy-element extension)</div><div class="grid" id="grid-a"></div></section>')
newsec = '''
<section class="view" id="v-spiral"><p class="note">The elements on one spiral, after Russell's spiral: one turn per period, each element at its place in the period, and its distance from the axis set by a reflection of its own chain. The translucent gold cylinder is the wall, radius 1/√2. Drag to turn, scroll to zoom, click an element to open it. This is a way of drawing the same numbers, not a claim about Russell's own chart.</p>
<div class="ctl"><label for="spiralmode">radius</label><select id="spiralmode"><option value="anion">anion rung Γ₀</option><option value="core">first core opening Γ</option><option value="strongest">strongest step Γ</option></select><span id="spiralnote"></span></div><canvas id="spiral3d" aria-label="3D spiral of the elements; drag to turn"></canvas></section>
<section class="view" id="v-heavy"><p class="note" id="heavynote"></p><figure><svg class="chart" id="heavysvg" viewBox="0 0 1300 560" role="img" aria-label="Step ratios from radon to darmstadtium"></svg></figure></section>
<section class="view" id="v-decay"><p class="note">Strip the same number of electrons from two isobars and their ground-mass gap moves by the difference of their removal energies: Q(q + 1) − Q(q) = I<sub>H</sub> − I<sub>L</sub>. Starting from each measured neutral gap and adding the archived thresholds one charge at a time gives the curves below. Above zero the first atom is heavier and decays toward the second; below zero the direction reverses. The bare ends agree with the storage-ring decays of bare rhenium-187 and bare dysprosium-163 and with the lead–thallium reversal.</p><div id="decaybox"></div></section>
<section class="view" id="v-window"><p class="note" id="windownote"></p><figure><svg class="chart" id="windowsvg" viewBox="0 0 1300 420" role="img" aria-label="The cutoff window around the wall"></svg></figure></section>
<section class="view" id="v-faces"><p class="note" id="facenote"></p><figure><svg class="chart" id="facesvg" viewBox="0 0 640 640" style="max-width:640px" role="img" aria-label="Two-face plane"></svg></figure></section>
<section class="view" id="v-corpus"><p class="note">The papers this table stands on, and where each one touches it. Links go to public records only.</p><div class="cards" id="corpus"></div></section>
'''
rep('<section class="view" id="v-tests">', newsec + '<section class="view" id="v-tests">')
# data
i = s.index('const d={"wall"'); dec = json.JSONDecoder(); _, end = dec.raw_decode(s[i+8:])
s = s[:i+8] + data + s[i+8+end:]
# spark, tile
i = s.index('function spark(e){'); j = s.index('function tile(e)')
s = s[:i] + '''function spark(e){
  const ie=e.ie, n=ie.length;if(n<2)return '<svg viewBox="0 0 100 48" aria-hidden="true"></svg>';
  const qs=e.q||ie.map((_,i)=>i),sk={};e.steps.forEach(s=>sk[s.k]=s);const lo=Math.log(ie[0]), hi=Math.log(Math.max(...ie)), sp=Math.max(hi-lo,1e-6);
  const X=i=>4+92*i/(n-1), Y=v=>44-38*(Math.log(v)-lo)/sp;
  let s=`<svg viewBox="0 0 100 48" preserveAspectRatio="none" aria-hidden="true">`;
  for(let k=0;k<n-1;k++){const st=sk[qs[k]+1];const gap=qs[k+1]!==qs[k]+1;s+=`<line x1="${X(k)}" y1="${Y(ie[k])}" x2="${X(k+1)}" y2="${Y(ie[k+1])}" stroke="${gap?'#2a3644':(st&&st.out?'#f2c14e':'#4f88a8')}" stroke-width="${st&&st.out?3:1.3}" ${gap?'stroke-dasharray="2 2"':''} vector-effect="non-scaling-stroke"/>`;}
  return s+'</svg>';
}
''' + s[j:]
rep('function tile(e){const [a,c]=e.sig;return `<div class="tile c-${a}${c}" tabindex="0"',
    'function tile(e){const [a,c]=e.sig;return `<div class="tile c-${a}${c}${e.heavy?\' heavy\':\'\'}${e.ie.length?\'\':\' nodata\'}" tabindex="0"')
rep('for(let p=1;p<=6;p++)', 'for(let p=1;p<=7;p++)')
rep("$('grid-f').innerHTML=Array.from({length:18},(_,i)=>{const e=EL.find(x=>x.period===8&&x.col===i+1);return e?tile(e):'<div></div>';}).join('');",
    "$('grid-f').innerHTML=Array.from({length:18},(_,i)=>{const e=EL.find(x=>x.period===8&&x.col===i+1);return e?tile(e):'<div></div>';}).join('');\n  $('grid-a').innerHTML=Array.from({length:18},(_,i)=>{const e=EL.find(x=>x.period===9&&x.col===i+1);return e?tile(e):'<div></div>';}).join('');")
rep("const L=EL.filter(e=>e.sig[0]===a&&e.sig[1]===c);", "const L=EL.filter(e=>!e.heavy&&e.sig[0]===a&&e.sig[1]===c);")
rep("drawCores();drawDisk();drawStone();drawColour();drawOct();cards();", "drawCores();drawDisk();drawStone();drawColour();drawOct();cards();drawHeavy();drawDecay();drawWindow();drawFaces();corpus();")
rep("const pts=EL.flatMap(e=>e.cores", "const pts=EL.filter(e=>!e.heavy).flatMap(e=>e.cores")
rep("EL.forEach(e=>{e.steps.forEach((s,k)=>{const G=Math.sqrt(s.g2)", "EL.filter(e=>!e.heavy).forEach(e=>{e.steps.forEach((s,k)=>{const G=Math.sqrt(s.g2)")
# cards: add to C1 and A
rep("$('cards').innerHTML=C1.map(", '''C1.push(
   ["DERIVED · archive, separate count","Radon onward","Radon to darmstadtium add "+EL.filter(e=>e.heavy).reduce((a,e)=>a+e.steps.length,0).toLocaleString()+" adjacent steps from the same archive; "+EL.filter(e=>e.heavy).reduce((a,e)=>a+e.outside,0)+" lie outside the wall. Francium's radon-core opening, from the semiempirical IE₂ [22.4] eV, is z = "+f(byZ[87].cores.find(c=>c.core==='radon').z,4)+", inside, with an uncertainty of ±1.9 eV that reaches the wall. Most energies here are theoretical and the steps stay out of the 3,570."],
   ["DERIVED · three measured anchors","Decay direction follows the ladder","Holmium-163 and dysprosium-163 swap ground-mass order between 56+ and 57+; lead-205 and thallium-205 between 79+ and 80+; rhenium-187 stays heavier than osmium-187 at every charge, and its bare-ion gap comes to "+f(D.decay[1].Q[D.decay[1].Q.length-1]/1000,2)+" keV against the evaluated 72.97 keV for bare rhenium's bound-state decay."],
   ["PREREGISTERED · pending","Does the anion side predict chemistry?","ANION-SIDE-CHEMISTRY-01, committed before any data on 22 November 2026 (7065cb3): do the 12 inside elements form lone single-atom anions in solids with an alkali metal more often than the 53 outside ones? Pass at a gap of 0.40 or more with p < 0.01; kill under 0.20. Not yet scored."],
   ["DERIVED · rule from VOTKP v3.3 §27","A visible ground-state line","First ionisation energy below 6.82 eV, calibrated on hydrogen to aluminium, with area 0.946 under the curve on silicon onward, marks atoms with a visible ground-state line. Each drawer states the side. It is an isolated-atom spectral property, separate from the colour line."]);
  $('cards').innerHTML=C1.map(''')
rep("$('about').innerHTML=A.map(", '''A.unshift(['This edition','v2, 22 November 2026. It keeps every view of v1.1 and adds the spiral, radon onward, decay, the window, the two-face plane and the papers behind the table, plus energy grades, uncertainties and five more readings on every step in each drawer: face apex, loop angle, obliqueness, log-det ledger and the one-electron 1s reading. Earlier editions: v1 (21 November) and v1.1 (Zenodo record 24432624). Builders: build_ptable_v2_data.py and build_ptable_v2_html.py on the branch.']);
  $('about').innerHTML=A.map(''')
rep('All nine views retain Claude’s v1 baseline','All the anion views keep the v1 baseline')
# drawer
i = s.index('function openEl(Z){'); j = s.index("$('close').onclick=")
s = s[:i] + oel + s[j:]
rep("e.steps.forEach((s,k)=>{const A=P[k],B=P[k+1]", "e.steps.forEach((s,k0)=>{const k=e.q?e.q.indexOf(s.k-1):s.k-1;const A=P[k],B=P[k+1]")
# routing
rep("const VIEWS=['standard','signature','cores','disk','stone','colour','octaves','tests','about'];",
    "const VIEWS=['standard','signature','cores','disk','stone','colour','octaves','spiral','heavy','decay','window','faces','corpus','tests','about'];")
rep("document.querySelectorAll('#nav a').forEach(a=>a.setAttribute('aria-current',a.getAttribute('href')==='#'+v?'page':'false'));}",
    "document.querySelectorAll('#nav a').forEach(a=>a.setAttribute('aria-current',a.getAttribute('href')==='#'+v?'page':'false'));if(v==='spiral')drawSpiral();else if(S3){S3.stop();S3=null;}}\n$('spiralmode').onchange=drawSpiral;")
# append new functions before routing block
rep('/* hash routing */', add + '\n/* hash routing */')
# no stale credits left
for bad in ['Codex review', 'Claude’s standalone', "Claude’s v1 baseline"]:
    if bad in s: print('NOTE still contains:', bad, s.count(bad))
open('Periodic_Table_of_Elemental_Peels_v2_Jeromie_Beasley.html', 'w').write(s)
print('written', len(s))
