# SCRIPT: SR-MK-V1 — inserts the series layer into a copy of the Surprise app and shell (originals untouched)
L=open('src/sr_layer_v1.js').read(); a=open('src/lh_app.js').read(); s=open('src/shell.html').read()
def rep(t,o,n):
    assert t.count(o)==1, o[:60]; return t.replace(o,n)
a=rep(a,'/* ---------- readouts ---------- */', L+'\n/* ---------- readouts ---------- */')
a=rep(a,"  hypLines.commit();frameN++;\n}","  hypLines.commit();frameN++;\n  xFrame(dt,S);\n}")
a=rep(a,"  $('o_tau').textContent=fmt(CLOCK.tau,2);","  $('xr').innerHTML=xRows();\n  $('o_tau').textContent=fmt(CLOCK.tau,2);")
binds="""document.querySelectorAll('button[data-xl]').forEach(b=>b.addEventListener('click',()=>{SX.level=+b.dataset.xl;document.querySelectorAll('button[data-xl]').forEach(q=>q.setAttribute('aria-pressed',q===b));xBuild();$('x_eigbtn').style.display=SX.level===3?'':'none';}));
$('x_on').addEventListener('click',()=>{SX.on=!SX.on;$('x_on').setAttribute('aria-pressed',SX.on);$('x_on').textContent='Series: '+(SX.on?'shown':'hidden');});
$('x_photon').addEventListener('click',()=>xPhoton());
$('x_restart').addEventListener('click',()=>xBuild());
$('x_sea').addEventListener('click',()=>{SX.seaBack=!SX.seaBack;$('x_sea').textContent='Sea pushes back: '+(SX.seaBack?'yes':'no');xBuild();});
$('x_mode').addEventListener('click',()=>{SX.mode=SX.mode==='move'?'mode':'move';$('x_mode').textContent=SX.mode==='move'?'Showing: where the light is':'Showing: eigenvector (colour = phase)';});
$('x_n').addEventListener('input',e=>{SX.n=+e.target.value;$('o_xn').textContent=SX.n;});
$('x_into').addEventListener('click',()=>xIntoMode());
$('x_eigbtn').addEventListener('click',()=>{$('x_eigbtn').textContent='Computing…';setTimeout(()=>{xModes();$('x_eigbtn').textContent='Eigenvectors ready';},30);});
"""
a=rep(a,"/* ---------- the one clock ---------- */",binds+"/* ---------- the one clock ---------- */")
a=rep(a,"get state(){return{S,TR,STK,PAIRS,LOOPS,TH};}","get state(){return{S,TR,STK,PAIRS,LOOPS,TH,XW,XS,XEN,XE0,XIN,XAL,XAS,SX};},xBuild,xPhoton,xModes,xIntoMode,SX,xrows:()=>xRows()")
a=rep(a,"Light at the Hypersurface, Surprise v1.","The Series of the Ball (v1; built on Light at the Hypersurface, Surprise v1).")
s=rep(s,'<h1>Light at the Hypersurface</h1>','<h1>The Series of the Ball</h1>')
s=rep(s,'Jeromie Beasley · v1 · 15 Nov 2026 · AI-assisted','Jeromie Beasley · v1 · the moving matrix on the ball ends · 15 Nov 2026 · AI-assisted')
s=s.replace('<title>Light at the Hypersurface, Surprise v1 — Jeromie Beasley','<title>Series of the Ball — Jeromie Beasley')
sec='''  <div class="sec">The series of the ball</div>
  <p class="what" style="font-size:11.5px;margin:4px 0">Each face of the ball is the end of a ball: a sphere meeting the rim at right angles, whose end comes in. The generators carry every end into the next, so inside each end sit five smaller ends of the same kind, and inside each of those five more: 6, then 36, then 186 ends. They cross below the wall (z &lt; 3 + 2√2), kiss at it, and stand apart above it. The moving matrix lives on the ends: a photon kicked into one end goes on to the next through the cells they bound, the electron sea moves under the same matrix, and each end’s field turns, passing on all it takes. The bright lines trace all the light that has gone between ends. In eigenvector view each end is lit by the weight of one eigenvector of the matrix and coloured by its phase, turning at its own energy.</p>
  <div class="row"><button data-xl="1" aria-pressed="false">6 ends</button><button data-xl="2" aria-pressed="true">36 ends</button><button data-xl="3" aria-pressed="false">186 ends</button><button id="x_on" aria-pressed="true">Series: shown</button></div>
  <div class="row"><button id="x_photon">Kick in a photon</button><button id="x_sea">Sea pushes back: yes</button><button id="x_restart">Restart from rest</button></div>
  <div class="row"><button id="x_mode">Showing: where the light is</button><button id="x_into">Put the light in this eigenvector</button><button id="x_eigbtn" style="display:none">Compute eigenvectors (a few seconds)</button></div>
  <div class="ctl"><label>Eigenvector <output id="o_xn">0</output><input id="x_n" type="range" min="0" max="71" step="1" value="0"></label></div>
  <div id="xr"></div>
  <div class="sec">Laws, live</div>'''
s=rep(s,'  <div class="sec">Laws, live</div>',sec)
open('src/app_series.js','w').write(a); open('src/shell_series.html','w').write(s); print('ok')
