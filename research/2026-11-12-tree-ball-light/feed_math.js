/* FEED: the tree's four-step loop W(z) = Bi Bj Bi^-1 Bj^-1, steps of ratio z along arms i and j. Tree coordinates (i,j,k). */
var FM=(function(){
var cm=function(a,b){return[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]]},ca=function(a,b){return[a[0]+b[0],a[1]+b[1]]};
var mm=function(A,B){return[ca(cm(A[0],B[0]),cm(A[1],B[2])),ca(cm(A[0],B[1]),cm(A[1],B[3])),ca(cm(A[2],B[0]),cm(A[3],B[2])),ca(cm(A[2],B[1]),cm(A[3],B[3]))]};
var mv=function(A,v){return[ca(cm(A[0],v[0]),cm(A[1],v[1])),ca(cm(A[2],v[0]),cm(A[3],v[1]))]};
var nrm=function(v){var n=Math.hypot(v[0][0],v[0][1],v[1][0],v[1][1]);return[[v[0][0]/n,v[0][1]/n],[v[1][0]/n,v[1][1]/n]]};
var pauli=function(a0,a){return[ca(a0,a[2]),ca(a[0],cm([0,-1],a[1])),ca(a[0],cm([0,1],a[1])),ca(a0,[-a[2][0],-a[2][1]])]};
var boostM=function(d,eta){var c=Math.cosh(eta/2),s=Math.sinh(eta/2);return pauli([c,0],[[s*d[0],0],[s*d[1],0],[s*d[2],0]])};
var rotM=function(a,ang){var c=Math.cos(ang/2),s=Math.sin(ang/2);return pauli([c,0],[[0,-s*a[0]],[0,-s*a[1]],[0,-s*a[2]]])};
var bloch=function(v){v=nrm(v);var p=cm([v[0][0],-v[0][1]],v[1]);return[2*p[0],2*p[1],v[0][0]*v[0][0]+v[0][1]*v[0][1]-v[1][0]*v[1][0]-v[1][1]*v[1][1]]};
var stateOf=function(n){var l=Math.hypot(n[0],n[1],n[2]);n=[n[0]/l,n[1]/l,n[2]/l];return n[2]>-1+1e-12?nrm([[1+n[2],0],[n[0],n[1]]]):[[0,0],[1,0]]};
var dot=function(a,b){return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]},cross=function(a,b){return[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]};
var unit=function(a){var l=Math.hypot(a[0],a[1],a[2]);return l<1e-14?null:[a[0]/l,a[1]/l,a[2]/l]};
var ZW=3+2*Math.SQRT2,D=[Math.SQRT1_2,Math.SQRT1_2,0];
function loopM(r){return mm(mm(boostM([1,0,0],r),boostM([0,1,0],r)),mm(boostM([1,0,0],-r),boostM([0,1,0],-r)))}
function calc(z){var r=Math.log(z),G=Math.tanh(r/2),R=G*G,T=1-R,P=2*R,x=R/T,tr=2-4*x*x,W=loopM(r);
 var o={z:z,r:r,G:G,R:R,T:T,P:P,tr:tr,W:W,d:D};
 if(Math.abs(R-.5)<2e-4){o.kind="wall";return o}
 if(R<.5){var s=Math.sqrt(1-2*R);o.kind="turn";o.K=1/(1-2*R);o.rho=Math.sqrt((1-s)/(1+s));o.eta=2*Math.atanh(o.rho);o.theta=2*Math.acos(1-2*x*x);
  o.S=boostM(D,o.eta);o.Si=boostM(D,-o.eta);var U=mm(mm(o.Si,W),o.S),sh=Math.sin(o.theta/2);
  o.axis=unit([-(U[1][1]+U[2][1])/(2*sh),-(U[1][0]-U[2][0])/(2*sh),-(U[0][1]-U[3][1])/(2*sh)]);return o}
 o.kind="run";o.lam=2*Math.acosh(-tr/2);var disc=Math.sqrt(tr*tr-4),l1=(tr-disc)/2,l2=(tr+disc)/2;
 var ev=function(l){return bloch([W[1],[l-W[0][0],-W[0][1]]])};o.att=ev(l1);o.rep=ev(l2);o.lbig=l1;return o}
/* prepared direction n (tree coords). Inside the wall: angle to the loop axis, read-out axis, occupation after t loops. */
function prep(o,n){var p={psi:stateOf(n)};if(o.kind!=="turn")return p;
 p.own=nrm(mv(o.Si,p.psi));p.s0=bloch(p.own);var c=dot(p.s0,o.axis);p.cos=c;p.sin2=Math.max(0,1-c*c);p.phi=Math.acos(Math.max(-1,Math.min(1,c)));
 p.q=unit(cross(o.axis,p.s0));return p}
function ownAt(o,p,t){return nrm(mv(rotM(o.axis,t*o.theta),p.own))}
function occ(o,p,t){if(!p.q)return .5;var b=bloch(ownAt(o,p,t));return(1+dot(b,p.q))/2}
function labAt(o,p,t){return bloch(mv(o.S,ownAt(o,p,t)))}
function kick(o,psi){return nrm(mv(o.W,psi))}
/* 4-vector boost of a hyperboloid point [t,x,y,z] along unit d */
function boost4(v,d,eta){var c=Math.cosh(eta),s=Math.sinh(eta),p=v[1]*d[0]+v[2]*d[1]+v[3]*d[2],f=(c-1)*p+s*v[0];return[c*v[0]+s*p,v[1]+f*d[0],v[2]+f*d[1],v[3]+f*d[2]]}
return{calc:calc,prep:prep,occ:occ,labAt:labAt,ownAt:ownAt,kick:kick,bloch:bloch,stateOf:stateOf,boost4:boost4,dot:dot,ZW:ZW,mv:mv,nrm:nrm}})();
