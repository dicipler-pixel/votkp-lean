"""Regenerate the complete neutral-anchor Ho/Dy interval certificate in integer micro-eV."""
import gzip
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
archive=HERE.parents[3]/'data/element_thresholds_20261011.json.gz'
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
with gzip.open(archive,'rt') as f:
    atoms=json.load(f,parse_float=F)['records']
dy,ho=atoms[65:67]
assert (dy['symbol'],ho['symbol'])==('Dy','Ho')
def bounds(t):
    x,u=F(t['IE_eV']),F(t['unc_eV'])
    return (x-u)*10**6,(x+u)*10**6
def micro(v):
    assert v.denominator==1
    return str(v.numerator)
steps=[]
for q,(a,b) in enumerate(zip(dy['thresholds'],ho['thresholds'])):
    assert a['q']==b['q']==q
    la,ua=bounds(a)
    lb,ub=bounds(b)
    steps.append('('+micro(lb-ua)+', '+micro(ub-la)+')')
source = '''-- Generated from the pinned Ho/Dy energy and uncertainty columns with certify.py.
-- All quantities are exact integer micro-eV. Q = mass(Ho) minus mass(Dy), times c².
namespace ElementPaper.HoDyRange

abbrev Box := Int × Int

def add (a b : Box) : Box := (a.1+b.1, a.2+b.2)

theorem addEncloses (a b : Box) (u v : Int)
    (ha : a.1 ≤ u ∧ u ≤ a.2) (hb : b.1 ≤ v ∧ v ≤ b.2) :
    (add a b).1 ≤ u+v ∧ u+v ≤ (add a b).2 := by
  simp [add]
  omega

def increments : List Box :=
  [''' + ',\n   '.join(steps) + ''']

def massBounds := increments.scanl add (2862600000, 2863800000)

theorem allChargeBoxes :
    massBounds.length = 67 ∧
    (massBounds.take 57).all (fun p => decide (0 < p.1)) = true ∧
    (massBounds.drop 57).all (fun p => decide (p.2 < 0)) = true := by decide +kernel

theorem endpoints :
    massBounds[56]! = (1280245833,2622567045) ∧
    massBounds[57]! = (-5199754167,-3837432955) := by decide +kernel

end ElementPaper.HoDyRange

#print axioms ElementPaper.HoDyRange.addEncloses
#print axioms ElementPaper.HoDyRange.allChargeBoxes
#print axioms ElementPaper.HoDyRange.endpoints
'''
(HERE/'HoDyRange.lean').write_text(source)
