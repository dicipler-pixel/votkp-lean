/* Run with Node and jsdom installed. Reads the standalone as a page with no network access. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {JSDOM,VirtualConsole} = require('jsdom');
const input = path.join(__dirname,'Periodic_Table_of_Elemental_Peels_Codex_Comparison.html');
const resultBytes = fs.readFileSync(path.join(__dirname,'../fair_baseline/results.json'));
const expected = JSON.parse(resultBytes);
const errors = [];
const log = new VirtualConsole();
log.on('jsdomError', error => errors.push(String(error)));
(async function verify(){
  const dom = new JSDOM(fs.readFileSync(input,'utf8'),{
    url:'https://local.invalid/#neighbours',runScripts:'dangerously',virtualConsole:log,
    pretendToBeVisual:true
  });
  const win=dom.window, doc=win.document;
  await new Promise(resolve=>win.setTimeout(resolve,120));
  const $=id=>doc.getElementById(id);
  const set=(id,value)=>{const el=$(id);el.value=value;el.dispatchEvent(new win.Event('change'));};
  const byId=id=>Array.from($(id).options,o=>o.value);
  try{
    assert.deepEqual(errors,[]);
    assert.equal(doc.querySelectorAll('#nav a').length,18);
    for(const link of doc.querySelectorAll('#nav a')) assert.ok($('v-'+link.hash.slice(1)));
    assert.ok($('v-neighbours').classList.contains('on'));
    assert.equal($('v-neighbours').dataset.resultsSha256,crypto.createHash('sha256').update(resultBytes).digest('hex'));
    const transfer=JSON.parse(fs.readFileSync(path.join(__dirname,'../reference_transfer/results.json')));
    assert.equal($('cmp-heavy').rows.length,1+transfer.heavy.queries);
    assert.deepEqual(Array.from($('cmp-heavy').querySelectorAll('.cmp-discordant'),r=>r.cells[0].textContent),['Rf','Db','Sg']);
    assert.match($('cmp-historical').textContent,/recovered 58 columns.*recovered 56/);
    assert.match($('cmp-grades').textContent,/4 experimental, 24 semiempirical and 44 theoretical/);
    const ies=xs=>xs.reduce((array,x)=>[...array,array[array.length-1]*Math.exp(x)],[1]);
    const query=ies([2,8,4,4,4,4,4,4]), ref=ies(Array(8).fill(1));
    const keep=win.cmpScale(query,ref), rev=win.cmpScale(ref,query), same=win.cmpScale(query,query);
    const close=(v,w)=>assert.ok(Math.abs(v-w)<1e-11,v+' versus '+w);
    close(keep.query,34);close(keep.neighbour,8);close(keep.scale,4);close(keep.mismatch,2);
    close(rev.scale,0.25);close(rev.mismatch,2);close(same.scale,1);close(same.mismatch,1);
    let displayed=0;
    for(const cohort of ['primary','without_lanthanides']){
      const {methods,elements,comparisons}=expected[cohort];
      set('cmp-cohort',cohort);
      assert.deepEqual(byId('cmp-element'),elements.map(e=>e.symbol));
      assert.deepEqual(byId('cmp-method'),Object.keys(methods));
      for(const label of ['long','short']){
        set('cmp-label',label);
        for(const symbol of ['F','Fe','At']){
          set('cmp-element',symbol);
          const i=elements.findIndex(e=>e.symbol===symbol);
          for(const [key,m] of Object.entries(methods)){
            set('cmp-method',key);
            const row=$('cmp-score').querySelector('.cmp-selected');
            assert.equal(row.cells[1].textContent,m.neighbors[i]);
            assert.ok(row.cells[3].textContent.startsWith(m.hits[label]+' / '+elements.length+' '));
            assert.equal($('cmp-energies').rows.length,10);
            assert.ok($('cmp-span').textContent.includes(symbol+' '));
            assert.ok($('cmp-scale').textContent.startsWith('Multiply '+m.neighbors[i]+'’s eight'));
            assert.equal($('cmp-traces').querySelectorAll('circle').length,16);
            assert.equal($('cmp-contrasts').rows.length,1+comparisons.filter(q=>q.label===label&&q.shape==='simplex').length);
            displayed++;
          }
        }
      }
    }
    win.location.hash='standard';
    await new Promise(resolve=>win.setTimeout(resolve,10));
    assert.ok($('v-standard').classList.contains('on'));
    assert.ok($('grid').querySelectorAll('.tile').length>50);
    win.location.hash='neighbours';
    await new Promise(resolve=>win.setTimeout(resolve,10));
    assert.ok($('v-neighbours').classList.contains('on'));
    assert.deepEqual(errors,[]);
    console.log('PASS: transfer tests, reciprocal and self-pair scale controls; all 18 routes map to sections; direct entry and return route; '+displayed+' comparison selections; file-bound results hash; no script errors.');
  } finally {win.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
