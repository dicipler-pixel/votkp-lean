# SCRIPT: SYNTHESIS-CHECKS-01
# Three elementary identities used in SYNTHESIS.md, section 2.
# 1. On a wire of dimension q the cross block is the q x q identity: rank = q and sum of squared singular values = q.
# 2. Both the rank and the weight multiply under tensor (Kronecker) product.
# 3. Under an invertible local map the rank does not move and the weight can rise, so the weight is not monotone under restriction.
import numpy as np
q=5;B=np.eye(q);print('wire q=5: rank',np.linalg.matrix_rank(B),' weight',np.sum(B*B))
A=np.random.default_rng(0).normal(size=(3,4));C=np.random.default_rng(1).normal(size=(2,5));K=np.kron(A,C)
print('multiplicative: rank',np.linalg.matrix_rank(K),'=',np.linalg.matrix_rank(A)*np.linalg.matrix_rank(C),' weight',round(np.sum(K*K),10),'=',round(np.sum(A*A)*np.sum(C*C),10))
D=np.diag([1.0,0.1]);M=np.diag([1.0,10.0]);print('restriction by an invertible map: rank',np.linalg.matrix_rank(M@D),'unchanged; weight',np.sum(D*D),'->',np.sum((M@D)**2),'(rises)')
