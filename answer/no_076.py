import numpy as np
from numpy.lib import stride_tricks
# Consider a one-dimensional array Z, build a two-dimensional array
# whose first row is (Z[0],Z[1],Z[2]) and each subsequent row
# is shifted by 1 (last row should be (Z[-3],Z[-2],Z[-1]) (★★★)
'''
hint: from numpy.lib import stride_tricks

INPUT:
[0 1 2 3 4]

OUTPUT:
[[0 1 2]
 [1 2 3]
 [2 3 4]]

'''

Z = np.arange(6)
print(Z)
window = 3
print(stride_tricks.as_strided(
    Z, shape=(Z.size - window + 1, window), strides=(Z.itemsize, Z.itemsize)))

# def rolling(a, window):
#     shape = (a.size - window + 1, window)
#     strides = (a.itemsize, a.itemsize)
#     return stride_tricks.as_strided(a, shape=shape, strides=strides)
# X = rolling(Z, 3)
# print(X)
