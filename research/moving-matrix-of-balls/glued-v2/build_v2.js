// SCRIPT: MM-GLUE-BUILD-V2 — assembles Moving_Matrix_of_Balls_Glued_v2_20261115.html
// three.js r158 and mixer3d_parts_v1 copied verbatim from Balls in One Ball, Mixer v2 (via the Surprise page); then LH, MM-MATH-V1, MM-GLUE-V1, the app.
const fs=require('fs'),path=require('path');
const src=fs.readFileSync(path.join(__dirname,'..','surprise','Light_at_the_Hypersurface_Surprise_v1.html'),'utf8');
const blocks=[];let i=0;for(;;){const a=src.indexOf('<script>',i);if(a<0)break;const b=src.indexOf('</script>',a);blocks.push(src.slice(a,b+9));i=b+9;}
if(!blocks[1].includes('mixer3d_parts_v1'))throw new Error('layout');
let html=fs.readFileSync(path.join(__dirname,'src','shell_v2.html'),'utf8');
const rep=(k,v)=>{if(!html.includes(k))throw new Error('missing '+k);const at=html.indexOf(k);html=html.slice(0,at)+v+html.slice(at+k.length);};
rep('<!--THREE-->',blocks[0]);rep('<!--KIT-->',blocks[1]);
const math=fs.readFileSync(path.join(__dirname,'src','lh_math.js'),'utf8')+'\n'+fs.readFileSync(path.join(__dirname,'..','mm','mm_math_v1.js'),'utf8')+'\n'+fs.readFileSync(path.join(__dirname,'mm_glue_v1.js'),'utf8');
rep('/*MATH*/',math);rep('/*APP*/',fs.readFileSync(path.join(__dirname,'src','app_v2.js'),'utf8'));
const out=path.join(__dirname,'Moving_Matrix_of_Balls_Glued_v2_20261115.html');fs.writeFileSync(out,html);console.log('wrote',out,html.length);
