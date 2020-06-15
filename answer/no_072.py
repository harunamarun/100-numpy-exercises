import numpy as np
# 72. How to swap two rows of an array? (★★★)
'''
hint: array[[]] = array[[]]

INPUT:
[[0 1 2]
 [3 4 5]
 [6 7 8]]

OUTPUT:
[[0 1 2]
 [6 7 8]
 [3 4 5]]

'''

A = np.arange(9).reshape((3, 3))
print(A)

A[2, :], A[1, :] = A[1, :], A[2, :].copy()

print(A)


# A[[0,1]] = A[[1,0]]
