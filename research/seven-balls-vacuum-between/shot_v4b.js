// SCRIPT: SB-V4-SHOT-B — close view of one open y-z gap with the other layers off
const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1500,height:900}});
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(2500);
const info=await p.evaluate(()=>{window.seven.seek(12);window.seven.set({show:{light:false,free:false,hits:false,rims:false,occ:false,push:false,record:false,clocks:false,names:true,circles:false},outOp:0.35});
  const S=window.seven.state();const a=S.balls[3],c=S.balls[5];const m=[(a.c[0]+c.c[0])/2,(a.c[1]+c.c[1])/2,(a.c[2]+c.c[2])/2];window.seven.setView(Math.PI/2+0.3,0.15,3.2,m);document.body.classList.add('clean');return m;});
await p.evaluate(()=>{dispatchEvent(new Event('resize'));});await p.waitForTimeout(500);await p.screenshot({path:process.argv[3]});console.log(info);await b.close();})();
