import numpy as np
# 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)


A = np.arange(144).reshape(3, 4, 3, 4)
print(A)

sum = A.sum(axis=(-2, -1))
print(sum)


A = np.arange(8).reshape(2, 2, 2)
print(A)

sum = A.sum(axis=(0))
print(sum)
