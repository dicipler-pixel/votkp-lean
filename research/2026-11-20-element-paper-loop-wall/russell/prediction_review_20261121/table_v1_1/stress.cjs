/* Sweep all drawers twice to exercise accumulated renderer resources and the narrow viewport. */
const {chromium}=require('playwright'), assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url'),path=require('node:path');
(async()=>{
 const b=await chromium.launch({executablePath:process.env.CHROMIUM,args:['--no-sandbox','--disable-dev-shm-usage','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 try{
  for(const width of [1320,375]){
   const page=await b.newPage({viewport:{width,height:850},reducedMotion:'reduce',offline:true});const errors=[],warnings=[];
   page.on('pageerror',e=>errors.push(e.message));page.on('console',msg=>{if(msg.type()==='warning')warnings.push(msg.text())});
   await page.route(/^https?:/,r=>r.abort());await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);
   await page.waitForSelector('#grid .tile');
   for(let z=1;z<=85;z++){
    await page.locator('#v-standard .tile[data-z="'+z+'"]').click({timeout:9000});
    await page.waitForSelector('#drawer.on');
    const result=await page.evaluate(()=>{const cv=document.querySelector('#chain3d');const gl=cv.getContext('webgl2')||cv.getContext('webgl');const ladder=[...document.querySelectorAll('#drawer h4')].find(h=>h.textContent.toLowerCase().includes('full peel ladder')).parentElement;const rows=ladder.querySelectorAll('table tr').length-1;return {rows,live:!!gl&&!gl.isContextLost(),drawerWidth:document.querySelector('#drawer').getBoundingClientRect().width,cssWidth:cv.clientWidth,bufferWidth:cv.width}});
    assert.equal(result.rows,z);assert(result.live);assert.equal(result.cssWidth,result.bufferWidth);
    await page.keyboard.press('Escape'); await page.waitForSelector('#drawer.on',{state:'hidden'});
   }
   console.log(width,'elements passed',85,'errors',errors.length,'relevant console warning summaries',JSON.stringify([...new Set(warnings.map(w=>w.split('\n')[0]))].map(t=>[t,warnings.filter(w=>w.startsWith(t)).length])));
   assert.deepEqual(errors,[]);await page.close();
  }
 }finally{await b.close()}
})().catch(e=>{console.error(e);process.exit(1)})
