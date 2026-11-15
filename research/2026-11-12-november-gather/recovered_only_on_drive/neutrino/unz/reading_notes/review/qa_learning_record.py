"""Structural and embedded-asset QA for the self-contained reading document."""
from pathlib import Path
import base64, hashlib, json, re
from lxml import html

ROOT=Path(__file__).resolve().parent.parent
target=ROOT/'deliverables/Neutrino_Research_Reading_Record_20261030.html'
data=target.read_bytes()
doc=html.fromstring(data)
ids=doc.xpath('//@id')
assert len(ids)==len(set(ids)), 'Duplicate anchors'
broken=[a for a in doc.xpath('//a/@href') if a.startswith('#') and a[1:] not in ids]
assert not broken, broken
assert not doc.xpath('//script'), 'The record must work without executable scripts'
assert not doc.xpath('//link[@rel="stylesheet"]|//iframe|//object'), 'Unexpected external render dependency'
assert b'\x00' not in data, 'Unexpected literal NUL in final HTML'
assert not doc.xpath('//@*[starts-with(name(),"on")]'), 'Unexpected event handler'
assert not re.search(r'MATHKEEP\d+END',data.decode()), 'Unrestored mathematics placeholder'
assert all(not u.lower().startswith('javascript:') for u in doc.xpath('//a/@href'))
images=[]
for el in doc.xpath('//img'):
    src=el.get('src','')
    assert src.startswith('data:image/png;base64,'), 'Unexpected external image dependency'
    raw=base64.b64decode(src.split(',',1)[1],validate=True)
    assert raw.startswith(b'\x89PNG\r\n\x1a\n')
    assert el.get('alt')
    images.append({'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
notes=doc.xpath('//details')
assert len(notes)==34, f'Incomplete final reading notes: {len(notes)}'
result={
 'file':str(target),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
 'details':len(notes),'anchors':len(ids),'broken_local_anchors':broken,
 'embedded_images':images,'external_render_dependencies':0,
 'mathematical_expressions_preserved_as_literal_tex':len(doc.xpath('//code[@class="math"]')),
 'validation':'HTML structure, source-note inclusion, safe links, embedded PNG and anchor checks passed',
 'visual_browser_qa':'Unavailable in this runtime; browser executable was absent and its download failed. No browser-render inspection is claimed.',
}
(ROOT/'review/reading_record_qa.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
