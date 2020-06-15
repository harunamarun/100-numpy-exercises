import numpy as np
# 83. How to find the most frequent value in an array?
'''
hint: np.bincount, argmax

INPUT:
[[0 4 4 0 1]
 [3 0 3 4 3]
 [1 2 3 4 2]
 [1 0 1 4 0]
 [3 4 3 1 2]]

OUTPUT:
3

'''

Z = np.random.randint(0, 5, (5, 5))
print(Z)
A = np.bincount(Z.flatten())
print(A.argmax())

# Z = np.random.randint(0,10,50)
# print(np.bincount(Z).argmax())
