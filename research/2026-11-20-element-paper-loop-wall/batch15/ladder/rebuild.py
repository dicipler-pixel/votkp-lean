"""Generate batches 15 and 17 with the shared ladder kernel and separate live-ASD tables."""
import argparse
import csv
import importlib.util
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE=Path(__file__).resolve().parent
PAPER=HERE.parents[1]
SETS={15:(71,'Lu Hf Ta W Re','batch15_lu_re.csv'),17:(81,'Tl Pb Bi Po At','batch17_tl_at.csv')}

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch',type=int,choices=SETS)
    parser.add_argument('--fetch',action='store_true')
    args=parser.parse_args()
    first,symbols,filename=SETS[args.batch]
    folder=PAPER/f'batch{args.batch}/ladder'
    if args.fetch:
        pull=load('getstate',PAPER/'batch13/ladder/fetch_states.py')
        def fetch(pair):
            z,s=pair
            from urllib.parse import urlencode
            from subprocess import check_output
            from fetch_asd import datarows
            params=dict(at_num_out='on',biblio='on',e_out=0,el_name_out='on',level_out='on',seq_out='on',shells_out='on',spectra=s,unc_out='on',units=1)
            url='https://physics.nist.gov/cgi-bin/ASD/ie.pl?'+urlencode(params)
            data=datarows(check_output(['curl','-fsSL','--retry','2','--max-time','60',url]).decode())
            assert len(data)==z and data[0][2]==s and data[-1][2]=='H'
            assert all(len(row)==8 and int(row[0])==z for row in data)
            return [[z,q,*row[1:]] for q,row in enumerate(data)]
        with ThreadPoolExecutor(max_workers=3) as pool:
            tables=list(pool.map(fetch,enumerate(symbols.split(),first)))
        with (folder/'asd_states_20261121.csv').open('w',newline='') as f:
            out=csv.writer(f,lineterminator='\n')
            out.writerow(pull.FIELDS)
            for rows in tables:
                out.writerows(rows)
        return
    generator=load('shared_ladder',PAPER/'batch13/ladder/generate.py')
    # These closed-core tokens occur in heavy-element ASD output.
    from assign_openings import CORES
    CORES.update({'Yb':'[Xe]4f^{14}6s^{2}','Hg':'[Xe]4f^{14}5d^{10}6s^{2}'})
    generator.SHELLS.update({68:"4f14",78:"5d10",80:"Hg"})
    generator.COMPLETE.update({"4f14":"[Xe]4f^{14}", "5d10":"[Xe]4f^{14}5d^{10}", "Hg":"[Hg]"})
    generator.build(PAPER.parents[1]/'data/element_thresholds_20261011.json.gz',folder,
                    first=first,last=first+4,input_dir=folder,filename=filename)

if __name__=='__main__':
    main()
