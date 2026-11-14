# SCRIPT: c2_rescale
"""Put the corrected constant into the per-knot certificate file.

c2_certify_census.py wrote bound = C sum_j |G_j|^5 / Vol with C = 0.685556567092, which the
finer computation of c2_certified_bound2.py shows is too small (the supremum of |R|/|G|^5 over the
disk is 0.6855670950379..., at |G| = 0.265893). The value used now is C = 0.75, the constant
PROVED by c2_enclosure.py: 0.6954 on |G| <= 0.5 from the Taylor expansion, 0.75 on |G| >= 0.5 from
a box cover. The rescaling is exact because bound is proportional to C.

Rather than recompute 12,942 hyperbolic structures (ten minutes of SnapPy) to change one
constant, the records are rescaled by C_new/C_old. That is exact, because bound is proportional to
C and the shapes do not enter it otherwise; the script recomputes nothing else and says so.

    python3 code/votkp/c2_rescale.py
"""
import json

C_OLD = 0.685556567092
C_NEW = 0.75
F = C_NEW / C_OLD
PATH = '.scratch/c2_certify.jsonl'

if __name__ == '__main__':
    rows = []
    for line in open(PATH):
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    changed = 0
    for r in rows:
        if r.get('C') == C_NEW:
            continue
        r['bound'] *= F
        r['bound_max'] *= F
        r['C'] = C_NEW
        changed += 1
    with open(PATH, 'w') as fh:
        for r in rows:
            fh.write(json.dumps(r) + '\n')
    print(f'{changed} of {len(rows)} records rescaled by {F:.12f} (C {C_OLD} -> {C_NEW})')
