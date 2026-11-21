"""Check every candidate sign subset with independent integer difference constraints."""
import csv
from fractions import Fraction as F
from itertools import product
from math import lcm
from pathlib import Path

DIR=Path(__file__).resolve().parent


def read(name):
    with (DIR/name).open() as f:
        return list(csv.DictReader(f))


def enumerate_signs(lo,hi):
    n=len(lo)
    den=lcm(*(x.denominator for x in lo+hi))
    unit=den*(n+1)
    # A strictly positive difference between rational box endpoints is >=1/den.
    # A directed path has <=n-1 edges, so spacing strict comparisons by 1/unit
    # preserves every feasible strict comparison and fits in the smallest positive slack.
    low=[int(x*unit) for x in lo]
    high=[int(x*unit) for x in hi]
    candidates=[i for i in range(n-1) if hi[i]>lo[i+1]]
    count=0
    max_n=0
    # Restrict the two sweeps to the variable region plus the fixed tails. Those
    # tails need no iteration: compute exactly what their directed edges impose.
    left=candidates[0]
    right=candidates[-1]+1
    low[left]=max(low[:left+1])
    high[right]=min(high[right:])
    low=low[left:right+1]
    high=high[left:right+1]
    m=len(low)
    reverse=[False]*(m-1)
    for chosen in product((False,True),repeat=len(candidates)):
        for i,flag in zip(candidates,chosen):
            reverse[i-left]=flag
        v=low.copy()
        for i,desc in enumerate(reverse):
            if not desc and v[i]>v[i+1]:
                v[i+1]=v[i]
        for i in range(m-2,-1,-1):
            if reverse[i] and v[i]<=v[i+1]:
                v[i]=v[i+1]+1
        if all(x<=u for x,u in zip(v,high)):
            count+=1
            max_n=max(sum(chosen),max_n)
    return 2**len(candidates),count,max_n


if __name__=='__main__':
    asd=read('asd_states_20261121.csv')
    summary=read('joint_direction.csv')
    total=0
    for record in summary:
        data=[r for r in asd if r['Z']==record['Z']]
        E=[F(r['NIST_energy_eV'].strip('[]()')) for r in data]
        U=[F(r['NIST_unc_eV']) for r in data]
        lo=[e-u for e,u in zip(E,U)]
        hi=[e+u for e,u in zip(E,U)]
        n,count,max_n=enumerate_signs(lo,hi)
        assert count==int(record['total_sign_patterns']) and max_n==int(record['max_simultaneous'])
        print(record['symbol'],'subsets',n,'feasible',count,'maximum',max_n)
        total+=n
    print('candidate patterns exhaustively tested',total)
