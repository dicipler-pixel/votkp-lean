# SCRIPT: c7_circuit
"""C7. The circuit polynomial of a knot diagram.

Shade the diagram in checkerboard fashion: shaded regions are the nodes of a graph, a
crossing is a branch joining the two shaded regions that touch it, and a branch carries
weight z if its crossing is right-handed and 1 if left-handed. Then

    Q(z) = sum over spanning trees of z^(number of right-handed branches),

which by the weighted matrix-tree theorem is any cofactor of the weighted Laplacian.

The colouring, and the bug this file fixes. Faces are traced from the PD code: the four
corners of a crossing are pd[i][k] / pd[i][k+1], and the face permutation sends the dart
(crossing, position) along its arc to the next position at the far end. That gives the
correct FACE COUNT (n+2 for a knot). What it does not give directly is the checkerboard
COLOUR: two corners of the same crossing that are diagonally opposite are necessarily the
same colour, but they are not adjacent, so they cannot both supply an adjacency edge.
Adjacency -- hence opposite colour -- comes from two corners at the same crossing that
share an arc, i.e. faces face(i,k) and face(i,k+1). Building the adjacency graph from the
crossing pairs instead (as an earlier version did) produces a graph that is not bipartite
and the colouring fails for every knot. That was the bug.

Pre-registered rules:
  R1  Q(1) = det(K) for alternating diagrams. CONFIRMED iff it holds on every alternating
      knot tested; Q(1) counts spanning trees, and the identity is the classical
      matrix-tree / Kauffman clock-state fact.
  R2  Q is invariant under flypes. Tested by comparing Q across the diagrams KnotInfo
      supplies for the same knot; a flype changes the diagram but not the knot.
"""
import sys, json
sys.path.insert(0,'code')
import sympy as sp
import snappy

def sn(nm):
    import re
    m = re.match(r'^(\d+)([an])_(\d+)$', nm)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}' if m else nm

def trace_faces(pd):
    """Face of each dart (crossing, position). Dart = arc pd[i][k] at crossing i."""
    pos = {}
    for i, t in enumerate(pd):
        for k in range(4):
            pos.setdefault(t[k], []).append((i, k))
    for a, v in pos.items():
        if len(v) != 2:
            raise ValueError(f'arc {a} occurs {len(v)} times')
    phi = {}
    for i in range(len(pd)):
        for k in range(4):
            x = pd[i][k]
            j, m = [v for v in pos[x] if v != (i, k)][0]
            phi[(i, k)] = (j, (m + 1) % 4)
    face = {}; nf = 0
    for d in phi:
        if d in face: continue
        c = d
        while c not in face:
            face[c] = nf; c = phi[c]
        nf += 1
    return face, nf

def corner(face, i, k):
    """Face occupying the corner between arcs k and k+1 at crossing i."""
    return face[(i, (k + 1) % 4)]

def checkerboard(pd, flip=False):
    face, nf = trace_faces(pd)
    n = len(pd)
    # adjacency: corners k and k+1 share arc k+1, so their faces are opposite colours
    adj = {}
    for i in range(n):
        for k in range(4):
            a, b = corner(face, i, k), corner(face, i, (k + 1) % 4)
            if a != b:
                adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    colour = {}
    for start in range(nf):
        if start in colour: continue
        colour[start] = 0; stack = [start]
        while stack:
            u = stack.pop()
            for v in adj.get(u, ()):
                if v not in colour:
                    colour[v] = 1 - colour[u]; stack.append(v)
                elif colour[v] == colour[u]:
                    raise ValueError('face graph not bipartite')
    if len(set(colour.values())) == 1:
        raise ValueError('faces could not be coloured')
    # black = colour 0; a crossing joins the two black corners, which are diagonally opposite
    edges = []
    for i in range(n):
        c0, c2 = corner(face, i, 0), corner(face, i, 2)
        if colour[c0] == 0:  edges.append((c0, c2, i))
        else:                edges.append((corner(face, i, 1), corner(face, i, 3), i))
    if flip:
        edges = [(corner(face, i, 1), corner(face, i, 3), i) if colour[corner(face, i, 0)] == 0
                 else (corner(face, i, 0), corner(face, i, 2), i) for i in range(n)]
    return edges, nf

def circuit_polynomial(pd, signs):
    edges, nf = checkerboard(pd)
    verts = sorted({x for (a, b, _) in edges for x in (a, b)})
    idx = {v: i for i, v in enumerate(verts)}
    z = sp.symbols('z')
    n = len(verts)
    Lap = sp.zeros(n, n)
    for (a, b, i) in edges:
        w = z if signs[i] > 0 else sp.Integer(1)
        ia, ib = idx[a], idx[b]
        Lap[ia, ia] += w; Lap[ib, ib] += w
        Lap[ia, ib] -= w; Lap[ib, ia] -= w
    Q = sp.expand(Lap[0:n-1, 0:n-1].det())
    return sp.Poly(Q, z), n

if __name__ == '__main__':
    import knotnames, csv
    fams = sys.argv[1:] or ['3','4','5','6','7','8']
    names = []
    for f in fams: names += knotnames.names_in(f)
    K = knotnames.load()
    csv.field_size_limit(10**9)
    ALT = {}
    for r in csv.DictReader(open('.scratch/venv/lib/python3.12/site-packages/database_knotinfo/csv_data/knotinfo_data_complete.csv'), delimiter='|'):
        ALT[r['name']] = (r['alternating'] or '').strip()
    ok = 0; bad = []; skipped = []; nonalt = 0
    for nm in names:
        if ALT.get(nm) != 'Y':
            nonalt += 1; continue
        try:
            L = snappy.Link(sn(nm))
            pd = [list(c) for c in L.PD_code()]
            signs = [c.sign for c in L.crossings]
            Q, nv = circuit_polynomial(pd, signs)
            q1 = int(Q.eval(1))
            det = abs(int(K[nm]['det']))
            if q1 == det: ok += 1
            else: bad.append((nm, q1, det))
        except Exception as ex:
            skipped.append((nm, f'{type(ex).__name__}: {ex}'))
    print(f'alternating knots tested: {ok+len(bad)}   Q(1)=det: {ok}   mismatches: {len(bad)}')
    print(f'non-alternating skipped: {nonalt}   construction failed: {len(skipped)}')
    for b in bad[:10]: print('   MISMATCH', b)
    for s in skipped[:6]: print('   SKIP', s)
