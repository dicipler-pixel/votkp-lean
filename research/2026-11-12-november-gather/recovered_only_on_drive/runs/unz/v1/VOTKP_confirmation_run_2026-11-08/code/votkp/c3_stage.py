# SCRIPT: c3_stage
"""C3/C4 stage 1: emit a compact Magma script per knot, plus the data needed to parse.

For each knot we take the Ptolemy variety for the geometric obstruction class, emit its
ideal into a minimal Magma script that returns the radical's primary decomposition and,
for each zero-dimensional prime component, the lex Groebner basis, and we save alongside
it the variable names and the py_eval section that turns a solution into the full set of
Ptolemy coordinates (including the shape parameters z_).
"""
import sys, os, json
sys.path.insert(0,'code'); sys.path.insert(0,'code/votkp')
import snappy
from c3_solutions import sn

KNOTS = ['4_1','5_2','6_1','6_2','6_3','7_2','7_3','7_4','7_5','7_6','7_7']

def build(nm):
    M = snappy.Link(sn(nm)).exterior()
    classes = M.ptolemy_obstruction_classes()
    V = M.ptolemy_variety(2, obstruction_class=1 if len(classes) > 1 else None)
    vars_ = list(V.variables)
    eqs = [str(e) for e in V.equations]
    body = []
    body.append('R<%s> := PolynomialRing(RationalField(), %d, "grevlex");' % (
        ', '.join(vars_), len(vars_)))
    body.append('I := ideal<R | %s>;' % ', '.join(eqs))
    body.append('Q := Radical(I);')
    body.append('print "==DIM==", Dimension(Q);')
    body.append('D := PrimaryDecomposition(Q);')
    body.append('print "==NCOMP==", #D;')
    body.append('for comp in D do')
    body.append('  print "==COMP==";')
    body.append('  print "==DIMC==", Dimension(comp);')
    body.append('  n := #(GroebnerBasis(comp));')
    body.append('  print "==NBAS==", n;')
    body.append('  for b in GroebnerBasis(comp) do print "==POLY==", b; end for;')
    body.append('  try print "==LEX==", GroebnerBasis(comp, "lex"); catch e print "==LEXERR==", e; end try;')
    body.append('end for;')
    body.append('print "==ALLDONE==";')
    return dict(knot=nm, variables=vars_, equations=eqs,
                script='\n'.join(body), py_eval=V.py_eval_section(),
                n_tet=M.num_tetrahedra(),
                shapes=[[complex(t).real, complex(t).imag] for t in M.tetrahedra_shapes('rect', bits_prec=53)])

if __name__ == '__main__':
    os.makedirs('.scratch/magma', exist_ok=True)
    meta = {}
    for nm in KNOTS:
        d = build(nm)
        open('.scratch/magma/%s.m' % nm.replace('_',''), 'w').write(d['script'])
        meta[nm] = {k: v for k, v in d.items() if k != 'script'}
        print(f"{nm:6s} vars {len(d['variables']):2d}  eqs {len(d['equations']):2d}  "
              f"script {len(d['script']):5d} bytes")
    json.dump(meta, open('.scratch/magma/meta.json','w'), indent=1)
