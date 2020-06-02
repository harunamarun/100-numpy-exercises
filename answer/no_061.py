import numpy as np
# 61. Find the nearest value from a given value in an array (★★☆)
Z = np.random.rand(3,3)
Z = Z.flatten()
z = 0.5
Zabs = np.abs(Z-z)
print(Z[Zabs.argmin()])

# m = Z.flat[np.abs(Z - z).argmin()]
# print(m)