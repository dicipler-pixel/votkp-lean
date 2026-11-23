/* The comparison view uses committed neighbour identities and the mixer's own ionization energies. */
const cmpData = COMPARISON_RESULTS;
const cmpMethodNames = {
  circle:'Circle', diamond:'Diamond', cube:'Cube', simplex:'Triangle family',
  log_ratio:'Euclidean log ratios', log_ie_z:'Standardized log energies',
  mat2vec:'mat2vec', magpie:'Magpie', raw_ie:'Raw energies'
};

function cmpMethodName(key){
  return cmpMethodNames[key] || key.replaceAll('_',' ');
}

function cmpOptions(select, pairs, initial){
  select.replaceChildren();
  for(const [value,label] of pairs) select.add(new Option(label,value));
  if(pairs.some(([value])=>value===initial)) select.value=initial;
}

function cmpRow(table, values, header=false){
  const row=table.insertRow();
  values.forEach((value,i)=>{
    const cell=document.createElement(header || i===0 ? 'th':'td');
    if(header || i===0) cell.scope=header?'col':'row';
    cell.textContent=value;
    row.append(cell);
  });
  return row;
}

function cmpTrace(selected,other){
  const svg=$('cmp-traces'), ns='http://www.w3.org/2000/svg';
  function add(tag,attrs,txt){
    const node=document.createElementNS(ns,tag);
    for(const [k,v] of Object.entries(attrs)) node.setAttribute(k,v);
    if(txt!==undefined) node.textContent=txt;
    svg.append(node); return node;
  }
  function label(x,y,txt,extra={}){
    return add('text',{x,y,fill:'#aabad0','font-size':14,...extra},txt);
  }
  const ratios=e=>e.ie.slice(1,9).map((v,i)=>v/e.ie[i]);
  const first=ratios(selected), second=ratios(other), wall=3+2*Math.sqrt(2);
  const ymax=Math.max(wall,...first,...second)*1.1;
  const x=k=>72+85*k, y=z=>250-190*Math.log(z)/Math.log(ymax);
  svg.replaceChildren();
  add('title',{id:'cmp-trace-title'},selected.name+' and '+other.name+' ratios across the first eight removal steps');
  [1,2,4,8,16,32,64].filter(z=>z<ymax).forEach(z=>{
    add('line',{x1:72,x2:667,y1:y(z),y2:y(z),stroke:'#253543'});
    label(58,y(z)+4,z+'×',{'text-anchor':'end'});
  });
  add('line',{x1:72,x2:667,y1:y(wall),y2:y(wall),stroke:'#f2c14e','stroke-dasharray':'6 5'});
  label(670,y(wall)+4,'wall',{fill:'#f2c14e','font-size':12});
  for(let k=0;k<8;k++) label(x(k),272,String(k+1),{'text-anchor':'middle'});
  label(369,294,'removal step k',{'text-anchor':'middle'});
  function series(z,color,dash,name,keyX){
    const pts=z.map((value,i)=>[x(i),y(value)]);
    add('line',{x1:keyX,x2:keyX+28,y1:25,y2:25,stroke:color,'stroke-width':3,'stroke-dasharray':dash});
    label(keyX+35,30,name,{fill:color});
    add('polyline',{points:pts.map(p=>p.join(',')).join(' '),fill:'none',stroke:color,
      'stroke-width':2.6,'stroke-dasharray':dash,'stroke-linejoin':'round'});
    pts.forEach(([cx,cy],i)=>{
      const node=add('circle',{cx,cy,r:3.5,fill:color});
      const tip=document.createElementNS(ns,'title');tip.textContent=name+' · k = '+(i+1)+' · z = '+z[i].toPrecision(7);
      node.append(tip);
    });
  }
  series(first,'#63d3ff','none',selected.name,72);
  series(second,'#f5a9ce','7 5',other.name,310);
}

function cmpScale(first,second){
  const logSteps=ie=>ie.slice(1,9).map((v,k)=>Math.log(v/ie[k]));
  const x=logSteps(first), y=logSteps(second);
  const u=x.map((v,k)=>Math.log(v/y[k]));
  const lo=Math.min(...u), hi=Math.max(...u);
  return {query:Math.log(first[8]/first[0]),neighbour:Math.log(second[8]/second[0]),
    scale:Math.exp((hi+lo)/2),mismatch:Math.exp((hi-lo)/2)};
}

function cmpDrawTransfer(){
  const table=$('cmp-heavy');
  if(table.rows.length) return;
  const {historical,heavy,experimental_queries,rows}=cmpData.transfer;
  $('cmp-historical').textContent='Each of '+historical.queries+' F–At elements was matched outside its own period. The triangle family recovered '+historical.simplex_hits+' columns and Euclidean log ratios recovered '+historical.log_hits+' (paired sign test p = '+historical.descriptive_sign_p+'). La–Lu and Ac–Lr were excluded.';
  $('cmp-heavy-summary').textContent='Each heavy query searched only the fixed '+heavy.reference_elements+'-element F–At reference panel. The triangle family recovered '+heavy.simplex_hits+' of '+heavy.queries+' columns and Euclidean log ratios recovered '+heavy.log_hits+' (p = '+heavy.descriptive_sign_p+'). Neither panel met the preregistered hurdle for a triangle-family advantage.';
  cmpRow(table,['Element','Column','Query grades','Triangle neighbour','Its grades','Log-ratio neighbour','Its grades'],true);
  for(const r of rows){
    const row=cmpRow(table,[r.symbol,r.column,r.grades,r.simplex+' · '+(r.simplex_hit==='True'?'match':'miss'),
      r.simplex_grades,r.logs+' · '+(r.logs_hit==='True'?'match':'miss'),r.logs_grades]);
    if(r.simplex_hit!==r.logs_hit) row.className='cmp-discordant';
  }
  const {two,attainable,heavy_queries,three,two_matched}=cmpData.transfer.prefix;
  $('cmp-prefix').textContent='Two rungs need three consecutive experimental thresholds. Across '+two.queries+' historical queries, the triangle family found '+two.simplex_hits+' columns and plain log ratios found '+two.log_hits+' (paired sign p = '+two.descriptive_sign_p+'). '+two.no_group.length+' queries had no eligible reference from their column, so at most '+attainable+' could match. Eligible heavy queries: '+heavy_queries+'.';
  $('cmp-prefix-matched').textContent='With the same '+three.queries+' queries and candidate pools, two rungs gave '+two_matched.simplex_hits+' triangle and '+two_matched.log_hits+' plain-log matches. Three rungs gave '+three.simplex_hits+' and '+three.log_hits+', respectively.';
  const g=heavy.query_thresholds;
  $('cmp-grades').textContent='Heavy query thresholds: '+g.E+' experimental, '+g.S+' semiempirical and '+g.T+' theoretical. Heavy queries with nine experimental inputs: '+experimental_queries+' of '+heavy.queries+'.';
}

function drawComparison(){
  const scope=$('cmp-cohort').value, group=$('cmp-label').value, data=cmpData[scope];
  const elementSelect=$('cmp-element'), methodSelect=$('cmp-method');
  if(elementSelect.dataset.cohort!==scope){
    const old=elementSelect.value || 'Fe';
    cmpOptions(elementSelect,data.elements.map(e=>[e.symbol,e.symbol+' · '+byZ[e.Z].name]),old);
    cmpOptions(methodSelect,Object.keys(data.methods).map(key=>[key,cmpMethodName(key)]),methodSelect.value || 'simplex');
    elementSelect.dataset.cohort=scope;
  }
  const i=data.elements.findIndex(e=>e.symbol===elementSelect.value);
  const element=data.elements[i], key=methodSelect.value;
  const lookup=new Map(data.elements.map(e=>[e.symbol,e]));
  const neighbour=lookup.get(data.methods[key].neighbors[i]);
  const selected=byZ[element.Z],other=byZ[neighbour.Z];
  const label=group==='long'?'column':'group';
  const match=element[group]===neighbour[group];
  $('cmp-pair').textContent=selected.name+' and '+other.name;
  $('cmp-match').textContent=cmpMethodName(key)+' · '+element.symbol+' '+label+' '+element[group]+' · '+neighbour.symbol+' '+label+' '+neighbour[group]+' · '+(match?'match':'different labels');
  const frow=scope==='primary'?'La through Lu use the mixer’s displayed columns 3–17.':'La through Lu are excluded from both the query and candidate sets.';
  $('cmp-label-note').textContent=group==='long'?frow:'Short-form labels merge the A/B partners. The three transition triads and the noble gases keep separate labels. '+frow;
  cmpTrace(selected,other);
  const keep=cmpScale(selected.ie,other.ie);
  $('cmp-span').textContent='Total log span T = ln(IE₉ / IE₁): '+selected.sym+' '+keep.query.toFixed(4)+' · '+other.sym+' '+keep.neighbour.toFixed(4)+'.';
  $('cmp-scale').textContent='Multiply '+other.sym+'’s eight log steps by '+keep.scale.toFixed(5)+' to match '+selected.sym+'. The largest multiplicative mismatch remaining on the step logs is '+keep.mismatch.toFixed(5)+'× in either direction.';
  cmpDrawTransfer();
  const score=$('cmp-score');score.replaceChildren();
  cmpRow(score,['Distance rule','Nearest',group==='long'?'Column match':'Group match','Hits / '+data.elements.length],true);
  for(const [method,record] of Object.entries(data.methods)){
    const near=lookup.get(record.neighbors[i]);
    const hits=record.hits[group];
    const row=cmpRow(score,[cmpMethodName(method),near.symbol,element[group]===near[group]?'yes':'no',
      hits+' / '+data.elements.length+' ('+(100*hits/data.elements.length).toFixed(1)+'%)']);
    if(method===key) row.className='cmp-selected';
  }
  const contrasts=$('cmp-contrasts');contrasts.replaceChildren();
  cmpRow(contrasts,['Baseline','Triangle minus baseline','Paired 95%','Deletion 95%','Triangle only','Baseline only'],true);
  const pp=n=>(n>0?'+':'')+(100*n).toFixed(1);
  for(const row of data.comparisons.filter(c=>c.shape==='simplex' && c.label===group))
    cmpRow(contrasts,[cmpMethodName(row.baseline),pp(row.delta),row.paired95.map(pp).join(' to '),row.deletion95.map(pp).join(' to '),row.shape_only,row.baseline_only]);
  const energies=$('cmp-energies');energies.replaceChildren();
  cmpRow(energies,['Removal',selected.sym+' table',selected.sym+' archive',other.sym+' table',other.sym+' archive'],true);
  const archived=(e,k)=>cmpData.archiveDifferences[e.sym]?.[k+1] ?? e.ie[k];
  for(let k=0;k<9;k++) cmpRow(energies,[k+1,selected.ie[k],archived(selected,k),other.ie[k],archived(other,k)]);
}
for(const id of ['cmp-cohort','cmp-label','cmp-element','cmp-method']) $(id).addEventListener('change',drawComparison);
