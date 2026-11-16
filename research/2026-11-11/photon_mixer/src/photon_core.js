/* SCRIPT: PHOTON-MIXER-CORE
   Physics core of the Ballad of a Dead Photon mixer (Jeromie Beasley). Every number an eye shows is computed here.
   SI units unless stated. Runs in the browser and in Node. */
(function(root){
"use strict";
const c = 299792458, h = 6.62607015e-34, e = 1.602176634e-19, kB = 1.380649e-23;
const HC_EV_NM = h*c/e*1e9;                 /* 1239.84198 eV nm */
const R_SUN = 6.957e8, AU = 1.495978707e11, YEAR = 3.15576e7, T_SUN = 5772;
/* 1. random walk out of the Sun: <r^2> = N l^2, so N ~ (R/l)^2 steps and t ~ N l / c = R^2/(l c) */
const walk = l => { const N = (R_SUN/l)**2; return { N, t: R_SUN*R_SUN/(l*c), years: R_SUN*R_SUN/(l*c)/YEAR, straight: R_SUN/c }; };
/* 2. Sun to Earth */
const flight = () => ({ t: AU/c, minutes: AU/c/60, proper: 0 });
/* photon energy and momentum */
const energyEV = lam_nm => HC_EV_NM/lam_nm;
const freq = lam_nm => c/(lam_nm*1e-9);
/* 3. Snell, critical angle, evanescent 1/e depth of the field (intensity depth is half of it) */
function snell(n1, n2, th1){ const s = n1*Math.sin(th1)/n2;
  if(s <= 1) return { tir:false, th2: Math.asin(s) };
  return { tir:true, thc: Math.asin(n2/n1) }; }
const critical = (n1, n2) => n2 < n1 ? Math.asin(n2/n1) : null;
const evanescentDepth = (lam_nm, n1, n2, th1) => { const q = n1*n1*Math.sin(th1)**2 - n2*n2; return q > 0 ? lam_nm/(2*Math.PI*Math.sqrt(q)) : Infinity; };
/* Fresnel power reflectance (unpolarised) below the critical angle */
function fresnelR(n1, n2, th1){ const s = snell(n1,n2,th1); if(s.tir) return 1; const ci = Math.cos(th1), ct = Math.cos(s.th2);
  const rs = (n1*ci - n2*ct)/(n1*ci + n2*ct), rp = (n2*ci - n1*ct)/(n2*ci + n1*ct); return 0.5*(rs*rs + rp*rp); }
/* 4. double slit, Fraunhofer: I(y) = cos^2(pi d y / lam L) sinc^2(pi a y / lam L); fringe spacing lam L / d */
function slitI(y, lam, d, a, L){ const u = Math.PI*d*y/(lam*L), v = Math.PI*a*y/(lam*L); const s = Math.abs(v) < 1e-12 ? 1 : Math.sin(v)/v; return Math.cos(u)**2 * s*s; }
const fringe = (lam, d, L) => lam*L/d;
/* 5. cosmological redshift: lam_obs = (1+z) lam_emit, E_obs = E_emit/(1+z) */
const redshift = (lam_nm, z) => ({ lam: lam_nm*(1+z), E: energyEV(lam_nm)/(1+z), stretch: 1+z });
/* 6. photoelectric effect: K_max = h f - phi, threshold lam_0 = hc/phi */
const photoelectric = (lam_nm, phi) => { const E = energyEV(lam_nm); return { E, K: Math.max(0, E - phi), emits: E > phi, lam0: HC_EV_NM/phi }; };
/* 7. chlorophyll a absorption, approximate shape (two bands near 430 nm and 662 nm in solution); illustrative, not data */
const chlA = lam => 1.0*Math.exp(-0.5*((lam-430)/16)**2) + 0.78*Math.exp(-0.5*((lam-662)/11)**2) + 0.06*Math.exp(-0.5*((lam-615)/18)**2) + 0.05*Math.exp(-0.5*((lam-560)/60)**2);
/* 8. sunset: Planck spectrum of the Sun times Rayleigh transmission through the airmass at elevation h_deg */
const planck = (lam_nm, T) => { const l = lam_nm*1e-9; return 2*h*c*c/l**5 / (Math.exp(h*c/(l*kB*T)) - 1); };
const tauRayleigh = lam_nm => { const u = lam_nm/1000; return 0.008569*u**-4*(1 + 0.0113*u**-2 + 0.00013*u**-4); };   /* Hansen & Travis 1974 */
const airmass = h_deg => 1/(Math.sin(h_deg*Math.PI/180) + 0.50572*Math.pow(h_deg + 6.07995, -1.6364));               /* Kasten & Young 1989 */
function sunSpectrum(h_deg, WL){ const X = airmass(Math.max(h_deg, -0.5)); return WL.map(l => planck(l, T_SUN)*Math.exp(-tauRayleigh(l)*X)); }
const K = { c, h, e, HC_EV_NM, R_SUN, AU, YEAR, T_SUN, walk, flight, energyEV, freq, snell, critical, evanescentDepth, fresnelR, slitI, fringe, redshift, photoelectric, chlA, planck, tauRayleigh, airmass, sunSpectrum };
if(typeof module !== 'undefined') module.exports = K; else root.PHO = K;
})(this);
