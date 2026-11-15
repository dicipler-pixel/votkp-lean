from html.parser import HTMLParser
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, json, re

BASE=Path('/workspace/scratch/4ea79d7a2197/review/research_record_parts')
SRC=Path('/workspace/scratch/4ea79d7a2197/review/research_record_source/Research_Review_and_Record.html')
BASE.mkdir(exist_ok=True)
for name in ['records','chunks','figures']: (BASE/name).mkdir(exist_ok=True)
def sha(s): return hashlib.sha256(s.encode() if isinstance(s,str) else s).hexdigest()
class Node:
    def __init__(self,tag,attrs=None,pos=None): self.tag=tag;self.attrs=dict(attrs or []);self.pos=pos;self.children=[];self.end=None
class Tree(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True);self.root=Node('root');self.stack=[self.root];self.nodes=[]
    def handle_starttag(self,t,a):
        n=Node(t,a,self.getpos());self.stack[-1].children.append(n);self.nodes.append(n)
        if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(n)
    def handle_startendtag(self,t,a): self.handle_starttag(t,a);self.handle_endtag(t)
    def handle_endtag(self,t):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==t:self.stack[i].end=self.getpos();self.stack=self.stack[:i];break
    def handle_data(self,d):self.stack[-1].children.append(d)
def children(n,t):return [z for z in walk(n) if z.tag==t]
def walk(n):
    yield n
    for c in n.children:
        if isinstance(c,Node):yield from walk(c)
def raw(n):return ''.join(c if isinstance(c,str) else raw(c) for c in n.children)
blocks={'p','div','section','article','main','h1','h2','h3','h4','h5','h6','li','ul','ol','tr','table','blockquote','figure','figcaption','summary','small'}
details_ids={}
def visible(n,skip_details=False):
    if n.tag in {'style','script','button','input','meta','title'}:return ''
    if n.tag=='details' and skip_details:return '\n[Source record '+details_ids[id(n)]+': '+raw(children(n,'summary')[0])+']\n'
    if n.tag=='pre':return '\n[BEGIN VERBATIM PRE]\n'+raw(n)+'\n[END VERBATIM PRE]\n'
    if n.tag=='img':return '\n[Figure alt: '+n.attrs.get('alt','')+']\n'
    if n.tag=='br':return '\n'
    if n.tag in {'td','th'}:return '\t'+''.join(c if isinstance(c,str) else visible(c,skip_details) for c in n.children)
    s=''.join(c if isinstance(c,str) else visible(c,skip_details) for c in n.children)
    return '\n'+s+'\n' if n.tag in blocks else s

b=SRC.read_bytes();text=b.decode('utf-8');p=Tree();p.feed(text);p.close()
details=[z for z in p.nodes if z.tag=='details'];pre=[z for z in p.nodes if z.tag=='pre']
for i,n in enumerate(details):details_ids[id(n)]=f'record_{i:03}'
curated=visible(p.root,True)
(BASE/'curated.txt').write_text(curated)
manifest=[];payload_seen={};duplicates=[];all_parts=[curated];unique_parts=[curated];unique_ranges=[]
at=len(curated);unique_ranges.append({'id':'curated','start':0,'end':at})
for i,n in enumerate(details):
    ident=details_ids[id(n)];summ=children(n,'summary');smalls=children(n,'small');pres=children(n,'pre')
    title=raw(summ[0]) if summ else '';meta='\n'.join(raw(z) for z in smalls);payload='\n'.join(raw(z) for z in pres)
    rendered=visible(n)
    # Payload identity is exact after HTML entity decoding. No whitespace normalization.
    bodyhash=sha(payload);duplicate=payload_seen.get(bodyhash)
    payload_seen.setdefault(bodyhash,ident)
    row={'id':ident,'category':'helper' if i<67 else 'note' if i<169 else 'script','title':title,'source_metadata':meta,'html_start':n.pos,'html_end':n.end,'pre_count':len(pres),'payload_chars':len(payload),'payload_sha256':bodyhash,'record_chars':len(rendered),'record_sha256':sha(rendered),'exact_payload_duplicate_of':duplicate,'path':str(BASE/'records'/f'{ident}.txt')}
    Path(row['path']).write_text(rendered);(BASE/'records'/f'{ident}_payload.txt').write_text(payload)
    manifest.append(row)
    header='\n\n===== BEGIN '+ident+' | '+title+' =====\n'+meta+'\n'
    ending='\n===== END '+ident+' =====\n'
    full=header+rendered+ending;all_parts.append(full)
    if duplicate:
        duplicates.append({'id':ident,'duplicate_of':duplicate,'payload_sha256':bodyhash,'payload_chars':len(payload)})
        part=header+'[EXACT PAYLOAD REPEAT OF '+duplicate+'; original record metadata retained here]\n'+ending
    else:part=full
    unique_parts.append(part);unique_ranges.append({'id':ident,'start':at,'end':at+len(part),'duplicate_of':duplicate});at+=len(part)
fullstream=''.join(all_parts);stream=''.join(unique_parts)
(BASE/'full_record_stream.txt').write_text(fullstream);(BASE/'unique_payload_reading_stream.txt').write_text(stream)
queue=[];start=0;i=0
while start<len(stream):
    end=min(start+24000,len(stream))
    if end<len(stream):
        candidate=stream.rfind('\n',start+18000,end)
        if candidate>start:end=candidate+1
    content=stream[start:end];path=BASE/'chunks'/f'chunk_{i:03}.txt';path.write_text(content)
    queue.append({'index':i,'path':str(path),'start':start,'end':end,'chars':len(content),'sha256':sha(content),'source_records':[r['id'] for r in unique_ranges if r['end']>start and r['start']<end]})
    start=end;i+=1
script_nodes=[z for z in p.nodes if z.tag=='script']
for i,z in enumerate(script_nodes):(BASE/f'html_script_{i:03}.txt').write_text(raw(z))
# Save supplied figures unchanged for later visual readers.
import base64
figures=[]
for i,z in enumerate(z for z in p.nodes if z.tag=='img'):
    src=z.attrs.get('src','');row={'index':i,'alt':z.attrs.get('alt',''),'position':z.pos}
    if src.startswith('data:') and ';base64,' in src:
        mime,data=src.split(';base64,',1);ext='png' if 'png'in mime else 'jpg';blob=base64.b64decode(data);dest=BASE/'figures'/f'figure_{i:02}.{ext}';dest.write_bytes(blob);row.update(path=str(dest),bytes=len(blob),sha256=sha(blob))
    figures.append(row)
category_counts=Counter(r['category'] for r in manifest)
metrics={'source':str(SRC),'library_file_id':'libfile_1e7121d745188191807ede339f740e57','source_bytes':len(b),'source_characters':len(text),'source_lines':len(text.splitlines()),'source_sha256':sha(b),'reading_status':'EXTRACTED ONLY; not read by this process','records':len(manifest),'categories':dict(category_counts),'pre_blocks':len(pre),'curated_pre_blocks':len(pre)-sum(r['pre_count']for r in manifest),'math_annotation_tags':sum(z.tag=='annotation' for z in p.nodes),'svg_tags':sum(z.tag=='svg' for z in p.nodes),'curated_chars':len(curated),'payload_chars_all':sum(r['payload_chars']for r in manifest),'unique_payload_count':len(payload_seen),'unique_payload_chars':sum(r['payload_chars']for r in manifest if not r['exact_payload_duplicate_of']),'exact_repeat_payload_count':len(duplicates),'exact_repeat_payload_chars':sum(d['payload_chars']for d in duplicates),'full_record_stream_chars':len(fullstream),'unique_reading_stream_chars':len(stream),'chunk_count':len(queue),'max_chunk_chars':max(q['chars']for q in queue),'html_script_blocks':[{'attrs':z.attrs,'chars':len(raw(z)),'sha256':sha(raw(z))}for z in script_nodes],'figures':figures,'deduplication_scope':'Only exact entity-decoded PRE payload equality inside this HTML; no whitespace normalization, semantic deduplication, or cross-archive equivalence. All original record metadata and exact source bytes retained.','extraction_method':'HTMLParser preserves data and entity-decodes once. Each PRE payload preserves all whitespace and mathematical/code characters. Plain scientific formulas are retained literally; no MathML or annotation tags are present. Buttons/frontend style/script excluded from scientific reading stream; frontend script separately saved.'}
for name,value in [('manifest.json',manifest),('exact_duplicates.json',duplicates),('source_ranges.json',unique_ranges),('reading_queue.json',queue),('extraction_summary.json',metrics)]: (BASE/name).write_text(json.dumps(value,indent=2,ensure_ascii=False))
assert ''.join(Path(q['path']).read_text() for q in queue)==stream
assert sum(q['chars'] for q in queue)==len(stream)
assert sum(r['pre_count']for r in manifest)==529
print(json.dumps(metrics,indent=2,ensure_ascii=False))
