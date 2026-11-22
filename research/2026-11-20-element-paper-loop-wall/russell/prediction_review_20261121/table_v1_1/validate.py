"""Validate every numeric row encoded in the derivative against the frozen data in Claude's original."""
import csv, hashlib, json, sys
from pathlib import Path
root=Path(__file__).resolve().parent
source,ledger=map(Path,sys.argv[1:3])
page=next(root.glob('*html'))
def baseline(s):
    return json.JSONDecoder().raw_decode(s.split("setTimeout(()=>{const d=",1)[1])[0]
new=page.read_text()
data=baseline(new)
assert data==baseline(source.read_text())
items=data["elements"]
afs=[e["anion"] for e in items if e["anion"]]
steps=[s for e in items for s in e["steps"]]
assert len(items)==85 and len(steps)==3570
assert sum(x["out"] for x in steps)==8
assert sum(len(e["ie"]) for e in items)==3655
assert len(afs)==65 and sum(x["out"] for x in afs)==53
assert sum(x["g2"]<.0009 for x in steps)==1562
rows=[r for r in csv.DictReader(ledger.open()) if r["k"]=="0" and r["energy_eV"]]
assert len(rows)==67 and sum(r["central_wall"]=="outside" for r in rows)==55
notes,_=json.JSONDecoder().raw_decode(new.split("const anionNote=",1)[1])
assert {e['sym'] for e in items if not e['anion']}==set(notes)
summary={e['sym']:e for e in items}
for a,b in [('O','F'),('P','S'),('As','Se'),('Sb','Te')]:
    assert summary[a]['anion']['out'] and not summary[b]['anion']['out']
assert summary['Bi']['anion']['out'] and summary['Po']['anion']==None and not summary['At']['anion']['out']
for sym in ['Ca','Sr','Ba']:assert summary[sym]['anion']['out']
print('embedded dataset identical to Claude v1: 85 elements, 3,655 energies, 3,570 ordinary pairs; eight outside')
print('v1 baseline 53/65; working-paper 55/67; evidence-linked annotations cover all 20 unscored baseline rows')
print('1,562 drawing floors confirmed; Ca/Sr/Ba membership and four observed octave steps checked')
print('HTML sha256',hashlib.sha256(page.read_bytes()).hexdigest())
