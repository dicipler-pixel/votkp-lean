# SCRIPT: BUILD-TREE-BALL-LIGHT-V2-01
# Builds Tree_Ball_Light_Mixer_v2_20261112.html from the original page (never written to).
# Every anchor must occur exactly once in the original, or the build stops.
import base64, sys
SRC="/mnt/user-data/uploads/11e6f62e-Tree_Ball_Light_Mixer__1_.html"
OUT="/home/claude/mixer_v2/Tree_Ball_Light_Mixer_v2_20261112.html"
s=open(SRC,encoding="utf-8").read()
def once(old,new):
    global s
    n=s.count(old); assert n==1,(n,old[:70]); s=s.replace(old,new)
def cut(a,b,new):
    global s
    assert s.count(a)==1 and s.count(b)==1,(s.count(a),s.count(b),a,b)
    i=s.index(a); j=s.index(b); assert i<j; s=s[:i]+new+s[j:]
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
FMJS=open("/home/claude/mixer_v2/feed_math.js",encoding="utf-8").read()

# ---------------- panel head
once("Garrett’s ratio-5 tree · phase, response and retained history<br>Jeromie Beasley · corrected research view · 11 November 2026",
     "Garrett’s ratio-5 tree · one loop feeds phase, pressure and turn<br>Jeromie Beasley · 12 November 2026 · developed with AI assistance")
once('<p class="what">Corrected derivative of the supplied mixer. Original data and v3 negative tests preserved. Colour B means internal SU(3), separate from optical/material colour.</p>',
     '<p class="what">One operator feeds the ball: the tree’s own four-step loop at step ratio z. Inside the wall the loop turns, at the wall it locks, past the wall it runs. Light is a prepared direction on the rim, carried by that loop.</p>'
     '<div class="ctl" id="feed"><label>Feed · step ratio z <output id="foz"></output><input id="fz" type="range" min="0.04879" max="2.99573" step="any" value="1.6094379124341003"></label>'
     '<div class="seg"><button id="fz3">z = 3</button><button id="fz5">Garrett z = 5</button><button id="fzw">wall 3 + 2√2</button><button id="fz8">z = 8</button></div><div class="tag" id="fline"></div></div>')
once("<p>Source models: Dirac Time §11; Light Keeps the Ledger 7.2 §§4.8–4.9f; Offset Speed Limit. Geometry: corrected ratio-5 Ball mixer. Optical and phase operators are attached finite models, not a derivation from the tree.</p>",
     "<p>Sources: Two Trees in One Ball and BallJoins (the loop and its trace); Dirac Time §11; Light Keeps the Ledger 7.2 §§4.8–4.9f; The Offset Speed Limit; The Price of a Direction (directions as rank-one projectors, distance 2 sin²θ); VOTKP v3.0 §22 (gap powers, two books). "
     "The phase view is fed by the loop: κ is half the loop’s turn and φ is the angle from the prepared direction to the loop’s axis. The tune-out view is a separate three-level response model placed at the end of a three-step route. "
     "The particle and Higgs views place Standard Model masses in the same ball; the feed does not move them.</p>"
     "<p>Loop checks (12 November 2026, kill lines written before each run): light on the peel disk, loop trace, centre of turn, Jordan block at the wall, loop-fed light, layer push. All exact to 1e-11 or better. Open: the run rate past the wall missed its 1e-6 line at early kicks and is not stated as a law; the count of distinguishable directions on the kick circle is not yet run. "
     + "".join('<a download="%s" href="data:application/octet-stream;base64,%s">%s</a> · '%(n,b64("/home/claude/mixer_v2/"+n),n) for n in
        ["feed_loop_01.py","feed_loop_01.out","feed_loop_02.py","feed_loop_02.out","feed_loop_03.py","feed_loop_03.out","feed_math.js","feed_math_test.js"]) + "</p>")
once("<p>Independent matrix checks: 909 optical frequency points, 9 environment scales, 100 phase states. All pass. Test evidence:",
     "<p>Response-model checks: 909 optical frequency points, 9 environment scales, 100 phase states. All pass. Test evidence:")

# ---------------- feed helpers (before the eyes)
HELP = FMJS + r'''
var FEED={z:5},TV=a=>new R(a[0],a[2],-a[1]),RIM=a=>TV(a).multiplyScalar(Ot),fz=document.getElementById("fz"),foz=document.getElementById("foz"),fline=document.getElementById("fline");
var setZ=z=>{FEED.z=z;fz.value=Math.log(z)};fz.oninput=()=>{FEED.z=Math.exp(+fz.value)};
document.getElementById("fz3").onclick=()=>setZ(3);document.getElementById("fz5").onclick=()=>setZ(5);document.getElementById("fzw").onclick=()=>setZ(FM.ZW);document.getElementById("fz8").onclick=()=>setZ(8);
var feedLine=o=>o.kind==="turn"?"turns "+(o.theta/(2*Math.PI)).toFixed(4)+" of a full turn per loop":o.kind==="wall"?"at the wall: one Jordan block, a full turn":"no turn: runs "+o.lam.toFixed(3)+" per loop";
function FU(){let o=FM.calc(FEED.z);foz.textContent="z = "+FEED.z.toFixed(3)+" · Γ² = "+o.R.toFixed(4);fline.innerHTML="<b>"+feedLine(o)+"</b>"}
var fixedLine=o=>{let p=[];for(let b=-6;b<=6.001;b+=.1){let c=Math.cosh(b),h=Math.sinh(b);p.push(zn(FM.boost4([c,h*o.axis[0],h*o.axis[1],h*o.axis[2]],o.d,o.eta)))}return p};
var centrePt=o=>zn(FM.boost4([1,0,0,0],o.d,o.eta));
var side=o=>Math.abs(o.rho*o.rho-.5)<5e-4?"on the half-line sphere":o.rho*o.rho<.5?"inside the half-line sphere":"outside the half-line sphere";
'''
once("var Wt={};Wt.end={", HELP+"var Wt={};Wt.end={")

# ---------------- the feed eye (was: wall)
WALL = r'''Wt.wall={title:"The loop that feeds the ball",grade:"PROVED (BallJoins J4: trace) · CHECKED FEED-LOOP-01/02/03 · known (Koide 1981, Foot)",eq:`W(z) = B_i B_j B_i⁻¹ B_j⁻¹,   each step of ratio z,   Γ = (z−1)/(z+1)
tr W = 2 − 4 sinh⁴(r/2) = 2 − 4 (R/T)²,   R = Γ²,  T = 1 − R
inside the wall: a turn θ about a centre at radius ρ,   ρ² = (1−s)/(1+s),  s = √(1−2Γ²)`,what:"Two perpendicular steps out and back make the loop W. While the layer passes more than it reflects (R < T) the loop is a turn: it leaves one line of the ball fixed and turns everything about it. The gold line is that fixed line and the gold point is its centre, the place the turn is seen from. As z grows the centre moves out along the bisector of the two arms. At Garrett’s step z = 5 it sits exactly on the half-line sphere, radius² = 1/2, and at no other step. At the wall, z = 3 + 2√2, R = T: the turn is one full turn and the loop is a single Jordan block. Past the wall nothing turns; the loop runs from one rim point to another. Koide is a separate encoding of the charged-lepton masses, balanced centred books (B200), not the edge-book ratio wall (B189). Integer generation levels and a tree-selected Koide cone were tested at finite depth and not found.",enter(){ci(),sn.style.display="none",document.getElementById("modes").style.display="",vs.innerHTML="";
let i=Ot*.99/Math.SQRT2,e=new Sr(i,i,96,1,!0);e.translate(0,-i/2,0),e.rotateX(Math.PI),this.cone=new ft(e,new tn({color:16734830,wireframe:!0,transparent:!0,opacity:.12,depthWrite:!1})),this.cone.quaternion.setFromUnitVectors(new R(0,1,0),yt),at.add(this.cone);
let t=.51099895,n=105.6583755,s=1776.93,r=hn[0].clone().multiplyScalar(Math.sqrt(t)).add(hn[1].clone().multiplyScalar(Math.sqrt(n))).add(hn[2].clone().multiplyScalar(Math.sqrt(s))).normalize();this.koide=new On(r,new R,Ot*.98,12576511,.25,.12),at.add(this.koide),this.loop=new Ht(new Ke,hi(16777215,.95)),at.add(this.loop),this.end=li(16734830,.4),at.add(this.end);
this.fix=new Ht(new Ke,hi(15909198,.95)),at.add(this.fix),this.centre=li(15909198,.6),at.add(this.centre),this.pa=li(16747900,.5),at.add(this.pa),this.pr=li(6542335,.5),at.add(this.pr);
ui([["(√m_e, √m_μ, √m_τ)",this.koide.cone,"#bfe6ff"],["loop end",this.end,"#ff9fb4"],["centre of turn",this.centre,"#f2c14e"],["runs to",this.pa,"#ff8d7c"],["runs from",this.pr,"#63d3ff"]]),document.getElementById("key").innerHTML="red mesh sphere: half line Γ² = ½ · white: the four-step loop from the centre · red dot: where it ends · gold line: the line the loop leaves fixed · gold point: centre of turn · red cone: Koide encoding (reading A)",Gt.position.set(8.4,5.2,10.4)},step(){let o=FM.calc(FEED.z),e=o.r,n=[[0,1],[1,1],[0,-1],[1,-1]],s=c=>{let h=_s;for(let u=c-1;u>=0;u--)h=To(h,n[u][0],n[u][1]*e);
return h},r=[zn(_s)];for(let c=1;c<=4;c++)xs(s(c-1),s(c),20).slice(1).forEach(h=>r.push(zn(h)));
this.loop.geometry.dispose(),this.loop.geometry=new Ke().setFromPoints(r),this.end.position.copy(zn(s(4))),this.koide.visible=this.cone.visible=Sn==="A";
let T=o.kind==="turn",H=o.kind==="run";this.fix.visible=this.centre.visible=T,this.pa.visible=this.pr.visible=H;
T&&(this.fix.geometry.dispose(),this.fix.geometry=new Ke().setFromPoints(fixedLine(o)),this.centre.position.copy(centrePt(o)));H&&(this.pa.position.copy(RIM(o.att)),this.pr.position.copy(RIM(o.rep)));
let l=[["μ→τ",16.8177],["d→s",19.8936],["s→b",44.738],["c→t",135.562],["e→μ",206.768],["u→c",589.352]];return[["reading of the ball here","radius = Γ of a step ratio; the rim holds prepared directions"],["step ratio z",o.z.toFixed(4)],["layer reflects R = Γ²",o.R.toFixed(5)],["layer passes T = 1 − R",o.T.toFixed(5)],["loop trace 2 − 4 (R/T)²",o.tr.toFixed(4)],["the loop",feedLine(o)],["obliqueness K = 1/(T − R)",T?o.K.toFixed(4):H?"not defined past the wall":"diverges at the wall"],["centre of turn, radius ρ",T?o.rho.toFixed(5)+" · "+side(o):"at the rim"],["the wall","z = 3 + 2√2 = 5.8284,  R = T = ½"],["Garrett’s step z = 5","ρ² = ½ exactly · K = 9 · turn 0.5903"],["generation steps (all past the wall)",l.map(c=>c[0]+" "+c[1].toFixed(1)).join(" · ")],["Koide cos² (reading A)",Sn==="A"?"0.5000017 (balanced centred books)":"not drawn in reading B"]]}};'''
cut("Wt.wall={","Wt.higgs={",WALL)

# ---------------- light eye, fed by the loop
LIGHT = r'''Wt.light={title:"Light · the loop drives the signal",grade:"CHECKED · FEED-LOOP-02 (exact to 3e-14) · light as a prepared direction on the rim",eq:`after t loops:   c(t) = [1 + sin(tθ) sinφ]/2
κ = θ/2 per loop,   φ = angle from the prepared direction to the loop axis
Γ = 1 − 2c,   g = κ² sin²φ,   Γ̇² ≤ 4g(1 − Γ²)`,what:"A prepared direction is a point on the rim, a rank-one projector. Each pass of the loop kicks it to the next point of one circle on the rim, the gold circle, drawn about the line the loop leaves fixed. Seen from the centre of turn the kicks are an even turn, and the share c read across that turn is the signal. Its peel coordinate is Γ = 1 − 2c, so the stored angle φ sets how far the signal can reach: it touches the half line only if sin²φ ≥ ½. Two preparations mirrored about the loop axis start with the same share and separate with opposite sign. Arms i and j lie square to the axis (sin²φ = 1). Arm k is tilted by the push on the layer: sin²φ = 2Γ². A direction on the fixed line gives no signal at any step. Past the wall there is no circle: every prepared direction runs to one rim point.",enter(){ci(),Xc('<div class="tag">Prepared direction</div><div class="seg" id="pd"><button data-d="i">arm i</button><button data-d="j">arm j</button><button data-d="k">arm k</button><button data-d="d">(1,1,1)</button><button data-d="f">fixed line</button></div><label>Loops t <output id="lt"></output><input id="time" type="range" min="0" max="12" step="0.001" value="0"></label><div><button id="playLight">Play / pause</button> <button id="resetLight">Reset</button></div>'),this.time=document.getElementById("time"),this.running=!0,this.dir="k",this.sig="",this.g=new jt,at.add(this.g);
document.querySelectorAll("#pd button").forEach(b=>b.onclick=()=>{this.dir=b.dataset.d});document.getElementById("playLight").onclick=()=>this.running=!this.running,document.getElementById("resetLight").onclick=()=>{this.time.value=0,this.running=!1},this.time.oninput=()=>this.running=!1,document.getElementById("key").textContent="Gold circle: where the loop’s kicks carry the prepared direction. Small dots: whole loops 0 to 11. White: the direction now. Gold line and point: fixed line and centre of turn. Chart: share c(t) for the two mirrored preparations (cyan, coral), 0 to 1; gold cursor: loops so far.",Gt.position.set(11.5,5.2,-6.5)},build(o){for(;this.g.children.length;){let c=this.g.children.pop();c.geometry&&c.geometry.dispose(),c.material&&c.material.dispose&&c.material.dispose()}let dv={i:[1,0,0],j:[0,1,0],k:[0,0,1],d:[1,1,1]}[this.dir];
if(this.dir==="f")dv=o.kind==="turn"?FM.bloch(FM.mv(o.S,FM.stateOf(o.axis))):o.kind==="run"?o.rep:[0,0,1];this.dv=dv;this.p=FM.prep(o,dv);this.now=li(16777215,.55),this.g.add(this.now);let L=[["direction now",this.now,"#ffffff"]];
if(o.kind==="turn"){let per=2*Math.PI/o.theta,pts=[];for(let m=0;m<=180;m++)pts.push(RIM(FM.labAt(o,this.p,per*m/180)));this.g.add(new Ht(new Ke().setFromPoints(pts),hi(15909198,.9)));for(let m=0;m<12;m++){let d=li(15909198,.2);d.position.copy(RIM(FM.labAt(o,this.p,m)));this.g.add(d)}this.g.add(new Ht(new Ke().setFromPoints(fixedLine(o)),hi(15909198,.6)));let c=li(15909198,.5);c.position.copy(centrePt(o));this.g.add(c);L.push(["centre of turn",c,"#f2c14e"])}
else if(o.kind==="run"){this.run=[];let psi=this.p.psi,pts=[];for(let m=0;m<=12;m++){let b=FM.bloch(psi);this.run.push(b);pts.push(RIM(b));let d=li(15909198,.2);d.position.copy(RIM(b));this.g.add(d);psi=FM.kick(o,psi)}this.g.add(new Ht(new Ke().setFromPoints(pts),hi(15909198,.5)));let a=li(16747900,.5);a.position.copy(RIM(o.att));this.g.add(a);L.push(["runs to",a,"#ff8d7c"])}ui(L)},step(i){this.running&&(this.time.value=(+this.time.value+i*.5)%12);
let o=FM.calc(FEED.z),t=+this.time.value,sg=o.z.toFixed(5)+this.dir;sg!==this.sig&&(this.sig=sg,this.build(o));document.querySelectorAll("#pd button").forEach(b=>b.classList.toggle("on",b.dataset.d===this.dir));document.getElementById("lt").textContent=t.toFixed(2);
let head=[["reading of the ball here","rim point = prepared direction (rank-one projector); Γ = 1 − 2c is the peel coordinate of the share"],["feed",o.z.toFixed(3)+" · "+feedLine(o)]];
if(o.kind==="turn"){let p=this.p,c=FM.occ(o,p,t),G=1-2*c,k=o.theta/2,g=k*k*p.sin2,sp=Math.sqrt(p.sin2),Gd=-o.theta*sp*Math.cos(t*o.theta),bd=4*g*(1-G*G);this.now.position.copy(RIM(FM.labAt(o,p,t)));qc(a=>{let q=FM.occ(o,p,a);return[q,1-q]},12,0,1,t,["c, prepared at +φ","c, mirrored at −φ"]);
return head.concat([["κ = θ/2 per loop",k.toFixed(5)],["stored angle φ",(p.phi/Math.PI).toFixed(4)+"π · sin²φ = "+p.sin2.toFixed(5)],["share c(+φ) / c(−φ)",c.toFixed(5)+" / "+(1-c).toFixed(5)],["Γ = 1 − 2c",G.toFixed(5)],["metric g = κ² sin²φ",g.toFixed(5)],["Γ̇² / bound 4g(1 − Γ²)",(Gd*Gd).toFixed(5)+" / "+bd.toFixed(5)],["largest Γ² the signal reaches",p.sin2.toFixed(5)+(p.sin2>=.5?" · reaches the half line":" · stays inside the half line")],["projector distance from the loop axis, 2 sin²(φ/2)",(1-p.cos).toFixed(5)]])}
if(o.kind==="run"){let n=Math.min(12,Math.floor(t)),b=this.run[n];this.now.position.copy(RIM(b));qc(a=>{let q=this.run[Math.min(12,Math.floor(a))];return[(1+FM.dot(q,o.att))/2,NaN]},12,0,1,t,["share on the far rim point, per whole loop",""]);return head.concat([["whole loops",String(n)],["share on the far rim point",((1+FM.dot(b,o.att))/2).toFixed(6)],["turn","none: the phase is spent, the loop runs"],["run per loop λ",o.lam.toFixed(4)+" (rate of approach not yet stated as a law)"]])}
this.now.position.copy(RIM(this.dv));qc(a=>[NaN,NaN],12,0,1,t,["at the wall",""]);return head.concat([["at the wall","one full turn, one Jordan block: the circle has closed onto a single rim point"]])}};'''
cut("Wt.light={","Wt.response={",LIGHT)

# ---------------- pressure eye (new), placed before the response eye's model export
PRESS = r'''Wt.pressure={title:"Light pressure on a layer",grade:"IDENTITY CHECKED · FEED-LOOP-03 · reading as physical pressure: untested",eq:`one lossless layer:  R = Γ² reflected,  T = 1 − R passed
push on the layer:  P = 2R   (a full absorber feels 1)
K = 1/(T − R) = 1/(1 − P) = 1 + P + P² + …`,what:"A step of ratio z is read as one lossless layer that reflects R = Γ² and passes T = 1 − R. Reflected light pushes twice, passed light not at all, so the push on the layer is P = 2R in units of the push on a full absorber. The loop’s obliqueness is K = 1/(1 − P): the sum of every repeated push, light held between layers and kicked again. While P < 1 the sum closes and the loop turns. At the wall R = T, the layer is pushed as hard as a full absorber, the sum no longer closes and the turn locks. Past the wall the push exceeds an absorber’s and the light is driven through, one way. The same P is the tilt of arm-k light, sin²φ = P, so arm-k light first reaches the half line at P = ½: z = 3, K = 2. The identities are exact; that P is the pressure of light in the layers of an atom is a reading, not yet tested.",enter(){ci(),Xc(""),this.A=TV(FM.calc(5).d).multiplyScalar(Ot/Math.SQRT2);let d=TV([Math.SQRT1_2,Math.SQRT1_2,0]),u=new R(0,1,0);this.d=d;
this.inA=new On(d,this.A.clone().sub(d.clone().multiplyScalar(1.5)).add(u.clone().multiplyScalar(.12)),1.5,16777215,.2,.1),at.add(this.inA);this.rf=new On(d.clone().negate(),this.A.clone().sub(u.clone().multiplyScalar(.12)),1,16747900,.2,.1),at.add(this.rf);this.tr=new On(d,this.A.clone().add(u.clone().multiplyScalar(.12)),1,6542335,.2,.1),at.add(this.tr);
this.ring=new ft(new br(.6,.025,10,90),new tn({color:15909198})),this.ring.quaternion.setFromUnitVectors(new R(0,0,1),d),this.ring.position.copy(this.A),at.add(this.ring);this.centre=li(15909198,.5),at.add(this.centre);
ui([["light in",this.inA.cone,"#ffffff"],["reflected R",this.rf.cone,"#ff8d7c"],["passed T",this.tr.cone,"#63d3ff"],["push P",this.ring,"#f2c14e"]]),document.getElementById("key").textContent="The layer is the half-line sphere where the bisector of arms i and j meets it. Coral: reflected share R. Cyan: passed share T. Gold ring: push P = 2R. Chart: P (cyan) and 1/K = T − R (coral) against Γ², 0 to 0.6; gold cursor: the feed.",Gt.position.set(9,5.4,9.6)},step(){let o=FM.calc(FEED.z);this.rf.setLength(.05+1.5*o.R,.2,.1),this.tr.setLength(.05+1.5*o.T,.2,.1),this.ring.scale.setScalar(.25+o.P);let T=o.kind==="turn";this.centre.visible=T;T&&this.centre.position.copy(centrePt(o));
qc(x=>[2*x,x<.5?1-2*x:NaN],.6,0,1.25,Math.min(.6,o.R),["P = 2Γ², push on the layer","1/K = T − R"]);let sum=0;for(let m=0;m<10;m++)sum+=Math.pow(o.P,m);
return[["reading of the ball here","one step = one layer; radius = Γ, R = Γ²"],["feed",o.z.toFixed(3)+" · "+feedLine(o)],["reflected R / passed T",o.R.toFixed(5)+" / "+o.T.toFixed(5)],["push P = 2R",o.P.toFixed(5)+(o.P<1?" · below a full absorber":Math.abs(o.P-1)<1e-3?" · equal to a full absorber":" · above a full absorber")],["K = 1/(1 − P)",T?o.K.toFixed(4):"the sum does not close"],["first ten pushes 1 + P + … + P⁹",sum.toFixed(4)],["arm-k light, sin²φ",T?o.P.toFixed(5)+(o.P>=.5?" · reaches the half line":" · stays inside"):"no turn"],["centre of turn",T?"ρ = "+o.rho.toFixed(5)+" · "+side(o):"at the rim"],["marks","z = 3: P = ½, K = 2 · z = 5: P = 8/9, K = 9 · wall: P = 1"]]}};'''
once("window.__lightModel=ai;", PRESS+"window.__lightModel=ai;")

# ---------------- order, default eye, feed readout in the frame loop
once('var Yc=["light","response","end","particles","wall","higgs"]','var Yc=["wall","light","pressure","response","end","particles","higgs"]')
once('Ro(Yc.includes(location.hash.slice(1))?location.hash.slice(1):"light")','Ro(Yc.includes(location.hash.slice(1))?location.hash.slice(1):"wall")')
once("So.update(),wo.rotation.y+=0,Br(Wt[kn].step(e,Fr))","So.update(),FU(),Br(Wt[kn].step(e,Fr))")
once('window.__sm={go:Ro,setMode:Co};','window.__sm={go:Ro,setMode:Co,setZ:setZ,feed:()=>FM.calc(FEED.z)};')

# ---------------- the kept eyes: his terms, one stated reading of the ball each
once('title:"Light \\xB7 tune-out and environment"','title:"Response \\xB7 tune-out and environment"')
once("This is an environment model, not a fitted pressure law or an elemental spectrum. Resonance bands are excluded: this model has no damping.",
     "This is a three-level response model placed at the end of a three-step route; the feed does not move it. It is not a pressure law or an elemental spectrum. Resonance bands are excluded: this model has no damping.")
once("These are geometric angles, not quantum amplitudes. The rejected helicity-locking test stays rejected. Zero induced turn is not zero particle spin, and inverse transport rotations do not create a spin singlet.",
     "These are geometric angles, not quantum amplitudes. Helicity locking was tested and not found. Zero induced turn is not zero particle spin, and inverse transport rotations do not make a spin singlet. The stored run is at Garrett’s step z = 5; the feed does not move it.")
once('return[["step on the chain",`${e+1} (12 animated; 40 in stored run)`]','return[["reading of the ball here","radius = tanh(η/2) of the summed steps"],["step on the chain",`${e+1} (12 animated; 40 in stored run)`]')
once("so heavy particles sit near the centre and light ones crowd the rim; the photon and the gluons are on the rim itself.",
     "so heavy particles sit near the centre and light ones crowd the rim; the photon and the gluons are on the rim itself. In this view radius² is the peel coordinate of E/m, so a particle crosses the half-line sphere at E = 3m.")
once('return[["reading of the arms",Sn==="A"?"A \\xB7 generations":"B \\xB7 colours"]','return[["reading of the ball here","radius² = Γ(E/m); half-line sphere at E = 3m"],["reading of the arms",Sn==="A"?"A \\xB7 generations":"B \\xB7 colours"]')
once('return[["v",(246*t).toFixed(1)+" GeV"]','return[["reading of the ball here","radius² = Γ(E/m); half-line sphere at E = 3m"],["v",(246*t).toFixed(1)+" GeV"]')
once("The finite commutator wall is unrelated to this massless boundary.","The half-line sphere of the loop is a different place from this massless rim.")
once("red mesh: finite commutator step wall \\u0393\\xB2 = \\xBD; outer rim: radius 1","red mesh: half line \\u0393\\xB2 = \\xBD; outer rim: radius 1")
open(OUT,"w",encoding="utf-8").write(s)
print("written",OUT,len(s))
