# SCRIPT: BUILD-PAPER-01  (assembles the HTML with embedded plates and prints the PDF)
import base64, sys, asyncio
body=open('body.html').read()
for k in range(1,7):
    import glob
    f=glob.glob('fig/fig%d_*.png'%k)[0]
    body=body.replace('{{FIG%d}}'%k,'data:image/png;base64,'+base64.b64encode(open(f,'rb').read()).decode())
css='''
:root{--bg:#0b0f17;--ink:#e8e6df;--dim:#9aa3b2;--gold:#f2c14e;--blue:#4aa3ff;--line:#243044}
*{box-sizing:border-box} html{background:var(--bg)}
body{margin:0 auto;max-width:860px;padding:48px 28px 80px;background:var(--bg);color:var(--ink);font-family:"DejaVu Serif",Georgia,serif;font-size:17px;line-height:1.62;-webkit-print-color-adjust:exact;print-color-adjust:exact}
header{border-bottom:1px solid var(--line);padding-bottom:26px;margin-bottom:10px}
.kicker{font-family:"DejaVu Sans",Arial,sans-serif;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}
h1{font-size:44px;line-height:1.1;margin:.35em 0 .25em;color:var(--gold);font-weight:700}
.sub{font-size:20px;color:var(--ink);font-style:italic;max-width:42em}
.by{margin-top:18px;font-family:"DejaVu Sans",Arial,sans-serif;font-size:17px;color:var(--blue);font-weight:700}
.note{margin-top:8px;font-family:"DejaVu Sans",Arial,sans-serif;font-size:12.5px;color:var(--dim);max-width:52em}
h2{font-family:"DejaVu Sans",Arial,sans-serif;font-size:22px;margin:1.9em 0 .5em;color:var(--ink);break-after:avoid}
h2.part{font-size:15px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);border-top:1px solid var(--line);padding-top:26px;margin-top:3em}
p{margin:.7em 0} b{color:#fff}
.eq{text-align:center;font-size:18.5px;margin:1.05em 0;color:#fff;font-family:"DejaVu Serif",Georgia,serif}
.grade{font-family:"DejaVu Sans",Arial,sans-serif;font-size:13.5px;color:var(--dim);border-left:3px solid var(--blue);padding-left:12px;margin:1em 0}
table{border-collapse:collapse;width:100%;margin:1.1em 0;font-family:"DejaVu Sans",Arial,sans-serif;font-size:13.5px;break-inside:avoid}
th,td{border-bottom:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top} th{color:var(--gold);font-weight:700}
figure{margin:1.6em 0;break-inside:avoid} figure img{width:100%;display:block;border:1px solid var(--line)} figcaption{font-family:"DejaVu Sans",Arial,sans-serif;font-size:13px;color:var(--dim);margin-top:8px}
.refs{font-size:14.5px;color:var(--ink)} .refs li{margin:.35em 0}
@page{size:A4;margin:16mm 14mm} @media print{body{max-width:none;padding:0;font-size:11.2pt} h1{font-size:30pt} .sub{font-size:14pt}}
'''
html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Centre Is Always in Flux</title><meta name="author" content="Jeromie Beasley"><style>'+css+'</style></head><body>'+body+'</body></html>'
out='The_Centre_Is_Always_in_Flux_v1_20261124'
open(out+'.html','w').write(html)
from playwright.async_api import async_playwright
async def go():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(); await pg.goto('file:///home/claude/paper/'+out+'.html'); await pg.wait_for_timeout(600)
        await pg.pdf(path=out+'.pdf',format='A4',print_background=True,margin={'top':'16mm','bottom':'16mm','left':'14mm','right':'14mm'})
        await b.close()
asyncio.run(go()); print('built',out)
