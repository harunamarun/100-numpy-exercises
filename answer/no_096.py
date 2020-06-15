import numpy as np
# 96. Given a two dimensional array, how to extract unique rows? (★★★)
'''
hint: np.ascontiguousarray | np.unique
INPUT:
[[1 0 1]
 [0 0 0]
 [1 1 1]
 [0 0 1]
 [1 1 1]
 [0 0 1]]
OUTPUT:
[[0 0 0]
 [0 0 1]
 [1 0 1]
 [1 1 1]]
'''
Z = np.random.randint(0, 2, (6, 3))
print(Z)
print(np.unique(Z, axis=0))

# Z = np.random.randint(0, 2, (6, 3))
# T = np.ascontiguousarray(Z).view(
#     np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
# _, idx = np.unique(T, return_index=True)
# uZ = Z[idx]
# print(uZ)
