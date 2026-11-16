/* SCRIPT: SF-MATH-V1
   Solar Field: the Sun and the planets out to Mars as balls of one kind. Jeromie Beasley. 15 Nov 2026. AI-assisted.
   Start in the perfect world (equal steps, circles, one plane, equal timing), where the books must balance; then each natural effect
   has its own dial from 0 (perfect) to 1 (as measured): steps, ellipse, tilt, timing.
   Reading (declared, not a theorem): the step between two bodies is the logarithm of the ratio of their distances from the Sun,
   r = ln z, Γ = (z − 1)/(z + 1); distances are hyperbolic lengths in the peel coordinate of the ball, which is not space.
   Data: NASA Planetary Fact Sheet (distance 10^6 km, period days, eccentricity, inclination degrees). Pure functions. */
var SF = (function(){
"use strict";
const PI = Math.PI, SUN_R = 0.6957, C_LIGHT = 0.299792458;             /* 10^6 km; 10^6 km per second */
const BODIES = [ { name:'Mercury', a:57.9, T:88.0, e:0.206, inc:7.0, col:[0.75,0.72,0.68] }, { name:'Venus', a:108.2, T:224.7, e:0.007, inc:3.4, col:[1,0.86,0.55] },
                 { name:'Earth', a:149.6, T:365.2, e:0.017, inc:0.0, col:[0.39,0.75,1] }, { name:'Mars', a:228.0, T:687.0, e:0.094, inc:1.8, col:[1,0.5,0.4] } ];
const R0 = Math.log(3), T0 = 365.2;                                    /* the perfect step (z = 3, Γ = 1/2) and the perfect period */
const lerp = (a,b,s) => a + (b-a)*s;
function kepler(M, e){ let E = M; for(let k=0;k<12;k++) E -= (E - e*Math.sin(E) - M)/(1 - e*Math.cos(E)); return E; }
/* state of every planet at day t for dials D = {steps, ellipse, tilt, timing} */
function state(day, D){ return BODIES.map((b, n) => { const T = lerp(T0, b.T, D.timing), e = b.e*D.ellipse, M = 2*PI*day/T + n*PI/2, E = kepler(M, e);
    const nu = 2*Math.atan2(Math.sqrt(1+e)*Math.sin(E/2), Math.sqrt(1-e)*Math.cos(E/2)), rho = 1 - e*Math.cos(E);        /* true anomaly; distance over semi-major axis */
    const dPerfect = (n+1)*R0, dReal = Math.log(b.a/SUN_R), d = lerp(dPerfect, dReal, D.steps) + Math.log(rho);            /* hyperbolic distance from the Sun's centre */
    return { name:b.name, col:b.col, d, phi:nu, inc:b.inc*D.tilt*PI/180, T, e, rho, lightSec:b.a*rho/C_LIGHT }; }); }
/* hyperboloid vectors (t, i, j, k) */
const mm = (A,B) => A.map(r => [0,1,2,3].map(j => r[0]*B[0][j]+r[1]*B[1][j]+r[2]*B[2][j]+r[3]*B[3][j]));
const mv = (A,v) => A.map(r => r[0]*v[0]+r[1]*v[1]+r[2]*v[2]+r[3]*v[3]);
const mink = (p,q) => p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3];
const boostI = r => { const c = Math.cosh(r), s = Math.sinh(r); return [[c,s,0,0],[s,c,0,0],[0,0,1,0],[0,0,0,1]]; };
const rotK = a => { const c = Math.cos(a), s = Math.sin(a); return [[1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1]]; };      /* turn in the plane of I and J */
const rotI = a => { const c = Math.cos(a), s = Math.sin(a); return [[1,0,0,0],[0,1,0,0],[0,0,c,-s],[0,0,s,c]]; };      /* tilt of the orbit plane about the I arm */
/* the step that takes the Sun's centre to the planet's centre, and its inverse (what the planet sees) */
const cell = p => mm(rotI(p.inc), mm(rotK(p.phi), boostI(p.d)));
const cellInv = p => mm(boostI(-p.d), mm(rotK(-p.phi), rotI(-p.inc)));
const centre = p => mv(cell(p), [1,0,0,0]);
/* share of the Sun's light that would pass through a ball of radius rad at distance d with nothing in the way (solid angle over 4π) */
function freeShare(d, rad){ if(d <= rad) return 1; const s = Math.sinh(rad)/Math.sinh(d); return (1 - Math.sqrt(1 - s*s))/2; }
/* least distance from point c to the geodesic piece from P along unit tangent V of length S */
function segDist(c, P, V, S){ const A = mink(c, P), B = mink(c, V);          /* cosh dist(s) = A cosh s + B sinh s, least where tanh s = −B/A */
  let s = Math.atanh(Math.max(-0.9999999, Math.min(0.9999999, -B/A))); s = Math.max(0, Math.min(S, s)); return Math.acosh(Math.max(1, A*Math.cosh(s) + B*Math.sinh(s))); }
return { BODIES, R0, T0, SUN_R, state, cell, cellInv, centre, freeShare, segDist, mm, mv, mink, kepler };
})();
if(typeof module !== 'undefined') module.exports = SF;
