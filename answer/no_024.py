import numpy as np
# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
X = np.random.random((5,3))
Y = np.random.random((3,2))
print(np.dot(X,Y))
# print(X@Y)