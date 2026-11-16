/* SCRIPT: SF-BODIES-V2
   Solar Field: the measured shape and magnetic field of each body. Jeromie Beasley. 15 Nov 2026. AI-assisted.
   Sources (fetched 15 Nov 2026): NASA NSSDC fact sheets for the Sun, Mercury, Venus, Earth, Mars (radii, flattening, rotation, obliquity,
   dipole strength, tilt, offset); Winslow et al., Mercury's magnetopause and bow shock from MESSENGER Magnetometer observations
   (subsolar standoff 1.45 R_M at mean ram pressure 14.3 nPa, flaring 0.5); Wikipedia Magnetopause table (Earth typical 10 R_E, 6 to 15).
   Earth's obliquity 23.44 deg and sidereal day 23.9345 h are standard values not fetched that night.
   Dipole: field lines r = L cos^2(latitude) about the dipole axis. Pressure balance (Chapman-Ferraro, field doubled at the boundary):
   (2 B_eq)^2 / (2 mu0) = P  =>  r0/R = (2 B_eq^2 / (mu0 P))^(1/6). Ram pressure at distance a: 14.3 nPa x (a_Mercury / a)^2. */
var SFB = (function(){
"use strict";
const MU0 = 4e-7*Math.PI, P_MERC = 14.3e-9, A_MERC = 57.9;
const BODY = [
 { name:'Sun',     Req:695700,   f:0.00005,  rotH:609.12,  obl:7.25,   dipG:1.5,   tilt:0,    off:0,    mp:null, mpSrc:'', note:'polar field 1 to 2 gauss (1.5 used); no outer boundary drawn', col:[1,0.86,0.45] },
 { name:'Mercury', Req:2440.5,   f:0.0009,   rotH:1407.6,  obl:0.034,  dipG:0.002, tilt:0.0,  off:0.17, mp:1.45, mpSrc:'MESSENGER', note:'dipole offset 0.17 R north', col:[0.75,0.72,0.68] },
 { name:'Venus',   Req:6051.8,   f:0.000,    rotH:-5832.6, obl:177.36, dipG:0,     tilt:0,    off:0,    mp:null, mpSrc:'', note:'no magnetic field listed', col:[1,0.86,0.55] },
 { name:'Earth',   Req:6378.137, f:0.003353, rotH:23.9345, obl:23.44,  dipG:0.306, tilt:9.35, off:0,    mp:10,   mpSrc:'typical', note:'dipole offset 0.076 R not drawn (its direction was not in the source)', col:[0.39,0.75,1] },
 { name:'Mars',    Req:3396.2,   f:0.00589,  rotH:24.6229, obl:25.19,  dipG:0,     tilt:0,    off:0,    mp:null, mpSrc:'', note:'no magnetic field listed', col:[1,0.5,0.4] } ];
/* subsolar standoff in body radii from pressure balance; aNow = present distance from the Sun in 10^6 km */
function standoff(b, aNow){ if(!b.dipG || b.name === 'Sun') return NaN; const B = b.dipG*1e-4, P = P_MERC*(A_MERC/aNow)*(A_MERC/aNow); return Math.pow(2*B*B/(MU0*P), 1/6); }
const ramP = aNow => P_MERC*(A_MERC/aNow)*(A_MERC/aNow);
/* boundary shape about the Sun line: r(theta) = r0 (2/(1 + cos theta))^alpha, theta from the sunward direction (alpha = 0.5, the MESSENGER fit) */
const boundary = (r0, th) => r0*Math.pow(2/(1 + Math.cos(th)), 0.5);
/* the chart of one ball: physical distance x = r/R_body goes to the Smith coordinate of the ratio 3x, so the surface sits at 1/2 (one step of ratio 3) */
const chart = x => (3*x - 1)/(3*x + 1);
return { BODY, standoff, ramP, boundary, chart, MU0, P_MERC, A_MERC };
})();
if(typeof module !== 'undefined') module.exports = SFB;
