import numpy as np
# 49. How to print all the values of an array? (★★☆)
print(np.get_printoptions())
np.set_printoptions(threshold=np.inf)
Z = np.ones((50,50))
print(Z)