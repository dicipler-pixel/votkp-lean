"""Audit all 85 rendered affinity cells against the reviewed inputs and their evidence status."""
import csv
import gzip
import json
from decimal import Decimal as D
from html.parser import HTMLParser
from pathlib import Path

HERE=Path(__file__).resolve().parent
PAPER=HERE.parent

class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows=[]
        self.row=[]
        self.cell=None
        self.element=False
    def handle_starttag(self,tag,attrs):
        if tag=='tr':
            self.row=[]
            self.element=False
        if tag=='td':
            self.cell=[]
            if dict(attrs).get('class')=='el':
                self.element=True
    def handle_data(self,data):
        if self.cell is not None:
            self.cell.append(data)
    def handle_endtag(self,tag):
        if tag=='td':
            self.row.append(self.cell)
            self.cell=None
        if tag=='tr' and self.element:
            self.rows.append(self.row)

def csvrows(file):
    with file.open() as f:
        return list(csv.DictReader(f))
ea={}
for r in csvrows(PAPER/'batch12/chemistry/anion_chemistry_h_nd.csv'):
    ea[r['symbol']]=D(r['EA_eV'])
for b in range(13,18):
    for r in csvrows(PAPER/f'batch{b}/ladder/affinities.csv'):
        if r['EA_eV']:
            ea[r['symbol']]=D(r['EA_eV'])
with gzip.open(PAPER.parents[1]/'data/element_thresholds_20261011.json.gz','rt') as f:
    atoms=json.load(f,parse_float=D)['records']
parser=Table()
parser.feed((PAPER/'VOTKP_Element_Paper_Loop_Wall_v8_20261121.html').read_text())
assert len(parser.rows)==85 and len(ea)==67
flags={'Tc':'estimated','Dy':'estimated','Tm':'disputed','Gd':'preliminary','Pm':'theory only','Sm':'EA > 0.05','Ho':'upper limit','Er':'upper limit','Po':'preliminary','Yb':'no stable','Hg':'no established'}
for a,row in zip(atoms,parser.rows):
    z,symbol=a['Z'],a['symbol']
    assert row[0][0]==symbol and int(row[0][-1])==z
    value=' '.join(row[1])
    if symbol in ea:
        refl=(D(a['thresholds'][0]['IE_eV'])-ea[symbol])/(D(a['thresholds'][0]['IE_eV'])+ea[symbol])
        assert row[1][0]==format(D(a['thresholds'][0]['IE_eV'])/ea[symbol],'.4f'),symbol
        assert row[1][1]=='Γ '+format(refl,'.4f'),symbol
    else:
        assert 'Γ' not in value and value.strip(),symbol
    if symbol in flags:
        assert flags[symbol] in value,(symbol,value)
print('85/85 element cells, 67 numeric ratios and reflections, 18 source-graded missing values, 11 special-status controls.')
