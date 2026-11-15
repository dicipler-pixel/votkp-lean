/* SCRIPT: iqgt_mixer_3d_v5_body_c1 — IQGT Mixer 3D v5 eyes 12 to 14 (v7.3.1 §9, §10, §12) on 3D Mixer Parts v3.
   Every number the paper prints is shown beside the number the mixer computes, labelled. */
(() => {
const M = API, V3 = (x,y,z) => new T.Vector3(x,y,z), Cr = window.Core, IQ = window.IQ;
const deg = r => r*180/Math.PI, rad = d => d*Math.PI/180;
const fx = (x, d) => (+x).toFixed(d), fe = x => (+x).toExponential(1);
const chk = (label, mixer, paper, ok) => ({label, mixer, paper, ok});
const med = a => a.slice().sort((p,q) => p-q)[a.length>>1];
const EYES = [];

/* data pasted at build time: bec.json (rows [k, eigen-image deg, subspace deg, relative gap, measured/predicted]) and bec_pair_small.json */
const BEC = {"odd vs even shots":[[1,3.68,3.68,0.494,1.056],[2,40.67,40.69,0.03,2.117],[3,40.69,5.19,0.296,0.989],[4,16.94,16.82,0.039,0.818],[5,19.23,13.96,0.058,0.705],[6,14.13,10.1,0.242,0.999],[7,30.1,29.85,0.028,0.542],[8,29.9,11.36,0.165,0.972],[9,10.46,13.92,0.134,1.019],[10,79.3,79.43,0.029,7.818],[11,78.87,12.79,0.234,0.968],[12,50.29,49.45,0.051,2.768]],"random split 1":[[1,2.94,2.94,0.467,0.95],[2,26.25,26.18,0.021,1.073],[3,26.24,5.73,0.31,1.112],[4,10.47,10.59,0.041,0.799],[5,17.65,18.07,0.063,1.078],[6,17.65,7.13,0.229,1.085],[7,38.67,38.76,0.056,2.193],[8,38.53,7.67,0.163,1.071],[9,10.29,9.7,0.129,1.117],[10,81.2,81.3,0.035,6.96],[11,80.96,11.75,0.243,0.989],[12,81.43,81.72,0.013,0.957]],"random split 2":[[1,4.0,4.0,0.487,0.981],[2,64.47,64.47,0.013,0.716],[3,64.14,8.72,0.301,0.987],[4,15.94,15.59,0.03,0.446],[5,21.12,21.51,0.058,0.991],[6,21.2,9.52,0.249,0.93],[7,9.93,9.29,0.004,0.103],[8,12.46,10.69,0.207,0.991],[9,12.43,11.36,0.103,0.938],[10,70.8,70.07,0.027,3.954],[11,68.92,14.21,0.248,0.998],[12,32.41,30.48,0.03,1.199]],"shares":[13.176,6.752,6.622,4.667,4.45,4.184,3.225,3.108,2.552,2.225,2.208,1.656]};
const PAIR = {"e2":[-1,-1,-1,-1,-2,-2,-1,0,-1,-2,-3,-3,1,2,-2,-4,-2,2,2,-2,-4,-2,2,2,-2,-5,-4,2,4,0,-6,-4,1,3,-1,-5,-4,2,4,1,-5,-5,0,2,-1,-4,-3,1,1,-1,-2,-2,-2,-1,-1,0,-1,-2,-1,0,0,-1,-4,-3,1,3,0,-5,-4,0,2,-1,-5,-3,1,4,-2,-7,-4,3,5,0,-7,-6,1,4,0,-5,-5,1,4,2,-4,-5,0,3,1,-3,-3,0,1,-1,-1,-3,-1,-1,0,0,-1,-2,-2,0,1,0,-3,-4,0,3,1,-4,-5,0,2,0,-5,-4,1,4,-2,-9,-6,4,6,-1,-10,-7,1,4,1,-5,-5,-1,3,3,-3,-5,-2,3,1,-2,-4,0,1,0,-2,-2,-2,-1,-1,0,-1,-2,-2,-1,1,0,-3,-4,0,3,1,-4,-5,-1,3,1,-6,-7,3,6,-3,-16,-11,6,10,-1,-15,-11,1,5,1,-5,-5,-1,3,3,-2,-5,-2,2,1,-2,-4,-1,0,0,-1,-2,-1,-1,0,0,-1,-2,-2,-1,1,0,-2,-4,-1,2,3,-3,-7,-3,3,3,-8,-8,5,10,-4,-25,-14,11,16,-1,-21,-15,1,6,3,-4,-6,-3,2,3,-2,-5,-3,2,2,-2,-4,-2,0,0,-1,-2,-1,-2,-1,0,-1,-2,-2,-1,2,2,-3,-4,-2,2,2,-4,-8,-3,3,1,-12,-10,8,15,-7,-42,-19,18,25,-2,-32,-21,2,8,1,-6,-7,-3,2,4,-2,-5,-3,0,2,0,-3,-2,-1,1,-1,-3,-1,-2,-1,1,1,-2,-3,-2,2,2,-2,-5,-3,1,2,-3,-9,-4,4,0,-17,-12,14,23,-10,-58,-27,26,39,-2,-45,-30,3,12,2,-8,-10,-3,1,3,0,-3,-3,0,2,1,-3,-2,-1,1,0,-1,-1,-2,-1,1,1,-2,-3,-2,1,2,-2,-5,-4,0,2,-3,-9,-3,5,-3,-23,-14,21,32,-14,-74,-36,36,52,0,-55,-37,3,14,2,-12,-12,-3,1,3,0,-3,-4,-1,2,1,-2,-2,-1,0,-1,-1,-1,-2,-2,0,1,-1,-3,-2,0,2,-2,-5,-5,-1,1,-3,-10,-2,6,-5,-27,-16,28,42,-18,-86,-44,47,71,1,-70,-48,4,18,4,-14,-13,-3,1,2,2,-3,-4,-2,3,2,-2,-3,-2,-1,0,-1,-1,-3,-2,0,1,-1,-2,-2,0,2,0,-4,-7,-3,-1,-4,-9,-1,6,-5,-32,-16,35,50,-21,-93,-48,56,82,4,-79,-58,4,20,4,-16,-13,-3,-1,1,0,-2,-5,-3,1,2,0,-2,-2,-1,0,-1,0,-1,-2,-1,1,-1,-2,-3,0,1,0,-5,-8,-3,0,-3,-8,1,7,-8,-35,-16,41,56,-22,-97,-52,65,89,5,-85,-65,4,24,6,-17,-15,-3,-1,0,0,-2,-4,-3,1,2,0,-3,-3,-1,1,-1,0,-2,-2,-1,0,-1,-2,-3,-1,1,0,-5,-8,-4,-1,-3,-5,1,7,-10,-39,-18,45,60,-24,-97,-53,68,93,7,-89,-70,5,26,7,-17,-15,-3,-1,-1,0,-2,-5,-4,0,2,0,-2,-2,-1,1,-1,0,-1,-2,-1,0,0,-1,-2,-2,-1,-1,-4,-8,-3,-1,-3,-5,2,7,-11,-40,-17,50,65,-27,-98,-54,72,95,7,-94,-73,5,30,8,-17,-15,-3,-1,-1,1,0,-5,-5,-2,1,1,-2,-3,-1,-1,-1,-1,-1,-2,-2,0,0,-1,-3,-2,-1,-1,-4,-8,-4,1,-1,-4,3,6,-12,-43,-15,56,69,-29,-98,-55,73,92,9,-95,-74,8,33,9,-17,-15,-3,-1,-1,0,-1,-5,-5,-2,1,1,-2,-3,-1,-1,1,0,-1,-1,-1,-1,1,-1,-3,-3,-1,-1,-2,-8,-5,0,-2,-4,3,5,-15,-42,-13,59,71,-30,-94,-55,73,90,7,-95,-74,8,34,9,-17,-13,-2,0,-1,-1,-1,-3,-5,-3,0,1,-2,-3,-2,-1,1,-1,-1,-1,-2,-1,1,-1,-3,-4,-2,-1,-2,-7,-6,-1,-1,-1,4,4,-18,-44,-12,62,71,-33,-92,-55,73,87,9,-95,-74,9,36,9,-17,-12,2,0,-2,-1,-1,-2,-5,-3,-1,1,-1,-2,-2,-1,1,-1,-1,-1,-2,-2,1,-1,-2,-4,-3,-1,-1,-7,-7,-2,-1,-1,4,4,-21,-45,-10,65,71,-34,-91,-55,74,86,8,-96,-74,10,37,9,-17,-13,3,0,-3,-1,-1,-2,-5,-4,-1,1,-1,-2,-2,-1,0,-1,0,-1,-2,-2,1,1,-2,-5,-5,-1,-1,-6,-7,-4,-1,1,5,4,-23,-47,-7,69,71,-37,-90,-52,75,84,8,-96,-72,12,37,7,-18,-12,3,1,-4,-2,-1,-2,-4,-5,-3,0,0,-2,-2,-2,-1,-1,0,-1,-2,-2,1,1,-2,-4,-4,-1,-1,-6,-9,-6,-2,3,6,4,-24,-47,-6,71,71,-38,-88,-51,76,82,8,-96,-71,17,37,7,-18,-12,3,0,-5,-2,0,-2,-3,-5,-3,0,0,-1,-2,-2,0,-1,0,-1,-2,-2,-1,1,-1,-4,-5,-3,-1,-4,-9,-7,-1,3,8,4,-29,-49,-4,73,72,-40,-87,-48,77,80,5,-97,-70,19,37,7,-20,-12,3,-1,-7,-4,0,-1,-3,-5,-4,0,1,-1,-2,-2,-1,-1,1,0,-2,-2,-1,1,0,-4,-7,-5,-2,-3,-7,-7,-1,5,8,3,-32,-50,-3,74,71,-44,-87,-46,75,80,4,-97,-69,20,37,6,-22,-11,4,-1,-7,-5,0,-1,-2,-3,-5,-2,1,0,-2,-2,-1,-1,1,0,-2,-3,-1,0,0,-4,-8,-5,-2,-3,-7,-7,-2,5,8,2,-34,-52,-3,77,67,-47,-89,-44,75,81,2,-98,-68,22,38,4,-25,-12,3,-1,-8,-6,-2,-1,-1,-3,-5,-2,1,-1,-2,-2,-1,-2,1,1,-2,-3,-2,0,1,-3,-7,-4,-1,-2,-6,-6,-3,3,8,2,-37,-55,0,80,67,-50,-88,-44,75,81,0,-98,-66,26,38,3,-25,-11,4,0,-7,-7,-3,-1,-2,-4,-5,-2,1,-1,-1,-2,-1,-2,0,1,-2,-2,-2,0,1,-3,-7,-5,-2,-1,-5,-8,-4,4,9,2,-39,-56,0,80,66,-52,-88,-43,75,82,-4,-98,-63,26,38,3,-26,-12,5,1,-7,-7,-3,-1,-2,-4,-4,-2,1,0,-2,-2,-1,-2,0,1,-1,-2,-2,-1,1,-2,-7,-7,-2,-1,-3,-8,-4,4,9,2,-42,-58,1,80,64,-55,-87,-41,77,81,-6,-98,-62,28,37,1,-27,-14,4,2,-6,-7,-3,-1,-1,-3,-4,-3,1,0,-1,-1,-1,-2,-1,1,-1,-2,-2,-1,1,-2,-5,-7,-2,1,-2,-7,-6,3,9,2,-41,-57,2,80,64,-57,-87,-39,77,83,-9,-99,-57,28,36,1,-27,-14,3,1,-6,-8,-4,-1,-1,-3,-4,-2,-1,-1,-1,-1,-1,-2,-1,1,0,-1,-3,-1,2,0,-5,-6,-3,-1,-1,-5,-5,3,10,2,-40,-58,2,80,62,-58,-87,-38,79,81,-13,-98,-54,28,35,-1,-27,-13,4,1,-7,-8,-4,-2,-1,-2,-2,-2,-1,-1,-1,-1,-1,-2,0,1,0,-1,-2,-1,2,0,-3,-5,-3,1,-1,-5,-5,2,11,5,-39,-58,-1,78,60,-59,-89,-37,81,81,-17,-97,-51,27,33,-3,-26,-12,3,1,-6,-7,-3,-2,-1,-2,-2,-1,-1,-1,-1,-1,-1,-2,-1,-1,0,-2,-2,-2,0,1,-2,-5,-3,1,-1,-3,-6,2,9,5,-36,-57,-2,77,59,-57,-93,-37,83,83,-19,-95,-47,26,29,-3,-24,-12,3,0,-4,-6,-3,-2,-2,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,0,0,-1,-3,-2,0,2,-1,-5,-3,1,1,-2,-4,2,9,6,-33,-55,-3,73,58,-57,-97,-37,81,81,-21,-93,-43,24,27,-2,-22,-11,1,0,-2,-4,-3,-2,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-2,-1,0,-1,-3,-2,0,1,0,-4,-4,0,1,-2,-4,1,8,6,-31,-52,-5,67,55,-55,-98,-34,80,78,-23,-90,-38,22,24,-3,-21,-11,1,0,-2,-3,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,-1,0,-1,-2,-2,0,1,0,-3,-4,-2,1,0,-2,1,7,6,-27,-47,-5,61,49,-55,-98,-30,78,74,-25,-86,-36,18,20,-2,-17,-10,0,-1,-2,-2,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,-1,-1,-2,-2,-1,1,0,-2,-3,-1,1,1,-3,-1,6,6,-23,-43,-5,52,42,-50,-96,-26,74,67,-24,-79,-31,15,16,-2,-15,-8,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,1,1,-2,-3,-1,1,1,-3,-2,4,4,-17,-35,-5,44,35,-47,-90,-21,61,54,-21,-63,-24,12,12,-3,-11,-6,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,1,1,-2,-3,-1,1,2,-3,-2,4,4,-13,-29,-6,34,29,-41,-84,-17,49,41,-18,-49,-18,9,8,-2,-8,-4,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,0,1,-2,-2,-1,1,1,-2,-3,2,4,-10,-23,-6,24,22,-34,-71,-14,36,30,-14,-36,-14,7,6,-1,-4,-3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,0,1,-1,-2,-2,1,1,-2,-2,1,3,-6,-17,-5,16,15,-24,-50,-10,24,19,-10,-25,-10,4,4,0,-3,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,-1,1,-1,-2,-2,-1,1,-1,-3,-1,1,-3,-10,-6,10,10,-14,-31,-7,14,12,-5,-15,-7,1,2,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-1,-2,-1,1,1,-1,-2,-2,0,-2,-5,-5,5,6,-7,-17,-5,8,7,-2,-5,-3,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-2,-1,1,-1,-2,-2,-1,-1,-2,-3,2,4,-3,-8,-4,3,4,0,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,1,-1,-2,-3,-2,0,-1,-2,-1,1,-2,-3,-2,-1,0,1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,1,-1,-2,-2,-2,0,-1,-2,-1,-1,-1,-2,-1,-1,-1,-1,0,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],"e3":[-1,-1,-1,-1,-1,0,1,-1,-2,-2,0,2,0,-2,-4,0,2,2,-2,-3,-1,2,1,-3,-5,-2,3,3,-3,-6,-3,3,3,-2,-5,-3,2,3,-1,-5,-3,2,3,-1,-4,-2,1,0,-1,-3,-2,0,-1,-1,-1,-2,-2,-1,0,1,-2,-3,-1,1,2,-1,-4,-2,2,2,-1,-4,-2,2,2,-3,-5,-2,4,3,-3,-8,-3,3,4,-1,-5,-4,1,4,0,-4,-3,1,4,0,-4,-3,0,1,0,-3,-2,0,0,0,0,-2,-2,-1,1,0,-1,-2,-2,2,2,-1,-5,-3,0,3,0,-4,-2,3,3,-3,-8,-3,6,5,-5,-11,-5,3,5,-1,-5,-5,1,4,1,-4,-5,0,4,1,-3,-3,0,2,0,-2,-2,-1,-1,0,-1,-2,-2,-1,1,1,-2,-3,-2,0,4,-1,-5,-3,2,3,0,-4,-4,2,3,-4,-13,-5,9,8,-6,-17,-7,4,6,0,-6,-5,1,4,2,-3,-5,-2,3,1,-2,-4,-2,2,0,-2,-2,-1,-1,1,1,-1,-2,-1,1,1,-2,-3,-3,0,3,1,-4,-4,2,4,1,-6,-4,4,5,-9,-20,-6,15,13,-9,-25,-11,7,8,0,-8,-7,0,4,2,-3,-5,-2,3,3,-2,-4,-2,2,0,-2,-2,-2,-1,0,1,-1,-2,-2,0,2,1,-3,-3,-2,3,1,-3,-5,0,4,1,-7,-3,8,7,-14,-34,-8,25,21,-14,-41,-15,10,11,-1,-10,-8,0,4,2,-2,-5,-3,2,2,-1,-4,-2,1,1,-1,-2,-1,-1,0,1,-1,-1,-2,-1,2,0,-2,-3,-2,3,2,-2,-5,0,4,1,-11,-3,12,11,-22,-49,-12,38,30,-20,-56,-22,14,16,-1,-14,-9,1,4,3,0,-5,-3,1,2,0,-3,-3,0,1,-1,-2,-2,-1,-1,0,0,-1,-2,-1,1,0,-2,-4,-2,3,3,-2,-5,0,4,0,-13,-3,16,14,-30,-65,-14,52,42,-26,-72,-29,16,20,-2,-17,-11,0,4,4,0,-4,-3,0,2,0,-3,-3,0,1,-1,-2,-2,-2,-1,0,0,-1,-3,-2,1,2,-1,-4,-3,2,4,0,-3,1,5,-1,-15,-2,21,17,-40,-78,-18,69,55,-33,-85,-40,20,26,-2,-20,-13,0,4,4,0,-3,-4,0,2,1,-2,-3,-1,0,0,-1,-2,-2,-1,0,0,-1,-2,-2,0,2,0,-3,-3,1,3,0,-2,1,5,-2,-16,-2,25,18,-47,-86,-21,78,63,-36,-94,-45,24,32,-3,-24,-15,-1,4,2,0,-2,-3,-2,2,2,-2,-3,-2,0,0,-1,-1,-2,-2,-1,1,0,-2,-2,0,2,0,-3,-3,1,4,1,-4,1,5,-4,-18,0,29,19,-54,-92,-23,85,72,-37,-97,-50,28,36,-4,-27,-17,-1,4,4,2,-1,-3,-2,0,2,-1,-3,-2,0,1,0,-2,-2,-2,-1,1,-1,-2,-2,0,2,1,-2,-2,2,4,2,-3,1,5,-6,-19,1,31,20,-56,-96,-24,91,78,-37,-98,-52,30,41,-4,-28,-16,1,5,3,2,-1,-2,-2,0,2,-1,-3,-2,0,1,1,-2,-1,-1,-1,1,0,-2,-2,-1,2,2,-1,-2,1,4,1,-2,0,3,-7,-20,2,35,22,-61,-97,-23,92,83,-38,-99,-55,33,44,-3,-31,-16,2,5,2,3,1,-2,-2,-1,2,1,-2,-2,-1,1,0,-1,-1,-2,-1,1,1,-2,-2,-1,2,2,-1,-2,-1,3,3,-2,0,2,-9,-21,3,38,23,-63,-98,-24,90,83,-37,-99,-57,34,48,-2,-33,-18,2,5,2,3,2,-1,-2,-2,2,1,-2,-3,-2,0,1,-1,-1,-2,-2,0,1,-1,-2,-1,2,2,0,-3,-2,2,2,-3,-2,1,-12,-22,4,42,21,-67,-98,-23,89,82,-38,-98,-56,37,49,-2,-33,-17,3,5,2,2,3,0,-4,-2,2,1,-2,-3,-2,0,1,-1,-1,-1,-1,-1,1,-1,-2,-2,2,4,2,-2,-2,1,1,-2,0,-1,-15,-23,6,44,20,-70,-98,-22,88,81,-40,-95,-55,41,52,-4,-33,-16,2,4,0,2,3,0,-4,-3,2,2,-1,-3,-2,0,1,0,-1,-1,-1,-1,0,1,-1,-1,2,4,2,-1,-2,1,1,-1,0,-2,-16,-21,8,46,18,-74,-97,-22,87,80,-39,-94,-55,42,54,-4,-33,-15,3,5,0,2,4,1,-4,-3,1,3,0,-2,-2,-1,1,-1,-1,-1,-2,-1,-1,0,-1,-1,1,3,2,-1,-2,-1,1,1,1,-3,-18,-23,9,49,18,-76,-97,-20,86,79,-41,-93,-55,43,54,-5,-34,-14,4,3,-1,1,5,2,-3,-3,0,2,0,-2,-2,-1,-1,-1,0,-1,-2,-1,-1,1,-1,-1,0,3,3,-2,-4,-1,1,1,1,-4,-19,-24,9,50,15,-78,-97,-19,86,78,-43,-93,-54,44,53,-6,-34,-14,4,3,-2,1,5,3,-2,-3,0,2,0,-2,-3,-2,-1,1,1,-1,-2,-2,-1,1,0,-1,0,3,4,0,-4,-2,2,4,3,-4,-23,-23,13,53,14,-79,-97,-17,85,76,-45,-90,-52,47,54,-8,-36,-14,4,2,-3,1,5,5,-2,-3,0,2,1,-2,-2,-2,-1,1,1,-1,-2,-2,-1,2,1,-1,0,3,4,2,-4,-3,0,3,3,-6,-25,-25,13,53,12,-81,-96,-16,84,76,-46,-93,-49,49,53,-10,-39,-14,6,3,-3,-2,5,5,-2,-4,-1,2,2,-2,-2,-2,-1,1,1,-1,-2,-2,-1,1,1,-1,0,2,4,2,-4,-3,1,5,5,-7,-29,-26,14,53,10,-82,-96,-14,83,76,-48,-92,-46,51,51,-11,-41,-14,7,3,-5,-2,5,5,-2,-3,-2,2,2,-1,-2,-2,-1,1,1,0,-1,-2,-2,1,2,-1,-1,1,4,3,-3,-5,0,5,5,-7,-29,-27,16,55,11,-82,-96,-12,82,75,-51,-94,-42,54,51,-13,-42,-14,6,3,-5,-2,5,4,-1,-2,-2,1,2,-1,-2,-2,-1,0,0,-1,-1,-2,-2,1,2,0,-1,0,4,4,-3,-5,-2,5,5,-7,-30,-27,17,57,9,-85,-96,-11,84,73,-51,-96,-40,53,49,-15,-42,-13,7,2,-6,-2,5,5,-1,-3,-2,1,1,-1,-2,-2,-1,0,-1,-1,-1,-3,-2,1,2,0,-1,0,5,5,-2,-6,-3,4,6,-8,-33,-29,17,57,7,-86,-96,-10,84,72,-53,-97,-38,52,48,-17,-42,-13,8,2,-6,-2,5,5,0,-3,-2,-1,1,-1,-1,-2,-1,-1,-1,1,-1,-3,-3,0,2,0,-1,0,4,4,-1,-5,-3,3,6,-7,-34,-29,17,57,7,-87,-95,-8,84,70,-55,-98,-37,54,46,-18,-43,-13,9,2,-6,-3,4,4,0,-2,-2,-1,1,-1,-1,-1,-1,-1,-1,0,-1,-3,-3,0,2,1,-1,-1,3,5,0,-4,-5,3,6,-6,-33,-30,16,57,4,-88,-95,-8,86,67,-57,-97,-33,53,43,-19,-42,-11,7,3,-5,-3,4,4,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,-2,-3,-2,1,1,-2,-2,3,4,2,-2,-3,4,6,-5,-31,-30,15,55,4,-88,-95,-7,91,65,-57,-97,-32,51,39,-19,-38,-10,7,3,-3,-3,2,2,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-2,-3,-2,1,1,-1,-1,2,4,3,-2,-3,3,6,-4,-29,-30,15,54,3,-88,-95,-6,94,63,-58,-97,-31,49,37,-19,-36,-10,7,3,-2,-2,2,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,-1,-2,-1,1,1,-1,-2,0,3,3,0,-2,3,6,-1,-25,-28,12,51,4,-86,-94,-4,97,59,-60,-95,-26,45,33,-18,-34,-9,6,4,-1,-1,2,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,-1,-2,-1,1,1,-2,-2,0,3,4,0,-2,3,6,-1,-23,-27,11,47,4,-85,-93,-3,98,56,-59,-92,-22,39,29,-16,-29,-7,6,4,0,-1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-1,-2,-2,-1,1,-1,-2,0,3,4,0,-2,1,6,0,-20,-24,11,43,5,-82,-92,-1,96,50,-57,-87,-20,35,25,-14,-26,-7,5,4,0,-1,1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,-1,1,-1,-2,-1,2,4,2,-1,1,5,2,-16,-23,8,38,5,-76,-87,0,93,46,-53,-81,-16,30,21,-13,-22,-6,5,3,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,1,-1,-2,-2,0,2,1,-1,1,4,2,-11,-19,5,30,3,-70,-81,1,81,38,-48,-72,-11,24,16,-9,-17,-3,3,0,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,1,-1,-2,-2,-1,2,1,-1,0,3,2,-9,-17,4,23,2,-62,-74,1,65,30,-40,-59,-9,18,12,-8,-12,-3,2,0,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,0,-1,-2,-1,2,2,-1,-1,2,2,-7,-14,2,18,3,-48,-58,1,48,22,-32,-43,-7,13,8,-4,-7,-2,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,-1,-2,-1,2,2,-1,-1,2,2,-3,-10,0,12,2,-33,-41,-1,33,16,-22,-29,-4,9,6,-3,-5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-2,1,1,-1,-2,-1,1,-1,-6,-1,7,1,-21,-27,-2,18,10,-12,-17,-4,4,3,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-2,-2,0,1,-1,-2,-2,0,0,-3,-1,4,1,-11,-16,-2,10,6,-5,-9,-3,2,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-1,0,1,-1,-2,-2,0,1,-2,-2,2,1,-4,-8,-2,5,4,-2,-4,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,1,-1,-2,-2,0,1,-1,-2,-1,-1,-1,-3,-2,2,2,-1,-1,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-2,-2,-1,1,-1,-2,-1,-1,-1,-2,-1,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],"w":52,"h":42};

/* ================= Act III: the room keeps its shape ================= */

/* 12. Roommates trade beds — Davis–Kahan, one vector against the cluster (§10.2, §12.1, Figure 17) */
EYES.push((() => {
  const OUTER = 3, EPS = 0.005, NG = 30, ND = 30, TAILB = deg(EPS/OUTER);
  const XL = -1.3, XW = 3.8, YB = -1.5, YH = 3.1, LX = -2.25;
  const CX = lg => XL + (lg + 2)/2*XW, CY = d => YB + (Math.log10(Math.max(d, 1e-4)) + 2.5)/4.1*YH;
  let Q = null, cloud = null, tally = 0;
  function build(){ if(cloud) return; Q = Cr.randOrth(7, Cr.rng(12012)); const r = Cr.rng(1202); cloud = [];
    for(let i=0;i<NG;i++){ const lg = -2*i/(NG-1), dl = Math.pow(10, lg);
      for(let j=0;j<ND;j++){ const x = IQ.corridorTrial(dl, OUTER, EPS, r, Q); cloud.push({lg, tip:deg(x.tip), tail:deg(x.tail), tailRad:x.tail, z:(r() - 0.5)*0.7}); } }
    tally = cloud.filter(c => c.tailRad > EPS/OUTER).length; }
  const draws = (dl, r) => Array.from({length:ND}, () => { const x = IQ.corridorTrial(dl, OUTER, EPS, r, Q); return {tip:deg(x.tip), tail:deg(x.tail), z:(r() - 0.5)*0.7}; });
  const dg = v => v < 1 ? fx(v, 3) : fx(v, 2);
  return { id:'roommates', title:'The tip and the tail: why the subspace is the observable', section:'§10.2, §12.1, Figure 17', grade:'proved', gradeLabel:'Proved (Davis–Kahan); draws computed here',
    eq:'‖sin 𝛩‖ ≤ ‖𝐸‖ / 𝛿\none vector: held by the inner gap 𝛿ᵢₙ    the cluster: held by the outer gap 𝛥ₒᵤₜ',
    text:'A seven-level operator whose three lowest levels form a cluster, separated from the other four levels by an outer gap 𝛥out = 3 (the amber slab). Each draw adds a random perturbation of norm 0.005. A single eigenvector inside the cluster (the tip) is held only by the inner gap 𝛿 to its nearest neighbour, so its turn grows as 𝛿 shrinks. The projector onto the whole cluster (the tail) is held by the outer gap, so its turn stays below ‖𝐸‖/𝛥out. Lowering the inner gap raises the rose points, while the teal points remain under the dashed bound.',
    legend:[['#4fe3c1','the three-level cluster (tail)'],['#ff6f91','one eigenvector inside it (tip)'],['#ffb547','the outer gap 𝛥out'],['#5ab0ff','the adjustable inner gap 𝛿']],
    controls:[{id:'lg', label:'Inner gap, log₁₀', min:-2, max:0, step:0.01, value:-1, fmt:v => (+v).toFixed(2) + '  (gap ' + Math.pow(10, v).toFixed(3) + ')'}],
    view:[0.42, 0.26, 6.2, 0.15], stageView:[0.42, 0.26, 7.8, 0.1],
    make(g, ctx){ build(); ctx.n = 0;
      /* the ladder of seven levels */
      ctx.rings = []; for(let i=0;i<7;i++){ const r = M.ring(0.4, PAL.dim, 0.008, 0.85); r.rotation.x = Math.PI/2; r.position.x = LX; g.add(r); ctx.rings.push(r); }
      ctx.slab = M.slab(0.95, 1, 0.95, PAL.gap, 0.09); ctx.slab.position.x = LX; g.add(ctx.slab);
      ctx.one = M.orb(0.05, PAL.tip, 6); g.add(ctx.one);
      const l1 = M.label('the cluster', '#7fd9c4', 0.18); l1.position.set(LX, YB - 0.3, 0.2); g.add(l1);
      ctx.lg = M.label('outer gap', '#c9954a', 0.18); ctx.lg.position.set(LX, 0, 0.8); g.add(ctx.lg);
      /* the log-log chart */
      const ax = 0x3a4a66; g.add(M.line([V3(XL, YB, 0), V3(XL + XW, YB, 0)], ax)); g.add(M.line([V3(XL, YB, 0), V3(XL, YB + YH, 0)], ax));
      [0.01, 0.1, 1, 10].forEach(d => { g.add(M.line([V3(XL, CY(d), 0), V3(XL + XW, CY(d), 0)], 0x22324f, 0.7)); const l = M.label(d + '°', '#7f8db0', 0.12); l.position.set(XL - 0.22, CY(d), 0); g.add(l); });
      [[-2, '0.01'], [-1, '0.1'], [0, '1']].forEach(([lg, s]) => { g.add(M.line([V3(CX(lg), YB, 0), V3(CX(lg), YB + YH, 0)], 0x1a2640, 0.6)); const l = M.label(s, '#7f8db0', 0.12); l.position.set(CX(lg), YB - 0.17, 0); g.add(l); });
      const lx = M.label('inner gap 𝛿', '#7f8db0', 0.15); lx.position.set(CX(-1), YB - 0.38, 0); g.add(lx);
      const ly = M.label('turn, degrees', '#7f8db0', 0.15); ly.position.set(XL + 0.55, YB + YH + 0.12, 0); g.add(ly);
      /* 900 precomputed trials */
      ctx.tips = M.points(cloud.length, 0.06); ctx.tails = M.points(cloud.length, 0.06);
      cloud.forEach((c, i) => { M.setPt(ctx.tips, i, V3(CX(c.lg), CY(c.tip), c.z), [0.8, 0.34, 0.46]); M.setPt(ctx.tails, i, V3(CX(c.lg), CY(c.tail), c.z), [0.2, 0.72, 0.6]); });
      M.flush(ctx.tips); M.flush(ctx.tails); g.add(ctx.tips); g.add(ctx.tails);
      /* the guides: rose, ‖E‖/δ in degrees; teal, the cluster ceiling ‖E‖/Δout */
      g.add(M.dashed([V3(CX(-2), CY(deg(EPS/0.01)), 0), V3(CX(0), CY(deg(EPS/1)), 0)], PAL.tip, 0.8));
      g.add(M.dashed([V3(XL, CY(TAILB), 0), V3(XL + XW, CY(TAILB), 0)], PAL.tail, 0.85));
      const gl1 = M.label('‖𝐸‖/𝛿', '#e88aa3', 0.14); gl1.position.set(CX(-1.75), CY(deg(EPS/Math.pow(10, -1.75))) + 0.2, 0); g.add(gl1);
      const gl2 = M.label('‖𝐸‖/𝛥out = 0.0955°', '#7fd9c4', 0.14); gl2.position.set(CX(-0.55), CY(TAILB) + 0.14, 0); g.add(gl2);
      /* the cursor and the fresh draws */
      ctx.cur = M.slab(0.03, YH, 0.95, PAL.metric, 0.07); ctx.cur.position.y = YB + YH/2; g.add(ctx.cur);
      ctx.lp = M.points(2*ND, 0.1); g.add(ctx.lp);
      ctx.o1 = M.orb(0.055, PAL.tip, 7); ctx.o2 = M.orb(0.055, PAL.tail, 7); g.add(ctx.o1); g.add(ctx.o2); ctx.t1 = M.trail(60, 0.08); ctx.t2 = M.trail(60, 0.08); g.add(ctx.t1); g.add(ctx.t2);
      const fl = M.grid(5.4, 22, 0x5ab0ff, 0.045); fl.position.y = YB - 0.05; g.add(fl);
      this.change(ctx); },
    change(ctx){ const lg = ctx.p.lg, dl = Math.pow(10, lg), r = Cr.rng(7000 + 131*(++ctx.n) + Math.round((lg + 2)*1000));
      const w = IQ.corridorOp(dl, OUTER), sc = 0.42, lo = w[0]; ctx.w = w;
      ctx.rings.forEach((rg, i) => { rg.position.y = YB + (w[i] - lo)*sc; rg.material.color.set(i < 3 ? PAL.tail : 0x6f7f9c); });
      const y2 = YB + (w[2] - lo)*sc, y3 = YB + (w[3] - lo)*sc; ctx.slab.scale.y = Math.max(0.01, y3 - y2); ctx.slab.position.y = (y2 + y3)/2; ctx.lg.position.y = (y2 + y3)/2;
      ctx.one.position.set(LX, ctx.rings[1].position.y, 0);
      ctx.live = draws(dl, r); ctx.cx = CX(lg); ctx.cur.position.x = ctx.cx;
      ctx.live.forEach((d, i) => { M.setPt(ctx.lp, 2*i, V3(ctx.cx, CY(d.tip), d.z), [1, 0.62, 0.72]); M.setPt(ctx.lp, 2*i + 1, V3(ctx.cx, CY(d.tail), d.z), [0.55, 1, 0.88]); }); M.flush(ctx.lp);
      ctx.mTip = med(ctx.live.map(d => d.tip)); ctx.mTail = med(ctx.live.map(d => d.tail)); ctx.bTip = deg(EPS/dl);
      const d0 = ctx.live[0]; ctx.o1.position.set(ctx.cx, CY(d0.tip), d0.z); ctx.o2.position.set(ctx.cx, CY(d0.tail), d0.z); M.clearTrail(ctx.t1); M.clearTrail(ctx.t2); },
    step(dt, t, ctx){ ctx.rings.forEach((rg, i) => { const s = 1 + 0.035*Math.sin(1.7*t + i*0.8); rg.scale.set(s, s, s); });
      ctx.cur.material.opacity = 0.07 + 0.02*Math.sin(2.2*t);
      const d = ctx.live[Math.floor(t*2.6) % ctx.live.length], k = 1 - Math.exp(-dt*16);
      ctx.o1.position.lerp(V3(ctx.cx, CY(d.tip), d.z), k); ctx.o2.position.lerp(V3(ctx.cx, CY(d.tail), d.z), k);
      M.pushTrail(ctx.t1, ctx.o1.position, [1, 0.44, 0.57]); M.pushTrail(ctx.t2, ctx.o2.position, [0.31, 0.89, 0.76]);
      return [['Median one-vector turn at this gap', dg(ctx.mTip) + '°', 'tip'], ['One-vector bound ‖𝐸‖/𝛿 at this gap', dg(ctx.bTip) + '°', 'tip'],
        ['Median cluster turn at this gap', dg(ctx.mTail) + '°', 'tail'], ['Cluster bound ‖𝐸‖/𝛥out', fx(TAILB, 4) + '°', 'gap'],
        ['Precomputed draws above the bound', tally + ' of ' + cloud.length, 'tail'], ['Paper prints, 900 draws', '0.08° → 7.8° (one vector), 0.04–0.05° (cluster)', 'tail']]; },
    test(){ build(); const r = Cr.rng(31), Q2 = Cr.randOrth(7, r); let worst = 0; const ms = {};
      [1, 0.01].forEach(dl => { const tips = [], tails = []; for(let i=0;i<300;i++){ const x = IQ.corridorTrial(dl, OUTER, EPS, r, Q2); tips.push(x.tip); tails.push(x.tail); worst = Math.max(worst, x.tail); } ms[dl] = {tip:med(tips), tail:med(tails)}; });
      const m = ms[0.01];
      return [chk('cluster turn, worst of 300 draws at inner gaps 1 and 0.01', fx(deg(worst), 4) + '°', '≤ 0.0955° = 0.005/3 rad (Davis–Kahan)', worst <= EPS/OUTER),
        chk('inner gap 0.01, median one-vector turn against cluster turn', 'tip ' + fx(deg(m.tip), 2) + '°, tail ' + fx(deg(m.tail), 3) + '°', 'tip ~7.8°, tail ~0.05°', m.tip > 10*m.tail),
        chk('inner gap 1, median one-vector turn', fx(deg(ms[1].tip), 3) + '°', '~0.08°', deg(ms[1].tip) > 0.04 && deg(ms[1].tip) < 0.16),
        chk('the 900 precomputed draws: cluster turns above the bound', String(tally), '0', tally === 0)]; } };
})());

/* 13. Split the crowd — measured data (§10.3–10.4, §12.3, Figures 16 and 19) */
EYES.push((() => {
  const NAMES = ['odd vs even shots', 'random split 1', 'random split 2'], NEAR = [2, 7, 10];
  const KX = k => -1.35 + (k - 1)*0.345, ZR = [-1.15, 0, 1.15], BY = -0.85, HS = 2.2/90;
  const inside = q => q[4] >= 0.93 - 1e-9 && q[4] <= 1.12 + 1e-9, resolved = q => q[3] >= 0.10 - 1e-9;
  const tally = () => { let res = 0, ok = 0; NAMES.forEach(n => BEC[n].forEach(q => { if(resolved(q)){ res++; if(inside(q)) ok++; } })); return {res, ok}; };
  const HE = [['odd/even, corrected', 6, 5.4, 10], ['odd/even, uncorrected', 5, 6.7, 10.8], ['random split, corrected', 3, 6.3, 12], ['random split, uncorrected', 8, 8.2, 12]], HX = [-1.95, -0.65, 0.65, 1.95], BH = -0.9, HH = 0.17;
  const E2 = PAIR.e2.map(v => v/99), E3 = PAIR.e3.map(v => v/99), PN = PAIR.w, PM = PAIR.h;
  const dark = [0.05, 0.09, 0.17], amb = [1, 0.71, 0.28], blu = [0.35, 0.69, 1];
  const pc = v => { const a = Math.min(1, Math.abs(v))**0.8, c = v >= 0 ? amb : blu; return [dark[0] + (c[0] - dark[0])*a, dark[1] + (c[1] - dark[1])*a, dark[2] + (c[2] - dark[2])*a]; };
  const bar2 = (w, d, c) => { const b = M.bar(w, d, c); b.material.emissiveIntensity = 0.26; b.material.opacity = 0.88; return b; };
  /* update a surface's heights and colours in place, without rebuilding its wireframe */
  const upd = (s, H, C) => { const u = s.userData, pos = u.geo.attributes.position, col = u.geo.attributes.color, n = u.N*u.M;
    for(let i=0;i<n;i++){ pos.setY(i, H(i)); const c = C(i); col.setXYZ(i, c[0], c[1], c[2]); } pos.needsUpdate = col.needsUpdate = true; u.geo.computeVertexNormals(); };
  return { id:'split', title:'Measured data: condensate and heat engine', section:'§10.3–10.4, §12.3, Figures 16 and 19', grade:'data', gradeLabel:'Measured data (public datasets)',
    eq:'measured motion / predicted motion ∈ [0.93, 1.12] at every resolved gap\n18 of 18 cuts with relative gap ≥ 0.10',
    text:'Each data set is divided into two independent halves, odd against even shots or at random, and the covariance of each half is diagonalised separately. In the condensate images, at every cut of the spectrum with relative gap at least 0.10 (a lit tile) the rank-k subspace moves between the halves as the gap formula predicts, 18 of 18. At the near-degenerate pairs (2,3), (7,8) and (10,11) (the amber arcs) a single eigen-image turns by tens of degrees between the halves, while the subspace that closes the pair holds. In the heat-engine readout the large jumps do not recur beyond chance: they are near-ties decided by shot noise.',
    legend:[['#ff6f91','one eigen-image'],['#4fe3c1','the rank-k subspace'],['#ffb547','a near-degenerate pair'],['#5ab0ff','the highlighted cut']],
    choices:[{id:'set', label:'Data set', value:'bec', options:[['bec', 'Condensate'], ['engine', 'Heat engine'], ['pair', 'Stripe pair (2, 3)']]}],
    view:[0.5, 0.5, 7.2, -0.15], stageView:[0.5, 0.5, 8.6, -0.05],
    make(g, ctx){ ctx.gC = new T.Group(); ctx.gH = new T.Group(); ctx.gP = new T.Group(); g.add(ctx.gC); g.add(ctx.gH); g.add(ctx.gP);
      const fl = M.grid(5.8, 24, 0x5ab0ff, 0.045); fl.position.y = BY - 0.03; ctx.gC.add(fl);
      /* the condensate: three splits by twelve cuts */
      NAMES.forEach((nm, r) => { const z = ZR[r], rows = BEC[nm]; const lab = M.label(nm, '#8a98b8', 0.17); lab.position.set(-2.5, BY + 0.05, z); ctx.gC.add(lab);
        rows.forEach(q => { const k = q[0], x = KX(k);
          const a = bar2(0.13, 0.13, PAL.tip), b = bar2(0.13, 0.13, PAL.tail); a.position.set(x - 0.075, BY, z); b.position.set(x + 0.075, BY, z); M.setBar(a, Math.max(0.02, q[1]*HS)); M.setBar(b, Math.max(0.02, q[2]*HS)); ctx.gC.add(a); ctx.gC.add(b);
          const good = resolved(q), tile = M.slab(0.32, 0.02, 0.3, good ? (inside(q) ? PAL.tail : PAL.tip) : 0x6f7f9c, good ? 0.6 : 0.16); tile.position.set(x, BY - 0.012, z); ctx.gC.add(tile); });
        NEAR.forEach(k => { const q1 = rows[k - 1], q2 = rows[k], x1 = KX(k) - 0.02, x2 = KX(k + 1) + 0.02, R = (x2 - x1)/2, top = Math.max(q1[1], q1[2], q2[1], q2[2])*HS + BY + 0.1, pts = [];
          for(let i=0;i<=24;i++){ const a = Math.PI*i/24; pts.push(V3((x1 + x2)/2 - R*Math.cos(a), top + 0.8*R*Math.sin(a), z)); } ctx.gC.add(M.tube(pts, 0.009, PAL.gap, 0.9)); }); });
      for(let k=1;k<=12;k++){ const l = M.label(String(k), '#5f6f8f', 0.11); l.position.set(KX(k), BY - 0.02, ZR[2] + 0.4); ctx.gC.add(l); }
      const lc = M.label('cuts of the spectrum', '#7f8db0', 0.14); lc.position.set(KX(6.5), BY - 0.02, ZR[2] + 0.72); ctx.gC.add(lc);
      ctx.cu = new T.Group(); { const fs = M.slab(0.34, 0.02, 3.3, PAL.metric, 0.3); fs.position.y = BY - 0.005; const vl = M.dashed([V3(0, BY, 0), V3(0, BY + 2.4, 0)], PAL.metric, 0.55), ob = M.orb(0.05, PAL.metric, 7); ob.position.y = BY + 2.4; ctx.cu.add(fs); ctx.cu.add(vl); ctx.cu.add(ob); }
      ctx.cu.position.x = KX(1); ctx.gC.add(ctx.cu); ctx.cx = KX(1);
      /* the heat engine: recurring jumps against chance */
      const fh = M.grid(5.8, 24, 0x5ab0ff, 0.045); fh.position.y = BH - 0.03; ctx.gH.add(fh);
      HE.forEach((h, i) => { const x = HX[i], a = bar2(0.26, 0.3, PAL.tip), b = bar2(0.26, 0.3, 0x7f8db0); a.position.set(x - 0.17, BH, 0); b.position.set(x + 0.17, BH, 0); M.setBar(a, h[1]*HH); M.setBar(b, h[2]*HH); b.material.opacity = 0.6; ctx.gH.add(a); ctx.gH.add(b);
        const mk = M.slab(0.84, 0.014, 0.36, PAL.gap, 0.6); mk.position.set(x, BH + h[3]*HH, 0); ctx.gH.add(mk); ctx.gH.add(M.tube([V3(x, BH, 0), V3(x, BH + h[3]*HH, 0)], 0.005, PAL.gap, 0.4));
        [[x - 0.17, h[1], '#e88aa3'], [x + 0.17, h[2], '#7f8db0'], [x, h[3], '#c9954a']].forEach(([lx, v, col], j) => { const nl = M.label(String(v), col, 0.12); nl.position.set(lx, BH + (j < 2 ? v : v)*HH + 0.14 + (j === 2 ? 0.08 : 0), j === 2 ? 0.3 : 0); ctx.gH.add(nl); }); const lab = M.label(h[0], '#7f8db0', 0.14); lab.position.set(x, BH - 0.1, 0.62); ctx.gH.add(lab); });
      const la = M.label('99th percentile by chance', '#c9954a', 0.14); la.position.set(0, BH + 12*HH + 0.25, 0); ctx.gH.add(la);
      ctx.hs = M.orb(0.05, 0xffffff, 6); ctx.gH.add(ctx.hs);
      /* the moving pair: two eigen-images and the stripe between them */
      const fp = M.grid(5.8, 24, 0x5ab0ff, 0.045); fp.position.y = -0.85; ctx.gP.add(fp);
      ctx.s2 = M.surface(PN, PM, -0.55, 0.55, -0.444, 0.444, 0.85); ctx.s3 = M.surface(PN, PM, -0.55, 0.55, -0.444, 0.444, 0.85); ctx.sm = M.surface(PN, PM, -1.0, 1.0, -0.808, 0.808, 0.88);
      ctx.s2.position.set(-1.85, 0, 0); ctx.s3.position.set(1.85, 0, 0); ctx.s2.userData.wire.material.opacity = ctx.s3.userData.wire.material.opacity = 0.035; ctx.sm.position.set(0, 0, 0); ctx.gP.add(ctx.s2); ctx.gP.add(ctx.s3); ctx.gP.add(ctx.sm);
      M.setSurface(ctx.s2, (a, b) => 0.45*E2[b*PN + a], (a, b) => pc(E2[b*PN + a])); M.setSurface(ctx.s3, (a, b) => 0.45*E3[b*PN + a], (a, b) => pc(E3[b*PN + a]));
      M.setSurface(ctx.sm, () => 0, () => dark); ctx.sm.userData.wire.visible = false;
      const l2 = M.label('eigen-image 2', '#7f8db0', 0.16); l2.position.set(-1.85, 0.8, 0); const l3 = M.label('eigen-image 3', '#7f8db0', 0.16); l3.position.set(1.85, 0.8, 0);
      const lm = M.label('cos 𝜑 · image 2 + sin 𝜑 · image 3', '#c9954a', 0.17); lm.position.set(0, 1.35, 0); ctx.gP.add(l2); ctx.gP.add(l3); ctx.gP.add(lm);
      const clk = M.ring(0.3, PAL.dim, 0.007, 0.8); clk.rotation.x = Math.PI/2; clk.position.set(0, -0.82, 1.55); ctx.gP.add(clk); ctx.clk = clk;
      ctx.co = M.orb(0.035, 0xffffff, 5); ctx.gP.add(ctx.co); ctx.ct = M.trail(50, 0.07); ctx.gP.add(ctx.ct);
      const lp = M.label('phase 𝜑 of the swing', '#7f8db0', 0.13); lp.position.set(0, -0.82, 2.05); ctx.gP.add(lp);
      ctx.phi = 0; this.change(ctx); },
    change(ctx){ const s = ctx.p.set; ctx.gC.visible = s === 'bec'; ctx.gH.visible = s === 'engine'; ctx.gP.visible = s === 'pair'; },
    step(dt, t, ctx){ const s = ctx.p.set;
      if(s === 'bec'){ const kf = (t*0.75) % 12, k = Math.floor(kf) + 1, tx = KX(k); ctx.cx += (tx - ctx.cx)*(1 - Math.exp(-dt*14)); ctx.cu.position.x = ctx.cx;
        const q = NAMES.map(n => BEC[n][k - 1]), ty = tally(), o = BEC[NAMES[0]][2];
        return [['Resolved cuts within 0.93–1.12', ty.ok + ' of ' + ty.res, 'tail'],
          ['Cut ' + k + ', relative gap in the three splits', q.map(x => fx(x[3], 3)).join(' · '), q.every(resolved) ? 'tail' : 'gap'],
          ['Cut ' + k + ', measured / predicted', q.map(x => fx(x[4], 3)).join(' · '), q.every(x => resolved(x) && inside(x)) ? 'tail' : 'gap'],
          ['Odd/even, cut 3: one eigen-image', fx(o[1], 2) + '°', 'tip'], ['Odd/even, cut 3: the subspace', fx(o[2], 2) + '°', 'tail'], ['Participation (paper)', '26.5 against 1,911 for noise', 'tail']]; }
      if(s === 'engine'){ const i = Math.floor(t*0.7) % 4, h = HE[i], x = HX[i]; ctx.hs.position.set(x - 0.17, BH + h[1]*HH + 0.12, 0);
        return [['Large jumps do not recur beyond chance', 'near-ties decided by shot noise', 'gap']].concat(HE.map(h2 => [h2[0], h2[1] + ' recurring · chance ' + h2[2] + ' · 99th ' + h2[3], 'tip']));
      }
      ctx.phi = (ctx.phi + dt*0.55) % (2*Math.PI); const c = Math.cos(ctx.phi), sn = Math.sin(ctx.phi);
      upd(ctx.sm, i => 0.62*(c*E2[i] + sn*E3[i]), i => pc(c*E2[i] + sn*E3[i]));
      const P = V3(Math.cos(ctx.phi)*0.3, -0.82, 1.55 + Math.sin(ctx.phi)*0.3); ctx.co.position.copy(P); M.pushTrail(ctx.ct, P, [1, 1, 1]);
      if(ctx.ov == null){ let d = 0, a = 0, b = 0; for(let i=0;i<E2.length;i++){ d += E2[i]*E3[i]; a += E2[i]*E2[i]; b += E3[i]*E3[i]; } ctx.ov = d/Math.sqrt(a*b); }
      return [['Phase 𝜑 of the swing', fx(deg(ctx.phi), 0) + '°', 'metric'], ['Overlap of images 2 and 3 (thumbnail)', fx(ctx.ov, 3), 'tail'],
        ['Paper: inside the pair, relative gap', '0.03', 'gap'], ['Paper: relative gap at the outer edge', '0.30', 'gap'], ['Paper: soliton oscillation', '2.70 Hz', 'tail']]; },
    test(){ const ty = tally(), o = BEC[NAMES[0]].find(q => q[0] === 3), he = HE.every(h => h[1] <= h[3]);
      return [chk('resolved cuts (relative gap ≥ 0.10) with measured/predicted in 0.93–1.12, three splits', ty.ok + ' of ' + ty.res, '18 of 18', ty.ok === 18 && ty.res === 18),
        chk('odd/even, cut 3: eigen-image against subspace', fx(o[1], 2) + '° vs ' + fx(o[2], 2) + '°', '40.69° vs 5.19°', Math.abs(o[1] - 40.69) < 0.005 && Math.abs(o[2] - 5.19) < 0.005),
        chk('heat engine: recurring jumps against the 99th percentile by chance', HE.map(h => h[1] + '/' + h[3]).join(', '), 'none beyond chance', he)]; } };
})());

/* 14. Fog in the room — the logarithmic derivative needs a kernel without a leak (§9, Remark 9.2) */
EYES.push((() => {
  const C0 = V3(-0.8, 0.15, 0), S = 0.95, NF = 3000, NS = 90;
  const q3 = V3(0.3, 0.55, 0.78).normalize(), q1 = V3(1, 0, 0).sub(q3.clone().multiplyScalar(q3.x)).normalize(), q2 = new T.Vector3().crossVectors(q3, q1);
  const XL = -0.62, XR = 0.62, YB = -1.5, YT = 1.5, CXe = l => XL + (l + 8)/7*(XR - XL), CYr = l => YB + (Math.max(l, -9) + 9)/9*(YT - YB);
  const NC = 36, rr = Cr.rng(14), A = new Float32Array(NF), B = new Float32Array(NF), Cc = new Float32Array(NF), P1 = new Float32Array(NF), P2 = new Float32Array(NF), P3 = new Float32Array(NF);
  for(let i=0;i<NF;i++){ let a, b; do { a = Cr.gauss(rr); } while(Math.abs(a) > 2.5); do { b = Cr.gauss(rr); } while(Math.abs(b) > 2.5); A[i] = a; B[i] = b; Cc[i] = Cr.gauss(rr); P1[i] = rr()*6.283; P2[i] = rr()*6.283; P3[i] = rr()*6.283; }
  const curve = (p1, leak) => Array.from({length:NC}, (_, i) => { const l = -8 + 7*i/(NC - 1); return {l, y:Math.log10(Math.max(1e-12, IQ.sld(p1, leak, Math.pow(10, l)).res))}; });
  return { id:'fog', title:'Mixed states and the symmetric logarithmic derivative', section:'§9, Remark 9.2', grade:'proved',
    eq:'∂𝜌 = ½{𝜌, 𝐿}     𝑔 = ⅛ Tr(𝜌{𝐿,𝐿}) (Bures)\nsolvable exactly when ∂𝜌 has no kernel–kernel block',
    text:'A rank-two density operator 𝜌 on three levels (the blue point cloud) has a one-dimensional kernel (the dashed axis). The symmetric logarithmic derivative 𝐿 is defined by ∂𝜌 = ½{𝜌, 𝐿}. It exists whenever the variation ∂𝜌 acts only within the support of 𝜌, or between the support and the kernel. If ∂𝜌 has a kernel–kernel block (the amber points along the kernel), the equation has no solution: however small the regularisation 𝛾 in (9.4) is made, the residual does not fall below the size of that block.',
    legend:[['#8fa9d8','the state 𝜌'],['#ffb547','kernel–kernel block of ∂𝜌'],['#4fe3c1','residual, solvable'],['#ff6f91','residual, no solution']],
    controls:[{id:'p1', label:'Weight on the first level', min:0.5, max:0.95, step:0.01, value:0.7, dp:2}, {id:'leak', label:'Kernel–kernel block of ∂𝜌', min:0, max:0.4, step:0.01, value:0, dp:2}],
    view:[0.5, 0.26, 6.3, 0.15], stageView:[0.5, 0.26, 8.4, 0.15],
    make(g, ctx){ ctx.fog = M.points(NF, 0.1); { const a = ctx.fog.geometry.attributes; for(let i=0;i<NF;i++){ const k = 0.2*Math.exp(-0.12*(A[i]*A[i] + B[i]*B[i])); a.color.setXYZ(i, 0.45*k + 0.04, 0.6*k + 0.05, 0.9*k + 0.06); } a.color.needsUpdate = true; } g.add(ctx.fog);
      const e1 = C0.clone().addScaledVector(q3, 2.05), e2 = C0.clone().addScaledVector(q3, -2.05);
      g.add(M.dashed([e1, e2], 0xa8b8d8, 0.9)); [-1, 1].forEach(sg => { const o = q1.clone().multiplyScalar(0.17*sg); g.add(M.dashed([e1.clone().add(o), e2.clone().add(o)], 0x56688a, 0.8)); });
      const lk = M.label('the kernel of 𝜌', '#7f8db0', 0.19); lk.position.copy(C0.clone().addScaledVector(q3, 2.4)); g.add(lk);
      const lf = M.label('the occupied subspace', '#7f9fcf', 0.17); lf.position.copy(C0.clone().addScaledVector(q1, -1.5).addScaledVector(q2, -0.95)); g.add(lf);
      ctx.sp = M.points(NS, 0.12); g.add(ctx.sp);
      /* the small floating chart: residual of the regularised equation against η */
      const cg = new T.Group(); cg.position.set(1.95, 0.05, 0); cg.rotation.y = -0.4; g.add(cg); ctx.cg = cg;
      const fr = M.slab(1.3, 3.1, 0.02, PAL.metric, 0.018); fr.position.z = -0.012; cg.add(fr);
      cg.add(M.line([V3(XL, YB, 0), V3(XR, YB, 0)], 0x3a4a66)); cg.add(M.line([V3(XL, YB, 0), V3(XL, YT, 0)], 0x3a4a66));
      [[1, 0], [0.17, -4], [-1.17, -8]].forEach(([y, l]) => cg.add(M.line([V3(XL, CYr(l), 0), V3(XR, CYr(l), 0)], 0x1a2640, 0.7)));
      [[0, '1'], [-4, '10⁻⁴'], [-8, '10⁻⁸']].forEach(([l, s]) => { const t = M.label(s, '#7f8db0', 0.1); t.position.set(XL - 0.17, CYr(l), 0); cg.add(t); });
      [[-8, '10⁻⁸'], [-1, '10⁻¹']].forEach(([l, s]) => { const t = M.label(s, '#7f8db0', 0.1); t.position.set(CXe(l), YB - 0.13, 0); cg.add(t); });
      const tx = M.label('regularisation 𝛾', '#7f8db0', 0.13); tx.position.set(0, YB - 0.33, 0); cg.add(tx); const ty = M.label('residual', '#7f8db0', 0.13); ty.position.set(XL + 0.15, YT + 0.17, 0); cg.add(ty);
      ctx.tb = M.tube([V3(), V3(0, 0.01, 0)], 0.016, PAL.tail, 0.95); cg.add(ctx.tb); ctx.pl = M.dashed([V3(XL, 0, 0), V3(XR, 0, 0)], PAL.gap, 0.7); cg.add(ctx.pl);
      ctx.bd = M.orb(0.03, 0xffffff, 5); cg.add(ctx.bd); ctx.bt = M.trail(60, 0.06); cg.add(ctx.bt);
      const fl = M.grid(5.4, 22, 0x5ab0ff, 0.04); fl.position.y = -1.7; g.add(fl);
      this.change(ctx); },
    change(ctx){ const p1 = ctx.p.p1, leak = ctx.p.leak, cv = curve(p1, leak); ctx.cv = cv;
      ctx.cpts = cv.map(c => V3(CXe(c.l), CYr(c.y), 0)); M.setTube(ctx.tb, ctx.cpts);
      ctx.res8 = IQ.sld(p1, leak, 1e-8).res; ctx.ok = ctx.res8 < 1e-5; ctx.bu = IQ.sld(p1, leak, 1e-9).bures;
      ctx.tb.material.color.set(ctx.ok ? PAL.tail : PAL.tip); ctx.pl.visible = leak > 0;
      if(leak > 0) M.setDashed(ctx.pl, [V3(XL, CYr(Math.log10(leak)), 0), V3(XR, CYr(Math.log10(leak)), 0)]);
      const n = Math.round(leak/0.4*NS); ctx.ns = n; },
    step(dt, t, ctx){ const p1 = ctx.p.p1, sa = S*Math.sqrt(p1), sb = S*Math.sqrt(1 - p1), pa = ctx.fog.geometry.attributes.position.array;
      for(let i=0;i<NF;i++){ const x = sa*A[i] + 0.05*Math.sin(0.7*t + P1[i]), y = sb*B[i] + 0.05*Math.sin(0.9*t + P2[i]), z = 0.03*Cc[i] + 0.04*Math.sin(0.8*t + P3[i]);
        pa[3*i] = C0.x + q1.x*x + q2.x*y + q3.x*z; pa[3*i + 1] = C0.y + q1.y*x + q2.y*y + q3.y*z; pa[3*i + 2] = C0.z + q1.z*x + q2.z*y + q3.z*z; }
      ctx.fog.geometry.attributes.position.needsUpdate = true;
      const sp = ctx.sp.geometry.attributes; for(let i=0;i<NS;i++){ const u = (t*0.32 + i/NS) % 1, sg = i % 2 ? 1 : -1, on = i < ctx.ns, f = on ? 1 - 0.75*u : 0, s = 0.08 + 2.0*u, w = 0.06*Math.sin(9*u + i);
        sp.position.setXYZ(i, C0.x + q3.x*sg*s + q1.x*w, C0.y + q3.y*sg*s + q1.y*w, C0.z + q3.z*sg*s + q1.z*w); sp.color.setXYZ(i, 1*f, 0.71*f, 0.28*f); }
      sp.position.needsUpdate = sp.color.needsUpdate = true;
      const u = (t*0.16) % 1.25, k = Math.min(1, u), idx = Math.round((1 - k)*(NC - 1)), c = ctx.cv[idx]; ctx.bd.position.copy(ctx.cpts[idx]); M.pushTrail(ctx.bt, ctx.cpts[idx], ctx.ok ? [0.31, 0.89, 0.76] : [1, 0.44, 0.57]);
      return [['Residual at 𝛾 = 10⁻⁸', ctx.res8 < 1e-3 ? fe(ctx.res8) : fx(ctx.res8, 4), ctx.ok ? 'tail' : 'tip'], ['Verdict', ctx.ok ? 'solvable' : 'no solution', ctx.ok ? 'tail' : 'tip'],
        ['Bures metric 𝑔', ctx.ok ? fx(ctx.bu, 4) : 'not defined', 'metric'], ['Marker at 𝛾, residual', fe(Math.pow(10, c.l)) + ', ' + fe(Math.pow(10, c.y))],
        ['Paper', 'adding a kernel–kernel block makes (9.1) unsolvable', 'tail']]; },
    test(){ const a = IQ.sld(0.7, 0, 1e-9).res, b = IQ.sld(0.7, 0.2, 1e-9).res;
      return [chk('no kernel–kernel block: residual at 𝛾 = 10⁻⁹', fe(a), 'solvable (residual falls to 0)', a < 1e-7), chk('kernel–kernel block 0.2: residual at 𝛾 = 10⁻⁹', fx(b, 6), 'unsolvable (stays at the block size, 0.2)', Math.abs(b - 0.2) < 1e-6)]; } };
})());

window.__IQGT_EYES_C1 = EYES;
})();
