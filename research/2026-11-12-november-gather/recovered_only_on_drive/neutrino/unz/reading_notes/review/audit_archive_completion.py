"""Verify the identity and coverage of the historical chunks reported fully read."""
from pathlib import Path
import hashlib, json

BASE=Path(__file__).resolve().parent
queue=json.loads((BASE/'archive_parts/reading_queue.json').read_text())
expected={row['path']:row for row in queue}
seen={}
assignments=[]
errors=[]
for i in range(1,7):
    assigned=json.loads((BASE/f'archive_parts/assignment_{i}.json').read_text())
    ledger=BASE/f'archive_full_coverage_{i}.json'
    result=json.loads(ledger.read_text()) if ledger.exists() else {}
    rows=result.get('coverage',result.get('completed',[]))
    if not isinstance(rows,list): rows=[]
    allowed={r['path'] for r in assigned}
    done=[]
    for row in rows:
        path=row['path']
        if path not in allowed:
            errors.append(f'Out-of-assignment path {path}')
            continue
        if path in seen:
            errors.append(f'Duplicate completion {path}')
            continue
        actual=hashlib.sha256(Path(path).read_bytes()).hexdigest()
        if row.get('sha256')!=actual:
            errors.append(f'Hash mismatch {path}')
            continue
        seen[path]={'assignment':i,'sha256':actual,'chars':expected[path]['chars'],'reader':row.get('reader',row.get('read_by','assignment reader'))}
        done.append(path)
    assignments.append({'assignment':i,'assigned':len(assigned),'completed':len(done),'complete':set(done)==allowed})

# Independently check the extraction chunk boundaries against their parent detail.
details=sorted({r['detail'] for r in queue})
for detail in details:
    rows=sorted((r for r in queue if r['detail']==detail),key=lambda r:r['char_start'])
    source=(BASE/f'archive_parts/detail_{detail:03d}.txt').read_text()
    cursor=0
    for row in rows:
        piece=Path(row['path']).read_text()
        if row['char_start']!=cursor or piece!=source[row['char_start']:row['char_end']]:
            errors.append(f'Chunk continuity mismatch {row["path"]}')
        cursor=row['char_end']
    if cursor!=len(source): errors.append(f'Incomplete parent extraction detail{detail}')

missing=sorted(set(expected)-set(seen))
audit={
 'complete':not missing and not errors,
 'scope':'All 204 previously queued full-source historical chunks; previously read curated chronology and selected sources are recorded separately in archive_reading.md.',
 'expected_chunks':len(queue),'completed_chunks':len(seen),
 'expected_characters':sum(r['chars'] for r in queue),
 'completed_characters':sum(r['chars'] for r in seen.values()),
 'assignments':assignments,'errors':errors,'missing':missing,
 'method':'Readers recorded complete text reading; this audit independently verifies chunk hashes, unique coverage and exact continuity with the preserved parent extractions. Hash verification alone is not a claim of semantic verification.',
 'completed':seen,
}
(BASE/'archive_completion_audit.json').write_text(json.dumps(audit,indent=2))
print(json.dumps({k:v for k,v in audit.items() if k not in {'completed','missing'}},indent=2))
