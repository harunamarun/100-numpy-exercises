import numpy as np
# 60. How to tell if a given 2D array has null columns? (★★☆)

Z = np.ones((3,3))
Z[1,1] = np.nan

print(Z)
print(~np.isnan(Z).any(axis=0).any())

# Z = np.random.randint(0,3,(3,10))
# print((~Z.any(axis=0)).any())