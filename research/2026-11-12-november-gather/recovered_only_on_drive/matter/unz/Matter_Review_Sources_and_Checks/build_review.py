from pathlib import Path
import html,re,json,hashlib,zipfile,shutil
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Preformatted
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parent;D=ROOT/'deliverables';D.mkdir(exist_ok=True)
for name,font in [('DV','DejaVuSans.ttf'),('DVB','DejaVuSans-Bold.ttf'),('DVM','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+font))
styles=getSampleStyleSheet()
for x in ['Title','Heading1','Heading2','Heading3','BodyText']:styles[x].fontName='DV'
styles['Title'].fontSize=25;styles['Title'].leading=30
styles['Heading1'].fontName='DVB';styles['Heading1'].fontSize=17;styles['Heading1'].leading=22;styles['Heading1'].spaceBefore=18
styles['Heading2'].fontName='DVB';styles['Heading2'].fontSize=13;styles['Heading2'].leading=17;styles['Heading2'].spaceBefore=13
styles['Heading3'].fontName='DVB';styles['Heading3'].fontSize=11;styles['Heading3'].leading=15
styles['BodyText'].fontSize=10;styles['BodyText'].leading=14.2;styles['BodyText'].spaceAfter=8
REVS=ROOT if (ROOT/'synthesis.md').exists() else ROOT/'reviews'
CODE=ROOT if (ROOT/'strengthening_checks.py').exists() else ROOT/'code'
sources=['synthesis.md','v3_review.md','combined_review.md','russell_review.md'];story=[];parts=[]
def inline(t):
 t=html.escape(t)
 t=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',t)
 t=re.sub(r'`([^`]+)`',r'\1',t)
 return t
for idx,src in enumerate(sources):
 if idx:story.append(PageBreak());parts.append('<hr><p class="kicker">Full independent reader report '+str(idx)+'</p>')
 for block in re.split(r'\n\s*\n',(REVS/src).read_text()):
  lines=block.strip().splitlines()
  if not lines:continue
  if lines[0].startswith('#'):
   for line in lines:
    if line.startswith('#'):
     level=len(line)-len(line.lstrip('#'));title=line[level:].strip();style='Title' if idx==0 and level==1 else 'Heading1' if level<=2 else 'Heading2';story.append(Paragraph(inline(title),styles[style]));parts.append(f'<h{min(level,3)}>{inline(title)}</h{min(level,3)}>')
    else:story.append(Paragraph(inline(line),styles['BodyText']));parts.append('<p>'+inline(line)+'</p>')
  else:
   # Keep list entries separate; prose paragraphs wrap naturally.
   units=lines if all(re.match(r'^(- |\d+[.)] )',x) for x in lines) else [' '.join(lines)]
   for line in units:
    story.append(Paragraph(inline(line),styles['BodyText']));parts.append('<p>'+inline(line)+'</p>')
def foot(c,d):
 c.setStrokeColor(colors.HexColor('#ccd3d8'));c.line(42,37,553,37);c.setFont('DV',8);c.setFillColor(colors.HexColor('#435665'));c.drawString(42,24,'Jeromie Beasley • Reconciled research review • 3 November 2026');c.drawRightString(553,24,str(d.page))
SimpleDocTemplate(str(D/'Matter_Reconciled_Review.pdf'),title='Matter and the atlas — reconciled review',author='Research review prepared for Jeromie Beasley',leftMargin=42,rightMargin=42,topMargin=40,bottomMargin=49).build(story,onFirstPage=foot,onLaterPages=foot)
(D/'Matter_Reconciled_Review.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Matter and the atlas — reconciled review</title><style>body{max-width:940px;padding:35px 24px;margin:auto;background:#f7f7f4;color:#172835;font:18px/1.65 Georgia,serif}h1,h2,h3{font-family:Arial,sans-serif;line-height:1.2;color:#182b40}h1{font-size:2.2em}h2{margin-top:2em}h3{margin-top:1.8em}hr{margin:4em 0;border:0;border-top:1px solid #abc}.kicker{font:14px Arial;color:#536a7b}p{overflow-wrap:anywhere}@media print{body{font-size:11pt;background:white}}</style>'+''.join(parts)+'</html>')
inputnames=['Matter_Then_On_Down_Combined_Edition.docx','Matter_All_We_Have_ed1_2026-11-03.html','matter_then_on_down_v3.pdf','Russell_Corrected_v1_2026-11-03 (1).html','matter_then_on_down_v2 (1).pdf']
inputs=(ROOT/'sources') if (ROOT/'sources').exists() else ROOT.parent/'upload';manifest={name:hashlib.sha256((inputs/name).read_bytes()).hexdigest() for name in inputnames};(ROOT/'source_hashes.json').write_text(json.dumps(manifest,indent=2))
(ROOT/'README.txt').write_text('RECONCILED REVIEW — 3 November 2026\nThe five supplied inputs are preserved byte-for-byte in sources/. Reports are in reviews/. New checks are in code/; output JSON records are included.\nRun the three Python check scripts with Python 3, numpy and scipy. No Lean compilation is claimed. To rebuild reading documents, run build_review.py from the extracted archive with reportlab and installed DejaVu fonts. It discovers reviews/ and sources/ automatically.\nOriginal source PDFs are inputs, not newly published reading deliverables. The current review PDF and HTML are separate and are not duplicated in this ZIP.\nThe previous formal reproduction ZIP, earlier source corpus, and original movie assets are not duplicated here; their supplied/current paths or names remain referenced in the reviews. This archive is the complete reproduction record for this review\'s new checks, not a replacement for those earlier source packages.\n')
with zipfile.ZipFile(D/'Matter_Review_Sources_and_Checks.zip','w',zipfile.ZIP_DEFLATED) as z:
 for n in inputnames:z.write(inputs/n,'sources/'+n)
 for n in sources:z.write(REVS/n,'reviews/'+n)
 for n in ['strengthening_protocol.txt','strengthening_checks.py','strengthening_checks.json','metric_signature_check.py','metric_signature_check.json','russell_controls.py','russell_controls.json']:z.write(CODE/n,'code/'+n)
 for n in ['build_review.py','source_hashes.json','README.txt']:z.write(ROOT/n,n)
 prev=ROOT.parent/'matter_compare/deliverables'
 for n in ['combined_checks.py','combined_results.json']:
  if (prev/n).exists():z.write(prev/n,'earlier_comparison_run/'+n)
print('PDF, HTML and ZIP created')
