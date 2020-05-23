import numpy as np
# 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
Z = np.random.rand(10)
Z[Z.argmax()] = 0
print(Z)