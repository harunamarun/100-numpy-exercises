import numpy as np
# 58. Subtract the mean of each row of a matrix (★★☆)
Z = np.arange(9).reshape(3,3)
Y = Z - Z.mean(axis=1, keepdims=True)
print(Y)

#  keepdims 初期値はFalse