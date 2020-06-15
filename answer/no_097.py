import numpy as np
# 97. Considering 2 vectors A & B,
# write the einsum equivalent of inner, outer, sum, and mul function (★★★)
'''
hint: np.einsum
'''
A = np.arange(3)
B = np.arange(3)
print(np.dot(A, B))
print(np.einsum("i,i", A, B))

print(np.outer(A, B))
print(np.einsum("i,j->ij", A, B))

print(np.sum(A))
print(np.einsum("i->", A))

print(A*B)
print(np.einsum("i,i->i", A, B))
