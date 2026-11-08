# SCRIPT: MAJORANA-BRAID-01
# Claim being tested (Jeromie's words, woo removed): "the gamma matrices are knot
# braiding operators." This is Ivanov's theorem (2001): exchanging two Majorana
# fermions acts by a gamma-matrix (Clifford) operation, and those operations obey
# the braid-group relations. Why the checks below prove it:
#   (C) Clifford: build Majorana ops g1..g4 and verify {g_a,g_b}=2 delta_ab -- i.e.
#       they ARE a gamma-matrix algebra.
#   (U) the braid generator B_i = exp(pi/4 g_{i+1} g_i) = (1 + g_{i+1}g_i)/sqrt2
#       is unitary.
#   (X) B_i implements the exchange: B_i g_i B_i^dag = g_{i+1}, B_i g_{i+1} B_i^dag = -g_i
#       (a 90-degree rotation in the i,(i+1) plane -- the braid, with the spinor sign).
#   (B) the braid relation B_i B_{i+1} B_i = B_{i+1} B_i B_{i+1} holds.
#   (S) B_i^2 = g_{i+1} g_i != I -- the generator is NOT order 2, the non-Abelian /
#       spinorial signature (a full return needs the double cover, the 720-degree fact).
import numpy as np
I2=np.eye(2); X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.array([[1,0],[0,-1]],complex)
kron=lambda *a: a[0] if len(a)==1 else np.kron(a[0],kron(*a[1:]))
# 2 fermion modes -> 4 Majoranas on a 4-dim space (Jordan-Wigner)
g=[kron(X,I2), kron(Y,I2), kron(Z,X), kron(Z,Y)]
dim=4; Im=np.eye(dim)
def dag(M): return M.conj().T
# (C) Clifford / gamma algebra
cliff=max(np.max(np.abs(g[a]@g[b]+g[b]@g[a]-2*(a==b)*Im)) for a in range(4) for b in range(4))
# braid generators B1,B2,B3
B=[ (Im + g[i+1]@g[i])/np.sqrt(2) for i in range(3) ]
uni=max(np.max(np.abs(dag(b)@b-Im)) for b in B)
# (X) exchange action of B1 on g1,g2
ex1=np.max(np.abs(B[0]@g[0]@dag(B[0]) - g[1]))
ex2=np.max(np.abs(B[0]@g[1]@dag(B[0]) + g[0]))
# (B) braid relation on (B1,B2) and (B2,B3)
br1=np.max(np.abs(B[0]@B[1]@B[0] - B[1]@B[0]@B[1]))
br2=np.max(np.abs(B[1]@B[2]@B[1] - B[2]@B[1]@B[2]))
# far commutation B1,B3
fc=np.max(np.abs(B[0]@B[2]-B[2]@B[0]))
# (S) B^2 = g2 g1, and order (B not order 2)
sq=np.max(np.abs(B[0]@B[0] - g[1]@g[0]))
order2 = np.max(np.abs(B[0]@B[0]-Im))
print("(C) Clifford {g_a,g_b}=2d_ab  max dev : %.2e   -> they ARE gamma matrices"%cliff)
print("(U) braid generators unitary  max dev : %.2e"%uni)
print("(X) B1 g1 B1^+ = g2            max dev : %.2e"%ex1)
print("    B1 g2 B1^+ = -g1           max dev : %.2e   -> the exchange, with the spinor sign"%ex2)
print("(B) braid relation B1B2B1=B2B1B2 dev  : %.2e"%br1)
print("    braid relation B2B3B2=B3B2B3 dev  : %.2e"%br2)
print("    far gens commute [B1,B3]      dev : %.2e   -> full braid-group B_4 rep"%fc)
print("(S) B1^2 = g2 g1              max dev : %.2e"%sq)
print("    |B1^2 - I| = %.3f  (nonzero: generator NOT order 2 -> non-Abelian/spinorial)"%order2)
