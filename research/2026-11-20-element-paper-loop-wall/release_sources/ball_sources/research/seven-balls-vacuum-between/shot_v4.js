// SCRIPT: SB-V4-SHOT — load the page, run its full checks, take screenshots
const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1500,height:900}});
const errs=[];p.on('pageerror',e=>errs.push(String(e)));p.on('console',m=>{if(m.type()==='error')errs.push(m.text());});
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(2500);
const r=await p.evaluate(()=>{window.seven.set({z:[3,5,7]});const s=window.seven.seek(12);const c=window.runChecks();return {t:s.t,all:c.all,rows:c.rows.map(x=>(x.pass?'PASS ':'FAIL ')+x.name+' = '+x.val)};});
console.log('errors',errs);console.log('t',r.t,'ALL',r.all);r.rows.forEach(x=>console.log(x));
await p.evaluate(()=>{window.seven.setView(0.8,0.35,7.5);});await p.waitForTimeout(400);
await p.screenshot({path:process.argv[3]+'_a.png'});
await p.evaluate(()=>{document.getElementById('pumpbox').open=true;window.seven.set({look:'glass',cut:true});window.seven.setView(0.78,0.0,5.2,[0.5,0.6,0]);});await p.waitForTimeout(400);
await p.screenshot({path:process.argv[3]+'_b.png'});
const rd=await p.evaluate(()=>document.getElementById('rd3').innerText+'\n'+document.getElementById('pumprd').innerText+'\n'+document.getElementById('books').innerText);console.log(rd);
await b.close();})();
