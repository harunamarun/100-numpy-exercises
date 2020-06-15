import numpy as np
from numpy.lib import stride_tricks
# 81. Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
# how to generate an array
# R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]? (★★★)
'''
hint: stride_tricks.as_strided

INPUT:
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]

OUTPUT:
[[ 1  2  3  4]
 [ 2  3  4  5]
 [ 3  4  5  6]
 [ 4  5  6  7]
 [ 5  6  7  8]
 [ 6  7  8  9]
 [ 7  8  9 10]
 [ 8  9 10 11]
 [ 9 10 11 12]
 [10 11 12 13]
 [11 12 13 14]]]

'''

Z = np.arange(1, 15)
print(Z)
R = stride_tricks.as_strided(
    Z, shape=(11, 4), strides=(Z.itemsize, Z.itemsize))
print(R)

# Z = np.arange(1,15,dtype=np.uint32)
# R = stride_tricks.as_strided(Z,(11,4),(4,4))
# print(R)
