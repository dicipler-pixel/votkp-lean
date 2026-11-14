"""Package the completed reading record and audit trail, excluding transfer metadata."""
from pathlib import Path
import hashlib, json, re, zipfile

ROOT = Path(__file__).resolve().parent.parent
REVIEW = ROOT / 'review'
OUT = ROOT / 'deliverables'
REQUIRED = [
    'corpus_discrete_reading.md', 'corpus_gravity_reading.md',
    'corpus_geometry_reading.md', 'corpus_applications_reading.md',
    'corpus_transport_reading.md', 'corpus_boundary_music_reading.md',
]
for name in REQUIRED:
    assert (REVIEW / name).is_file(), f'Missing completed reading: {name}'
for i in range(1, 7):
    assert (REVIEW / f'archive_full_reading_{i}.md').is_file()
    assert (REVIEW / f'archive_full_coverage_{i}.json').is_file()
    assert (REVIEW / f'research_record_reading_{i}.md').is_file()
    assert (REVIEW / f'research_record_coverage_{i}.json').is_file()
for audit in ['archive_completion_audit.json', 'research_record_completion_audit.json']:
    assert json.loads((REVIEW / audit).read_text())['complete'] is True, f'Incomplete reading: {audit}'
for name in ['archive_completion.md','research_record_completion.md']:
    assert (REVIEW / name).is_file(), f'Missing final synthesis: {name}'

groups = [
    'votkp_reading.md','iqgt_reading.md','corpus_discrete_reading.md',
    'light_reading.md','upg_reading.md','corpus_applications_reading.md',
    'dirac_reading.md','corpus_applications_reading.md','corpus_gravity_reading.md',
    'nonnormality_reading.md','corpus_discrete_reading.md','corpus_boundary_music_reading.md',
    'corpus_transport_reading.md','corpus_discrete_reading.md','corpus_geometry_reading.md',
    'corpus_transport_reading.md','corpus_gravity_reading.md','corpus_applications_reading.md',
    'corpus_applications_reading.md','corpus_transport_reading.md','corpus_gravity_reading.md',
    'corpus_gravity_reading.md','corpus_geometry_reading.md','corpus_transport_reading.md',
    'corpus_transport_reading.md','corpus_geometry_reading.md','corpus_geometry_reading.md',
    'corpus_geometry_reading.md',
]
rows = []
for line in (REVIEW / 'current_papers_index_20261013_read.md').read_text().splitlines():
    m = re.match(r'- (2026-\d\d-\d\d) \| (.*?) \| version: (.*?) \| record (\d+) \| main file: (.*?) \| in Drive:', line)
    if m:
        row = dict(zip(['index_date','title','indexed_version','zenodo_record','indexed_main_file'],m.groups()))
        row['reading_note'] = groups[len(rows)]
        row['coverage'] = 'Complete scientific-text reading of this family; exact read versions, scope, and reproduction limits are specified in the note.'
        rows.append(row)
assert len(rows) == 28
(REVIEW / 'indexed_family_coverage.json').write_text(json.dumps({
    'warning':'The 13 October index identifies families, not all later versions. Consult each reading note for the actual source read. Reading is not independent proof or reproduction.',
    'families':rows},indent=2,ensure_ascii=False))

selected = set()
def add(p):
    if p.is_file() and '__pycache__' not in p.parts:
        selected.add(p)
for pattern in ['*reading.md','archive_full_reading_*.md','archive_full_addendum_*.md','archive_full_coverage_*.json','research_record_reading_*.md','research_record_addendum_*.md','*completion.md','*completion_audit.json','neutrino_verification.md','corpus_discovery.md','*connection_notes*','*synthesis_check*.txt','final_*_check.txt','*coverage*.json','inventory.json','corpus_version_inventory.json','current_papers_index_20261013_read.md','shear_stationarity_check.json','nonnormality_independent_checks.py','reading_record_qa.json']:
    for p in REVIEW.glob(pattern): add(p)
for name in ['build_learning_record.mjs','build_reading_packet.py','extract_nonnormality.py','extract_archive.py','extract_research_record.py','audit_archive_completion.py','audit_research_record_coverage.py','qa_learning_record.py','two_book_flow_check.md','two_book_flow_check.py','two_book_flow_check.json']:
    add(REVIEW / name)
for rel in ['transport_agent/source_coverage.json','transport_agent/price_kernel_algebra_check.json','discrete_sources/reading_manifest.json','geometry_agent/source_ids.json','applications_agent/source_manifest.json','gravity_agent/source_manifest.json']:
    add(REVIEW / rel)
for folder in ['neutrino_agent/rerun','votkp_agent/fresh_checks','nonnormality_checks','colour_checks','mccormick_upstream','archive_replay']:
    for p in (REVIEW / folder).rglob('*'):
        if p.suffix.lower() in {'.py','.json','.csv','.txt','.log','.md','.cff'} or p.name=='LICENSE': add(p)
for folder in ['iqgt_agent','bh_agent','geometry_agent','corpus_sources']:
    for p in (REVIEW / folder).rglob('*'):
        if any(x in p.parts for x in ['deps','site-packages','__pycache__']): continue
        if (p.suffix in {'.log'} or p.name in {'source_ids.json','source_manifest.json','independent_probes.py','davis_kahan_counterexample.json','price_kernel_algebra_check.json'}): add(p)
for name in ['manifest.json','reading_queue.json','exact_dedup_stats.json','dedup_stats.json']:
    add(REVIEW / 'archive_parts' / name)
for p in (REVIEW / 'archive_parts').glob('assignment_*.json'): add(p)
for p in (REVIEW / 'research_record_parts').glob('*.json'): add(p)
for p in (REVIEW / 'research_record_parts' / 'figures').glob('*.png'): add(p)
report = OUT / 'Neutrino_Research_Reading_Record_20261030.html'
assert report.is_file()
add(report)

readme = '''RESEARCH READING RECORD — JEROMIE BEASLEY
30 October 2026, America/Chicago

Open deliverables/Neutrino_Research_Reading_Record_20261030.html for the connected reading.
The review directory contains the complete reader notes, definitions, assumptions,
negative results, version corrections, and selected fresh verification evidence.
indexed_family_coverage.json maps the 28 indexed research families to their notes.
archive_completion_audit.json and archive_full_coverage_*.json track the historical pass.
research_record_completion_audit.json tracks the separate full Research Review source.

Scope: scientific reading of identified source versions is distinct from independent
proof, fresh simulation, and every external dataset. Read the per-source limits.
The original papers were not edited. No publication or external message was sent.
Some older notes document the first phase and its then-unread queue; the archive
completion supplement records the later pass and supersedes that queue's status.
The final Research Review supplement likewise supersedes that source's earlier
excerpt-only status. Neither supplement covers unnamed or absent original sources.

Provenance: exact source IDs, versions and hashes are retained. Historical absolute
workspace paths in notes describe the execution environment; packaged files retain
their review-relative paths where available. Original source files remain at their
linked Library/Drive locations. The raw search/transfer responses, signed URLs,
dependencies and caches are deliberately absent. This is not an all-code replication
environment. In particular, no fresh nonlinear GR threshold bisection was performed.

The upstream McCormick source excerpt is pinned to commit
41a0f83b8792b04190dd8ea99cd97dec5efe02a5 and includes its MIT license.
SHA256_MANIFEST.json covers all packaged files except itself.
'''
payloads = {'README.txt': readme.encode()}
for p in sorted(selected): payloads[str(p.relative_to(ROOT))] = p.read_bytes()
manifest = {name: {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for name,data in payloads.items()}
payloads['SHA256_MANIFEST.json']=json.dumps(manifest,indent=2).encode()
OUT.mkdir(exist_ok=True)
target = OUT / 'Neutrino_Research_Reading_Notes_and_Checks_20261030.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,data in payloads.items(): z.writestr(name,data)
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    for name,entry in manifest.items():
        assert hashlib.sha256(z.read(name)).hexdigest()==entry['sha256']
print(json.dumps({'file':str(target),'files':len(payloads),'bytes':target.stat().st_size,'integrity':'all packaged SHA256 hashes verified'}))
