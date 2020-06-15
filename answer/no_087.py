import numpy as np
# 87. Consider a 16x16 array, how to get the block-sum
# (block size is 4x4)? (★★★)
'''
hint: np.add.reduceat

INPUT:
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

OUTPUT:
[[16. 16. 16. 16.]
 [16. 16. 16. 16.]
 [16. 16. 16. 16.]
 [16. 16. 16. 16.]]

'''

Z = np.ones((16, 16))
print(Z)
k = 4
column = np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0)
print(column)
S = np.add.reduceat(column, np.arange(0, Z.shape[1], k), axis=1)
print(S)


# Z = np.arange(4*4).reshape(4, 4)
# np.add.reduceat(Z,[i])
# It means to add colum from ith to end.
# np.add.reduceat(Z,[2])
# =====
# [[20 22 24 26]]

# np.add.reduceat(Z,[0],axis = 1)
# =====
# [[ 6]
#  [22]
#  [38]
#  [54]]

# np.add.reduceat(Z,[i, j])
# It means to add colum from ith to j-1th and from jth to end
# np.add.reduceat(Z,[0, 2])
# =====
# [[ 4  6  8 10]
#  [20 22 24 26]]
