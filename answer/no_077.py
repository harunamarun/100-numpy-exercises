import numpy as np
# 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)
'''
hint: np.logical_not, np.negative

INPUT:
[-1  0  1  2  3  4]

OUTPUT:
[ 1  0 -1 -2 -3 -4]
[0 1 0 0 0 0]
'''

Z = np.arange(-1, 5)
print(Z)
print(np.negative(Z))
# when Z is scolar out become scolar
print(np.logical_not(Z, out=Z))
