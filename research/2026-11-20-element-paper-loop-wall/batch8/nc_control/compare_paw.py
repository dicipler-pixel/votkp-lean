"""Read replayed PAW and norm-conserving readouts, tabulate like-for-like spatial settings."""
import argparse
import csv
from pathlib import Path

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('work',type=Path)
    p.add_argument('output',type=Path);args=p.parse_args()
    with args.output.open('w',newline='') as out:
        w=csv.writer(out,lineterminator='\n')
        w.writerow(['element','mesh','real_grid','NC_B','PAW_smooth_B','NC_shell_fraction','PAW_smooth_shell_fraction','delta_NC_minus_PAW'])
        for el in ('Kr','Rb'):
            for mesh in (4,6):
                n=args.work/'projlogs'/f'{el}-{mesh}-28.txt';q=args.work/'paw_comparison'/f'{el}-{mesh}.txt'
                if not n.is_file() or not q.is_file(): continue
                a=n.read_text().strip().split(',');b=q.read_text().strip().split(',')
                if len(a)!=11 or len(b)!=11:continue
                assert a[:4]==b[:4]
                w.writerow([el,mesh,28,a[4],b[4],a[8],b[8],f'{float(a[8])-float(b[8]):.9f}'])
