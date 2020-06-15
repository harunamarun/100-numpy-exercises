import numpy as np
# 74. Given an array C that is a bincount,
# how to produce an array A such that np.bincount(A) == C? (★★★)
'''
hint: np.repeat

INPUT:
[0 1 1 1]  # np.bincount([1, 2, 3])

OUTPUT:
[0 1 1 1]

'''
Z = [1, 2, 3]
C = np.bincount(Z)
A = Z.copy()
print(C)
print(np.bincount(A))


# C = np.bincount([1,1,2,3,4,4,6])
# A = np.repeat(np.arange(len(C)), C)
# print(A)
