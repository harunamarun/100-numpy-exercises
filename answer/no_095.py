import numpy as np
# 95. Convert a vector of ints into a matrix binary representation (★★★)
'''
hint: np.unpackbits
INPUT:
[  0   1   2   3  15  16  32  64 128]
OUTPUT:
[[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1]
 [0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 1 1]
 [0 0 0 0 1 1 1 1]
 [0 0 0 1 0 0 0 0]
 [0 0 1 0 0 0 0 0]
 [0 1 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0]]
'''
Z = np.array([0, 1, 2, 4, 8, 16, 32, 64, 128], dtype=np.uint8)
size = np.size(Z)
T = Z.reshape((size, 1))
print(np.unpackbits(T, axis=1))


# I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])
# B = ((I.reshape(-1,1) & (2**np.arange(8))) != 0).astype(int)
# print(B[:,::-1])


# I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
# print(np.unpackbits(I[:, np.newaxis], axis=1))
