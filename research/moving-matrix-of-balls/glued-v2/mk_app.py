# SCRIPT: MM-GLUE-MKAPP-V2 — inserts the matrix layer into a copy of the Surprise app (the original is left untouched)
L=open('src/mm_layer_v1.js').read(); a=open('src/lh_app.js').read()
a=a.replace('/* ---------- readouts ---------- */', L+'\n/* ---------- readouts ---------- */')
a=a.replace("  hypLines.commit();frameN++;\n}","  hypLines.commit();frameN++;\n  mFrame(dt,S);\n}")
a=a.replace("  $('o_tau').textContent=fmt(CLOCK.tau,2);","  $('mm').innerHTML=mRows();\n  $('o_tau').textContent=fmt(CLOCK.tau,2);")
binds="""$('m_on').addEventListener('click',()=>{MX.on=!MX.on;$('m_on').setAttribute('aria-pressed',MX.on);$('m_on').textContent='Moving matrix: '+(MX.on?'running':'hidden');});
$('m_photon').addEventListener('click',()=>mPhoton());
$('m_restart').addEventListener('click',()=>mBuild());
$('m_sea').addEventListener('click',()=>{MX.seaBack=!MX.seaBack;$('m_sea').textContent='Sea pushes back: '+(MX.seaBack?'yes':'no');mBuild();});
"""
a=a.replace("/* ---------- the one clock ---------- */",binds+"/* ---------- the one clock ---------- */")
a=a.replace("get state(){return{S,TR,STK,PAIRS,LOOPS,TH};}","get state(){return{S,TR,STK,PAIRS,LOOPS,TH,MW,MS,MEN,ME0,MIN,MAL,MAS,MNN};},mBuild,mPhoton,MX,mrows:()=>mRows()")
a=a.replace("Light at the Hypersurface, Surprise v1.","The Moving Matrix of Balls, glued at the hypersurface (v2; built on Light at the Hypersurface, Surprise v1).")
for k in ['mFrame(dt,S)','mRows()','m_photon','MW,MS,MEN']: assert k in a, k
open('src/app_v2.js','w').write(a); print('ok')
