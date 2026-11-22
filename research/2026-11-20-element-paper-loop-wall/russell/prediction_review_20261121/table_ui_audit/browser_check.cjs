/* node browser_check.cjs PB_TABLE_FOLDER R158_THREE_MIN_JS [chromium_executable] */
const fs=require('fs'),http=require('http'),path=require('path'),{chromium}=require('playwright');
const [base,three,exe]=process.argv.slice(2);
const html='Periodic_Table_of_Elemental_Peels_v1_20261121.html';
(async()=>{
 const server=http.createServer((req,res)=>{
    const name=req.url.split('?')[0].split('/').pop()||html;
    if(![html,'ptable_data.json'].includes(name)){res.writeHead(404).end();return;}
    res.setHeader('Content-Type',name.endsWith('.json')?'application/json':'text/html');
    res.end(fs.readFileSync(path.join(base,name)));
 });
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const addr='http://127.0.0.1:'+server.address().port+'/';
 const browser=await chromium.launch({executablePath:exe||'/usr/bin/chromium',args:['--no-sandbox','--disable-dev-shm-usage','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 try{
 const page=await browser.newPage({viewport:{width:1400,height:950}});
 const errors=[];page.on('pageerror',x=>errors.push(x.message));
 await page.route(/fonts\.g(static|oogleapis)\.com/,r=>r.fulfill({body:'',contentType:'text/css'}));
 await page.route('**/three.min.js',r=>r.fulfill({body:fs.readFileSync(three),contentType:'application/javascript'}));
 await page.goto(addr);await page.waitForSelector('#grid .tile');
 const routes=['standard','signature','cores','disk','stone','colour','octaves','tests','about'];
 for(const id of routes){
   await page.locator('#nav a[href="#'+id+'"]').click();await page.waitForSelector('#v-'+id+'.on');
   const on=await page.locator('.view.on').count();if(on!==1)throw Error('route mismatch '+id);
 }
 console.log('all nine served routes open with a unique selected view');
 await page.locator('#nav a[href="#standard"]').click();
 console.log('standard tiles',await page.locator('#grid .tile,#grid-f .tile').count());
 console.log('signature tiles',await page.locator('#classes .tile').count());
 for(const z of [1,2,8,12,20,38,62,66,69,78,84,85]){
   await page.locator('#v-standard .tile[data-z="'+z+'"]').click();
   await page.waitForSelector('#drawer.on');
   const v=await page.evaluate(()=>({anion:document.querySelector('.signbox>div').innerText.replace(/\s+/g,' '),lines:document.querySelectorAll('#drawer table.steps:last-of-type').length,webGL:!!(document.querySelector('#chain3d').getContext('webgl2')||document.querySelector('#chain3d').getContext('webgl'))}));
   console.log('served detail',z,JSON.stringify(v));
   await page.keyboard.press('Escape');
 }
 console.log('served JavaScript exceptions',JSON.stringify(errors));
 const off=await browser.newPage();
 const fileErrors=[];off.on('pageerror',x=>fileErrors.push(x.message));
 await off.route(/^https?:/,r=>r.abort());
 await off.goto('file://'+path.resolve(base,html));
 await off.waitForTimeout(500);
 console.log('file mode with adjacent JSON, remote requests blocked: tiles',await off.locator('#grid .tile,#grid-f .tile').count(),'JS exceptions',fileErrors);
 }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
})().catch(e=>{console.error(e);process.exit(1)});
