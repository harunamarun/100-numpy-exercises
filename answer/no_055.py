import numpy as np
# 55. What is the equivalent of enumerate for numpy arrays? (★★☆)
print(np.__file__)
Z = np.arange(9).reshape(3,3)
print(Z)

for i, value in np.ndenumerate(Z):
    print(i,value)


# for index in np.ndindex(Z.shape):
#     print(index, Z[index])