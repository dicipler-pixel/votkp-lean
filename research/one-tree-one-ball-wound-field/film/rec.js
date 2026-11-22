// SCRIPT: WOUND-FILM-RECORD  films one scene of the wound-field ball at 15 fps into frames/<scene>/
const {chromium}=require('playwright');const fs=require('fs');
const sc=process.argv[2];const cues=JSON.parse(fs.readFileSync('cues.json'));const D=cues[sc].dur;const FPS=15;
const ease=x=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x);};
const plan={
 s1:t=>['cells',{map:0,lam:1,cell:20,L:6-2.4745*ease(t/(D-3))},null],
 s2:t=>['shape',{map:0,lam:1,L:4},null],
 s3:t=>['close',{map:0,lam:1,L0:6,v:.5},Math.min(.9999,t/D)],
 s4:t=>['drugs',{map:0,lam0:1,c:.3333,L:3.5255,fm:1,fG:t<5?1:t<11?1+3*ease((t-5)/5):t<16?4-3.75*ease((t-11)/4):.25+.75*ease((t-16)/4)},null],
 s5:t=>['cells',{map:t<12?0:1,lam:1,cell:20,L:t<19?3.5255:3.5255-1.7628*ease((t-19)/6)},null]};
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1220,height:834}});await p.goto('file://'+process.cwd()+'/One_Tree_One_Ball_Wound_Field_v2.html');await p.waitForTimeout(1200);
fs.mkdirSync('frames/'+sc,{recursive:true});const N=Math.ceil(D*FPS);
for(let i=0;i<N;i++){const [id,set,u]=plan[sc](i/FPS);
 await p.evaluate(([id,set,u])=>{if(!window.__id||window.__id!==id){window.API.show(id);window.__id=id;}Object.assign(window.API.P,set);window.API.frame(1/15,id,u);},[id,set,u]);
 await p.screenshot({path:`frames/${sc}/${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});}
console.log(sc,'frames',N);await b.close();})();
