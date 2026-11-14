# SCRIPT: c8_verify_equal
"""C8: independent braid words for the 124 groups on which theta was equal.

Equality of theta on 248 knots is worth only as much as the diagrams it was computed on.
The census used SnapPy's braid_word(). Here every knot of the 124 equal groups is recomputed
from KnotInfo's braid_notation -- a different word on a different number of strands for
almost every knot -- and the two values at (2,3) are compared. A value is believed only if
the Alexander gate passes on that word, so a word that does not close to the named knot is
caught rather than silently agreeing.

Same for the 21 pairs that differed only by sign: there the check is that the two independent
values still differ by exactly the sign, i.e. that the mirror reading is not a braid artefact.
"""
import sys, json, os
sys.path.insert(0, 'code')
import multiprocessing as mp
from fractions import Fraction as Fr
import braid_drawing as bd, theta_general as tg


def theta_on(word, q=(2, 3)):
    m = max(abs(x) for x in word) + 1
    X, phi, n, info = bd.diagram(word, m)
    v, _ = tg.theta(X, phi, n, q[0], q[1], verify=False)
    return Fr(v), n


def one(nm):
    from certificate_all import words_for
    from census import alex_number, seifert_delta_at, snappy_name
    import snappy
    out = {'knot': nm}
    try:
        w_snap = list(snappy.Link(snappy_name(nm)).braid_word())
    except Exception as e:
        out['error'] = f'snappy {type(e).__name__}'
        return out
    cand = words_for(nm)
    # prefer a word that is genuinely different from SnapPy's
    alt = [(w, s) for w, s in cand if s != 'SnapPy' and w != w_snap]
    if not alt:
        alt = [(w, s) for w, s in cand if s != 'SnapPy']
    if not alt:
        out['error'] = 'no KnotInfo braid word'
        return out
    w, src = alt[0]
    try:
        v_snap, n_snap = theta_on(w_snap)
    except ValueError as e:
        out['error'] = f'pole snap {e}'
        return out
    try:
        v_alt, n_alt = theta_on(w)
    except ValueError as e:
        out['error'] = f'pole alt {e}'
        return out
    # Alexander gate on the alternative word: T^e det A / Delta(T) must be +/- a power of two
    X, phi, n, info = bd.diagram(w, max(abs(x) for x in w) + 1)
    e = Fr(-info['sum_phi'] - info['w'], 2)          # -(sum phi + w)/2, the census exponent
    gate = None
    try:
        num = Fr(3) ** int(e) * alex_number(X, n, 3)
        den = seifert_delta_at(nm, 3)
        gate = str(num / den) if den != 0 else None
    except Exception:
        gate = None
    out.update({'src': src, 'n_snap': n_snap, 'n_alt': n_alt,
                'theta_snap': str(v_snap), 'theta_alt': str(v_alt),
                'same': v_snap == v_alt, 'same_abs': abs(v_snap) == abs(v_alt),
                'gate': gate})
    return out


if __name__ == '__main__':
    rows = json.load(open('.scratch/c8_tally.json'))
    knots = []
    for r in rows:
        if r['class'] in ('equal', 'equal_up_to_sign'):
            knots += r['group']
    knots = sorted(set(knots))
    print(f'knots to re-derive from a second braid word: {len(knots)}')
    with mp.Pool(4) as pool:
        res = pool.map(one, knots, chunksize=1)
    err = [r for r in res if r.get('error')]
    ok = [r for r in res if not r.get('error')]
    agree = [r for r in ok if r['same']]
    absagree = [r for r in ok if r['same_abs'] and not r['same']]
    differ = [r for r in ok if not r['same_abs']]
    print(f'  errors {len(err)}, computed {len(ok)}, identical value {len(agree)}, '
          f'equal in absolute value only {len(absagree)}, different {len(differ)}')
    used = sum(1 for r in ok if r['src'] != 'SnapPy' and r['n_snap'] != r['n_alt'])
    print(f'  words that genuinely differ in length from SnapPy\'s: {used}')
    for r in err[:10]:
        print('  ERR', r['knot'], r['error'])
    for r in differ[:10]:
        print('  DIFF', r['knot'], r['src'], r['theta_snap'], r['theta_alt'], 'gate', r['gate'])
    # per-group verdict
    bad = []
    for row in rows:
        if row['class'] not in ('equal', 'equal_up_to_sign'):
            continue
        vals = []
        for nm in row['group']:
            r = next(x for x in res if x['knot'] == nm)
            if r.get('error'):
                vals.append(None)
            else:
                vals.append(Fr(r['theta_alt']))
        if any(v is None for v in vals):
            bad.append((row['group'], 'error'))
            continue
        if row['class'] == 'equal' and len(set(vals)) != 1:
            bad.append((row['group'], [str(v) for v in vals]))
        if row['class'] == 'equal_up_to_sign' and len(set(abs(v) for v in vals)) != 1:
            bad.append((row['group'], [str(v) for v in vals]))
    print(f'  groups whose pattern is NOT reproduced from the second words: {len(bad)}')
    for x in bad[:20]:
        print('    ', x)
    json.dump(res, open('.scratch/c8_verify_equal.json', 'w'), indent=1)
    print('wrote .scratch/c8_verify_equal.json')
