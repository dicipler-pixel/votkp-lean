#!/usr/bin/env python3
"""Grid certificates for every zero of the census, on the shortest braid available.

The grid cost is (2n+5)(2n+4) where n is the crossing count of the DIAGRAM, so the
choice of braid representative matters enormously.  KnotInfo publishes a braid
notation for every knot and it is usually far shorter than the word SnapPy's
braid_word() returns: 8_3 goes from 24 crossings to 10, which cuts its grid from
2756 cells to 600.  Since theta is an invariant, any braid representative of the
knot serves, so we take the shortest.

Each certificate is checked against the repaired Alexander gate before it is
believed, so a braid that does not close to the named knot is caught.
"""
import sys; sys.path.insert(0,'code')
import ast, csv, json, os
import braid_drawing as bd, theta_general as tg
from fractions import Fraction as Fr

CSVP = '.scratch/venv/lib/python3.12/site-packages/database_knotinfo/csv_data/knotinfo_data_complete.csv'

def words_for(nm):
    """Candidate braid words: SnapPy's, KnotInfo's. Returns list of (word, source)."""
    import snappy
    from census import snappy_name
    out = []
    try:
        out.append((list(snappy.Link(snappy_name(nm)).braid_word()), 'SnapPy'))
    except Exception:
        pass
    try:
        csv.field_size_limit(10**9)
        for r in csv.DictReader(open(CSVP), delimiter='|'):
            if r['name'] == nm:
                b = (r['braid_notation'] or '').strip()
                if b.startswith('['):
                    out.append(([int(x) for x in ast.literal_eval(b)], 'KnotInfo'))
                break
    except Exception:
        pass
    return out

def build(word):
    m = max(abs(x) for x in word) + 1
    X, phi, n, info = bd.diagram(word, m)
    npos = sum(1 for s, _, _ in X if s > 0)
    nneg = sum(1 for s, _, _ in X if s < 0)
    e = Fr(-info['sum_phi'] - info['w'], 2)
    return dict(X=X, phi=phi, n=n, e=int(e), L=int(e) - nneg, U=int(e) + npos,
                npos=npos, nneg=nneg, w=info['w'])

def gate_ok(nm, d, T=5):
    from census import alex_number, seifert_delta_at
    num = Fr(T)**d['e'] * alex_number(d['X'], d['n'], T)
    den = seifert_delta_at(nm, T)
    if den == 0:
        return None
    return num/den

def best_diagram(nm):
    best = None
    for word, src in words_for(nm):
        try:
            d = build(word); d['word'] = word; d['src'] = src
        except Exception:
            continue
        if best is None or d['n'] < best['n']:
            best = d
    return best

def certify(nm):
    from zero_certificate import root_bound, seifert_delta
    d = best_diagram(nm)
    if d is None:
        return dict(knot=nm, ok=False, why='no usable braid')
    r = gate_ok(nm, d)
    if r is None or r not in (Fr(1), Fr(-1)):
        return dict(knot=nm, ok=False, why=f'gate r={r}', n=d['n'], src=d['src'])
    R = root_bound(seifert_delta(nm))
    nx, ny = 2*d['n'] + 5, 2*d['n'] + 4
    xs = [R + 1 + i for i in range(nx)]
    ys = [R + 1 + i for i in range(ny)]
    checked = 0
    for x in xs:
        for y in ys:
            try:
                v, _ = tg.theta(d['X'], d['phi'], d['n'], x, y, verify=False)
            except ValueError:
                return dict(knot=nm, ok=False, why=f'singular ({x},{y})', n=d['n'], src=d['src'])
            checked += 1
            if v != 0:
                return dict(knot=nm, ok=False, why='nonzero on grid', at=(x, y, str(v)),
                            n=d['n'], src=d['src'])
    return dict(knot=nm, ok=True, n=d['n'], src=d['src'], word=d['word'],
                L=d['L'], U=d['U'], degx=2*d['n']+4, degy=2*d['n']+3,
                cells=checked, R=R)

if __name__ == '__main__':
    names = sys.argv[1:]
    out = '.scratch/certificates.jsonl'
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: done.add(json.loads(line)['knot'])
            except Exception: pass
    with open(out, 'a') as fh:
        for nm in names:
            if nm in done: continue
            r = certify(nm)
            fh.write(json.dumps(r) + '\n'); fh.flush()
            print(('CERTIFIED ' if r['ok'] else 'FAILED    ') + f"{nm:10s} n={r.get('n','?')} "
                  f"src={r.get('src','?')} cells={r.get('cells','-')} "
                  f"{'' if r['ok'] else r.get('why','')}", flush=True)
