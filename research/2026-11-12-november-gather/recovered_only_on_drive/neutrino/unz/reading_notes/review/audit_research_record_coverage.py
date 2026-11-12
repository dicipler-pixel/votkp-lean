"""Validate reported reading coverage; hashes establish identity, not understanding."""
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import hashlib, json

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'research_record_parts'
def read(p):return json.loads(p.read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
errors=[]
def require(ok,msg):
    if not ok:errors.append(msg)
summary=read(BASE/'extraction_summary.json');source=Path(summary['source']).read_bytes()
require(sha(source)==summary['source_sha256'],'Original HTML hash mismatch')
manifest=read(BASE/'manifest.json');queue=read(BASE/'reading_queue.json')
class PreParser(HTMLParser):
    def __init__(self):super().__init__();self.detail=0;self.in_pre=False;self.parts=[];self.record_pre=[];self.curated_pre=[]
    def handle_starttag(self,t,a):
        if t=='details':self.detail+=1
        if t=='pre':self.in_pre=True;self.parts=[]
    def handle_data(self,d):
        if self.in_pre:self.parts.append(d)
    def handle_endtag(self,t):
        if t=='pre':
            (self.record_pre if self.detail else self.curated_pre).append(''.join(self.parts));self.in_pre=False
        if t=='details':self.detail-=1
p=PreParser();p.feed(source.decode());p.close()
require(len(p.record_pre)==len(manifest)==529,'Missing or extra embedded record/PRE')
require(len(p.curated_pre)==summary['curated_pre_blocks'],'Curated PRE count mismatch')
for i,r in enumerate(manifest):
    body=(BASE/'records'/f"{r['id']}_payload.txt").read_bytes()
    require(sha(body)==r['payload_sha256'],f"Payload hash mismatch {r['id']}")
    require(body.decode()==p.record_pre[i],f"Original HTML payload mismatch {r['id']}")
    rb=Path(r['path']).read_bytes();require(sha(rb)==r['record_sha256'],f"Record hash mismatch {r['id']}")
stream=(BASE/'unique_payload_reading_stream.txt').read_text();position=0;pieces=[]
for q in queue:
    b=Path(q['path']).read_bytes();t=b.decode()
    require(sha(b)==q['sha256'],f"Chunk hash mismatch {q['index']}")
    require(len(t)==q['chars']<=24000,f"Chunk size mismatch {q['index']}")
    require(q['start']==position and q['end']==position+len(t),f"Chunk gap/overlap {q['index']}")
    require(t==stream[q['start']:q['end']],f"Stream content mismatch {q['index']}")
    position=q['end'];pieces.append(t)
require(''.join(pieces)==stream,'Complete chunk concatenation mismatch')
require(len(stream)==summary['unique_reading_stream_chars'],'Reading stream size mismatch')
expected={q['path']:q for q in queue};assigned=[];completed={};readers=[]
for i in range(1,7):
    assignment=read(BASE/f'assignment_{i}.json');my_paths={q['path'] for q in assignment['chunks']};assigned.extend(my_paths)
    require(assignment['source_sha256']==summary['source_sha256'],f'Assignment {i} source mismatch')
    ledger=ROOT/f'research_record_coverage_{i}.json';report=ROOT/f'research_record_reading_{i}.md'
    own=[]
    if ledger.exists():
        record=read(ledger);entries=record.get('coverage',record.get('completed',record.get('chunks',[])))
        for row in entries:
            path=row.get('path');status=row.get('status')
            declared_read=(status in ('fully_read','completed','read_complete') or
                           any(row.get(key) is True for key in ('read_in_full','read_complete','read_fully','completed')))
            if not declared_read:continue
            require(path in my_paths,f'Reader {i} reported unassigned path {path}')
            if path not in expected:continue
            require(row.get('sha256')==expected[path]['sha256'],f'Reader {i} recorded hash mismatch {path}')
            require(path not in completed,f'Duplicate reported reading {path}')
            completed[path]={'reader':i,'sha256':row.get('sha256'),'chars':expected[path]['chars']};own.append(path)
        if record.get('complete') is True:require(set(own)==my_paths,f'Reader {i} premature complete flag')
        if own:require(report.exists() and report.stat().st_size>0,f'Reader {i} missing reading note')
    readers.append({'reader':i,'assigned':len(my_paths),'completed':len(own),'complete':set(own)==my_paths,'report':str(report),'ledger':str(ledger)})
counts=Counter(assigned);require(set(counts)==set(expected),'Assignments omit or introduce chunks')
require(all(n==1 for n in counts.values()),'Assignments overlap')
missing=sorted(set(expected)-set(completed))
out={'complete':not errors and not missing and all(r['complete']for r in readers),'source_sha256':summary['source_sha256'],'expected_chunks':len(queue),'completed_chunks':len(completed),'expected_characters':len(stream),'completed_characters':sum(r['chars']for r in completed.values()),'readers':readers,'missing_paths':missing,'errors':errors,'completed':completed,'method':'Full reader declarations checked against assigned paths, original HTML PRE payloads, source/record/chunk SHA256 identities and continuous reading stream. Hashes prove identity and coverage bookkeeping, not scientific validity or human understanding. No scientific source program is executed.'}
(ROOT/'research_record_completion_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ('completed','missing_paths','readers')},indent=2))
