"""Exact checks of ordering between the Kr-core and filled 3d10 openings."""
import argparse
from fractions import Fraction as F
from pathlib import Path
from batch9_ladder import load


def ratio_limits(record, remaining):
    k = record['Z'] - remaining
    x,y = record['thresholds'][k-1:k+1]
    a,b,da,db = (F(value) for value in (x['IE_eV'],y['IE_eV'],x['unc_eV'],y['unc_eV']))
    return (b-db)/(a+da), b/a, (b+db)/(a-da)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive',type=Path)
    args = p.parse_args()
    signs = []
    for record in load(args.archive):
        kr=ratio_limits(record,36)
        d10=ratio_limits(record,28)
        if kr[0]>d10[2]:
            relation='above'
            margin=kr[0]-d10[2]
        elif kr[2]<d10[0]:
            relation='below'
            margin=d10[0]-kr[2]
        else:
            raise ValueError('Uncertainties overlap: no robust rank decision.')
        signs.append(relation)
        print(f"{record['name']}: Kr-core opening {relation} 3d10 opening. "
              f"Worst endpoint separation {float(margin):.9f}.")
    if signs!=['above','above','below','below','below']:
        raise ValueError('Rank swap differs from molybdenum–technetium bracket.')


if __name__=='__main__':
    main()
