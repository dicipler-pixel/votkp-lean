/* SCRIPT: PHOTON-MIXER-V2-RUN
   Runs the mixer, then adds the film-style frame: a centred white scene title with a grey subtitle over the stage,
   and the byline footer. Drops the Frame PNG button (downloads do not work on a live page). */
(function(){
"use strict";
const MIXER = window.PHX && window.PHX.MIXER;
function fail(msg){ document.body.insertAdjacentHTML('beforeend', '<div style="position:fixed;inset:0;display:grid;place-items:center;padding:24px;color:#cfd6dd;font:15px/1.5 system-ui,sans-serif;text-align:center;background:#000">'+msg+'</div>'); }
let gl = null; try { const c = document.createElement('canvas'); gl = c.getContext('webgl2') || c.getContext('webgl'); } catch(e){}
if(!window.THREE || !window.Mixer3D || !MIXER){ fail('The 3D library did not load. Reload the page; if it stays blank, the network blocked cdn.jsdelivr.net.'); return; }
if(!gl){ fail('This browser has 3D graphics (WebGL) turned off, so the scenes cannot draw. Open the page in Chrome, Safari or Firefox with hardware acceleration on.'); return; }
try { window.Mixer3D.run(MIXER); } catch(e){ fail('The mixer stopped while starting: '+String(e && e.message || e)); return; }
const png = document.getElementById('m_png'); if(png) png.remove();
const css = document.createElement('style');
css.textContent = `
.ph-title{position:fixed;left:380px;right:0;top:22px;text-align:center;pointer-events:none;z-index:2}
.ph-title h2{margin:0;font:600 30px/1.15 "Inter Tight",system-ui,sans-serif;color:#fff;letter-spacing:.01em;text-shadow:0 0 18px #000}
.ph-title p{margin:6px 0 0;font:400 15px/1.3 "Inter Tight",system-ui,sans-serif;color:#9aa3ad}
.ph-title .sec{display:block;margin-bottom:6px;font:500 11px/1 "JetBrains Mono",monospace;letter-spacing:.18em;color:#63d3ff;text-transform:uppercase}
.ph-foot{position:fixed;left:380px;right:0;bottom:12px;text-align:center;pointer-events:none;z-index:2;font:400 12px/1.3 "Inter Tight",system-ui,sans-serif;color:#7d8791}
body.clean .ph-title, body.clean .ph-foot{left:0}
@media (max-width:640px){.ph-title{left:0;top:10px}.ph-title h2{font-size:20px}.ph-foot{left:0;font-size:10px}}`;
document.head.append(css);
document.body.insertAdjacentHTML('beforeend', `<div class="ph-title" id="ph_t"><span class="sec" id="ph_s"></span><h2 id="ph_h"></h2><p id="ph_p"></p></div>
<div class="ph-foot">Jeromie Beasley · X @d1c1pler · YouTube @AtlasMemoriae · GitHub dicipler-pixel · atlas-memoriae.dicipler.workers.dev</div>`);
const tag = document.getElementById('tag');
function sync(){ const t = tag.textContent || ''; const e = MIXER.eyes.find(x => t.indexOf(x.section) >= 0) || MIXER.eyes[0];
  document.getElementById('ph_s').textContent = e.section; document.getElementById('ph_h').textContent = e.title; document.getElementById('ph_p').textContent = e.sub || ''; }
new MutationObserver(sync).observe(tag, {childList:true, characterData:true, subtree:true}); sync();
})();
