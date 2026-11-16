// SCRIPT: PHOTON-CORE-TEST-01  (each line states the known value it must reproduce)
const K=require('./photon_core.js'); let bad=0; const ok=(n,a,b,t)=>{const p=Math.abs(a-b)<=t*Math.max(1,Math.abs(b)); if(!p)bad++; console.log((p?'ok  ':'FAIL')+' '+n+' '+a+' vs '+b);};
ok('hc in eV nm',K.HC_EV_NM,1239.84198,1e-8);
ok('sun to earth seconds',K.flight().t,499.004784,1e-6);
ok('E(550 nm) eV',K.energyEV(550),2.254258,1e-5);
ok('glass-air critical angle deg',K.critical(1.5,1)*180/Math.PI,41.8103149,1e-7);
ok('snell 30deg 1->1.5 deg',K.snell(1,1.5,Math.PI/6).th2*180/Math.PI,19.4712206,1e-7);
ok('fresnel normal 1->1.5',K.fresnelR(1,1.5,0),0.04,1e-12);
ok('evanescent depth formula, 500 nm, n1=1.5, n2=1, 60 deg',K.evanescentDepth(500,1.5,1,Math.PI/3),500/(2*Math.PI*Math.sqrt(2.25*0.75-1)),1e-12);
ok('fringe 550nm d=0.1mm L=1m (mm)',K.fringe(550e-9,1e-4,1)*1e3,5.5,1e-12);
ok('redshift z=1 halves energy',K.redshift(500,1).E,K.energyEV(500)/2,1e-12);
ok('photoelectric threshold phi=2.3 (nm)',K.photoelectric(400,2.3).lam0,539.0617,1e-6);
ok('airmass at zenith',K.airmass(90),1.0,1e-3);
ok('airmass at 10 deg (Kasten-Young ~5.6)',K.airmass(10),5.6,0.01);
ok('Rayleigh tau at 550 nm (~0.097)',K.tauRayleigh(550),0.097,0.02);
ok('random walk years, l=1 mm (R^2/(l c))',K.walk(1e-3).years,K.R_SUN**2/(1e-3*K.c)/K.YEAR,1e-12);
console.log('walk l=1mm years',K.walk(1e-3).years.toExponential(3),' l=0.1mm',K.walk(1e-4).years.toExponential(3));
console.log('failures',bad);
