import numpy as np
# 82. Compute a matrix rank (★★★)
'''
hint: np.linalg.svd

INPUT:
[[1, 2, 3, 0],
[2, 4, 6, 0],
[1, 0, 1, 2],
[1, 0, 0, 3]]

OUTPUT:
3

'''
Z = np.array([[1, 2, 3, 0],
              [2, 4, 6, 0],
              [1, 0, 1, 2],
              [1, 0, 0, 3]])

print(np.linalg.matrix_rank(Z))


# U, S, V = np.linalg.svd(Z)  # Singular Value Decomposition
# print("S")
# print(S)
# rank = np.sum(S > 1e-10)
# print(rank)
