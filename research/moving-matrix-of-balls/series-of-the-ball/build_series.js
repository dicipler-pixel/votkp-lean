// SCRIPT: SR-BUILD-V1 — assembles The_Series_of_the_Ball_v1_20261115.html (three.js + kit verbatim from the Surprise page; LH, MM, SR, rest states, app)
const fs=require('fs'),path=require('path'),D=__dirname;
const src=fs.readFileSync(path.join(D,'..','surprise','Light_at_the_Hypersurface_Surprise_v1.html'),'utf8');
const blocks=[];let i=0;for(;;){const a=src.indexOf('<script>',i);if(a<0)break;const b=src.indexOf('</script>',a);blocks.push(src.slice(a,b+9));i=b+9;}
let html=fs.readFileSync(path.join(D,'src','shell_series.html'),'utf8');
const rep=(k,v)=>{const at=html.indexOf(k);if(at<0)throw new Error('missing '+k);html=html.slice(0,at)+v+html.slice(at+k.length);};
rep('<!--THREE-->',blocks[0]);rep('<!--KIT-->',blocks[1]);
const rest=JSON.stringify(JSON.parse(fs.readFileSync(path.join(D,'rest_series_v1.json'),'utf8')));
rep('/*MATH*/',fs.readFileSync(path.join(D,'src','lh_math.js'),'utf8')+'\n'+fs.readFileSync(path.join(D,'..','mm','mm_math_v1.js'),'utf8')+'\n'+fs.readFileSync(path.join(D,'sr_math_v1.js'),'utf8')+'\nwindow.SR_REST='+rest+';\n');
rep('/*APP*/',fs.readFileSync(path.join(D,'src','app_series.js'),'utf8'));
const out=path.join(D,'The_Series_of_the_Ball_v1_20261115.html');fs.writeFileSync(out,html);console.log('wrote',out,html.length);
