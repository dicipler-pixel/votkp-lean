"""Extract only the configuration occupations in Table A.2, La through Tb (V–VII)."""
import argparse
import csv
import re
import subprocess
from pathlib import Path

DIR = Path(__file__).resolve().parent
ATOMS = ['La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb']
ROMAN = {'V':4,'VI':5,'VII':6}


def parse(raw):
    text=' '.join(raw.split())
    if 'Table A.2.' not in text or 'Ground configurations' not in text:
        raise ValueError('Expected Table A.2 on the requested page')
    markers=list(re.finditer(r'(?<![A-Za-z])(La|Ce|Pr|Nd|Pm|Sm|Eu|Gd|Tb|Dy) (VII|VI|V)\b',text))
    data=[]
    for first,second in zip(markers,markers[1:]):
        sym,stage=first.groups()
        if sym=='Dy':
            break
        z=57+ATOMS.index(sym)
        textrow=text[first.end():second.start()]
        # All nine elements in this extract have 5p and optionally 4f
        # outside the Cd core. Read the four adjacent model columns in order.
        cols=list(re.finditer(r'5p(\d+)(?:\s+4f(\d*)\b)?',textrow))
        if len(cols)!=4:
            raise ValueError((sym,stage,textrow,cols))
        configs=[]
        for match in cols:
            n5p=int(match[1])
            n4f=0 if match[2] is None else int(match[2] or 1)
            if n5p+n4f+48 != z-ROMAN[stage]:
                raise ValueError(('electron count mismatch',sym,stage,match.group()))
            configs.append(f'[Cd]5p^{{{n5p}}}'+(f'4f^{{{n4f}}}' if n4f else ''))
        data.append([z,sym,ROMAN[stage],*configs])
    if len(data)!=27:
        raise ValueError('Expected all 27 ground configurations')
    return data


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('pdf',type=Path)
    p.add_argument('--out',type=Path,default=DIR/'table_A2.csv')
    args=p.parse_args()
    raw=subprocess.check_output(['pdftotext','-f','13','-l','13','-raw',str(args.pdf),'-'],text=True)
    with args.out.open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['Z','symbol','q','NIST_in_2024_table','Kilbane_2010','Banerjee_2023','Carvajal_2024'])
        w.writerows(parse(raw))
