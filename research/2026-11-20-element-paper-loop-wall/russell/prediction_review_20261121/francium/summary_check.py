"""Regenerate tabulated results from the same arrays used by the calculations."""
import csv
import json
from pathlib import Path

folder=Path(__file__).parent
readcsv=lambda filename: list(csv.DictReader((folder/filename).open()))
readjson=lambda filename: [json.loads(s) for s in (folder/filename).read_text().splitlines()]
notes=(folder/'REVIEW.md').read_text()

def replace_table(heading,rows):
    global notes
    left,right=notes.split(heading+'\n',1)
    table,rest=right.split('\n\n',1)
    separator=table.splitlines()[0]
    notes=left+heading+'\n'+separator+'\n'+'\n'.join('| '+' | '.join(row)+' |' for row in rows)+'\n\n'+rest

holdouts=readcsv('continuation.csv')
replace_table('| Prior pair | Target | Forecast z | Archived z | Forecast IE₂ − archived IE₂ (eV) |',
    [[f"{r['input_a']}, {r['input_b']}",r['target'],f"{float(r['predicted_ratio']):.6f}",
      f"{float(r['ratio_archive']):.6f}" if r['actual_grade']=='E' else 'pending measurement',
      f"{float(r['error_eV']):+.6f}" if r['actual_grade']=='E' else 'pending'] for r in holdouts])
runs=readcsv('allelectron_summary.csv')
def ae(atom,rel,func):return next(r for r in runs if r['atom']==atom and r['rel']==str(rel) and r['functional']==func and r['dx']=='0.00625')
selected=[('Rb',2,'PBE'),('Cs',2,'PBE'),('Fr',0,'PBE'),('Fr',1,'PBE'),('Fr',2,'PBE'),('Fr',2,'PZ')]
rows=[]
for atom,rel,func in selected:
    r=ae(atom,rel,func); rows.append([f"{atom}, {['nonrelativistic','scalar-relativistic','full Dirac'][rel]} {func}",r['IE1_eV'],r['IE2_eV'],f"{float(r['ratio']):.5f}",r['upper_threshold_eV'] or '—'])
replace_table('| Atom and model | IE₁ (eV) | IE₂, lower channel (eV) | Internally calculated z | Upper channel (eV) |',rows)
rows=[]
for r in readjson('eom_runs.jsonl'):
    if r['virtual_budget']!=60:continue
    a=r['atom'];e=r['IE2_roots_eV'];wavenumber={'Rb':7374.5,'Cs':13847.3609,'Fr':None}[a]
    assert max(e[:4])-min(e[:4])<1e-5 and max(e[4:])-min(e[4:])<1e-5
    rows.append([a+'²⁺',f'{e[0]:.6f}',f'{e[4]:.6f}',f'{e[4]-e[0]:.6f}',f'{wavenumber*0.00012398419843320026:.4f}' if wavenumber else 'pending'])
assert len(rows)==3
replace_table('| Ion | EOM lower (eV) | EOM upper (eV) | EOM separation (eV) | Spectroscopic separation (eV) |',rows)
(folder/'REVIEW.md').write_text(notes)
print('Regenerated 4 continuation rows, 6 radial rows, and 3 correlated doublets from their raw arrays.')
