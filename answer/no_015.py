import numpy as np
# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
Z = np.ones((5, 5))
Z[1:-1, 1:-1] = 0
print(Z)
