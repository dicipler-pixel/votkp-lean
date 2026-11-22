/* node browser_check.cjs /path/to/standalone.html ; CHROMIUM selects an executable. */
const assert=require('node:assert/strict'), fs=require('node:fs'), path=require('node:path');
const {createHash}=require('node:crypto'),{pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
async function main(){
 const source=path.resolve(process.argv[2]), bytes=fs.readFileSync(source);
 console.log('HTML SHA256',createHash('sha256').update(bytes).digest('hex'));
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM,args:['--no-sandbox','--disable-dev-shm-usage','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--disable-background-networking']});
 try {
  const ctx=await browser.newContext({viewport:{width:1320,height:900},reducedMotion:'reduce',offline:true});
  const page=await ctx.newPage();const errors=[],external=[];
  page.on('pageerror',err=>errors.push(err.message));
  await page.route(/^https?:/,route=>{external.push(route.request().url());return route.abort()});
  await page.goto(pathToFileURL(source).href);
  await page.waitForSelector('#grid .tile');
  const routes=['standard','signature','cores','disk','stone','colour','octaves','tests','about'];
  for(const route of routes){
   await page.locator('#nav a[href="#'+route+'"]').click();
   await page.waitForSelector('#v-'+route+'.on');
   assert.equal(await page.locator('.view.on').count(),1);
  }
  console.log('Chrome',browser.version(),'verified views',routes.length);
  await page.locator('#nav a[href="#standard"]').click();
  assert.equal(await page.locator('#v-standard .tile[data-z]').count(),85);
  console.log('standard table elements',85);
  const notes=[];
  for(const z of [1,2,8,12,20,38,56,62,66,69,84,85]){
   await page.locator('#v-standard .tile[data-z="'+z+'"]').click();
   await page.waitForSelector('#drawer.on');
   const state=await page.evaluate(()=>({label:document.querySelector('.signbox div').innerText.replace(/\s+/g,' '),rows:document.querySelector('.sec table.steps:last-of-type')!=null,webgl:!!(document.querySelector('#chain3d').getContext('webgl2')||document.querySelector('#chain3d').getContext('webgl'))}));
   assert(state.rows && state.webgl);notes.push([z,state.label]);
   if(z===38){
    const cv=page.locator('#chain3d');const box=await cv.boundingBox();assert(box.width>100&&box.height>100);
    const red=await page.evaluate(()=>matchMedia('(prefers-reduced-motion: reduce)').matches);assert(red);
    const before=await cv.screenshot();const x=box.x+box.width/2,y=box.y+box.height/2;
    await page.mouse.move(x,y);await page.mouse.down();await page.mouse.move(x+66,y+31,{steps:6});await page.mouse.up();
    await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
    const after=await cv.screenshot();assert(!before.equals(after));
    // Screenshots exclude all non-canvas HTML. The stable frame is checked after the pointer move.
    assert(after.equals(await cv.screenshot()));
    console.log('Sr WebGL canvas',box.width,'x',box.height,'PNG bytes before/after',before.length,after.length,'drag changes image; remains stable after release');
    if(process.env.CANVAS_PNG)fs.writeFileSync(process.env.CANVAS_PNG,after);
   }
   await page.keyboard.press('Escape');await page.waitForSelector('#drawer.on',{state:'hidden'});
  }
  console.log('individual drawers',JSON.stringify(notes));
  console.log('blocked external fetches',JSON.stringify([...new Set(external)]));
  console.log('JavaScript exceptions',JSON.stringify(errors));assert.deepEqual(errors,[]);
 }finally{await browser.close()}
}
main().catch(e=>{console.error(e);process.exit(1)})
