"""O III prospective state-resolved design. No response data are read or scored."""
import argparse
import gzip
import hashlib
import json
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

DIGEST = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
# NBS NSRDS 3 section 11 (1985), Table of Energy Levels, O III.
TERMS = {
    3: ('267258.71', '267377.11', '267634.00'),
    4: ('356736.30', '356844.98', '357117.01'),
    5: ('391830.76', '391917.80', '392209.53'),
}
PER_EV = F('8065.543937')  # same cm^-1/eV convention as North's check
L, H = F('7.576234') / F('1.30447'), F('8.15168') / F('1.3895212')
P = argparse.ArgumentParser(description=__doc__)
P.add_argument('archive', type=Path)
P.add_argument('--level-width', type=F, default=F(0),
               help='Hypothetical common symmetric half-width in cm^-1. Default holds level positions fixed.')
args = P.parse_args()
assert args.level_width >= 0
assert hashlib.sha256(args.archive.read_bytes()).hexdigest() == DIGEST
records = {r['symbol']: r for r in json.load(gzip.open(args.archive, 'rt'), parse_float=str)['records']}
oxygen = records['O']
stages = {row['q']: row for row in oxygen['thresholds']}
I1, I2 = [F(stages[k]['IE_eV']) for k in (0, 1)]
d1, d2 = [F(stages[k]['unc_eV']) for k in (0, 1)]
assert (I1, d1, I2, d2) == tuple(map(F, ('13.618055', '.000007', '35.12112', '.00006')))


def dec(x):
    return D(x.numerator) / D(x.denominator)


def box(e):
    e = F(e)
    return ((I2-d2+(e-args.level_width)/PER_EV)/(I1+d1),
            (I2+e/PER_EV)/I1,
            (I2+d2+(e+args.level_width)/PER_EV)/(I1-d1))


def native(x):
    return x > 1 and x*x - 6*x + 1 > 0


def g(z):
    return (z-1)/(z+1)


def inverse_g(x):
    return (1+x)/(1-x)


def sinh_h(z):
    return (z-1)/(2*z.sqrt())


def six(lo, hi):
    x, y = dec(lo), dec(hi)
    u = (sinh_h(x)*sinh_h(y)).sqrt()
    return {
        'Arithmetic z': (x+y)/2,
        'Geometric z': (x*y).sqrt(),
        'Harmonic z': 2*x*y/(x+y),
        'Arithmetic gamma': inverse_g((g(x)+g(y))/2),
        'Arithmetic gamma squared': inverse_g(((g(x)**2+g(y)**2)/2).sqrt()),
        'Geometric sinh(h)': (u+(1+u*u).sqrt())**2,
    }


def fmt(x):
    return f'{dec(x):.12f}'


with localcontext() as ctx:
    ctx.prec = 55
    z = {n: list(map(box, es)) for n, es in TERMS.items()}
    singlet = box('358668.90')
    fits = six(L, H)
    def calibration_box(symbol, ea, ea_width):
        neutral = records[symbol]['thresholds'][0]
        assert neutral['q'] == 0
        ie, die, ea, dea = map(F, (neutral['IE_eV'], neutral['unc_eV'], ea, ea_width))
        return ((ie-die)/(ea+dea), (ie+die)/(ea-dea))

    ls = calibration_box('Ag', '1.30447', '0.00002')
    hs = calibration_box('Si', '1.3895212', '0.0000007')
    lows, highs = six(ls[0], hs[0]), six(ls[1], hs[1])
    print('six-rival calibration range', f'{min(lows.values()):.12f}', f'{max(highs.values()):.12f}')
    w = 3+2*D(2).sqrt()
    print('Setting sensitivity for supplied level half-width (cm^-1):', args.level_width)
    for n, row in z.items():
        for j, (lo, center, hi) in enumerate(row):
            print(f'{n}s J={j}   {fmt(lo)}  {fmt(center)}  {fmt(hi)}')
    print('singlet 4s J=1', *(fmt(x) for x in singlet))
    nominal = [z[4][i][1] for i in (1, 2)]
    inner = [z[4][1][2], z[4][2][0]]
    outer = [z[4][1][0], z[4][2][2]]
    for label, (a,b) in [('nominal', nominal), ('intersection', inner), ('union', outer)]:
        print(label, f'[{fmt(a)}, {fmt(b)})', 'width', fmt(b-a))
    assert nominal[1]-nominal[0] == F('272.03')/PER_EV/I1
    assert tuple(map(fmt, nominal)) == ('5.827870339202', '5.830347008705')
    if args.level_width == 0:
        assert tuple(map(fmt, inner)) == ('5.827877740784', '5.830339605858')
        assert tuple(map(fmt, outer)) == ('5.827862937628', '5.830354411559')
    print('central gap width ratio', fmt((H-L)/(nominal[1]-nominal[0])))
    j2 = z[4][2]
    for name, c in fits.items():
        assert all(dec(v[1]) < c for v in z[4])
        stable = dec(j2[2]) < lows[name]
        print(f'{name:25s} {c:.12f}   J=2 inside   stable on input boxes: {stable}')
    print('Geometry J=2', 'outside' if native(j2[1]) else 'inside')
    print('Geometric calls stable under proposed extra width:',
          all(native(l) == native(x) == native(u) for l,x,u in z[4]))
    print('J1/J2 pattern conditional on unknown level widths and ground-source rectangle:')
    for j in (0,1,2):
        energy=dec(F(TERMS[4][j]))
        if native(z[4][j][1]):
            margin=energy-dec(PER_EV)*(w*dec(I1+d1)-dec(I2-d2))
        else:
            margin=dec(PER_EV)*(w*dec(I1-d1)-dec(I2+d2))-energy
        print(j, f'{margin:.9f}', 'cm^-1 to exact wall')
    for n in (3,4,5):
        native_calls = [int(native(p[1])) for p in z[n]]
        print('native calls', n, native_calls)
        assert native_calls == {3:[0,0,0],4:[0,0,1],5:[1,1,1]}[n]
        for c in fits.values():
            assert [int(dec(p[1])>c) for p in z[n]] == ([1,1,1] if n==5 else [0,0,0])
    print('Interaction controls, columns (0,1),(0,2),(1,2). Row contrast higher n minus lower n.')
    for na,nb in combinations((3,4,5),2):
        a,b = [[int(native(p[1])) for p in z[n]] for n in (na,nb)]
        print(na,nb, [b[j]-b[i]-(a[j]-a[i]) for i,j in combinations((0,1,2),2)])
    assert not native(nominal[0]) and native(nominal[1])
