import numpy as np
# 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))
X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
print(np.linalg.det(C))