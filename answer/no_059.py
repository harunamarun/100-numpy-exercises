import numpy as np
# 59. How to sort an array by the nth column? (★★☆)
Z = np.random.randint(0,10,(3,3))
print(Z)

index = Z[:,0].argsort()
print(Z[index])
