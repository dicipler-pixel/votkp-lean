"""Verify the public Russell ledger package and join local translations of observables by original ID."""
import argparse
import ast
import csv
import hashlib
import re
import zipfile
from collections import Counter
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('public_zip',type=Path)
parser.add_argument('readouts_tsv',type=Path)
parser.add_argument('output',type=Path)
args = parser.parse_args()
expected = {'laws_class.py':'fe578c0f6311d1195c95ec0158d6584878c9e726aef6bd8e5f7ee9a8615ecdb0','laws_uo.py':'44c8ea8d8245493c393740070734cac5e0d10e418edbaa915cea0bfbc65a4d3e','ledger_read3.md':'acf7011e565655db9260ec4709e1197e1d7d4f894477291825026cdeb6b77c45'}
texts = {}
with zipfile.ZipFile(args.public_zip) as z:
    for filename, digest in expected.items():
        raw = z.read('russell-rebuild/ledger/'+filename)
        assert hashlib.sha256(raw).hexdigest() == digest, filename
        texts[filename] = raw.decode()
ledger={}
entries=re.findall(r'(?ms)^([GU]\d+)\s*\|\s*([^|]+?)\s*\|(.*?)(?=^[GU]\d+\s*\||^##|\Z)',texts['ledger_read3.md'].split('## THOUGHT-PROCESS MAP')[0])
for key,page,record in entries:
    pieces=re.search(r'\|\s*([ABCD](?:[/→][ABCD])*|—)\s*\|\s*([^|]+)\s*\|', record)
    assert pieces,key
    ledger[key]=[page, pieces[1], pieces[2].strip(), record[:pieces.start()].strip()]

laws=ast.literal_eval(next(x.value for x in ast.parse(texts['laws_uo.py']).body if isinstance(x,ast.Assign)))
for n, law, page in laws:
    ledger[f'L{n}']=[str(page),None,None,law]
for expr in ast.parse(texts['laws_class.py']).body:
    if not (isinstance(expr,ast.Expr) and isinstance(expr.value,ast.Call) and isinstance(expr.value.func,ast.Name) and expr.value.func.id=='c'):
        continue
    numbers,cls,grade=expr.value.args[:3]
    if isinstance(numbers, ast.Call):
        assert isinstance(numbers.func,ast.Name) and numbers.func.id=='range'
        numbers=range(*(ast.literal_eval(n) for n in numbers.args))
    else:
        numbers=ast.literal_eval(numbers)
        if isinstance(numbers,int):numbers=[numbers]
    for n in numbers:
        ledger[f'L{n}'][1:3]=[ast.literal_eval(cls),ast.literal_eval(grade)]
assert set(ledger)=={f'{prefix}{n}' for prefix,last in [('G',104),('U',282),('L',199)] for n in range(1,last+1)}
assert all(v[2] is not None for v in ledger.values())
# This spell-out is the literal candidate screen. Unambiguous element names plus topic terms.
keywords='hydrogen helium lithium beryllium boron carbon nitrogen oxygen fluorine neon sodium magnesium aluminium aluminum silicon phosphorus sulfur sulphur chlorine argon potassium calcium scandium titanium vanadium chromium manganese iron cobalt nickel copper zinc gallium germanium arsenic selenium bromine krypton rubidium strontium yttrium zirconium niobium molybdenum technetium ruthenium rhodium palladium silver cadmium indium tin antimony tellurium iodine xenon caesium cesium barium lanthanum cerium praseodymium neodymium promethium samarium europium gadolinium terbium dysprosium holmium erbium thulium ytterbium lutetium hafnium tantalum tungsten rhenium osmium iridium platinum gold thallium bismuth polonium astatine radon francium radium actinium thorium protactinium uranium'.split()
pattern=re.compile(r'\b(?:'+'|'.join(keywords)+r'|elements?|elemental|isotopes?|octaves?|periodic|valenc\w*|spectr\w*|inert gases|atomic (?:weight|number)|metals?|halogens?|nuclei|radioactiv\w*|radio-active)\b',re.I)
# Mercury and lead both have pervasive nonchemical homonyms. Supplement direct contextual hits by ID.
hits={k for k,v in ledger.items() if pattern.search(re.sub(r'\s+',' ',v[3]))}
annotated=set(); rows=[]
with args.readouts_tsv.open() as source:
    for reading in csv.DictReader(source,delimiter='\t'):
        for key in reading['ids'].split():
            page,cls,grade,_=ledger[key]
            annotated.add(key)
            rows.append([key,page,cls,grade,key in hits,*[reading[s] for s in ['readout','operation','parity','independent evidence or reason to withhold','priority evidence']]])
with (args.output/'element_crosswalk_v1.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['original_id','book_page','original_class','original_grade','literal_screen_hit','reviewed_readout','operation','parity','evidence_or_limitation','historical_priority']);w.writerows(sorted(rows,key=lambda r:({'G':0,'U':1,'L':2}[r[0][0]],int(r[0][1:]))))
print('Source counts when grouped by the first listed grade (reproduces Appendix C)')
for s in 'GUL':print(s,Counter(v[2][0] for k,v in ledger.items() if k.startswith(s)))
print('References without separate grade:',sorted(k for k,v in ledger.items() if v[2]=='—'))
print('Literal screen hits:',len(hits),'; reviewed unique IDs:',len(annotated),'; readout rows:',len(rows))
print('Unaddressed literal candidates:',sorted(hits-annotated))
print('Contextual additions:',sorted(annotated-hits))
