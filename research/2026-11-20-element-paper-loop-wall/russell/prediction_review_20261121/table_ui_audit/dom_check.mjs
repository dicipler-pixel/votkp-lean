import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const [base, dependency] = process.argv.slice(2);
const {parseHTML} = await import(path.resolve(dependency));
const html = fs.readFileSync(path.join(base,'Periodic_Table_of_Elemental_Peels_v1_20261121.html'),'utf8');
const {document} = parseHTML(html);
const data = JSON.parse(fs.readFileSync(path.join(base,'ptable_data.json'),'utf8'));
const location={hash:''}, events={}, window={};
const context=vm.createContext({document,window,location,console,addEventListener:(id,fn)=>{events[id]=fn;},fetch:async url=>{assert.equal(url,'ptable_data.json');return {json:async()=>data};}});
const script=Array.from(document.querySelectorAll('script')).at(-1);
vm.runInContext(script.textContent,context);
await new Promise(r=>setImmediate(r));
const $=id=>document.getElementById(id);
for(const name of ['standard','signature','cores','disk','stone','colour','octaves','tests','about']){
 location.hash='#'+name;events.hashchange();
 assert.equal(document.querySelectorAll('.view.on').length,1);assert.ok($('v-'+name).classList.contains('on'));
 assert.equal(document.querySelector('#nav [aria-current=page]').getAttribute('href'),location.hash);
}
const tiles=Array.from(document.querySelectorAll('#grid .tile,#grid-f .tile'));assert.equal(tiles.length,85);assert.equal($('classes').querySelectorAll('.tile').length,85);
for(const tile of tiles){
 tile.onclick();const z=Number(tile.dataset.z);assert.ok($('dbody').textContent.includes(data.elements[z-1].name));assert.equal($('drawer').getAttribute('aria-hidden'),'false');$('close').onclick();assert.equal($('drawer').getAttribute('aria-hidden'),'true');
}
const circleCount=$('disksvg').querySelectorAll('circle').length;assert.equal(circleCount,3640);
console.log('Headless DOM runtime, local JSON, no WebGL engine: 9/9 routes; 85 standard + 85 signature tiles; 85/85 drawers open and close; 3,640 disk circles = 5 guides + 3,570 steps + 65 anion rings. No JS exception. The 3D animation, keyboard focus behavior, CSS layout and visuals were not validated.');
