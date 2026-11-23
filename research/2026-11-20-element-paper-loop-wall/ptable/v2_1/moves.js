/* where the electron moves (v2.1) */
const MV_SRC='<a href="https://www.nist.gov/pml/atomic-reference-data-electronic-structure-calculations" target="_blank" rel="noopener">NIST ground-state configurations</a>';
const MV_SP966='<a href="https://www.nist.gov/document/periodic-table-2024" target="_blank" rel="noopener">NIST periodic table (SP 966)</a>';
const MOVES={
 Cr:['d','[Ar] 3d⁵ 4s¹','[Ar] 3d⁴ 4s²'],Cu:['d','[Ar] 3d¹⁰ 4s¹','[Ar] 3d⁹ 4s²'],
 Nb:['d','[Kr] 4d⁴ 5s¹','[Kr] 4d³ 5s²'],Mo:['d','[Kr] 4d⁵ 5s¹','[Kr] 4d⁴ 5s²'],Ru:['d','[Kr] 4d⁷ 5s¹','[Kr] 4d⁶ 5s²'],
 Rh:['d','[Kr] 4d⁸ 5s¹','[Kr] 4d⁷ 5s²'],Pd:['d','[Kr] 4d¹⁰','[Kr] 4d⁸ 5s²'],Ag:['d','[Kr] 4d¹⁰ 5s¹','[Kr] 4d⁹ 5s²'],
 Pt:['d','[Xe] 4f¹⁴ 5d⁹ 6s¹','[Xe] 4f¹⁴ 5d⁸ 6s²'],Au:['d','[Xe] 4f¹⁴ 5d¹⁰ 6s¹','[Xe] 4f¹⁴ 5d⁹ 6s²'],
 La:['t','[Xe] 5d¹ 6s²','[Xe] 4f¹ 6s²','4f against 5d'],Ce:['t','[Xe] 4f¹ 5d¹ 6s²','[Xe] 4f² 6s²','4f against 5d'],Gd:['t','[Xe] 4f⁷ 5d¹ 6s²','[Xe] 4f⁸ 6s²','4f against 5d'],
 Ac:['t','[Rn] 6d¹ 7s²','[Rn] 5f¹ 7s²','5f against 6d'],Th:['t','[Rn] 6d² 7s²','[Rn] 5f² 7s²','5f against 6d'],Pa:['t','[Rn] 5f² 6d¹ 7s²','[Rn] 5f³ 7s²','5f against 6d'],
 U:['t','[Rn] 5f³ 6d¹ 7s²','[Rn] 5f⁴ 7s²','5f against 6d'],Np:['t','[Rn] 5f⁴ 6d¹ 7s²','[Rn] 5f⁵ 7s²','5f against 6d'],Cm:['t','[Rn] 5f⁷ 6d¹ 7s²','[Rn] 5f⁸ 7s²','5f against 6d'],
 Lr:['t','[Rn] 5f¹⁴ 7s² 7p¹','[Rn] 5f¹⁴ 6d¹ 7s²','7p against 6d']};
function mvNote(sym){const m=MOVES[sym];if(!m)return '';
  const src=['Np','Cm','Lr'].includes(sym)?MV_SP966:MV_SRC;
  const kind=m[0]==='d'?'In its d row the electron moves to d: the ground state is '+m[1]+' where the filling order alone gives '+m[2]+'.'
    :'On an n + l tie ('+m[3]+') the electron goes to '+(sym==='Lr'?'7p':'d')+': the ground state is '+m[1]+' where filling the f shell first gives '+m[2]+'.';
  const lr=sym==='Lr'?' The 7p ground state is a theoretical assignment, backed by the 2015 measurement of lawrencium’s first ionisation energy (Sato et al., Nature 520, 209).':'';
  return kind+lr+' Source: '+src+'.';}
function drawMoves(){const T=D.moves,svg=$('movessvg');const W=1300,H=150*T.rows.length+60,L=90,R=40;svg.setAttribute('viewBox',`0 0 ${W} ${H}`);
  const all=T.rows.flatMap(r=>r.pts.map(p=>p.z1)),lo=Math.floor(Math.min(...all)*10)/10-0.05,hi=Math.ceil(Math.max(...all)*10)/10+0.05,X=v=>L+(W-L-R)*(v-lo)/(hi-lo);
  for(let v=Math.ceil(lo*10)/10;v<=hi;v+=0.1){const x=X(v);svg.appendChild(el('line',{x1:x,x2:x,y1:20,y2:H-40,stroke:'#121a24'}));axisText(svg,x,H-18,v.toFixed(1),{'text-anchor':'middle'});}
  axisText(svg,(L+W)/2,H-2,'first peel step z₁ = IE₂ / IE₁',{'text-anchor':'middle'});
  T.rows.forEach((r,i)=>{const y=60+150*i;axisText(svg,12,y+4,r.row+' row',{fill:'#e6edf4','font-size':15});
    axisText(svg,12,y+22,`${r.errors} error${r.errors===1?'':'s'}`,{'font-size':12});
    svg.appendChild(el('line',{x1:L,x2:W-R,y1:y,y2:y,stroke:'#1c2633'}));
    const srt=[...r.pts].sort((a,b)=>a.z1-b.z1);
    srt.forEach((p,j)=>{const x=X(p.z1),dy=(j%2?-1:1)*(p.mover?0:0);const c=el('circle',{cx:x,cy:y,r:7,fill:p.mover?'#f2c14e':'none',stroke:p.mover?'#f2c14e':'#63d3ff','stroke-width':1.8,style:'cursor:pointer'});
      c.appendChild(el('title',{},`${p.sym}: z₁ = ${p.z1.toFixed(3)} · ${p.mover?'the electron moves to d':'it stays'}`));c.onclick=()=>openEl(p.Z);svg.appendChild(c);
      axisText(svg,x,y+(j%2?-14:26),p.sym,{'text-anchor':'middle','font-size':12,fill:p.mover?'#f2c14e':'#8fa0b2'});});});
  const pct=v=>(100*v).toFixed(1)+'%';
  $('movescard').innerHTML=`<div class="card"><div class="g">TEST D-MOVERS-PEEL-01 · survives in 3d and 4d, weak in 5d</div><h3>Does the first peel step see the electron move?</h3>
  <p>Kill condition, written before the run: in each d row, one cutoff on z₁ = IE₂/IE₁ must put the movers above the rest, with at most one error per row.</p>
  <p>3d: ${T.rows[0].errors} errors; chromium ${f(T.rows[0].pts.find(p=>p.sym==='Cr').z1,3)} and copper ${f(T.rows[0].pts.find(p=>p.sym==='Cu').z1,3)} are the two highest. 4d: ${T.rows[1].errors} error; technetium ${f(T.rows[1].pts.find(p=>p.sym==='Tc').z1,3)} sits above niobium ${f(T.rows[1].pts.find(p=>p.sym==='Nb').z1,3)}. 5d: ${T.rows[2].errors} error; only gold leads, and platinum ${f(T.rows[2].pts.find(p=>p.sym==='Pt').z1,3)} sits mid-row.</p>
  <p>Chemistry expects this: a mover keeps one s electron (palladium keeps none), so its second removal already comes from d, and that makes the first step bigger.</p>
  <p>Chance baseline, exact by enumeration: a randomly chosen set of the same size in the same row does as well or better in ${T.rows[0].hits} of ${T.rows[0].total} cases for 3d (${pct(T.rows[0].p)}), ${T.rows[1].hits} of ${T.rows[1].total} for 4d (${pct(T.rows[1].p)}) and ${T.rows[2].hits} of ${T.rows[2].total} for 5d (${pct(T.rows[2].p)}). All three rows at once: ${T.joint_frac}. Total errors of ${T.total_obs} or fewer across the three rows: ${T.total_hits} of ${T.total_den.toLocaleString()} (${(100*T.total_hits/T.total_den).toFixed(2)}%).</p></div>`;
  const sec=(t,ids)=>`<div class="cls"><h3>${t} <span class="n">${ids.length}</span></h3><div class="tiles">${ids.map(s=>tile(EL.find(e=>e.sym===s))).join('')}</div></div>`;
  $('movesclasses').innerHTML=sec('The electron moves to d, in its d row',['Cr','Cu','Nb','Mo','Ru','Rh','Pd','Ag','Pt','Au'])+sec('On an n + l tie the electron goes to d (lawrencium: 7p)',['La','Ce','Gd','Ac','Th','Pa','U','Np','Cm','Lr']);
  bindTiles($('movesclasses'));}
{const _oe=openEl;openEl=function(Z){_oe(Z);const e=byZ[Z];if(e&&MOVES[e.sym])$('dbody').insertAdjacentHTML('beforeend',`<div class="sec"><h4>Where the electron moves</h4><p class="note" style="margin:0">${mvNote(e.sym)}</p></div>`);};}
