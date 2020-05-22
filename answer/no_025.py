import numpy as np
# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
Z = np.random.randint(0, 10, 10)
print(Z)
print(np.where((Z >= 3) & (Z <= 8),-Z,Z))

# Z[(3 < Z) & (Z <= 8)] *= -1
# print(Z)