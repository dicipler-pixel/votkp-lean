// SCRIPT: FEED-MATH-JS-01
// WHY: the page runs this JavaScript, not the Python. It must give the Python numbers of FEED-LOOP-02/03.
// KILL LINE: any difference above 1e-9 from the stored Python values, or from the closed forms.
const fs=require('fs');eval(fs.readFileSync(__dirname+'/feed_math.js','utf8')+';globalThis.FM=FM');
const py=JSON.parse(fs.readFileSync(__dirname+'/feed_loop_02.out'));let worst=0;const chk=(n,a,b)=>{const e=Math.abs(a-b);worst=Math.max(worst,e);if(e>1e-9)console.log('FAIL',n,a,b)};
for(const row of py.table){const o=FM.calc(row.z);chk('K',o.K,row.K);chk('rho',o.rho,row.rho);chk('theta',o.theta/(2*Math.PI),row.turn_over_2pi);chk('axz',o.axis[2],row.axis[2]);chk('axx',o.axis[0],row.axis[0])}
const o=FM.calc(5);for(const row of py.K5_rows){const p=FM.prep(o,row.prep);chk('sin2 '+row.prep,p.sin2,row.sin2phi);
 for(let n=0;n<40;n++){chk('occ',FM.occ(o,p,n),(1+Math.sin(n*o.theta)*Math.sin(p.phi))/2)}
 // lab kicks equal S U^n S^-1
 let psi=p.psi;for(let n=0;n<20;n++){const a=FM.bloch(psi),b=FM.labAt(o,p,n);chk('lab',Math.hypot(a[0]-b[0],a[1]-b[1],a[2]-b[2]),0);psi=FM.kick(o,psi)}}
// continuous time: Gamma=1-2c, bound
{const p=FM.prep(o,[0,0,1]);for(let t=0;t<6;t+=.137){const c=FM.occ(o,p,t);chk('cont',c,(1+Math.sin(t*o.theta)*Math.sin(p.phi))/2)}}
// run side
for(const z of [6.5,8,16.8177]){const h=FM.calc(z);let psi=FM.stateOf([0,0,1]);for(let n=0;n<40;n++)psi=FM.kick(h,psi);const b=FM.bloch(psi);chk('att '+z,Math.hypot(b[0]-h.att[0],b[1]-h.att[1],b[2]-h.att[2]),0);chk('unit',Math.hypot(...h.att),1)}
console.log('wall kind',FM.calc(FM.ZW).kind,'| z=5 rho^2',o.rho*o.rho,'K',o.K,'| worst',worst.toExponential(2),worst<1e-9?'PASS':'FAIL');
