import numpy as np
# 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)

X = [2,3,4]
I = [1,1,9]
F = np.bincount(I,X)
print(F)