import numpy as np
# 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)
'''
hint: array[:, :, None]

INPUT:
[[[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]],
     ...
],
[[2. 2. 2. 2. 2.]
 [2. 2. 2. 2. 2.]
 [2. 2. 2. 2. 2.]
 [2. 2. 2. 2. 2.]
 [2. 2. 2. 2. 2.]]

OUTPUT:
[[[2. 2. 2.]
  [2. 2. 2.]
  [2. 2. 2.]
  [2. 2. 2.]
  [2. 2. 2.]],
     ...
]
'''

A = np.ones((5, 5, 3))
B = 2 * np.ones((5, 5))
print(A)
print(B)
# create 3 dimensions
B1 = B[:, :, None]
print(A*B1)
