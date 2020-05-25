import numpy as np
# 53. How to convert a float (32 bits) array into an integer (32 bits) in place?

Z = ((100-1)*np.random.rand(10,10) + 1).astype(np.float32)
Z = Z.astype(np.int32)
print(Z)

# Y = Z.view(np.int32)
# Y[:] = Z
# print(Y)
