R<c_0011_0, c_0011_1, c_0011_2, c_0011_3, c_0011_6, c_0101_0, c_0101_2, c_0101_5> := PolynomialRing(RationalField(), 8, "grevlex");
I := ideal<R | - c_0011_0 * c_0011_2 + c_0011_2 * c_0101_5 + c_0011_6 * c_0101_0, c_0011_0 * c_0101_5 - c_0011_1 * c_0011_2 + c_0011_6 * c_0101_0, c_0011_0 * c_0101_2 - c_0011_2 * c_0101_0 - c_0011_2 * c_0101_2, - c_0011_0 * c_0101_2 + c_0011_1 * c_0101_2 + c_0011_3 * c_0101_0, - c_0011_0 * c_0011_2 + c_0011_2^2 - c_0011_6 * c_0101_2, c_0011_1 * c_0101_2 + c_0011_1^2 + c_0011_3 * c_0101_5, c_0011_0 * c_0011_1 + c_0011_3 * c_0101_5 + c_0011_6 * c_0101_2, c_0011_1 * c_0011_6 - c_0011_1^2 - c_0011_3 * c_0101_5, - 1 + c_0011_0>;
Q := Radical(I);
print "==DIM==", Dimension(Q);
D := PrimaryDecomposition(Q);
print "==NCOMP==", #D;
for comp in D do
  print "==COMP==";
  print "==DIMC==", Dimension(comp);
  n := #(GroebnerBasis(comp));
  print "==NBAS==", n;
  for b in GroebnerBasis(comp) do print "==POLY==", b; end for;
  try print "==LEX==", GroebnerBasis(comp, "lex"); catch e print "==LEXERR==", e; end try;
end for;
print "==ALLDONE==";