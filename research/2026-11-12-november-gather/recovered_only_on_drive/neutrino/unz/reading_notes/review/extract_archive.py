from html.parser import HTMLParser
from pathlib import Path
import json
class P(HTMLParser):
 def __init__(self):
  super().__init__();self.skip=0;self.depth=0;self.cur=[];self.main=[];self.details=[];self.summary=False;self.sum=[];self.section=''
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
  if t=='section':
   self.section=dict(a).get('id','');self.main.append('\nSECTION '+self.section+'\n')
  if t=='details':
   self.depth+=1
   if self.depth==1:self.cur=[];self.sum=[]
  if t=='summary':self.summary=True
  if t in ('p','h1','h2','h3','h4','tr','li','pre','br','div'):
   (self.cur if self.depth else self.main).append('\n')
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip-=1
  if t=='summary':self.summary=False
  if t=='details':
   self.depth-=1
   if self.depth==0:self.details.append({'summary':''.join(self.sum),'section':self.section,'text':''.join(self.cur)});self.main.append('\n[Embedded: '+''.join(self.sum)+']\n')
  if t in ('p','h1','h2','h3','h4','tr','li','pre','div'):(self.cur if self.depth else self.main).append('\n')
 def handle_data(self,d):
  if self.skip:return
  if self.summary:self.sum.append(d)
  (self.cur if self.depth else self.main).append(d)
p=P();p.feed(Path('/workspace/scratch/4ea79d7a2197/upload/BLACK_HOLE_OLD_CHATS_AND_MATH_20261014(1).html').read_text())
base=Path('/workspace/scratch/4ea79d7a2197/review/archive_parts');base.mkdir(exist_ok=True)
text='\n'.join(x.strip() for x in ''.join(p.main).splitlines() if x.strip());(base/'curated.txt').write_text(text)
info=[]
for i,d in enumerate(p.details):
 (base/f'detail_{i:03}.txt').write_text(d['text']);info.append({'index':i,'summary':d['summary'],'section':d['section'],'chars':len(d['text']),'lines':len(d['text'].splitlines())})
(base/'manifest.json').write_text(json.dumps(info,indent=2));print('curated',len(text));print(json.dumps(info,indent=2))
