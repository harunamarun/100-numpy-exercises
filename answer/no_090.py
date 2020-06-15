import numpy as np
import itertools
# 90. Given an arbitrary number of vectors,
# build the cartesian product (every combinations of every item) (★★★)
'''
INPUT:
[1, 2, 3], [4, 5], [6, 7]
OUTPUT:
[[1 4 6]
 [1 4 7]
 [1 5 6]
 [1 5 7]
 [2 4 6]
 [2 4 7]
 [2 5 6]
 [2 5 7]
 [3 4 6]
 [3 4 7]
 [3 5 6]
 [3 5 7]]

'''

print(list(itertools.product([1, 2, 3], [4, 5])))


def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)

    ix = np.indices(shape, dtype=int)
    ix = ix.reshape(len(arrays), -1).T

    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]

    return ix


print(cartesian(([1, 2, 3], [4, 5])))
