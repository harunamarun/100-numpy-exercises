import numpy as np
# 69. How to get the diagonal of a dot product? (★★★)
A = np.arange(9).reshape(3, 3)
B = np.arange(9).reshape(3, 3)

print(A)
print(B)

print(np.dot(A, B))


print(np.diag(np.dot(A, B)))
