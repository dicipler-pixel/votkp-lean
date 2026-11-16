/* SCRIPT: SF-OUTSIDE-CHECK-V4 — what the raw outside data says, worked out. */
const D = require('./sf_raw_outside_v4.json'), d = Math.PI/180, eps = 23.4392911*d;
const fromEcl = (l, b) => [Math.cos(b*d)*Math.cos(l*d), Math.cos(b*d)*Math.sin(l*d), Math.sin(b*d)];
const radec = (h, m, dg, dm) => { const ra = (h + m/60)*15*d, de = Math.sign(dg || 1)*(Math.abs(dg) + dm/60)*d, x = Math.cos(de)*Math.cos(ra), y = Math.cos(de)*Math.sin(ra), z = Math.sin(de); return [x, Math.cos(eps)*y + Math.sin(eps)*z, -Math.sin(eps)*y + Math.cos(eps)*z]; };
const ang = (a, b) => Math.acos(Math.max(-1, Math.min(1, a[0]*b[0] + a[1]*b[1] + a[2]*b[2])))/d, ecl = v => [((Math.atan2(v[1], v[0])/d) + 360) % 360, Math.asin(v[2])/d];
const nose = fromEcl(D.flow.inflow_ecl_lon_deg + 180, -D.flow.inflow_ecl_lat_deg), field = fromEcl(D.field.ecl_lon_deg, D.field.ecl_lat_deg);
const v1 = radec(17, 16, 12, 5), v2 = radec(20, 6, -59, 43);
const o = {};
o.nose_ecl_sun_moves_toward = ecl(nose).map(x => +x.toFixed(2)); o.flow_moves_toward_ecl = ecl(nose.map(x => -x)).map(x => +x.toFixed(2));
o.field_to_flow_deg = +ang(field, nose).toFixed(1); o.field_to_flow_deg_other_sense = +(180 - ang(field, nose)).toFixed(1);
o.V1_ecl = ecl(v1).map(x => +x.toFixed(2)); o.V2_ecl = ecl(v2).map(x => +x.toFixed(2));
o.V1_from_nose_deg = +ang(v1, nose).toFixed(1); o.V2_from_nose_deg = +ang(v2, nose).toFixed(1); o.V1_V2_apart_deg = +ang(v1, v2).toFixed(1);
o.V1_from_field_deg = +ang(v1, field).toFixed(1); o.V2_from_field_deg = +ang(v2, field).toFixed(1);
/* pressures, pascal */
const mp = 1.6726e-27, kB = 1.380649e-23, mu0 = 4e-7*Math.PI, P_merc = 14.3e-9, a_merc = 0.387098;
const wind = r => P_merc*Math.pow(a_merc/r, 2);
o.pPa = { wind_ram_at_shock_V1_94AU: wind(94)*1e12, wind_ram_at_shock_V2_84AU: wind(84)*1e12, wind_ram_after_slowdown_94AU: wind(94)*(1 - D.wind_inside.slowdown_before_shock)*1e12 };
const Bp = nT => Math.pow(nT*1e-9, 2)/(2*mu0);
o.pPa.field_pristine_293uG = Bp(0.293)*1e12; o.pPa.field_V1_04nT = Bp(0.4)*1e12; o.pPa.field_V2_07nT = Bp(0.7)*1e12;
o.pPa.flow_ram_plasma_n004_to_012 = [0.04, 0.12].map(n => n*1e6*mp*Math.pow(25.4e3, 2)*1e12);
o.pPa.thermal_plasma_n004_to_012_T7500 = [0.04, 0.12].map(n => 2*n*1e6*kB*7500*1e12);
o.pPa.outside_total_low = o.pPa.field_pristine_293uG + o.pPa.flow_ram_plasma_n004_to_012[0] + o.pPa.thermal_plasma_n004_to_012_T7500[0];
o.pPa.outside_total_high = o.pPa.field_V2_07nT + o.pPa.flow_ram_plasma_n004_to_012[1] + o.pPa.thermal_plasma_n004_to_012_T7500[1];
/* where the Sun's wind ram alone falls to the outside total: r = a_merc sqrt(P_merc/P) */
o.balance_AU = [o.pPa.outside_total_high, o.pPa.outside_total_low].map(P => +(a_merc*Math.sqrt(P_merc/(P*1e-12))).toFixed(1));
o.shock_ratio_V1_over_V2 = +(94/84).toFixed(3); o.sheath_V2_minus_V1_AU = 36 - 28;
for(const k in o.pPa) o.pPa[k] = Array.isArray(o.pPa[k]) ? o.pPa[k].map(x => +x.toFixed(4)) : +o.pPa[k].toFixed(4);
console.log(JSON.stringify(o, null, 1)); require('fs').writeFileSync('outside_check_v4.out.json', JSON.stringify(o, null, 1));
