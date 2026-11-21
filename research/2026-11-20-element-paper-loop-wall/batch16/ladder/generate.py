"""Generate the Os–Hg packet using the checked Ba–Tb numerical conventions."""
import argparse
import importlib.util
from pathlib import Path
DIR=Path(__file__).resolve().parent
def main():
    spec=importlib.util.spec_from_file_location('batch13_generator',DIR.parents[1]/'batch13/ladder/generate.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive',type=Path)
    p.add_argument('--out',type=Path,default=DIR)
    args=p.parse_args()
    module.build(args.archive,args.out,input_dir=DIR,first=76,last=80,filename='batch16_os_hg.csv')
if __name__=='__main__':
    main()
