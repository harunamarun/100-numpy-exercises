import numpy as np
# 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)

# should return [1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 5]

Z = np.array([1, 2, 3, 4, 5])
num_of_zero = 3
# created zero's array which length is result
result = np.zeros(len(Z) + (len(Z)-1)*(num_of_zero))
print(result)
result[::num_of_zero+1] = Z
print(result)
