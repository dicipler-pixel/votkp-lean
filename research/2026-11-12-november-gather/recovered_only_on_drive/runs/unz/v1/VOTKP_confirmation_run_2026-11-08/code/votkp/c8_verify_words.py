# SCRIPT: c8_verify_words
"""C8: every knot of the unseparated groups, re-derived from a second braid word.

For the 145 groups on which theta did not separate the members, the census value came from
SnapPy's braid_word(). Here each of the knots is recomputed from KnotInfo's braid_notation --
usually a different word, often on a different number of strands -- and the two values are
compared at a point where BOTH words are finite. (At (2,3) a knot can be a pole: det A at
(2,3) carries Delta(2)Delta(3)Delta(6), which is a property of the knot, not of the word.)

The comparison is on the exact rational value, so "agree" means agree over the integers. The
Alexander gate -- T^e det A / Delta(T) a power of two at T = 3 -- is run on the alternative
word, so a word that does not close to the named knot is caught rather than silently
agreeing.
"""
import sys, json
sys.path.insert(0, 'code')
import multiprocessing as mp
from fractions import Fraction as Fr
import braid_drawing as bd, theta_general as tg

POOL = [(2, 3), (2, 5), (3, 5), (5, 7), (2, 7), (3, 7)]
VERD = '.scratch/c8_verdicts.json'


def build(word):
    m = max(abs(x) for x in word) + 1
    X, phi, n, info = bd.diagram(word, m)
    return X, phi, n, info


def values(X, phi, n):
    out = []
    for q in POOL:
        try:
            v, _ = tg.theta(X, phi, n, q[0], q[1], verify=False)
        except ValueError:
            out.append(None)
            continue
        out.append(Fr(v))
    return out


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
    cand = [(w, s) for w, s in words_for(nm) if s != 'SnapPy' and w != w_snap] or \
           [(w, s) for w, s in words_for(nm) if s != 'SnapPy']
    if not cand:
        out['error'] = 'no second word'
        return out
    w, src = cand[0]
    try:
        a, b = build(w_snap), build(w)
    except Exception as e:
        out['error'] = f'build {type(e).__name__}'
        return out
    va, vb = values(*a[:3]), values(*b[:3])
    out.update({'src': src, 'n_snap': a[2], 'n_alt': b[2], 'word_len_snap': len(w_snap),
                'word_len_alt': len(w), 'n_strands_snap': max(abs(x) for x in w_snap) + 1,
                'n_strands_alt': max(abs(x) for x in w) + 1})
    for j, q in enumerate(POOL):
        if va[j] is not None and vb[j] is not None:
            out['point'] = list(q)
            out['theta_snap'] = str(va[j])
            out['theta_alt'] = str(vb[j])
            out['same'] = va[j] == vb[j]
            break
    else:
        out['error'] = 'no common finite point'
        return out
    # Alexander gate on the alternative word
    X, phi, n, info = b
    e = Fr(-info['sum_phi'] - info['w'], 2)
    try:
        num = Fr(3) ** int(e) * alex_number(X, n, 3)
        den = seifert_delta_at(nm, 3)
        out['gate'] = str(num / den) if den != 0 else None
        if out['gate'] is not None:
            r = abs(Fr(out['gate']))
            n_, d_ = r.numerator, r.denominator
            out['gate_ok'] = r == 1 or ((n_ & (n_ - 1) == 0) and (d_ & (d_ - 1) == 0))
    except Exception:
        out['gate'] = None
    return out


if __name__ == '__main__':
    V = json.load(open(VERD))
    knots = sorted({nm for r in V if r['verdict'] in ('equal', 'sign', 'partly') for nm in r['group']})
    print(f'knots in the 145 unseparated groups: {len(knots)}')
    with mp.Pool(4) as pool:
        res = pool.map(one, knots, chunksize=1)
    err = [r for r in res if r.get('error')]
    ok = [r for r in res if not r.get('error')]
    print(f'  errors {len(err)}: {[ (r["knot"], r["error"]) for r in err[:6]]}')
    print(f'  computed {len(ok)}, identical at a common point {sum(1 for r in ok if r["same"])}, '
          f'different {sum(1 for r in ok if not r["same"])}')
    print(f'  of those, a word of different length: '
          f'{sum(1 for r in ok if r["word_len_alt"] != r["word_len_snap"])}, '
          f'different strand number: {sum(1 for r in ok if r["n_strands_alt"] != r["n_strands_snap"])}')
    print(f'  Alexander gate on the second word: passed {sum(1 for r in ok if r.get("gate_ok"))}, '
          f'failed {sum(1 for r in ok if r.get("gate_ok") is False)}, not computable '
          f'{sum(1 for r in ok if r.get("gate") is None)}')
    for r in ok:
        if not r['same']:
            print('   DIFF', r['knot'], r['point'], r['theta_snap'], r['theta_alt'])
    json.dump(res, open('.scratch/c8_verify_words.json', 'w'), indent=1)
    print('wrote .scratch/c8_verify_words.json')
